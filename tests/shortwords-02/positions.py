"""Short-word rebuild, step 1: which short words can stand in the same position, and which stand next
to each other (author's rule 1, 2026-10-13: positions by real co-occurrence, not build.py's groups).

Frames: every reference example sentence (spec.py examples, as gf_check.py reads them) and every UDHR
sentence (examples/01-udhr.md) of at most MAXLEN tokens that the formal grammar parses.

  substitution  in each frame, each short word (grammar word or digit 0-5) and each two-syllable operator
                is replaced in turn by every short word; the new sentence is parsed with the GF grammar
                (grammar/Apupiwe.pgf). If it still parses, the two words can stand in the same position
                there: a listener who mishears one as the other gets a grammatical sentence. Recorded
                twice: any parse, and a parse that isn't only a fragment reading (FragNP/FragAdv/FragAP)
                when the original sentence had a full reading.
  adjacency     short word + short word bigrams (no pause between) in the same corpus, all sentences,
                parsed or not, with counts.

Output (this folder): frames.txt, substitution.tsv (A, B, contexts of A, B fits any, B fits as a full
sentence), adjacency.tsv (A, B, count), corpus-counts.tsv (short-word token counts).
Slow part: about 50k GF parses, run in parallel; results cached in substitution.tsv.

  direnv exec . python3 tests/shortwords-02/positions.py
"""
import collections, csv, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import gf_check as G
import spec as SPEC

MAXLEN = 16
OPERATORS = "genso wanme inwun wemen konsin nedin tason mesun manni buntu buni donon lanno anko nuwen kiyo mena".split()


def read(name):
    with open(os.path.join(ROOT, "data", name)) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


GRAM = read("grammar.tsv")
DIGITS = [r for r in read("numbers.tsv") if r["kind"] == "digit" and len(r["form"]) <= 3 and r["form"] not in ("ufo", "oma")]
SHORT = {g["form"]: g["gloss"] for g in GRAM}
SHORT.update({d["form"]: f"D{d['value']}" for d in DIGITS})


def udhr_sentences():
    text = open(os.path.join(ROOT, "examples", "01-udhr.md")).read()
    paras = re.findall(r"\n([^\n#>{][^\n]*)\n\{\.apu\}", text)
    out = []
    for p in paras:
        for s in re.split(r"(?<=[.?!])\s+", p.strip()):
            s = s.strip().rstrip(".?!").strip().lower()
            if s:
                out.append(" ".join(G.tokens(s)))
    return out


def reference_sentences():
    out = []
    for rid, apu, eng in SPEC.examples(SPEC.load()):
        if rid in G.OUTSIDE or apu in G.OUTSIDE_SENT:
            continue
        out += G.sentences(apu)
    return [x.replace('"', "").strip() for x in out]   # a quote mark makes GF reject the command


def parse_many(sents, workers=12):
    """For each sentence: (parses?, has a non-fragment tree?)."""
    chunks = [list(range(i, len(sents), workers)) for i in range(workers)]

    def run(ix):
        cmds = "".join(f'ps "@@@ {i}"\np -lang=ApupiweApu "{sents[i]}"\n' for i in ix)
        r = subprocess.run(["gf", "--run", G.PGF], input=cmds, capture_output=True, text=True, timeout=36000)
        res, cur = {}, None
        for line in r.stdout.splitlines():
            if line.startswith("@@@ "):
                cur = int(line.split()[1]); res[cur] = [False, False]
            elif cur is None or not line.strip():
                continue
            elif not line.startswith("MkUtt"):   # errors, including "command not parsed" (fixed 2026-10-15, tests/deletion-01)
                pass
            else:
                res[cur][0] = True
                if not re.search(r"\bFrag(NP|Adv|AP)\b", line):
                    res[cur][1] = True
        return res

    out = {}
    with ThreadPoolExecutor(workers) as ex:
        for res in ex.map(run, chunks):
            out.update(res)
    return [tuple(out.get(i, (False, False))) for i in range(len(sents))]


def main():
    G.build()
    ref, udhr = reference_sentences(), udhr_sentences()
    corpus = ref + udhr
    # adjacency and token counts over the whole corpus (pauses break adjacency)
    adj, uni = collections.Counter(), collections.Counter()
    for s in corpus:
        toks = s.replace(",", " , ").split()
        for a, b in zip(toks, toks[1:]):
            if a in SHORT and b in SHORT:
                adj[a, b] += 1
        for t in toks:
            if t in SHORT or t in OPERATORS:
                uni[t] += 1
    with open(os.path.join(HERE, "adjacency.tsv"), "w") as fh:
        fh.write("A\tB\tglossA\tglossB\tcount\n")
        for (a, b), n in adj.most_common():
            fh.write(f"{a}\t{b}\t{SHORT[a]}\t{SHORT[b]}\t{n}\n")
    with open(os.path.join(HERE, "corpus-counts.tsv"), "w") as fh:
        fh.write("form\tgloss\ttokens\n")
        for t in list(SHORT) + OPERATORS:
            fh.write(f"{t}\t{SHORT.get(t, 'operator')}\t{uni[t]}\n")

    cand = [s for s in dict.fromkeys(ref + [u for u in udhr if len(u.split()) <= MAXLEN])]
    ok = parse_many(cand)
    frames = [(s, full) for s, (p, full) in zip(cand, ok) if p]
    with open(os.path.join(HERE, "frames.txt"), "w") as fh:
        fh.write(f"# {len(frames)} frames that parse (of {len(cand)}: {len(ref)} reference sentences, "
                 f"{len(udhr)} UDHR sentences, UDHR kept if <= {MAXLEN} tokens)\n")
        for s, full in frames:
            fh.write(s + "\n")
    jobs, meta = [], []
    for fi, (s, full) in enumerate(frames):
        toks = s.split()
        for i, t in enumerate(toks):
            if t not in SHORT and t not in OPERATORS:
                continue
            for b in SHORT:
                if b == t:
                    continue
                jobs.append(" ".join(toks[:i] + [b] + toks[i + 1:]))
                meta.append((t, b, full, fi, i))
    print(f"{len(frames)} frames, {len(jobs)} substitutions", flush=True)
    res = parse_many(jobs, workers=14)
    ctx = collections.Counter()           # contexts (frame, position) of A
    fit_any, fit_full = collections.Counter(), collections.Counter()
    seen = set()
    for (t, b, full, fi, i), (p, nonfrag) in zip(meta, res):
        if (fi, i) not in seen:
            seen.add((fi, i)); ctx[t] += 1
        if p:
            fit_any[t, b] += 1
            if nonfrag or not full:
                fit_full[t, b] += 1
    with open(os.path.join(HERE, "substitution.tsv"), "w") as fh:
        fh.write("A\tB\tglossA\tglossB\tcontexts_A\tfits_any\tfits_full\n")
        for t in list(SHORT) + OPERATORS:
            for b in SHORT:
                if b != t and ctx[t]:
                    fh.write(f"{t}\t{b}\t{SHORT.get(t, 'operator')}\t{SHORT[b]}\t{ctx[t]}\t{fit_any[t, b]}\t{fit_full[t, b]}\n")
    print("done")


if __name__ == "__main__" and len(sys.argv) == 1:
    main()


# ---- MODMOD: not in the grammar yet. It stands between a content modifier and the next content word
# (design log 2026-10-13: demi wiwi MODMOD buda "a dark-red cloth"). A short word shares its position if it
# can stand there in these frames (each parses without it).
MODMOD_FRAMES = ["to ibe demi wiwi X buda", "demi wiwi X buda gun upe", "wan nagu demi wiwi X buda tan",
                 "to momu guyi kudu X upe", "me sin yidu demi wiwi X buda mon guyi"]


def modmod():
    G.build()
    base = parse_many([f.replace(" X", "") for f in MODMOD_FRAMES], workers=5)
    assert all(p for p, _ in base), base
    jobs = [(f, b) for f in MODMOD_FRAMES for b in SHORT]
    res = parse_many([f.replace("X", b) for f, b in jobs], workers=12)
    fits = collections.Counter()
    for (f, b), (p, full) in zip(jobs, res):
        fits[b] += bool(full)
    with open(os.path.join(HERE, "modmod.tsv"), "w") as fh:
        fh.write(f"# {len(MODMOD_FRAMES)} frames: {' | '.join(MODMOD_FRAMES)}\nform\tgloss\tfits\n")
        for b in SHORT:
            fh.write(f"{b}\t{SHORT[b]}\t{fits[b]}\n")
    print("MODMOD shares a position with:", " ".join(f"{b}({fits[b]})" for b in SHORT if fits[b]))


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "modmod":
    modmod()


# ---- operators that no parsed frame contains (the reference cites them as words): frames from their rules
OP_FRAMES = {"wanme": ["wanme wan obu", "so wanme wan sin isi"], "inwun": ["inwun wan obu", "inwun to sin nawi"],
             "wemen": ["wemen wan obu", "kon da wemen wan sin isi"], "buni": ["so pen isi , buni"],
             "donon": ["wan gun no ibe guyi , donon"]}


def operators():
    G.build()
    frames = [(o, f) for o, fs in OP_FRAMES.items() for f in fs]
    base = parse_many([f for _, f in frames], workers=8)
    assert all(p for p, _ in base), list(zip(frames, base))
    jobs = [(o, f, b) for o, f in frames for b in SHORT]
    res = parse_many([" ".join(b if t == o else t for t in f.split()) for o, f, b in jobs], workers=12)
    fits = collections.Counter()
    for (o, f, b), (p, full) in zip(jobs, res):
        fits[o, b] += bool(full)
    with open(os.path.join(HERE, "operators-extra.tsv"), "w") as fh:
        fh.write("A\tB\tglossA\tglossB\tcontexts_A\tfits_any\tfits_full\n")
        for o, fs in OP_FRAMES.items():
            for b in SHORT:
                fh.write(f"{o}\t{b}\toperator\t{SHORT[b]}\t{len(fs)}\t{fits[o, b]}\t{fits[o, b]}\n")
    for o in OP_FRAMES:
        print(o, [b for b in SHORT if fits[o, b]])


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "operators":
    operators()

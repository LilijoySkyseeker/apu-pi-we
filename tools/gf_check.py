"""Parse every reference example with the GF grammar (formal-grammar.md checks 2 and 3).

For each example (from spec.py examples): does it parse; how many structural readings (differing in
attachment or clause boundaries) and how many readings in all (the rest differ only in a bare root's
role: thing, event or quality); is the intended reading among them; and the English of the intended
reading, bracketed, next to the reference gloss.

A reading's structure is the set of units it builds, read from GF's bracketed Apupiwe linearization:
  S    a clause (Cl0)                          REL  a relative clause
  ADV  a relation phrase, linked clause or manner phrase
  NP   a noun phrase                           AP   a quality phrase
counting only units of two or more words: a one-word unit is a bare root in some role. Two readings
with the same units differ only in the roles of bare roots. grammar/intended.tsv holds the
intended structure of each sentence in this bracket notation, e.g.
  to sin miya ewo man sigo kiyo nin leso   [S to sin miya [NP ewo [REL man sigo]] kiyo [ADV nin leso]]
and whether the reference presents it as the precise form (then it must have one structural reading).

Examples that aren't sentences: 2.10 (mm, huh?) is outside the grammar; an example made only of grammar
or number words that doesn't parse is a word citation, checked against the word lists. "…" and a
trailing pause stand for the rest of a sentence and are filled with FILLER. A name's words are joined
into one token (tokens()), since a name runs to the next grammar word or pause (11.1).

  python tools/gf_check.py              # every example; exit 1 if one fails to parse or misses its reading
  python tools/gf_check.py -v           # also list every structural reading
  python tools/gf_check.py "to o unfu"  # one sentence: its structural readings and English
Run inside the dev shell (direnv exec . python3 tools/gf_check.py); it builds grammar/Apupiwe.pgf if stale.
"""
import csv, os, re, subprocess, sys, collections

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(TOOLS, "..")
G = os.path.join(ROOT, "grammar")
PGF = os.path.join(G, "Apupiwe.pgf")
sys.path.insert(0, TOOLS)
import spec as SPEC

FILLER = "wan obu"          # "she comes": stands in for "…"
OUTSIDE = {"2.10"}          # interjections carry no grammar (2.10)
# Single examples outside the reference grammar on purpose: words not in the lexicon (11.1, 11.3)
OUTSIDE_SENT = {"mara sin obu": "casual speech: a name without en (11.1)",
                "to nawi sushi sa": "a speaker's borrowing, not in the lexicon (11.3)",
                "to sin google bu": "a speaker's borrowing used as a verb (11.3)"}
UNIT = {"Cl0": "S", "Rel": "REL", "Adv": "ADV", "Manner": "ADV",
        "NP": "NP", "NPi": "NP", "NPq": "NP", "CN": "NP", "AP": "AP"}
ORDER = ["S", "NP", "AP", "REL", "ADV"]
VERBISH = {"action", "motion", "sense", "mind"}
ADJISH = {"quality", "size", "color", "taste"}


def read(path):
    with open(path) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


LEX = {r["form"]: r for r in read(os.path.join(ROOT, "data", "lexicon.tsv"))}
GRAMMAR_WORDS = ({r["form"] for r in read(os.path.join(ROOT, "data", "grammar.tsv"))}
                 | {r["form"] for r in read(os.path.join(ROOT, "data", "numbers.tsv"))}
                 | set("genso wanme inwun wemen konsin nedin tason mesun manni buntu buni donon lanno anko nuwen kiyo mena".split())
                 | {w for w, r in LEX.items() if r["field"] == "number"})


def build():
    """Rebuild the PGF when a grammar source is newer (the lexicon comes from tools/gf_lexicon.py)."""
    srcs = [os.path.join(G, f) for f in os.listdir(G) if f.endswith(".gf")]
    if os.path.exists(PGF) and all(os.path.getmtime(s) <= os.path.getmtime(PGF) for s in srcs):
        return
    conc = [c for c in ("ApupiweApu.gf", "ApupiweEng.gf") if os.path.exists(os.path.join(G, c))]
    r = subprocess.run(["gf", "-make", "-s"] + conc, cwd=G, capture_output=True, text=True)
    if r.returncode or not os.path.exists(PGF):
        sys.exit("gf_check: grammar doesn't compile:\n" + r.stdout + r.stderr)


def gf(cmds):
    r = subprocess.run(["gf", "--run", PGF], input=cmds, capture_output=True, text=True, timeout=1800)
    return r.stdout


def tokens(sentence):
    """Words and pauses. A name runs from en to the next grammar word or pause (11.1), so its words
    are joined into one token for the grammar's String: en xi jinping sin oyi -> en xi_jinping sin oyi."""
    out = []
    for w in sentence.replace(",", " , ").split():
        if len(out) >= 2 and out[-2] == "en" and w != "," and w not in GRAMMAR_WORDS:
            out[-1] += "_" + w
        else:
            out.append(w)
    return out


def sentences(apu):
    """The sentences of an example, lowercased, "…" filled, final marks dropped."""
    t = apu.lower().replace("*", "")
    out = []
    for s in re.split(r"(?<=[.?!])\s+", t.strip()):
        s = s.strip().rstrip(".?!").strip()
        if not s:
            continue
        s = s.replace("…", FILLER)
        if s.endswith(","):
            s = s + " " + FILLER
        out.append(" ".join(tokens(s)))
    return out


# ---- reading structure ---------------------------------------------------------------------

def nodes(bracketed):
    """Words and nodes (category, id, start, end) of GF's bracketed linearization. GF writes
    "(Cat:id word word)", with closers attached to the last word; a discontinuous node repeats its id."""
    words, stack, found = [], [], []
    for tok in bracketed.split():
        if re.fullmatch(r"\(\w+:\d+", tok):
            cat, nid = tok[1:].split(":")
            stack.append((cat, nid, len(words)))
            continue
        m = re.fullmatch(r"(.*?)(\)*)", tok)
        if m.group(1):
            words.append(m.group(1))
        for _ in m.group(2):
            cat, nid, s = stack.pop()
            found.append((cat, nid, s, len(words)))
    # merge the pieces of a discontinuous node; keep it only if the pieces are contiguous
    merged = {}
    for cat, nid, s, e in found:
        c, a, b, n = merged.get(nid, (cat, s, e, 0))
        merged[nid] = (cat, min(a, s), max(b, e), n + e - s)
    return words, [(c, a, b) for c, a, b, n in merged.values() if n == b - a]


def spans(bracketed):
    """(label, start, end) units of a reading, and its words."""
    words, ns = nodes(bracketed)
    units = {(UNIT[c], a, b) for c, a, b in ns if c in UNIT and b - a >= 2}
    return frozenset(units), words


def render(units, words):
    """Bracket notation of a set of units over the words."""
    opens, closes = collections.defaultdict(list), collections.Counter()
    for lab, s, e in sorted(units, key=lambda u: (u[1], -u[2], ORDER.index(u[0]))):
        opens[s].append(lab)
        closes[e] += 1
    out = []
    for i, w in enumerate(words + [""]):
        out += ["]"] * closes[i]
        if i < len(words):
            out += ["[" + lab for lab in opens[i]]
            out.append(w)
    return re.sub(r"\[(\w+) ", r"[\1 ", " ".join(out)).replace(" ]", "]")


def parse_notation(text):
    """The units of a bracket-notation string, and its words."""
    units, stack, words = set(), [], []
    for t in re.findall(r"\[\w+|\]|[^\s\[\]]+", text):
        if t.startswith("["):
            stack.append((t[1:], len(words)))
        elif t == "]":
            lab, s = stack.pop()
            units.add((lab, s, len(words)))
        else:
            words.append(t)
    return frozenset(units), words


def role_fit(tree):
    """How well a tree's roles match each root's usual kind: picks a natural tree to show in English."""
    score = 0
    for w, r in re.findall(r"\b([a-z]+)_([NVA])\b", tree):
        f = LEX.get(w, {}).get("field", "")
        usual = "V" if f in VERBISH else "A" if f in ADJISH else "N"
        score += r == usual
    return score - 0.01 * tree.count("(")


# ---- English -------------------------------------------------------------------------------

ENG_UNIT = {"Rel": 2, "Adv": 2, "Manner": 2, "NP": 3, "NPi": 3}   # unit: fewest words to bracket


def english_brackets(bracketed):
    """Plain English with [ ] around noun phrases of two or more words, relation phrases and relative clauses."""
    words, ns = nodes(bracketed)
    spans = sorted({(a, b) for c, a, b in ns if c in ENG_UNIT and b - a >= ENG_UNIT[c] and (a, b) != (0, len(words))},
                   key=lambda x: (x[0], -x[1]))
    keep = []
    for a, b in spans:  # drop spans that cross one already kept
        if all(b <= x or a >= y or (x <= a and b <= y) or (a <= x and y <= b) for x, y in keep):
            keep.append((a, b))
    opens, closes = collections.Counter(a for a, _ in keep), collections.Counter(b for _, b in keep)
    out = []
    for i, w in enumerate(words + [""]):
        out.append("]" * closes[i])
        if i < len(words):
            out.append("[" * opens[i] + w)
    return re.sub(r"\s+", " ", " ".join(out)).replace(" ]", "]").replace(" &+ ", "").strip()


# ---- the check -----------------------------------------------------------------------------

def parse_all(sents):
    """Trees per sentence, then structural units and English per tree, in two GF runs."""
    cmds = "".join(f'ps "@@@ {i}"\np -lang=ApupiweApu "{s}"\n' for i, s in enumerate(sents))
    out = gf(cmds)
    trees, cur, fails = collections.defaultdict(list), None, {}
    for line in out.splitlines():
        if line.startswith("@@@ "):
            cur = int(line.split()[1])
        elif cur is None or not line.strip():
            continue
        elif line.startswith(("The parser failed", "Unknown words", "The sentence is not complete")):
            fails[cur] = line.strip()
        else:
            trees[cur].append(line.strip())
    flat = [(i, t) for i in range(len(sents)) for t in trees.get(i, [])]
    cmds = "".join(f'ps "@@@"\nl -lang=ApupiweApu -bracket {t}\nl -lang=ApupiweEng -bracket -bind {t}\n' for _, t in flat)
    out = gf(cmds).split("@@@")[1:]
    info = collections.defaultdict(list)
    for (i, t), chunk in zip(flat, out):
        lines = [l for l in chunk.strip().splitlines() if l.strip()]
        units, words = spans(lines[0])
        eng = english_brackets(lines[1]) if len(lines) > 1 else "?"
        info[i].append({"tree": t, "units": units, "words": words, "english": eng})
    return info, fails


def readings(parses, sentence=None):
    """Structural readings: groups of trees with the same units, each with its most natural tree."""
    groups = collections.defaultdict(list)
    for p in parses:
        groups[p["units"]].append(p)
    out = []
    for units, ps in groups.items():
        best = max(ps, key=lambda p: role_fit(p["tree"]))
        words = sentence.split() if sentence and len(sentence.split()) == len(best["words"]) else best["words"]
        out.append({"units": units, "trees": len(ps), "best": best, "notation": render(units, words)})
    return sorted(out, key=lambda r: r["notation"])


def load_intended():
    path = os.path.join(G, "intended.tsv")
    if not os.path.exists(path):
        return {}
    want = collections.defaultdict(list)
    for r in read(path):
        want[r["sentence"]].append(r)
    return want


def main(argv):
    build()
    verbose = "-v" in argv
    args = [a for a in argv if not a.startswith("-")]
    if args:
        sents = [" ".join(tokens(a)) for a in args]
        info, fails = parse_all(sents)
        for i, s in enumerate(sents):
            print(f"{s}: {len(info.get(i, []))} readings" + (f"  FAIL {fails[i]}" if i in fails else ""))
            for r in readings(info.get(i, []), s):
                print(f"  {r['notation']}   ({r['trees']} trees)\n      {r['best']['english']}\n      {r['best']['tree']}")
        return 0

    spec = SPEC.load()
    examples = list(SPEC.examples(spec))
    want = load_intended()
    jobs, rows = [], []
    for rid, apu, eng in examples:
        if rid in OUTSIDE or apu in OUTSIDE_SENT:
            rows.append((rid, apu, eng, "outside", []))
            continue
        ss = sentences(apu)
        rows.append((rid, apu, eng, "sentence", [(len(jobs) + k, s) for k, s in enumerate(ss)]))
        jobs += ss
    info, fails = parse_all(jobs)

    tally = collections.Counter()
    bad = []
    for rid, apu, eng, kind, items in rows:
        if kind == "outside":
            why = OUTSIDE_SENT.get(apu, "interjection, outside the grammar (2.10)")
            print(f"{rid:7} OUTSIDE  {apu}  ({eng}): {why}")
            tally["outside"] += 1
            continue
        lines, ok_parse, ok_int, ok_one, precise = [], True, True, True, False
        for idx, s in items:
            rs = readings(info.get(idx, []), s)
            if not rs:
                ok_parse = False
                lines.append(f"    {s}: NO PARSE ({fails.get(idx, '')})")
                continue
            intended = want.get(s, [])
            got = {r["units"]: r for r in rs}
            marks = []
            for w in intended:
                u, _ = parse_notation(w["intended"])
                hit = got.get(u)
                if hit is None:
                    ok_int = False
                    marks.append(f"    MISSING intended: {w['intended']}")
                else:
                    marks.append(f"    intended: {w['intended']}\n      English: {hit['best']['english']}")
                if w.get("precise") == "yes":
                    precise = True
                    if len(rs) != 1:
                        ok_one = False
            if not intended:
                marks.append("    (no intended reading recorded)")
            ntrees = sum(r["trees"] for r in rs)
            lines.append(f"    {s}: {len(rs)} structural, {ntrees} readings")
            lines += marks
            if verbose or not intended or (precise and len(rs) != 1):
                lines += [f"      | {r['notation']}  ({r['trees']})  {r['best']['english']}" for r in rs]
        if not ok_parse:
            words = [t for _, s in items for t in s.split()]
            if all(t in GRAMMAR_WORDS for t in words):
                print(f"{rid:7} CITE     {apu}  ({eng}): grammar-word citation, in the word lists")
                tally["citation"] += 1
                continue
        status = "ok" if ok_parse and ok_int and ok_one else "FAIL"
        if not ok_parse:
            tally["no parse"] += 1
        else:
            tally["parse"] += 1
            has_int = all(want.get(s) for _, s in items)
            if has_int and ok_int:
                tally["intended present"] += 1
            elif has_int:
                tally["intended missing"] += 1
            else:
                tally["no intended recorded"] += 1
            if precise:
                tally["precise"] += 1
                tally["precise, 1 structural" if ok_one else "precise, >1 structural"] += 1
        if status == "FAIL" or not (ok_parse and all(want.get(s) for _, s in items)):
            bad.append(rid)
        print(f"{rid:7} {status:8} {apu}  ({eng})")
        print("\n".join(lines))
    print("\nSUMMARY", dict(tally))
    print(f"{len(examples)} examples")
    failed = tally["no parse"] + tally["intended missing"] + tally["precise, >1 structural"] + tally["no intended recorded"]
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

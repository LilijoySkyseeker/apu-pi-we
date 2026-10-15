"""Deletion audit (design log 2026-10-15; research/notes/unknown-unknowns.md items 5, 11, 14).

When one short grammar word (or a digit 0-5) is lost to noise, does the rest stop making sense (the listener
notices and repairs), or does a normal sentence with another meaning remain?

Frames: the shortwords-02 frames (reference examples + UDHR sentences <= 16 tokens that the GF grammar
parses; positions.py) plus the casual texts of tests/coverage-01 (talk and chat, part2b/ap-base, texts
01-10 and 21-28) where a sentence parses. Each short-word token is deleted in turn and the remainder parsed:
  detectable    no parse
  weak          parses only as a fragment (FragNP/FragAdv/FragAP) where the original had a full reading
  undetectable  parses as a full sentence (or as a fragment, if the original was a fragment)
"strained" (added): every full reading of the remainder puts more roots in an unusual role (a thing-word
as a verb, etc.) than the original's most natural reading did. Reported beside the plain GF result.
Meaning of an undetectable loss: a rule by the word's class and its neighbours (meaning()), checked by hand
on a sample (sample.txt).

  direnv exec . python3 tests/deletion-01/deletion.py          # parse (cached in cache.json) and write
Output here: frames.tsv, deletion.tsv, words.tsv, positions.tsv, sample.txt.
"""
import collections, csv, glob, json, os, random, re, subprocess, sys
sys.dont_write_bytecode = True   # importing positions.py must not write into tests/shortwords-02
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.insert(0, os.path.join(ROOT, "tests", "shortwords-02"))
import gf_check as G
import positions as P

SHORT = P.SHORT                      # grammar.tsv forms + digits 0-5 -> gloss
FREQ = {g["form"]: float(g["freq"]) for g in P.GRAM}
FREQ.update({d["form"]: 4.0 for d in P.DIGITS})   # digits 4.0 as shortwords-02 (inherited, no recorded source)
CLASS = {g["form"]: g["class"] for g in P.GRAM}
CLASS.update({d["form"]: "digit" for d in P.DIGITS})
CASUAL = [f"{i:02d}" for i in list(range(1, 11)) + list(range(21, 29))]   # talk 01-05, 21-24; chat 06-10, 25-28
PRON = set("to me pen din wan yi sun bu go nen".split())
ACTS = set("min so tin fon de yo ba".split())
RELS = set("pi mon tun se gan li ya wo fu nin gi anko nuwen".split())


# ---- frames ------------------------------------------------------------------------------------

def casual_sentences():
    out = []
    for name in CASUAL:
        path = os.path.join(ROOT, "tests", "coverage-01", "part2b", "ap-base", name + ".txt")
        for line in open(path):
            line = line.strip()
            if not re.search(r"[.?!]$", line):      # titles and headings have no final mark
                continue
            line = re.sub(r"^[^\s:]+(\s[^\s:]+)?:\s+", "", line)   # speaker label
            for s in re.split(r"(?<=[.?!])\s+", line):
                s = s.strip().rstrip(".?!").strip().lower()
                if not s or re.search(r'[^a-z ,\'-]', s) or "lol" in s.split():
                    continue                         # quotes, brackets, digits, clock times, emoticons
                out.append((name, " ".join(G.tokens(s))))
    return out


# ---- parsing ------------------------------------------------------------------------------------

def gf_parse(sents, workers=14):
    """Trees per sentence (list of tree strings; empty = no parse)."""
    if not sents:
        return []
    chunks = [list(range(i, len(sents), workers)) for i in range(workers)]

    def run(ix):
        cmds = "".join(f'ps "@@@ {i}"\np -lang=ApupiweApu "{sents[i]}"\n' for i in ix)
        r = subprocess.run(["gf", "--run", G.PGF], input=cmds, capture_output=True, text=True, timeout=36000)
        res, cur = {}, None
        for line in r.stdout.splitlines():
            if line.startswith("@@@ "):
                cur = int(line.split()[1]); res[cur] = []
            elif cur is None or not line.strip():
                continue
            elif line.startswith("MkUtt"):   # anything else is an error ("command not parsed" too)
                res[cur].append(line.strip())
        return res

    out = {}
    with ThreadPoolExecutor(workers) as ex:
        for res in ex.map(run, chunks):
            out.update(res)
    return [out.get(i, []) for i in range(len(sents))]


def gf_english(trees, workers=14):
    if not trees:
        return []
    chunks = [list(range(i, len(trees), workers)) for i in range(workers)]

    def run(ix):
        cmds = "".join(f'ps "@@@ {i}"\nl -lang=ApupiweEng -bind {trees[i]}\n' for i in ix)
        r = subprocess.run(["gf", "--run", G.PGF], input=cmds, capture_output=True, text=True, timeout=36000)
        res, cur = {}, None
        for line in r.stdout.splitlines():
            if line.startswith("@@@ "):
                cur = int(line.split()[1]); res[cur] = ""
            elif cur is not None and line.strip() and not res[cur]:
                res[cur] = line.strip()
        return res

    out = {}
    with ThreadPoolExecutor(workers) as ex:
        for res in ex.map(run, chunks):
            out.update(res)
    return [out.get(i, "") for i in range(len(trees))]


FRAG = re.compile(r"\bFrag(NP|Adv|AP)\b")


def odd(tree):
    """Roots in an unusual role (a thing-word as a verb, an action word as a quality ...)."""
    n = 0
    for w, r in re.findall(r"\b([a-z]+)_([NVA])\b", tree):
        f = G.LEX.get(w, {}).get("field", "")
        usual = "V" if f in G.VERBISH else "A" if f in G.ADJISH else "N"
        n += r != usual
    return n


def summary(trees):
    """(parses, has a full reading, fewest odd roles among full readings (or among all), best tree)."""
    if not trees:
        return False, False, None, ""
    full = [t for t in trees if not FRAG.search(t)]
    pool = full or trees
    best = max(pool, key=G.role_fit)
    return True, bool(full), min(odd(t) for t in pool), best


# ---- meaning of an undetectable loss (rule by class, with context) --------------------------------

def meaning(toks, i):
    """(label, dimension, note): label is changed / unspecified / barely."""
    w = toks[i]
    prev = toks[i - 1] if i else ""
    nxt = toks[i + 1] if i + 1 < len(toks) else ""
    if prev == w or nxt == w:
        return "barely", "", "doubled: the other copy carries it"
    if w == "en":
        return "barely", "", "a name without en (casual form, 11.1)"
    if w == "mu":
        if "fa" in toks[i + 1:]:
            return "barely", "", "fa still negates (6.2.2)"
        if prev == "le":
            return "changed", "polarity", "le mu 'not yet' -> le 'still'"
        return "changed", "polarity", ""
    if w == "fa":
        if "mu" in toks[:i]:
            return "barely", "", "mu still negates"
        return "changed", "polarity", "none -> bare noun"
    if w == "min":
        if func(toks, i) == "min (tag)":
            return "changed", "stance", "end tag 'right?' lost"
        if prev == "wun":
            return "changed", "speech act", "indirect question 'whether' -> 'that'"
        return "changed", "speech act", "question -> statement"
    if w in ("so", "tin", "fon", "de", "yo"):
        return "changed", "speech act", {"so": "request -> statement", "tin": "instruction -> statement",
                                         "fon": "advice -> statement", "de": "commitment -> statement",
                                         "yo": "warning -> statement"}[w]
    if w == "ba":
        return "changed", "emphasis", "exclamation -> statement"
    if w == "yu":
        return "changed", "speech act", "question word lost: question -> statement"
    if w == "nun":
        return "barely", "", "politeness only"
    if w == "a":
        return "barely", "", "stance 'you know'"
    if w == "kon":
        return "changed", "confidence", ""
    if w in ("bo",):
        return "barely", "", "'someone/something' -> bare noun (no articles)"
    if w == "la":
        if prev in PRON:
            return "changed", "reference", f"{prev} la -> {prev} (plural pronoun -> singular)"
        return "barely", "", "plural is optional (5.2.6)"
    if w in ("tan", "ben"):
        if prev == "gi":
            return "changed", "connective", "gi tan 'so' -> gi"
        if prev and prev not in SHORT and prev not in (",",):
            return "barely", "", "determiner after a noun; context"
        return "unspecified", "reference", "pronoun 'this/that' dropped"
    if w in ("we", "in", "kin"):
        return "changed", "quantity", ""
    if w in ("sin", "le", "buntu"):
        return "changed", "tense/aspect", ""
    if w == "nen":
        if prev in PRON or (prev and prev not in SHORT and prev != ","):
            return "barely", "", "'himself, in person' after a noun or pronoun"
        return "unspecified", "reference", "reflexive object dropped"
    if w in PRON:
        return "unspecified", "reference", "pronoun dropped (4.5); context may restore"
    if w in ("no", "ge", "du", "pu"):
        return "changed", "reference", "derived noun -> plain root"
    if w == "en":
        return "barely", "", ""
    if w == "yen":
        if i == 0 or prev == ",":
            return "barely", "", "linker/clause 'and' after a pause"
        return "changed", "structure", "list or joined verbs -> one phrase"
    if w == "lu":
        return "changed", "structure", "alternatives -> one phrase"
    if w == "un":
        return "changed", "connective", "contrast lost"
    if w == "don":
        return "changed", "condition", "condition asserted as fact"
    if w == "wun":
        return "barely", "", "complement 'that' (hand-checked)"
    if w == "man":
        return "changed", "structure", "relative clause -> main clause / modifier"
    if w == "gun":
        return "barely", "", "copula; bare state reads as statement or description (4.2.2)"
    if w == "ke":
        return "changed", "degree", "comparison lost"
    if w == "bi":
        return "barely", "", "'very' lost"
    if w == "na":
        return "changed", "scope", "'only' lost"
    if w == "wi":
        return "changed", "scope", "'even' lost"
    if w in ("fe", "o"):
        return "barely", "", "'also' / focus lost"
    if w in RELS:
        if w == "fu" and nxt in SHORT and CLASS.get(nxt) == "digit":
            return "changed", "number", "'about' lost"
        return "changed", "role", "relation word lost"
    if CLASS.get(w) == "digit":
        return "changed", "number", ""
    return "changed", "?", ""


# Hand check (README, "Hand checks"): of the losses the class rule labels "changed", the share a reader judged
# plainly changed and still natural (the rest: barely changed, or odd enough to be noticed). Samples of 8-30.
HAND = {"rel": 0.2, "yu": 0.79, "digit": 0.43, "we": 0.5, "man": 0.13, "yen": 0.13, "deriv": 0.3,
        "lu": 0.0, "ke": 0.33, "le": 0.3, "sin": 0.9, "un": 0.0}


UNSPEC_W = 0.06   # a dropped pronoun misleads: 1 of 16 casual-text samples (hand check); the rest context restores


def hand(w):
    if w in HAND:
        return HAND[w]
    if w in RELS:                       # relation words, including gi nin ya wo as clause links
        return HAND["rel"]
    return HAND.get(CLASS.get(w), 1.0)


STAKES_HIGH = set("mu fa so tin fon de yo yu".split())
STAKES_LOW = set("ba nun a la tan ben bo bi fe o nen gun wun un yen en".split())


def stakes(toks, i):
    """3 high (negation, speech act, warning: PROMPT), 1 low (politeness, stance: PROMPT; the rest added), 2 medium."""
    w = toks[i]
    if w == "min":
        return 1 if func(toks, i) == "min (tag)" else 3
    return 3 if w in STAKES_HIGH else 1 if w in STAKES_LOW else 2


def func(toks, i):
    """Row label: min split into act / tag / indirect."""
    w = toks[i]
    if w == "min":
        if i == len(toks) - 1 and i and toks[i - 1] in (",", "a", "buni", "donon"):
            return "min (tag)"
        return "min (whether)" if i and toks[i - 1] == "wun" else "min (act)"
    return w


# ---- main ----------------------------------------------------------------------------------------

def main():
    G.build()
    cache_path = os.path.join(HERE, "cache.json")
    cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}

    def parse(sents):
        todo = [s for s in dict.fromkeys(sents) if s not in cache]
        if todo:
            print(f"parsing {len(todo)}", flush=True)
            for s, t in zip(todo, gf_parse(todo)):
                cache[s] = {"n": len(t), "sum": list(summary(t))}
            json.dump(cache, open(cache_path, "w"))
        return [cache[s] for s in sents]

    # frames: shortwords-02 (same build as positions.py) + casual texts
    # a quote mark left in a sentence makes GF reject the command; positions.py counted that as a parse
    ref = [s.replace('"', "").strip() for s in P.reference_sentences()]
    udhr = [s.replace('"', "").strip() for s in P.udhr_sentences()]
    cand = [("ref" if s in ref else "udhr", s) for s in dict.fromkeys(ref + [u for u in udhr if len(u.split()) <= P.MAXLEN])]
    cas_all = casual_sentences()
    seen = {s for _, s in cand}
    cas = [(n, s) for n, s in cas_all if len(s.split()) <= P.MAXLEN and s not in seen]
    cas = list(dict.fromkeys(cas))
    res = parse([s for _, s in cand + cas])
    frames = []
    for (src, s), r in zip(cand + cas, res):
        if r["n"]:
            frames.append((src if src in ("ref", "udhr") else "casual-" + src, s, r))
    cas_stats = collections.Counter()
    for n, s in cas_all:
        cas_stats["sentences"] += 1
        if len(s.split()) > P.MAXLEN:
            cas_stats["too long"] += 1
    cas_parsed = collections.Counter(src for src, _, _ in frames if src.startswith("casual"))
    cas_tried = collections.Counter("casual-" + n for n, _ in cas)

    # deletions
    jobs = []
    for fi, (src, s, r) in enumerate(frames):
        toks = s.split()
        for i, t in enumerate(toks):
            if t in SHORT:
                rest = toks[:i] + toks[i + 1:]
                rest = [x for k, x in enumerate(rest) if not (x == "," and (k == 0 or k == len(rest) - 1))]
                if not rest:
                    continue
                jobs.append((fi, i, " ".join(rest)))
    dres = parse([j[2] for j in jobs])

    # English of the original's and the remainder's most natural reading
    eng_need = {}
    for src, s, r in frames:
        eng_need[s] = r["sum"][3]
    for (fi, i, rest), r in zip(jobs, dres):
        if r["n"]:
            eng_need[rest] = r["sum"][3]
    eng_path = os.path.join(HERE, "english.json")
    eng = json.load(open(eng_path)) if os.path.exists(eng_path) else {}
    todo = [s for s, t in eng_need.items() if t and s not in eng]
    if todo:
        print(f"linearizing {len(todo)}", flush=True)
        for s, e in zip(todo, gf_english([eng_need[s] for s in todo])):
            eng[s] = e
        json.dump(eng, open(eng_path, "w"))

    # frames.tsv: the original readings
    fsum = []
    with open(os.path.join(HERE, "frames.tsv"), "w") as fh:
        fh.write("frame\tsource\tsentence\ttrees\tfull\todd_roles\tenglish_best\n")
        for fi, (src, s, r) in enumerate(frames):
            p, full, od, best = r["sum"]
            fsum.append((full, od))
            fh.write(f"{fi}\t{src}\t{s}\t{r['n']}\t{'yes' if full else 'fragment'}\t{od}\t{eng.get(s, '')}\n")

    # deletion.tsv
    rows = []
    for (fi, i, rest), r in zip(jobs, dres):
        src, s, _ = frames[fi]
        toks = s.split()
        w = toks[i]
        ofull, ood = fsum[fi]
        p, full, od, best = r["sum"]
        if w == "en":
            cls = "undetectable"   # parser can't read a bare name (unknown token); 11.1 allows it in casual speech
            note_override = "en: parser lacks bare names; a bare name is the casual form (11.1)"
        elif not p:
            cls = "detectable"
        elif ofull and not full:
            cls = "weak"
        else:
            cls = "undetectable"
            note_override = ""
        if w != "en":
            note_override = ""
        strained = cls == "undetectable" and w != "en" and od is not None and od > ood
        lab, dim, note = meaning(toks, i) if cls == "undetectable" else ("", "", "")
        rows.append({"frame": fi, "source": src, "word": w, "function": func(toks, i), "class": CLASS[w],
                     "pos": i, "first": "yes" if i == 0 else "no", "sentence": s, "remainder": rest,
                     "result": cls, "strained": "yes" if strained else "no", "trees": r["n"],
                     "meaning": lab, "dimension": dim, "stakes": stakes(toks, i),
                     "note": "; ".join(x for x in (note, note_override) if x),
                     "english_orig": eng.get(s, ""), "english_rest": eng.get(rest, "") if p else ""})
    cols = list(rows[0])
    with open(os.path.join(HERE, "deletion.tsv"), "w") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]) for c in cols) + "\n")

    # words.tsv: per word (min split by function; digits pooled for the ranking, listed one by one after it)
    by = collections.defaultdict(list)
    for r in rows:
        by[r["function"]].append(r)
        if CLASS[r["word"]] == "digit":
            by["digit (any)"].append(r)
    out = []
    for fn, rs in by.items():
        n = len(rs)
        c = collections.Counter(r["result"] for r in rs)
        und = [r for r in rs if r["result"] == "undetectable"]
        und_strict = [r for r in und if r["strained"] == "no"]
        chg = [r for r in und if r["meaning"] == "changed"]
        uns = [r for r in und if r["meaning"] == "unspecified"]
        chg_strict = [r for r in chg if r["strained"] == "no"]
        w = rs[0]["word"]
        h = hand(w)
        st = sum(r["stakes"] for r in rs) / n
        # expected harm per token: undetectable and plainly changed (rule share x hand factor) or unspecified
        # (x UNSPEC_W), times stakes
        harm = sum(r["stakes"] * (h if r["meaning"] == "changed" else UNSPEC_W if r["meaning"] == "unspecified" else 0)
                   for r in und) / n
        out.append({"function": fn, "word": "digit" if fn == "digit (any)" else w, "class": CLASS[w],
                    "gloss": "D0-5" if fn == "digit (any)" else SHORT[w], "freq": FREQ[w], "tokens": n,
                    "detectable": c["detectable"], "weak": c["weak"], "undetectable": c["undetectable"],
                    "undet_share": round(c["undetectable"] / n, 2),
                    "undet_share_strict": round(len(und_strict) / n, 2),
                    "changed_share": round(len(chg) / n, 2),
                    "changed_share_strict": round(len(chg_strict) / n, 2),
                    "unspecified_share": round(len(uns) / n, 2),
                    "hand_factor": h, "changed_share_hand": round(len(chg) / n * h, 2),
                    "stakes": round(st, 2), "harm_per_token": round(harm, 3),
                    "score": round(FREQ[w] * harm, 3),
                    "dims": ",".join(sorted({r["dimension"] for r in chg}))})
    # freq for min split: share of min tokens in each function
    mins = [o for o in out if o["word"] == "min"]
    tot = sum(o["tokens"] for o in mins)
    for o in mins:
        o["freq"] = round(FREQ["min"] * o["tokens"] / tot, 2)
        o["score"] = round(o["freq"] * o["harm_per_token"], 3)
    out.sort(key=lambda o: -o["score"])
    cols = list(out[0])
    ranked = [o for o in out if o["class"] != "digit" or o["function"] == "digit (any)"]
    digits = [o for o in out if o["class"] == "digit" and o["function"] != "digit (any)"]
    with open(os.path.join(HERE, "words.tsv"), "w") as fh:
        fh.write("rank\t" + "\t".join(cols) + "\n")
        for k, o in enumerate(ranked, 1):
            fh.write(f"{k}\t" + "\t".join(str(o[c]) for c in cols) + "\n")
        for o in digits:
            fh.write("-\t" + "\t".join(str(o[c]) for c in cols) + "\n")
    # words with no token in the frames
    missing = [w for w in SHORT if w not in {r["word"] for r in rows}]

    # positions.tsv: speech-act particles and nun, first word or not; what precedes them
    pos = collections.defaultdict(collections.Counter)
    allsents = [s for _, s in cand] + [s for _, s in cas_all]
    for s in dict.fromkeys(allsents):
        toks = s.split()
        for i, t in enumerate(toks):
            if t in ACTS or t == "nun":
                fn = func(toks, i)
                pos[fn]["tokens"] += 1
                if i == 0:
                    pos[fn]["first"] += 1
                elif toks[i - 1] == ",":
                    pos[fn]["after pause"] += 1
                elif toks[i - 1] in ("genso", "ba"):
                    pos[fn]["after genso/ba"] += 1
                else:
                    pos[fn]["other"] += 1
                if i == len(toks) - 1:
                    pos[fn]["last"] += 1
    with open(os.path.join(HERE, "positions.tsv"), "w") as fh:
        fh.write("# all corpus sentences (reference, UDHR, casual), parsed or not\n")
        fh.write("function\ttokens\tfirst\tafter_pause\tafter_genso_ba\tother\tlast_word\n")
        for fn in sorted(pos):
            c = pos[fn]
            fh.write(f"{fn}\t{c['tokens']}\t{c['first']}\t{c['after pause']}\t{c['after genso/ba']}\t{c['other']}\t{c['last']}\n")

    # sample for hand checks: undetectable losses, stratified
    random.seed(15)
    und = [r for r in rows if r["result"] == "undetectable" and r["word"] != "en"]
    sample = random.sample(und, min(60, len(und)))
    with open(os.path.join(HERE, "sample.txt"), "w") as fh:
        for r in sorted(sample, key=lambda r: r["word"]):
            fh.write(f"[{r['word']}] {r['meaning']} {r['dimension']} strained={r['strained']} ({r['note']})\n"
                     f"   {r['sentence']}\n     = {r['english_orig']}\n   {r['remainder']}\n     = {r['english_rest']}\n\n")

    tally = collections.Counter(r["result"] for r in rows)
    print(f"frames {len(frames)} (ref/udhr {sum(1 for f in frames if not f[0].startswith('casual'))}, casual "
          f"{sum(cas_parsed.values())} of {sum(cas_tried.values())} tried; casual sentences {dict(cas_stats)})")
    print("casual parsed per text", dict(sorted(cas_parsed.items())), "tried", dict(sorted(cas_tried.items())))
    print(f"deletions {len(rows)}", dict(tally))
    print("short words with no token in the frames:", " ".join(missing))


if __name__ == "__main__":
    main()

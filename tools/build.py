"""Build the word lists from scratch under the drift-aware rules (2026-10-08).

Rules this enforces (see docs/drift.md):
- Inventory without /v/ (and optionally without /z/).
- Content words: no two words may collide after predicted drift. Later syllables blur
  e/i and o/u, middle consonants voice (p t k > b d g), a final -n melts away, and s/z merge.
- Grammar words: words that share a slot must have different first consonants; words in
  the same wider position must stay distinct after drift (onset + vowel class).
- As before: confusion weighted by meaning (antonyms > same field > other), frequent words short.

  python build.py scale            # roadmap A1: inventory comparison at ~3,000 roots
  python build.py build [--no-z]   # rebuild data/grammar.tsv, data/lexicon.tsv
  python build.py numbers3         # rebuild base-6 number words
"""
import csv, math, os, random, sys
import numpy as np
from confusion import CP, VP, CODA_MISS

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
VOWELS = "i e a o u".split()
FULL = "p t k f s b d g z m n l w j".split()  # /v/ deleted
TIER_FREQ = {5: 10, 4: 5, 3: 2.5, 2: 1.2, 1: 0.6}
EFFORT = 0.02


class Inventory:
    def __init__(self, consonants):
        self.cons = consonants
        self.onsets = [""] + consonants
        self.syl = [(o, v, c) for o in self.onsets for v in VOWELS for c in ("", "n")]
        self.name = [(o.replace("j", "y") + v + c) for o, v, c in self.syl]
        self.idx = {n: i for i, n in enumerate(self.name)}
        on = self.onsets
        C = np.array([[CP[a, b] for b in on] for a in on])
        C /= C.sum(1, keepdims=True)  # renormalize over this inventory
        V = np.array([[VP[a, b] for b in VOWELS] for a in VOWELS])
        n = len(self.syl)
        self.S = np.zeros((n, n))
        for i, (o1, v1, c1) in enumerate(self.syl):
            for j, (o2, v2, c2) in enumerate(self.syl):
                self.S[i, j] = (C[on.index(o1), on.index(o2)] * V[VOWELS.index(v1), VOWELS.index(v2)]
                                * ((1 - CODA_MISS) if c1 == c2 else CODA_MISS))
        self.later = [i for i, s in enumerate(self.syl) if s[0] != ""]  # non-initial syllables need an onset

    def length(self, form):
        return sum(1 + 0.4 * bool(self.syl[s][2]) for s in form) - 0.1 * (self.syl[form[0]][0] == "")

    def content_key(self, form):
        out = []
        for k, s in enumerate(form):
            o, v, c = self.syl[s]
            o = {"z": "s"}.get(o, o)
            if k > 0:
                o = {"p": "b", "t": "d", "k": "g"}.get(o, o)
                v = {"e": "i", "o": "u"}.get(v, v)
                c = ""
            out.append(o + v + c)
        return ".".join(out)

    def grammar_key(self, s):
        o, v, c = self.syl[s]
        return {"z": "s"}.get(o, o) + {"e": "i", "o": "u"}.get(v, v)

    def show(self, form):
        return "".join(self.name[s] for s in form)


# ---------------------------------------------------------------- content words
def optimize_content(inv, items, W, steps, seed=1, max_len=3, fixed_len=None, verbose=False):
    """items: list of (gloss, freq). W: n x n meaning weights. Returns list of forms (tuples)."""
    rng = random.Random(seed)
    n = len(items)
    freq = np.array([f for _, f in items], dtype=float)
    L = max_len
    forms = np.full((n, L), -1)
    lens = np.zeros(n, dtype=int)
    keys = {}

    def random_form():
        ln = fixed_len or (2 if rng.random() < 0.8 else 3)
        f = [rng.randrange(len(inv.syl))] + [rng.choice(inv.later) for _ in range(ln - 1)]
        return tuple(f)

    def cost(i, form):
        ln = len(form)
        mask = lens == ln
        mask[i] = False
        c = 0.0
        if mask.any():
            A = forms[mask][:, :ln]
            p_out = np.ones(A.shape[0]); p_in = np.ones(A.shape[0])
            for k in range(ln):
                p_out *= inv.S[form[k], A[:, k]]
                p_in *= inv.S[A[:, k], form[k]]
            c = (W[i, mask] * (freq[i] * p_out + freq[mask] * p_in)).sum()
        return c + EFFORT * freq[i] * (inv.length(form) - 2.0)

    for i in range(n):  # initial: random forms with unique drift keys
        while True:
            f = random_form()
            k = inv.content_key(f)
            if k not in keys:
                break
        keys[k] = i
        forms[i, :len(f)] = f
        lens[i] = len(f)
    cur = [cost(i, tuple(forms[i, :lens[i]])) for i in range(n)]
    T0 = sum(cur) / n
    for step in range(steps):
        T = T0 * (1 - step / steps) + 1e-12
        i = rng.randrange(n)
        new = random_form()
        k = inv.content_key(new)
        if k in keys:
            continue
        old = tuple(forms[i, :lens[i]])
        before = cost(i, old)
        forms[i] = -1; forms[i, :len(new)] = new; lens[i] = len(new)
        delta = cost(i, new) - before
        if delta < 0 or rng.random() < math.exp(-delta / T):
            del keys[inv.content_key(old)]
            keys[k] = i
        else:
            forms[i] = -1; forms[i, :len(old)] = old; lens[i] = len(old)
        if verbose and step % 200000 == 0:
            print(f"  step {step}", flush=True)
    out = [tuple(forms[i, :lens[i]]) for i in range(n)]
    return out


def confusion_total(inv, forms, freq, W):
    tot = 0.0
    for i, a in enumerate(forms):
        for j, b in enumerate(forms):
            if i != j and len(a) == len(b):
                tot += W[i, j] * freq[i] * math.prod(inv.S[x, y] for x, y in zip(a, b))
    return tot


# ---------------------------------------------------------------- scale check (A1)
def scale(n_roots=3000, steps=1500000):
    rng = random.Random(7)
    tiers = [5] * 60 + [4] * 240 + [3] * 700 + [2] * 1000 + [1] * 1000
    tiers = tiers[:n_roots]
    fields = [rng.randrange(40) for _ in range(n_roots)]
    items = [(f"c{i}", TIER_FREQ[t]) for i, t in enumerate(tiers)]
    W = np.where(np.equal.outer(fields, fields), 3.0, 1.0)
    for _ in range(n_roots // 20):  # 5% antonym pairs
        a, b = rng.randrange(n_roots), rng.randrange(n_roots)
        W[a, b] = W[b, a] = 30.0
    np.fill_diagonal(W, 0)
    freq = np.array([f for _, f in items])
    for name, cons in [("14 consonants (no v)", FULL),
                       ("13 consonants (no v, no z)", [c for c in FULL if c != "z"])]:
        inv = Inventory(cons)
        forms = optimize_content(inv, items, W, steps)
        lens = np.array([len(f) for f in forms])
        sylw = (lens * freq).sum() / freq.sum()
        conf = confusion_total(inv, forms, freq, W) / freq.sum()
        print(f"{name}: 3-syllable roots {np.mean(lens == 3):.1%}; "
              f"frequency-weighted syllables/root {sylw:.3f}; "
              f"confusion per word {conf:.5f}", flush=True)


# ---------------------------------------------------------------- grammar words
GROUPS_STRICT = {  # same slot: first consonant must differ
    "act": "Q REQUEST INSTRUCT ADVISE INTEND WARN EXCLAIM POLITE",
    "pred": "NOT BE DONE ONGOING MORE VERY ONLY ALSO EVEN FOCUS",
    "stance": "NOT CONF UNSPEC ONLY WH ALSO EVEN FOCUS",
    "end": "Q YOUKNOW",  # sentence-end stance position (2026-10-10)
    "pron": "I YOU WE.incl WE.excl HE/SHE OBVIATIVE LOGOPHOR GENERIC SELF",
    "det": "PLURAL THIS THAT.dem ALL SOME PART NONE WH",
    "prep": "OF AT TO FROM WITH FOR BEFORE AFTER LIKE WHILE",
    "link": "AND OR BUT IF BECAUSE THAT.comp WHO.rel WHILE",
    "deriv": "AGENT RESULT TOOL PLACE",
}
GROUPS_WIDE = {  # same wider position: must stay distinct after drift
    "start": "act link",
    "pre": "pred stance",
    "postnoun": "det prep",
    "npstart": "pron deriv",
    "finish": "end",
}


def optimize_grammar(inv, words, steps=400000, seed=3):
    """words: list of (gloss, freq). Returns {gloss: syllable index}."""
    rng = random.Random(seed)
    gl = [g for g, _ in words]
    freq = np.array([f for _, f in words])
    n = len(gl)
    strict = [[gl.index(x) for x in v.split()] for v in GROUPS_STRICT.values()]
    wide = [sorted({gl.index(x) for g in v.split() for x in GROUPS_STRICT[g].split()})
            for v in GROUPS_WIDE.values()]
    pair_strict = np.zeros((n, n), bool)
    for grp in strict:
        for a in grp:
            for b in grp:
                pair_strict[a, b] = a != b
    pair_wide = np.zeros((n, n), bool)
    for grp in wide:
        for a in grp:
            for b in grp:
                pair_wide[a, b] = a != b
    Wc = np.ones((n, n))
    Wc[pair_wide] = 3.0
    notix = gl.index("NOT")
    Wc[notix, :] = Wc[:, notix] = np.maximum(Wc[notix, :], 10.0)
    np.fill_diagonal(Wc, 0)
    onset = np.array([inv.onsets.index(s[0]) for s in inv.syl])
    gkey = [inv.grammar_key(s) for s in range(len(inv.syl))]
    gkid = {k: i for i, k in enumerate(sorted(set(gkey)))}
    gkey = np.array([gkid[k] for k in gkey])
    coda = np.array([bool(s[2]) for s in inv.syl])

    assign = np.array(rng.sample(range(len(inv.syl)), n))

    def cost(i, s):
        others = np.arange(n) != i
        A = assign[others]
        c = (Wc[i, others] * (freq[i] * inv.S[s, A] + freq[others] * inv.S[A, s])).sum()
        c += 100.0 * (pair_strict[i, others] & (onset[A] == onset[s])).sum()
        c += 30.0 * (pair_wide[i, others] & (gkey[A] == gkey[s])).sum()
        c += 2.0 * freq[i] * 0.1 * (onset[s] == 0)  # vowel-only words fuse first
        c += EFFORT * freq[i] * 0.4 * coda[s]
        return c

    T0 = 5.0
    for step in range(steps):
        T = T0 * (1 - step / steps) + 1e-9
        i = rng.randrange(n)
        if rng.random() < 0.5:
            s = rng.randrange(len(inv.syl))
            if s in assign:
                continue
            old = assign[i]
            before = cost(i, old)
            assign[i] = s
            d = cost(i, s) - before
            if not (d < 0 or rng.random() < math.exp(-d / T)):
                assign[i] = old
        else:
            j = rng.randrange(n)
            if i == j:
                continue
            a, b = assign[i], assign[j]
            before = cost(i, a) + cost(j, b)
            assign[i], assign[j] = b, a
            d = cost(i, b) + cost(j, a) - before
            if not (d < 0 or rng.random() < math.exp(-d / T)):
                assign[i], assign[j] = a, b
    violations = sum(1 for i in range(n) for j in range(i + 1, n)
                     if (pair_strict[i, j] and onset[assign[i]] == onset[assign[j]])
                     or (pair_wide[i, j] and gkey[assign[i]] == gkey[assign[j]]))
    return {gl[i]: int(assign[i]) for i in range(n)}, violations


# ---------------------------------------------------------------- full build
def read(name):
    with open(os.path.join(DATA, name)) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def write(name, rows, fields):
    with open(os.path.join(DATA, name), "w", newline="") as fh:
        w = csv.DictWriter(fh, fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def build():
    cons = [c for c in FULL if c != "z"] if "--no-z" in sys.argv else FULL
    inv = Inventory(cons)
    grammar = read("grammar.tsv")
    if not any(g["gloss"] == "POLITE" for g in grammar):
        grammar.append({"gloss": "POLITE", "class": "act", "freq": "3", "form": ""})
    words = [(g["gloss"], float(g["freq"])) for g in grammar]
    gmap, viol = optimize_grammar(inv, words)
    old_g = {g["gloss"]: g["form"] for g in grammar}
    for g in grammar:
        g["form"] = inv.name[gmap[g["gloss"]]]
    print(f"grammar words: {len(grammar)}, rule violations: {viol}")

    lex = read("lexicon.tsv")
    ants = [tuple(l.split()) for l in open(os.path.join(DATA, "antonyms.tsv")) if l.strip()]
    gl = [w["gloss"] for w in lex]
    freq_of = lambda w: 3.0 if w["field"] == "number" else TIER_FREQ[int(w["tier"])]
    items = [(w["gloss"], freq_of(w)) for w in lex]
    n = len(items)
    fields = [w["field"] for w in lex]
    W = np.ones((n, n))
    same = np.equal.outer(fields, fields)
    W[same] = 3.0
    num = np.array([f == "number" for f in fields])
    W[num, :] = 10.0; W[:, num] = 10.0
    W[np.ix_(num, num)] = 30.0
    pos = {g: i for i, g in enumerate(gl)}
    for a, b in ants:
        if a in pos and b in pos:
            W[pos[a], pos[b]] = W[pos[b], pos[a]] = 30.0
    np.fill_diagonal(W, 0)
    forms = optimize_content(inv, items, W, steps=1500000, verbose=True)
    # numbers are kept to two syllables: re-run them alone if any came out longer
    old_l = {w["gloss"]: w["form"] for w in lex}
    for w, f in zip(lex, forms):
        w["form"] = inv.show(f)
    freq = np.array([f for _, f in items])
    print(f"content words: {n}; 3-syllable: {sum(len(f) == 3 for f in forms)}; "
          f"confusion per word {confusion_total(inv, forms, freq, W) / freq.sum():.5f}")
    write("grammar.tsv", grammar, ["gloss", "class", "freq", "form"])
    write("lexicon.tsv", lex, ["gloss", "field", "tier", "form", "kind"])
    with open(os.path.join(DATA, "rename-2026-10-08.tsv"), "w") as fh:
        fh.write("kind\tgloss\told\tnew\n")
        for g in grammar:
            fh.write(f"grammar\t{g['gloss']}\t{old_g.get(g['gloss'], '')}\t{g['form']}\n")
        for w in lex:
            fh.write(f"content\t{w['gloss']}\t{old_l[w['gloss']]}\t{w['form']}\n")


# ---------------------------------------------------------------- numbers v3: base 6 (2026-10-08)
NUMBER_WORDS = ["6", "36", "216", "6^4", "6^8", "6^12", "POINT", "MINUS"]


def numbers3(seed=21):
    """Base-6 numerals. Digits 0-5: one stressed open syllable each, no other form.
    Place words 6, 36, 216, group words 6^4, 6^8, 6^12, and POINT and MINUS: two syllables.
    Digits must not equal or nearly equal grammar words that can stand next to a number, and
    a digit followed by such a grammar word (or another digit) must not sound like a content word."""
    rx = __import__("re")
    inv = Inventory([c for c in FULL if c != "z"])
    grammar = read("grammar.tsv")
    near = set(GROUPS_STRICT["det"].split() + GROUPS_STRICT["prep"].split() + GROUPS_STRICT["link"].split()
               + GROUPS_STRICT["pred"].split() + GROUPS_STRICT["pron"].split() + ["UNSPEC", "CONF", "IT"])
    gforms = {g["form"] for g in grammar}
    near_forms = [g["form"] for g in grammar if g["gloss"] in near]
    bad_keys = {inv.grammar_key(inv.idx[f]) for f in near_forms}
    lex = [w for w in read("lexicon.tsv") if w["field"] != "number"]
    split = lambda f: tuple(inv.idx[x] for x in rx.findall(r"[^aeiou]?[aeiou](?:n(?![aeiou]))?", f))
    content_keys = {inv.content_key(split(w["form"])) for w in lex}
    near_syl = [(inv.idx[g["form"]], 10.0 if g["gloss"] == "NOT" else 1.0) for g in grammar if g["gloss"] in near]
    devoice = {"b": "p", "d": "t", "g": "k"}
    dkey = lambda i: devoice.get(inv.syl[i][0], inv.syl[i][0]) + {"e": "i", "o": "u"}.get(inv.syl[i][1], inv.syl[i][1])
    cands = [i for i, x in enumerate(inv.syl) if x[0] != "" and x[2] == "" and inv.name[i] not in gforms
             and inv.grammar_key(i) not in bad_keys]

    def juncture_bad(sel):
        bad = 0
        for d in sel:
            for f in near_forms + [inv.name[x] for x in sel]:
                s2 = inv.idx[f]
                if inv.syl[s2][0] != "" and inv.content_key((d, s2)) in content_keys:
                    bad += 1
        return bad

    def cost(sel):
        c = sum(inv.S[a, b] + inv.S[b, a] for i, a in enumerate(sel) for b in sel[i + 1:])
        c += 10.0 * (len(sel) - len({dkey(a) for a in sel}))
        c += 10.0 * (len(sel) - len({inv.syl[a][0] for a in sel}))  # different first consonants
        for a in sel:
            for u, w in near_syl:
                c += w * (inv.S[a, u] + inv.S[u, a])
        return c + 1.0 * juncture_bad(sel)

    rng = random.Random(seed)
    best, best_c = None, float("inf")
    for restart in range(20):
        sel = rng.sample(cands, 6)
        cur = cost(sel)
        for _ in range(4000):
            k = rng.randrange(6); new = rng.choice(cands)
            if new in sel:
                continue
            old = sel[k]; sel[k] = new
            c = cost(sel)
            if c <= cur:
                cur = c
            else:
                sel[k] = old
        if cur < best_c:
            best, best_c = list(sel), cur
    digits = best
    print("juncture problems in digits:", juncture_bad(digits))

    # two-syllable number words
    taken = set(content_keys) | {inv.content_key((a, b)) for a in digits for b in digits}
    other2 = np.array([split(w["form"]) for w in lex if len(split(w["form"])) == 2])
    open_syl = [i for i, x in enumerate(inv.syl) if x[2] == ""]
    pool = [(a, b) for a in open_syl for b in open_syl if inv.syl[b][0] != "" and inv.content_key((a, b)) not in taken
            and a not in digits]
    n = len(NUMBER_WORDS)
    assign = rng.sample(range(len(pool)), n)

    def wcost(i, k):
        a, b = pool[k]
        c = 10.0 * (inv.S[a, other2[:, 0]] * inv.S[b, other2[:, 1]] + inv.S[other2[:, 0], a] * inv.S[other2[:, 1], b]).sum()
        for j in range(n):
            if j != i:
                x, y = pool[assign[j]]
                c += 30.0 * (inv.S[a, x] * inv.S[b, y] + inv.S[x, a] * inv.S[y, b])
                if inv.content_key((a, b)) == inv.content_key((x, y)):
                    c += 1000
        c += sum(3.0 * (inv.S[a, d] + inv.S[d, a]) for d in digits)  # first syllable unlike any digit
        return c

    for _ in range(60000):
        i, k = rng.randrange(n), rng.randrange(len(pool))
        if k in assign:
            continue
        if wcost(i, k) < wcost(i, assign[i]):
            assign[i] = k
    rows = [{"value": str(v), "kind": "digit", "form": inv.name[d]} for v, d in enumerate(digits)]
    kinds = {"6": "place", "36": "place", "216": "place", "6^4": "group", "6^8": "group", "6^12": "group",
             "POINT": "sign", "MINUS": "sign"}
    for w, k in zip(NUMBER_WORDS, assign):
        rows.append({"value": w, "kind": kinds[w], "form": inv.show(pool[k])})
    write("numbers.tsv", rows, ["value", "kind", "form"])
    lex += [{"gloss": r["value"], "field": "number", "tier": "3", "form": r["form"]} for r in rows if r["kind"] != "digit"]
    write("lexicon.tsv", lex, ["gloss", "field", "tier", "form", "kind"])
    for r in rows:
        print(f"{r['value']:>6} {r['kind']:6} {r['form']}")


if __name__ == "__main__":
    {"scale": scale, "build": build, "numbers3": numbers3}[sys.argv[1]]()

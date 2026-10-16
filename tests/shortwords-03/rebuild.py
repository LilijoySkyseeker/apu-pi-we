"""Short-word rebuild, rerun (tests/shortwords-03, 2026-10-15) of the dry run in tests/shortwords-02.
Copied from shortwords-02/rebuild.py; changes for the rerun (README.md here):
  - offensive filter tiered (design log 2026-10-15): offensive.blocked(form) is a hard rule (H5);
    offensive.matches(form) is the small tie-break penalty ("C3 mode", 0.002 each). No "hard" mode.
  - variants: confusion2.variants() now has 50 (src-av, src-lp). SW_VARIANTS=all|no-av|no-lp|half-a|half-b
    picks a subset (drop test, hold-out check); SW_OVERRIDE="param=value,..." sets a parameter in every v2
    variant (one-at-a-time sensitivity; value may be low/high/best from the parameter table).
  - --lock OF,ALL keeps those words at today's forms (the name apu pi we).
  - reopt: re-optimise from a given layer (sensitivity, drop test); score: robust score of layers.
Proposes forms only: reads data/, writes nothing outside this folder.

Words: every row of data/grammar.tsv, MODMOD (new), ENDEAR (new, added 2026-10-15), digits 0-5. Every form is one syllable (C)V(n).

Hard rules (a move that breaks one is never taken):
  H1  every word has a consonant onset (rule 3)
  H2  digits are open syllables, CV (numbers3 in tools/build.py; reference 2.11 is stated for open syllables)
  H3  no two short words share a form (rule 6; today's layer has no homophones either)
  H4  two words that share a position (positions.py + the position table) never differ only by voicing,
      f/p, glide vs no onset or a final -n (rule 2)
  H5  no word takes a form on the offensive hard list (offensive.blocked; author 2026-10-15)
Costs:
  robust score  CVaR 0.25 over confusion2.variants() (48: best, 32 LHS, 14 corners, v1) of each variant's
                cost / that variant's median over random layers (notes §6); cost = word confusion
                sum_a sum_b W_ab f_a P_v(a heard as b)  +  junction misparse risk of short-word bigrams
                sum_(A,B) w_AB P_v((A,B) heard as (A',B')) over boundary events, confusion2 junction terms
                W_ab = 1 if a and b share a position, else 0.1; x10 for pairs with NOT, x3 digit-digit
                (stakes inherited from tools/build.py); w_AB from corpus bigram counts (adjacency.tsv)
  penalties     offensive tie-break match (offensive.matches, not blocked; goal C3) ; shared pair differing by only one feature (rule 2b) ;
                form equal to the first syllable of a two-syllable operator sharing its position (rule 6)

  python3 rebuild.py full      [--seed0 N] [--seeds N] [--steps N] [--keep X] [--start F] [--lock OF,ALL] --out F
  python3 rebuild.py patch
  python3 rebuild.py report name=file.tsv ...   # tables -> results.txt, forms.tsv
"""
import collections, csv, itertools, math, os, random, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import confusion2 as M2
import offensive

SYL, NAME, IDX, ONSETS, VOWELS = M2.SYLLABLES, M2.NAME, M2.IDX, M2.ONSETS, M2.VOWELS
NS = len(SYL)
OI, VI = M2.OI, M2.VI


def read(path):
    with open(path) as fh:
        return list(csv.DictReader((l for l in fh if not l.startswith("#")), delimiter="\t"))


# ------------------------------------------------------------------------------------------ words
GRAM = read(os.path.join(ROOT, "data", "grammar.tsv"))
DIG = [r for r in read(os.path.join(ROOT, "data", "numbers.tsv")) if r["kind"] == "digit" and r["value"] in "012345"]
DIGIT_FREQ = 4.0     # as tests/shortwords-01/analysis.py (no recorded source: a guess)
MODMOD_FREQ = 1.0    # guess: colour shades and other stacked modifiers (design log 2026-10-13)
WORDS = [{"gloss": g["gloss"], "cls": g["class"], "freq": float(g["freq"]), "old": g["form"]} for g in GRAM]
WORDS.append({"gloss": "MODMOD", "cls": "np", "freq": MODMOD_FREQ, "old": ""})
ENDEAR_FREQ = 1.0    # added: unmeasured (task addendum 2026-10-15); child-directed speech higher, ordinary text lower
WORDS.append({"gloss": "ENDEAR", "cls": "np", "freq": ENDEAR_FREQ, "old": ""})
NEW = ("MODMOD", "ENDEAR")   # words with no form today: never counted as a change
WORDS += [{"gloss": f"D{d['value']}", "cls": "digit", "freq": DIGIT_FREQ, "old": d["form"]} for d in DIG]
N = len(WORDS)
GL = [w["gloss"] for w in WORDS]
GI = {g: i for i, g in enumerate(GL)}
FREQ = np.array([w["freq"] for w in WORDS])
IS_DIGIT = np.array([w["cls"] == "digit" for w in WORDS])
OLD_FORM = {w["gloss"]: w["old"] for w in WORDS}
FORM_GLOSS = {w["old"]: w["gloss"] for w in WORDS if w["old"]}
OPERATORS = "genso wanme inwun wemen konsin nedin tason mesun manni buntu buni donon lanno anko nuwen kiyo mena".split()

# ------------------------------------------------------------------------------------------ position table
# Named positions, from the reference (rule ids) and the formal grammar's categories (grammar/Apupiwe.gf).
# Two-syllable operators are listed where they stand, for the operator rule; they are not re-formed here.
PRON = "I YOU WE.incl WE.excl HE/SHE OBVIATIVE IT LOGOPHOR GENERIC SELF".split()
DERIV = "AGENT RESULT TOOL PLACE".split()
DET = "THIS THAT.dem ALL SOME PART NONE UNSPEC WH".split()
DIGS = [f"D{i}" for i in range(6)]
PHRASE_OP = "NOT ONLY ALSO EVEN FOCUS".split()
POSITIONS = [
    ("P1 call (slots 1, 13)", "4.1.2, 10.1", ["NAME"], ["lanno"]),
    ("P2 linker (slot 2)", "4.3.6", ["AND", "BUT", "BECAUSE"], []),
    ("P3 relation word: scene (slot 2), relation phrase (slot 10)", "4.3.1, 4.4.1, 13.1; GF Prep",
     ["AT", "TO", "FROM", "WITH", "FOR", "BEFORE", "AFTER", "LIKE", "WHILE", "BECAUSE"], ["anko", "nuwen"]),
    ("P4 topic (slot 2)", "4.3.2", ["OF"], []),
    ("P5 if/when clause (slot 2), trailing clause (slot 11)", "4.3.3, 4.1.2; GF Sub, Cond",
     ["IF", "WHILE", "AFTER", "BEFORE", "BECAUSE", "THAT.comp"], []),
    ("P6 speech act (slot 3) and politeness (slot 4)", "7.1, 10.2.1; GF Part, PMod, Nun",
     ["Q", "REQUEST", "INSTRUCT", "ADVISE", "INTEND", "WARN", "EXCLAIM", "POLITE"], ["genso"]),
    ("P7 clause operator (slot 5)", "6.1; GF ConfOpt, SrcOpt", ["CONF"], ["wanme", "inwun", "wemen"]),
    ("P8 noun-phrase start (slots 6, 9; after a relation word)", "5.1, 5.2.4, 5.2.8, 5.4, 6.2.1, 10.3, 11.1; GF Pron, Deriv, DetQ, NumQ, OpNP",
     PRON + DERIV + ["NAME"] + DET + DIGS + PHRASE_OP, ["lanno"]),
    ("P9 before the verb (slot 7) and before a quality", "6.2, 8.1, 4.7; GF Op, Asp, HabOpt, OpAP",
     PHRASE_OP + ["MORE", "VERY", "DONE", "ONGOING", "BE"], ["konsin", "nedin", "tason", "manni", "buntu"]),
    ("P10 after a content modifier", "5.1 (rule pending, design log 2026-10-13)", ["MODMOD"], []),
    ("P16 after a noun or a name (endearment)", "design log 2026-10-15 (rule pending)", ["ENDEAR"], []),
    ("P11 number slot: number, la, determiner after the noun", "5.1, 5.2.5-5.2.8, rule 4 of the rebuild; GF NumOpt, LaOpt, DetOpt",
     DIGS + ["PLURAL"] + DET + ["SELF"], ["mesun", "mena"]),
    ("P12 after the noun phrase: pi phrase, relative clause", "5.1, 5.2.9, 5.3", ["OF", "WHO.rel"], []),
    ("P13 joining words", "4.4.5; GF Conj", ["AND", "OR", "BUT"], []),
    ("P14 number after kon, mena, fu", "6.1.2, 5.2.5, 9.3.1", DIGS + ["UNSPEC"], []),
    ("P15 stance (slot 12)", "7.2, 4.8.4; GF Stance, ChoiceYu", ["Q", "YOUKNOW", "WH"], ["buni", "donon"]),
]
for _, _, ws, _ in POSITIONS:
    for w in ws:
        assert w in GI, w

TABLE_SHARED = np.zeros((N, N), bool)
for _, _, ws, _ in POSITIONS:
    for a in ws:
        for b in ws:
            if a != b:
                TABLE_SHARED[GI[a], GI[b]] = True


def load_substitution():
    """substitution.tsv (positions.py). Returns: shared (fits_full >= 1 in either direction), the pooled share
    (fits A->B + fits B->A) / (contexts A + contexts B), operators' shared words, raw counts."""
    path = os.path.join(HERE, "substitution.tsv")
    gf = np.zeros((N, N), bool)
    ops = collections.defaultdict(set)
    fits, ctx = collections.Counter(), collections.Counter()
    extra = os.path.join(HERE, "operators-extra.tsv")   # positions.py operators: frames for operators the corpus lacks
    rows = (read(path) if os.path.exists(path) else []) + (read(extra) if os.path.exists(extra) else [])
    if rows:
        for r in rows:
            b = r["glossB"]
            if b not in GI:
                continue
            n = int(r["fits_full"])
            if r["glossA"] == "operator":
                if n:
                    ops[r["A"]].add(b)
                continue
            fits[r["glossA"], b] = n
            ctx[r["glossA"]] = int(r["contexts_A"])
            if n:
                gf[GI[r["glossA"]], GI[b]] = gf[GI[b], GI[r["glossA"]]] = True
    pool = np.zeros((N, N))
    for i, j in itertools.permutations(range(N), 2):
        den = ctx[GL[i]] + ctx[GL[j]]
        if den:
            pool[i, j] = (fits[GL[i], GL[j]] + fits[GL[j], GL[i]]) / den
    return gf, pool, ops, (fits, ctx)


def load_modmod(fname="modmod.tsv"):
    """modmod.tsv / endear.tsv (positions.py modmod / endear): how many of the hand frames each short word fits."""
    path = os.path.join(HERE, fname)
    if not os.path.exists(path):
        return {}, 1
    rows = read(path)
    nframes = int(re.search(r"(\d+) frames", open(path).readline()).group(1)) if "frames" in open(path).readline() else 5
    return {r["gloss"]: int(r["fits"]) for r in rows}, nframes


GF_SHARED, POOL, OP_SHARED, SUBCOUNT = load_substitution()
MODMOD_FITS, MODMOD_FRAMES = load_modmod()
SHARED = TABLE_SHARED | GF_SHARED
ENDEAR_FITS, ENDEAR_FRAMES = load_modmod("endear.tsv")
for w, fits_, nfr in (("MODMOD", MODMOD_FITS, MODMOD_FRAMES), ("ENDEAR", ENDEAR_FITS, ENDEAR_FRAMES)):
    m = GI[w]
    for g, n in fits_.items():
        if n:
            SHARED[m, GI[g]] = SHARED[GI[g], m] = True
            POOL[m, GI[g]] = POOL[GI[g], m] = n / nfr
np.fill_diagonal(SHARED, False)
for _, _, ws, ops in POSITIONS:
    for o in ops:
        OP_SHARED[o] |= set(ws)

# ------------------------------------------------------------------------------------------ pair weights
# how often a mishearing of a as b still gives a grammatical sentence: the pooled substitution share; a pair in
# the same slot of the position table counts at least 0.5; pairs that never substitute keep a floor of 0.1
W = 0.1 + 0.9 * np.maximum(POOL, 0.5 * TABLE_SHARED)
W[GI["NOT"], :] *= 10; W[:, GI["NOT"]] *= 10
W[np.ix_(IS_DIGIT, IS_DIGIT)] *= 3
np.fill_diagonal(W, 0)
WF = W * FREQ[:, None]          # cost of a heard as b: W_ab f_a P(a->b)


def load_adjacency():
    path = os.path.join(HERE, "adjacency.tsv")
    if not os.path.exists(path):
        return []
    rows = [r for r in read(path) if r["glossA"] in GI and r["glossB"] in GI]
    total = sum(int(r["count"]) for r in rows)
    # scale: a bigram as common as the average short word weighs like that word's frequency
    tok = read(os.path.join(HERE, "corpus-counts.tsv"))
    ntok = sum(int(r["tokens"]) for r in tok if r["gloss"] in GI)
    scale = FREQ.sum() / max(ntok, 1)
    return [(GI[r["glossA"]], GI[r["glossB"]], int(r["count"]) * scale) for r in rows]


ADJ = load_adjacency()
ADJ_A = np.array([a for a, _, _ in ADJ], int)
ADJ_B = np.array([b for _, b, _ in ADJ], int)
ADJ_W = np.array([w for _, _, w in ADJ])

# ------------------------------------------------------------------------------------------ syllable facts
VOI = {"b": "p", "d": "t", "g": "k"}


def merger(s, t):
    (o1, v1, c1), (o2, v2, c2) = SYL[s], SYL[t]
    if s == t:
        return "same form"
    if v1 != v2:
        return None
    if o1 == o2:
        return "final -n" if c1 != c2 else None
    if c1 != c2:
        return None
    if VOI.get(o1, o1) == VOI.get(o2, o2):
        return "voicing"
    if {o1, o2} == {"f", "p"}:
        return "f/p"
    if "" in (o1, o2) and {o1, o2} - {""} <= {"w", "j"}:
        return "glide vs none"
    return None


MERGE = np.array([[merger(s, t) is not None for t in range(NS)] for s in range(NS)])
CF = {"p": ("-", "lab", "stop"), "b": ("+", "lab", "stop"), "t": ("-", "cor", "stop"), "d": ("+", "cor", "stop"),
      "k": ("-", "dor", "stop"), "g": ("+", "dor", "stop"), "f": ("-", "lab", "fric"), "s": ("-", "cor", "fric"),
      "m": ("+", "lab", "nas"), "n": ("+", "cor", "nas"), "l": ("+", "cor", "lat"), "w": ("+", "lab", "glide"),
      "j": ("+", "pal", "glide")}
VF = {"i": ("hi", "front"), "e": ("mid", "front"), "a": ("lo", "central"), "o": ("mid", "back"), "u": ("hi", "back")}


def fdist(s, t):
    (o1, v1, c1), (o2, v2, c2) = SYL[s], SYL[t]
    d = 0
    if o1 != o2:
        d += 1 if "" in (o1, o2) else sum(x != y for x, y in zip(CF[o1], CF[o2]))
    d += sum(x != y for x, y in zip(VF[v1], VF[v2]))
    return d + (c1 != c2)


FD = np.array([[fdist(s, t) for t in range(NS)] for s in range(NS)])
ONE_FEATURE = FD == 1
HAS_ONSET = np.array([o != "" for o, _, _ in SYL])
OPEN = np.array([c == "" for _, _, c in SYL])
BLOCKED = np.array([offensive.blocked(n) for n in NAME])                                 # hard (H5)
OFFENSIVE = np.array([offensive.matches(n) and not offensive.blocked(n) for n in NAME])  # tie-break only (C3)
FLIP = np.array([M2.SYL_INDEX[o, v, "n" if c == "" else ""] for o, v, c in SYL])
ONSET_SWAP = np.array([[M2.SYL_INDEX[oh, v, c] for oh in ONSETS] for o, v, c in SYL])  # syllable with onset replaced
S_O = np.array([OI[o] for o, _, _ in SYL]); S_V = np.array([VI[v] for _, v, _ in SYL]); S_C = np.array([c == "n" for _, _, c in SYL], int)
# operator first syllables
OP_FIRST = {o: IDX[re.findall(r"[^aeiou]?[aeiou](?:n(?![aeiou]))?", o)[0]] for o in OPERATORS}

# ------------------------------------------------------------------------------------------ variants
VARSET = os.environ.get("SW_VARIANTS", "all")
OVERRIDE = os.environ.get("SW_OVERRIDE", "")


def _ov_value(k, v):
    d = M2.PARAMS.get(k) or M2.ADDED.get(k)
    return float(d[v]) if v in ("low", "high", "best") else float(v)


def pick_variants():
    """The variant set for this run (env SW_VARIANTS, SW_OVERRIDE)."""
    vs = M2.variants(av=VARSET != "no-av", lp=VARSET != "no-lp")
    if VARSET in ("half-a", "half-b"):
        # hold-out split (added): stratified, half of the Latin-hypercube draws and half of the rest, fixed seed
        rng = random.Random(7)
        lhs = [i for i, (n, _) in enumerate(vs) if n.startswith("lhs-")]
        rest = [i for i in range(len(vs)) if i not in lhs]
        rng.shuffle(lhs); rng.shuffle(rest)
        a = set(lhs[:len(lhs) // 2] + rest[:len(rest) // 2])
        vs = [v for i, v in enumerate(vs) if (i in a) == (VARSET == "half-a")]
    if OVERRIDE:
        ov = {}
        for kv in OVERRIDE.split(","):
            k, v = kv.split("=")
            keys = ["glide_hiatus_front", "glide_hiatus_back"] if k == "glide_hiatus" else [k]
            for kk in keys:
                ov[kk] = _ov_value(kk, v)
        vs = [(n, p if p.get("model") == "v1" else dict(p, **ov)) for n, p in vs]
    return vs


VARIANTS = pick_variants()
VNAMES = [n for n, _ in VARIANTS]
NV = len(VARIANTS)


def build_tables():
    S = np.zeros((NV, NS, NS), np.float32)
    gA = np.zeros((NV, NS)); gB = np.zeros((NV, NS))
    BF = np.zeros((NV, 5, 2, len(ONSETS), len(ONSETS)))
    for k, (name, p) in enumerate(VARIANTS):
        m = M2.Model(p)
        S[k] = m.S_initial
        Cl, Vm, K = m.C["initial"], m.V, m.K
        for s, (o, v, c) in enumerate(SYL):
            gA[k, s] = Cl[OI[o], OI[o]] * Vm[VI[v], VI[v]]
            ci = M2.CODAS.index(c)
            gB[k, s] = Vm[VI[v], VI[v]] * K[ci, ci]
        for vi, v in enumerate(VOWELS):
            for ci, c in enumerate(M2.CODAS):
                for oi, o in enumerate(ONSETS):
                    b = m.boundary(v, c, o)
                    flip = "n" if c == "" else ""
                    for hi, oh in enumerate(ONSETS):
                        BF[k, vi, ci, oi, hi] = b.get((flip, oh), 0.0)
    return S, gA, gB, BF


S_ALL, GA, GB, BF = build_tables()


def conf_costs(assign):
    """Per-variant word-confusion cost of an assignment (array of syllable indices, one per word)."""
    P = S_ALL[:, assign][:, :, assign]               # (V, N, N)
    return (P * WF[None]).sum((1, 2))


def junc_costs(assign, detail=False):
    if not len(ADJ):
        return np.zeros(NV)
    owner = np.full(NS, -1); owner[assign] = np.arange(N)
    sA, sB = assign[ADJ_A], assign[ADJ_B]
    e1 = owner[FLIP[sA]] >= 0                         # A with its coda flipped is a word
    e2 = owner[ONSET_SWAP[sB]] >= 0                   # (P, 14): B with onset oh is a word
    bf = BF[:, S_V[sA], S_C[sA], S_O[sB], :]          # (V, P, 14)
    val = GA[:, sA] * GB[:, sB] * (bf * e2[None]).sum(2)
    per = val * (ADJ_W * e1)[None]
    return per if detail else per.sum(1)


def totals(assign):
    return conf_costs(assign), junc_costs(assign)


def random_layer(rng):
    onset = [s for s in range(NS) if HAS_ONSET[s] and not BLOCKED[s]]
    opn = [s for s in onset if OPEN[s]]
    d = rng.sample(opn, int(IS_DIGIT.sum()))
    rest = rng.sample([s for s in onset if s not in d], N - len(d))
    a = np.zeros(N, int); a[IS_DIGIT] = d; a[~IS_DIGIT] = rest
    return a


_MED = None


def medians():
    global _MED
    if _MED is None:
        rng = random.Random(99)
        c = np.array([sum(totals(random_layer(rng))) for _ in range(400)])
        _MED = np.median(c, 0)
    return _MED


TOPQ = int(math.ceil(0.25 * NV))


def cvar(cost_v):
    x = np.sort(cost_v / medians())[::-1]
    return x[:TOPQ].mean()


# ------------------------------------------------------------------------------------------ rules
def hard_ok(assign, i, s, fixed_other=None):
    """Can word i take syllable s, given the other words' syllables?"""
    if not HAS_ONSET[s] or BLOCKED[s] or (IS_DIGIT[i] and not OPEN[s]):
        return False
    others = (np.arange(N) != i) & (assign >= 0)
    if (assign[others] == s).any():
        return False
    sh = SHARED[i] & others
    return not MERGE[s, assign[sh]].any()


def penalties(assign, off_w, one_w, op_w):
    off = OFFENSIVE[assign].sum()
    iu = np.triu_indices(N, 1)
    one = (SHARED[iu] & ONE_FEATURE[assign[iu[0]], assign[iu[1]]]).sum()
    ops = sum(1 for o, ws in OP_SHARED.items() for g in ws if assign[GI[g]] == OP_FIRST[o])
    return off_w * off + one_w * one + op_w * ops, (int(off), int(one), int(ops))


def violations(assign):
    out = []
    for a, b in itertools.combinations(range(N), 2):
        if SHARED[a, b] and MERGE[assign[a], assign[b]]:
            out.append((GL[a], GL[b], NAME[assign[a]], NAME[assign[b]], merger(assign[a], assign[b])))
    for i in range(N):
        if not HAS_ONSET[assign[i]]:
            out.append((GL[i], "", NAME[assign[i]], "", "no onset"))
        if IS_DIGIT[i] and not OPEN[assign[i]]:
            out.append((GL[i], "", NAME[assign[i]], "", "digit with -n"))
        if BLOCKED[assign[i]]:
            out.append((GL[i], "", NAME[assign[i]], "", "blocked (offensive hard list)"))
    return out


# ------------------------------------------------------------------------------------------ annealer
PEN = (0.002, 0.004, 0.02)  # offensive tie-break match, one-feature, operator ("C3 mode" of the dry run)


OLD_SYL = np.array([IDX[w["old"]] if w["old"] else -1 for w in WORDS])
KEEP = [0.0]    # penalty per existing word whose form changes (the keep sweep; 0 = a plain full rebuild)


def anneal(start, free, steps, seed, pen, T0=0.02):
    """Simulated annealing over the words in `free` (indices), others fixed. start must satisfy the hard rules
    for fixed words; free words are repaired first."""
    rng = random.Random(seed)
    a = start.copy()
    if any(not hard_ok(a, i, a[i]) for i in free):   # build a legal start: place free words one by one
        for _ in range(200):
            a[list(free)] = -1
            order = sorted(free, key=lambda i: (-SHARED[i].sum(), rng.random()))
            for i in order:
                opts = [s for s in range(NS) if hard_ok(a, i, s)]
                if not opts:
                    break
                a[i] = rng.choice(opts)
            if (a >= 0).all():
                break
        assert (a >= 0).all(), "no legal start found"
    conf, junc = totals(a)

    def objective(conf, junc, a):
        return cvar(conf + junc) + penalties(a, *pen)[0] + KEEP[0] * ((a != OLD_SYL) & (OLD_SYL >= 0)).sum()

    cur = objective(conf, junc, a)
    best, best_a = cur, a.copy()
    free = list(free)
    for step in range(steps):
        T = T0 * (1 - step / steps) + 1e-6
        i = rng.choice(free)
        if rng.random() < 0.6:
            s = rng.randrange(NS)
            if s == a[i] or not hard_ok(a, i, s):
                continue
            old = a[i]
            a[i] = s
        else:
            j = rng.choice(free)
            if i == j:
                continue
            a[i], a[j] = a[j], a[i]
            if not (hard_ok(a, i, a[i]) and hard_ok(a, j, a[j])):
                a[i], a[j] = a[j], a[i]
                continue
            old = None
        c2, j2 = totals(a)
        new = objective(c2, j2, a)
        if new < cur or rng.random() < math.exp(-(new - cur) / T):
            cur, conf, junc = new, c2, j2
            if cur < best:
                best, best_a = cur, a.copy()
        else:
            if old is None:
                a[i], a[j] = a[j], a[i]
            else:
                a[i] = old
    return best_a, best


def old_assign():
    """Today's forms; MODMOD and ENDEAR (no form yet) get the best legal free syllables: each starts on a legal
    free syllable, then each in turn takes its best one given the other, three rounds."""
    a = np.array([IDX[w["old"]] if w["old"] else -1 for w in WORDS])
    for g in NEW:
        a[GI[g]] = next(s for s in range(NS) if s not in a and hard_ok(a, GI[g], s))
    for _ in range(3):
        for g in NEW:
            i = GI[g]
            best, bs = None, a[i]
            for s in range(NS):
                if s != a[i] and (s in a or not hard_ok(a, i, s)):
                    continue
                b = a.copy(); b[i] = s
                c = cvar(sum(totals(b))) + penalties(b, *PEN)[0]
                if best is None or c < best:
                    best, bs = c, s
            a[i] = bs
    return a


def write_layer(name, a, note=""):
    path = os.path.join(HERE, name)
    with open(path + ".tmp", "w") as fh:     # atomic (added after the host crash): a layer file that exists is complete
        fh.write(f"# {note}\n" if note else "")
        fh.write("gloss\tclass\tfreq\told\tnew\n")
        for i, w in enumerate(WORDS):
            fh.write(f"{w['gloss']}\t{w['cls']}\t{w['freq']:g}\t{w['old']}\t{NAME[a[i]]}\n")
    os.replace(path + ".tmp", path)


def read_layer(name):
    rows = [r for r in csv.DictReader((l for l in open(os.path.join(HERE, name)) if not l.startswith("#")), delimiter="\t")]
    return np.array([IDX[{r["gloss"]: r["new"] for r in rows}[g]] for g in GL])


def lock_set(argv):
    """--lock OF,ALL: words that keep today's form (the name apu pi we)."""
    return sorted(GI[g] for g in arg(argv, "--lock", "").split(",") if g)


def objective_of(a):
    return cvar(sum(totals(a))) + penalties(a, *PEN)[0] + KEEP[0] * ((a != OLD_SYL) & (OLD_SYL >= 0)).sum()


def full(argv):
    steps = int(arg(argv, "--steps", 60000))
    seeds = int(arg(argv, "--seeds", 6))
    KEEP[0] = float(arg(argv, "--keep", 0.0))
    out = arg(argv, "--out", "full.tsv")
    lock = lock_set(argv)
    free = [i for i in range(N) if i not in lock]
    results = []
    seed0 = int(arg(argv, "--seed0", 0))
    for seed in range(seed0, seed0 + seeds):
        start = read_layer(arg(argv, "--start", "")) if "--start" in argv else random_layer(random.Random(seed))
        start[lock] = OLD_SYL[lock]
        a, obj = anneal(start, free, steps, seed, PEN)
        sc = cvar(sum(totals(a)))
        print(f"seed {seed}: changed {int(((a != OLD_SYL) & (OLD_SYL >= 0)).sum())}  objective {obj:.4f}  robust score {sc:.4f}  penalties {penalties(a, *PEN)[1]}  "
              f"violations {len(violations(a))}", flush=True)
        results.append((obj, seed, a))
    obj, seed, a = min(results, key=lambda r: r[0])
    write_layer(out, a, f"full rebuild, C3 tie-break, keep={KEEP[0]}, lock={','.join(GL[i] for i in lock) or 'none'}, variants={VARSET}{' ' + OVERRIDE if OVERRIDE else ''}, "
                        f"best of {seeds} seeds (seed {seed}), {steps} steps, start {arg(argv, '--start', 'random')}, objective {obj:.4f}")
    print(f"wrote {out}")


def reopt(argv):
    """Re-optimise from a layer under the current variant set (sensitivity, drop test, controls).
    --layer F  --free all|changed (changed: words whose form differs from today, plus MODMOD: the patch's own
    change set)  --keep X  --lock OF,ALL  --steps N  --T0 X  --seed N  [--out F]. Prints the forms that moved."""
    KEEP[0] = float(arg(argv, "--keep", 0.0))
    a0 = read_layer(arg(argv, "--layer", ""))
    lock = lock_set(argv)
    if arg(argv, "--free", "all") == "changed":
        free = [i for i in range(N) if (a0[i] != OLD_SYL[i] or OLD_SYL[i] < 0) and i not in lock]
    else:
        free = [i for i in range(N) if i not in lock]
    steps, T0, seed = int(arg(argv, "--steps", 100000)), float(arg(argv, "--T0", 0.002)), int(arg(argv, "--seed", 1))
    o0 = objective_of(a0)
    a, obj = anneal(a0, free, steps, seed, PEN, T0=T0)
    if objective_of(a) > o0:          # never report a worse layer than the start
        a, obj = a0.copy(), o0
    moved = [f"{GL[i]} {NAME[a0[i]]}->{NAME[a[i]]}" for i in range(N) if a[i] != a0[i]]
    tag = f"{os.path.basename(arg(argv, '--layer', ''))} variants={VARSET} override={OVERRIDE or 'none'}"
    print(f"REOPT {tag} | moved {len(moved)} | objective {o0:.4f} -> {obj:.4f} | robust {cvar(sum(totals(a0))):.4f} -> "
          f"{cvar(sum(totals(a))):.4f} | {'; '.join(moved)}", flush=True)
    if "--out" in argv:
        write_layer(arg(argv, "--out", ""), a, f"reopt of {tag}, steps {steps}, T0 {T0}, seed {seed}, objective {obj:.4f}")


def score(argv):
    """Robust score (and objective parts) of layer files under the current variant set."""
    for f in argv:
        a = read_layer(f)
        print(f"SCORE {f} variants={VARSET} override={OVERRIDE or 'none'} robust {cvar(sum(totals(a))):.4f} "
              f"penalties {penalties(a, *PEN)[1]} changed {int(((a != OLD_SYL) & (OLD_SYL >= 0)).sum())}", flush=True)


# ------------------------------------------------------------------------------------------ minimal patch
def merger_edges(a):
    return [(i, j) for i, j in itertools.combinations(range(N), 2) if SHARED[i, j] and MERGE[a[i], a[j]]]


def min_covers(edges, forced, keep=frozenset(), limit=200000):
    """All minimum vertex covers of the merger graph that contain `forced` (branch on an uncovered edge)."""
    best = [None]; out = []

    def rec(cover, k):
        if best[0] is not None and len(cover) > best[0]:
            return
        e = next(((i, j) for i, j in edges if i not in cover and j not in cover), None)
        if e is None:
            if best[0] is None or len(cover) < best[0]:
                best[0] = len(cover); out.clear()
            out.append(frozenset(cover)); return
        for v in e:
            if v not in keep:
                rec(cover | {v}, k + 1)

    rec(frozenset(forced), 0)
    return sorted(set(out), key=lambda c: sum(FREQ[list(c)]))


def patch(argv):
    rule3 = "--no-rule3" not in argv
    steps = int(arg(argv, "--steps", 6000))
    pen = PEN
    out = arg(argv, "--out", "patch.tsv" if rule3 else "patch-no-rule3.tsv")
    a0 = np.array([IDX[w["old"]] if w["old"] else -1 for w in WORDS])
    a0[GI["MODMOD"]] = IDX["fan"]          # placeholders, re-formed below
    a0[GI["ENDEAR"]] = IDX["fen"]
    forced = {GI["MODMOD"], GI["ENDEAR"], GI["YOUKNOW"]} | {i for i in range(N) if a0[i] >= 0 and BLOCKED[a0[i]]}
    if rule3:
        forced |= {i for i in range(N) if WORDS[i]["old"] and not HAS_ONSET[IDX[WORDS[i]["old"]]]}
    edges = [(i, j) for i, j in merger_edges(a0) if GI["MODMOD"] not in (i, j) and GI["ENDEAR"] not in (i, j)]
    keep = frozenset(GI[g] for g in arg(argv, "--keep-words", "").split(",") if g)
    covers = min_covers(edges, forced, keep)
    print(f"{len(edges)} merger pairs; minimum change set {len(covers[0])} words; {len(covers)} such sets", flush=True)
    results = []
    for k, cov in enumerate(covers[:40]):
        free = sorted(cov)
        a = a0.copy(); a[free] = -1
        rng = random.Random(k)
        for _ in range(200):     # added: up to 200 random greedy starts (the dry run tried one and skipped some sets)
            a[free] = -1
            for i in sorted(free, key=lambda i: (-SHARED[i].sum(), rng.random())):
                opts = [s for s in range(NS) if s not in a and hard_ok(a, i, s)]
                if not opts:
                    break
                a[i] = rng.choice(opts)
            if (a >= 0).all():
                break
        if (a < 0).any():
            print(f"  set {k}: no legal start found, skipped"); continue
        best_a, obj = anneal(a, free, steps, k, pen)
        bad = merger_edges(best_a)
        results.append((obj, k, best_a, cov))
        print(f"  set {k}: {' '.join(GL[i] for i in sorted(cov))}  objective {obj:.4f}  mergers left {len(bad)}", flush=True)
    obj, k, a, cov = min(results, key=lambda r: r[0])
    write_layer(out, a, f"minimal patch ({'with' if rule3 else 'without'} rule 3): {len(cov)} words change; "
                        f"best of {len(results)} minimum change sets; objective {obj:.4f}")
    print(f"wrote {out}")


# ------------------------------------------------------------------------------------------ report
DESK16 = [("INSTRUCT", "WE.excl"), ("INTEND", "D5"), ("WARN", "AFTER"), ("WARN", "FOCUS"), ("UNSPEC", "D0"),
          ("WE.incl", "THAT.dem"), ("OBVIATIVE", "EVEN"), ("OF", "VERY"), ("OF", "D1"), ("BEFORE", "YOUKNOW"),
          ("AFTER", "FOCUS"), ("AND", "NAME"), ("BUT", "THAT.comp"), ("MORE", "RESULT"), ("LIKE", "PLACE"), ("IT", "PLACE")]
ROBUST13 = [("MORE", "D5"), ("INSTRUCT", "PART"), ("Q", "WHILE"), ("OF", "D1"), ("LIKE", "PLACE"), ("PLURAL", "ONLY"),
            ("NONE", "D2"), ("FROM", "ALSO"), ("I", "D0"), ("NONE", "EXCLAIM"), ("LIKE", "IT"), ("VERY", "D1"),
            ("INTEND", "RESULT")]
V2 = [k for k, n in enumerate(VNAMES) if n != "v1"]


def sym(a, i, j):
    """Symmetric confusion of words i and j in layer a: (best, max over v2 variants), percent."""
    x = (S_ALL[:, a[i], a[j]] + S_ALL[:, a[j], a[i]]) / 2
    return 100 * x[VNAMES.index("best")], 100 * x[V2].max()


def pair_line(a, i, j):
    b, w = sym(a, i, j)
    m = merger(a[i], a[j])
    return f"{NAME[a[i]]}~{NAME[a[j]]}", b, w, m


def ops_to_rename(a):
    out = []
    for o in OPERATORS:
        hit = [g for g in OP_SHARED.get(o, ()) if a[GI[g]] == OP_FIRST[o]]
        if hit:
            out.append(f"{o} ({NAME[OP_FIRST[o]]} = {', '.join(hit)})")
    return out


def digit_clash(a):
    lex = read(os.path.join(ROOT, "data", "lexicon.tsv"))
    ds = {NAME[a[GI[f"D{k}"]]] for k in range(6)}
    hits = [w["form"] for w in lex if w["field"] != "loan" and re.findall(r"[^aeiou]?[aeiou](?:n(?![aeiou]))?", w["form"])[0] in ds]
    return hits


def report(argv):
    layers = {"old": old_assign()}
    for spec in argv:                       # name=file.tsv
        name, f = spec.split("=")
        layers[name] = read_layer(f)
    out = []
    P = out.append
    P("SHORT-WORD REBUILD, RERUN (tests/shortwords-03). Generated by rebuild.py report.\n")
    P("SUMMARY: layer, changed, robust, mergers, C3 tie-break matches, blocked, one-feature pairs, operator clashes, name, "
      "desk-16 fixed, robust-13 fixed, shared pairs >= 10% in some v2 variant, digit/content clashes")
    for name, a in layers.items():
        c, j = totals(a)
        changed = sum(1 for i in range(N) if WORDS[i]["old"] and NAME[a[i]] != WORDS[i]["old"])
        pen = penalties(a, *PEN)[1]
        viol = violations(a)
        fixed = lambda pairs: sum(1 for g1, g2 in pairs if not MERGE[a[GI[g1]], a[GI[g2]]] and sym(a, GI[g1], GI[g2])[1] < 2)
        ten = sum(1 for i, k in itertools.combinations(range(N), 2) if SHARED[i, k] and sym(a, i, k)[1] >= 10)
        P(f"  {name:18} {changed:3d} {cvar(c + j):.4f} {sum(1 for v in viol if v[1]):3d} {pen[0]:3d} {int(BLOCKED[a].sum()):2d} {pen[1]:3d} {pen[2]:2d}"
          f"  apu {NAME[a[GI['OF']]]} {NAME[a[GI['ALL']]]}  {fixed(DESK16):2d}/16 {fixed(ROBUST13):2d}/13 {ten:3d} {len(digit_clash(a)):3d}")
    P("")
    P(f"{N} words ({N - 8} grammar words, MODMOD, ENDEAR, 6 digits); {NV} model variants; robust score = CVaR 0.25 of cost / random-layer median")
    P(f"shared-position pairs: {SHARED[np.triu_indices(N, 1)].sum()} of {N * (N - 1) // 2} "
      f"(table {TABLE_SHARED[np.triu_indices(N, 1)].sum()}, GF substitution {GF_SHARED[np.triu_indices(N, 1)].sum()}); "
      f"adjacent short-word bigrams: {len(ADJ)}\n")
    P(f"{'layer':16}{'changed':>8}{'robust':>8}{'conf':>8}{'junc':>8}{'worst variant':>22}{'offens.':>8}{'1-feat':>7}{'op-clash':>9}{'mergers':>8}{'no onset':>9}")
    for name, a in layers.items():
        c, j = totals(a)
        x = (c + j) / medians()
        changed = sum(1 for i in range(N) if WORDS[i]["old"] and NAME[a[i]] != WORDS[i]["old"])
        pen = penalties(a, *PEN)[1]
        viol = violations(a)
        P(f"{name:16}{changed:8d}{cvar(c + j):8.4f}{cvar(c):8.4f}{(j / medians()).mean():8.4f}"
          f"{VNAMES[int(np.argmax(x))] + f' {x.max():.3f}':>22}{pen[0]:8d}{pen[1]:7d}{pen[2]:9d}"
          f"{sum(1 for v in viol if v[1]):8d}{sum(1 for v in viol if v[4] == 'no onset'):9d}")
    P("(changed: grammar words and digits whose form differs from today; MODMOD and ENDEAR are new in every layer. conf = robust score of"
      " word confusion alone; junc = mean junction cost / median. offens. = C3 tie-break matches (offensive.matches, not blocked); 1-feat = shared"
      " pairs differing by one feature; op-clash = operator/first-syllable clashes; mergers = shared pairs that collapse)\n")

    P("FORMS (gloss, class, freq, then each layer; * = changed from today, ! = C3 tie-break match (offensive.matches))")
    names = list(layers)
    P(f"{'gloss':12}{'class':7}{'freq':>5}  " + "".join(f"{n:>15}" for n in names))
    for i in sorted(range(N), key=lambda i: -FREQ[i]):
        cells = []
        for n in names:
            f = NAME[layers[n][i]]
            mark = ("*" if n != "old" and f != WORDS[i]["old"] else "") + ("!" if OFFENSIVE[layers[n][i]] else "")
            cells.append(f"{f + mark:>15}")
        P(f"{GL[i]:12}{WORDS[i]['cls']:7}{FREQ[i]:5g}  " + "".join(cells))
    P("")
    top = sorted(range(N), key=lambda i: (-FREQ[i], i))[:10]
    P("TEN MOST FREQUENT WORDS (freq ties broken by grammar.tsv order): " + ", ".join(f"{GL[i]} {WORDS[i]['old']}" for i in top))
    for n in names[1:]:
        ch = [f"{WORDS[i]['old']}->{NAME[layers[n][i]]}" for i in top if NAME[layers[n][i]] != WORDS[i]["old"]]
        P(f"  {n}: {len(ch)} change: {' '.join(ch)}")
    P("")
    P("THE LANGUAGE'S NAME apu pi we (apu = language, pi = OF, we = ALL)")
    for n in names:
        P(f"  {n:16} apu {NAME[layers[n][GI['OF']]]} {NAME[layers[n][GI['ALL']]]}")
    P("")
    for title, pairs in (("THE DESK ANALYSIS'S 16 MERGER PAIRS", DESK16), ("MODEL V2'S MOST ROBUSTLY DANGEROUS SHORT PAIRS", ROBUST13)):
        P(f"{title}: forms, symmetric confusion % (v2 best / worst v2 variant), merger, shared position")
        for g1, g2 in pairs:
            i, j = GI[g1], GI[g2]
            row = f"  {g1 + '/' + g2:22}{'shared' if SHARED[i, j] else 'apart':7}"
            for n in names:
                f, b, w, m = pair_line(layers[n], i, j)
                row += f" | {n}: {f:10} {b:4.1f}/{w:4.1f}{' ' + m if m else ''}"
            P(row)
        P("")
    for n in names[1:]:
        a = layers[n]
        P(f"LAYER {n}: closest shared-position pairs (by worst v2 variant, symmetric %)")
        rows = []
        for i, j in itertools.combinations(range(N), 2):
            if SHARED[i, j]:
                b, w = sym(a, i, j)
                rows.append((w, b, i, j))
        for w, b, i, j in sorted(rows, reverse=True)[:12]:
            P(f"  {NAME[a[i]]:>4}~{NAME[a[j]]:<4} {GL[i]}/{GL[j]:12} best {b:4.1f}  worst {w:4.1f}  (feature distance {FD[a[i], a[j]]})")
        jd = junc_costs(a, detail=True)[VNAMES.index("best")]
        k = np.argsort(-jd)[:6]
        P("  top junction risks (bigram, v2 best, weighted): " + "; ".join(
            f"{NAME[a[ADJ_A[x]]]} {NAME[a[ADJ_B[x]]]} ({GL[ADJ_A[x]]} {GL[ADJ_B[x]]}) {jd[x]:.4f}" for x in k if jd[x] > 0) or "none")
        P("  operators to rename (first syllable = a word sharing the operator's position): " + ("; ".join(ops_to_rename(a)) or "none"))
        dc = digit_clash(a)
        P(f"  content words (loans exempt) that would begin with a digit syllable (rule 4; re-formed in the placement): {len(dc)} {' '.join(dc[:20])}")
        off = [f"{GL[i]}={NAME[a[i]]}" for i in range(N) if OFFENSIVE[a[i]]]
        P(f"  C3 tie-break matches (offensive.matches): {len(off)}: {' '.join(off)}")
        one = [f"{NAME[a[i]]}~{NAME[a[j]]}" for i, j in itertools.combinations(range(N), 2) if SHARED[i, j] and ONE_FEATURE[a[i], a[j]]]
        P(f"  shared pairs differing by one feature: {len(one)}: {' '.join(one)}")
        P(f"  rule violations: {violations(a) or 'none'}")
        P("")
    P("OLD LAYER: rule violations under the new position table")
    for v in violations(layers["old"]):
        P(f"  {v}")
    P("  operators to rename today: " + ("; ".join(ops_to_rename(layers["old"])) or "none"))
    open(os.path.join(HERE, "results.txt"), "w").write("\n".join(out) + "\n")
    with open(os.path.join(HERE, "forms.tsv"), "w") as fh:
        fh.write("gloss\tclass\tfreq\t" + "\t".join(names) + "\n")
        for i in range(N):
            fh.write(f"{GL[i]}\t{WORDS[i]['cls']}\t{FREQ[i]:g}\t" + "\t".join(NAME[layers[n][i]] for n in names) + "\n")
    print("\n".join(out))


def positions_md(argv):
    """positions.md: the named position table, the measured substitution relation and the adjacency counts."""
    fits, ctx = SUBCOUNT
    f = lambda g: f"{g} **{OLD_FORM[g]}**" if OLD_FORM.get(g) else g
    out = ["# Position table (generated by `rebuild.py positions`)", "",
           "## 1. Named positions (reference + formal grammar)", "",
           "Words in the same row share a position. A word can stand in several rows. Operators are listed for the operator rule only.", "",
           "| position | source (reference rule; GF category) | short words | two-syllable operators |", "|---|---|---|---|"]
    for name, src, ws, ops in POSITIONS:
        out.append(f"| {name} | {src} | {', '.join(f(w) for w in ws)} | {', '.join(ops)} |")
    iu = np.triu_indices(N, 1)
    out += ["", "## 2. Measured: who can replace whom (GF substitution, `positions.py`)", "",
            f"In {sum(1 for _ in open(os.path.join(HERE, 'frames.txt'))) - 1} parsed frames (reference examples and UDHR sentences), each short word was replaced by every other "
            "short word and re-parsed. A pair shares a position if either replaces the other in at least one frame with a full-sentence "
            f"reading. Result: {GF_SHARED[iu].sum()} of {N * (N - 1) // 2} pairs (MODMOD, ENDEAR: hand frames in `modmod.tsv`, `endear.tsv`). Together with "
            f"section 1: {SHARED[iu].sum()} pairs. The hard rule (no merger) applies to all of them; the confusion cost weighs each "
            "pair by its pooled substitution share (how often the swap still parses).", "",
            f"Per word: corpus contexts (frames where it stands), how many words share a position with it (of the other {N - 1}), and the words that never do.", "",
            "| word | contexts | shares with | never shares with |", "|---|---|---|---|"]
    for i in sorted(range(N), key=lambda i: -SHARED[i].sum()):
        never = [GL[j] for j in range(N) if j != i and not SHARED[i, j]]
        out.append(f"| {f(GL[i])} | {ctx.get(GL[i], 0) if GL[i] not in NEW else str(MODMOD_FRAMES if GL[i] == 'MODMOD' else ENDEAR_FRAMES) + ' frames'} | {SHARED[i].sum()} | {', '.join(never) if len(never) < 40 else str(len(never)) + ' words'} |")
    out += ["", "Operators: short words that can stand where each operator stands (GF substitution plus section 1).", ""]
    for o in OPERATORS:
        out.append(f"- **{o}** (first syllable **{NAME[OP_FIRST[o]]}**): {len(OP_SHARED.get(o, ()))} words")
    out += ["", "## 3. Next to each other (corpus bigrams, no pause between)", "",
            f"Short word + short word, counts in the reference examples and the UDHR translation (`adjacency.tsv`, all {len(ADJ)} pairs). Top 40:", ""]
    out.append(", ".join(f"{f(GL[a])} {f(GL[b])} {int(round(w / ADJ_W.min()))}" for a, b, w in sorted(ADJ, key=lambda x: -x[2])[:40]))
    open(os.path.join(HERE, "positions.md"), "w").write("\n".join(out) + "\n")
    print("wrote positions.md")


def arg(argv, name, default):
    return argv[argv.index(name) + 1] if name in argv else default


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "full":
        full(sys.argv[2:])
    elif cmd == "positions":
        positions_md(sys.argv[2:])
    elif cmd == "report":
        report(sys.argv[2:])
    elif cmd == "patch":
        patch(sys.argv[2:])
    elif cmd == "reopt":
        reopt(sys.argv[2:])
    elif cmd == "score":
        score(sys.argv[2:])
    elif cmd == "score-old":
        a = old_assign()
        print("old layer, MODMOD ->", NAME[a[GI["MODMOD"]]], "ENDEAR ->", NAME[a[GI["ENDEAR"]]], "robust", cvar(sum(totals(a))), penalties(a, *PEN)[1])
        print("\n".join(map(str, violations(a))))

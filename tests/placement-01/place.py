"""Joint placement of the final concept list (tests/conceptlist-01/concepts.tsv) on mishearing model v2.

Task: PROMPT.md here; method and choices: README.md here ("added" marks my choices).
Proposals only: reads data/ and tests/, writes only into this folder.

  python3 place.py medians            # random-lexicon medians per variant (normalisation) -> state/medians.json
  python3 place.py start              # A: today's valid roots kept, the rest added one at a time -> state/A.json
  python3 place.py descend [SEED]     # C: everything re-placed by coordinate descent from A -> state/C-SEED.json
  python3 place.py report STATE       # numbers, forms.tsv, report.txt

Every long step writes its state atomically (tmp file + rename) and resumes from it.

Objective (rule 1, design log 2026-10-13/15): per model variant v (confusion2.variants(), 48),
  conf_v = sum_{i != j, same length} W_ij f_i P_v(i heard as j)
  P_v(i -> j) = S_v,initial[i1, j1] * prod_k S_v,internal[ik, jk]
the robust score R = mean over the worst quarter of variants (12 of 48) of conf_v / med_v, med_v = the
variant's median conf over random lexicons (every root at a random valid two-syllable form; loans and
operators at their forms). Placement minimises
  J = med_best * R + EFFORT * sum_i f_i (length_i - 2)
(added: med_best, the best-estimate variant's random median, puts R back into the units words.py's
effort term was set in, so the length trade-off keeps its meaning).
W: same field x3, antonym x30, any pair with a number word x10 (placement.py, words.py). f: TIER_FREQ.
"""
import csv, json, math, os, random, re, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import words as W
import offensive
import confusion2 as M2
from build import TIER_FREQ, EFFORT

INV, SYL, IDX = W.INV, W.SYL, W.IDX
NS = len(SYL)
STATE = os.path.join(HERE, "state")
os.makedirs(STATE, exist_ok=True)
assert [o.replace("j", "y") + v + c for o, v, c in M2.SYLLABLES] == SYL  # same syllable indexing

FIXED_OPS = set("genso wanme inwun wemen konsin buntu tason nedin mesun manni buni donon lanno anko nuwen kiyo mena".split())
HAPLO_MIN = 10  # added: a grammar word bans its syllable as a root's first syllable if it stands right before a content word >= 10 times in the corpus (bigrams.tsv; ~1% of the 930 such bigrams)
ALLOW3 = "--no3" not in sys.argv  # sensitivity run: two syllables only (added)
SUFFIX = "-no3" if not ALLOW3 else ""
TIE = W.TIE     # C3 tie-break window, words.py (2%)
K3 = 400        # added: three-syllable candidates evaluated per word, half drawn from vowel-initial open forms (the cheapest by
                # the length term), half from all valid forms; the space is sparse, so the effort term decides most of the choice


def save(name, obj):
    path = os.path.join(STATE, name)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(obj, fh)
    os.replace(tmp, path)


def load_state(name):
    path = os.path.join(STATE, name)
    return json.load(open(path)) if os.path.exists(path) else None


def tup(form):
    return tuple(W.split(form))


def show(t):
    return "".join(SYL[s] for s in t)


# ------------------------------------------------------------------------------------------ items
def parse_antonyms(cell, glosses):
    """concepts.tsv antonym cells join glosses with '; ', and some glosses contain '; ' themselves."""
    parts, out, i = cell.split("; "), [], 0
    clean = lambda s: re.sub(r"\s*\((added|decided)\)$", "", s).strip()
    while i < len(parts):
        for j in range(len(parts), i, -1):
            g = clean("; ".join(parts[i:j]))
            if g in glosses:
                out.append(g); i = j; break
        else:
            i += 1
    return out


def load_items():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "tests/conceptlist-01/concepts.tsv")), delimiter="\t"))
    items = []
    for r in rows:
        if r["route"] == "loan candidate":   # added: no form until the loan panel decides (4 rows)
            continue
        items.append({"gloss": r["concept"], "field": r["field"], "tier": int(r["tier"]), "route": r["route"],
                      "old": r["form"], "fixed": r["route"] != "root", "ant": r["antonym"]})
    for r in W.read("lexicon.tsv"):
        if r["form"] in FIXED_OPS:
            items.append({"gloss": r["gloss"], "field": r["field"], "tier": int(r["tier"]), "route": "operator",
                          "old": r["form"], "fixed": True, "ant": ""})
    for it in items:
        it["freq"] = TIER_FREQ[it["tier"]]
    return items, rows


def weights(items):
    n = len(items)
    f = np.array([it["field"] for it in items])
    Wm = np.where(f[:, None] == f[None, :], 3.0, 1.0)
    num = f == "number"
    Wm[num, :] = 10.0; Wm[:, num] = 10.0
    idx = {it["gloss"]: i for i, it in enumerate(items)}
    pairs = set()
    for l in open(os.path.join(W.DATA, "antonyms.tsv")):
        p = l.rstrip("\n").split("\t")
        if len(p) == 2 and p[0] in idx and p[1] in idx:
            pairs.add(frozenset((idx[p[0]], idx[p[1]])))
    for i, it in enumerate(items):
        if it["ant"]:
            for g in parse_antonyms(it["ant"], idx):
                pairs.add(frozenset((i, idx[g])))
    for p in pairs:
        if len(p) == 2:
            a, b = tuple(p)
            Wm[a, b] = Wm[b, a] = 30.0
    np.fill_diagonal(Wm, 0.0)
    return Wm.astype(np.float32), sorted(tuple(sorted(p)) for p in pairs if len(p) == 2)


ITEMS, CROWS = load_items()
N = len(ITEMS)
FREQ = np.array([it["freq"] for it in ITEMS])
WM, ANT_PAIRS = weights(ITEMS)
MOVABLE = [i for i, it in enumerate(ITEMS) if not it["fixed"]]

# ------------------------------------------------------------------------------------------ rules
GRAM = W.read("grammar.tsv")
DIGITS = W.digit_syllables()                        # mu ni sa de wo ma
BIG = list(csv.DictReader(open(os.path.join(HERE, "bigrams.tsv")), delimiter="\t"))
HAPLO = {IDX[r["form"]] for r in BIG if int(r["before_content"]) >= HAPLO_MIN and r["gloss"] in {g["gloss"] for g in GRAM}}
RESERVED = {INV.content_key(tup(r["form"])) for r in W.read("senary.tsv")}
HAS_ONSET = np.array([INV.syl[s][0] != "" for s in range(NS)])
FIRST_OK = np.array([s not in DIGITS and s not in HAPLO for s in range(NS)])
# juncture.py check 3: a grammar word Cn whose open form C is also a grammar word makes "Cn X" ~ "C nX" for a
# vowel-initial content word X; so X and nX must not both be content words (only if such a pair exists)
GFORMS = {g["form"] for g in GRAM}
JPAIR = any(INV.syl[IDX[f]][2] == "n" and (INV.syl[IDX[f]][0].replace("j", "y") + INV.syl[IDX[f]][1]) in GFORMS for f in GFORMS)
N_OF = {s: M2.SYL_INDEX["n", v, c] for s, (o, v, c) in enumerate(M2.SYLLABLES) if o == ""}       # onsetless -> n-onset
O_OF = {M2.SYL_INDEX["n", v, c]: M2.SYL_INDEX["", v, c] for (o, v, c) in M2.SYLLABLES if o == ""}  # n-onset -> onsetless
LEN2 = np.array([[INV.length((a, b)) - 2.0 for b in range(NS)] for a in range(NS)])

KEYS = {}


def kid(key):
    return KEYS.setdefault(key, len(KEYS))


KEY2 = np.array([[kid(INV.content_key((a, b))) for b in range(NS)] for a in range(NS)])
VALID2 = np.zeros((NS, NS), bool)
OFF2 = np.zeros((NS, NS), bool)
for a in range(NS):
    for b in range(NS):
        fm = SYL[a] + SYL[b]
        OFF2[a, b] = offensive.matches(fm)
        VALID2[a, b] = FIRST_OK[a] and HAS_ONSET[b] and not offensive.blocked(fm) and INV.content_key((a, b)) not in RESERVED


def valid3(t):
    fm = show(t)
    return (FIRST_OK[t[0]] and HAS_ONSET[t[1]] and HAS_ONSET[t[2]] and not offensive.blocked(fm)
            and INV.content_key(t) not in RESERVED)


def pool3(seed=5, n=600000):
    """Valid three-syllable forms (a random sample of the ~2.3M), as arrays: forms, key ids, length - 2,
    offensive match, juncture-relevant first syllable (onsetless or n-onset), vowel-initial-open flag."""
    rng = np.random.default_rng(seed)
    a = rng.integers(0, NS, n); b = rng.integers(0, NS, n); c = rng.integers(0, NS, n)
    vo = [s for s in range(NS) if INV.syl[s][0] == "" and INV.syl[s][2] == ""]
    a[: n // 4] = rng.choice(vo, n // 4)                     # oversample V.CV.CV (cheapest lengths)
    ok = FIRST_OK[a] & HAS_ONSET[b] & HAS_ONSET[c]
    out = [t for t in dict.fromkeys(zip(a[ok].tolist(), b[ok].tolist(), c[ok].tolist())) if valid3(t)]
    F = np.array(out)
    K = np.array([kid(INV.content_key(t)) for t in out])
    L = np.array([INV.length(t) - 2.0 for t in out])
    OFF = np.array([offensive.matches(show(t)) for t in out])
    JR = np.array([(t[0] in O_OF) or (t[0] in N_OF) for t in out])
    VOP = np.array([t[0] in vo for t in out])
    return F, K, L, OFF, JR, VOP


# ------------------------------------------------------------------------------------------ model
VARIANTS = M2.variants()
NV = len(VARIANTS)
TOPQ = int(math.ceil(0.25 * NV))
_models = [M2.Model(p) for _, p in VARIANTS]
S0 = np.stack([m.S_initial for m in _models]).astype(np.float32)   # (V, 140, 140) first syllable
S1 = np.stack([m.S_internal for m in _models]).astype(np.float32)  # later syllables
del _models


def conf_total(forms, items_idx=None, Wm=None, freq=None):
    """conf_v (V,) of a whole lexicon. forms: list of tuples (None = absent)."""
    Wm = WM if Wm is None else Wm
    freq = FREQ if freq is None else freq
    out = np.zeros(NV)
    ix = [i for i in range(len(forms)) if forms[i] is not None]
    lens = {}
    for i in ix:
        lens.setdefault(len(forms[i]), []).append(i)
    for L, g in lens.items():
        if len(g) < 2:
            continue
        g = np.array(g)
        F = np.array([forms[i] for i in g])
        Wf = (Wm[np.ix_(g, g)] * freq[g][:, None]).astype(np.float32)
        for v in range(NV):
            P = S0[v][np.ix_(F[:, 0], F[:, 0])]
            for k in range(1, L):
                P = P * S1[v][np.ix_(F[:, k], F[:, k])]
            out[v] += float((P * Wf).sum(dtype=np.float64))
    return out


def pair_matrix(forms, v):
    """P[i, j] under variant v, same-length words, diagonal 0."""
    n = len(forms)
    P = np.zeros((n, n), np.float32)
    lens = {}
    for i, f in enumerate(forms):
        lens.setdefault(len(f), []).append(i)
    for L, g in lens.items():
        g = np.array(g)
        F = np.array([forms[i] for i in g])
        Q = S0[v][np.ix_(F[:, 0], F[:, 0])]
        for k in range(1, L):
            Q = Q * S1[v][np.ix_(F[:, k], F[:, k])]
        P[np.ix_(g, g)] = Q
    np.fill_diagonal(P, 0)
    return P


def cvar(x):
    return np.sort(x)[::-1][:TOPQ].mean()


# ------------------------------------------------------------------------------------------ medians
def random_forms(rng, base, movable, taken_keys):
    forms = list(base)
    taken = set(taken_keys)
    cand = np.argwhere(VALID2)
    for i in movable:
        while True:
            a, b = cand[rng.integers(len(cand))]
            k = KEY2[a, b]
            if k not in taken:
                taken.add(k); forms[i] = (int(a), int(b)); break
    return forms


def _med_worker(args):
    seed, which = args
    os.environ["OMP_NUM_THREADS"] = "1"
    rng = np.random.default_rng(seed)
    if which == "after":
        base = [tup(it["old"]) if it["fixed"] else None for it in ITEMS]
        taken = {kid(INV.content_key(f)) for f in base if f is not None} | {kid(k) for k in RESERVED}
        return conf_total(random_forms(rng, base, MOVABLE, taken)).tolist()
    T = TODAY
    base = [tup(it["form"]) if it["fixed"] else None for it in T["items"]]
    taken = {kid(INV.content_key(f)) for f in base if f is not None} | {kid(k) for k in RESERVED}
    forms = random_forms(rng, base, [i for i, it in enumerate(T["items"]) if not it["fixed"]], taken)
    return conf_total(forms, Wm=T["W"], freq=T["freq"]).tolist()


def today():
    """Today's lexicon (data/lexicon.tsv, all 519 content words) with the same weights."""
    lex = W.read("lexicon.tsv")
    items = [{"gloss": r["gloss"], "field": r["field"], "tier": int(r["tier"]), "form": r["form"],
              "fixed": r["field"] == "loan" or r["form"] in FIXED_OPS or len(W.split(r["form"])) != 2, "ant": ""} for r in lex]
    for it in items:
        it["freq"] = TIER_FREQ[it["tier"]]
    Wt, _ = weights(items)
    return {"items": items, "W": Wt, "freq": np.array([it["freq"] for it in items]),
            "forms": [tup(it["form"]) for it in items]}


TODAY = today()
NDRAW = 200  # added: random lexicons per median (shortwords-03 used 400 one-syllable layers; these are ~9x bigger and slower)


def cmd_medians():
    st = load_state("medians.json") or {}
    from multiprocessing import Pool
    for which in ("after", "today"):
        done = st.get(which + "_draws", [])
        todo = [(1000 * (which == "today") + s, which) for s in range(len(done), NDRAW)]
        with Pool(16) as pool:
            for k in range(0, len(todo), 32):
                done += pool.map(_med_worker, todo[k:k + 32])
                st[which + "_draws"] = done
                save("medians.json", st)
                print(f"medians {which}: {len(done)}/{NDRAW}", flush=True)
        st[which] = np.median(np.array(done), 0).tolist()
        save("medians.json", st)


MED = None


def medians(which="after"):
    st = load_state("medians.json")
    return np.array(st[which])


# ------------------------------------------------------------------------------------------ placer
class Placer:
    def __init__(self, forms):
        self.med = medians("after")
        self.mb = self.med[0]                     # "best" variant
        self.forms = list(forms)
        self.X0 = np.zeros((NV, NS, 2 * N), np.float32)
        self.X1 = np.zeros((NV, NS, 2 * N), np.float32)
        self.owner = {}                           # key id -> item
        self.occ = set()                          # exact forms
        for k in RESERVED:
            self.owner[kid(k)] = -1
        for i, f in enumerate(self.forms):
            if f is not None:
                self._put(i, f)
        self.T = conf_total(self.forms)
        self.eff = sum(EFFORT * FREQ[i] * (INV.length(f) - 2.0) for i, f in enumerate(self.forms) if f is not None)
        self.pool3 = pool3()
        self.vo_ix = np.where(self.pool3[5])[0]
        self.rng = np.random.default_rng(11)

    def _cols(self, i, f):
        if len(f) == 2:
            a, b = f
            self.X0[:, :, i] = S0[:, :, a]; self.X0[:, :, N + i] = S0[:, a, :]
            self.X1[:, :, i] = S1[:, :, b]; self.X1[:, :, N + i] = S1[:, b, :]
        else:
            self.X0[:, :, i] = 0; self.X0[:, :, N + i] = 0; self.X1[:, :, i] = 0; self.X1[:, :, N + i] = 0

    def _put(self, i, f):
        k = kid(INV.content_key(f))
        assert self.owner.get(k, i) == i, (ITEMS[i]["gloss"], show(f), self.owner.get(k))
        self.owner[k] = i
        self.occ.add(f)
        self.forms[i] = f
        self._cols(i, f)

    def _remove(self, i):
        f = self.forms[i]
        del self.owner[kid(INV.content_key(f))]
        self.occ.discard(f)
        self.forms[i] = None
        self.X0[:, :, i] = 0; self.X0[:, :, N + i] = 0; self.X1[:, :, i] = 0; self.X1[:, :, N + i] = 0

    def grid2(self, i):
        u = np.concatenate([FREQ[i] * WM[i], WM[i] * FREQ]).astype(np.float32)
        return np.matmul(self.X0 * u, self.X1.transpose(0, 2, 1))     # (V, 140, 140)

    def contrib3(self, i, cands):
        """(V, K) pair cost of word i at each three-syllable candidate against the placed 3-syllable words."""
        others = [k for k, f in enumerate(self.forms) if f is not None and len(f) == 3 and k != i]
        C = np.asarray(cands).reshape(-1, 3)
        res = np.zeros((NV, len(C)))
        if not others:
            return res
        O = np.array([self.forms[k] for k in others])
        wo = (FREQ[i] * WM[i, others]).astype(np.float32)
        wi = (WM[i, others] * FREQ[others]).astype(np.float32)
        for v in range(NV):
            a, b = S0[v], S1[v]
            out = a[C[:, :1], O[None, :, 0]] * b[C[:, 1:2], O[None, :, 1]] * b[C[:, 2:3], O[None, :, 2]]
            inn = a[O[None, :, 0], C[:, :1]] * b[O[None, :, 1], C[:, 1:2]] * b[O[None, :, 2], C[:, 2:3]]
            res[v] = out @ wo + inn @ wi
        return res

    def free2(self, i):
        taken = np.zeros(len(KEYS) + 1, bool)
        for k, o in self.owner.items():
            if o != i:
                taken[k] = True
        ok = VALID2 & ~taken[KEY2]
        if JPAIR:   # juncture.py check 3
            for f in self.occ:
                if len(f) == 2:
                    a, b = f
                    if a in O_OF:
                        ok[O_OF[a], b] = False
                    if a in N_OF:
                        ok[N_OF[a], b] = False
        return ok

    def ok3(self, i, t):
        if not valid3(t) or self.owner.get(kid(INV.content_key(t)), i) != i:
            return False
        if JPAIR:
            a = t[0]
            if a in O_OF and (O_OF[a],) + t[1:] in self.occ:
                return False
            if a in N_OF and (N_OF[a],) + t[1:] in self.occ:
                return False
        return True

    def best(self, i, allow3=None):
        """Best form for movable word i given the others: (form, marginal J). Word i must be removed."""
        allow3 = ALLOW3 if allow3 is None else allow3
        base = self.T.copy()
        effb = self.eff
        g = self.grid2(i).astype(np.float64)                          # (V,140,140)
        new = (base[:, None, None] + g) / self.med[:, None, None]
        r = -np.partition(-new, TOPQ - 1, axis=0)[:TOPQ].mean(0)       # CVaR per cell
        J0 = self.mb * cvar(base / self.med) + effb
        marg2 = self.mb * r + effb + EFFORT * FREQ[i] * LEN2 - J0
        ok = self.free2(i)
        marg2 = np.where(ok, marg2, np.inf)
        cands = []
        flat = np.argsort(marg2, axis=None)[:200]
        for fl in flat:
            a, b = divmod(int(fl), NS)
            if not np.isfinite(marg2[a, b]):
                break
            cands.append((float(marg2[a, b]), (a, b)))
        best2 = cands[0][0]
        if allow3 and best2 > EFFORT * FREQ[i] * 0.9:   # a 3-syllable form costs at least this much effort
            F3, K3k, L3, OFF3, JR3, VOP3 = self.pool3
            vo_ix, all_ix = self.vo_ix, len(F3)
            pick = np.concatenate([self.rng.choice(vo_ix, K3 // 2, replace=False), self.rng.choice(all_ix, K3 // 2, replace=False)])
            taken = np.zeros(len(KEYS) + 1, bool)
            for k, o in self.owner.items():
                if o != i:
                    taken[k] = True
            pick = pick[~taken[K3k[pick]]]
            pick = np.array([p for p in pick if not JR3[p] or self.ok3(i, tuple(F3[p]))], int)
            forms3 = [tuple(int(x) for x in F3[p]) for p in pick]
            lens3 = L3[pick]
            cur = self.forms_prev.get(i) if hasattr(self, "forms_prev") else None
            if cur is not None and len(cur) == 3:
                forms3.append(cur); lens3 = np.append(lens3, INV.length(cur) - 2.0)
            c3 = self.contrib3(i, forms3)                               # (V,K)
            new3 = (base[:, None] + c3) / self.med[:, None]
            r3 = -np.partition(-new3, TOPQ - 1, axis=0)[:TOPQ].mean(0)
            m3 = self.mb * r3 + effb + EFFORT * FREQ[i] * lens3 - J0
            for k in np.argsort(m3)[:50]:
                cands.append((float(m3[k]), forms3[k]))
        cands.sort()
        lim = cands[0][0] + TIE * abs(cands[0][0])
        near = [c for c in cands if c[0] <= lim]
        clean = [c for c in near if not (OFF2[c[1]] if len(c[1]) == 2 else offensive.matches(show(c[1])))]
        m, f = (clean or near)[0]
        return f, m, g

    def place(self, i, f, g=None):
        """Put word i (removed) at f, updating totals."""
        if len(f) == 2:
            if g is None:
                g = self.grid2(i).astype(np.float64)
            add = g[:, f[0], f[1]]
        else:
            add = self.contrib3(i, [f])[:, 0]
        self.T = self.T + add
        self.eff += EFFORT * FREQ[i] * (INV.length(f) - 2.0)
        self._put(i, f)

    def take_out(self, i):
        f = self.forms[i]
        if len(f) == 2:
            g = self.grid2(i).astype(np.float64)
            sub = g[:, f[0], f[1]]
        else:
            sub = self.contrib3(i, [f])[:, 0]
        self.T = self.T - sub
        self.eff -= EFFORT * FREQ[i] * (INV.length(f) - 2.0)
        self._remove(i)
        return f

    def J(self):
        return self.mb * cvar(self.T / self.med) + self.eff

    def R(self):
        return cvar(self.T / self.med)


def ok_today(f, owner, occ):
    """Can today's form stay under the new rules? (first syllable, onset, offensive, reserved, key free)"""
    if len(f) == 2 and not VALID2[f]:
        return False
    if len(f) == 3 and not valid3(f):
        return False
    if kid(INV.content_key(f)) in owner:
        return False
    if JPAIR:
        a = f[0]
        if (a in O_OF and (O_OF[a],) + f[1:] in occ) or (a in N_OF and (N_OF[a],) + f[1:] in occ):
            return False
    return True


def cmd_start():
    st = load_state(f"A{SUFFIX}.json")
    if st and st.get("done"):
        print("A done"); return
    forms = [tup(it["old"]) if it["fixed"] else None for it in ITEMS]
    owner = {kid(k): -1 for k in RESERVED}
    occ = set()
    for i, f in enumerate(forms):
        if f is not None:
            assert kid(INV.content_key(f)) not in owner, ITEMS[i]["gloss"]
            owner[kid(INV.content_key(f))] = i; occ.add(f)
    kept, todo = [], []
    for i in MOVABLE:
        it = ITEMS[i]
        if it["old"]:
            f = tup(it["old"])
            if ok_today(f, owner, occ):
                forms[i] = f; owner[kid(INV.content_key(f))] = i; occ.add(f); kept.append(i); continue
        todo.append(i)
    print(f"today's roots kept as they are: {len(kept)}; to place: {len(todo)}", flush=True)
    if st:
        forms = [tuple(f) if f else None for f in st["forms"]]
        todo = st["todo"]
    P = Placer(forms)
    t0 = time.time()
    while todo:
        i = todo[0]
        f, m, g = P.best(i)
        P.place(i, f, g)
        todo = todo[1:]
        if len(todo) % 50 == 0:
            save(f"A{SUFFIX}.json", {"forms": P.forms, "todo": todo, "done": False})
            print(f"  A: {len(todo)} left, R {P.R():.4f} J {P.J():.4f} ({time.time() - t0:.0f}s)", flush=True)
    save(f"A{SUFFIX}.json", {"forms": P.forms, "todo": [], "done": True, "R": P.R(), "J": P.J()})
    print(f"A done: R {P.R():.4f} J {P.J():.4f}")


def cmd_descend(seed, maxsweeps=12):
    start = f"A{SUFFIX}.json"
    name = f"C{SUFFIX}-{seed}.json"
    st = load_state(name)
    if st and st.get("done"):
        print(name, "done"); return
    if st:
        forms, sweep, pos, hist = [tuple(f) for f in st["forms"]], st["sweep"], st["pos"], st["hist"]
        moved = st["moved"]
    else:
        forms, sweep, pos, hist, moved = [tuple(f) for f in load_state(start)["forms"]], 0, 0, [], 0
    P = Placer(forms)
    rng = random.Random(seed)
    t0 = time.time()
    while sweep < maxsweeps:
        order = list(MOVABLE)
        random.Random(seed * 1000 + sweep).shuffle(order)
        for k in range(pos, len(order)):
            i = order[k]
            P.forms_prev = {i: P.forms[i]}
            old = P.take_out(i)
            f, m, g = P.best(i)
            P.place(i, f, g)
            if f != old:
                moved += 1
            if (k + 1) % 100 == 0:
                save(name, {"forms": P.forms, "sweep": sweep, "pos": k + 1, "hist": hist, "moved": moved, "done": False})
                print(f"  seed {seed} sweep {sweep + 1} {k + 1}/{len(order)} moved {moved} R {P.R():.4f} J {P.J():.4f} ({time.time() - t0:.0f}s)", flush=True)
        P.T = conf_total(P.forms)   # resync
        hist.append({"sweep": sweep + 1, "moved": moved, "R": P.R(), "J": P.J()})
        print(f"seed {seed} sweep {sweep + 1}: moved {moved}, R {P.R():.4f}, J {P.J():.4f}", flush=True)
        sweep += 1; pos = 0
        done = moved == 0
        moved = 0
        save(name, {"forms": P.forms, "sweep": sweep, "pos": 0, "hist": hist, "moved": 0, "done": done})
        if done:
            break
    st = load_state(name); st["done"] = True; save(name, st)


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "medians":
        cmd_medians()
    elif cmd == "start":
        cmd_start()
    elif cmd == "descend":
        cmd_descend(int([a for a in sys.argv[2:] if a.isdigit()][0]) if [a for a in sys.argv[2:] if a.isdigit()] else 1)
    elif cmd == "info":
        print(N, "items;", len(MOVABLE), "movable;", len(ANT_PAIRS), "antonym pairs;", NV, "variants; HAPLO", sorted(SYL[s] for s in HAPLO),
              "; JPAIR", JPAIR, "; valid 2-syll forms", int(VALID2.sum()))

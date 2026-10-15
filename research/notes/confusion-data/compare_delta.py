"""Listener variants built from a study's change (confusion-data.md §8.5, §9.5): compare the transferred
patterns ("av", "lp" in tools/confusion2.py) with mix4 (best) and with the study patterns used directly
("av-direct", "lp-direct"). Read-only.

Prints, at best parameters with no listener groups, inside a word (as confusion2's self-check):
  - the ratio cond/base the study gives each pair, with the floor (both directions averaged)
  - the consonant pairs that move most from best under each transferred variant, with the direct value
  - mean confusion over groups of pairs (what seeing the lips or losing the highs should change)
  - each consonant's error under best, transferred and direct
  - how the top pairs move with the floor (0.005, 0.01, 0.02)
  - the short words' top 10 under best, transferred and direct (tests/confusion-v2 word list; these
    with the listener groups at their best shares, as tests/confusion-v2/check.py ranks them)

  python3 compare_delta.py
"""
import csv, os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import confusion2 as M2

CONS, OI = M2.CONS, M2.OI
PAIRS = [(a, b) for i, a in enumerate(CONS) for b in CONS[i + 1:]]
bp = M2.best_params()
E = bp["E_C"]
om = lambda pat: M2.onset_matrix(M2.no_groups(dict(bp, C_pattern=pat)), "internal")
sp = lambda X, a, b: 100 * (X[OI[a], OI[b]] + X[OI[b], OI[a]]) / 2
best = om("mix4")

# short words, as tests/confusion-v2/check.py
def read(name):
    with open(os.path.join(ROOT, "data", name)) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))
def split(form):
    parts = re.findall(r"[^aeiou]?[aeiou](?:n(?![aeiou]))?", form)
    return tuple(M2.IDX[p] for p in parts)
SHORT = [(g["gloss"], g["form"]) for g in read("grammar.tsv")] + [
    (f"digit{r['value']}", r["form"]) for r in read("numbers.tsv") if r["kind"] == "digit" and len(split(r["form"])) == 1]
words = [split(f) for _, f in SHORT]

def short_top(pat, n=10):
    """The variant itself (best parameters, listener groups at their shares), as check.py ranks it."""
    P = M2.Model(dict(bp, C_pattern=pat)).word_matrix(words)
    Q = (P + P.T) / 2
    iu = np.triu_indices(len(words), 1)
    x = Q[iu]
    return [(SHORT[iu[0][k]][1], SHORT[iu[1][k]][1], 100 * x[k]) for k in np.argsort(-x)[:n]]

LIPS = set("pbmf")
INSIDE = set("tdnslkgj")  # w left out (rounded lips, partly visible)
GROUPS = {
    "av": {"lips differ (one of p b m f, other t d n s l k g j)": [(a, b) for a, b in PAIRS if (a in LIPS) != (b in LIPS) and "w" not in (a, b)],
           "lips vs lip and teeth (p-f, b-f)": [("p", "f"), ("b", "f")],
           "same lips, nasality (b-m, p-m)": [("b", "m"), ("p", "m")],
           "both inside the mouth (t d n s l k g j)": [(a, b) for a, b in PAIRS if a in INSIDE and b in INSIDE],
           "voicing p-b t-d k-g": [("p", "b"), ("t", "d"), ("k", "g")]},
    "lp": {"f-s": [("f", "s")], "t-p, t-k (t's burst)": [("p", "t"), ("t", "k")], "p-k": [("p", "k")],
           "voiced stop place b-d b-g d-g": [("b", "d"), ("b", "g"), ("d", "g")],
           "f-p, f-b": [("f", "p"), ("f", "b")], "s-t": [("s", "t")],
           "voicing p-b t-d k-g": [("p", "b"), ("t", "d"), ("k", "g")], "m-n": [("m", "n")]},
}

for name, (base, cond) in M2.DELTAS.items():
    B, C = M2._source(base, E), M2._source(cond, E)
    X, D = om(name), om(name + "-direct")
    print("=" * 100)
    print(f"{name}: {cond} vs {base}, level-matched to E = {E}; floor {M2.DELTA_FLOOR}")
    miss = [c for c in CONS if np.isnan(B[OI[c], OI[c]])]
    same = all(np.isclose(sp(X, a, b), sp(best, a, b)) for a, b in PAIRS if a in miss or b in miss)
    print(f"  consonants the study lacks: {' '.join(miss)}; every pair with one of them equals best: {same}")
    print(f"  {'pair':6}{'base':>7}{'cond':>7}{'ratio':>7}{'best':>7}{name:>7}{'direct':>8}   (percent; ratio = (cond+floor)/(base+floor), mean of both directions)")
    rows = sorted(PAIRS, key=lambda q: -abs(sp(X, *q) - sp(best, *q)))
    for a, b in rows[:12]:
        r = [(C[OI[x], OI[y]] + M2.DELTA_FLOOR) / (B[OI[x], OI[y]] + M2.DELTA_FLOOR) for x, y in ((a, b), (b, a))]
        rs = f"{np.mean(r):7.2f}" if not np.isnan(r).any() else "      -"
        bs = f"{sp(B, a, b):7.1f}" if not np.isnan(sp(B, a, b)) else "      -"
        cs = f"{sp(C, a, b):7.1f}" if not np.isnan(sp(C, a, b)) else "      -"
        print(f"  {a}-{b:4}{bs}{cs}{rs}{sp(best, a, b):7.1f}{sp(X, a, b):7.1f}{sp(D, a, b):8.1f}")
    rows_d = sorted(PAIRS, key=lambda q: -abs(sp(D, *q) - sp(best, *q)))
    print("  direct, 5 pairs that move most from best: " + ", ".join(
        f"{a}-{b} {sp(best, a, b):.1f} -> {sp(D, a, b):.1f} [{name} {sp(X, a, b):.1f}]" for a, b in rows_d[:5]))
    print(f"  groups, mean pair confusion (percent): {'best':>6}{name:>6}{'direct':>8}")
    for g, prs in GROUPS[name].items():
        m = lambda X: np.mean([sp(X, a, b) for a, b in prs])
        print(f"    {g:52}{m(best):6.2f}{m(X):6.2f}{m(D):8.2f}")
    print("  row error (percent):")
    for lab, M in (("best", M2.pattern("mix4", E)), (name, M2.pattern(name, E)), ("direct", M2.pattern(name + "-direct", E))):
        print(f"    {lab:7}" + " ".join(f"{c}:{100 * (1 - M[OI[c], OI[c]]):4.1f}" for c in CONS))
    print("  floor sensitivity, the same 5 pairs:")
    for fl in (0.005, 0.01, 0.02):
        T = M2._transfer(M2.pattern("mix4", E), B, C, fl)
        print(f"    floor {fl:<6}" + ", ".join(f"{a}-{b} {sp(T, a, b):.1f}" for a, b in rows[:5]))
    print("  short words, top 10 (percent, listener groups at best shares, word-initial unknown):")
    tb, tx, td = short_top("mix4"), short_top(name), short_top(name + "-direct")
    print(f"    {'best':24}{name:24}{'direct':24}")
    for (a1, b1, x1), (a2, b2, x2), (a3, b3, x3) in zip(tb, tx, td):
        print(f"    {a1 + '~' + b1 + f' {x1:.1f}':24}{a2 + '~' + b2 + f' {x2:.1f}':24}{a3 + '~' + b3 + f' {x3:.1f}':24}")

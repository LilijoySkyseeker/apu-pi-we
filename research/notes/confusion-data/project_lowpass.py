"""Low-pass (no high frequencies) consonant confusions projected onto Apupiwe's 13 consonants, with
the unfiltered condition of the same study at a similar overall error for comparison, and a
hearing-impaired matrix as a check. Uses project.py's method unchanged (read_tsv, project,
level_match: other responses dropped and rows renormalized, one factor on every row's error mass).
Sources: confusion-data.md §9.

Run: python3 project_lowpass.py [E]   (prints the comparison; writes proj-lp-*.tsv)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from project import OURS, read_tsv, project, level_match, pair, GROUPS

# Miller & Nicely 1955 file labels (th dh sh zh, v z have no Apupiwe category: dropped).
MN = {c: c for c in OURS}
MN_FILES = {
    "mn55-lp1200": "mn55-lowpass-1200.tsv",   # Table X, 200-1200 cps, +12 dB
    "mn55-lp2500": "mn55-lowpass-2500.tsv",   # Table XI, 200-2500 cps, +12 dB
    "mn55-lp5000": "mn55-lowpass-5000.tsv",   # Table XII, 200-5000 cps, +12 dB
    "mn55-n0dB": "mn55-noise-0dB.tsv",        # Table IV, 200-6500 cps, 0 dB (error level of lp2500)
    "mn55-n6dB": "mn55-noise-6dB.tsv",        # Table V, 200-6500 cps, +6 dB (error level of lp5000)
}


def trevino():
    """Trevino & Allen 2013 Table III: average the female and male token of each consonant."""
    M = read_tsv("trevino2013-HI-avg.tsv", skipcols=("sum",))
    toks = {}
    for row, _ in M:
        toks.setdefault(row.split("_")[0], set()).add(row)
    A = {}
    for c, rows in toks.items():
        for col in {b for (_, b) in M}:
            A[c, col] = sum(M.get((r, col), 0.0) for r in rows) / len(rows)
    return project(A)


def sources():
    S = {n: project(read_tsv(f, MN, ("sum",))) for n, f in MN_FILES.items()}
    S["trevino13-HI"] = trevino()
    return S


PAIRS = [("mn55-n0dB", "mn55-lp2500"), ("mn55-n6dB", "mn55-lp5000"), ("mn55-n0dB", "mn55-lp1200")]


def mean_err(P):
    st = [a for a in OURS if (a, a) in P]
    return sum(1 - P[a, a] for a in st) / len(st)


def all_pairs(Q):
    out = {}
    for i, a in enumerate(OURS):
        for b in OURS[i + 1:]:
            x = pair(Q, a, b)
            if x is not None:
                out[a, b] = x
    return out


if __name__ == "__main__":
    E = float(sys.argv[1]) if len(sys.argv) > 1 else 0.20
    S = sources()
    print("stimuli present (of 13):")
    for n, P in S.items():
        miss = [a for a in OURS if (a, a) not in P]
        print(f"  {n:14s} raw mean error {100*mean_err(P):5.1f}%  missing: {' '.join(miss) or '-'}")
    LM = {n: level_match(S[n], E)[0] for n in S}
    print(f"\ngroups, symmetric pair confusion in percent, level-matched to E={E}")
    print("group".ljust(22) + "".join(n.replace("mn55-", "").rjust(13) for n in S))
    for g, prs in GROUPS.items():
        line = g.ljust(22)
        for n in S:
            v = [pair(LM[n], a, b) for a, b in prs]; v = [x for x in v if x is not None]
            line += f"{100*sum(v)/len(v):13.2f}" if v else "-".rjust(13)
        print(line)
    for un, lp in PAIRS:
        x, y = all_pairs(LM[un]), all_pairs(LM[lp])
        rx, ry = all_pairs(S[un]), all_pairs(S[lp])
        rows = sorted(x, key=lambda k: -abs(y[k] - x[k]))
        print(f"\n{un} -> {lp}: largest changes (level-matched E={E}; raw in brackets), percent")
        for k in rows[:12]:
            print(f"  {k[0]}-{k[1]:2s} {100*x[k]:6.2f} -> {100*y[k]:6.2f}  ({100*rx[k]:5.2f} -> {100*ry[k]:5.2f})")
    # check: does the hearing-impaired pattern rise where low-pass rises?
    hi, lp, un = all_pairs(LM["trevino13-HI"]), all_pairs(LM["mn55-lp2500"]), all_pairs(LM["mn55-n0dB"])
    common = [k for k in hi if k in lp]
    print(f"\ncheck, pairs of consonants in all three (level-matched E={E}), percent; sorted by HI")
    print("  pair    HI    lp2500   n0dB")
    for k in sorted(common, key=lambda k: -hi[k])[:14]:
        print(f"  {k[0]}-{k[1]:2s} {100*hi[k]:6.2f} {100*lp[k]:7.2f} {100*un[k]:7.2f}")
    import statistics as st
    def rank(d):
        order = sorted(common, key=lambda k: d[k])
        return {k: i for i, k in enumerate(order)}
    def spearman(a, b):
        ra, rb = rank(a), rank(b)
        return st.correlation([ra[k] for k in common], [rb[k] for k in common])
    print(f"  Spearman over {len(common)} pairs: HI~lp2500 {spearman(hi, lp):.2f}, HI~n0dB {spearman(hi, un):.2f}")
    for n in S:
        with open(os.path.join(HERE, f"proj-lp-{n}.tsv"), "w") as f:
            f.write(f"# derived by project_lowpass.py (project.py's method) from the source TSV for {n}: rows/columns restricted to Apupiwe consonants, other responses dropped and rows renormalized. Not level-matched. Probabilities. Consonants not tested (l w j) have no row and get no responses.\n")
            st_ = [a for a in OURS if (a, a) in S[n]]
            f.write("sent\\heard\t" + "\t".join(OURS) + "\t(none)\n")
            for a in st_:
                f.write(a + "\t" + "\t".join(f"{S[n][a, b]:.4f}" for b in OURS + [""]) + "\n")

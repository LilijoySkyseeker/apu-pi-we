"""Audiovisual (face-to-face) consonant confusions projected onto Apupiwe's 13 consonants, with
the audio-only condition from the same study for comparison. Uses project.py's method unchanged
(read_tsv, project, level_match: other responses dropped and rows renormalized, /h/ = heard no
consonant, one factor on every row's error mass). Sources: confusion-data.md §8.

Run: python3 project_av.py [E]   (prints the comparison; writes proj-av-*.tsv)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from project import OURS, MAP_H, read_tsv, project, level_match, pair, GROUPS

# (name, file, rename, skipcols); pairs below compare the audio-only and audiovisual
# conditions of the same study.
def sources():
    ident = {c: c for c in OURS}
    vs = dict(ident, y="j", h="" if MAP_H else "?h"); vs.pop("j")   # dj = /dZ/ stays out
    S = {}
    for mod in ("AO", "AV"):
        for lvl in ("high", "low"):
            S[f"vonseth25-{mod}-{lvl}"] = project(read_tsv(f"vonseth2025-{mod}-{lvl}.tsv", vs, ("sum",)))
    for mod in ("A", "AV"):
        S[f"braida98-{mod}"] = project(read_tsv(f"braida1998-japanese-{mod}.tsv", ident))
    return S

PAIRS = [("vonseth25-AO-high", "vonseth25-AV-high"), ("vonseth25-AO-low", "vonseth25-AV-low"),
         ("braida98-A", "braida98-AV")]

# Place of articulation, to label each pair (same place = the face can't separate them).
PLACE = {"p": "bilabial", "b": "bilabial", "m": "bilabial", "f": "labiodental", "w": "labial-velar",
         "t": "alveolar", "d": "alveolar", "n": "alveolar", "s": "alveolar", "l": "alveolar",
         "k": "velar", "g": "velar", "j": "palatal"}

def kind(a, b):
    return "same place" if PLACE[a] == PLACE[b] else "place differs"

def mean_err(P):
    st = [a for a in OURS if (a, a) in P]
    return sum(1 - P[a, a] for a in st) / len(st)

if __name__ == "__main__":
    E = float(sys.argv[1]) if len(sys.argv) > 1 else 0.20
    S = sources()
    print("stimuli present (of 13):")
    for n, P in S.items():
        miss = [a for a in OURS if (a, a) not in P]
        print(f"  {n:20s} raw mean error {100*mean_err(P):5.1f}%  missing: {' '.join(miss) or '-'}")
    LM = {n: level_match(S[n], E)[0] for n in S}
    print(f"\ngroups, symmetric pair confusion in percent, level-matched to E={E}")
    print("group".ljust(22) + "".join(n.replace("vonseth25-", "vs-").rjust(13) for n in S))
    for g, prs in GROUPS.items():
        line = g.ljust(22)
        for n in S:
            v = [pair(LM[n], a, b) for a, b in prs]; v = [x for x in v if x is not None]
            line += f"{100*sum(v)/len(v):13.2f}" if v else "-".rjust(13)
        print(line)
    for ao, av in PAIRS:
        rows = []
        for i, a in enumerate(OURS):
            for b in OURS[i + 1:]:
                x, y = pair(LM[ao], a, b), pair(LM[av], a, b)
                if x is None or y is None:
                    continue
                rx, ry = pair(S[ao], a, b), pair(S[av], a, b)
                rows.append((y - x, a, b, x, y, rx, ry))
        print(f"\n{ao} -> {av}: largest changes (level-matched E={E}; raw in brackets), percent")
        for d, a, b, x, y, rx, ry in sorted(rows, key=lambda r: -abs(r[0]))[:10]:
            print(f"  {a}-{b:2s} {kind(a, b):14s} {100*x:6.2f} -> {100*y:6.2f}  ({100*rx:5.2f} -> {100*ry:5.2f})")
        print(f"  by raw change (no level matching; AV mean error is lower):")
        for d, a, b, x, y, rx, ry in sorted(rows, key=lambda r: -abs(r[6] - r[5]))[:8]:
            print(f"  {a}-{b:2s} {kind(a, b):14s} raw {100*rx:5.2f} -> {100*ry:5.2f}")
    for n in S:
        with open(os.path.join(HERE, f"proj-av-{n}.tsv"), "w") as f:
            f.write(f"# derived by project_av.py (project.py's method) from the source TSV for {n}: rows/columns restricted to Apupiwe consonants, other responses dropped and rows renormalized; column '' = /h/ responses (heard no consonant). Not level-matched. Probabilities. Consonants not tested have no row and get no responses.\n")
            st = [a for a in OURS if (a, a) in S[n]]
            f.write("sent\\heard\t" + "\t".join(OURS) + "\t(none)\n")
            for a in st:
                f.write(a + "\t" + "\t".join(f"{S[n][a, b]:.4f}" for b in OURS + [""]) + "\n")

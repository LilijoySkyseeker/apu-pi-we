"""ya~yan check (design log 2026-10-16): every single-word move of YOUKNOW, then of BEFORE, to a legal free form,
all other words fixed, scored under the default variant set. Writes yayan-moves.tsv; yayan.md reads it.

  python3 yayan.py [layer]   (default runs/sens-g-mid-lock-0.01-control-1.tsv, the adopted layer)

A move qualifies if: the moved word's form no longer differs from the other's only by a final -n (or any other
merger type); it passes hard_ok (H1-H5: onset, digit open, no shared form, no merger with a word sharing a
position, not offensive.blocked); it adds no merger-type pair with ANY short word, shared position or not
(stricter than H4: trading ya~yan for another such pair isn't a separation); robust score <= the layer's.
"""
import itertools, os, sys
import numpy as np
import rebuild as R

layer = sys.argv[1] if len(sys.argv) > 1 else "runs/sens-g-mid-lock-0.01-control-1.tsv"
a0 = R.read_layer(layer)
B, Y = R.GI["BEFORE"], R.GI["YOUKNOW"]


def all_mergers(a):
    return {(R.GL[i], R.GL[j]) for i, j in itertools.combinations(range(R.N), 2) if R.MERGE[a[i], a[j]]}


def shared_mergers(a):
    return {(R.GL[i], R.GL[j]) for i, j in R.merger_edges(a)}


base = R.cvar(sum(R.totals(a0)))
base_pen = R.penalties(a0, *R.PEN)[1]
m0, sm0 = all_mergers(a0), shared_mergers(a0)
print(f"BASE {layer} variants={R.VARSET} n={R.NV} robust {base:.4f} penalties {base_pen} "
      f"merger-type pairs {len(m0)} (shared-position {len(sm0)}) objective {R.objective_of(a0):.4f}")
rows = []
for w, other in ((Y, B), (B, Y)):
    for s in range(R.NS):
        if s == a0[w]:
            continue
        a = a0.copy(); a[w] = s
        legal = R.hard_ok(a0, w, s)
        why = []
        if not R.HAS_ONSET[s]: why.append("no onset")
        if R.BLOCKED[s]: why.append("blocked")
        if (np.delete(a0, w) == s).any(): why.append("taken by " + R.GL[int(np.where(a0 == s)[0][0])])
        elif not legal and R.HAS_ONSET[s] and not R.BLOCKED[s]: why.append("shared-position merger")
        sep = R.merger(s, a0[other]) is None
        new = sorted(all_mergers(a) - m0)
        sc = R.cvar(sum(R.totals(a)))
        pen = R.penalties(a, *R.PEN)[1]
        q = legal and sep and not new and sc <= base + 1e-12
        rows.append((R.GL[w], R.NAME[a0[w]], R.NAME[s], legal, ";".join(why), sep,
                     " ".join(f"{x}~{y}" for x, y in new), sc, pen, R.objective_of(a), q))
rows.sort(key=lambda r: r[7])
with open(os.path.join(R.HERE, "yayan-moves.tsv"), "w") as fh:
    fh.write(f"# yayan.py on {layer}; variants={R.VARSET} ({R.NV}); base robust {base:.4f} penalties {base_pen}\n")
    fh.write("word\tfrom\tto\thard_ok\twhy_not\tseparates\tnew_merger_pairs\trobust\tpenalties(off,1feat,op)\tobjective\tqualifies\n")
    for r in rows:
        fh.write("\t".join([r[0], r[1], r[2], str(r[3]), r[4], str(r[5]), r[6], f"{r[7]:.4f}",
                            ",".join(map(str, r[8])), f"{r[9]:.4f}", str(r[10])]) + "\n")
legal = [r for r in rows if r[3]]
print(f"moves {len(rows)}, legal {len(legal)}, legal+separating {sum(r[5] for r in legal)}, "
      f"+no new merger {sum(1 for r in legal if r[5] and not r[6])}, qualifying {sum(r[10] for r in rows)}")
for r in [r for r in legal if r[5]][:25]:
    print(f"  {r[0]:8} {r[1]}->{r[2]:4} robust {r[7]:.4f} ({r[7] - base:+.4f}) pen {r[8]} new {r[6] or '-'} {'QUALIFIES' if r[10] else ''}")

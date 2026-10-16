"""Check (added): what does it cost to keep today's form for the frequent roots the descent moved without
being forced to? Restores each unforced moved root of tier >= T to today's form when that form is still
free (key and juncture), in order of tier, and reports R and J before/after. Analysis only.
  python3 keepcheck.py STATE [T]
"""
import sys
import place as P

name = sys.argv[1]; T = int(sys.argv[2]) if len(sys.argv) > 2 else 4
A = [tuple(f) for f in P.load_state("A-no3.json" if "no3" in name else "A.json")["forms"]]
pl = P.Placer([tuple(f) for f in P.load_state(name)["forms"]])
R0, J0 = pl.R(), pl.J()
order = sorted([i for i in P.MOVABLE if P.ITEMS[i]["old"] and P.ITEMS[i]["tier"] >= T], key=lambda i: -P.ITEMS[i]["tier"])
rows = []
for i in order:
    old = P.tup(P.ITEMS[i]["old"])
    if pl.forms[i] == old or A[i] != old:     # not moved, or forced to move
        continue
    cur = pl.take_out(i)
    k = P.kid(P.INV.content_key(old))
    if pl.owner.get(k, i) == i and P.ok_today(old, {kk: o for kk, o in pl.owner.items() if o != i}, pl.occ):
        pl.place(i, old); rows.append((pl.J() - J0, i)); pl.take_out(i)
    else:
        rows.append((None, i))
    pl.place(i, cur)
ok = sorted(r for r in rows if r[0] is not None)
print(f"{name}: {len(rows)} unforced moves of tier >= {T}; {len(ok)} could go back alone (others: form now taken). "
      f"Cost of putting each back alone, as % of J ({J0:.3f}):")
print("  " + ", ".join(f"{P.ITEMS[i]['gloss'].split(',')[0].split(';')[0]} {P.ITEMS[i]['old']}->{P.show(pl.forms[i])} {100 * d / J0:+.2f}%" for d, i in ok))
print("  taken: " + ", ".join(f"{P.ITEMS[i]['gloss'].split(',')[0]} {P.ITEMS[i]['old']}" for d, i in rows if d is None))

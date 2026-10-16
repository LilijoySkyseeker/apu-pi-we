"""Compare the rerun's substitution relation with the dry run's (shortwords-02), after the positions.py fix.
  python3 compare_positions.py
"""
import collections, csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
OLD = os.path.join(HERE, "..", "shortwords-02")


def load(d):
    rows = list(csv.DictReader(open(os.path.join(d, "substitution.tsv")), delimiter="\t"))
    ctx = {r["glossA"]: int(r["contexts_A"]) for r in rows}
    shared = {frozenset((r["glossA"], r["glossB"])) for r in rows if int(r["fits_full"]) and r["glossA"] != "operator"}
    fits = sum(int(r["fits_full"]) for r in rows if r["glossA"] != "operator")
    anyf = sum(int(r["fits_any"]) for r in rows if r["glossA"] != "operator")
    return ctx, shared, fits, anyf, len(rows)


o, n = load(OLD), load(HERE)
print(f"rows {o[4]} -> {n[4]}; words with contexts {len(o[0])} -> {len(n[0])}; total contexts {sum(o[0].values())} -> {sum(n[0].values())}")
print(f"substitutions that parse (full) {o[2]} -> {n[2]}; any parse {o[3]} -> {n[3]}")
print(f"GF-shared pairs {len(o[1])} -> {len(n[1])}; lost {len(o[1] - n[1])}; gained {len(n[1] - o[1])}")
print("words that lost all contexts:", sorted(set(o[0]) - set(n[0])))
print("lost pairs (first 40):", sorted("~".join(sorted(p)) for p in o[1] - n[1])[:40])
print("gained pairs:", sorted("~".join(sorted(p)) for p in n[1] - o[1]))
for f in ("adjacency.tsv",):
    a = {(r["A"], r["B"]): int(r["count"]) for r in csv.DictReader(open(os.path.join(OLD, f)), delimiter="\t")}
    b = {(r["A"], r["B"]): int(r["count"]) for r in csv.DictReader(open(os.path.join(HERE, f)), delimiter="\t")}
    print(f"{f}: pairs {len(a)} -> {len(b)}; tokens {sum(a.values())} -> {sum(b.values())}; new {sorted(set(b) - set(a))}; gone {sorted(set(a) - set(b))}")
fo = open(os.path.join(OLD, "frames.txt")).read().splitlines()[1:]
fn = open(os.path.join(HERE, "frames.txt")).read().splitlines()[1:]
print(f"frames {len(fo)} -> {len(fn)}; new {len(set(fn) - set(fo))}; gone {len(set(fo) - set(fn))}")
for s in sorted(set(fo) - set(fn))[:10]:
    print("  gone:", s)
for s in sorted(set(fn) - set(fo))[:10]:
    print("  new:", s)

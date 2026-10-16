"""Summaries for the rerun's checks (README.md). Reads layer files and logs in this folder; writes nothing.

  python3 checks.py agree FILE...          pairwise agreement of forms between layers (seed runs of one option)
  python3 checks.py diff A B               words whose form differs between two layers
  python3 checks.py sens NAME              sensitivity table from logs/sens-NAME-*.log
  python3 checks.py drop NAME              drop-test table from logs/drop-NAME-*.log
"""
import csv, glob, itertools, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def layer(f):
    path = f if os.path.isabs(f) else os.path.join(HERE, f)
    rows = csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t")
    return {r["gloss"]: r["new"] for r in rows}


def agree(files):
    ls = [layer(f) for f in files]
    xs = [sum(a[g] == b[g] for g in a) / len(a) for a, b in itertools.combinations(ls, 2)]
    print(f"{len(ls)} layers, {len(xs)} pairs: mean agreement {100 * sum(xs) / len(xs):.1f}%  "
          f"min {100 * min(xs):.1f}%  max {100 * max(xs):.1f}%")


def diff(a, b):
    A, B = layer(a), layer(b)
    d = [f"{g} {A[g]}->{B[g]}" for g in A if A[g] != B[g]]
    print(f"{len(d)} differ: {'; '.join(d)}")


def reopt_line(path):
    for line in open(path):
        if line.startswith("REOPT"):
            m = re.search(r"moved (\d+) \| objective ([\d.]+) -> ([\d.]+) \| robust ([\d.]+) -> ([\d.]+) \| (.*)", line)
            return int(m.group(1)), float(m.group(4)), float(m.group(5)), m.group(6).strip()
    return None


def sens(name):
    ctrl = [reopt_line(f) for f in sorted(glob.glob(os.path.join(HERE, f"logs/sens-{name}-control-*.log")))]
    print(f"controls (no override): moved {[c[0] for c in ctrl if c]}  " + " | ".join(c[3] for c in ctrl if c and c[3]))
    rows = []
    for f in sorted(glob.glob(os.path.join(HERE, f"logs/sens-{name}-*.log"))):
        m = re.search(rf"sens-{re.escape(name)}-(.+)-(low|high)\.log$", f)
        if not m:
            continue
        r = reopt_line(f)
        if r:
            rows.append((m.group(1), m.group(2), *r))
    rows.sort(key=lambda r: -r[2])
    for p, v, moved, r0, r1, words in rows:
        print(f"  {p:20} {v:4}  moved {moved:2d}  robust {r0:.4f} -> {r1:.4f}  {words}")


def drop(name):
    for f in sorted(glob.glob(os.path.join(HERE, f"logs/drop-{name}-*.log"))):
        r = reopt_line(f)
        if r:
            print(f"  {os.path.basename(f):32} moved {r[0]:2d}  robust {r[1]:.4f} -> {r[2]:.4f}  {r[3]}")


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    {"agree": lambda: agree(args), "diff": lambda: diff(*args), "sens": lambda: sens(*args), "drop": lambda: drop(*args)}[cmd]()

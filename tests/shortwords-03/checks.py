"""Summaries for the rerun's checks (README.md). Reads layer files and logs in this folder; writes nothing.

  python3 checks.py agree FILE...          pairwise agreement of forms between layers (seed runs of one option)
  python3 checks.py diff A B               words whose form differs between two layers
  python3 checks.py sens NAME              sensitivity table from logs/sens-NAME-*.log
  python3 checks.py drop NAME              drop-test table from logs/drop-NAME-*.log
  python3 checks.py vsctl NAME             (added) forms each sens/drop run moved relative to the control run of the same
                                           seed (sens: seed 1; drop: seeds 1-3); the annealing's own drift cancels out
  python3 checks.py rank                   (added) option ranking by robust score under each override, from sens-score.txt
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


def vsctl(name):
    ctl = {s: layer(f"runs/sens-{name}-control-{s}.tsv") for s in (1, 2, 3)}
    rows = []
    for f in sorted(glob.glob(os.path.join(HERE, f"runs/sens-{name}-*.tsv"))):
        m = re.search(rf"sens-{re.escape(name)}-(.+-(?:low|high))\.tsv$", f)
        if m:
            a = layer(f); d = [g for g in a if a[g] != ctl[1][g]]
            rows.append((len(d), m.group(1), " ".join(f"{g}:{ctl[1][g]}>{a[g]}" for g in d)))
    for n, k, w in sorted(rows, key=lambda r: -r[0]):
        print(f"  {k:26} {n:2d}  {w}")
    for vs in ("no-av", "no-lp"):
        for s in (1, 2, 3):
            f = os.path.join(HERE, f"runs/drop-{name}-{vs}-{s}.tsv")
            if os.path.exists(f):
                a = layer(f); d = [g for g in a if a[g] != ctl[s][g]]
                print(f"  drop {vs} seed {s}: {len(d)}  {' '.join(f'{g}:{ctl[s][g]}>{a[g]}' for g in d)}")


def rank():
    d = {}
    for line in open(os.path.join(HERE, "sens-score.txt")):
        p = line.split()
        d.setdefault(p[3].replace("override=", ""), []).append((float(p[5]), p[1].replace(".tsv", "")))
    base = [f for _, f in sorted(d["none"])]
    for o, v in d.items():
        order = [f for _, f in sorted(v)]
        print(f"{o:26} {'same' if order == base else 'DIFF'}  " + " < ".join(f"{f} {r:.3f}" for r, f in sorted(v)))


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    {"agree": lambda: agree(args), "diff": lambda: diff(*args), "sens": lambda: sens(*args), "drop": lambda: drop(*args),
     "vsctl": lambda: vsctl(*args), "rank": rank}[cmd]()

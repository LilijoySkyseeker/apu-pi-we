"""coverage-02: assemble walk.tsv / calibration.tsv from candidates.tsv and the hand classification in src/,
and print the per-stretch G shares.  direnv exec . python3 tests/coverage-02/assemble.py"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))


def rd(p):
    with open(os.path.join(HERE, p), encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


cand = {int(r["crank"]): r for r in rd("candidates.tsv")}


def skip_reason(r):
    st = r["status"]
    for key, why in (("roots-1500 deep", "on the list (first words)"), ("additions", "on the list (additions.tsv)"),
                     ("roots-1500", "on the list (roots-1500)"), ("root:", "existing root"),
                     ("compound:", "listed phrase"), ("cover:", "merge cover")):
        if key in st:
            return why + ": " + st
    return None


def build(manual, lo, hi, out):
    man = {int(r["crank"]): r for r in rd(manual)}
    rows, stats = [], {}
    for k in range(lo, hi + 1):
        r = cand[k]
        if k in man:
            m = man[k]
            cls, gl, note = m["class"], m["gloss_or_phrase"], m["note"]
        else:
            why = skip_reason(r)
            if why is None:
                raise SystemExit(f"unclassified rank {k} {r['canonical']}")
            cls, gl, note = "-", "", why
        name = r["canonical"] + (f" ({r['best_label']})" if r["best_label"] != r["canonical"] else "")
        rows.append([k, name, cls, gl, note])
        s = stats.setdefault((k - lo) // 100, {"n": 0, "G": 0, "altG": 0, "c": {}})
        if cls != "-":
            s["n"] += 1
            s["c"][cls] = s["c"].get(cls, 0) + 1
            if cls == "G": s["G"] += 1
            if cls == "G" or "alt:G" in note: s["altG"] += 1
    with open(os.path.join(HERE, out), "w") as f:
        f.write("rank\tconcept\tclass\tgloss_or_phrase\tnote\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")
    for i, s in sorted(stats.items()):
        a = lo + 100 * i
        print(f"{out}: {a}-{min(a + 99, hi)}  candidates {s['n']}  G {s['G']} ({100 * s['G'] / s['n']:.0f}%)"
              f"  G+alt {s['altG']} ({100 * s['altG'] / s['n']:.0f}%)  {dict(sorted(s['c'].items()))}")


build("src/calib-manual.tsv", 1143, 1242, "calibration.tsv")
build("src/walk-manual.tsv", 1243, 1442, "walk.tsv")

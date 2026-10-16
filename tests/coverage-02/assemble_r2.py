"""coverage-02 round 2: the phrase line (author 2026-10-16, decision (b)).
Applies src/r2-overrides.tsv (and src/r2-calib-overrides.tsv) on top of round 1's hand classification,
adds src/walk-r2-extra.tsv (1443-1542), writes walk-r2.tsv, calibration-r2.tsv and stretches-blind.tsv,
and prints the per-stretch G shares.  direnv exec . python3 tests/coverage-02/assemble_r2.py"""
import os
import assemble as A  # round 1 helpers (also rebuilds the round-1 files, unchanged)

HERE = A.HERE


def merged(*files):
    man = {}
    for f in files:
        for r in A.rd(f):
            man[int(r["crank"])] = r
    return man


def write_manual(man, path):
    with open(os.path.join(HERE, path), "w") as f:
        f.write("crank\tclass\tgloss_or_phrase\tnote\n")
        for k in sorted(man):
            m = man[k]
            note = m["note"]
            if m["class"] == "P" and "r2:" not in note and "world compound" not in note:
                note = (note + "; " if note else "") + "r2: P (phrase at most 3 syllables)"
            f.write(f"{k}\t{m['class']}\t{m['gloss_or_phrase']}\t{note}\n")


os.makedirs(os.path.join(HERE, "src", "r2"), exist_ok=True)
write_manual(merged("src/walk-manual.tsv", "src/r2-overrides.tsv", "src/walk-r2-extra.tsv"), "src/r2/walk.tsv")
write_manual(merged("src/calib-manual.tsv", "src/r2-calib-overrides.tsv"), "src/r2/calib.tsv")
print("--- round 2")
A.build("src/r2/calib.tsv", 1143, 1242, "calibration-r2.tsv")
A.build("src/r2/walk.tsv", 1243, 1542, "walk-r2.tsv")

with open(os.path.join(HERE, "stretches-blind.tsv"), "w") as f:
    f.write("rank\tconcept\n")
    for k in range(1243, 1443):
        r = A.cand[k]
        f.write(f"{k}\t{r['canonical']}" + (f" ({r['best_label']})" if r['best_label'] != r['canonical'] else "") + "\n")

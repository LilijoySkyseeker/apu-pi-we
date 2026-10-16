"""deeplayer-01 step 2a: one index of today's coverage, and automatic match candidates for each WOLD meaning.
Sources (read-only): data/lexicon.tsv, data/compounds.tsv, tests/coverage-01/part3/{ladder,additions}.tsv (+ pending-splits.md,
whose new roots are the additions), tests/coverage-02/candidates.tsv (status column: existing roots and merges),
tests/coverage-02/additions.tsv, tests/coverage-02 walk round 1 (walk.tsv) and round 2 (src/r2-overrides.tsv,
src/walk-r2-extra.tsv; round 2 was in progress on 2026-10-16), tests/balance-02/concepts-entrants.tsv.
Writes coverage-index.tsv and candidates.tsv (each WOLD meaning with up to 8 index hits by word overlap).
The hand sense check is src/match.tsv; this script only proposes.
direnv exec . python3 tests/deeplayer-01/build_index.py"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))


def rd(p):
    with open(os.path.join(ROOT, p)) as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


idx = []  # (source, concept, kind, detail)
for r in rd("data/lexicon.tsv"):
    idx.append(("lexicon", r["gloss"], "root", r["form"]))
for r in rd("data/compounds.tsv"):
    idx.append(("compounds", r["gloss"], "phrase", r["form"]))
for r in rd("tests/coverage-01/part3/ladder.tsv"):
    st = r["status"]
    kind = {"keep": "list", "split": "list", "grammar": "grammar"}.get(st.split(":")[0], st)
    idx.append(("ladder", r["concept"], kind, f"{st}/{r['route']} {r['note']}"[:120]))
for r in rd("tests/coverage-01/part3/additions.tsv"):
    idx.append(("additions-01", r["concept"], "list", r["reason"][:100]))
cand = {int(r["crank"]): r for r in rd("tests/coverage-02/candidates.tsv")}
for r in cand.values():
    if r["status"]:
        idx.append(("candidates-02", r["canonical"] + " | " + r["best_label"], r["status"].split(";")[0][:20], r["merge_note"][:80]))
for r in rd("tests/coverage-02/additions.tsv"):
    idx.append(("additions-02", r["concept"], "proposed:" + r["route"], r["gloss"]))
walk = {}
for r in rd("tests/coverage-02/walk.tsv"):
    walk[int(r["rank"])] = (r["concept"], r["class"], r["gloss_or_phrase"])
for f in ("tests/coverage-02/src/r2-overrides.tsv", "tests/coverage-02/src/walk-r2-extra.tsv"):
    for r in rd(f):
        k = int(r["crank"])
        walk[k] = (cand[k]["canonical"], r["class"], r["gloss_or_phrase"])
for k, (c, cl, g) in sorted(walk.items()):
    if cl in ("G", "P", "L"):
        idx.append(("walk-02", c, "walk:" + cl, g))
for r in rd("tests/balance-02/concepts-entrants.tsv"):
    idx.append(("entrants-02", r["canonical"], "entrant:" + r["judgement"], r["note (added: Claude's reading)"][:100]))

with open(os.path.join(HERE, "coverage-index.tsv"), "w") as f:
    f.write("source\tconcept\tkind\tdetail\n")
    for t in idx:
        f.write("\t".join(x.replace("\t", " ") for x in t) + "\n")

STOP = set("the a an to of or and in on be one's oneself something someone with for by at up out off as is it from".split())


def words(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP and len(w) > 1}


iw = [(words(t[1]), t) for t in idx]
ev = rd("tests/deeplayer-01/evidence.tsv")
with open(os.path.join(HERE, "candidates.tsv"), "w") as f:
    f.write("wold_id\tfield\tmeaning\thits\n")
    for e in ev:
        mw = words(e["meaning"]) | words(e["concepticon"])
        hits = [(len(mw & w), t) for w, t in iw if mw & w]
        hits.sort(key=lambda x: (-x[0], len(x[1][1])))
        h = " || ".join(f"{t[1]} [{t[0]}:{t[2]}]" for _, t in hits[:8])
        f.write(f"{e['wold_id']}\t{e['field']}\t{e['meaning']}\t{h}\n")
print(len(idx), "index rows;", len(ev), "meanings")

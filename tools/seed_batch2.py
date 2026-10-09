"""Seed batch 2 (2026-10-08): the agreed trigger fired. The first vocabulary blind test lost more
than 1 point to missing everyday words (yam, goat, rice), so the seed grows into ranks 301-650 of
data/concept-ranking.tsv, taking only concepts present in all six macro-areas with at least 10% of
each area's lineages (the weakly ordered pool, research/notes/concept-sources.md), plus the words
that test needed and paraphrase could not carry. Appends to data/concepts.tsv.

  python seed_batch2.py
"""
import csv, os
import words as W

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
ROOTS = {  # concept -> (gloss, field, antonym)
    "FRUIT": ("fruit", "nature"), "AIR": ("air", "nature"), "FOG": ("fog", "nature"),
    "LIGHTNING": ("lightning", "nature"), "LAKE": ("lake", "nature"), "ROOF": ("roof", "thing"),
    "CLIMB": ("climb", "motion"), "SPLIT": ("split", "action"), "CHEW": ("chew", "action"),
    "SQUEEZE": ("squeeze", "action"), "SCRATCH": ("scratch", "action"), "SWELL": ("swell", "action"),
    "STAB": ("stab", "action"), "STEAL": ("steal", "action"), "HUNT": ("hunt", "action"),
    "SHOOT": ("shoot", "action"), "FLOW": ("flow", "motion"), "COUNT": ("count", "mind"),
    "CHICKEN": ("chicken", "animal"), "INTESTINES": ("intestines", "body"), "FROG": ("frog", "animal"),
    "ARMPIT": ("armpit", "body"), "BASKET": ("basket", "thing"), "TURTLE": ("turtle", "animal"),
    "SPIDER": ("spider", "animal"), "SCORPION": ("scorpion", "animal"), "GRASSHOPPER": ("grasshopper", "animal"),
    "BAT": ("bat", "animal"), "CLOTHES": ("clothes", "thing"),
}
ON_DEMAND = {  # from tests/vocabulary-01: paraphrase lost the meaning
    "GOAT": ("goat", "animal", "came back as 'cattle' from 'horned animals'"),
    "YAM": ("tuber", "nature", "came back as 'food' from 'food from the ground'"),
    "RICE": ("rice", "nature", "came back as 'grain'"),
    "FIELD": ("field", "nature", "read correctly from 'ground of plants', but long; frequent in farming talk"),
    "BOIL": ("boil", "action", "read correctly from 'make very hot', kept as a root because frequent"),
    "REACH": ("reach", "motion", "needed 'cannot come to it' paraphrase"),
    "GATHER": ("gather", "action", "base for harvest"),
}
BUILT = {  # concept -> (expression, evidence)
    "KNIFE": ("du FONsu (tool for cutting)", "built word; decoded correctly in tests/wordbuilding-ab-01"),
    "AXE": ("du SPLIT (tool for splitting)", "built word"), "SPEAR": ("du STAB (tool for stabbing)", "built word"),
    "FIREWOOD": ("wood + li + fire", "compound with relation"), "STICK": ("wood + long", "established compound"),
    "NAPE (OF NECK)": ("back + pi + neck", "compound"), "GREY": ("white + dark", "colour beyond the six basic terms: compound (method 3.1)"),
    "SKIRT": ("clothes + below", "compound"), "CANOE": ("boat", "lumped with boat"),
    "POINTED": ("sharp", "lumped with sharp"), "NO": ("mu / echo answer", "grammar"),
    "HARVEST": ("gather + pi + food", "compound"),
}


def main():
    ranking = {r["gloss"]: r for r in csv.DictReader(open(os.path.join(DATA, "concept-ranking.tsv")), delimiter="\t")}
    rows = W.read("concepts.tsv")
    have = {w["gloss"] for w in W.read("lexicon.tsv")}
    for c, spec in ROOTS.items():
        gl, field = spec[0], spec[1]
        if gl not in have:
            W.add_content(gl, field, 2)
        r = ranking[c]
        rows.append({"rank": r["rank"], "concept": c, "decision": "root", "expression": gl,
                     "evidence": f"batch 2; coverage {r['coverage']}, {r['families']} families, all 6 areas"})
    for c, (gl, field, why) in ON_DEMAND.items():
        if gl not in have:
            W.add_content(gl, field, 2)
        r = ranking.get(c, {})
        rows.append({"rank": r.get("rank", ""), "concept": c, "decision": "root", "expression": gl,
                     "evidence": f"on demand (tests/vocabulary-01): {why}"})
    for c, (expr, why) in BUILT.items():
        r = ranking.get(c, {})
        rows.append({"rank": r.get("rank", ""), "concept": c, "decision": "built/compound", "expression": expr,
                     "evidence": f"batch 2; {why}"})
    W.write("concepts.tsv", rows, ["rank", "concept", "decision", "expression", "evidence"])
    print(len(rows), "rows")


if __name__ == "__main__":
    main()

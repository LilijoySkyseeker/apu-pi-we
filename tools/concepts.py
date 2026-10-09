"""Rank concepts by area-balanced lineage coverage (roadmap B1; docs/vocabulary-method.md).

The one data-extraction script the vocabulary plan allows. Inputs (download once, not committed):
  CLICS4 concepts.csv + languages.csv   https://doi.org/10.5281/zenodo.16900179
  Concepticon conceptlists/Goddard-2011-63.tsv (NSM primes)   https://github.com/concepticon/concepticon-data

Coverage of a concept = for each macro-area, the share of the area's lineages (families, or
isolates counted as their own lineage) whose word lists name the concept; averaged over areas.
Writes data/concept-ranking.tsv.

  python concepts.py /tmp/cl/concepts.csv.zip /tmp/cl/languages.csv /tmp/cc/cd/concepticondata/conceptlists/Goddard-2011-63.tsv
"""
import csv, io, os, sys, zipfile
from collections import defaultdict

csv.field_size_limit(10 ** 9)
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "concept-ranking.tsv")


def main(concepts_zip, languages_csv, nsm_tsv):
    area_lineages = defaultdict(set)
    for r in csv.DictReader(open(languages_csv, encoding="utf-8")):
        lineage = r["Family"] or r["Glottocode"]
        if r["Macroarea"]:
            area_lineages[r["Macroarea"]].add(lineage)
    areas = sorted(area_lineages)
    nsm = {r["CONCEPTICON_GLOSS"] for r in csv.DictReader(open(nsm_tsv, encoding="utf-8"), delimiter="\t")
           if r.get("CONCEPTICON_GLOSS")}

    z = zipfile.ZipFile(concepts_zip)
    rows = []
    for r in csv.DictReader(io.TextIOWrapper(z.open(z.namelist()[0]), encoding="utf-8")):
        named = set(r["Families"].split()) | set(r["Languages"].split())  # isolates appear as languages
        shares = [len(named & area_lineages[a]) / len(area_lineages[a]) for a in areas]
        rows.append({
            "gloss": r["Concepticon_Gloss"] or r["ID"],
            "coverage": round(sum(shares) / len(shares), 4),
            "families": r["Family_Count"],
            "areas_present": sum(1 for x in shares if x > 0),
            "min_area_share": round(min(shares), 3),
            "nsm_prime": int((r["Concepticon_Gloss"] or "") in nsm),
        })
    rows.sort(key=lambda x: -x["coverage"])
    for i, r in enumerate(rows, 1):
        r["rank"] = i
    found = {r["gloss"] for r in rows}
    for g in sorted(nsm - found):  # primes CLICS4 doesn't have still enter the seed
        rows.append({"gloss": g, "coverage": "", "families": "", "areas_present": "", "min_area_share": "",
                     "nsm_prime": 1, "rank": ""})
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, ["rank", "gloss", "coverage", "families", "areas_present", "min_area_share",
                                "nsm_prime"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    print(f"{len(rows)} concepts; areas: {', '.join(f'{a} {len(area_lineages[a])}' for a in areas)}")
    print("NSM primes not in CLICS4:", len(nsm - found))


if __name__ == "__main__":
    main(*sys.argv[1:4])

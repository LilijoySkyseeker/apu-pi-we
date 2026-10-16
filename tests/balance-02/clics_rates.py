"""balance-02 part 2: rung-4 (family-balanced) rates for the overridden pairs, from CLICS4 forms.

  direnv exec /home/agent/work/repos/universal-language python3 tests/balance-02/clics_rates.py DIR

DIR holds forms.csv, concepts.csv, languages.csv from CLICS4 v1.0 (Zenodo 19608447, clics4-v1.0.zip, cldf/;
not kept in the repo, 108 MB). A language lumps a pair when one segment string is listed under both concepts;
rate = mean over families of the share of their languages that lump (as tools/clics_rates.awk). 'no copies'
drops forms whose ConceptInSource is a broad set ("FOOT OR LEG"), the inflation research/notes/colexification.md
warns of (added). Bootstrap: 2,000 resamples of families, seed 1. Writes clics-rates.tsv here.
"""
import collections, csv, os, random, sys
csv.field_size_limit(10**9)
D = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
gloss = {r["ID"]: r["Concepticon_Gloss"] for r in csv.DictReader(open(os.path.join(D, "concepts.csv")))}
fam = {r["ID"]: r["Family"] or "iso_" + r["ID"] for r in csv.DictReader(open(os.path.join(D, "languages.csv")))}
PAIRS = [("MOON", "MONTH"), ("DAY (24 HOURS)", "DAY (NOT NIGHT)"), ("HEAR", "LISTEN"), ("TAKE", "GET"),
         ("ARM", "HAND"), ("GHOST", "SPIRIT"), ("GHOST", "SOUL"), ("LEG", "FOOT")]
need = {c for p in PAIRS for c in p}
forms = collections.defaultdict(lambda: collections.defaultdict(set))
for r in csv.DictReader(open(os.path.join(D, "forms.csv"))):
    g = gloss.get(r["Parameter_ID"])
    if g in need:
        seg = r["Segments"].replace(" + ", " ").replace("_", " ") or r["Form"]
        forms[r["Language_ID"]][g].add((seg, bool(r["ConceptInSource"])))


def fams(a, b, drop):
    per = collections.defaultdict(list)
    for L, d in forms.items():
        fa = {f for f, c in d.get(a, ()) if not (drop and c)}
        fb = {f for f, c in d.get(b, ()) if not (drop and c)}
        if fa and fb:
            per[fam[L]].append(1 if fa & fb else 0)
    return per


rows = []
random.seed(1)
for a, b in PAIRS:
    for drop in (False, True):
        per = fams(a, b, drop)
        fr = [sum(v) / len(v) for v in per.values()]
        nv = sum(len(v) for v in per.values()); lv = sum(sum(v) for v in per.values())
        xs = sorted(sum(random.choice(fr) for _ in fr) / len(fr) for _ in range(2000))
        rows.append([f"{a}/{b}", "no copies" if drop else "all forms", f"{lv}/{nv}",
                     f"{sum(1 for v in per.values() if sum(v))}/{len(per)}", f"{100 * sum(fr) / len(fr):.1f}",
                     f"{100 * xs[50]:.0f}-{100 * xs[1949]:.0f}", f"{sum(x >= .5 for x in xs) / 2000:.2f}"])
with open(os.path.join(HERE, "clics-rates.tsv"), "w") as f:
    f.write("pair\tforms\tvarieties_lumping\tfamilies_lumping\tfamily_balanced_pct\tbootstrap_95\tshare_of_resamples_ge_50\n")
    for r in rows:
        f.write("\t".join(r) + "\n"); print(*r, sep="\t")

"""Rung-4 lump rates for the sets pass (sets.md) and the pound/crush question, from CLICS4.

  direnv exec /home/agent/work/repos/universal-language python3 tests/conceptlist-01/sets_rates.py DIR

DIR is CLICS4 v1.0's cldf/ folder (as tests/deeplayer-02/bq_rates.py; kept outside the repo). Same method as
bq_rates.py: a language lumps a pair when one segment string is listed under both concepts; the rate is the
mean over families of the share of their languages that lump; broad "X OR Y" source items listed under both
concepts are dropped (the narrower copy rule). Bootstrap 2,000 family resamples, seed 1. Writes sets-rates.tsv.
"""
import collections, csv, os, random, sys
csv.field_size_limit(10**9)
D = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
PAIRS = [
    ("pound / crush (monpa)", "POUND", "CRUSH"), ("pound / grind (inke)", "POUND", "GRIND"),
    ("warm / hot", "WARM", "HOT"), ("blue / green", "BLUE", "GREEN"), ("grey / white", "GREY", "WHITE"),
    ("grey / black", "GREY", "BLACK"), ("surprised / fear (fright)", "SURPRISED", "FEAR (FRIGHT)"),
    ("surprised / afraid", "SURPRISED", "FEAR (BE AFRAID)"), ("pity / grief", "PITY", "GRIEF"),
    ("envy / angry", "ENVY", "ANGRY"), ("hail / ice", "HAIL", "ICE"),
    ("older / younger brother (of man)", "OLDER BROTHER (OF MAN)", "YOUNGER BROTHER (OF MAN)"),
    ("older brother / older sister (of man)", "OLDER BROTHER (OF MAN)", "OLDER SISTER (OF MAN)"),
    ("summer / hot", "SUMMER", "HOT"), ("winter / cold", "WINTER", "COLD"), ("autumn / springtime", "AUTUMN", "SPRINGTIME"),
]
gloss = {r["ID"]: r["Concepticon_Gloss"] for r in csv.DictReader(open(os.path.join(D, "concepts.csv")))}
fam = {r["ID"]: r["Family"] or "iso_" + r["ID"] for r in csv.DictReader(open(os.path.join(D, "languages.csv")))}
need = {c for p in PAIRS for c in p[1:]}
forms = collections.defaultdict(lambda: collections.defaultdict(set))
for r in csv.DictReader(open(os.path.join(D, "forms.csv"))):
    g = gloss.get(r["Parameter_ID"])
    if g in need:
        forms[r["Language_ID"]][g].add((r["Segments"].replace(" + ", " ").replace("_", " ") or r["Form"], r["ConceptInSource"]))
random.seed(1)
out = ["pair\tconcepticon\tvarieties_lumping\tfamilies\tfamily_balanced_pct\tbootstrap_95"]
for label, a, b in PAIRS:
    per = collections.defaultdict(list)
    for L, d in forms.items():
        shared = {c for _, c in d.get(a, ()) if " OR " in c} & {c for _, c in d.get(b, ()) if " OR " in c}
        fa = {f for f, c in d.get(a, ()) if c not in shared}
        fb = {f for f, c in d.get(b, ()) if c not in shared}
        if fa and fb:
            per[fam[L]].append(1 if fa & fb else 0)
    if not per:
        out.append(f"{label}\t{a}/{b}\t0/0\t0\t\t"); continue
    fr = [sum(v) / len(v) for v in per.values()]
    xs = sorted(sum(random.choice(fr) for _ in fr) / len(fr) for _ in range(2000))
    nv, lv = sum(len(v) for v in per.values()), sum(sum(v) for v in per.values())
    out.append(f"{label}\t{a}/{b}\t{lv}/{nv}\t{len(per)}\t{100 * sum(fr) / len(fr):.1f}\t{100 * xs[50]:.0f}-{100 * xs[1949]:.0f}")
open(os.path.join(HERE, "sets-rates.tsv"), "w").write("\n".join(out) + "\n")
print("\n".join(out))

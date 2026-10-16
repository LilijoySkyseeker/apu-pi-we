"""deeplayer-02 part 1: rung-4 (family-balanced) lump rates for the 17 WOLD boundary questions, from CLICS4.

  direnv exec /home/agent/work/repos/universal-language python3 tests/deeplayer-02/bq_rates.py DIR

DIR holds forms.csv, concepts.csv, languages.csv from CLICS4 v1.0 (Zenodo 19608447, clics4-v1.0.zip, cldf/;
kept in the scratchpad, not the repo). Adapted from tests/balance-02/clics_rates.py, unchanged in method:
a language lumps a pair when one segment string is listed under both concepts; rate = mean over families of
the share of their languages that lump (as tools/clics_rates.awk). 'no copies' drops, per language, the
forms of one broad source item (ConceptInSource "SPRING OR WELL") listed under both concepts of the pair.
That is narrower than balance-02's rule, which dropped every form with any ConceptInSource, including
plain relabels ("HIT" for STRIKE, "TURN" for TURN (SOMETHING)) and broad items on one side only (added).
Bootstrap: 2,000 resamples of families, seed 1. Writes bq-rates.tsv here.
Flags: 'near 50' when the rate is within 5 points of 50; 'range spans 50' when the 95% range crosses it.
"""
import collections, csv, os, random, sys
csv.field_size_limit(10**9)
D = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
gloss = {r["ID"]: r["Concepticon_Gloss"] for r in csv.DictReader(open(os.path.join(D, "concepts.csv")))}
fam = {r["ID"]: r["Family"] or "iso_" + r["ID"] for r in csv.DictReader(open(os.path.join(D, "languages.csv")))}
# (BQ id, WOLD meaning, Concepticon A, Concepticon B, role): role 'main' decides; 'aux' informs only
PAIRS = [
    ("1-37", "well / spring", "WELL", "SPRING (OF WATER)", "main"),
    ("1-861", "put out a fire / close (tapi)", "EXTINGUISH", "SHUT", "main"),
    ("3-585", "hawk / eagle", "HAWK", "EAGLE", "main"),
    ("4-345", "claw / nail (tolin)", "CLAW", "FINGERNAIL", "main"),
    ("4-68", "shiver / shake (susin)", "SHIVER", "SHAKE", "main"),
    ("5-24", "bake / roast", "BAKE", "ROAST (SOMETHING)", "main"),
    ("5-24", "bake / fry", "BAKE", "FRY", "aux"),
    ("5-24", "roast / fry (deeplayer-01's one root)", "ROAST (SOMETHING)", "FRY", "aux"),
    ("5-48", "scrape / scratch (sumin)", "SCRAPE", "SCRATCH", "main"),
    ("5-87", "to milk / milk (tunlo)", "DRAW MILK", "MILK", "main"),
    ("6-62", "clothes button / lock key (tinli's other sense)", "BUTTON", "KEY", "main"),
    ("9-211", "pound (in a mortar) / hit (payon)", "POUND", "STRIKE", "main"),
    ("9-211", "pound / beat", "POUND", "BEAT", "aux"),
    ("9-77", "mat / carpet, rug", "MAT", "RUG", "main"),
    ("10-17", "twist / turn (duko)", "TWIST", "TURN (SOMETHING)", "main"),
    ("10-53", "chase / follow (lefan)", "PURSUE", "FOLLOW", "main"),
    ("16-51", "dare / brave", "DARE", "BRAVE", "main"),
    ("19-45", "command / lead (wungu)", "COMMAND", "LEAD (GUIDE)", "main"),
    ("19-45", "command / order", "COMMAND", "ORDER", "aux"),
    ("21-42", "murder / kill (omen)", "MURDER", "KILL", "main"),
    ("5-82", "pepper / chili (part 2 fallback)", "PEPPER", "CHILI PEPPER", "aux"),
    ("8-82", "coconut / palm tree (part 2 fallback)", "COCONUT", "PALM TREE", "aux"),
    ("check", "moon / month (reproduces balance-02's 69.9)", "MOON", "MONTH", "aux"),
]
need = {c for p in PAIRS for c in p[2:4]}
forms = collections.defaultdict(lambda: collections.defaultdict(set))
for r in csv.DictReader(open(os.path.join(D, "forms.csv"))):
    g = gloss.get(r["Parameter_ID"])
    if g in need:
        seg = r["Segments"].replace(" + ", " ").replace("_", " ") or r["Form"]
        forms[r["Language_ID"]][g].add((seg, r["ConceptInSource"]))


def fams(a, b, drop):
    per = collections.defaultdict(list)
    for L, d in forms.items():
        # shared copies: one broad source item ("SPRING OR WELL") listed under both concepts of the pair
        shared = ({c for _, c in d.get(a, ()) if " OR " in c} & {c for _, c in d.get(b, ()) if " OR " in c}
                  if drop else set())
        fa = {f for f, c in d.get(a, ()) if c not in shared}
        fb = {f for f, c in d.get(b, ()) if c not in shared}
        if fa and fb:
            per[fam[L]].append(1 if fa & fb else 0)
    return per


rows = []
random.seed(1)
for bq, label, a, b, role in PAIRS:
    for drop in (False, True):
        per = fams(a, b, drop)
        if not per:
            rows.append([bq, label, f"{a}/{b}", role, "no copies" if drop else "all forms", "0/0", "0/0", "", "", "", "no data"])
            continue
        fr = [sum(v) / len(v) for v in per.values()]
        nv = sum(len(v) for v in per.values()); lv = sum(sum(v) for v in per.values())
        xs = sorted(sum(random.choice(fr) for _ in fr) / len(fr) for _ in range(2000))
        rate = 100 * sum(fr) / len(fr)
        lo, hi = 100 * xs[50], 100 * xs[1949]
        flag = "near 50" if abs(rate - 50) <= 5 else ("range spans 50" if lo < 50 <= hi else "")
        rows.append([bq, label, f"{a}/{b}", role, "no copies" if drop else "all forms", f"{lv}/{nv}",
                     f"{sum(1 for v in per.values() if sum(v))}/{len(per)}", f"{rate:.1f}",
                     f"{lo:.0f}-{hi:.0f}", f"{sum(x >= .5 for x in xs) / 2000:.2f}", flag])
with open(os.path.join(HERE, "bq-rates.tsv"), "w") as f:
    f.write("wold_id\tpair\tconcepticon\trole\tforms\tvarieties_lumping\tfamilies_lumping\tfamily_balanced_pct\t"
            "bootstrap_95\tshare_of_resamples_ge_50\tflag\n")
    for r in rows:
        f.write("\t".join(r) + "\n"); print(*r, sep="\t")

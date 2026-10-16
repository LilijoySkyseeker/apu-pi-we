"""deeplayer-01 step 1: per-meaning evidence from WOLD (lexibank/wold CLDF, src/*.csv).
Writes evidence.tsv: the 1,460 core meanings (Core_list=yes) with field, label and counts over WOLD's 41 languages / 24 families.
  langs, fams        languages / families with any word for the meaning
  root_langs, root_fams   with a native unanalyzable word (Borrowed 4 or 5, Analyzability 'unanalyzable')  (added: the "own root" reading)
  loan_langs         languages whose every word for it is clearly or probably borrowed (Borrowed 1 or 2)
  borrowed_score     WOLD's own mean borrowed score for the meaning
direnv exec . python3 tests/deeplayer-01/evidence.py"""
import csv, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
S = os.path.join(HERE, "src")
P = [r for r in csv.DictReader(open(os.path.join(S, "parameters.csv"))) if r["Core_list"] == "yes"]
L = {r["ID"]: r for r in csv.DictReader(open(os.path.join(S, "languages.csv")))}
forms = collections.defaultdict(lambda: collections.defaultdict(list))
for r in csv.DictReader(open(os.path.join(S, "forms.csv"))):
    forms[r["Parameter_ID"]][r["Language_ID"]].append(r)

with open(os.path.join(HERE, "evidence.tsv"), "w") as f:
    f.write("wold_id\tfield\tmeaning\tconcepticon\tlangs\tfams\troot_langs\troot_fams\tloan_langs\tborrowed_score\n")
    for p in P:
        fl = forms[p["ID"]]
        langs = set(fl)
        fams = {L[l]["Family"] for l in langs}
        root = {l for l, ws in fl.items() if any(w["Analyzability"] == "unanalyzable" and w["Borrowed"][0] in "45" for w in ws)}
        loan = {l for l, ws in fl.items() if all(w["Borrowed"][0] in "12" for w in ws)}
        bs = p["Borrowed_score"]
        f.write("\t".join([p["ID"], p["Semantic_field"], p["Name"], p["Concepticon_Gloss"], str(len(langs)), str(len(fams)),
                           str(len(root)), str(len({L[l]['Family'] for l in root})), str(len(loan)),
                           f"{float(bs):.2f}" if bs else ""]) + "\n")
print(len(P), "meanings")

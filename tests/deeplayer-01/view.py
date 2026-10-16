"""view.py FIELD-PREFIX: a compact line per meaning for the hand pass (working aid).
Shows langs/fams/root_fams/loan_langs, the coverage-02 rank of the head word (r=), and index hits."""
import csv, sys, os, re
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(H, "..", "..")
ev = list(csv.DictReader(open(os.path.join(H, "evidence.tsv")), delimiter="\t"))
ca = list(csv.DictReader(open(os.path.join(H, "candidates.tsv")), delimiter="\t"))
rank = {}
for r in csv.DictReader(open(os.path.join(R, "tests/coverage-02/candidates.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE):
    for k in (r["canonical"], r["best_label"]):
        rank.setdefault(k.lower(), r["crank"])
for e, c in zip(ev, ca):
    if not e["field"].startswith(sys.argv[1]): continue
    hs = [h for h in c["hits"].split(" || ") if h and "roots-1500" not in h]
    hs = [h.replace("candidates-02:", "c:") for h in hs]
    head = re.sub(r"^(the|to) ", "", e["meaning"]).split(" or ")[0]
    head = re.sub(r"\(.*\)", "", head).strip()
    print(f"{e['wold_id']}|{e['meaning']}|{e['langs']}/{e['fams']}/{e['root_fams']}/{e['loan_langs']}|r={rank.get(head,'-')}|{' || '.join(hs)[:260]}")

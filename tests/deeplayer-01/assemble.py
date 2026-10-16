"""deeplayer-01 step 4: pass.tsv and the per-field table from evidence.tsv, candidates.tsv and the hand pass src/match.tsv.
In src/match.tsv, "@" / "@2" in the by column stands for the first / second automatic index hit (candidates.tsv), resolved here.
direnv exec . python3 tests/deeplayer-01/assemble.py"""
import csv, os, re, collections

H = os.path.dirname(os.path.abspath(__file__))


def rd(p):
    with open(os.path.join(H, p)) as f:
        return list(csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE))


ev = {r["wold_id"]: r for r in rd("evidence.tsv")}
hits = {r["wold_id"]: [h for h in r["hits"].split(" || ") if h and "roots-1500" not in h] for r in rd("candidates.tsv")}
m = {r["wold_id"]: r for r in rd("src/match.tsv")}
CL = ["cov", "D", "BQ", "P", "C", "L", "X"]
rank = {}  # coverage-02 frequency rank of the head word (approximate: label match only)
for r in csv.DictReader(open(os.path.join(H, "..", "coverage-02", "candidates.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE):
    for kk in (r["canonical"], r["best_label"]):
        rank.setdefault(kk.lower(), r["crank"])


def tier(e, r):
    """(added) D tiers: core = own root in at least 15 of WOLD's 24 families and no alternative class noted; else edge."""
    if r["status"] != "D":
        return ""
    if r["gloss"].startswith("(="):
        return "same"
    return "core" if int(e["root_fams"]) >= 15 and "alt:" not in r["note"] else "edge"


rows, tab = [], collections.OrderedDict()
for k, e in ev.items():
    r = m[k]
    by = r["by"]
    if by.startswith("@"):
        i = int(by[1:] or 1) - 1
        by = hits[k][i]
    head = re.sub(r"\(.*\)", "", re.sub(r"^(the|to) ", "", e["meaning"]).split(" or ")[0]).strip()
    rk = rank.get(head, "") if r["status"] != "cov" else ""
    rows.append([k, e["field"], e["meaning"], e["langs"], e["fams"], e["root_fams"], e["loan_langs"], r["status"], tier(e, r), rk, by, r["gloss"], r["note"]])
    tab.setdefault(e["field"], collections.Counter())[r["status"]] += 1
with open(os.path.join(H, "pass.tsv"), "w") as f:
    f.write("wold_id\tfield\tmeaning\tlangs\tfamilies\troot_families\tloan_langs\tclass\tD_tier\tfreq_rank\tcovered_by_or_phrase\tgloss\tnote\n")
    for r in rows:
        f.write("\t".join(r) + "\n")
tot = collections.Counter()
print("| Field | Meanings | " + " | ".join(CL) + " | not covered |")
print("|---|---|" + "---|" * (len(CL) + 1))
for fld, c in sorted(tab.items(), key=lambda x: -(x[1]["D"] + x[1]["BQ"])):
    tot.update(c)
    n = sum(c.values())
    print(f"| {fld} | {n} | " + " | ".join(str(c[x]) for x in CL) + f" | {100 * (n - c['cov']) // n}% |")
n = sum(tot.values())
print(f"| **All** | {n} | " + " | ".join(f"**{tot[x]}**" for x in CL) + f" | {100 * (n - tot['cov']) // n}% |")
tc = collections.Counter(r[8] for r in rows if r[7] == "D")
print("D rows", tot["D"], dict(tc), "-> new roots", tot["D"] - tc["same"])

"""balance-02 part 3: regional rules that bind, applied to every loan judged so far.

  direnv exec /home/agent/work/repos/universal-language python3 tests/balance-02/loan_rules.py

Columns per loan:
  - coverage candidates (c01-c11), older lexicon loans (older.txt) and the eight metric units: balance-01's
    loans-per-loan.tsv (its counted columns, checked there against loans-final.tsv / loans-rerun.tsv);
  - symbols: tests/symbols-01/panel.tsv, sourced columns as its emit.py counts them (all 18 tested forms);
  - imitative and nursery words: tests/imitative-01/panel.tsv, sourced columns as its emit.py counts them.
The current rule (R0) and each alternative keep "at least 12 of 20" and replace only the regional part.
Writes loans-rules.tsv (one row per loan) and loans-rules-flips.tsv here.
"""
import collections, csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
REG = ["EA", "SEA", "SA", "WA", "EU", "SSA", "AM"]
REGION = {"zh": "EA", "ja": "EA", "ko": "EA", "vi": "SEA", "th": "SEA", "id": "SEA", "tl": "SEA",
          "hi": "SA", "bn": "SA", "ta": "SA", "fa": "WA", "ar": "WA", "tr": "WA", "ru": "EU", "es": "EU",
          "fr": "EU", "sw": "SSA", "ha": "SSA", "yo": "SSA", "qu": "AM"}
# Language families (added; Glottolog top-level families). 13 families; Indo-European has 6 panel languages.
FAMILY = {"zh": "Sino-Tibetan", "ja": "Japonic", "ko": "Koreanic", "vi": "Austroasiatic", "th": "Tai-Kadai",
          "id": "Austronesian", "tl": "Austronesian", "hi": "Indo-European", "bn": "Indo-European",
          "ta": "Dravidian", "fa": "Indo-European", "ar": "Afro-Asiatic", "tr": "Turkic", "ru": "Indo-European",
          "es": "Indo-European", "fr": "Indo-European", "sw": "Atlantic-Congo", "ha": "Afro-Asiatic",
          "yo": "Atlantic-Congo", "qu": "Quechuan"}
NREG = collections.Counter(REGION.values())


def read(p):
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))


def loans():
    out = []
    for r in read(os.path.join(REPO, "tests", "balance-01", "loans-per-loan.tsv")):
        if r["group"] == "symbols":
            continue
        cols = {x for g in REG for x in r[g].split() if x != "-"}
        out.append((r["concept"], r["group"], r["verdict"], cols))
    def panel(path, key, srcre):
        rows = read(path)
        d = collections.OrderedDict()
        for r in rows:
            k = key(r)
            d.setdefault(k, set())
            if r["shared"] == "y" and re.search(srcre, r["src"]):
                d[k].add(r["lang"])
        return d
    sym = panel(os.path.join(REPO, "tests", "symbols-01", "panel.tsv"), lambda r: f"{r['symbol']} ({r['form']})",
                r"\b(Wt|We|Wp|Sub|Lz|Web)\b|M\*")
    for k, cols in sym.items():
        out.append((k, "symbols", "recorded: " + ("pass" if k.startswith((".com", "hashtag")) else "fail"), cols))
    imi = panel(os.path.join(REPO, "tests", "imitative-01", "panel.tsv"), lambda r: f"{r['concept']} ({r['form']})",
                r"\b(Wt|We|Wb)\b|M\*")
    for k, cols in imi.items():
        out.append((k, "imitative", "recorded: " + ("pass, not adopted" if k == "mother (mama)" else "fail"), cols))
    return out


def regs(cols):
    return collections.Counter(REGION[c] for c in cols)


RULES = {
    # current: >=12 of 20 across >=4 of 7 regions (never binds: 3 largest regions hold 10 languages)
    "R0 now: 4 of 7 regions": lambda c: len(c) >= 12 and len(regs(c)) >= 4,
    # A: regional depth: a region counts only when at least 2 of its languages share the form (added).
    #    At 4 such regions it never binds either (checked: 0 flips), so 5 of the 6 regions that have 2+ languages
    "A depth: 5 regions with 2+ languages": lambda c: len(c) >= 12 and sum(1 for g, n in regs(c).items() if n >= 2) >= 5,
    # B: families: at least 7 of the panel's 13 families (more than half; each family once, like rung 4) (added)
    "B families: 7 of 13": lambda c: len(c) >= 12 and len({FAMILY[x] for x in c}) >= 7,
    # C: no region decides: still 12 of 20 if any one region's columns are replaced by the panel-wide rate
    #    of the rest, i.e. the pass survives dropping any one region and re-scaling (added)
    "C no single region decides": lambda c: len(c) >= 12 and all(
        (len(c) - n) / (20 - NREG[g]) >= 0.6 for g, n in regs(c).items()),
    # D: Spanish-Quechua counted once (loans.md pattern 2: the assumed Spanish loan "gives Spanish two votes")
    "D es+qu one vote": lambda c: (len(c) - (1 if {"es", "qu"} <= c else 0)) >= 12 and len(regs(c)) >= 4,
}


def main():
    L = loans()
    rows, flips = [], []
    for name, group, verdict, cols in L:
        res = {k: f(cols) for k, f in RULES.items()}
        rg = regs(cols)
        rows.append([name, group, verdict, len(cols), len(rg), sum(1 for n in rg.values() if n >= 2),
                     len({FAMILY[x] for x in cols}), " ".join(sorted(cols))] + ["pass" if v else "fail" for v in res.values()])
        for k, v in res.items():
            if v != res["R0 now: 4 of 7 regions"]:
                flips.append([k, name, group, verdict, len(cols), " ".join(f"{g}:{rg[g]}" for g in REG if rg[g]),
                              len({FAMILY[x] for x in cols}), "pass -> fail" if not v else "fail -> pass"])
    with open(os.path.join(HERE, "loans-rules.tsv"), "w") as f:
        f.write("\t".join(["loan", "group", "recorded_verdict", "columns", "regions", "regions_with_2plus",
                           "families", "languages"] + list(RULES)) + "\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")
    with open(os.path.join(HERE, "loans-rules-flips.tsv"), "w") as f:
        f.write("rule\tloan\tgroup\trecorded_verdict\tcolumns\tregions\tfamilies\tflip\n")
        for r in flips:
            f.write("\t".join(str(x) for x in r) + "\n")
    print(len(L), "loans;", sum(1 for r in rows if r[8] == "pass"), "pass R0")
    for k in RULES:
        fl = [r for r in flips if r[0] == k]
        print(f"{k}: {len(fl)} flips: " + ", ".join(f"{r[1]}({r[4]})" for r in fl))


if __name__ == "__main__":
    main()

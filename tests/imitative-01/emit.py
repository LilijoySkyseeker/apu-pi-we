"""Counts and per-concept tables from panel.tsv (imitative-01).

  python3 emit.py counts     # one line per concept and tested form: sourced / with memory / lenient, regions
  python3 emit.py tables     # markdown evidence tables for README.md
  python3 emit.py check      # rows whose shared mark differs from the adapted consonants (pattern 3);
                             # MISMATCH lines are errors, the others are listed-but-not-everyday words

A column counts when it is shared (y) and sourced: its src has Wt, We or Wb (M* is a Wiktionary listing).
A column from memory alone (M) counts only in the "with memory" figure. Lenient adds the "l" columns
(same consonants except a dropped or added one, or the base of a reduplicated form; see README).
Pass: at least 12 counted columns across at least 4 of the 7 regions.
"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REGION = {"zh": "EA", "ja": "EA", "ko": "EA", "vi": "SEA", "th": "SEA", "id": "SEA", "tl": "SEA", "hi": "SA",
          "bn": "SA", "ta": "SA", "fa": "WA", "ar": "WA", "tr": "WA", "ru": "EU", "es": "EU", "fr": "EU",
          "sw": "SSA", "ha": "SSA", "yo": "SSA", "qu": "AM"}
NAME = {"zh": "Mandarin", "ja": "Japanese", "ko": "Korean", "vi": "Vietnamese", "th": "Thai", "id": "Indonesian",
        "tl": "Tagalog", "hi": "Hindi", "bn": "Bengali", "ta": "Tamil", "fa": "Persian", "ar": "Arabic",
        "tr": "Turkish", "ru": "Russian", "es": "Spanish", "fr": "French", "sw": "Swahili", "ha": "Hausa",
        "yo": "Yoruba", "qu": "Quechua"}
KIND = {"E": "everyday", "N": "nursery", "E+N": "both"}
rows = list(csv.DictReader(open(os.path.join(HERE, "panel.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE))
order = list(dict.fromkeys((r["concept"], r["form"]) for r in rows))


def sourced(r):
    return bool(re.search(r"\b(Wt|We|Wb)\b|M\*", r["src"]))


def skel(form):
    return re.sub(r"[aeiou]", "", form)


def count(key):
    rs = [r for r in rows if (r["concept"], r["form"]) == key]
    out = {}
    for label, ok in (("sourced", lambda r: r["shared"] == "y" and sourced(r)),
                      ("memory", lambda r: r["shared"] == "y"),
                      ("lenient", lambda r: r["shared"] in ("y", "l"))):
        hit = [r for r in rs if ok(r)]
        out[label] = (len(hit), len({REGION[r["lang"]] for r in hit}), [r["lang"] for r in hit])
    return out


def verdict(c):
    s, m, l = c["sourced"], c["memory"], c["lenient"]
    if s[0] >= 12 and s[1] >= 4:
        return "pass"
    if m[0] >= 12 and m[1] >= 4:
        return "fail (passes with memory)"
    if l[0] >= 12 and l[1] >= 4:
        return "borderline (passes lenient)"
    return "fail"


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "counts"
    if what == "check":
        for r in rows:
            if r["adapted"]:
                same = skel(r["adapted"]) == skel(r["form"])
                if same != (r["shared"] == "y"):
                    why = "same consonants, lenient by judgment (see note)" if same and r["shared"] == "l" else "MISMATCH"
                    print(f"{r['concept']}\t{r['form']}\t{r['lang']}\t{r['adapted']}\tshared={r['shared']}\t{why}")
        sys.exit()
    for key in order:
        c = count(key)
        s, m, l = c["sourced"], c["memory"], c["lenient"]
        if what == "counts":
            print(f"{key[0]}\t{key[1]}\tsourced {s[0]}/{s[1]}\tmemory {m[0]}/{m[1]}\tlenient {l[0]}/{l[1]}\t"
                  f"{verdict(c)}\t{' '.join(s[2])}")
        else:
            rs = [r for r in rows if (r["concept"], r["form"]) == key]
            print(f"#### {key[0]}: *{key[1]}* [{rs[0]['ipa_form']}]\n")
            print("| Lang | Word (kind) | Adapted | Shared | src | Note |\n|---|---|---|---|---|---|")
            for r in rs:
                sh = {"y": "✓", "n": "✗", "l": "✗ (✓ lenient)"}[r["shared"]]
                print(f"| {NAME[r['lang']]} | {r['everyday']} ({KIND[r['kind']]}) | {r['adapted']} | {sh} | "
                      f"{r['src']} | {r['note']} |")
            print(f"\nSourced {s[0]}/20 in {s[1]} regions; with memory {m[0]}/{m[1]}; lenient {l[0]}/{l[1]}. "
                  f"**{verdict(c)}.**\n")

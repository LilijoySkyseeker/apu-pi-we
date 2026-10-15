"""Counts and per-symbol tables from panel.tsv (symbols-01).

  python3 emit.py counts     # one line per symbol: sourced / with memory / lenient counts and regions
  python3 emit.py tables     # markdown evidence tables for README.md

A column counts when it is shared (y) and sourced: its src has Wt, We, Wp, Sub, Lz or Web (M* is a
Wiktionary listing). A column from memory alone (M) counts only in the "with memory" figure. Lenient adds
the "n (y lenient)" columns. Pass: at least 12 counted columns across at least 4 of the 7 regions.
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
rows = list(csv.DictReader(open(os.path.join(HERE, "panel.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE))
order = list(dict.fromkeys(r["symbol"] for r in rows))


def sourced(r):
    return bool(re.search(r"\b(Wt|We|Wp|Sub|Lz|Web)\b|M\*", r["src"]))


def count(sym):
    rs = [r for r in rows if r["symbol"] == sym]
    out = {}
    for label, ok in (("sourced", lambda r: r["shared"] == "y" and sourced(r)),
                      ("memory", lambda r: r["shared"] == "y"),
                      ("lenient", lambda r: r["shared"].startswith("y") or "lenient" in r["shared"])):
        hit = [r for r in rs if ok(r)]
        out[label] = (len(hit), len({REGION[r["lang"]] for r in hit}))
    out["deciding"] = [r["lang"] for r in rs if r["shared"] == "y" and not sourced(r)]
    return rs[0]["form"], out


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "counts"
    for sym in order:
        form, c = count(sym)
        if what == "counts":
            s, m, l = c["sourced"], c["memory"], c["lenient"]
            ok = "pass" if s[0] >= 12 and s[1] >= 4 else ("fail (passes with memory)" if m[0] >= 12 and m[1] >= 4 else "fail")
            print(f"{sym}\t{form}\tsourced {s[0]}/{s[1]}\tmemory {m[0]}/{m[1]}\tlenient {l[0]}/{l[1]}\t{ok}\tmemory-only: {' '.join(c['deciding'])}")
        else:
            print(f"#### `{sym}` ({form})\n\n| Lang | Everyday word | Shared | src | Note |\n|---|---|---|---|---|")
            for r in rows:
                if r["symbol"] == sym:
                    sh = {"y": "✓", "n": "✗"}.get(r["shared"], "✗ (✓ lenient)")
                    print(f"| {NAME[r['lang']]} | {r['everyday']} | {sh} | {r['src']} | {r['note']} |")
            s, m, l = c["sourced"], c["memory"], c["lenient"]
            print(f"\nSourced {s[0]}/20 in {s[1]} regions; with memory columns {m[0]}/{m[1]}; lenient {l[0]}/{l[1]}.\n")

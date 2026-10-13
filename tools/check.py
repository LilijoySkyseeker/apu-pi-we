"""Check language text for unknown words (roadmap C3, built 2026-10-08).

Hand translation has now used stale word forms three times: forms renamed in a rebuild
(Ate for "far", ban for "rather"). This flags every word that isn't a current grammar word,
root, number word or digit, or a name after the article "en".

  python check.py FILE...        # checks language lines in code blocks and **bold** spans
  python check.py --text "..."   # checks one string
"""
import re, sys
import words as W

KNOWN = ({g["form"] for g in W.read("grammar.tsv")} | {w["form"] for w in W.read("lexicon.tsv")}
         | {r["form"] for r in W.read("numbers.tsv")} | {w["form"] for w in W.read("senary.tsv")})


def unknown(text):
    toks = re.findall(r"[A-Za-z]+", text)
    bad = []
    for i, t in enumerate(toks):
        if t.lower() in KNOWN:
            continue
        if i > 0 and toks[i - 1].lower() == "en":   # a name
            continue
        if len(t) == 1 and t.isupper():   # a placeholder in a template (X, Y)
            continue
        bad.append(t)
    return bad


def check_file(path):
    problems, in_code = [], False
    for n, line in enumerate(open(path), 1):
        if line.startswith("```"):
            in_code = not in_code
            continue
        spans = [line] if in_code else re.findall(r"\*\*([^*]+)\*\*", line)
        for sp in spans:
            toks = re.findall(r"[A-Za-z]+", sp)
            known = sum(t.lower() in KNOWN for t in toks)
            if toks and known >= max(1, len(toks) // 2):   # looks like language, not an English gloss
                bad = unknown(sp)
                if bad:
                    problems.append(f"{path}:{n}: {' '.join(bad)}")
    return problems


if __name__ == "__main__":
    if sys.argv[1] == "--text":
        print(unknown(sys.argv[2]) or "ok")
    else:
        out = [p for f in sys.argv[1:] for p in check_file(f)]
        print("\n".join(out) if out else "no unknown words")

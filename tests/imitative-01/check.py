"""Check adapted imitative and nursery forms against the language's words (imitative-01).

  python3 check.py FORM [FORM ...]

For each form: same form or same content key (as names.py does) in data/lexicon.tsv, data/grammar.tsv and
data/numbers.tsv; same form as a spelling-alphabet word (reference 11.5); offensive.py blocked() and matches().
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import words as W
import offensive as O

ICAO = re.search(r"say each letter by its word.*?: (a \*\*alufa.*?)\. Within",
                 open(os.path.join(HERE, "..", "..", "docs", "language.md")).read()).group(1)
SPELL = dict((f, l) for l, f in re.findall(r"(\w) \*\*(\w+)\*\*", ICAO))


def report(form):
    out = []
    for name, col in (("lexicon.tsv", "gloss"), ("grammar.tsv", "gloss"), ("numbers.tsv", "value")):
        for r in W.read(name):
            if r["form"] == form:
                out.append(f"same form as {r['form']} '{r[col]}' ({name})")
            elif name == "lexicon.tsv":
                try:
                    if W.INV.content_key(W.split(r["form"])) == W.INV.content_key(W.split(form)):
                        out.append(f"same content key as {r['form']} '{r[col]}'")
                except Exception:
                    pass
    if form in SPELL:
        out.append(f"spelling-alphabet word for {SPELL[form]}")
    if O.blocked(form):
        out.append("BLOCKED (offensive hard list)")
    if O.matches(form):
        out.append("offensive tie-break match")
    return out or ["clear"]


if __name__ == "__main__":
    W.split  # forms must be pronounceable
    for f in sys.argv[1:]:
        W.split(f)
        print(f, "; ".join(report(f)))

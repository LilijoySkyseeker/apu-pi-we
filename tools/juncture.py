"""Juncture check: word sequences that sound like a different word or sequence.

Written tests can't hear these, so check them by rule (idea borrowed from the senary
project's juncture.py, 2026-10-08). Reports:
  1. digit + following word that sounds like a content word (stress pattern is identical)
  2. grammar words that differ only by a final -n (they merge before an n-initial word)
  3. grammar word ending in -n + vowel-initial content word, heard as the open grammar word
     + an n-initial content word ("den Ewo" ~ "de NEwo")

  python juncture.py      # prints problems; exit code 1 if any
"""
import re, sys
import words as W

inv = W.INV
grammar = W.read("grammar.tsv")
lex = [w for w in W.read("lexicon.tsv")]
digits = [r["form"] for r in W.read("numbers.tsv") if r["kind"] == "digit" and r["form"] in W.IDX]  # one-syllable digits; 6-9 behave like content words
ckey = {inv.content_key(W.split(w["form"])): w for w in lex if len(W.split(w["form"])) >= 2}
gforms = {g["form"]: g["gloss"] for g in grammar}
problems = []

for d in digits:  # 1
    for f in list(gforms) + digits:
        k = inv.content_key((W.IDX[d], W.IDX[f]))
        if inv.syl[W.IDX[f]][0] != "" and k in ckey:
            problems.append(f"digit+word: {d.upper()} {f} ~ {ckey[k]['gloss']} {ckey[k]['form']}")

opens = {}
for f, gl in gforms.items():  # 2
    o, v, c = inv.syl[W.IDX[f]]
    opens.setdefault((o, v), []).append(f"{gl}={f}")
for k, v in opens.items():
    if len(v) > 1:
        problems.append(f"-n pair: {' / '.join(v)}")

for f, gl in gforms.items():  # 3
    o, v, c = inv.syl[W.IDX[f]]
    if c != "n" or (o.replace("j", "y") + v) not in gforms:
        continue
    for w in lex:
        if w["form"][0] in "aeiou":
            heard = "n" + w["form"]
            if heard in {x["form"] for x in lex}:
                problems.append(f"-n + vowel: {f} {w['form']} ~ {o.replace('j','y') + v} {heard}")

print("\n".join(problems) if problems else "no juncture problems")
sys.exit(1 if problems else 0)

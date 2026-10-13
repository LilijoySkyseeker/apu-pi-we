"""Modern-use evidence for boundary cases (ladder 1, rung 3; vocabulary-method §0).

  python3 boundary.py "moon|month" "word|language" ...

For each pair of meanings and each of the 20 languages, from the frequency and sense data of Part 1:
  - lump: the language's most frequent word for one meaning also carries the other;
  - separate words: the language also has a word carrying only one meaning, and how frequent it is
    relative to the lumped word (signal 3: lumping languages separating the meanings in modern use);
  - each meaning's share of running text (signal 1).
Evidence that a lump costs meaning comes only from languages that have the lump (safeguard 1).
Wiktionary sense order and AI glosses make this approximate: read the words, not just the counts.
"""
import os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
LANGS = "zh ja ko vi th id fil hi bn ta fa ar tr ru es fr sw ha yo qu".split()


def load(code):
    fr = {}
    for fn in (f"freq-{code}.tsv", f"sfreq-{code}.tsv"):
        p = os.path.join(DATA, fn)
        if os.path.exists(p):
            for l in open(p).read().split("\n")[1:]:
                if l:
                    w, f = l.split("\t")
                    fr[w] = max(fr.get(w, 0), float(f))
    senses = {}
    for l in open(os.path.join(DATA, f"gloss-{code}.tsv")).read().split("\n")[1:]:
        if l:
            w, _, labs = l.split("\t")
            senses[w] = [x for x in labs.split(" | ") if x]
    return fr, senses


def words_for(meaning, fr, senses):
    out = [(w, fr.get(w, 0)) for w, labs in senses.items() if meaning in labs]
    return sorted(out, key=lambda x: -x[1])


def main(pairs):
    data = {c: load(c) for c in LANGS}
    for pair in pairs:
        a, b = pair.split("|")
        print(f"\n== {a} / {b}")
        lumpers, separating = [], []
        for c in LANGS:
            fr, senses = data[c]
            wa, wb = words_for(a, fr, senses), words_for(b, fr, senses)
            if not wa or not wb:
                print(f"  {c:4} (no data for {'both' if not wa and not wb else a if not wa else b})")
                continue
            both = [w for w, _ in wa if w in {x for x, _ in wb}]
            only_a = [(w, f) for w, f in wa if w not in both]
            only_b = [(w, f) for w, f in wb if w not in both]
            top_a, top_b = wa[0][0], wb[0][0]
            lump = top_a in both or top_b in both
            tag = "LUMP" if lump else "split"
            line = f"  {c:4} {tag:5} {a}: {', '.join(w for w, _ in wa[:3])} | {b}: {', '.join(w for w, _ in wb[:3])}"
            if lump:
                lumpers.append(c)
                fl = max(f for w, f in wa + wb if w in both)
                sep = [(w, f / fl) for w, f in (only_a[:1] + only_b[:1]) if f / fl >= 0.1]
                if sep:
                    separating.append(c)
                    line += "  separate: " + ", ".join(f"{w} ({r:.0%} of the lumped word)" for w, r in sep)
            print(line)
        print(f"  -> lump in {len(lumpers)} of {len(LANGS)} ({' '.join(lumpers)}); of those, a separate word in modern use in {len(separating)} ({' '.join(separating)})")


if __name__ == "__main__":
    main(sys.argv[1:])

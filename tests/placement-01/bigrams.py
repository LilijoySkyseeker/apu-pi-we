"""Grammar word + content word bigrams, for rule 3's haplology constraint (design log 2026-10-15,
"No root starts like the grammar word before it").

Same corpus and tokenising as tests/shortwords-03/positions.py (reference examples + UDHR, all
sentences, a comma breaks adjacency), now in the new short-word forms. adjacency.tsv there counts only
short word + short word, so this recounts the same corpus for short word + any other token (added: the
rule needs grammar word + content word, which adjacency.tsv doesn't record).

Output: bigrams.tsv (form, gloss, tokens, before_content, share).
  direnv exec ../.. python3 bigrams.py
"""
import collections, csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "tests", "shortwords-03"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import positions as P

short = dict(P.SHORT)  # form -> gloss (grammar words + digits 0-5)
import words as W


def is_content(b):  # a word of two or more syllables that is not a short word (roots, loans, operators: all start a stressed word)
    try:
        return len(W.split(b)) >= 2
    except (AssertionError, KeyError):
        return False


corpus = P.reference_sentences() + P.udhr_sentences()
tok, before = collections.Counter(), collections.Counter()
for s in corpus:
    t = s.replace(",", " , ").split()
    for a in t:
        if a in short:
            tok[a] += 1
    for a, b in zip(t, t[1:]):
        if a in short and b not in short and is_content(b):
            before[a] += 1
rows = sorted(short, key=lambda f: -before[f])
with open(os.path.join(HERE, "bigrams.tsv"), "w") as fh:
    fh.write("form\tgloss\ttokens\tbefore_content\tshare\n")
    for f in rows:
        fh.write(f"{f}\t{short[f]}\t{tok[f]}\t{before[f]}\t{before[f] / max(tok[f], 1):.3f}\n")
print(f"{len(corpus)} sentences")

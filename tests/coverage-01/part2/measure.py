"""Length of each translation, by vocabulary size: syllables per text (a placeholder ⟨x⟩ counts as 2).

  python3 measure.py            # prints a table and writes length.tsv

Apupiwe words are split into (C)V(n) syllables; names (after en) are counted by vowel groups, since their spelling isn't Apupiwe's.
"""
import glob, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../tools"))
import words as W

HERE = os.path.dirname(os.path.abspath(__file__))
SIZES = ["base", "1000", "1500", "2000"]


def syllables(text):
    n = 2 * len(re.findall(r"⟨[^⟩]*⟩", text))
    text = re.sub(r"⟨[^⟩]*⟩", " ", text.lower())
    for w in re.findall(r"[^\W\d_]+", text):
        try:
            n += len(W.split(w))          # an Apupiwe word: its (C)V(n) syllables
        except (AssertionError, KeyError):
            n += len(re.findall(r"[aeiouy]+", w)) or 1   # a name in its own spelling
    return n


def main():
    rows = []
    texts = sorted({os.path.basename(p) for s in SIZES for p in glob.glob(os.path.join(HERE, f"ap-{s}", "[0-9][0-9].txt"))})
    for t in texts:
        row = [t[:2]]
        for s in SIZES:
            p = os.path.join(HERE, f"ap-{s}", t)
            row.append(syllables(open(p).read()) if os.path.exists(p) else None)
        rows.append(row)
    with open(os.path.join(HERE, "length.tsv"), "w") as f:
        f.write("text\t" + "\t".join(SIZES) + "\n")
        for r in rows:
            f.write("\t".join("" if x is None else str(x) for x in r) + "\n")
    tot = {s: sum(r[i + 1] for r in rows if all(x is not None for x in r[1:])) for i, s in enumerate(SIZES)}
    complete = sum(all(x is not None for x in r[1:]) for r in rows)
    print(f"texts with all sizes: {complete}")
    for s in SIZES:
        if tot["base"]:
            print(f"{s:>5}: {tot[s]} syllables ({tot[s] / tot['base']:.0%} of base)")


if __name__ == "__main__":
    main()

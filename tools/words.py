"""Add words to the language without disturbing existing ones, and measure texts.

Grammar words and content words may share syllables (the old partition was dropped
2026-10-08); stress marks where content words begin. New content words must stay distinct
from every existing word after predicted drift (see build.py and docs/drift.md).
Note: add-grammar does not check the same-slot consonant rule; rebuild with build.py for that.

data/grammar.tsv and data/lexicon.tsv are the source of truth. Existing words never
move: in a living language, words are stable. New words take the best free form.

  python words.py add-grammar GLOSS CLASS FREQ
  python words.py add-content GLOSS FIELD TIER [--antonym WORD] [--no-approximants]
  python words.py syllables "text in the language"
"""
import argparse, csv, os, re
import numpy as np
from build import Inventory, FULL, TIER_FREQ, EFFORT

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
INV = Inventory([c for c in FULL if c != "z"])  # 13 consonants since 2026-10-08
SYL, IDX, S = INV.name, INV.idx, INV.S
APPROXIMANTS = {"l", "w", "j"}


def read(name):
    with open(os.path.join(DATA, name)) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def write(name, rows, fields):
    with open(os.path.join(DATA, name), "w", newline="") as fh:
        w = csv.DictWriter(fh, fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


def split(form):
    """Split a word into syllables of the form (C)V(n)."""
    parts = re.findall(r"[^aeiou]?[aeiou](?:n(?![aeiou]))?", form)
    assert "".join(parts) == form, form
    return [IDX[p] for p in parts]


def add_grammar(gloss, cls, freq):
    grammar = read("grammar.tsv")
    taken = {IDX[g["form"]] for g in grammar}
    best, best_c = None, float("inf")
    for cand in range(len(SYL)):
        if cand in taken:
            continue
        c = 0.0
        for g in grammar:
            u = IDX[g["form"]]
            w = 3.0 if g["class"] == cls else 1.0
            if g["gloss"] == "NOT":
                w = 10.0
            c += w * (freq * S[cand, u] + float(g["freq"]) * S[u, cand])
        c += EFFORT * freq * 0.4 * bool(INV.syl[cand][2])
        if c < best_c:
            best, best_c = cand, c
    grammar.append({"gloss": gloss, "class": cls, "freq": freq, "form": SYL[best]})
    write("grammar.tsv", grammar, ["gloss", "class", "freq", "form"])
    print(f"{gloss} = {SYL[best]}  (cost {best_c:.4f})")


def add_content(gloss, field, tier, antonyms=(), no_approximants=False):
    lexicon = read("lexicon.tsv")
    content = list(range(len(SYL)))
    lexicon = [w for w in lexicon if w["gloss"] != gloss]
    if no_approximants:
        content = [i for i in content if INV.syl[i][0] not in APPROXIMANTS]
    second = [i for i in content if INV.syl[i][0] != ""]
    taken = {INV.content_key(split(w["form"])) for w in lexicon}
    ex = np.array([split(w["form"]) for w in lexicon if len(split(w["form"])) == 2])
    ex_words = [w for w in lexicon if len(split(w["form"])) == 2]
    weight = np.array([30.0 if w["gloss"] in antonyms else
                       10.0 if w["field"] == "number" else
                       3.0 if w["field"] == field else 1.0 for w in ex_words])
    efreq = np.array([TIER_FREQ[int(w["tier"])] for w in ex_words])
    f = TIER_FREQ[tier]
    best, best_c = None, float("inf")
    for a in content:
        for b in second:
            form = SYL[a] + SYL[b]
            if INV.content_key((a, b)) in taken:
                continue
            p_out = S[a, ex[:, 0]] * S[b, ex[:, 1]]
            p_in = S[ex[:, 0], a] * S[ex[:, 1], b]
            c = (weight * (f * p_out + efreq * p_in)).sum()
            c += EFFORT * f * (INV.length((a, b)) - 2.0)
            if c < best_c:
                best, best_c = form, c
    lexicon.append({"gloss": gloss, "field": field, "tier": tier, "form": best})
    write("lexicon.tsv", lexicon, ["gloss", "field", "tier", "form"])
    if antonyms:
        with open(os.path.join(DATA, "antonyms.tsv"), "a") as fh:
            for x in antonyms:
                fh.write(f"{gloss}\t{x}\n")
    print(f"{gloss} = {best}  (cost {best_c:.4f})")


def syllables(text):
    return sum(len(split(w)) for w in re.findall(r"[a-z]+", text.lower()))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("add-grammar"); g.add_argument("gloss"); g.add_argument("cls"); g.add_argument("freq", type=float)
    c = sub.add_parser("add-content"); c.add_argument("gloss"); c.add_argument("field"); c.add_argument("tier", type=int)
    c.add_argument("--antonym", action="append", default=[]); c.add_argument("--no-approximants", action="store_true")
    s = sub.add_parser("syllables"); s.add_argument("text")
    a = p.parse_args()
    if a.cmd == "add-grammar":
        add_grammar(a.gloss, a.cls, a.freq)
    elif a.cmd == "add-content":
        add_content(a.gloss, a.field, a.tier, a.antonym, a.no_approximants)
    else:
        print(syllables(a.text))

"""Add words to the language without disturbing existing ones, and measure texts.

data/grammar.tsv and data/lexicon.tsv are the source of truth. Existing words never
move: in a living language, words are stable. New words take the best free form.

  python words.py add-grammar GLOSS CLASS FREQ
  python words.py add-content GLOSS FIELD TIER [--antonym WORD] [--no-approximants]
  python words.py syllables "text in the language"
"""
import argparse, csv, os, re
import numpy as np
from confusion import CP, VP, CODA_MISS, SYLLABLES, syl_str

DATA = os.path.join(os.path.dirname(__file__), "..", "data")
SYL = [syl_str(s) for s in SYLLABLES]
IDX = {s: i for i, s in enumerate(SYL)}
S = np.array([[CP[a[0], b[0]] * VP[a[1], b[1]] * ((1 - CODA_MISS) if a[2] == b[2] else CODA_MISS)
               for b in SYLLABLES] for a in SYLLABLES])  # S[i, j] = P(hear j | said i)
TIER_FREQ = {5: 10, 4: 5, 3: 2.5, 2: 1.2, 1: 0.6}
EFFORT = 0.02
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
    grammar, lexicon = read("grammar.tsv"), read("lexicon.tsv")
    gsyl = {IDX[g["form"]] for g in grammar}
    csyl = {s for w in lexicon for s in split(w["form"])}
    best, best_c = None, float("inf")
    for cand in range(len(SYL)):
        if cand in gsyl or cand in csyl:
            continue
        c = 0.0
        for g in grammar:
            u = IDX[g["form"]]
            w = 3.0 if g["class"] == cls else 1.0
            if g["gloss"] == "NOT":
                w = 10.0
            c += w * (freq * S[cand, u] + float(g["freq"]) * S[u, cand])
        c += EFFORT * freq * 0.4 * bool(SYLLABLES[cand][2])
        if c < best_c:
            best, best_c = cand, c
    grammar.append({"gloss": gloss, "class": cls, "freq": freq, "form": SYL[best]})
    write("grammar.tsv", grammar, ["gloss", "class", "freq", "form"])
    print(f"{gloss} = {SYL[best]}  (cost {best_c:.4f}; {len(SYL) - len(gsyl) - len(csyl) - 1} free syllables left)")


def add_content(gloss, field, tier, antonyms=(), no_approximants=False):
    grammar, lexicon = read("grammar.tsv"), read("lexicon.tsv")
    gsyl = {IDX[g["form"]] for g in grammar}
    content = [i for i in range(len(SYL)) if i not in gsyl]
    if no_approximants:
        content = [i for i in content if SYLLABLES[i][0] not in APPROXIMANTS]
    second = [i for i in content if SYLLABLES[i][0] != ""]
    taken = {w["form"] for w in lexicon}
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
            if form in taken:
                continue
            p_out = S[a, ex[:, 0]] * S[b, ex[:, 1]]
            p_in = S[ex[:, 0], a] * S[ex[:, 1], b]
            c = (weight * (f * p_out + efreq * p_in)).sum()
            c += EFFORT * f * (0.4 * bool(SYLLABLES[a][2]) + 0.4 * bool(SYLLABLES[b][2])
                               - 0.1 * (SYLLABLES[a][0] == ""))
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

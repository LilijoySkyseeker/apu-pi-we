"""Should today's roots move? Compare ways of placing ~1,500 two-syllable roots (author, 2026-10-13: measure first).

  python3 placement.py [N]       # N = 1500 (uses ../part2b/roots-N.txt)

Strategies, all under the same constraints as tools/words.py (unique drift key, no offensive form,
no digit as first syllable, onset on the second syllable, senary forms reserved):
  A  today's roots fixed; new roots added one at a time in list order (what words.py does now)
  B  today's roots fixed; new roots re-placed together (coordinate descent until no move helps)
  C  everything re-placed together, today's roots included
Score: the words.py/build.py objective, summed over all pairs: meaning weight × (frequency-weighted
probability one word is heard as the other), plus the length effort term; lower is better. Also
reported: near pairs (pair confusion above today's 99th percentile) and the frequency-weighted mean
confusion with each word's nearest neighbour.

New concepts have no field or tier yet; they're approximated (Wordbank category → field, frequency
rank → tier). Good enough to compare strategies, not to choose final forms.
"""
import csv, os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../../../tools"))
import words as W
import offensive
from build import TIER_FREQ, EFFORT

INV, S, SYL = W.INV, W.S, W.SYL
n_syl = len(SYL)
FIXED = set("genso wanme inwun wemen konsin buntu tason nedin mesun manni buni donon lanno anko nuwen kiyo mena".split())  # two-syllable operators: part of the short-word layer, decided separately

WB_FIELD = {"animals": "animal", "food_drink": "food", "body_parts": "body", "clothing": "thing", "household": "thing",
            "furniture_rooms": "thing", "toys": "thing", "vehicles": "thing", "outside": "nature", "places": "space",
            "locations": "space", "people": "people", "action_words": "action", "descriptive_words": "quality",
            "time_words": "time"}


def load(N):
    lex = [r for r in W.read("lexicon.tsv") if len(W.split(r["form"])) == 2]
    old = [{"gloss": r["gloss"], "field": r["field"], "freq": TIER_FREQ[int(r["tier"])],
            "form": tuple(W.split(r["form"])), "old": True} for r in lex]
    rank = {}
    for l in open(os.path.join(HERE, "../concepts.tsv")).read().split("\n")[1:]:
        if l:
            r = l.split("\t"); rank.setdefault(r[1], int(r[0]))
    wb = {}
    for l in open(os.path.join(HERE, "../wordbank-merged.tsv")):
        r = l.rstrip("\n").split("\t")
        if len(r) > 3 and r[1].isdigit():
            wb.setdefault(r[2], r[0])
    wbcat = {r[0]: r[2] for r in (l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "../wordbank.tsv"))) if len(r) > 2}
    new = []
    for c in open(os.path.join(HERE, f"../part2b/roots-{N}.txt")).read().split("\n"):
        if not c:
            continue
        rk = rank.get(c, 3000)
        tier = 3 if rk <= 500 else 2 if rk <= 1500 else 1
        if c in wb:
            tier = max(tier, 2)
        field = WB_FIELD.get(wbcat.get(wb.get(c, ""), ""), "misc")
        new.append({"gloss": c, "field": field, "freq": TIER_FREQ[tier], "form": None, "old": False})
    return old, new


def weights(items):
    n = len(items)
    f = [it["field"] for it in items]
    Wm = np.where(np.equal.outer(f, f), 3.0, 1.0)
    num = np.array([x == "number" for x in f])
    Wm[num, :] = 10.0; Wm[:, num] = 10.0
    idx = {it["gloss"]: i for i, it in enumerate(items)}
    for l in open(os.path.join(W.DATA, "antonyms.tsv")):
        p = l.rstrip("\n").split("\t")
        if len(p) == 2 and p[0] in idx and p[1] in idx:
            Wm[idx[p[0]], idx[p[1]]] = Wm[idx[p[1]], idx[p[0]]] = 30.0
    np.fill_diagonal(Wm, 0.0)
    return Wm


def candidates():
    digits = W.digit_syllables()
    reserved = set()
    if os.path.exists(os.path.join(W.DATA, "senary.tsv")):
        reserved = {INV.content_key(W.split(r["form"])) for r in W.read("senary.tsv")}
    valid = np.zeros((n_syl, n_syl), bool)
    key = {}
    for a in range(n_syl):
        if a in digits:
            continue
        for b in range(n_syl):
            if INV.syl[b][0] == "":
                continue
            k = INV.content_key((a, b))
            if k in reserved or offensive.blocked(SYL[a] + SYL[b]):
                continue
            valid[a, b] = True
    for a in range(n_syl):  # every form has a key (today's words may sit on forms the checks now reject)
        for b in range(n_syl):
            key[(a, b)] = INV.content_key((a, b))
    length = np.array([[INV.length((a, b)) - 2.0 for b in range(n_syl)] for a in range(n_syl)])
    return valid, key, length


def cost_grid(i, forms, freq, Wm, mask_others):
    """Cost of every (a, b) for word i, given the other placed words."""
    A = np.array([forms[k][0] for k in mask_others]); B = np.array([forms[k][1] for k in mask_others])
    w = Wm[i, mask_others]
    out = freq[i] * (S[:, A] * w) @ S[:, B].T                  # i heard as k
    inn = (S[A, :].T * (w * freq[mask_others])) @ S[B, :]      # k heard as i
    return out + inn + EFFORT * freq[i] * LENGTH


def place(i, forms, freq, Wm, taken):
    others = [k for k in range(len(forms)) if k != i and forms[k] is not None]
    g = cost_grid(i, forms, freq, Wm, others)
    g = np.where(VALID, g, np.inf)
    own = KEY.get(forms[i]) if forms[i] is not None else None
    for k in taken:
        if k != own:
            pass
    order = np.argsort(g, axis=None)
    for flat in order[:4000]:
        a, b = divmod(int(flat), n_syl)
        if KEY[(a, b)] not in taken or KEY[(a, b)] == own:
            return (a, b), g[a, b]
    raise RuntimeError("no free form")


def total(forms, freq, Wm):
    F = np.array(forms)
    P = S[F[:, 0]][:, F[:, 0]] * S[F[:, 1]][:, F[:, 1]]     # P[i, j]: i heard as j
    np.fill_diagonal(P, 0.0)
    conf = (Wm * freq[:, None] * P).sum()
    eff = EFFORT * sum(freq[i] * LENGTH[f] for i, f in enumerate(forms))
    nn = (P + P.T).max(1)
    return conf + eff, P + P.T, (freq * nn).sum() / freq.sum()


def descend(forms, freq, Wm, movable, rounds=8):
    taken = {KEY[f]: i for i, f in enumerate(forms)}
    for r in range(rounds):
        moved = 0
        for i in movable:
            del taken[KEY[forms[i]]]
            new, _ = place(i, forms, freq, Wm, taken)
            if new != forms[i]:
                moved += 1
            forms[i] = new
            taken[KEY[new]] = i
        print(f"    round {r + 1}: {moved} moved", flush=True)
        if moved == 0:
            break
    return forms


def report(name, forms, freq, Wm, thr, old_forms, n_old):
    t, P, nn = total(forms, freq, Wm)
    iu = np.triu_indices(len(forms), 1)
    near = int((P[iu] > thr).sum())
    moved = sum(forms[i] != old_forms[i] for i in range(n_old))
    print(f"{name}: score {t:.2f} | near pairs {near} | nearest-neighbour confusion {nn:.5f} | today's roots moved {moved}")
    return t


if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    old, new = load(N)
    items = old + new
    n_old = len(old)
    freq = np.array([it["freq"] for it in items])
    Wm = weights(items)
    VALID, KEY, LENGTH = candidates()
    old_forms = [it["form"] for it in old]
    fixed = [i for i, it in enumerate(old) if SYL[it["form"][0]] + SYL[it["form"][1]] in FIXED]
    print(f"{n_old} two-syllable roots today, {len(new)} new; {int(VALID.sum())} usable forms")

    # today's 99th percentile of pair confusion, for "near pairs"
    _, P0, _ = total(old_forms, freq[:n_old], Wm[:n_old, :n_old])
    thr = np.quantile(P0[np.triu_indices(n_old, 1)], 0.99)
    report("today (517 only)", old_forms, freq[:n_old], Wm[:n_old, :n_old], thr, old_forms, n_old)

    # A: one at a time
    forms = old_forms + [None] * len(new)
    taken = {KEY[f]: i for i, f in enumerate(old_forms)}
    for i in range(n_old, len(items)):
        forms[i], _ = place(i, forms, freq, Wm, taken)
        taken[KEY[forms[i]]] = i
    A = list(forms)
    report("A one at a time", A, freq, Wm, thr, old_forms, n_old)

    print("  B: new roots re-placed together")
    B = descend(list(A), freq, Wm, list(range(n_old, len(items))))
    report("B batch the new", B, freq, Wm, thr, old_forms, n_old)

    print("  C: everything re-placed together")
    C = descend(list(B), freq, Wm, [i for i in range(len(items)) if i not in fixed])
    report("C all together", C, freq, Wm, thr, old_forms, n_old)

    with open(os.path.join(HERE, f"placement-{N}.tsv"), "w") as f:
        f.write("gloss\ttoday\tA\tB\tC\n")
        for i, it in enumerate(items):
            show = lambda x: "" if x is None else SYL[x[0]] + SYL[x[1]]
            f.write(f"{it['gloss']}\t{show(old_forms[i]) if i < n_old else ''}\t{show(A[i])}\t{show(B[i])}\t{show(C[i])}\n")

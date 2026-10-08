"""Which number base transmits numbers most reliably through noise? (2026-10-08)

For each base b, find the best set of b digit words under this language's sound rules, then
estimate, for a random quantity of a given size:
  - digits needed, syllables spoken, and the chance that at least one digit is misheard
    as another digit (the error that silently changes the value).
Confusion data: tools/confusion.py (Miller & Nicely 1955 at -6 dB, plus estimates).
Two digit-word shapes are tested: one open syllable (CV) and two (CV.CV).

  python base_test.py
"""
import math, random
import numpy as np
from build import Inventory, FULL

INV = Inventory([c for c in FULL if c != "z"])
OPEN = [i for i, s in enumerate(INV.syl) if s[2] == "" and s[0] != ""]  # CV syllables
DEVOICE = {"b": "p", "d": "t", "g": "k"}


def drift_key(form):
    return tuple(DEVOICE.get(INV.syl[s][0], INV.syl[s][0]) + {"e": "i", "o": "u"}.get(INV.syl[s][1], INV.syl[s][1])
                 for s in form)


def p_confuse(a, b):
    return math.prod(INV.S[x, y] for x, y in zip(a, b))


def best_set(b, n_syl, steps=60000, seed=0):
    rng = random.Random(seed)
    pool = [(x,) for x in OPEN] if n_syl == 1 else [(x, y) for x in OPEN for y in OPEN]

    def cost(sel):
        c = sum(p_confuse(x, y) + p_confuse(y, x) for i, x in enumerate(sel) for y in sel[i + 1:])
        keys = [drift_key(x) for x in sel]
        return c + 10.0 * (len(keys) - len(set(keys)))

    sel = rng.sample(pool, b)
    cur = cost(sel)
    for step in range(steps):
        k = rng.randrange(b)
        new = rng.choice(pool)
        if new in sel:
            continue
        old = sel[k]
        sel[k] = new
        c = cost(sel)
        if c <= cur or rng.random() < math.exp(-(c - cur) / (1e-4 * (1 - step / steps) + 1e-9)):
            cur = c
        else:
            sel[k] = old
    return sel


def per_digit_error(sel):
    """Mean probability that a digit is heard as some other digit of the set."""
    return float(np.mean([sum(p_confuse(x, y) for y in sel if y != x) for x in sel]))


def main():
    print("base  shape   P(digit->other digit)  digits/quantity  syllables  P(any digit wrong)")
    for n_syl in (1, 2):
        for b in (6, 8, 10, 12):
            sel = best_set(b, n_syl)
            p = per_digit_error(sel)
            for mag, label in ((1e3, "~1,000"), (1e6, "~1,000,000"), (1e10, "10-digit ID")):
                d = math.ceil(math.log(mag) / math.log(b))
                p_any = 1 - (1 - p) ** d
                print(f"{b:>4}  {'CV' if n_syl == 1 else 'CV.CV':5}   {p:.5f}               "
                      f"{d:>2} ({label:>10})   {d * n_syl:>3}      {p_any:.5f}")
            print(f"      words: {' '.join(INV.show(f) for f in sel)}")


if __name__ == "__main__":
    main()

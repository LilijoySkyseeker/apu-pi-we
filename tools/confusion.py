"""Confusion model for the conlang's sound system, and an optimizer that
assigns syllables to grammar words and number words so they are hard to mishear.

Consonant data: Miller & Nicely 1955, Table III (S/N = -6 dB, 200-6500 Hz),
transcribed for the 12 of our consonants they tested. Everything marked
ASSUMPTION is an estimate, not data.
"""
import functools, itertools, math, random

# ---------- consonants: Miller & Nicely 1955, Table III, -6 dB ----------
MN_ORDER = "p t k f θ s ʃ b d g v ð z ʒ m n".split()
MN_ROWS = {  # spoken -> counts of responses, columns in MN_ORDER
    "p": [80, 43, 64, 17, 14, 6, 2, 1, 1, 0, 1, 1, 0, 0, 2, 0],
    "t": [71, 84, 55, 5, 9, 3, 8, 1, 0, 0, 0, 1, 2, 0, 2, 3],
    "k": [66, 76, 107, 12, 8, 9, 4, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    "f": [18, 12, 9, 175, 48, 11, 1, 7, 2, 1, 2, 2, 0, 0, 0, 0],
    "s": [8, 5, 4, 23, 39, 107, 45, 4, 2, 3, 1, 1, 3, 2, 0, 1],
    "b": [1, 0, 0, 5, 4, 4, 0, 136, 10, 9, 47, 16, 6, 1, 5, 4],
    "d": [0, 0, 0, 0, 0, 0, 8, 5, 80, 45, 11, 20, 20, 26, 1, 0],
    "g": [0, 0, 0, 0, 2, 0, 0, 3, 63, 66, 3, 19, 37, 56, 0, 3],
    "v": [0, 0, 0, 2, 0, 2, 0, 48, 5, 5, 145, 45, 12, 0, 4, 0],
    "z": [0, 0, 0, 0, 1, 1, 1, 7, 20, 27, 16, 28, 94, 44, 0, 1],
    "m": [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 4, 1, 3, 0, 177, 46],
    "n": [0, 0, 0, 0, 4, 0, 0, 1, 5, 2, 0, 7, 1, 6, 47, 163],
}
MN_SET = list(MN_ROWS)
APPROX = ["l", "w", "j"]
CONS = MN_SET + APPROX
ONSETS = [""] + CONS  # "" = vowel-initial syllable


def consonant_matrix():
    P = {}
    for a in MN_SET:  # renormalize over our consonants only
        row = MN_ROWS[a]
        tot = sum(row[MN_ORDER.index(b)] for b in MN_SET)
        for b in MN_SET:
            P[a, b] = row[MN_ORDER.index(b)] / tot
    # ASSUMPTION: approximants, no Miller & Nicely data.
    place = {"p": 0, "b": 0, "m": 0, "f": 0, "v": 0, "w": 0,
             "t": 1, "d": 1, "n": 1, "s": 1, "z": 1, "l": 1,
             "k": 2, "g": 2, "j": 2}
    voiced = set("b d g v z m n l w j".split())
    for a in APPROX:
        for b in CONS:
            if a == b:
                continue
            if b in APPROX:
                p = 0.06
            elif b in voiced:
                p = 0.03 if place[a] == place[b] else 0.01
            else:
                p = 0.003
            P[a, b] = P[b, a] = p * (0.5 if b in MN_SET else 1)
    for a in CONS:  # fill approximant rows/diagonals so rows sum to 1
        off = sum(P.get((a, b), 0) for b in CONS if b != a)
        if a in APPROX:
            P[a, a] = 1 - off
        else:  # scale MN row to leave room for approximant confusions
            extra = sum(P[a, b] for b in APPROX)
            for b in MN_SET:
                P[a, b] *= (1 - extra)
    # ASSUMPTION: a missing onset vs a weak consonant.
    weak = {"w": 0.05, "j": 0.05, "l": 0.03, "v": 0.03, "f": 0.03}
    for b in CONS:
        p = weak.get(b, 0.005)
        P["", b] = p / 3
        P[b, ""] = p
        P[b, b] -= p
    P["", ""] = 1 - sum(P["", b] for b in CONS)
    return P


VOWELS = "i e a o u".split()
def vowel_matrix():  # ASSUMPTION: 5 well-spread vowels; neighbours confuse most
    adj = {("i", "e"), ("e", "a"), ("a", "o"), ("o", "u")}
    same_height = {("i", "u"), ("e", "o")}
    P = {}
    for a in VOWELS:
        for b in VOWELS:
            if a == b:
                continue
            k = (a, b) if (a, b) in adj | same_height else (b, a)
            P[a, b] = 0.04 if k in adj else 0.01 if k in same_height else 0.003
        P[a, a] = 1 - sum(P[a, b] for b in VOWELS if b != a)
    return P


CODA_MISS = 0.08  # ASSUMPTION: final -n lost or added


CP, VP = consonant_matrix(), vowel_matrix()
SYLLABLES = [(o, v, c) for o in ONSETS for v in VOWELS for c in ("", "n")]


def syl_str(s):
    return s[0].replace("j", "y") + s[1] + s[2]


@functools.lru_cache(maxsize=None)
def p_syl(a, b):
    pc = 1 - CODA_MISS if a[2] == b[2] else CODA_MISS
    return CP[a[0], b[0]] * VP[a[1], b[1]] * pc


def p_word(a, b):  # same-length words, syllable by syllable
    return math.prod(p_syl(x, y) for x, y in zip(a, b)) if len(a) == len(b) else 0.0


def length(s):
    return (0.8 if s[0] == "" else 1.0) + (0.4 if s[2] else 0.0)


# ---------- grammar words ----------
# (gloss, class, relative frequency)  frequencies are rough guesses from English analogs
GRAMMAR = [
    ("I", "pron", 10), ("YOU", "pron", 8), ("WE.incl", "pron", 3), ("WE.excl", "pron", 3),
    ("HE/SHE/IT", "pron", 8), ("OBVIATIVE", "pron", 2), ("LOGOPHOR", "pron", 1), ("SIDE.A", "pron", 0.5), ("SIDE.B", "pron", 0.5),
    ("PLURAL", "det", 4), ("THIS", "det", 4), ("THAT.dem", "det", 3), ("ALL", "det", 3),
    ("SOME", "det", 2), ("PART", "det", 1), ("NONE", "det", 1),
    ("Q", "act", 4), ("REQUEST", "act", 2), ("INSTRUCT", "act", 1.5), ("ADVISE", "act", 1),
    ("INTEND", "act", 2), ("WARN", "act", 0.5), ("NONLITERAL", "act", 0.5),
    ("WH", "op", 3), ("UNSPEC", "op", 1), ("NOT", "op", 7), ("CONF", "op", 1.5),
    ("SEEN", "op", 0.5), ("TOLD", "op", 0.8), ("INFER", "op", 0.5),
    ("DONE", "asp", 3), ("ONGOING", "asp", 2), ("SOON", "asp", 1.5),
    ("OF", "rel", 8), ("AT", "rel", 5), ("TO", "rel", 5), ("FROM", "rel", 3), ("WITH", "rel", 3),
    ("FOR", "rel", 3), ("BEFORE", "rel", 1.5), ("AFTER", "rel", 1.5),
    ("AND", "link", 9), ("OR", "link", 2), ("BUT", "link", 2), ("IF", "link", 2),
    ("BECAUSE", "link", 1.5), ("THAT.comp", "link", 5), ("WHO.rel", "link", 4),
]
# Pairs whose confusion flips the meaning: weighted heavily.
OPPOSITES = [
    ("WE.incl", "WE.excl"), ("HE/SHE/IT", "OBVIATIVE"), ("HE/SHE/IT", "LOGOPHOR"), ("OBVIATIVE", "LOGOPHOR"), ("SIDE.A", "SIDE.B"),
    ("I", "YOU"), ("ALL", "NONE"), ("SOME", "NONE"), ("SOME", "PART"), ("ALL", "PART"),
    ("THIS", "THAT.dem"), ("INSTRUCT", "ADVISE"), ("REQUEST", "INSTRUCT"),
    ("SEEN", "TOLD"), ("SEEN", "INFER"), ("TOLD", "INFER"), ("DONE", "SOON"),
    ("DONE", "ONGOING"), ("BEFORE", "AFTER"), ("TO", "FROM"), ("AND", "OR"),
    ("NONLITERAL", "WARN"),
]
# NOT is special: confusing it with anything, or with silence, flips meaning.
CRITICAL_ANY = {"NOT"}
EFFORT = 0.0004  # weight of length cost relative to confusion cost


def pair_weights(words, classes, opposites, critical):
    W = {}
    idx = {w: i for i, w in enumerate(words)}
    for i, j in itertools.permutations(range(len(words)), 2):
        w = 3.0 if classes[i] == classes[j] else 1.0
        if words[i] in critical or words[j] in critical:
            w = max(w, 10.0)
        W[i, j] = w
    for a, b in opposites:
        W[idx[a], idx[b]] = W[idx[b], idx[a]] = 30.0
    return W


def anneal(n_items, pool, cost_pair, cost_self, steps=200000, seed=1, T0=None):
    rng = random.Random(seed)
    assign = rng.sample(range(len(pool)), n_items)
    used = set(assign)

    def item_cost(i, s):
        c = cost_self(i, s)
        for j in range(n_items):
            if j != i:
                c += cost_pair(i, s, j, assign[j])
        return c

    total = sum(cost_self(i, assign[i]) for i in range(n_items)) + sum(
        cost_pair(i, assign[i], j, assign[j]) for i in range(n_items) for j in range(i + 1, n_items))
    T0 = T0 or total / n_items
    best, best_total = list(assign), total
    for step in range(steps):
        T = T0 * (1 - step / steps) + 1e-9
        i = rng.randrange(n_items)
        if rng.random() < 0.5:  # move to an unused syllable
            new = rng.randrange(len(pool))
            if new in used:
                continue
            old = assign[i]
            before = item_cost(i, old)
            assign[i] = new
            delta = item_cost(i, new) - before
            if delta < 0 or rng.random() < math.exp(-delta / T):
                used.discard(old); used.add(new); total += delta
            else:
                assign[i] = old
        else:  # swap two items
            j = rng.randrange(n_items)
            if i == j:
                continue
            a, b = assign[i], assign[j]
            before = item_cost(i, a) + item_cost(j, b) - cost_pair(i, a, j, b)
            assign[i], assign[j] = b, a
            after = item_cost(i, b) + item_cost(j, a) - cost_pair(i, b, j, a)
            delta = after - before
            if delta < 0 or rng.random() < math.exp(-delta / T):
                total += delta
            else:
                assign[i], assign[j] = a, b
        if total < best_total:
            best, best_total = list(assign), total
    return best, best_total


def grammar_run(seed=1):
    words = [g[0] for g in GRAMMAR]
    classes = [g[1] for g in GRAMMAR]
    freq = [g[2] for g in GRAMMAR]
    pool = [(s,) for s in SYLLABLES]
    W = pair_weights(words, classes, OPPOSITES, CRITICAL_ANY)

    def cost_pair(i, si, j, sj):
        a, b = pool[si], pool[sj]
        return freq[i] * p_word(a, b) * W[i, j] + freq[j] * p_word(b, a) * W[j, i]

    def cost_self(i, si):
        return EFFORT * freq[i] * length(pool[si][0]) * 100

    best, cost = anneal(len(words), pool, cost_pair, cost_self, seed=seed)
    return words, classes, freq, pool, best, cost, cost_pair


# ---------- number words ----------
NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
           "ten", "hundred", "thousand"]


def number_run(seed=1):
    cv = [s for s in SYLLABLES if s[2] == "" and s[0] != ""]  # CV only: digits are frequent
    pool = [(a, b) for a in cv for b in cv]
    freq = [1.0] * len(NUMBERS)

    def cost_pair(i, si, j, sj):
        a, b = pool[si], pool[sj]
        # also penalize words that differ only in one syllable that is a near-miss
        return 30 * (p_word(a, b) + p_word(b, a))

    best, cost = anneal(len(NUMBERS), pool, cost_pair, lambda i, s: 0.0, steps=150000, seed=seed)
    return pool, best, cost, cost_pair


def random_baseline(n, pool, cost_pair, trials=200, seed=7):
    rng = random.Random(seed)
    costs = []
    for _ in range(trials):
        a = rng.sample(range(len(pool)), n)
        costs.append(sum(cost_pair(i, a[i], j, a[j]) for i in range(n) for j in range(i + 1, n)))
    costs.sort()
    return costs[len(costs) // 2]


if __name__ == "__main__":
    words, classes, freq, pool, best, cost, cp = grammar_run()
    base = random_baseline(len(words), pool, cp)
    print(f"GRAMMAR WORDS  cost={cost:.4f}  random-assignment median={base:.4f}")
    for cls in ["act", "op", "pron", "det", "asp", "rel", "link"]:
        row = [f"{words[i]}={syl_str(pool[best[i]][0])}" for i in range(len(words)) if classes[i] == cls]
        print(f"  {cls:5s} " + "  ".join(row))
    pairs = sorted(((cp(i, best[i], j, best[j]), words[i], words[j]) for i in range(len(words))
                    for j in range(i + 1, len(words))), reverse=True)[:8]
    print("  worst remaining pairs:", ", ".join(f"{a}/{b} {c:.4f}" for c, a, b in pairs))

    pool_n, best_n, cost_n, cp_n = number_run()
    base_n = random_baseline(len(NUMBERS), pool_n, cp_n)
    print(f"\nNUMBER WORDS  cost={cost_n:.5f}  random-assignment median={base_n:.5f}")
    print("  " + "  ".join(f"{NUMBERS[i]}={''.join(syl_str(s) for s in pool_n[best_n[i]])}"
                         for i in range(len(NUMBERS))))
    pairs = sorted(((cp_n(i, best_n[i], j, best_n[j]), NUMBERS[i], NUMBERS[j])
                    for i in range(len(NUMBERS)) for j in range(i + 1, len(NUMBERS))), reverse=True)[:5]
    print("  worst remaining pairs:", ", ".join(f"{a}/{b} {c:.5f}" for c, a, b in pairs))

    # sanity: the consonant pairs the data says are most confusable
    cm = sorted(((CP[a, b] + CP[b, a], a, b) for a, b in itertools.combinations(MN_SET, 2)), reverse=True)[:8]
    print("\nMost confusable consonant pairs at -6 dB (Miller & Nicely):",
          ", ".join(f"{a}/{b} {c:.2f}" for c, a, b in cm))

"""Lexicon v0 generator (historical). It produced data/lexicon.tsv on 2026-10-08.
Re-running writes data/lexicon_v0_regenerated.tsv and never touches the live lexicon;
use words.py to add words.

Assigns two-syllable forms to core concepts and number words.

Principles:
- Syllables are partitioned: content words never contain a grammar-word syllable,
  so any grammar syllable a listener hears is a grammar word.
- Confusion cost is weighted by how substitutable two meanings are: antonyms worst,
  same semantic field next, everything else baseline. Numbers are kept far from
  each other and from everything.
- Frequent concepts get the shortest forms (CV.CV); rare ones may take a final -n.
"""
import itertools, math, os, random, sys
import numpy as np
from confusion import CP, VP, CODA_MISS, SYLLABLES, syl_str

# ---------- grammar words: current table, plus additions placed greedily ----------
GRAMMAR = {
    "Q": "yun", "REQUEST": "fu", "INSTRUCT": "gon", "ADVISE": "to", "INTEND": "zin", "WARN": "ze",
    "NONLITERAL": "san", "WH": "mi", "UNSPEC": "wan", "NOT": "na", "CONF": "mon", "SEEN": "kin",
    "TOLD": "sun", "INFER": "ven", "I": "e", "YOU": "vun", "WE.incl": "nin", "WE.excl": "so",
    "HE/SHE/IT": "lu", "OBVIATIVE": "tan", "LOGOPHOR": "gan", "SIDE.A": "ku", "SIDE.B": "sin",
    "PLURAL": "in", "THIS": "va", "THAT.dem": "nun", "ALL": "len", "SOME": "vi", "PART": "kon",
    "NONE": "bon", "DONE": "fa", "ONGOING": "gi", "SOON": "yan", "OF": "on", "AT": "yi", "TO": "ke",
    "FROM": "gen", "WITH": "zo", "FOR": "men", "BEFORE": "fi", "AFTER": "tun", "AND": "gu",
    "OR": "be", "BUT": "fen", "IF": "ti", "BECAUSE": "win", "THAT.comp": "yo", "WHO.rel": "mu",
}
NEW_GRAMMAR = [("BE", 8), ("MORE", 3), ("VERY", 3), ("LIKE", 3)]  # copula; comparison; degree; similarity

SYL_STR = [syl_str(s) for s in SYLLABLES]
N = len(SYLLABLES)
S = np.array([[CP[a[0], b[0]] * VP[a[1], b[1]] * ((1 - CODA_MISS) if a[2] == b[2] else CODA_MISS)
               for b in SYLLABLES] for a in SYLLABLES])  # S[i, j] = P(hear j | said i)
idx = {s: i for i, s in enumerate(SYL_STR)}


def place_new_grammar():
    used = {idx[v] for v in GRAMMAR.values()}
    for word, freq in NEW_GRAMMAR:
        best, best_c = None, 1e9
        for cand in range(N):
            if cand in used or SYLLABLES[cand][2]:  # frequent: no coda
                continue
            c = sum(S[cand, u] + S[u, cand] for u in used) * freq
            c += 10 * (S[cand, idx["na"]] + S[idx["na"], cand])  # keep away from NOT
            if c < best_c:
                best, best_c = cand, c
        used.add(best)
        GRAMMAR[word] = SYL_STR[best]
    return used


# ---------- concepts: (gloss, field, frequency tier 1-5) ----------
C = """
person people 5|child people 4|man people 3|woman people 3|friend people 3|family people 2|mother people 3|father people 3|name people 3|group people 2|enemy people 2
body body 3|head body 3|eye body 3|ear body 2|nose body 2|mouth body 3|tooth body 2|tongue body 1|hair body 2|hand body 4|foot body 3|leg body 2|heart body 3|blood body 2|bone body 2|skin body 2|back body 2|belly body 1
water nature 5|fire nature 3|ground nature 3|stone nature 3|sky nature 2|sun nature 3|moon nature 2|star nature 2|rain nature 3|wind nature 2|tree nature 3|leaf nature 1|wood nature 2|sea nature 2|river nature 2|mountain nature 2|sand nature 1|smoke nature 1|cloud nature 1|light nature 3|storm nature 2|snow nature 1|ice nature 1|salt nature 1|ash nature 1|plant nature 2
animal animal 3|dog animal 3|bird animal 3|fish animal 3|horse animal 2|cow animal 1|snake animal 1|insect animal 1|egg animal 2|wing animal 1|tail animal 1|meat animal 2
house thing 4|door thing 2|food thing 4|tool thing 2|rope thing 1|boat thing 2|cart thing 2|cloth thing 2|money thing 3|book thing 2|weapon thing 2|bed thing 2|cup thing 1|thing thing 5
day time 4|night time 3|year time 3|time time 4|morning time 2|evening time 1|moment time 2
place space 4|inside space 3|outside space 2|above space 3|below space 3|front space 2|near space 3|far space 3|left space 2|right space 2|road space 3
many size 4|few size 3|big size 4|small size 4|long size 3|short size 2|wide size 1|heavy size 2|light.weight size 1|thick size 1|full size 2|empty size 2|half size 2|whole size 2
good quality 5|bad quality 4|new quality 3|old quality 3|true quality 3|same quality 3|other quality 4|hot quality 2|cold quality 2|wet quality 1|dry quality 1|hard quality 2|soft quality 1|sharp quality 1|fast quality 2|slow quality 2|strong quality 2|weak quality 1|clean quality 1|dirty quality 1|beautiful quality 2|important quality 2|easy quality 2|difficult quality 2|ready quality 2|sick quality 2|dead quality 2
black color 2|white color 2|red color 2|green color 1|yellow color 1|blue color 1
think mind 5|know mind 5|want mind 5|feel mind 4|like mind 4|fear mind 3|hope mind 2|remember mind 3|forget mind 2|learn mind 3|understand mind 3|mean mind 3|choose mind 2|need mind 4|can mind 5|must mind 3|try mind 3|happy mind 3|sad mind 2|angry mind 2|pain mind 2
see sense 5|hear sense 4|say sense 5|tell sense 4|ask sense 3|talk sense 3|word sense 4|call sense 2|show sense 3|look sense 3|listen sense 2|sing sense 1|write sense 2|read sense 2|laugh sense 2|cry sense 2
go motion 5|come motion 5|move motion 3|walk motion 2|run motion 3|fly motion 2|swim motion 1|fall motion 2|sit motion 3|stand motion 3|lie.down motion 2|enter motion 2|leave motion 3|return motion 3|arrive motion 2|follow motion 2|carry motion 2|push motion 1|pull motion 1|throw motion 1|turn motion 2|stop motion 3|start motion 3|wait motion 3|stay motion 3
do action 5|have action 5|give action 4|take action 4|get action 3|put action 3|hold action 2|use action 3|find action 3|lose action 2|keep action 2|open action 2|close action 2|break action 2|cut action 2|hit action 2|eat action 4|drink action 3|sleep action 3|wake action 2|work action 4|play action 3|help action 4|fight action 2|kill action 2|die action 3|live action 4|grow action 2|burn action 2|build action 2|buy action 2|sell action 2|pay action 2|wash action 1|cook action 2|wear action 2|hide action 2|change action 3|happen action 4|win action 2
way abstract 3|kind abstract 3|reason abstract 2|problem abstract 3|idea abstract 2|story abstract 2|rule abstract 2|war abstract 1|peace abstract 1|game abstract 2|life abstract 3|power abstract 2|magic abstract 2|god abstract 1
"""
CONCEPTS = [tuple(x.split()) for line in C.strip().splitlines() for x in line.split("|")]
CONCEPTS = [(g, f, int(t)) for g, f, t in CONCEPTS]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "100", "1000"]
ANTONYMS_RAW = """good bad|big small|long short|hot cold|new old|come go|give take|open close|live die|find lose
buy sell|many few|full empty|fast slow|strong weak|hard soft|wet dry|clean dirty|near far|above below
inside outside|left right|front back|day night|black white|happy sad|remember forget|start stop|man woman
mother father|easy difficult|heavy light.weight|sit stand|enter leave|same other|sun moon|push pull
sleep wake|morning evening|friend enemy|war peace|go return|come leave|win lose|ask tell|want fear"""
ANTONYMS = [tuple(a.split()) for a in ANTONYMS_RAW.replace("\n", "|").split("|") if a.strip()]
TIER_FREQ = {5: 10, 4: 5, 3: 2.5, 2: 1.2, 1: 0.6}
EFFORT = 0.02  # cost of extra length beyond CV.CV, per unit frequency


def main(steps=400000, seed=1):
    used = place_new_grammar()
    grammar_syls = used
    content_syls = [i for i in range(N) if i not in grammar_syls]
    first = content_syls
    second = [i for i in content_syls if SYLLABLES[i][0] != ""]
    pool = np.array([(a, b) for a in first for b in second])
    lengths = np.array([2.0 + 0.4 * bool(SYLLABLES[a][2]) + 0.4 * bool(SYLLABLES[b][2])
                        - 0.1 * (SYLLABLES[a][0] == "") for a, b in pool])

    items = [(g, f, TIER_FREQ[t]) for g, f, t in CONCEPTS] + [(n, "number", 3.0) for n in NUMBERS]
    n = len(items)
    names = [x[0] for x in items]
    fields = [x[1] for x in items]
    freq = np.array([x[2] for x in items])
    W = np.ones((n, n))
    for i, j in itertools.product(range(n), repeat=2):
        if fields[i] == fields[j]:
            W[i, j] = 3.0
        if fields[i] == "number" or fields[j] == "number":
            W[i, j] = 30.0 if fields[i] == fields[j] else 10.0
    pos = {g: i for i, g in enumerate(names)}
    for a, b in ANTONYMS:
        W[pos[a], pos[b]] = W[pos[b], pos[a]] = 30.0
    np.fill_diagonal(W, 0)

    rng = random.Random(seed)
    assign = np.array(rng.sample(range(len(pool)), n))

    def conf_vec(form, others):  # symmetric confusion of one form with each other form
        a, b = pool[form]
        A, B = pool[others, 0], pool[others, 1]
        return S[a, A] * S[b, B], S[A, a] * S[B, b]

    def item_cost(i, form):
        p_out, p_in = conf_vec(form, assign)
        c = freq[i] * p_out * W[i] + freq * p_in * W[:, i]
        c[i] = 0
        return c.sum() + EFFORT * freq[i] * (lengths[form] - 2.0)

    def total_cost():
        return sum(item_cost(i, assign[i]) for i in range(n)) / 2  # pairs counted twice; effort halved too

    used_forms = set(assign.tolist())
    cur = total_cost()
    T0 = cur / n
    best, best_c = assign.copy(), cur
    for step in range(steps):
        T = T0 * (1 - step / steps) + 1e-12
        i = rng.randrange(n)
        new = rng.randrange(len(pool))
        if new in used_forms:
            continue
        old = assign[i]
        before = item_cost(i, old)
        assign[i] = new
        delta = item_cost(i, new) - before
        if delta < 0 or rng.random() < math.exp(-delta / T):
            used_forms.discard(int(old)); used_forms.add(new); cur += delta
            if cur < best_c:
                best, best_c = assign.copy(), cur
        else:
            assign[i] = old

    assign = best
    # random baseline (confusion part only, same weights)
    def conf_total(a):
        tot = 0.0
        for i in range(n):
            p_out, _ = conf_vec(a[i], a)
            p_out[i] = 0
            tot += (freq[i] * p_out * W[i]).sum()
        return tot
    base = np.median([conf_total(np.array(rng.sample(range(len(pool)), n))) for _ in range(20)])
    print(f"confusion cost {conf_total(assign):.4f}  vs random median {base:.4f}")
    print("new grammar words:", {w: GRAMMAR[w] for w, _ in NEW_GRAMMAR})
    print(f"content syllables available: {len(content_syls)} of {N}; grammar uses {len(grammar_syls)}")

    form = {names[i]: SYL_STR[pool[assign[i]][0]] + SYL_STR[pool[assign[i]][1]] for i in range(n)}
    with open(os.path.join(os.path.dirname(__file__), "..", "data", "lexicon_v0_regenerated.tsv"), "w") as fh:
        for i in range(n):
            fh.write(f"{names[i]}\t{fields[i]}\t{form[names[i]]}\n")
    by_field = {}
    for i in range(n):
        by_field.setdefault(fields[i], []).append(f"{names[i]}={form[names[i]]}")
    for f, xs in by_field.items():
        print(f"[{f}] " + " ".join(xs))
    worst = []
    for i in range(n):
        p_out, p_in = conf_vec(assign[i], assign)
        for j in range(i + 1, n):
            worst.append(((freq[i] * p_out[j] * W[i, j] + freq[j] * p_in[j] * W[j, i]), names[i], names[j]))
    worst.sort(reverse=True)
    print("worst pairs:", ", ".join(f"{a}/{b}({form[a]}/{form[b]}) {c:.4f}" for c, a, b in worst[:10]))
    ants = [(a, b, form[a], form[b]) for a, b in ANTONYMS]
    print("antonyms:", ", ".join(f"{a}={x}/{b}={y}" for a, b, x, y in ants))
    lens = {t: np.mean([len(form[g]) for g, f, tt in CONCEPTS if tt == t]) for t in range(1, 6)}
    print("mean letters by frequency tier:", {t: round(v, 2) for t, v in lens.items()})


if __name__ == "__main__":
    main(steps=int(sys.argv[1]) if len(sys.argv) > 1 else 400000)

"""Compare mishearing model v1 (tools/confusion.py) and v2 (tools/confusion2.py) before switching
the optimizers (author, 2026-10-13). Read-only: changes no word and no data file.

  (a) how well each model reproduces the published matrices (consonants, onset loss, vowels)
  (b) which pairs of today's words each model ranks most confusable
  (c) the 16 merger pairs of tests/shortwords-01/README.md under each listener-group variant
  (d) how much the pair ranking varies across the 48 robustness variants (§6)
  (e) junction misparses among today's words under v2 (n + vowel, n + nasal, coda loss)

  python3 check.py > results.txt
"""
import csv, itertools, os, re, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
sys.path.insert(0, os.path.join(ROOT, "tools"))
import confusion2 as M2

CONS, ONSETS, OI, VOWELS = M2.CONS, M2.ONSETS, M2.OI, M2.VOWELS
E = 0.20
pct = lambda x: f"{100 * x:5.1f}"


def read(name):
    with open(os.path.join(ROOT, "data", name)) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def split(form):
    parts = re.findall(r"[^aeiou]?[aeiou](?:n(?![aeiou]))?", form)
    assert "".join(parts) == form, form
    return tuple(M2.IDX[p] for p in parts)


def show(w):
    return "".join(M2.NAME[s] for s in w)


# ---------------------------------------------------------------- word lists
gram = read("grammar.tsv")
nums = read("numbers.tsv")
lex = read("lexicon.tsv")
SHORT = [(g["gloss"], g["form"]) for g in gram] + [(f"digit{r['value']}", r["form"]) for r in nums
                                                    if r["kind"] == "digit" and len(split(r["form"])) == 1]
CONTENT = [(w["gloss"], w["form"]) for w in lex]
short_w = [split(f) for _, f in SHORT]
content_w = [split(f) for _, f in CONTENT]

V = M2.variants()
VN = [n for n, _ in V]
MODELS = {n: M2.Model(p) for n, p in V}
v1, best = MODELS["v1"], MODELS["best"]
shared = M2.Model(M2.no_groups())  # v2 without listener groups: the shared acoustic pattern


def sym_pairs(model, words):
    P = model.word_matrix(words)
    Q = (P + P.T) / 2
    iu = np.triu_indices(len(words), 1)
    return Q[iu], iu


def ranks(x):
    """Rank 1 = most confusable."""
    r = np.empty(len(x), int)
    r[np.argsort(-x, kind="stable")] = np.arange(1, len(x) + 1)
    return r


def spearman(a, b):
    ra, rb = ranks(a).astype(float), ranks(b).astype(float)
    return float(np.corrcoef(ra, rb)[0, 1])


# ================================================================= (a)
print("=" * 100)
print("(a) PUBLISHED MATRICES. Each source level-matched to mean onset error 0.20 ('heard no consonant'")
print("    folded into the diagonal); models compared on the 78 symmetric consonant-pair confusions.")
print("    v2 in-sample = mix of 4 (contains the source); v2 leave-one-out = mix of the other 3.")
print("    rho = Spearman rank correlation; MAE = mean absolute error, percentage points; top10 = how many")
print("    of the source's 10 most confused pairs are in the model's 10.\n")


def cons_pairs(Mx, only=None):
    out = {}
    for a, b in itertools.combinations(CONS, 2):
        if only and (a not in only or b not in only):
            continue
        out[a, b] = (Mx[OI[a], OI[b]] + Mx[OI[b], OI[a]]) / 2
    return out


def v1_matched():
    """v1's onset matrix, 'no onset' folded in, level-matched to E like the sources."""
    C = M2._v1()[0]
    P = {(a, b): C[OI[a], OI[b]] for a in CONS for b in ONSETS}
    Q = M2._level_match(P, E)
    Mx = np.zeros((14, 14))
    for a in CONS:
        for b in CONS:
            Mx[OI[a], OI[b]] = Q[a, b]
        Mx[OI[a], OI[a]] += Q[a, ""]
    return Mx


V1C = v1_matched()
SRC = ["cooke08", "cutler-native", "cutler-dutch", "mandarin6", "mn55"]
extra = {"mandarin12": "proj-mandarin-snr12.tsv"}
M2.PATTERN_FILES.update(extra)
print(f"{'source':16}{'model':22}{'rho':>7}{'MAE':>7}{'top10':>7}")
for s in SRC + list(extra):
    S = M2._source(s, E)
    have = [c for c in CONS if not np.isnan(S[OI[c], OI[c]])]
    ref = cons_pairs(S, have)
    keys = list(ref)
    r = np.array([ref[k] for k in keys])
    top_ref = set(np.argsort(-r)[:10])
    cands = [("v1 (MN55 + guesses)", V1C), ("v2 mix4 in-sample", M2.pattern("mix4", E))]
    if s in M2.MIX4:
        loo = np.mean([M2._source(t, E) for t in M2.MIX4 if t != s], axis=0)
        cands.append(("v2 leave-one-out", loo))
    for name, Mx in cands:
        mp = cons_pairs(Mx, have)
        m = np.array([mp[k] for k in keys])
        top_m = set(np.argsort(-m)[:10])
        print(f"{s:16}{name:22}{spearman(r, m):7.2f}{100 * np.abs(r - m).mean():7.2f}{len(top_ref & top_m):7d}")
    print()

print("Consonant pairs, symmetric confusion in percent at mean onset error 0.20 (v2 = best, no listener groups,")
print("inside a word; v1 level-matched). Top 20 under v2, with v1's value:")
C2 = M2.onset_matrix(M2.no_groups(), "internal")
p2, p1 = cons_pairs(C2), cons_pairs(V1C)
order = sorted(p2, key=lambda k: -p2[k])
for i in range(0, 20, 5):
    print("  " + "   ".join(f"{a}-{b} {pct(p2[a, b])} (v1 {pct(p1[a, b]).strip()})" for a, b in order[i:i + 5]))
print("  v1's top 10: " + ", ".join(f"{a}-{b} {pct(p1[a, b]).strip()}" for a, b in sorted(p1, key=lambda k: -p1[k])[:10]))
print()

print("Onset loss, C -> no onset, percent (sources level-matched to 0.20; v1 has one rate for every context):")
srcs = {"Cutler native (CV, after silence)": "cutler-native", "Cutler Dutch (CV)": "cutler-dutch",
        "Cooke 2008 (VCV, after a vowel)": "cooke08"}
print(f"{'':36}" + "".join(f"{c:>6}" for c in CONS))
C1 = M2._v1()[0]
print(f"{'v1':36}" + "".join(pct(C1[OI[c], 0]).rjust(6) for c in CONS))
for nm, ctx in (("v2 after a pause", "pause"), ("v2 after a vowel (a)", "a"), ("v2 after i (glide/hiatus)", "i")):
    C = M2.onset_matrix(M2.no_groups(), ctx)
    print(f"{nm:36}" + "".join(pct(C[OI[c], 0]).rjust(6) for c in CONS))
for nm, s in srcs.items():
    Q = M2._level_match(M2._read_proj(M2.PATTERN_FILES[s]), E)
    print(f"{nm:36}" + "".join(pct(Q[c, '']).rjust(6) for c in CONS))

print("\nVowels: shares of vowel error by pair (Cutler 2004 0 dB projected onto i<-i, e<-eɪ, a<-ɑ, o<-oʊ, u<-u).")
VMAP = {"i": "i", "eɪ": "e", "ɑ": "a", "oʊ": "o", "u": "u"}
VP_ORDER = [("i", "e"), ("o", "u"), ("a", "o"), ("e", "a"), ("i", "u"), ("e", "o")]


def vshares(Vm):
    tot = Vm.sum() - np.trace(Vm)
    sh = [(Vm[VOWELS.index(a), VOWELS.index(b)] + Vm[VOWELS.index(b), VOWELS.index(a)]) / tot for a, b in VP_ORDER]
    return sh + [1 - sum(sh)], tot / 5


def read_vowels(fname):
    rows = [r for r in csv.reader(open(os.path.join(M2.DATA, fname), encoding="utf-8"), delimiter="\t")
            if r and not r[0].startswith("#")]
    hdr = rows[0][1:]
    Vm = np.zeros((5, 5))
    for r in rows[1:]:
        if r[0] not in VMAP:
            continue
        for h, x in zip(hdr, r[1:]):
            if h in VMAP:
                Vm[VOWELS.index(VMAP[r[0]]), VOWELS.index(VMAP[h])] = float(x)
    return Vm / Vm.sum(1, keepdims=True)


print(f"{'':30}" + "".join(f"{a + '-' + b:>7}" for a, b in VP_ORDER) + f"{'rest':>7}{'mean err':>10}{'L1 to v1':>10}{'L1 to v2':>10}")
s1, e1 = vshares(M2._v1()[1])
s2, e2 = vshares(M2.vowel_matrix(M2.no_groups()))
print(f"{'v1':30}" + "".join(f"{x:7.2f}" for x in s1) + f"{100 * e1:9.1f}%")
print(f"{'v2 best (at E_C 0.20)':30}" + "".join(f"{x:7.2f}" for x in s2) + f"{100 * e2:9.1f}%")
for f in ("cutler2004-native-initial-vowels.tsv", "cutler2004-native-final-vowels.tsv",
          "cutler2004-dutch-initial-vowels.tsv", "cutler2004-dutch-final-vowels.tsv"):
    s, e = vshares(read_vowels(f))
    d1 = sum(abs(a - b) for a, b in zip(s, s1)); d2 = sum(abs(a - b) for a, b in zip(s, s2))
    print(f"{f[11:-11]:30}" + "".join(f"{x:7.2f}" for x in s) + f"{100 * e:9.1f}%{d1:10.2f}{d2:10.2f}")
print("(v1's mean vowel error sits beside a 40% consonant error; v2's beside 20%: the ratio, not the level, is comparable.)")

# ================================================================= (b)
print("\n" + "=" * 100)
print("(b) TODAY'S WORDS: most confusable pairs, symmetric P(a heard as b) averaged both ways, word-initial")
print("    context unknown (junction mix). Short words = 61 grammar words + digits 0-5; content = lexicon.tsv.")
print("    rank under the other model in brackets.\n")


def table_b(label, names, words, n=15):
    x1, iu = sym_pairs(v1, words)
    x2, _ = sym_pairs(best, words)
    r1, r2 = ranks(x1), ranks(x2)
    pairs = list(zip(*iu))
    nm = lambda k: f"{names[pairs[k][0]][1]}~{names[pairs[k][1]][1]} ({names[pairs[k][0]][0]}/{names[pairs[k][1]][0]})"
    print(f"{label}: {len(pairs)} pairs. Spearman(v1, v2) over all pairs = {spearman(x1, x2):.2f}")
    print(f"  {'top under v1':52}{'v1 %':>6}{'[v2 rank]':>10}   {'top under v2':52}{'v2 %':>6}{'[v1 rank]':>10}")
    o1, o2 = np.argsort(-x1)[:n], np.argsort(-x2)[:n]
    for a, b in zip(o1, o2):
        print(f"  {nm(a)[:52]:52}{pct(x1[a]):>6}{r2[a]:>10}   {nm(b)[:52]:52}{pct(x2[b]):>6}{r1[b]:>10}")
    top = 30
    up = [k for k in np.argsort(-x2)[:top] if r1[k] > 3 * top]
    down = [k for k in np.argsort(-x1)[:top] if r2[k] > 3 * top]
    print(f"\n  More dangerous under v2 (v2 top {top}, v1 rank > {3 * top}):")
    for k in sorted(up, key=lambda k: r2[k]):
        print(f"    {nm(k)[:60]:60} v2 rank {r2[k]:4d} ({pct(x2[k]).strip()}%)  v1 rank {r1[k]:6d}")
    print(f"  Overrated by v1 (v1 top {top}, v2 rank > {3 * top}):")
    for k in sorted(down, key=lambda k: r1[k]):
        print(f"    {nm(k)[:60]:60} v1 rank {r1[k]:4d} ({pct(x1[k]).strip()}%)  v2 rank {r2[k]:6d}")
    print()
    return x1, x2, pairs


table_b("SHORT WORDS", SHORT, short_w)
table_b("CONTENT WORDS", CONTENT, content_w)

# ================================================================= (c)
print("=" * 100)
print("(c) THE 16 MERGER PAIRS (tests/shortwords-01/README.md), symmetric confusion in percent, word-initial.")
print("    v1; v2 best (population: listener groups at their shares); shared = v2 with no listener group;")
print("    voi-typ = a voicing-group listener at m best, asp_share best; then each group's worst listener")
print("    (pi = 1, m high; voicing also asp_share low); then v2 best in fixed junctions for the glide pairs.\n")
MERGERS = [("tin", "din"), ("de", "te"), ("yo", "wo"), ("yo", "o"), ("bo", "po"), ("pen", "ben"),
           ("yi", "wi"), ("pi", "bi"), ("pi", "fi"), ("ya", "a"), ("wo", "o"), ("yen", "en"),
           ("un", "wun"), ("ke", "ge"), ("fu", "pu"), ("bu", "pu")]
gloss = {f: g for g, f in SHORT}
cols = [("v1", v1), ("v2", best), ("shared", shared), ("voi-typ", M2.Model(M2.worst_listener("voicing", "best")))]
cols += [(g.replace("voicing", "voi") + "!", MODELS[f"worst-{g}"]) for g in M2.GROUPS]
ctxs = ["pause", "i", "u", "a"]
print(f"{'pair':28}" + "".join(f"{c:>9}" for c, _ in cols) + "".join(f"{'@' + c:>8}" for c in ctxs))
for a, b in MERGERS:
    wa, wb = split(a), split(b)
    line = f"{a + '~' + b + ' (' + gloss[a][:7] + '/' + gloss[b][:7] + ')':28}"
    for _, m in cols:
        line += f"{pct((m.p_word(wa, wb) + m.p_word(wb, wa)) / 2):>9}"
    for c in ctxs:
        line += f"{pct((best.p_word(wa, wb, c) + best.p_word(wb, wa, c)) / 2):>8}"
    print(line)
print("(!) = worst listener of that group. @ctx = after a pause / after a word ending in i, u, a.")

# ================================================================= (d)
print("\n" + "=" * 100)
print(f"(d) ROBUSTNESS across {len(V) - 1} v2 variants (best, 32 Latin-hypercube draws, 14 corners) and v1.")
print("    Pair ranks by symmetric confusion within each variant.\n")


def robustness(label, names, words, topk=10):
    X = np.array([sym_pairs(MODELS[n], words)[0] for n in VN])
    _, iu = sym_pairs(best, words)
    pairs = list(zip(*iu))
    R = np.array([ranks(x) for x in X])
    v2i = [i for i, n in enumerate(VN) if n != "v1"]
    bi = VN.index("best")
    rho = np.array([spearman(X[bi], X[i]) for i in range(len(VN))])
    print(f"{label}: {len(pairs)} pairs")
    print(f"  Spearman of each variant's pair ranking with v2 best: v2 variants min {rho[v2i].min():.2f}, "
          f"median {np.median(rho[v2i]):.2f}; v1 {rho[VN.index('v1')]:.2f}")
    low = sorted(((rho[i], VN[i]) for i in v2i if VN[i] != "best"))[:5]
    print("  least like best: " + ", ".join(f"{n} {r:.2f}" for r, n in low))
    top = (R[v2i] <= topk)
    regret = np.where(top.any(0))[0]
    print(f"  pairs in some v2 variant's top {topk}: {len(regret)} (best's top {topk} is {topk})")
    nm = lambda k: f"{names[pairs[k][0]][1]}~{names[pairs[k][1]][1]} ({names[pairs[k][0]][0]}/{names[pairs[k][1]][0]})"
    worst_rank = R[v2i].max(0)
    med_rank = np.median(R[v2i], 0)
    order = np.lexsort((med_rank, worst_rank))
    print(f"  Most robustly dangerous (sorted by worst rank over the v2 variants):")
    print(f"    {'pair':52}{'worst':>7}{'median':>8}{'in top' + str(topk):>9}{'v1 rank':>9}{'best %':>8}{'max %':>7}  where worst")
    for k in order[:15]:
        wv = VN[v2i[int(np.argmax(R[v2i][:, k]))]]
        print(f"    {nm(k)[:52]:52}{worst_rank[k]:7d}{med_rank[k]:8.0f}{int(top[:, k].sum()):9d}{R[VN.index('v1'), k]:9d}"
              f"{pct(X[bi, k]):>8}{pct(X[v2i, k].max()):>7}  {wv}")
    print(f"  Variant-specific dangers (top {topk} in a variant, median rank > {5 * topk}):")
    spec = [k for k in regret if med_rank[k] > 5 * topk]
    for k in sorted(spec, key=lambda k: R[v2i][:, k].min()):
        where = [VN[v2i[i]] for i in np.where(top[:, k])[0]]
        print(f"    {nm(k)[:52]:52} median {med_rank[k]:6.0f}; top {topk} in {', '.join(where[:6])}{' ...' if len(where) > 6 else ''}")
    print()


robustness("SHORT WORDS", SHORT, short_w)
robustness("CONTENT WORDS", CONTENT, content_w, topk=20)

# ================================================================= (e)
print("=" * 100)
print("(e) JUNCTIONS under v2 best: a two-word sequence of today's words heard as another sequence of")
print("    today's words through the word boundary alone (Model.misparses). P = probability of that")
print("    whole misparse; 'ok' = probability the sequence is heard right. Any word + any word")
print("    (grammar, digits, lexicon); plain onset substitutions left out (word scoring sees them).\n")
allw = SHORT + CONTENT
vocab = {}
for (g, f), w in zip(allw, short_w + content_w):
    vocab.setdefault(w, g)
hits = []
for (g1, f1), w1 in zip(allw, short_w + content_w):
    for (g2, f2), w2 in zip(allw, short_w + content_w):
        if M2.SYLLABLES[w1[-1]][2] == "" and M2.SYLLABLES[w2[0]][0] not in ("", "n", "m", "j", "w"):
            continue  # no junction event possible
        for h1, h2, pr, kind in best.misparses(w1, w2, vocab, threshold=0.02):
            ok = best.p_sequence([w1, w2], [w1, w2])
            hits.append((pr, ok, kind, f"{f1} {f2} ({g1} {g2[:12]})", f"{show(h1)} {show(h2)} ({vocab[h1]} {vocab[h2][:12]})"))
hits.sort(reverse=True)
kinds = {k: 0 for k in ("n+vowel", "n+nasal", "glide/hiatus", "onset presence", "coda", "coda+onset")}
for h in hits:
    kinds[h[2]] = kinds.get(h[2], 0) + 1
print(f"  {len(hits)} misparses with boundary probability >= 2%: " + ", ".join(f"{k} {v}" for k, v in kinds.items()))
for k in [k for k in kinds if kinds[k]]:
    print(f"  {k}, top 8:")
    for pr, ok, kind, s, h in [x for x in hits if x[2] == k][:8]:
        print(f"    {s:36} heard as {h:36} P {pct(pr)}%  ok {pct(ok)}%")

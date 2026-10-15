"""Mishearing model v2 (adopted by the author 2026-10-13).

Sources: research/notes/confusion-data.md §5 (structure), §6 (robustness method), §7 (open
uncertainties); every rate and range is read from research/notes/confusion-data/model-v2-params.tsv,
the consonant patterns from the proj-*.tsv matrices next to it. Not used by the optimizers yet: the
author compares v1 and v2 first (tests/confusion-v2/).

Indexing is the same as build.Inventory over 13 consonants: syllables (onset, vowel, coda) with
onsets ["", p t k f s b d g m n l w j], vowels i e a o u, codas "" / "n", onset outermost.

Parts (each with its source; "added here" = a choice made while implementing, not in the notes):
  consonant substitutions  level-matched pattern (mix of four studies or one source), §5.1; voicing
                           multiplier §5.2
  onset presence           by junction: after a pause, a vowel-final word (glide/hiatus by the vowel),
                           an n-final word, or inside a word, §5.3. The "initial" context mixes the
                           junctions with weights CTX_WEIGHTS (added here; from data/*.tsv, see below)
  coda -n                  asymmetric loss/addition, §5.4
  junctions                n + vowel resegmentation and n + nasal, scored on two-word sequences, §5.4
  vowels                   V_ratio x E_C spread over pair shares, §5.5
  listener groups          each raises one contrast to m for a share pi of listeners, §5.6. Overlaid as
                           independent features (a listener may lack several contrasts)
  face-to-face listener    design log 2026-10-15: one robustness variant ("src-av") with the consonant
                           pattern of listeners who see the talker (von Seth, Aller & Davis 2025, audiovisual,
                           16-channel vocoded), level-matched like the other single sources; /s/, which the
                           study lacks, is filled from mix4 (added here). confusion-data.md §8.
  listener without highs   design log 2026-10-15: one robustness variant ("src-lp") with the consonant
                           pattern of speech low-pass filtered at 2500 Hz (Miller & Nicely 1955 Table XI,
                           +12 dB), standing for age-related high-frequency loss and the telephone band;
                           level-matched like the other single sources; l w j, which the study lacks, are
                           filled from mix4 as in mn55+mix. confusion-data.md §9.
  aspiration               design log 2026-10-13: p t k aspirated word-initially in the reference. For
                           the voicing group the word-initial confusion is
                             asp_share * asp_conf + (1 - asp_share) * L2_voicing_m
                           (added here: asp_conf from Yu & Do 2024 Mandarin aspiration confusion, asp_share
                           a guess for how many talkers really aspirate); word-internal p t k are
                           unaspirated, so L2_voicing_m applies there.

Rates marked "at E_C = 0.20" in the TSV scale with E_C/0.20 (consonant pattern, C->none, none->C,
coda, aspiration confusion; vowels via V_ratio x E_C). Junction ambiguities (glide/hiatus,
resegmentation, n + nasal) and listener-group levels m are not noise rates and do not scale.

  python3 confusion2.py          # self-check and a short summary
"""
import csv, functools, math, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "research", "notes", "confusion-data")
VOWELS = "i e a o u".split()
CONS = "p t k f s b d g m n l w j".split()
ONSETS = [""] + CONS
CODAS = ("", "n")
SYLLABLES = [(o, v, c) for o in ONSETS for v in VOWELS for c in CODAS]
NAME = [o.replace("j", "y") + v + c for o, v, c in SYLLABLES]
IDX = {n: i for i, n in enumerate(NAME)}
SYL_INDEX = {s: i for i, s in enumerate(SYLLABLES)}
OI = {o: i for i, o in enumerate(ONSETS)}
VI = {v: i for i, v in enumerate(VOWELS)}

# ---------------------------------------------------------------- parameters
def _read_params():
    rows = [r for r in csv.reader(open(os.path.join(DATA, "model-v2-params.tsv"), encoding="utf-8"), delimiter="\t")
            if r and not r[0].startswith("#")]
    hdr = rows[0]
    out = {}
    for r in rows[1:]:
        d = dict(zip(hdr, r))
        for k in ("best", "low", "high"):
            try:
                d[k] = float(d[k])
            except ValueError:
                pass
        out[d["id"]] = d
    return out


PARAMS = _read_params()  # id -> {parameter, best, low, high, sampling, status, source}

# Added here (not in the TSV). Each with its source.
ADDED = {
    # Share of word-initial syllables that follow a pause, in the "initial" mix (author, 2026-10-13:
    # sample it instead of fixing 0.20). The n-final share stays 0.20; the rest is split over the vowels.
    "ctx_pause_share": {"best": 0.20, "low": 0.10, "high": 0.40, "sampling": "uniform", "status": "guess",
                        "source": "added; author 2026-10-13"},
    # Yu & Do 2024 Mandarin, aspiration pairs level-matched to E_C = 0.20 (§1.8: 0.34% at +6 dB,
    # 0.36% at +12 dB, 0.93% in quiet): how often an aspiration-language listener confuses an
    # aspirated [pʰ] with an unaspirated/voiced one.
    "asp_conf": {"best": 0.0035, "low": 0.002, "high": 0.01, "sampling": "log-uniform", "status": "data",
                 "source": "Yu & Do 2024 via confusion-data.md §1.8, §4"},
    # Share of word-initial p t k tokens that are really aspirated (reference: aspirated; "unaspirated
    # p t k are a harmless variant"). Talkers whose L1 has unaspirated p t k (Spanish, French,
    # Russian) won't always aspirate. No data.
    "asp_share": {"best": 0.8, "low": 0.5, "high": 0.95, "sampling": "uniform", "status": "guess",
                  "source": "design log 2026-10-13 (aspiration decision); rate guessed"},
}
# Junction mix for a word-initial syllable whose left neighbour is unknown ("initial" context).
# n-final share from data/grammar.tsv + data/lexicon.tsv, frequency-weighted (0.25 of word ends,
# each vowel 0.13-0.20, computed 2026-10-13, rounded to equal vowels); pause share is a guess.
CTX_WEIGHTS = {"pause": 0.20, "n": 0.20, "i": 0.12, "e": 0.12, "a": 0.12, "o": 0.12, "u": 0.12}


def ctx_weights(p):
    """The 'initial' mix for a parameter set: pause share sampled (ctx_pause_share), n-final 0.20, rest
    split evenly over the five vowels."""
    ps = p.get("ctx_pause_share", CTX_WEIGHTS["pause"])
    v = (1 - ps - CTX_WEIGHTS["n"]) / 5
    return {"pause": ps, "n": CTX_WEIGHTS["n"], **{x: v for x in "ieaou"}}

PATTERN_FILES = {
    "cooke08": "proj-cooke08-noise.tsv",
    "cutler-native": "proj-cutler04-native-CV0dB.tsv",
    "cutler-dutch": "proj-cutler04-dutch-CV0dB.tsv",
    "mandarin6": "proj-mandarin-snr6.tsv",
    "mn55": "proj-mn55-6dB.tsv",
    # Face-to-face listener (design log 2026-10-15; confusion-data.md §8). Used only by the "src-av"
    # variant, not in C_pattern's categories. Lacks /s/: filled from mix4 in pattern().
    "av": "proj-av-vonseth25-AV-high.tsv",
    # Listener without high frequencies (design log 2026-10-15; confusion-data.md §9). Used only by
    # the "src-lp" variant. Lacks l w j: filled from mix4 in pattern().
    "lp": "proj-lp-mn55-lp2500.tsv",
}
MIX4 = ("cooke08", "cutler-native", "cutler-dutch", "mandarin6")
PATTERNS = ("mix4",) + MIX4 + ("mn55+mix",)  # C_pattern's categories (TSV)

# Listener groups (§5.6): pi key, m key, and what they raise.
GROUPS = {
    "voicing": ("L2_voicing_pi", "L2_voicing_m", [("p", "b"), ("t", "d"), ("k", "g")]),
    "no-f": ("L2_fp_pi", "L2_fp_m", [("f", "p")]),
    "no-p": ("L2_nop_pi", "L2_nop_m", [("p", "b")]),
    "no-w": ("L2_now_pi", "L2_now_m", [("w", "b")]),
    "no-l": ("L2_nol_pi", "L2_nol_m", [("l", "n"), ("l", "d")]),
    "no-mid": ("L2_mid_pi", "L2_mid_m", [("e", "i"), ("o", "u")]),   # vowels
    "cv-only": ("L2_cv_pi", "L2_cv_coda_loss", []),                  # coda -n loss
}
VOICING = [("p", "b"), ("t", "d"), ("k", "g")]
V_SHARES = ["V_share_i_e", "V_share_o_u", "V_share_a_o", "V_share_e_a", "V_share_i_u", "V_share_e_o", "V_share_rest"]
V_PAIRS = {"V_share_i_e": [("i", "e")], "V_share_o_u": [("o", "u")], "V_share_a_o": [("a", "o")],
           "V_share_e_a": [("e", "a")], "V_share_i_u": [("i", "u")], "V_share_e_o": [("e", "o")],
           "V_share_rest": [("i", "a"), ("i", "o"), ("e", "u"), ("a", "u")]}


def best_params():
    """The best-estimate parameter set (TSV 'best' column plus ADDED)."""
    p = {k: d["best"] for k, d in PARAMS.items() if not d["sampling"].startswith("via")}
    p.update({k: d["best"] for k, d in ADDED.items()})
    p["model"] = "v2"
    return p


def v1_params():
    return {"model": "v1"}


# ---------------------------------------------------------------- consonant patterns
def _read_proj(fname):
    rows = [r for r in csv.reader(open(os.path.join(DATA, fname), encoding="utf-8"), delimiter="\t")
            if r and not r[0].startswith("#")]
    hdr = [("" if h == "(none)" else h) for h in rows[0][1:]]
    return {(r[0], h): float(v) for r in rows[1:] for h, v in zip(hdr, r[1:])}


def _level_match(P, E):
    """research/notes/confusion-data/project.py level_match: one factor on every row's error mass."""
    stims = [a for a in CONS if (a, a) in P]
    err = {a: 1 - P[a, a] for a in stims}
    s = E / (sum(err.values()) / len(stims))
    Q = {}
    for a in stims:
        e = min(0.95, err[a] * s)
        for b in ONSETS:
            Q[a, b] = (1 - e) if b == a else (P[a, b] / err[a] * e if err[a] > 0 else 0.0)
    return Q


@functools.lru_cache(maxsize=None)
def _source(name, E):
    """Substitution matrix (14 x 14 over ONSETS) of one source level-matched to E, with the
    'heard no consonant' mass returned to the diagonal (onset presence is modelled by junction)."""
    Q = _level_match(_read_proj(PATTERN_FILES[name]), E)
    M = np.full((len(ONSETS), len(ONSETS)), np.nan)
    M[0] = 0.0; M[0, 0] = 1.0
    for a in CONS:
        if (a, a) not in Q:
            continue
        for b in CONS:
            M[OI[a], OI[b]] = Q[a, b]
        M[OI[a], OI[a]] += Q[a, ""]
    return M


@functools.lru_cache(maxsize=None)
def pattern(name, E):
    """Consonant substitution pattern at mean onset error E (incl. the share later given to C->none)."""
    if name == "mix4":
        return np.mean([_source(s, E) for s in MIX4], axis=0)
    if name == "mn55+mix":  # MN55 for the 10 consonants it tested, mix4 for l w j and responses to them
        mix, mn = pattern("mix4", E), _source("mn55", E)
        M = mix.copy()
        lwj = [OI[c] for c in "lwj"]
        for a in CONS:
            i = OI[a]
            if np.isnan(mn[i, i]):
                continue
            to_lwj = mix[i, lwj].sum()
            M[i] = np.nan_to_num(mn[i]) * (1 - to_lwj)
            M[i, lwj] = mix[i, lwj]
        return M
    if name in ("av", "lp"):
        return _fill_from_mix(_source(name, E), pattern("mix4", E))
    return _source(name, E)


def _fill_from_mix(src, mix):
    """Rows of consonants the source didn't test come from mix; in tested rows, responses to an
    untested consonant come from mix and the rest of the row is scaled to make room (the mn55+mix
    rule, for any missing set). Added here 2026-10-15 for the audiovisual source (no /s/); also used
    for the low-pass source (no l w j), where it gives the same result as mn55+mix."""
    M = src.copy()
    miss = [OI[c] for c in CONS if np.isnan(src[OI[c], OI[c]])]
    for c in CONS:
        i = OI[c]
        if i in miss:
            M[i] = mix[i]
            continue
        to_miss = mix[i, miss].sum()
        M[i] = np.nan_to_num(src[i]) * (1 - to_miss)
        M[i, miss] = mix[i, miss]
    return M


# ---------------------------------------------------------------- component matrices
def _k(p):
    return p["E_C"] / 0.20


def _raise(M, a, b, level, share):
    """Listener-group overlay: a share of listeners confuse a<->b at `level` each way."""
    for x, y in ((a, b), (b, a)):
        M[x, y] += share * max(0.0, level - M[x, y])


def onset_matrix(p, context="initial"):
    """P[sent onset, heard onset] over ONSETS for a syllable in `context`:
    'pause' (word-initial after a pause), a vowel 'i e a o u' (word-initial after a word ending in
    that vowel), 'n' (after an n-final word), 'internal' (non-initial syllable of a word), or
    'initial' (word-initial, left neighbour unknown: CTX_WEIGHTS mix)."""
    if p.get("model") == "v1":
        return _v1()[0]
    if context == "initial":
        return sum(w * onset_matrix(p, c) for c, w in ctx_weights(p).items())
    k = _k(p)
    M = pattern(p["C_pattern"], p["E_C"]).copy()
    for a, b in VOICING:
        M[OI[a], OI[b]] *= p["voice_mult"]; M[OI[b], OI[a]] *= p["voice_mult"]
    np.fill_diagonal(M, 0.0)
    initial = context != "internal"
    for g, (pi, m, pairs) in GROUPS.items():
        if g in ("no-mid", "cv-only") or p[pi] <= 0:
            continue
        level = p[m]
        if g == "voicing" and initial:  # aspirated p t k word-initially in the reference
            level = p["asp_share"] * p["asp_conf"] * k + (1 - p["asp_share"]) * p[m]
        for a, b in pairs:
            _raise(M, OI[a], OI[b], level, p[pi])
    # onset presence
    none = {c: 0.0 for c in CONS}
    if context == "pause":
        for c in CONS:
            key = ("C_none_pause_p" if c == "p" else "C_none_pause_tk" if c in "tk" else
                   "C_none_pause_bfg" if c in "bfg" else "C_none_pause_other")
            none[c] = p[key] * k
    else:
        for c in CONS:
            none[c] = p["C_none_after_vowel"] * k
        if context in VOWELS:
            none["j"] = p["glide_hiatus_front"] if context in "ie" else p["glide_hiatus_other"]
            none["w"] = p["glide_hiatus_back"] if context in "uo" else p["glide_hiatus_other"]
        elif context == "n":
            none["j"] = none["w"] = p["glide_hiatus_other"]
    added = {c: p["none_C_pause"] * k / len(CONS) for c in CONS}  # none -> some C (spread evenly)
    if context in VOWELS or context == "n":
        added["j"], added["w"] = none["j"], none["w"]  # hiatus <-> glide, each direction
    for c in CONS:
        M[OI[c], 0] = none[c]
        M[0, OI[c]] = added[c]
    for i in range(len(ONSETS)):
        off = M[i].sum()
        if off > 0.97:
            M[i] *= 0.97 / off; off = 0.97
        M[i, i] = 1 - off
    return M


def vowel_matrix(p):
    if p.get("model") == "v1":
        return _v1()[1]
    E_V = p["V_ratio"] * p["E_C"]
    total = len(VOWELS) * E_V  # error mass summed over the five rows
    sh = np.array([p[s] for s in V_SHARES]); sh = sh / sh.sum()
    M = np.zeros((5, 5))
    for s, w in zip(V_SHARES, sh):
        prs = V_PAIRS[s]
        for a, b in prs:
            M[VI[a], VI[b]] = M[VI[b], VI[a]] = w * total / 2 / len(prs)
    pi, m, pairs = GROUPS["no-mid"]
    for a, b in pairs:
        _raise(M, VI[a], VI[b], p[m], p[pi])
    np.fill_diagonal(M, 0.0)
    np.fill_diagonal(M, 1 - M.sum(1))
    return M


def coda_matrix(p):
    """P[sent coda, heard coda] over ("", "n") inside a syllable (no junction event)."""
    if p.get("model") == "v1":
        return _v1()[2]
    k = _k(p)
    loss, add = min(0.9, p["coda_loss"] * k), min(0.9, p["coda_add"] * k)
    pi, m, _ = GROUPS["cv-only"]
    loss += p[pi] * max(0.0, p[m] - loss)
    return np.array([[1 - add, add], [loss, 1 - loss]])


def syllable_matrix(p, context="initial"):
    """S[i, j] = P(syllable i heard as syllable j), SYLLABLES order (= build.Inventory over 13 consonants)."""
    return np.kron(np.kron(onset_matrix(p, context), vowel_matrix(p)), coda_matrix(p))


@functools.lru_cache(maxsize=1)
def _v1():
    """v1 (tools/confusion.py) as build.Inventory uses it: onsets renormalized over this inventory."""
    import confusion as v1
    C = np.array([[v1.CP[a, b] for b in ONSETS] for a in ONSETS])
    C /= C.sum(1, keepdims=True)
    V = np.array([[v1.VP[a, b] for b in VOWELS] for a in VOWELS])
    K = np.array([[1 - v1.CODA_MISS, v1.CODA_MISS], [v1.CODA_MISS, 1 - v1.CODA_MISS]])
    return C, V, K


# ---------------------------------------------------------------- words
class Model:
    """One parameter set, with its syllable matrices cached. Words are tuples of syllable indices."""

    def __init__(self, p):
        self.p = p
        self.S_initial = syllable_matrix(p, "initial")
        self.S_internal = syllable_matrix(p, "internal")
        self.C = {c: onset_matrix(p, c) for c in ["pause", "n", "internal", "initial"] + VOWELS}
        self.V, self.K = vowel_matrix(p), coda_matrix(p)

    def S(self, context):
        return syllable_matrix(self.p, context)

    def p_word(self, a, b, left="initial"):
        """P(word a heard as word b); same length only. `left`: context of the first syllable."""
        if len(a) != len(b):
            return 0.0
        S0 = self.S_initial if left == "initial" else self.S(left)
        return S0[a[0], b[0]] * math.prod(self.S_internal[x, y] for x, y in zip(a[1:], b[1:]))

    def word_matrix(self, words, left="initial"):
        """P[i, j] = P(words[i] heard as words[j]) for same-length words, else 0; diagonal kept."""
        n = len(words)
        P = np.zeros((n, n))
        S0 = self.S_initial if left == "initial" else self.S(left)
        lens = np.array([len(w) for w in words])
        for L in set(lens):
            ix = np.where(lens == L)[0]
            A = np.array([words[i] for i in ix])
            Q = S0[np.ix_(A[:, 0], A[:, 0])]
            for k in range(1, L):
                Q = Q * self.S_internal[np.ix_(A[:, k], A[:, k])]
            P[np.ix_(ix, ix)] = Q
        return P

    # ------------------------------------------------------------ junctions (§5.3-5.4)
    def boundary(self, v1, c1, o2):
        """Joint distribution of (heard coda of word 1, heard onset of word 2) at a word boundary,
        given word 1 ends in vowel v1 + coda c1 and word 2 starts with onset o2.
        Returns {(coda, onset): prob}. Includes the n + vowel resegmentation ("Vn V" <-> "V nV")
        and the n + nasal case ("Vn nV"/"Vn mV" <-> "V nV"/"V mV")."""
        p = self.p
        ctx = "n" if c1 == "n" else v1
        C, K = self.C[ctx], self.K
        ci = CODAS.index(c1)
        out = {}
        for ch in CODAS:
            for oh in ONSETS:
                q = K[ci, CODAS.index(ch)] * C[OI[o2], OI[oh]]
                if q > 0:
                    out[ch, oh] = q
        if p.get("model") == "v1":
            return out
        events = []
        if c1 == "n" and o2 == "":
            events.append((p["reseg_n_V"], ("", "n")))
        if c1 == "" and o2 == "n":
            events.append((p["reseg_n_V"], ("n", "")))
        if c1 == "n" and o2 in ("n", "m"):
            events.append((p["gem_n_N"], ("", o2)))
        if c1 == "" and o2 in ("n", "m"):
            events.append((p["gem_n_N"], ("n", o2)))
        r = sum(e for e, _ in events)
        if r > 0.95:
            events = [(e * 0.95 / r, o) for e, o in events]; r = 0.95
        out = {key: q * (1 - r) for key, q in out.items()}
        for e, key in events:
            out[key] = out.get(key, 0.0) + e
        return out

    def p_sequence(self, sent, heard, left="initial"):
        """P(a word sequence `sent` is heard as `heard`); both lists of words (tuples of syllable
        indices) with the same word lengths. Every boundary is scored jointly (boundary());
        everything else syllable by syllable."""
        if [len(w) for w in sent] != [len(w) for w in heard]:
            return 0.0
        prob = 1.0
        for w, (a, b) in enumerate(zip(sent, heard)):
            for k, (x, y) in enumerate(zip(a, b)):
                (o1, v1, c1), (o2, v2, c2) = SYLLABLES[x], SYLLABLES[y]
                prob *= self.V[VI[v1], VI[v2]]
                last = k == len(a) - 1 and w < len(sent) - 1
                if not last:
                    prob *= self.K[CODAS.index(c1), CODAS.index(c2)]
                if k > 0:
                    prob *= self.C["internal"][OI[o1], OI[o2]]
                elif w == 0:
                    prob *= self.C[left][OI[o1], OI[o2]]
                # word-initial onsets of later words are scored in the boundary below
            if w < len(sent) - 1:
                _, va, ca = SYLLABLES[a[-1]]
                _, _, cb = SYLLABLES[b[-1]]
                o_next, oh_next = SYLLABLES[sent[w + 1][0]][0], SYLLABLES[heard[w + 1][0]][0]
                prob *= self.boundary(va, ca, o_next).get((cb, oh_next), 0.0)
        return prob

    def misparses(self, w1, w2, vocab, threshold=0.01, junction_only=True):
        """Two-word sequences from `vocab` (a set of word tuples) that the sequence (w1, w2) is heard
        as through a boundary event alone (coda of w1 and/or onset of w2 change, nothing else).
        junction_only drops plain onset substitutions (C -> other C, coda unchanged), which word-level
        scoring already sees. Returns [(h1, h2, prob, kind)] with prob = p_sequence((w1, w2) -> (h1, h2))
        for boundary outcomes whose own probability is >= threshold."""
        o1, v1, c1 = SYLLABLES[w1[-1]]
        o2, v2, c2 = SYLLABLES[w2[0]]
        out = []
        for (ch, oh), q in self.boundary(v1, c1, o2).items():
            if (ch, oh) == (c1, o2) or q < threshold:
                continue
            kind = junction_kind(c1, o2, ch, oh)
            if junction_only and kind == "substitution":
                continue
            h1 = w1[:-1] + (SYL_INDEX[o1, v1, ch],)
            h2 = (SYL_INDEX[oh, v2, c2],) + w2[1:]
            if h1 in vocab and h2 in vocab:
                out.append((h1, h2, self.p_sequence([w1, w2], [h1, h2]), kind))
        return out


def junction_kind(c1, o2, ch, oh):
    """Name the boundary event (sent coda c1 + onset o2 heard as ch + oh)."""
    if (c1, o2, ch, oh) in (("n", "", "", "n"), ("", "n", "n", "")):
        return "n+vowel"
    if o2 in ("n", "m") and oh == o2 and ch != c1:
        return "n+nasal"
    if ch == c1 and {o2, oh} in ({"", "j"}, {"", "w"}):
        return "glide/hiatus"
    if ch == c1 and "" in (o2, oh):
        return "onset presence"
    if ch != c1 and oh == o2:
        return "coda"
    if ch == c1:
        return "substitution"
    return "coda+onset"


# ---------------------------------------------------------------- robustness variants (§6)
def _transform(u, d):
    lo, hi = d["low"], d["high"]
    if d["sampling"].startswith("log-uniform") and lo > 0:
        return math.exp(math.log(lo) + u * (math.log(hi) - math.log(lo)))
    return lo + u * (hi - lo)


def variants(n_lhs=32, seed=2026, av=True, lp=True):
    """The §6 variant set: [(name, params)].
    best; n_lhs Latin-hypercube draws (uniform / log-uniform per the TSV; C_pattern stratified over
    its categories; vowel shares Dirichlet around the best values, concentration 20); fixed corners:
    each consonant source alone, voicing x0.1 and x3, each listener group at pi = 1 with its high m
    (other groups off), and v1.
    av: add "src-av", a face-to-face listener (audiovisual consonant pattern in place of the consonant
    pattern, everything else at best values; design log 2026-10-15). av=False gives the 48 variants
    used before it, unchanged (same draws, same order).
    lp: add "src-lp", a listener without high frequencies (low-pass 2500 Hz consonant pattern in place
    of the consonant pattern, everything else at best values; design log 2026-10-15), after src-av.
    lp=False gives the variants used before it, unchanged."""
    rng = np.random.default_rng(seed)
    best = best_params()
    out = [("best", best)]
    cont = {k: d for k, d in list(PARAMS.items()) + list(ADDED.items())
            if d["sampling"] in ("uniform", "log-uniform") and k != "E_C"}
    draws = [dict(best) for _ in range(n_lhs)]
    for k, d in cont.items():
        u = (rng.permutation(n_lhs) + rng.random(n_lhs)) / n_lhs
        for i in range(n_lhs):
            draws[i][k] = _transform(u[i], d)
    cats = [PATTERNS[i % len(PATTERNS)] for i in range(n_lhs)]
    rng.shuffle(cats)
    alpha = 20 * np.array([best[s] for s in V_SHARES])
    for i in range(n_lhs):
        draws[i]["C_pattern"] = cats[i]
        for s, x in zip(V_SHARES, rng.dirichlet(alpha)):
            draws[i][s] = float(x)
        out.append((f"lhs-{i:02d}", draws[i]))
    for s in PATTERNS[1:]:
        out.append((f"src-{s}", dict(best, C_pattern=s)))
    if av:
        out.append(("src-av", dict(best, C_pattern="av")))
    if lp:
        out.append(("src-lp", dict(best, C_pattern="lp")))
    lo, hi = PARAMS["voice_mult"]["low"], PARAMS["voice_mult"]["high"]
    out.append((f"voicing-x{lo:g}", dict(best, voice_mult=lo)))
    out.append((f"voicing-x{hi:g}", dict(best, voice_mult=hi)))
    for g, (pi, m, _) in GROUPS.items():
        q = dict(best, **{GROUPS[h][0]: 0.0 for h in GROUPS})
        q[pi], q[m] = 1.0, PARAMS[m]["high"]
        if g == "voicing":
            q["asp_share"] = ADDED["asp_share"]["low"]
        out.append((f"worst-{g}", q))
    out.append(("v1", v1_params()))
    return out


def worst_listener(group, level="high"):
    """A single listener of `group` (pi = 1, others off) with m at its 'best' or 'high' value."""
    pi, m, _ = GROUPS[group]
    q = dict(best_params(), **{GROUPS[h][0]: 0.0 for h in GROUPS})
    q[pi] = 1.0
    q[m] = PARAMS[m][level] if level != "best" else PARAMS[m]["best"]
    if group == "voicing" and level == "high":
        q["asp_share"] = ADDED["asp_share"]["low"]
    return q


def no_groups(p=None):
    """A parameter set with every listener group switched off (the shared acoustic pattern only)."""
    return dict(p or best_params(), **{GROUPS[h][0]: 0.0 for h in GROUPS})


# ---------------------------------------------------------------- self-check
def check(p):
    for ctx in ["pause", "n", "internal", "initial"] + VOWELS:
        S = syllable_matrix(p, ctx)
        assert S.shape == (140, 140)
        assert (S >= -1e-12).all(), ctx
        assert np.allclose(S.sum(1), 1.0), (ctx, S.sum(1).min(), S.sum(1).max())
    if p.get("model") != "v1":
        m = Model(p)
        for v in VOWELS:
            for c in CODAS:
                for o in ONSETS:
                    assert abs(sum(m.boundary(v, c, o).values()) - 1) < 1e-9


if __name__ == "__main__":
    V = variants()
    for name, p in V:
        check(p)
    print(f"{len(V)} variants, all syllable matrices stochastic")
    assert [n for n, _ in variants(av=False, lp=False)] == [n for n, _ in V if n not in ("src-av", "src-lp")]
    assert [n for n, _ in variants(lp=False)] == [n for n, _ in V if n != "src-lp"]
    A = onset_matrix(no_groups(dict(best_params(), C_pattern="av")), "internal")
    assert not np.isnan(A).any()
    sa = lambda a, b: (A[OI[a], OI[b]] + A[OI[b], OI[a]]) / 2
    print("src-av, no listener groups, internal: voicing p-b %.3f t-d %.3f k-g %.3f | p-t %.3f m-n %.3f l-n %.3f m-b %.3f n-d %.3f"
          % (sa("p", "b"), sa("t", "d"), sa("k", "g"), sa("p", "t"), sa("m", "n"), sa("l", "n"), sa("m", "b"), sa("n", "d")))
    L = onset_matrix(no_groups(dict(best_params(), C_pattern="lp")), "internal")
    assert not np.isnan(L).any()
    sl = lambda a, b: (L[OI[a], OI[b]] + L[OI[b], OI[a]]) / 2
    print("src-lp, no listener groups, internal: f-s %.3f f-p %.3f f-b %.3f p-t %.3f p-k %.3f t-k %.3f d-g %.3f m-n %.3f s-t %.3f"
          % (sl("f", "s"), sl("f", "p"), sl("f", "b"), sl("p", "t"), sl("p", "k"), sl("t", "k"), sl("d", "g"), sl("m", "n"), sl("s", "t")))
    p = best_params()
    C = onset_matrix(no_groups(p), "internal")
    sym = lambda a, b: (C[OI[a], OI[b]] + C[OI[b], OI[a]]) / 2
    print("best, no listener groups, internal: voicing p-b %.3f t-d %.3f k-g %.3f | p-t %.3f m-n %.3f l-n %.3f f-b %.3f"
          % (sym("p", "b"), sym("t", "d"), sym("k", "g"), sym("p", "t"), sym("m", "n"), sym("l", "n"), sym("f", "b")))
    for g in GROUPS:
        print(f"  worst-{g}: listener pi=1, m high")

"""Report on a placement (README "Results"): scores, near pairs, B2 margin, p-initial count, moves,
haplology and juncture checks, offensive matches; forms.tsv.

  python3 report.py [STATE ...]     # default: the best finished state/C-*.json; also scores state/A.json
"""
import csv, glob, io, json, os, runpy, sys, contextlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import place as P

ITEMS, N, NV, TOPQ = P.ITEMS, P.N, P.NV, P.TOPQ
VN = [n for n, _ in P.VARIANTS]
out = io.StringIO()
PICK = [None]


def say(*a):
    print(*a)
    print(*a, file=out)


def forms_of(name):
    return [tuple(f) for f in P.load_state(name)["forms"]]


def scores(forms, Wm=None, freq=None, med=None):
    Wm = P.WM if Wm is None else Wm
    freq = P.FREQ if freq is None else freq
    T = P.conf_total(forms, Wm=Wm, freq=freq)
    x = T / med
    R = P.cvar(x)
    eff = sum(P.EFFORT * freq[i] * (P.INV.length(f) - 2.0) for i, f in enumerate(forms))
    worst = [VN[k] for k in np.argsort(-x)[:3]]
    return R, med[0] * R + eff, x[0], worst


def sym_pairs(forms):
    """Per pair: best-variant symmetric confusion, and its robust version (mean of the worst quarter of
    variants of P(i->j) + P(j->i)). Upper triangle, same-length pairs only."""
    n = len(forms)
    lens = np.array([len(f) for f in forms])
    iu = np.triu_indices(n, 1)
    same = lens[iu[0]] == lens[iu[1]]
    iu = (iu[0][same], iu[1][same])
    allv = np.zeros((NV, len(iu[0])), np.float32)
    for v in range(NV):
        Pm = P.pair_matrix(forms, v)
        allv[v] = (Pm + Pm.T)[iu]
    rob = -np.partition(-allv, TOPQ - 1, axis=0)[:TOPQ].mean(0)
    return iu, allv[0], rob


# B2: single-feature neighbours (research/notes/unknown-unknowns.md #9: voicing, e/i, o/u, m/n, f/p, l/y/w, +-final n)
ALT_O = {"p": "bf", "b": "p", "t": "d", "d": "t", "k": "g", "g": "k", "m": "n", "n": "m", "f": "p", "l": "wj", "w": "lj", "j": "lw"}
ALT_V = {"e": "i", "i": "e", "o": "u", "u": "o"}


def neighbours(f):
    out = []
    for k, s in enumerate(f):
        o, v, c = P.M2.SYLLABLES[s]
        alts = [(x, v, c) for x in ALT_O.get(o, "")] + [(o, x, c) for x in ALT_V.get(v, "")] + [(o, v, "n" if c == "" else "")]
        for a in alts:
            out.append(f[:k] + (P.M2.SYL_INDEX[a],) + f[k + 1:])
    return out


def b2(forms, which):
    real = set(forms)
    tot = hit = 0
    for i in which:
        for nb in neighbours(forms[i]):
            tot += 1; hit += nb in real
    return hit, tot


def juncture(forms):
    import words as W
    orig = W.read
    rows = [{"gloss": it["gloss"], "field": it["field"], "tier": str(it["tier"]), "form": P.show(f)} for it, f in zip(ITEMS, forms)]
    W.read = lambda name: rows if name == "lexicon.tsv" else orig(name)
    buf = io.StringIO()
    code = 0
    try:
        with contextlib.redirect_stdout(buf):
            runpy.run_path(os.path.join(P.ROOT, "tools", "juncture.py"))
    except SystemExit as e:
        code = e.code
    finally:
        W.read = orig
    return code, buf.getvalue().strip()


def main(names, tag=""):
    medA, medT = P.medians("after"), P.medians("today")
    T = P.TODAY
    say(f"{N} content words ({len(P.MOVABLE)} roots placed, {N - len(P.MOVABLE)} fixed: loans and operators); {NV} variants; "
        f"robust score R = mean of worst {TOPQ} of conf_v / random median (1.0 = random lexicon)")
    say(f"random medians, best variant: today {medT[0]:.2f}, full list {medA[0]:.2f}; v1 variant: today {medT[-1]:.2f}, full list {medA[-1]:.2f}")
    Rt, Jt, bt, wt = scores(T["forms"], T["W"], T["freq"], medT)
    say(f"today's lexicon ({len(T['forms'])} words, data/lexicon.tsv): R {Rt:.4f} | best variant {bt:.4f} | worst variants {', '.join(wt)}")
    res = {}
    for nm in names:
        f = forms_of(nm)
        R, J, b, w = scores(f, med=medA)
        res[nm] = (R, J, f)
        say(f"{nm}: R {R:.4f} | J {J:.3f} | best variant {b:.4f} | worst variants {', '.join(w)}")
    cs = [n for n in names if n.startswith("C")] or names
    pick = min(cs, key=lambda n: res[n][1])
    PICK[0] = (pick, res[pick][2])
    forms = res[pick][2]
    say(f"chosen: {pick} (lowest J)")
    if len(cs) > 1:
        same = sum(1 for i in P.MOVABLE if len({res[n][2][i] for n in cs}) == 1)
        sl = sum(1 for i in P.MOVABLE if len({len(res[n][2][i]) for n in cs}) == 1)
        say(f"seeds agree on {same} of {len(P.MOVABLE)} root forms ({100 * same / len(P.MOVABLE):.0f}%); on length for {sl}")
    an = [n for n in names if n.startswith("A")]
    A = res[an[0]][2] if an else None

    # length
    n3 = [i for i in P.MOVABLE if len(forms[i]) == 3]
    say(f"three-syllable roots: {len(n3)}" + (": " + ", ".join(f"{ITEMS[i]['gloss']} {P.show(forms[i])}" for i in n3) if n3 else ""))
    # moved
    old = [i for i in P.MOVABLE if ITEMS[i]["old"]]
    mv = [i for i in old if P.show(forms[i]) != ITEMS[i]["old"]]
    must = [i for i in old if A is not None and P.show(A[i]) != ITEMS[i]["old"]]
    say(f"today's roots moved: {len(mv)} of {len(old)} (forced by the rules: {len(must)})")
    # near pairs
    tf = T["forms"]
    iu0, b0, r0 = sym_pairs(tf)
    thr_b, thr_r = np.quantile(b0, 0.99), np.quantile(r0, 0.99)
    iu, bb, rr = sym_pairs(forms)
    say(f"near pairs (above today's 99th percentile of pair confusion): best variant thr {thr_b:.2e}: today {int((b0 > thr_b).sum())} "
        f"of {len(b0)} pairs, after {int((bb > thr_b).sum())} of {len(bb)}; robust (worst-quarter mean) thr {thr_r:.2e}: today "
        f"{int((r0 > thr_r).sum())}, after {int((rr > thr_r).sum())}")
    if A is not None:
        _, ba, ra = sym_pairs(A)
        say(f"  A (one at a time): best {int((ba > thr_b).sum())}, robust {int((ra > thr_r).sum())}")
    # nearest-neighbour confusion, frequency-weighted (placement.py's second measure), best variant
    Pm = P.pair_matrix(forms, 0); nn = (Pm + Pm.T).max(1)
    Pt = P.pair_matrix(tf, 0); nnt = (Pt + Pt.T).max(1)
    say(f"frequency-weighted nearest-neighbour confusion (best variant): today {(T['freq'] * nnt).sum() / T['freq'].sum():.5f}, after {(P.FREQ * nn).sum() / P.FREQ.sum():.5f}")
    # B2
    troots = [i for i, it in enumerate(T["items"]) if not it["fixed"]]
    h0, t0 = b2(tf, troots)
    roots = P.MOVABLE
    h1, t1 = b2(forms, roots)
    h2, t2 = b2(forms, range(N))
    say(f"B2 margin (single-feature neighbours that are real words): today's roots {h0}/{t0} = {100 * h0 / t0:.2f}%; "
        f"new roots {h1}/{t1} = {100 * h1 / t1:.2f}%; all content words {h2}/{t2} = {100 * h2 / t2:.2f}%")
    if A is not None:
        ha, ta = b2(A, roots)
        say(f"  A (one at a time): roots {ha}/{ta} = {100 * ha / ta:.2f}%")
    # p-initial
    p0 = sum(1 for i in troots if P.INV.syl[tf[i][0]][0] == "p")
    p1 = sum(1 for i in roots if P.INV.syl[forms[i][0]][0] == "p")
    pall = sum(1 for i in range(N) if P.INV.syl[forms[i][0]][0] == "p")
    say(f"p-initial roots: today {p0} of {len(troots)}; after {p1} of {len(roots)} (all content words incl. loans: {pall})")
    on = {}
    for i in roots:
        o = P.INV.syl[forms[i][0]][0] or "V"
        on[o] = on.get(o, 0) + 1
    say("  first-onset counts, new roots: " + " ".join(f"{k}:{v}" for k, v in sorted(on.items(), key=lambda x: -x[1])))
    # haplology / digit check
    bad = [i for i in roots if forms[i][0] in P.HAPLO or forms[i][0] in P.DIGITS]
    fixedbad = [i for i in range(N) if ITEMS[i]["fixed"] and (forms[i][0] in P.HAPLO or forms[i][0] in P.DIGITS)]
    say(f"haplology + digit check (roots starting with {' '.join(sorted(P.SYL[s] for s in P.HAPLO))} or a digit): "
        f"{'passed' if not bad else 'FAILED ' + str([P.show(forms[i]) for i in bad])}; fixed words that do (kept by rule 2): "
        + ", ".join(f"{P.show(forms[i])} ({ITEMS[i]['gloss']})" for i in fixedbad))
    keys = [P.INV.content_key(f) for f in forms]
    say(f"unique drift keys: {'yes' if len(set(keys)) == N else 'NO'}; reserved senary keys used: {sum(k in P.RESERVED for k in keys)}; "
        f"second syllable onset: {'yes' if all(all(P.HAS_ONSET[s] for s in f[1:]) for f in forms) else 'NO'}; "
        f"blocked forms: {sum(P.offensive.blocked(P.show(f)) for f in forms)}")
    code, txt = juncture(forms)
    say(f"juncture.py on the result: exit {code}: {txt}")
    offr = [i for i in roots if P.offensive.matches(P.show(forms[i]))]
    offt = [i for i in troots if P.offensive.matches(P.show(tf[i]))]
    say(f"offensive.matches (C3 tie-break only): new roots {len(offr)}: " + ", ".join(f"{P.show(forms[i])} ({ITEMS[i]['gloss']})" for i in offr)
        + f"; today's roots {len(offt)}")

    # lists for the author
    idx = {it["gloss"]: i for i, it in enumerate(ITEMS)}
    pos = {(a, b): k for k, (a, b) in enumerate(zip(*iu))}
    say("\nantonym pairs, closest (best-variant / robust symmetric confusion):")
    ap = []
    for a, b in P.ANT_PAIRS:
        k = pos.get((min(a, b), max(a, b)))
        if k is not None:
            ap.append((rr[k], bb[k], a, b))
    for r, b, x, y in sorted(ap, reverse=True)[:15]:
        say(f"  {r:.2e} {b:.2e}  {P.show(forms[x])} {ITEMS[x]['gloss']}  ~  {P.show(forms[y])} {ITEMS[y]['gloss']}")
    say("\nnear pairs among frequent words (both tier >= 3), by robust confusion, top 25:")
    fr = [(rr[k], bb[k], a, b) for k, (a, b) in enumerate(zip(*iu)) if ITEMS[a]["tier"] >= 3 and ITEMS[b]["tier"] >= 3]
    for r, b, x, y in sorted(fr, reverse=True)[:25]:
        say(f"  {r:.2e} {b:.2e}  {P.show(forms[x])} {ITEMS[x]['gloss']} (t{ITEMS[x]['tier']}, {ITEMS[x]['field']})  ~  "
            f"{P.show(forms[y])} {ITEMS[y]['gloss']} (t{ITEMS[y]['tier']}, {ITEMS[y]['field']})  W {P.WM[x, y]:.0f}")
    say("\nall near pairs (robust, above today's 99th percentile), top 40:")
    top = np.argsort(-rr)[:40]
    for k in top:
        a, b = iu[0][k], iu[1][k]
        say(f"  {rr[k]:.2e} {bb[k]:.2e}  {P.show(forms[a])} {ITEMS[a]['gloss']} (t{ITEMS[a]['tier']})  ~  {P.show(forms[b])} {ITEMS[b]['gloss']} (t{ITEMS[b]['tier']})")
    say("\nfrequent roots (tier >= 4) whose form changed:")
    for i in sorted(old, key=lambda i: (-ITEMS[i]["tier"], ITEMS[i]["gloss"])):
        if ITEMS[i]["tier"] >= 4 and P.show(forms[i]) != ITEMS[i]["old"]:
            say(f"  t{ITEMS[i]['tier']} {ITEMS[i]['gloss']}: {ITEMS[i]['old']} -> {P.show(forms[i])}")
    say("\nnew roots, tier >= 4:")
    for i in P.MOVABLE:
        if ITEMS[i]["tier"] >= 4 and not ITEMS[i]["old"]:
            say(f"  t{ITEMS[i]['tier']} {ITEMS[i]['gloss']}: {P.show(forms[i])}")

    with open(os.path.join(HERE, f"forms{tag}.tsv.tmp"), "w") as fh:
        fh.write("concept\told form\tnew form\tfield\ttier\troute\n")
        byg = {it["gloss"]: (it, f) for it, f in zip(ITEMS, forms)}
        for r in P.CROWS:
            it, f = byg.get(r["concept"], (None, None))
            fh.write(f"{r['concept']}\t{r['form']}\t{P.show(f) if f else ''}\t{r['field']}\t{r['tier']}\t{r['route']}\n")
        for it, f in zip(ITEMS, forms):
            if it["route"] == "operator":
                fh.write(f"{it['gloss']}\t{it['old']}\t{P.show(f)}\t{it['field']}\t{it['tier']}\toperator (fixed)\n")
    os.replace(os.path.join(HERE, f"forms{tag}.tsv.tmp"), os.path.join(HERE, f"forms{tag}.tsv"))
    with open(os.path.join(HERE, f"report{tag}.txt"), "w") as fh:
        fh.write(out.getvalue())


if __name__ == "__main__":
    # main run (rules as given): A and C-*; sensitivity (two syllables only): A-no3 and C-no3-*
    if "--no3" in sys.argv:
        names = ["A-no3.json"] + sorted(os.path.basename(p) for p in glob.glob(os.path.join(P.STATE, "C-no3-*.json")))
        main(names, "-no3")
    else:
        names = [a for a in sys.argv[1:]] or (["A.json"] + sorted(os.path.basename(p) for p in glob.glob(os.path.join(P.STATE, "C-[0-9]*.json"))))
        main(names)

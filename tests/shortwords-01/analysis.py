"""Short-word layer, desk analysis (author asked 2026-10-13; cold review C §2 "word forms", auxlang survey voicing finding).

For every pair of grammar words (and digits) that can fill the same slot, report what separates them and
whether that difference survives the mergers real speakers make:
  voicing   p=b, t=d, k=g    (about a third of languages have no voicing contrast; WALS 4A)
  f=p       many languages lack /f/ and substitute p (WALS 19A; A4 F-notes)
  glide     w/y vs no onset  (wun ~ un: the judge's strict-group bug)
  coda      final -n lost     (drift.md: vowel + n -> nasal vowel; grammar words keep -n only in the reference)
Also: two-syllable operators whose first syllable is a same-slot grammar word (manni ~ man, konsin ~ kon).

  python3 analysis.py
"""
import csv, os, sys, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "../../tools"))
import words as W
from build import GROUPS_STRICT

INV, S, IDX = W.INV, W.S, W.IDX
gram = {r["gloss"]: r for r in W.read("grammar.tsv")}
digits = [r for r in W.read("numbers.tsv") if r["kind"] == "digit" and r["form"] in IDX]  # one-syllable digits 0-5; 6-9 are two syllables
VOI = {"b": "p", "d": "t", "g": "k"}


def parts(form):
    o, v, c = INV.syl[IDX[form]]
    return o, v, c


def keys(form, merge):
    o, v, c = parts(form)
    if "voicing" in merge: o = VOI.get(o, o)
    if "f=p" in merge and o == "f": o = "p"
    if "glide" in merge and o in ("w", "j"): o = ""
    if "coda" in merge: c = ""
    return (o, v, c)


def diff(a, b):
    (o1, v1, c1), (o2, v2, c2) = parts(a), parts(b)
    out = []
    if o1 != o2:
        if VOI.get(o1, o1) == VOI.get(o2, o2): out.append("voicing")
        elif {o1, o2} <= {"f", "p", "b"}: out.append("f/p")
        elif "" in (o1, o2) and {o1, o2} - {""} <= {"w", "j"}: out.append("glide vs none")
        else: out.append(f"onset {o1 or '∅'}/{o2 or '∅'}")
    if v1 != v2: out.append(f"vowel {v1}/{v2}")
    if c1 != c2: out.append("coda -n")
    return ", ".join(out)


rows = []
groups = {k: v.split() for k, v in GROUPS_STRICT.items()}
groups["number slot (det + digits)"] = GROUPS_STRICT["det"].split() + [f"digit {d['value']}" for d in digits]
form = {g: r["form"] for g, r in gram.items()}
form.update({f"digit {d['value']}": d["form"] for d in digits})
freq = {g: float(r["freq"]) for g, r in gram.items()}
freq.update({f"digit {d['value']}": 4.0 for d in digits})
for grp, members in groups.items():
    for a, b in itertools.combinations(members, 2):
        fa, fb = form[a], form[b]
        p = max(S[IDX[fa], IDX[fb]], S[IDX[fb], IDX[fa]])
        merged = [m for m in ("voicing", "f=p", "glide", "coda") if keys(fa, [m]) == keys(fb, [m])]
        rows.append((grp, a, fa, b, fb, p, diff(fa, fb), merged))

risky = [r for r in rows if r[7]]
print(f"{len(rows)} same-slot pairs; {len(risky)} collapse under at least one common merger:\n")
for grp, a, fa, b, fb, p, d, m in sorted(risky, key=lambda r: -r[5]):
    print(f"  {grp:28} {fa:>5} {a:12} ~ {fb:<5} {b:12} differ by {d:22} collapses under {', '.join(m):14} S={p:.3f}")
print("\nClosest remaining pairs by the model (no merger involved), top 10:")
for grp, a, fa, b, fb, p, d, m in sorted([r for r in rows if not r[7]], key=lambda r: -r[5])[:10]:
    print(f"  {grp:28} {fa:>5} {a:12} ~ {fb:<5} {b:12} differ by {d:22} S={p:.3f}")

print("\nTwo-syllable operators whose first syllable is a grammar word in the same position:")
ops = "genso wanme inwun wemen konsin buntu tason nedin mesun manni buni donon lanno anko nuwen kiyo mena".split()
gforms = {r["form"]: g for g, r in gram.items()}
for o in ops:
    first = W.SYL[W.split(o)[0]]
    if first in gforms:
        print(f"  {o:7} starts with {first} ({gforms[first]})")


# ---- every pair, regardless of the build tool's slot groups ----
print("\nAll pairs of short words (grammar words + digits 0-5) that collapse under a merger, any slots:")
allw = list(form.items())
for (a, fa), (b, fb) in itertools.combinations(allw, 2):
    merged = [m for m in ("voicing", "f=p", "glide") if keys(fa, [m]) == keys(fb, [m])]
    if merged and fa != fb:
        print(f"  {fa:>5} {a:12} ~ {fb:<5} {b:12} {', '.join(merged)}")

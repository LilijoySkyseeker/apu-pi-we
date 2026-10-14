"""Project published consonant confusion matrices onto Apupiwe's 13 consonants
plus "" (no onset), and compare their error patterns at a matched noise level.

Rules (choices, not data): stimulus rows outside the 13 are dropped; responses
outside the 13 are dropped and the row renormalized (an Apupiwe listener has no
such category; this spreads them proportionally). /h/ responses count as "" (heard
no consonant) when MAP_H is True. Mandarin: aspirated /pʰ tʰ kʰ/ stand for p t k,
plain /p t k/ for b d g (aspiration as the voicing cue).
Run: python3 project.py  (prints a comparison; writes proj-*.tsv)
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OURS = "p t k b d g f s m n l w j".split()
MAP_H = True

def read_tsv(name, rename=None, skipcols=()):
    rows = [r for r in csv.reader(open(os.path.join(HERE, name), encoding="utf-8"), delimiter="\t") if r and not r[0].startswith("#")]
    hdr = rows[0][1:]
    M = {}
    for r in rows[1:]:
        for h, v in zip(hdr, r[1:]):
            if h in skipcols: continue
            try: M[r[0], h] = float(v)
            except ValueError: pass
    if rename:
        M = {(rename.get(a, "?" + a), rename.get(b, "?" + b)): v for (a, b), v in M.items()}
    return M

def project(M):
    stims = {a for a, _ in M}
    P = {}
    for a in OURS:
        if a not in stims: continue
        row = {}
        for b in OURS + [""]:
            row[b] = M.get((a, b), 0.0)
        tot = sum(row.values())
        for b, v in row.items(): P[a, b] = v / tot
    return P

def sources():
    S = {}
    ident = {c: c for c in OURS}
    # Cooke & Scharenborg 2008, noise average; y = /j/
    r = dict(ident, y="j", h="" if MAP_H else "?h"); r.pop("j")
    S["cooke08-noise"] = project(read_tsv("cooke2008-native-noise.tsv", r))
    S["cooke08-clean"] = project(read_tsv("cooke2008-native-clean.tsv", r))
    r = dict(ident, h="" if MAP_H else "?h")
    S["cutler04-native-CV0dB"] = project(read_tsv("cutler2004-native-initial-consonants.tsv", r, ("rowsum",)))
    S["cutler04-dutch-CV0dB"] = project(read_tsv("cutler2004-dutch-initial-consonants.tsv", r, ("rowsum",)))
    mand = {"p": "p", "t": "t", "k": "k", "b": "b", "d": "d", "g": "g", "f": "f", "s": "s", "m": "m", "n": "n", "l": "l", "w": "w", "y": "j"}
    # pinyin p = /pʰ/ -> our p; pinyin b = /p/ -> our b (labels already coincide)
    for c in ("snr12", "snr6", "quiet"):
        S[f"mandarin-{c}"] = project(read_tsv(f"yu-do2024-mandarin-{c}.tsv", mand, ("sum",)))
    # Miller & Nicely 1955 -6 dB, as transcribed in tools/confusion.py
    sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
    import confusion as cf
    M = {(a, b): cf.MN_ROWS[a][cf.MN_ORDER.index(b)] for a in cf.MN_ROWS for b in cf.MN_ORDER}
    S["mn55-6dB"] = project(M)
    return S

def level_match(P, E):
    """Scale every row's error mass by one factor so the mean error is E."""
    stims = sorted({a for a, _ in P})
    err = {a: 1 - P[a, a] for a in stims}
    s = E / (sum(err.values()) / len(stims))
    Q = {}
    for a in stims:
        e = min(0.95, err[a] * s)
        for b in OURS + [""]:
            if b == a: Q[a, b] = 1 - e
            else: Q[a, b] = P[a, b] / err[a] * e if err[a] > 0 else 0.0
    return Q, s

GROUPS = {
    "voicing p-b t-d k-g": [("p", "b"), ("t", "d"), ("k", "g")],
    "place vl stops": [("p", "t"), ("p", "k"), ("t", "k")],
    "place vd stops": [("b", "d"), ("b", "g"), ("d", "g")],
    "f-p": [("f", "p")], "f-b": [("f", "b")], "f-s": [("f", "s")],
    "m-n": [("m", "n")], "m-b": [("m", "b")], "n-d": [("n", "d")],
    "l-n": [("l", "n")], "l-d": [("l", "d")], "l-w": [("l", "w")], "l-j": [("l", "j")],
    "w-j": [("w", "j")], "w-b": [("w", "b")], "w-g": [("w", "g")], "j-g": [("j", "g")], "j-d": [("j", "d")],
}

def pair(Q, a, b):
    if (a, a) not in Q or (b, b) not in Q: return None
    return (Q[a, b] + Q[b, a]) / 2

if __name__ == "__main__":
    E = float(sys.argv[1]) if len(sys.argv) > 1 else 0.20
    S = sources()
    names = list(S)
    print(f"mean error matched to E={E}; cells = symmetric pair confusion (P[a,b]+P[b,a])/2, percent")
    print("group".ljust(22) + "".join(n[:14].rjust(15) for n in names))
    LM = {n: level_match(S[n], E) for n in names}
    print("raw mean error".ljust(22) + "".join(f"{100*sum(1-S[n][a,a] for a in OURS if (a,a) in S[n])/sum(1 for a in OURS if (a,a) in S[n]):15.1f}" for n in names))
    for g, prs in GROUPS.items():
        line = g.ljust(22)
        for n in names:
            vals = [pair(LM[n][0], a, b) for a, b in prs]
            vals = [v for v in vals if v is not None]
            line += (f"{100*sum(vals)/len(vals):15.2f}" if vals else "-".rjust(15))
        print(line)
    line = "C -> no onset (mean)".ljust(22)
    for n in names:
        Q = LM[n][0]; st = [a for a in OURS if (a, a) in Q]
        line += f"{100*sum(Q[a, ''] for a in st)/len(st):15.2f}"
    print(line)
    for n in names:
        with open(os.path.join(HERE, f"proj-{n}.tsv"), "w") as f:
            f.write(f"# derived by project.py from the source TSV for {n}: rows/columns restricted to Apupiwe consonants, other responses dropped and rows renormalized; column '' = /h/ responses (heard no consonant). Not level-matched. Probabilities.\n")
            st = [a for a in OURS if (a, a) in S[n]]
            f.write("sent\\heard\t" + "\t".join(OURS) + "\t(none)\n")
            for a in st:
                f.write(a + "\t" + "\t".join(f"{S[n][a, b]:.4f}" for b in OURS + [""]) + "\n")

"""Which Apupiwe contrasts are missing from L1 inventories (PHOIBLE 2.0).
Input: phoible.csv from https://github.com/phoible/dev (data/phoible.csv).
One inventory per Glottocode (lowest InventoryID); marginal phonemes ignored.
Usage: python3 phoible_gaps.py /path/to/phoible.csv [iso639-3:weight ...]
With weights, also prints the weighted share (e.g. by speakers)."""
import csv, sys, collections, unicodedata

def base(seg):
    # strip diacritics/modifiers but keep the base letter(s)
    return "".join(ch for ch in unicodedata.normalize("NFD", seg) if not unicodedata.combining(ch) and ch not in "ʰʷʲˠˤ̪ːˑ̃")

def load_all(path):
    """All inventories, grouped by InventoryID."""
    by = collections.defaultdict(list)
    for r in csv.DictReader(open(path, encoding="utf-8")):
        if r["Marginal"] != "TRUE": by[int(r["InventoryID"])].append(r)
    return by

def load(path):
    inv = collections.defaultdict(list); first = {}; iso = {}; name = {}
    for r in csv.DictReader(open(path, encoding="utf-8")):
        g = r["Glottocode"]; i = int(r["InventoryID"])
        if g not in first or i < first[g]:
            if g in first and i < first[g]: inv[g] = []
            first[g] = i
        if i != first[g] or r["Marginal"] == "TRUE": continue
        inv[g].append(r); iso[g] = r["ISO6393"]; name[g] = r["LanguageName"]
    return inv, iso, name

def gaps(rows):
    segs = {r["Phoneme"] for r in rows}
    bases = {base(s) for s in segs}
    cons = [r for r in rows if r["SegmentClass"] == "consonant"]
    vow = [r for r in rows if r["SegmentClass"] == "vowel"]
    def stop(r): return r["consonantal"] == "+" and r["sonorant"] == "-" and r["continuant"] == "-" and r["delayedRelease"] in "-0" and r["click"] != "+"
    vl_stop = any(stop(r) and r["periodicGlottalSource"] == "-" for r in cons)
    vd_stop = any(stop(r) and r["periodicGlottalSource"] == "+" for r in cons)  # implosives count as voiced
    lab_fric = any(r["labial"] == "+" and r["continuant"] == "+" and r["sonorant"] == "-" and r["periodicGlottalSource"] == "-" for r in cons)
    lat_approx = any(r["lateral"] == "+" and r["sonorant"] == "+" for r in cons)
    rhotic_or_lat = lat_approx or any(base(r["Phoneme"]) in ("r", "ɾ", "ɹ", "ɽ", "ʀ", "ʁ", "ɻ", "ɺ") for r in cons)
    mid_front = any(r["high"] == "-" and r["low"] == "-" and r["front"] == "+" for r in vow)
    mid_back = any(r["high"] == "-" and r["low"] == "-" and r["back"] == "+" for r in vow)
    return {
        "no voicing contrast in stops": not (vl_stop and vd_stop),
        "no /p/ (any p)": "p" not in bases,
        "no /b/": "b" not in bases,
        "no /d/": "d" not in bases,
        "no /g/": "g" not in bases and "ɡ" not in bases,
        "no voiceless labial fricative (f/ɸ)": not lab_fric,
        "no /f/ exactly": "f" not in bases,
        "no /s/": "s" not in bases,
        "no lateral approximant": not lat_approx,
        "no liquid at all": not rhotic_or_lat,
        "no /w/": "w" not in bases,
        "no /j/": "j" not in bases,
        "no front mid vowel (e/i risk)": not mid_front,
        "no back mid vowel (o/u risk)": not mid_back,
    }

if __name__ == "__main__":
    inv, iso, name = load(sys.argv[1])
    G = {g: gaps(rows) for g, rows in inv.items() if rows}
    keys = list(next(iter(G.values())))
    print(f"languages (one inventory per Glottocode): {len(G)}")
    for k in keys:
        n = sum(v[k] for v in G.values())
        print(f"  {k:40s} {n:5d}  {100*n/len(G):5.1f}%")
    if len(sys.argv) > 2:
        W = {a.split(":")[0]: float(a.split(":")[1]) for a in sys.argv[2:]}
        # every PHOIBLE inventory of the language; a gap counts by the share of inventories showing it
        allinv = load_all(sys.argv[1])
        byiso = collections.defaultdict(list); nm = {}
        for i, rows in allinv.items():
            c = rows[0]["ISO6393"]
            if c in W: byiso[c].append(gaps(rows)); nm[c] = rows[0]["LanguageName"]
        missing = [k for k in W if k not in byiso]
        tot = sum(W[k] for k in byiso)
        print(f"\nweighted over {len(byiso)} languages (weights total {tot:g}); not found in PHOIBLE: {missing}")
        for k in keys:
            share = {c: sum(g[k] for g in gl) / len(gl) for c, gl in byiso.items()}
            s = sum(W[c] * share[c] for c in byiso)
            who = [f"{nm[c]} {share[c]:.0%}" for c in byiso if share[c] > 0]
            print(f"  {k:40s} {100*s/tot:5.1f}%  {', '.join(who)}")

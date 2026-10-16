"""deeplayer-02 part 2: score the 18 loan candidates (loanwork/panel.txt) under the panel rule of 2026-10-15
(at least 12 of 20 languages across at least 5 of the 7 regions), adapt passing medians with tools/names.py,
and check collisions and tools/offensive.py. Writes loans.tsv here.

  direnv exec /home/agent/work/repos/universal-language python3 tests/deeplayer-02/loans.py

A column counts when marked y or b and attested: its source names Wt, We, subs or Leipzig (a memory-only
column, M, counts only once sourced; author 2026-10-13). 'ceiling' adds the u (no data) and memory-only
columns, to show whether any unknown could change a verdict.
"""
import csv, os, re, sys
REPO = "/home/agent/work/repos/universal-language"
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, REPO + "/tools")
os.chdir(REPO + "/tools")
import names, offensive

LANGS = [("zh", "EA"), ("ja", "EA"), ("ko", "EA"), ("vi", "SEA"), ("th", "SEA"), ("id", "SEA"), ("tl", "SEA"),
         ("hi", "SA"), ("bn", "SA"), ("ta", "SA"), ("fa", "WA"), ("ar", "WA"), ("tr", "WA"), ("ru", "EU"),
         ("es", "EU"), ("fr", "EU"), ("sw", "SSA"), ("ha", "SSA"), ("yo", "SSA"), ("qu", "AM")]
REG = dict(LANGS)
ORDER = ["EA", "SEA", "SA", "WA", "EU", "SSA", "AM"]


def parse(path):
    items, cur = [], None
    for line in open(path):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith("@ "):
            c, page, sense = [x.strip() for x in line[2:].split("|", 2)]
            cur = dict(concept=c, page=page, sense=sense, rows={}, median="", note="", text=[])
            items.append(cur); continue
        m = re.match(r"(median|note|text):\s?(.*)", line)
        if m:
            k, v = m.groups()
            (cur["text"].append(v) if k == "text" else cur.__setitem__(k, v)); continue
        code, rest = line.split(" ", 1)
        word, mark, src = [x.strip() for x in rest.rsplit("|", 2)]
        assert mark in ("y", "n", "b", "u") and code in REG, line
        cur["rows"][code] = (word, mark, src)
    for it in items:
        assert set(it["rows"]) == set(REG), it["concept"]
    return items


def attested(src):
    return any(s in src for s in ("Wt", "We", "subs", "Leipzig"))


def score(it):
    got = [c for c, (w, m, s) in it["rows"].items() if m in "yb" and attested(s)]
    ceil = [c for c, (w, m, s) in it["rows"].items() if m in "ybu"]
    regs = sorted({REG[c] for c in got}, key=ORDER.index)
    cregs = {REG[c] for c in ceil}
    ok = len(got) >= 12 and len(regs) >= 5
    return got, regs, len(ceil), len(cregs), "pass" if ok else "fail"


# collisions: every form the language already uses
FORMS = {}
for name, col in (("lexicon.tsv", "gloss"), ("grammar.tsv", "gloss"), ("numbers.tsv", "value")):
    for r in csv.DictReader(open(os.path.join(REPO, "data", name)), delimiter="\t"):
        FORMS.setdefault(r["form"], []).append(f"{r[col]} ({name.split('.')[0]})")
spell = open(os.path.join(REPO, "docs", "language.md")).read().split('id="r-11-5"')[1].split("##")[0]
for w in re.findall(r"\*\*([a-z]+)\*\*", spell):
    FORMS.setdefault(w, []).append("spelling word (language.md 11.5)")

# What a failing candidate becomes (deep-layer test, then the phrase line). root_families = WOLD languages'
# families with a native unanalyzable word (tests/deeplayer-01/pass.tsv), out of 24. [x] = on a list, no form yet.
FALLBACK = {
    "dolphin": "phrase: [pig] pi puya 'sea pig' (zh haitun, ja iruka 海豚, vi ca heo); 6/24 root families, not household",
    "mule": "phrase: from horse + [donkey], formed at use; 4/24 root families",
    "parrot": "root 'parrot': 13/24 root families, no world compound (edge tier, no alternative, as the author's line (b))",
    "camel": "neither: culture-bound regional animal (C), borrowed from its users' word as kangaroo is; 3/24 root families, "
             "four unrelated loan shapes",
    "cockroach": "root 'cockroach': a household pest across cultures (deep-layer); 9/24 root families; the world's "
                 "'X insect' builds use different X",
    "frying pan": "phrase: du [roast/fry] 'frying tool', 3 syllables (ar miqlah and sw kikaango are the instrument of 'fry')",
    "pepper": "root 'pepper, the spice': in kitchens across cultures; chili was decided as the phrase '[pepper] tikun' "
              "(2026-10-16), so it needs this word; PEPPER/CHILI PEPPER lump 14.8% (30 families), so not one word",
    "cotton": "root 'cotton': clothing material across cultures, 11/24 root families; on the balance audit's gap list",
    "silk": "phrase: demi pi enna 'cloth of (the) worm', formed at use; 2/24 root families, not everyday across cultures",
    "tattoo": "phrase: [pattern] pi unne 'skin pattern'; 7/24 root families; fails the deep-layer test",
    "candle": "root 'candle': a household light across cultures, 8/24 root families; on the balance audit's gap list",
    "coconut": "phrase: [palm tree] pi tanun 'palm fruit' (ja yashi no mi, ko yaja yeolmae); COCONUT/PALM TREE lump 5.2%",
    "helmet": "phrase: [hat] gufu 'hard hat', the world's compound (vi mu bao hiem, th muak nirapai, fa kolah-e imeni "
              "'safety hat', sw kofia ya chuma 'iron hat')",
    "injection": "phrase: [needle] pi [medicine]; where the world doesn't borrow it, it says 'needle' (sw sindano, ha allura, "
                 "yo abere, ta uci)",
    "mattress": "root 'mattress': household across cultures, 7/24 root families; or widen soti 'bed' (roadmap candidate)",
    "tin can": "phrase: nansa pi [metal] 'metal box' (vi hop thiec, ar ʿulbat as-safih 'tin box')",
}

rows = []
for it in parse(os.path.join(HERE, "loanwork", "panel.txt")):
    got, regs, cn, cr, v = score(it)
    form = coll = blk = mt = ""
    if v == "pass":
        form = names.adapt(it["median"])
        coll = "; ".join(FORMS.get(form, [])) or "none"
        blk, mt = str(offensive.blocked(form)).lower(), str(offensive.matches(form)).lower()
    rows.append([it["concept"], f"{len(got)}/20", f"{len(regs)} ({' '.join(regs)})", f"{cn}/{cr}", v,
                 f"[{it['median']}]", form, coll, blk, mt, FALLBACK.get(it["concept"], "loan"), it["note"]])
with open(os.path.join(HERE, "loans.tsv"), "w") as f:
    f.write("concept\tcount\tregions\tceiling_count/regions\tverdict\tmedian_ipa\tadapted\tcollision\t"
            "offensive_blocked\toffensive_matches\tdecision\tnote\n")
    for r in rows:
        f.write("\t".join(r) + "\n"); print(*r[:10], sep="\t")

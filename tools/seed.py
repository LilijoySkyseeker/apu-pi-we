"""Seed vocabulary decisions (roadmap B1 step 3; docs/vocabulary-method.md), 2026-10-08.

Reads data/concept-ranking.tsv (top 300 by area-balanced lineage coverage, plus NSM primes),
records a decision and evidence line for every seed concept in data/concepts.tsv, and adds the
new roots with words.py (topic area + opposites tagged for the optimizer).

  python seed.py
"""
import csv, os
import words as W

DATA = os.path.join(os.path.dirname(__file__), "..", "data")

# Concepts the grammar, numbers or existing words already express (method §2.1).
COVERED = {
    "ONE": ("number", "fi", "base-6 digit"), "TWO": ("number", "sa", "digit"), "THREE": ("number", "ka", "digit"),
    "FOUR": ("number", "da", "digit"), "FIVE": ("number", "te", "digit"), "SIX": ("number", "NObi", "place word 6"),
    "SEVEN": ("number", "NObi FI", "6+1"), "EIGHT": ("number", "NObi SA", "6+2"), "NINE": ("number", "NObi KA", "6+3"),
    "TEN": ("number", "NObi DA", "6+4"), "ELEVEN": ("number", "NObi TE", "6+5"), "TWELVE": ("number", "SA NObi", "2×6"),
    "TWENTY": ("number", "KA NObi SA", "3×6+2"),
    "WHAT": ("grammar", "yu", "question word"), "WHO": ("grammar", "Ewo yu", "person what"),
    "WHERE": ("grammar", "KEmu yu", "place what"), "HOW": ("grammar", "fu yu", "like what"),
    "WHEN": ("grammar", "MUyi yu", "time what"), "WHY": ("grammar", "gi yu", "because what"),
    "WE (INCLUSIVE)": ("grammar", "pen", "inclusive we"), "WE (EXCLUSIVE)": ("grammar", "din", "exclusive we"),
    "THOU": ("grammar", "me", "you"), "HE": ("grammar", "wan", "no gender"), "SHE": ("grammar", "wan", "no gender"),
    "THEY": ("grammar", "wan la", "he/she + plural"), "THAT": ("grammar", "ben", "determiner"),
    "HERE": ("grammar", "KEmu tan", "place this"), "THERE": ("grammar", "KEmu ben", "place that"),
    "IN": ("grammar", "mon / BEse", "at / inside"), "BELOW OR UNDER": ("existing", "below", ""),
    "IN FRONT OF": ("existing", "front", ""), "BEHIND": ("existing", "back", "body part doubles as direction"),
    "AFTERWARDS": ("grammar", "wo tan", "after this"), "THEN": ("grammar", "wo tan", "after this"),
    "NOTHING": ("grammar", "MUsu fa", "thing none"), "SOMEONE": ("grammar", "Ewo in", "person some"),
    "PEOPLE": ("grammar", "Ewo la", "person plural"), "THERE IS OR THERE ARE": ("grammar", "gun", "subjectless BE"),
    "BE ALIVE": ("existing", "live", ""), "BE ALIVE OR LIFE": ("existing", "live / life", ""),
    "FOR A LONG TIME": ("grammar", "nin MUyi NEtu", "during long time"),
    "MALE PERSON": ("existing", "man", ""), "STRIKE": ("existing", "hit", ""), "BURNING": ("existing", "burn", ""),
    "TURN AROUND": ("existing", "turn", ""), "LIE DOWN": ("existing", "lie.down", ""),
    "FLESH": ("existing", "meat", "FLESH/MEAT lumped by 87% of families (CLICS4, upper bound)"),
    "PATH": ("existing", "road", "PATH/ROAD lumped by 85% of families (upper bound)"),
    "EARTH (SOIL)": ("existing", "ground", ""), "RIGHT": ("existing", "right.side", ""),
    "SCARED": ("compound", "BE + fear", "is afraid; fear root exists"),
}
# Built from existing words or new roots (method §2.4): concept -> (expression, evidence)
COMPOUND = {
    "BOY": ("child + male", "child male"), "GIRL": ("child + female", "child female"),
    "OLD MAN": ("man + old", "man old"), "OLD WOMAN": ("woman + old", "woman old"),
    "WIFE": ("spouse + female", "spouse female; kinship rule: no sexed spouse roots"),
    "OLDER BROTHER (OF MAN)": ("sibling + old + male", "kinship rule: sibling + older/younger + male/female"),
    "OLDER BROTHER (OF WOMAN)": ("sibling + old + male", "speaker's sex not marked"),
    "YOUNGER BROTHER (OF MAN)": ("sibling + young + male", ""), "YOUNGER BROTHER (OF WOMAN)": ("sibling + young + male", ""),
    "OLDER SISTER (OF MAN)": ("sibling + old + female", ""), "OLDER SISTER (OF WOMAN)": ("sibling + old + female", ""),
    "YOUNGER SISTER (OF MAN)": ("sibling + young + female", ""), "YOUNGER SISTER (OF WOMAN)": ("sibling + young + female", ""),
    "UPPER LEG (THIGH)": ("leg + above", "part of leg"), "LOWER LEG": ("leg + below", ""),
    "UPPER ARM": ("arm + above", ""), "LOWER ARM": ("arm + below", ""),
    "NIPPLE": ("breast + above", "tip of breast"),
    "SMELL (STINK)": ("smell + bad", "smell + bad"),
}
# New roots: concept -> (gloss, field, antonym of an earlier-added or existing word, evidence)
ROOTS = {
    "BREAST": ("breast", "body"), "NECK": ("neck", "body"), "LIVER": ("liver", "body"), "KNEE": ("knee", "body"),
    "THROAT": ("throat", "body"), "NAVEL": ("navel", "body"), "LUNG": ("lung", "body"), "BRAIN": ("brain", "body"),
    "LIP": ("lip", "body"), "SHOULDER": ("shoulder", "body"), "BUTTOCKS": ("buttocks", "body"),
    "PENIS": ("penis", "body"), "VULVA": ("vulva", "body"), "TESTICLES": ("testicles", "body"),
    "FINGER": ("finger", "body"), "TOE": ("toe", "body"), "FINGERNAIL": ("nail", "body"),
    "FEATHER": ("feather", "animal"), "HORN (ANATOMY)": ("horn", "animal"), "LOUSE": ("louse", "animal"),
    "ANT": ("ant", "animal"), "MOSQUITO": ("mosquito", "animal"),
    "GRASS": ("grass", "nature"), "ROOT": ("root", "nature"), "FLOWER": ("flower", "nature"), "SEED": ("seed", "nature"),
    "BARK": ("bark", "nature"), "DUST": ("dust", "nature"), "THUNDER": ("thunder", "nature"), "SHADE": ("shade", "nature"),
    "FAT (ORGANIC SUBSTANCE)": ("fat", "body"), "SWEAT (SUBSTANCE)": ("sweat", "body"), "MILK": ("milk", "thing"),
    "BITE": ("bite", "action"), "SPIT": ("spit", "action"), "TIE": ("tie", "action"), "VOMIT": ("vomit", "action"),
    "BLOW (OF WIND)": ("blow", "action"), "COUGH": ("cough", "action"), "PISS": ("urinate", "action"),
    "SHIT (DEFECATE)": ("defecate", "action"), "FART": ("fart", "action"), "BREATHE": ("breathe", "action"),
    "SUCK": ("suck", "action"), "SNEEZE": ("sneeze", "action"), "YAWN": ("yawn", "action"), "SNORE": ("snore", "action"),
    "CRUSH": ("crush", "action"), "DIG": ("dig", "action"),
    "SMELL (PERCEIVE)": ("smell", "sense"), "TOUCH": ("touch", "sense"), "TASTE": ("taste", "sense"),
    "SALTY": ("salty", "taste"), "SWEET": ("sweet", "taste"), "BITTER": ("bitter", "taste", "sweet"), "SOUR": ("sour", "taste"),
    "ROTTEN": ("rotten", "quality"), "RIPE": ("ripe", "quality"), "RAW": ("raw", "quality", "ripe"),
    "BLUNT": ("blunt", "quality", "sharp"), "ROUND": ("round", "quality"), "FLAT": ("flat", "quality"),
    "STRAIGHT": ("straight", "quality"), "CROOKED": ("crooked", "quality", "straight"),
    "SMOOTH": ("smooth", "quality"), "ROUGH": ("rough", "quality", "smooth"),
    "CORRECT (RIGHT)": ("correct", "quality"), "WRONG": ("wrong", "quality", "correct"),
    "YOUNG": ("young", "quality", "old"), "UGLY": ("ugly", "quality", "beautiful"),
    "QUIET": ("quiet", "quality"), "LOUD": ("loud", "quality", "quiet"),
    "THIN (SLIM)": ("thin", "size", "thick"), "THIN (OF SHAPE OF OBJECT)": ("thin", "size"),
    "NARROW": ("narrow", "size", "wide"), "DEEP": ("deep", "size"), "SHALLOW": ("shallow", "size", "deep"),
    "HIGH": ("high", "space"), "LOW": ("low", "space", "high"), "BESIDE": ("side", "space"), "BETWEEN": ("between", "space"),
}
# Added for reasons other than rank (method §3.1 kinship, §4 lens, ARM exception)
EXTRA_ROOTS = [
    ("sibling", "people", None, "kinship rule: sibling without sex (efficient-semantics notes)"),
    ("spouse", "people", None, "kinship rule"),
    ("arm", "body", None, "ARM/HAND lumped by 35% of families -> two words; no transparent derivation from 'hand' exists here, so a root (exception to the 20-50% band, noted)"),
    ("north", "space", None, "lens: both spatial frames cheap (research/notes/lens.md)"),
    ("south", "space", "north", "lens"), ("east", "space", None, "lens"), ("west", "space", "east", "lens"),
]


def tier(rank):
    return 4 if rank and rank <= 100 else 3 if rank and rank <= 200 else 2


def main():
    rank = list(csv.DictReader(open(os.path.join(DATA, "concept-ranking.tsv")), delimiter="\t"))
    seed = [r for r in rank if (r["rank"] and int(r["rank"]) <= 300) or r["nsm_prime"] == "1"]
    lex = {w["gloss"].lower(): w["form"] for w in W.read("lexicon.tsv")}
    gram = {g["gloss"].lower(): g["form"] for g in W.read("grammar.tsv")}
    rows, added = [], set()

    for gl, field, ant, ev in EXTRA_ROOTS:
        if gl not in lex:
            W.add_content(gl, field, 3, (ant,) if ant else ())
            added.add(gl)
    for r in seed:
        c, rk = r["gloss"], int(r["rank"]) if r["rank"] else None
        base = c.lower().split(" (")[0]
        ev = f"coverage {r['coverage']}, {r['families']} families, {r['areas_present']} areas" if r["coverage"] else "NSM prime"
        if c in COVERED:
            kind, expr, note = COVERED[c]
        elif c in COMPOUND:
            kind, (expr, note) = "compound", COMPOUND[c]
        elif c in ROOTS and ROOTS[c]:
            spec = ROOTS[c]
            gl, field = spec[0], spec[1]
            ant = spec[2] if len(spec) > 2 else None
            if gl not in lex and gl not in added:
                W.add_content(gl, field, tier(rk), (ant,) if ant else ())
                added.add(gl)
            kind, expr, note = "root", gl, ("opposite of " + ant) if ant else ""
        elif base in lex:
            kind, expr, note = "existing", base, ""
        elif base in gram:
            kind, expr, note = "grammar", gram[base], ""
        else:
            kind, expr, note = "UNDECIDED", "", ""
        rows.append({"rank": r["rank"], "concept": c, "decision": kind, "expression": expr,
                     "evidence": "; ".join(x for x in (ev, note) if x)})
    for gl, field, ant, ev in EXTRA_ROOTS:
        rows.append({"rank": "", "concept": gl.upper(), "decision": "root", "expression": gl, "evidence": ev})
    W.write("concepts.tsv", rows, ["rank", "concept", "decision", "expression", "evidence"])
    und = [r["concept"] for r in rows if r["decision"] == "UNDECIDED"]
    print(f"{len(rows)} rows; {len(added)} new roots; undecided: {und}")


if __name__ == "__main__":
    main()

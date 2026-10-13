"""Generate the GF lexicon (grammar/Lex.gf, LexApu.gf, LexEng.gf) from the data files. Never edit those by hand.

Content words have no fixed word class (language.md 4.2.3), so every root gets one function per role:
word_N (thing), word_V (event), word_A (quality), all with the same Apupiwe form (formal-grammar.md
"How content words fit"). Grammar words, the two-syllable operators and number words are not content
words; the hand-written grammar has them.

Apupiwe side: each role carries four features the grammar needs, all from the data files:
  act   the root names an action: gun + it is the undergoer's state (4.7.4)   data/roles.tsv
  obj   as a verb it takes an object, so a verb after it is that object (4.2.6)  data/roles.tsv
  tm    a time word: wo/ya after it belong to it (4.4.1, 8.2)                 lexicon field "time", time loans
  gd    a gender word: a derived word's base ends before it (5.4.4)            GENDER below
  res   followed by a result and an object, "make it so" (4.2.7)             RESULT below
English side: the gloss's first sense, looked up per role in the RGL's MorphoDictEng and IrregEng;
when the word doesn't exist in that role, a crude derivation is used (English is for checking glosses).

  python tools/gf_lexicon.py      # run inside the dev shell (needs gf)
"""
import csv, os, re, subprocess, sys, tempfile, collections

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "grammar")

# The two-syllable operators kept in lexicon.tsv (language.md 13.2): grammar words, not content words.
OPS2 = set("genso wanme inwun wemen konsin nedin tason mesun manni buntu buni donon lanno anko nuwen kiyo mena".split())
GENDER = {"futa", "lowu"}            # 5.2.2, 5.4.4
RESULT = {"muge"}                    # 4.2.7
TIME_EXTRA = {"awuwa", "minitu", "sekandu"}  # 8.2.5 loans
VERBISH = {"action", "motion", "sense", "mind"}
ADJISH = {"quality", "size", "color", "taste"}
# English where the gloss's first sense gives a poor word for a role.
OVERRIDE = {
    ("enpa", "N"): 'P.mkN "freedom"',
    ("nuta", "A"): 'P.mkA "afraid"',
    ("pume", "N"): 'P.mkN "thought"',
    ("nosen", "N"): 'P.mkN "God"',
    ("kuwi", "V"): 'P.mkV "protect"',
    ("ewo", "N"): 'P.mkN "person" "people"',
    ("guyi", "N"): 'D.house_N',
}


def read(name):
    with open(os.path.join(DATA, name)) as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def rgl_funs(module):
    """Function names of an RGL lexicon module, asked of GF itself."""
    with tempfile.TemporaryDirectory() as d:
        src = os.path.join(d, "T.gf")
        open(src, "w").write(f"--# -path=.:alltenses:morphodict\nabstract T = {module} ** {{}}\n")
        out = subprocess.run(["gf", "--run", src], input="pg -funs\n", capture_output=True, text=True).stdout
    names = {l.split(" :")[0].strip() for l in out.splitlines() if " : " in l}
    if not names:
        sys.exit(f"gf_lexicon: could not list {module}; run inside the dev shell (direnv exec . python3 ...)")
    return names


def first_sense(gloss):
    g = gloss.split(";")[0].split(",")[0].strip()
    g = re.sub(r"^(a|an|to|be) ", "", g)
    g = re.sub(r"\s*\(.*\)", "", g)
    return g


def ing(w):
    if w.endswith("ie"):
        return w[:-2] + "ying"
    if w.endswith("e") and not w.endswith("ee"):
        return w[:-1] + "ing"
    return w + "ing"


def english(form, gloss, field, MD, IRR):
    w = first_sense(gloss)
    key = w.replace(" ", "_")

    def verb():
        if key + "_V" in IRR:
            return f"I.{key}_V"
        if key + "_V" in MD:
            return f"D.{key}_V"
        cands = sorted(n for n in MD if n.startswith(key + "_") and n.endswith("_V") and n.count("_") == 2)
        irregular = [c for c in cands if not c.split("_")[1].endswith("ed")]
        return "D." + irregular[0] if irregular else None

    have = {"N": f"D.{key}_N" if key + "_N" in MD else None, "V": verb(),
            "A": f"D.{key}_A" if key + "_A" in MD else None}
    out, how = {}, {}
    for r in "NVA":
        if (form, r) in OVERRIDE:
            out[r], how[r] = OVERRIDE[(form, r)], "override"
        elif have[r]:
            out[r], how[r] = have[r], "dictionary"
        else:
            how[r] = "derived"
            if r == "N":
                out[r] = (f'P.mkN "{ing(w)}"' if field in VERBISH and have["V"] else
                          f'P.mkN "{w}ness"' if field in ADJISH and have["A"] else f'P.mkN "{w}"')
            elif r == "V":
                out[r] = f'P.mkV "{w}"'
            else:
                out[r] = f'P.mkA "{ing(w)}"' if have["V"] else f'P.mkA "{w}"'
    return out, how


def gfbool(b):
    return "True" if b else "False"


def main():
    lex = read("lexicon.tsv")
    roles = {r["form"]: r for r in read("roles.tsv")}
    numbers = {r["form"] for r in read("numbers.tsv")}
    grammar = {r["form"] for r in read("grammar.tsv")}
    content = [r for r in lex if r["form"] not in OPS2 | numbers | grammar and r["field"] != "number"]
    missing = [r["form"] for r in content if r["form"] not in roles]
    if missing:
        sys.exit("gf_lexicon: no row in data/roles.tsv for: " + " ".join(missing))
    MD, IRR = rgl_funs("MorphoDictEngAbs"), rgl_funs("IrregEngAbs")

    abs_, apu, eng, stats = [], [], [], collections.Counter()
    for r in sorted(content, key=lambda r: r["form"]):
        w = r["form"]
        ro = roles[w]
        feats = dict(act=ro["action"] == "yes", obj=ro["takes_object"] == "yes",
                     tm=r["field"] == "time" or w in TIME_EXTRA, gd=w in GENDER, res=w in RESULT)
        out, how = english(w, r["gloss"], r["field"], MD, IRR)
        f = " ; ".join(f"{k} = {gfbool(v)}" for k, v in feats.items())
        for role in "NVA":
            abs_.append(f"    {w}_{role} : {role} ;  -- {r['gloss']}")
            apu.append(f'    {w}_{role} = {{s = "{w}" ; {f}}} ;')
            eng.append(f"    {w}_{role} = {out[role]} ;")
            stats[how[role]] += 1

    hdr = "-- GENERATED by tools/gf_lexicon.py from data/lexicon.tsv and data/roles.tsv. Do not edit.\n"
    write("Lex.gf", hdr + "abstract Lex = {\n  cat\n    N ;  -- a root used as a thing\n"
          "    V ;  -- a root used as an event\n    A ;  -- a root used as a quality\n  fun\n"
          + "\n".join(abs_) + "\n}\n")
    write("LexApu.gf", hdr + "concrete LexApu of Lex = open Prelude in {\n  lincat N, V, A = {s : Str ; act, obj, tm, gd, res : Bool} ;\n"
          "  lin\n" + "\n".join(apu) + "\n}\n")
    write("LexEng.gf", hdr + "--# -path=.:alltenses:morphodict\n"
          "concrete LexEng of Lex = open SyntaxEng, (P=ParadigmsEng), (D=MorphoDictEng), (I=IrregEng) in {\n"
          "  lincat N = SyntaxEng.N ; V = SyntaxEng.V ; A = SyntaxEng.A ;\n  lin\n" + "\n".join(eng) + "\n}\n")
    print(f"{len(content)} roots, {3 * len(content)} functions; English per role: {dict(stats)}")


def write(name, text):
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Consolidate the concept list for the ~1,500-root placement (conceptlist-01).

Reads the decided inputs (read-only) and writes concepts.tsv and excluded.tsv
next to this file. Hand decisions taken from docs/design-log.md are in the
tables below, each with the log entry it comes from; choices of mine are
marked "added". Run from anywhere:

    direnv exec /home/agent/work/repos/universal-language python3 tests/conceptlist-01/build.py
"""
import csv, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "../.."))
P = lambda *a: os.path.join(REPO, *a)


def tsv(path):
    with open(P(path), newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def syll(phrase):
    """Syllables of an Apupiwe phrase: one per vowel; a bracketed [concept] counts 2 (coverage-02 r2)."""
    phrase = re.sub(r"\[[^\]]*\]", "aa", phrase)
    n = 0
    for w in phrase.lower().split():
        if w in LEXFORMS or re.fullmatch(r"[ptkbdgmnfslwy]?[aeiou]n?", w) or w == "aa":
            n += len(re.findall(r"[aeiou]", w))
        else:
            n += 2  # an English placeholder for a root without a form yet (added: counts as 2, as [x] does)
    return n


LEXFORMS = {r["form"] for r in tsv("data/lexicon.tsv")}


# ---------------------------------------------------------------- sources
SRC = {
    "LEX": "data/lexicon.tsv (today's lexicon)",
    "LAD": "coverage-01 ladder pass (part3/ladder.tsv; roots-1500, author 2026-10-13)",
    "WB": "first-word filter (part3/wordbank-final.tsv; author 2026-10-13, audit item 1)",
    "LOAN": "loan panel (part3/loans-final.tsv, loans-rerun.tsv; author 2026-10-13)",
    "REL": "religion decisions (part3/religion.tsv; author 2026-10-13)",
    "ADD1": "coverage-01 part3/additions.tsv (the decisions it cites)",
    "BAL": "balance-02 entrants, 51 added (author 2026-10-15) + their boundaries (author 2026-10-16)",
    "WALK": "concept walk round 2, G at ranks 1243-1342 (2026-10-16, stop under both raters)",
    "PL": "phrase line (author 2026-10-16) applied to a decided item",
    "WOLD-core": "WOLD deep layer, core D (author 2026-10-16, option b)",
    "WOLD-edge": "WOLD deep layer, edge D with no alternative (author 2026-10-16, option b)",
    "WOLD-codex": "WOLD deep layer, 20 added after Codex's check (author 2026-10-16)",
    "WOLD-47": "WOLD meaning covered only by a walk proposal, classified here by the deep-layer test (added)",
    "DROP": "drops and re-checks (author 2026-10-16)",
    "PL-retro": "phrase line applied to older phrases (author 2026-10-16, consolidated list's questions)",
    "SUBJ": "school subjects every system teaches get roots (author 2026-10-16)",
    "BQ02": "WOLD boundary questions decided by rung 4 (tests/deeplayer-02/bq.tsv; author 2026-10-16)",
    "LOAN02": "WOLD loan candidates through the panel (tests/deeplayer-02/loans.tsv; author 2026-10-16)",
}

# the retroactive phrase line (author 2026-10-16): these become roots unless the world's usual compound.
# Which is the world's compound is my reading (added): a compound of two content words most panel
# languages use; a derivation by affix (king-dom, child-hood) is not a compound.
RETRO = {
    "century": ("root", "fawu loki (4 syll); own words or loans (siecle, qarn, vek, abad)"),
    "kingdom": ("root", "gigin pi king (5 syll); king + country only in zh ja ko vi; elsewhere derived from king (added reading)"),
    "welcome": ("phrase", "world compound 'good come' (bienvenido, willkommen, hos geldiniz, svagat); a routine (10.2.5)"),
    "library": ("phrase", "world compound 'book house/place' (tushuguan, toshokan, kutuphane, ketabxane, pustakalay)"),
    "childhood": ("root", "muyi pi tiwu (5 syll); derived from child by affix in most languages (added reading)"),
    "patient (sick person)": ("root", "ewo simi (4 syll)"),
    "throne": ("root", "pu goyu pi king (6 syll)"),
    "corpse": ("root", "gawo fafin (4 syll); 'dead body' is a compound only in some (ja, en)"),
    "giant": ("root", "ewo bi kudu (5 syll)"),
    "plain (land)": ("root", "sekan mawun (4 syll)"),
    "prime minister": ("phrase", "world compound 'chief minister' (pradhan mantri, waziri mkuu, perdana menteri, shusho, basbakan); minister is a root"),
    "salary": ("root", "nimo pi doku (5 syll)"),
    "delicious": ("root", "tenmi upe (4 syll)"),
    "fill": ("root", "muge kete (4 syll)"),
    "descend": ("root", "isi deba (4 syll); also covers WOLD 10-473 descend and 10-92 land"),
    "acquaintance": ("root", "ewo pi lugo (5 syll)"),
}
RETRO_GLOSS = {"patient (sick person)": "patient, sick person (in care)", "plain (land)": "plain (flat open land)",
               "fill": "fill, make full", "descend": "descend, go down; land", "corpse": "corpse, dead body",
               "giant": "giant", "acquaintance": "acquaintance, person one knows"}
RETRO_FIELD = {"century": "time", "kingdom": "people", "childhood": "time", "patient (sick person)": "people",
               "throne": "thing", "corpse": "body", "giant": "people", "plain (land)": "nature", "salary": "abstract",
               "delicious": "quality", "fill": "action", "descend": "motion", "acquaintance": "people"}

# ------------------------------------------------------- rank and tier
cand = tsv("tests/coverage-02/candidates.tsv")
RANK = {}
for r in cand:
    for k in (r["canonical"], r["best_label"]):
        RANK.setdefault(k.lower(), int(r["crank"]))


def rank_of(label):
    l = label.lower()
    if l in RANK:
        return RANK[l]
    base = re.sub(r"\s*\(.*\)$", "", l)
    # a split sense: only the first (main) sense inherits the label's rank
    return None if base != l else RANK.get(base)


def tier_of(rank):
    """Corrected rank -> tier (added): cuts set from today's roots' medians by tier
    (t5 10, t4 74, t3 302, t2 520, t1 900 in the corrected ranking)."""
    if rank is None:
        return None
    return 5 if rank <= 25 else 4 if rank <= 150 else 3 if rank <= 450 else 2 if rank <= 900 else 1


# ----------------------------------------------------------- output rows
concepts = collections.OrderedDict()   # key -> row
excluded = []


def add(concept, route, form, field, tier, source, note="", antonym="", rank=None, key=None):
    key = (key or concept).lower()
    if key in concepts:
        c = concepts[key]
        c["source"] += "; also " + source
        if note:
            c["note"] = (c["note"] + "; " + note).strip("; ")
        return c
    concepts[key] = dict(concept=concept, route=route, form=form, field=field, tier=tier,
                         rank="" if rank is None else rank, antonym=antonym, source=source, note=note)
    return concepts[key]


def drop(concept, reason, source, note=""):
    excluded.append(dict(concept=concept, reason=reason, source=source, note=note))


def remove(key, reason, source):
    c = concepts.pop(key.lower())
    drop(c["concept"], reason, source, "was admitted by " + c["source"])


# ===================================================== 1. today's lexicon
lex = tsv("data/lexicon.tsv")
FIXED = set("genso wanme inwun wemen konsin buntu tason nedin mesun manni buni donon lanno anko nuwen kiyo mena".split())
FAILED_LOANS = {  # loans-rerun.tsv (author 2026-10-13): native root; the loan form retires
    "hour": "loans-rerun: fail 4/3", "minute, of time": "loans-rerun: fail 9/5",
    "second, of time": "loans-rerun: fail 7/4", "photo": "loans-rerun: fail 9/5",
    "degree (°)": "loans-rerun: fail 5/3", "police": "loans-rerun: fail 11/5 (author 2026-10-13)",
}
LEXGLOSS = {r["gloss"]: r["gloss"] for r in lex}
for r in lex:
    g, f, t, form = r["gloss"], r["field"], int(r["tier"]), r["form"]
    if form in FIXED:
        drop(g, "grammar: two-syllable operator, part of the short-word layer", "LEX",
             f"{form}; kept fixed by part4/placement.py (FIXED), not placed with the roots")
        continue
    if f == "loan":
        if g in FAILED_LOANS:
            fld = {"police": "people", "photo": "thing", "degree (°)": "abstract"}.get(g, "time")
            add(g, "root", "", fld, t, "LEX; LOAN",f"failed loan ({FAILED_LOANS[g]}); today's {form} retires, a native root replaces it")
        else:
            add(g, "kept loan", form, "loan", t, "LEX", "loan form fixed by the panel or the standard")
        continue
    note = ""
    if f == "number":
        note = "number word; placed with the roots (placement weights number pairs x10)"
    add(g, "root", form, f, t, "LEX", note)

concepts["nail, of a finger or toe"]["concept"] = "nail (of a finger or toe), claw"
concepts["nail, of a finger or toe"]["source"] += "; BQ02 (claw joins: 53.9%)"
concepts["nail, of a finger or toe"]["note"] = "claw/nail one root (author 2026-10-16, deeplayer-02 4-345); the lexicon gloss changes at adoption"
concepts["key, button"]["concept"] = "key (for a lock)"
concepts["key, button"]["source"] += "; BQ02"
concepts["key, button"]["note"] = "the button splits off as its own root; tinli stays 'key' (author 2026-10-16, deeplayer-02 6-62); the lexicon gloss changes at adoption"

# ===================================================== 2. ladder (+ first-word filter, loan panel)
lad = tsv("tests/coverage-01/part3/ladder.tsv")
wbf = {r["n"]: r for r in tsv("tests/coverage-01/part3/wordbank-final.tsv")}
loans = {r["concept"]: r for r in tsv("tests/coverage-01/part3/loans-final.tsv")}

FIELD = {  # ladder field -> the lexicon's field names (added)
    "home": "thing", "clothing": "thing", "transport": "thing", "tech": "thing", "food": "thing",
    "place": "space", "society": "people", "money": "abstract", "work": "abstract", "health": "body",
    "art": "abstract", "religion": "abstract", "": "abstract",
}
PRODUCE = set("apple orange banana potato carrot bean pea nut grape strawberry pear cucumber melon watermelon maize "
              "grain vegetable wheat tomato rose".split())
PERSON = set("teacher clown baby leader soldier hero actor expert governor secretary worker student mayor detective "
             "witness customer master citizen adult nurse guest prisoner spy scholar lawyer servant lover messenger "
             "host fool victim coach prostitute volunteer candidate minister judge king slave native professional "
             "ambassador doctor engineer captain pilot professor president saint priest".split())
VERB = set("jump dance draw kick kiss tickle paint drive hug catch cover bring lick hurry wipe pour sweep repair clap "
           "spill smile knock ride decide explain promise support attack visit prepare translate create rise threaten "
           "defeat notice announce arrest react prove measure pass pray travel transfer serve escape demand divide "
           "regret praise continue compare establish define arrange imagine supply expect approach comment invite "
           "discuss invest care worry protest contribute publish raise perform claim guarantee exchange punish cross "
           "fail introduce damage appear behave investigate invent solve print believe spread repeat manage release "
           "describe reform mention improve settle spend edit confess offer withdraw register treat suspect retire "
           "represent recognize prevent mix vote bless curse sacrifice analyze sink".split())
QUAL = set("pleasant cute naughty different special clear serious real modern possible alone direct brave original "
           "rich major fresh pure tense wise poor proud busy popular positive negative rare extreme regular innocent "
           "responsible perfect blind available drunk satisfied complex normal honest tight strict sensitive famous "
           "permanent single former foreign public international".split())


def ladder_field(r):
    c, f = r["concept"], r["field"]
    base = re.sub(r"\s*\(.*\)$", "", c)
    if base in PERSON:
        return "people"
    if base in VERB and f not in ("action", "motion", "sense", "mind"):
        return "action"
    if base in QUAL and f not in ("quality", "mind"):
        return "quality"
    if f == "food" and base in PRODUCE:
        return "nature"
    return FIELD.get(f, f)


# sense glosses for labels an English reader could take another way (added)
GLOSS = {
    "mouse": "mouse (the animal; also the computer mouse)", "ball": "ball (round toy)", "glasses": "glasses, spectacles",
    "swing": "swing (playground seat)", "slide": "slide (playground slide)", "slide (slip)": "slide, slip (move smoothly over a surface)",
    "block": "block (toy building block)", "block (obstruct)": "block, obstruct", "sink": "sink, basin",
    "tear": "tear, teardrop", "tear (rip)": "tear, rip", "party": "party, celebration", "party (political)": "political party",
    "state": "state, polity", "general": "general, overall", "case": "case, instance", "case (legal)": "case (legal), lawsuit",
    "letter": "letter, mail", "letter (alphabet)": "letter of the alphabet", "class": "class (school group)",
    "class (social)": "social class", "space": "space, room to fit", "space (outer)": "outer space",
    "interest": "interest, curiosity", "interest (money)": "interest (on money)", "race": "race, contest of speed",
    "race (people)": "race, ethnic group (social category)", "match": "match, contest", "match (fire)": "match, matchstick",
    "stage": "stage, phase", "stage (theatre)": "stage (theatre platform)", "bow": "bow, bend the body",
    "bow (weapon)": "bow (the weapon)", "cabinet": "cabinet (government)", "square": "square (the shape)",
    "square (place)": "square, plaza", "application": "app, software application", "application (request)": "application, formal request",
    "fan": "fan, supporter", "fan (device)": "fan (cooling device)", "plain": "plain, simple", "press (media)": "the press, news media",
    "strike (labour)": "strike (labour)", "tip (gratuity)": "tip, gratuity", "spring (water)": "spring (water source)",
    "patient (enduring)": "patient, enduring", "date (romantic)": "date (romantic meeting)", "general (military)": "general (army rank)",
    "last": "last, final", "point": "point, dot", "line": "line, stripe, row", "form": "form (format; a form to fill in)",
    "record": "record, recording", "rise": "rise, go up", "address": "address (postal or email)",
    "notice": "notice, become aware of", "article": "article (a written piece)", "unit": "unit (of measure)",
    "scene": "scene (of a play or film)", "style": "style, manner", "sign": "sign, signal, mark", "capital": "capital city",
    "step": "step, pace", "pass": "pass, go past or through", "ring": "ring (finger ring)", "bill": "bill, invoice",
    "suit": "suit (the garment)", "base": "base, basis", "fund": "fund (money set aside)", "view": "view, scenery, perspective",
    "title": "title, heading", "character": "character, personality", "expression": "expression (phrase; facial)",
    "list": "list", "screen": "screen (display)", "sense": "sense (good sense; a sense organ)", "score": "score, points",
    "crown": "crown (worn by a monarch)", "tense": "tense, strained, nervous", "board": "board, plank",
    "cross": "cross, go across", "charge": "charge (a battery)", "plot": "plot (of a story)", "term": "term (word for a concept)",
    "wave": "wave (of water; wave a hand)", "court": "court (of law)", "iron": "iron (the metal)", "cell": "cell (biological)",
    "major": "major, main, chief", "sentence": "sentence (grammar)", "content": "content (what is inside)",
    "master": "master, lord", "matter": "matter, affair, issue", "spirit": "spirit (a being)", "joint": "joint (of the body)",
    "rate": "rate (speed, ratio, rate of pay)", "band": "band (music group)", "shift": "shift (work shift)",
    "volume": "volume (loudness; a book volume)", "pole": "pole, post", "host": "host (who receives guests)",
    "grade": "grade", "trial": "trial", "single": "single", "medium": "medium", "port": "port, harbour",
    "branch": "branch (of a tree)", "spade": "spade, shovel", "pot": "pot, cooking pot", "yard": "yard, courtyard",
    "bear": "bear (the animal)", "dress": "dress (the garment)", "plate": "plate, dish", "cover": "cover, lid; to cover",
    "bubble": "bubble", "orange": "orange (the fruit)", "draw": "draw (make a picture)", "hall": "hall, large room",
    "approach": "approach, come near", "flag": "flag", "pair": "pair, couple", "direct": "direct, directly",
    "mind": "mind, intellect", "drive": "drive (a vehicle)", "catch": "catch, capture", "kick": "kick",
    "temple": "place of worship (temple, widened)", "priest": "religious leader (priest, widened)",
    "saint": "holy person (saint, widened)", "miracle": "wonder, an astonishing unexplained event (miracle is built: wonder of god)",
    "devil": "evil spirit, demon, devil", "sacrifice": "offering, sacrifice", "pray": "pray, worship",
    "believe": "believe; faith, belief", "bless": "bless, blessing", "heaven": "heaven, paradise", "sin": "sin",
    "hell": "hell", "soul": "soul", "curse": "curse", "religion": "religion", "monster": "monster",
    "lie (untruth)": "lie, tell an untruth", "even": "even", "goal": "goal, aim, purpose", "period": "period, era, interval",
    "level": "level, degree", "position": "position, posture, post", "middle": "middle, centre", "union": "union, alliance",
    "official": "official, civil servant", "operation": "operation, undertaking", "record ": "",
    "test": "test, exam", "judge": "judge (person; to judge)", "origin": "origin, source", "pressure": "pressure",
    "chapter": "chapter", "subject": "subject, topic", "appearance": "appearance, look", "circle": "circle",
    "course": "course (of study)", "standard": "standard, norm", "rich": "rich, wealthy", "divide": "divide, division",
    "habit": "habit, routine", "establish": "establish, found", "job": "job, occupation", "define": "define",
    "fault": "fault, flaw, defect", "wound": "wound, injury", "effect": "effect, impact", "element": "element, component",
    "novel": "novel (a long story)", "material": "material, substance", "raise": "raise, lift", "gender": "gender",
    "poison": "poison", "loan": "loan (money lent)", "shock": "shock", "essence": "essence, gist",
    "trick": "trick, deceive", "lover": "lover, partner in love", "former": "former, ex-", "presence": "presence",
    "sum": "sum, total", "edge": "edge, rim", "relationship": "relationship", "spread": "spread",
    "release": "release, let go", "department": "department", "contract": "contract", "exercise": "exercise (physical)",
    "practice": "practice, training", "evolution": "evolution", "promotion": "promotion", "instrument": "instrument (musical)",
    "atmosphere": "atmosphere (air layer; mood)", "argument": "argument, dispute", "access": "access", "frame": "frame",
    "note": "note (a short written message)", "register": "register, enrol", "background": "background",
    "review": "review", "deposit": "deposit", "compound": "compound", "organ": "organ (of the body)",
    "native": "native, indigenous", "moral": "moral, ethics", "merit": "merit", "mix": "mix",
    "gas": "gas (state of matter; fuel gas)", "model": "model (simplified representation; fashion model)",
    "bar": "bar (place serving drinks)", "club": "club, society", "bank": "bank (financial)",
    "program": "program (software; broadcast programme)", "code": "code (computer code; a cipher)",
    "mass": "mass (physical quantity)", "cream": "cream (of milk; cosmetic)", "station": "station (train, bus)",
    "channel": "channel (TV, radio)", "league": "league (sports)", "profile": "profile (online, personal)",
    "party": "party (social gathering, celebration)", "engine": "engine, motor", "fuel": "fuel (petrol, gasoline)",
}
SPLIT_FIRST = {}  # parent label -> sense-1 gloss, from the ladder notes

RELIGION_TRADITION = {"church", "angel", "bishop", "prophet", "mosque", "pope"}
DROP_TITLES = {"knight", "senator", "lieutenant", "colonel"}
MIL_RANKS = {"general (military)"}  # military ranks dropped, general included; civic offices kept (author 2026-10-16)
DROP_SPECIALIST = {"statistics", "psychology", "circuit", "orbit", "formula", "sphere"}
MIXED = {  # each sense re-checked alone (author 2026-10-16); the readings are mine (added)
    "compound": "chemical compound: specialist (long tail); a walled compound: culture-bound housing form, phrase 'guyi la man senmo'; compound word: built word, a grammar term",
    "grade": "school mark: covered by wifu 'number' / score (on the list); level: covered by level; slope: rare",
    "trial": "court trial: covered by case (legal) + court; a test: covered by test",
    "single": "unmarried: phrase su bedan (3 syll); one alone: alone / na fi; a music single: specialist",
    "term": "a word for a concept: covered by word; school term: covered by period; terms, conditions: covered by condition",
    "deposit": "bank deposit: phrase yaga nimo (4 syll; long tail, rank of the sense alone unknown); mineral deposit: specialist; put down: yaga",
    "review": "check again: covered by loban 'check'; a critique (film review): long tail",
    "promotion": "job promotion: long tail (rank of the sense alone unknown; 'rise in level'); sales promotion: specialist",
    "medium": "middle-sized: covered by middle; mass media: covered by press (media); a spirit medium: culture-bound",
    "background": "behind: nebe; setting: phrase; personal history: covered by history / weyu 'story'",
}
PHRASE_LINE_ITEMS = {  # (author 2026-10-16: a phrase if it meets the phrase line, else a root)
    "receipt": ("root", "kemin pi unfu (5 syll) is over the line"),
    "available": ("root", "lenu bone (4 syll) is over the line"),
    "priority": ("root", "ke bawe se we (5 syll) is over the line"),
    "passenger": ("phrase", "no [ride] (3 syll) meets the line"),
}
PL_LOANS = {"chemistry": "5-of-7-regions rule fails the loan (author 2026-10-15); a school subject every system teaches, so a root (author 2026-10-16)"}
SUBJECTS = {"chemistry", "physics", "biology", "history", "mathematics"}  # (author 2026-10-16); specialist fields stay long tail
BAL_PHRASE_OVERRIDES = {  # ladder roots that later boundary decisions turned into phrases or merged
    "opinion": ("phrase: 'what one thinks' (ge pume)", "attitude decision (author 2026-10-16): opinion is a phrase"),
    "festival": ("phrase: 'time of celebrating'; each culture's own festivals borrowed", "celebrate decision (author 2026-10-16)"),
    "merit": ("covered by worthy ('worthy, deserving' covers merit)", "worthy decision (author 2026-10-16)"),
}

for r in lad:
    n, c, st, route = r["n"], r["concept"], r["status"], r["route"]
    if st == "split" and route == "":
        continue  # placeholder; its .a/.b rows carry the senses
    w = wbf.get(n)
    if w and w["final"] not in ("keep", "loan"):
        fin = w["final"]
        if fin == "duplicate":
            drop(c, "covered by " + (st.split(":", 1)[1] if ":" in st else "an existing word"), "WB; LAD", w["reason"])
        elif fin == "built":
            drop(c, "phrase: built word (" + (st.split(":", 1)[1] if ":" in st else w["reason"]) + ")", "WB", w["reason"])
        elif fin == "borrow/phrase":
            drop(c, "culture-bound or long tail: borrowing or phrase", "WB", w["reason"])
        elif fin == "tradition":
            drop(c, "culture-bound: the tradition's own word, borrowed", "WB; REL", w["reason"])
        continue
    if st.startswith("covered:"):
        ph = st.split(":", 1)[1]
        s = syll(ph)
        RULED = {"son": "gender is a modifier", "daughter": "gender is a modifier", "queen": "gender is a modifier",
                 "bride": "gender is a modifier", "young man": "gender is a modifier", "old man": "gender is a modifier",
                 "prince": "kinship composed + gender modifier", "princess": "kinship composed + gender modifier",
                 "grandchild": "kinship composed (method 3.1)", "spring (season)": "seasons: to the sets pass (author 2026-10-16)",
                 "winter": "seasons: to the sets pass", "summer": "seasons: to the sets pass",
                 "pink": "colours: to the sets pass", "organism": "world compound 'living thing' (coverage-02 r2 calibration)"}
        if c in RETRO and RETRO[c][0] == "root":
            rk = rank_of(c)
            add(RETRO_GLOSS.get(c, c), "root", "", RETRO_FIELD[c], tier_of(rk) or int(r["tier"] or 1), "PL-retro; LAD",
                f"was the phrase {ph}: {RETRO[c][1]}", rank=rk, key=c)
            continue
        if c in RETRO:
            drop(c, f"phrase: {ph} ({RETRO[c][1]}; meets the phrase line as the world's compound)", "LAD; PL-retro", r["note"])
            continue
        if s <= 3:
            flag = ""
        elif c in RULED:
            flag = f" ({s} syll; kept by a decided rule: {RULED[c]})"
        else:
            if c not in ("relative", "parent"):  # both became roots later (SUPERSEDED below)
                raise SystemExit("ladder phrase over the line with no decision: " + c)
            flag = f" ({s} syll)"
        drop(c, f"phrase: {ph}{flag}", "LAD", r["note"])
        continue
    if st.startswith("merge:"):
        drop(c, "covered by " + st.split(":", 1)[1] + " (merged)", "LAD", r["note"])
        continue
    if st == "grammar":
        drop(c, "grammar or construction", "LAD", r["note"])
        continue
    base = re.sub(r"\s*\(.*\)$", "", c)
    if c in RELIGION_TRADITION or route == "borrow":
        drop(c, "culture-bound: the tradition's own word, borrowed", "REL", "religion decisions 2026-10-13 (b); ladder row never updated (coverage-02 drops.tsv)")
        continue
    if route == "phrase":  # idol
        drop(c, "phrase: statue + holy ('a sacred image'); 'idol' frames others' images", "REL", r["note"])
        continue
    if c in DROP_TITLES:
        drop(c, "culture-bound: military or political title, borrowed (long tail)", "DROP")
        continue
    if c in MIL_RANKS:
        drop(GLOSS.get(c, c), "culture-bound: military rank, borrowed (long tail)", "DROP",
             "author 2026-10-16: military ranks dropped, general included; civic offices (mayor, governor, minister) kept")
        continue
    if c in DROP_SPECIALIST:
        drop(c, "long tail: specialist term (loan or built word)", "DROP")
        continue
    if c in MIXED:
        drop(c, "dropped: no sense passes alone (mixed senses re-checked)", "DROP", MIXED[c] + " (sense readings added)")
        continue
    if c in PHRASE_LINE_ITEMS and PHRASE_LINE_ITEMS[c][0] == "phrase":
        drop(c, "phrase: " + PHRASE_LINE_ITEMS[c][1], "DROP; PL")
        continue
    if c in BAL_PHRASE_OVERRIDES:
        drop(c, BAL_PHRASE_OVERRIDES[c][0], "BAL", BAL_PHRASE_OVERRIDES[c][1])
        continue
    rk = rank_of(c)
    tier = tier_of(rk) or int(r["tier"] or 1)
    if w:
        tier = max(tier, 2)  # first words weigh at least tier 2 (part4/placement.py)
    src = "LAD" + ("; WB" if w else "")
    note = ""
    field = ladder_field(r)
    gloss = GLOSS.get(c) or c
    if st == "split" and route == "root":
        sense1 = re.match(r"1: ([^;]*)", r["note"])
        gloss = GLOSS.get(c) or (f"{c} ({sense1.group(1)})" if sense1 else c)
    if route == "loan?":
        L = loans[c]
        v = L["verdict"]
        if c in PL_LOANS:
            add(gloss, "root", "", field, tier, "LAD; LOAN; ADD1", PL_LOANS[c], rank=rk, key=c)
        elif c == "tea":
            add("tea", "root", "", field, tier, "LAD; LOAN; ADD1", "loan tayu fails once adapted (author 2026-10-15): invented root", rank=rk, key=c)
        elif v.startswith("pass"):
            add(gloss, "loan", L["adapted"], field, tier, src + "; LOAN", f"panel {L['count/regions']}; form fixed", rank=rk, key=c)
        elif v == "fail":
            add(gloss, "root", "", field, tier, src + "; LOAN", f"loan failed the panel ({L['count/regions']}): native root", rank=rk, key=c)
        elif v == "tradition":
            drop(c, "culture-bound: the tradition's own word, borrowed", "REL; LOAN", f"{L['adapted']} as a borrowing")
        elif v == "not core":
            drop(c, "culture-bound: outside the metric standard, borrowed by those who use it", "LOAN", L["note"])
        elif v.startswith("loan as a currency"):
            add("pound (the currency)", "loan", L["adapted"], "loan", tier, "LOAN", "a currency only; the weight is not core", rank=rk, key=c)
        else:
            raise SystemExit("unhandled loan verdict " + v)
        continue
    if route == "standard":
        add(gloss, "loan candidate", "", field, tier, src + "; LOAN-pending",
            "pending: loan panel (author 2026-10-16); ladder 2 rung 1 gave the standard's form; if it fails, a root or a phrase", rank=rk, key=c)
        continue
    if c in PHRASE_LINE_ITEMS:
        note = PHRASE_LINE_ITEMS[c][1] + " (re-checked 2026-10-16)"
        src += "; DROP; PL"
    if r["antonym"]:
        note = note
    add(gloss, "root", "", field, tier, src, note, rank=rk, key=c)
    concepts[c.lower()]["_ant"] = r["antonym"]

# religion: gloss widenings are in GLOSS; holy person etc. stay roots (REL)
for k in ("temple", "priest", "saint", "miracle", "devil", "heaven", "hell", "sin", "bless", "curse", "soul",
          "spirit", "pray", "believe", "sacrifice", "religion"):
    if k in concepts:
        concepts[k]["source"] += "; REL"

# ===================================================== 3. coverage-01 additions.tsv
ADD1 = {  # concept -> (gloss, field, note/decision); all roots unless noted
    "moon": ("moon", "nature", "split from dunan (author 2026-10-13)"),
    "ghost": ("ghost", "abstract", "split from spirit (author 2026-10-13)"),
    "word": ("word", "sense", "split from apu (author 2026-10-13)"),
    "keep": ("keep, retain", "action", "split from kuwi (author 2026-10-13)"),
    "request": ("request, ask for", "sense", "split from mido (author 2026-10-13)"),
    "lose (a contest)": ("lose (a contest)", "action", "split from agi (author 2026-10-13)"),
    "daytime": ("daytime", "time", "split from dili (author 2026-10-13)"),
    "rule": ("rule", "abstract", "split from wabun (author 2026-10-13)"),
    "percent": ("percent", "number", "author 2026-10-13, audit item 4"),
    "always": ("always", "time", "inventory 2 (author 2026-10-13)"),
    "often": ("often", "time", "inventory 2"), "sometimes": ("sometimes", "time", "inventory 2"),
    "never": ("never", "time", "inventory 2"), "later": ("later", "time", "inventory 2"),
    "police": None,  # handled as a failed loan in step 1
    "here": ("here", "space", "grid check (author 2026-10-15)"), "there": ("there", "space", "grid check (author 2026-10-15)"),
    "tea": None,  # handled in the ladder step
    "sofa": "skip", "chemistry": None,
    "parent": ("parent", "people", "sex-neutral root (author 2026-10-16)"),
    "lie (tell an untruth)": None,  # = ladder 884.b lie (untruth)
    "lunch": ("lunch", "thing", "three meals as roots (author 2026-10-16)"),
    "dinner": ("dinner", "thing", "three meals as roots (author 2026-10-16)"),
    "cassava": ("cassava", "nature", "WOLD follow-up (author 2026-10-16)"),
    "millet, sorghum": ("millet, sorghum", "nature", "WOLD follow-up (author 2026-10-16)"),
    "blind": None, "deaf": ("deaf", "body", "set with blind and mute (author 2026-10-16)"),
    "mute": ("mute, unable to speak", "body", "set with blind and deaf (author 2026-10-16)"),
    "order, command": ("order, command (someone to do something)", "sense", "WOLD follow-up (author 2026-10-16); with ti"),
    "relative": ("relative, family member", "people", "phrase ewo pi yonyo is 5 syll (author 2026-10-16)"),
    "spider": None,  # on the ladder already
    "shave": ("shave", "action", "WOLD follow-up (author 2026-10-16)"),
    "fish (to catch fish)": ("fish (catch fish)", "action", "WOLD follow-up (author 2026-10-16)"),
    "herd (to tend animals)": ("herd, tend animals", "action", "WOLD follow-up (author 2026-10-16)"),
}
for r in tsv("tests/coverage-01/part3/additions.tsv"):
    c = r["concept"]
    spec = ADD1[c]
    if spec is None:
        for k in (c, "lie (untruth)" if c.startswith("lie") else c):
            if k in concepts:
                concepts[k]["source"] += "; ADD1"
        continue
    if spec == "skip":
        e = next(e for e in excluded if e["concept"] == "sofa")
        e["reason"] = "culture-bound: borrowed (author 2026-10-16: sofa stays borrowed)"
        e["source"] += "; ADD1"
        e["note"] += "; the loan also fails 5-of-7 (2026-10-15)"
        continue
    g, f, d = spec
    rk = rank_of(c.split(",")[0].split(" (")[0])
    add(g, "root", "", f, tier_of(rk) or 2, "ADD1", d, rank=rk, key=c)
concepts["blind"]["source"] += "; ADD1 (set with deaf, mute)"
concepts["spider"]["source"] += "; ADD1 (own root, 2026-10-16)"
concepts["spider"]["concept"] = "spider"
for k in SUBJECTS:
    if k in concepts:
        concepts[k]["source"] += "; SUBJ"
    else:  # biology was on no list
        rk = rank_of(k)
        add(k, "root", "", "abstract", tier_of(rk) or 1, "SUBJ", "school subject every system teaches (author 2026-10-16)", rank=rk, key=k)
if "parent" in concepts:
    pass
# remove the ladder's parent "covered" exclusion is fine: the excluded row records the old phrase

# ===================================================== 4. balance-02 entrants (51) + boundaries 2026-10-16
BAL = {  # concept -> (route, gloss, field, note)
    "fact": ("root", "fact", "abstract", ""),
    "common": ("root", "common, ordinary, usual", "quality", "split: 'shared' is the phrase pi we"),
    "accept": ("root", "accept, take what is offered", "action", ""),
    "fate": ("root", "fate, destiny", "abstract", ""),
    "influence": ("root", "influence", "action", ""),
    "holy": ("root", "holy, sacred", "quality", "root (author 2026-10-15); merged rank 588"),
    "status": ("root", "status, standing, rank in a group", "people", ""),
    "avoid": ("root", "avoid", "action", ""),
    "suitable": ("root", "suitable, fit, proper", "quality", "absorbs fit"),
    "guess": ("root", "guess", "mind", ""),
    "partner": ("root", "partner (neutral in sex and setting)", "people", ""),
    "environment": ("root", "environment, surroundings", "nature", "separate from nature"),
    "disappear": ("root", "disappear, vanish", "motion", ""),
    "destroy": ("root", "destroy", "action", "separate from alun 'break'"),
    "explode": ("root", "explode, burst", "action", ""),
    "accuse": ("root", "accuse, blame, hold responsible", "sense", "accuse and blame one root"),
    "thread": ("root", "thread", "thing", ""),
    "waste": ("root", "waste (use up for nothing)", "action", ""),
    "forgive": ("root", "forgive", "mind", ""),
    "load": ("root", "load, burden", "thing", "absorbs burden"),
    "heap": ("root", "heap, pile", "thing", "phrase musu fanmu (4 syll) over the line (coverage-02 r2)"),
    "warm": ("root", "warm", "quality", "separate from tikun 'hot'"),
    "disaster": ("root", "disaster", "abstract", ""),
    "unique": ("root", "unique", "quality", "phrase-or-root decided: root (author 2026-10-16)"),
    "celebrate": ("root", "celebrate, celebration", "action", "festival = 'time of celebrating'"),
    "include": ("root", "include, contain", "action", "include and contain one root"),
    "exceed": ("root", "exceed, go beyond", "action", "phrase-or-root decided: root (author 2026-10-16)"),
    "decrease": ("root", "decrease, become or make less", "action", ""),
    "statue": ("root", "statue", "thing", ""),
    "participate": ("root", "participate, take part", "action", "phrase-or-root decided: root (author 2026-10-16)"),
    "characteristic": ("root", "characteristic, feature, trait", "abstract", ""),
    "obey": ("root", "obey", "action", ""),
    "familiar": ("root", "familiar, known", "quality", "phrase-or-root decided: root (author 2026-10-16)"),
    "earthquake": ("phrase", "phrase: fowo susin 'ground shake' (the world's compound)", None, ""),
    "heal": ("root", "heal, cure", "action", "absorbs cure"),
    "hate": ("root", "hate", "mind", ""),
    "attend": ("phrase", "phrase: 'go to' (isi tun)", None, ""),
    "cruel": ("root", "cruel", "quality", ""),
    "chain": ("root", "chain", "thing", ""),
    "bell": ("root", "bell", "thing", ""),
    "kindness": ("root", "kind, kindness", "quality", ""),
    "nonsense": ("root", "nonsense", "sense", "phrase apu su yofu (5 syll) over the line (coverage-02 r2)"),
    "obstacle": ("root", "obstacle", "thing", "phrase musu gi bamo (5 syll) over the line (coverage-02 r2)"),
    "fraud": ("root", "fraud, cheating", "action", ""),
    "achieve": ("root", "achieve", "action", "separate from wonku 'reach'"),
    "summary": ("root", "summary", "sense", "phrase-or-root decided: root (author 2026-10-16)"),
    "endure": ("root", "endure, bear, tolerate", "mind", ""),
    "substitute": ("root", "substitute, replacement", "action", ""),
    "shelter": ("phrase", "phrase: pu kuwi 'place that protects'", None, ""),
    "contain": ("merge", "covered by include (include and contain one root)", None, ""),
    "blame": ("merge", "covered by accuse (accuse and blame one root)", None, ""),
}
ents = tsv("tests/balance-02/concepts-entrants.tsv")
for r in ents:
    c, j = r["canonical"], r["judgement"]
    rk = int(r["canon_rank_fixed"])
    if j == "missing":
        route, g, f, note = BAL[c]
        if route == "root":
            add(g, "root", "", f, tier_of(rk), "BAL", note, rank=rk, key=c)
        else:
            drop(c, g, "BAL", "boundaries for the 51 additions (author 2026-10-16)")
    elif j == "covered":
        drop(c, "covered by " + r["note (added: Claude's reading)"].split(" (")[0].split(";")[0], "BAL", "balance-02 entrant judgement")
    elif j == "composes":
        ph = r["note (added: Claude's reading)"]
        core = re.split(r" \(|;", ph)[0].strip()
        s = syll(core)
        if c in RETRO:
            if RETRO[c][0] == "root":
                add(RETRO_GLOSS.get(c, c), "root", "", RETRO_FIELD[c], tier_of(rk), "PL-retro; BAL",
                    f"was the phrase {ph}: {RETRO[c][1]}", rank=rk, key=c)
            else:
                drop(c, f"phrase: {ph} ({RETRO[c][1]})", "BAL; PL-retro")
            continue
        if c in ("decade", "cooperate"):
            tail = f"world compound (coverage-02 r2 calibration); meets the phrase line"
        elif s <= 3:
            tail = f"{s} syll; meets the phrase line"
        else:
            raise SystemExit("entrant phrase over the line with no decision: " + c)
        drop(c, f"phrase: {ph} ({tail})", "BAL", "balance-02 entrant judged 'composes'")
    elif j == "artefact":
        drop(c, "artefact: pooled English label (" + r["note (added: Claude's reading)"] + ")", "BAL")
    elif j == "list":
        pass  # already on the list
drop("common (shared)", "phrase: pi we 'of all'", "BAL", "common split (author 2026-10-16)")
if "holy" in concepts:
    concepts["holy"]["source"] += "; REL (sacred = holy)"

# ===================================================== 5. the walk (coverage-02 round 2)
WALK_G = {  # rank<=1342 G (17), glosses from walk-r2 with the 2026-10-16 boundary calls
    "ancestor": ("ancestor", "people", ""),
    "coal": ("coal (fuel)", "nature", "one root; charcoal is wood + coal"),
    "wild": ("wild, not tamed or farmed", "quality", "without the 'savage' judgement (C4)"),
    "cave": ("cave", "nature", ""),
    "inherit (inheritance)": ("inherit, inheritance", "action", ""),
    "comfortable": ("comfortable, at ease", "quality", "separate from pleasant"),
    "depend (dependence)": ("depend (on), be conditional on", "abstract", "separate from gewan 'trust, rely on'"),
    "deny": ("deny, say it isn't true", "sense", "separate from refuse"),
    "pattern": ("pattern, repeated design", "abstract", ""),
    "revenge": ("revenge", "action", ""),
    "discrimination": ("discrimination, unfair treatment of a group", "people", ""),
    "attitude": ("attitude, stance", "mind", "opinion is a phrase"),
    "worthy": ("worthy, deserving", "quality", "covers merit"),
    "welfare": ("well-being, welfare", "abstract", "separate from health"),
    "infection": ("infection, infect", "body", "virus stays a loan"),
    "urgent": ("urgent", "quality", "an emergency in speech is yo yo"),
    "ceiling": ("ceiling", "thing", "separate from kuwun 'roof'"),
}
walk = tsv("tests/coverage-02/walk-r2.tsv")
CLASSNAME = {"P": "phrase", "A": "artefact: pooled English label", "N": "long tail: specialist or named",
             "C": "culture-bound", "L": "loan candidate"}
walk_rest = {}
for r in walk:
    k, c, cl = int(r["rank"]), r["concept"], r["class"]
    if cl == "-":
        continue
    if k <= 1342:
        if cl == "G":
            g, f, note = WALK_G[c]
            add(g, "root", "", f, tier_of(k), "WALK", note, rank=k, key=c)
        elif cl == "L":
            drop(c, "pending: loan panel (" + r["gloss_or_phrase"] + ")", "WALK", "stopping stretch; fallback " + r["note"])
        elif cl == "P":
            drop(c, "phrase: " + r["gloss_or_phrase"], "WALK", r["note"])
        else:
            drop(c, CLASSNAME[cl], "WALK", r["note"])
    else:
        walk_rest[c] = r

# ===================================================== 6. drops / re-checks already done in step 2

# ===================================================== 7. WOLD deep layer
wold = tsv("tests/deeplayer-01/pass.tsv")
W = {r["wold_id"]: r for r in wold}
WFIELD = {"The body": "body", "Animals": "animal", "Food and drink": "thing", "Agriculture and vegetation": "nature",
          "Clothing and grooming": "thing", "Motion": "motion", "The physical world": "nature",
          "Basic actions and technology": "action", "Speech and language": "sense", "Possession": "action",
          "Kinship": "people", "The house": "thing", "Emotions and values": "mind", "Spatial relations": "space",
          "Sense perception": "sense", "Cognition": "mind", "Social and political relations": "people",
          "Warfare and hunting": "thing", "Law": "abstract", "Modern world": "thing", "Quantity": "size",
          "Time": "time", "Religion and belief": "abstract", "Miscellaneous function words": "abstract"}
WFIX = {  # field by part of speech, where the WOLD field doesn't say (added)
    "4-521": "action", "4-78": "action", "4-854": "body", "4-92": "quality", "4-99": "quality",
    "1-775": "action", "5-23": "action", "5-46": "action", "5-47": "action", "5-54": "action", "8-31": "action",
    "6-33": "action", "6-35": "action", "18-17": "sense", "18-39": "sense", "11-54": "quality", "9-31": "action",
    "10-14": "action", "10-33": "motion", "10-34": "motion", "10-41": "motion", "4-215": "action",
    "11-61": "action", "11-62": "action", "10-15": "motion", "16-83": "quality", "4-94": "body",
    "15-712": "action", "6-31": "action", "18-19": "sense", "16-39": "sense", "9-46": "action",
    "9-461": "action", "9-72": "action", "9-81": "action", "8-21": "action", "4-751": "action", "5-19": "action",
    "2-75": "people", "4-856": "body", "1-324": "nature", "3-586": "animal", "3-831": "animal", "4-452": "body",
    "4-465": "body", "6-32": "thing", "20-26": "thing", "8-73": "nature", "8-81": "nature", "12-75": "thing",
    "9-25": "thing", "9-73": "nature", "9-5": "thing", "18-71": "thing", "18-72": "thing",  # nouns (round 2 fix, added)
}
SAME = {"2-77": "2-76", "6-72": "6-71", "8-531": "8-31", "8-931": "8-93", "9-75": "6-33", "10-451": "4-94"}
CODEX20 = ["1-324", "3-586", "3-831", "4-452", "4-856", "4-94", "6-31", "6-32", "8-73", "8-81", "9-46", "9-461",
           "9-72", "9-75", "9-81", "15-712", "16-39", "18-19", "20-26", "4-465"]
admitted = {}


def wold_add(wid, src, note=""):
    r = W[wid]
    rk = int(r["freq_rank"]) if r["freq_rank"].isdigit() else None
    g = r["gloss"]
    f = WFIX.get(wid) or WFIELD[r["field"]]
    nt = f"WOLD {wid}, {r['root_families']}/24 families with an own root" + (f"; {note}" if note else "")
    if wid == "4-856":
        g = "boil, abscess (on the skin)"
        nt += "; the log's 'boil (bubble)' is this meaning, not boiling (binla)"
    c = add(g, "root", "", f, tier_of(rk) or 1, src, nt, rank=rk, key="wold:" + wid)
    admitted[wid] = "wold:" + wid
    return c


for wid, r in W.items():
    if r["D_tier"] == "core":
        wold_add(wid, "WOLD-core")
for wid, r in W.items():
    if r["D_tier"] == "edge" and "alt:" not in r["note"]:
        wold_add(wid, "WOLD-edge")
for wid in CODEX20:
    if wid in SAME:
        concepts[admitted[SAME[wid]]]["source"] += "; WOLD-codex (" + wid + ", same root)"
        admitted[wid] = admitted[SAME[wid]]
        continue
    if wid in admitted:
        concepts[admitted[wid]]["source"] += "; WOLD-codex"
    else:
        wold_add(wid, "WOLD-codex")
for wid, tgt in SAME.items():
    if tgt in admitted and wid not in admitted:
        concepts[admitted[tgt]]["note"] += f"; also WOLD {wid} ({W[wid]['meaning']})"
        admitted[wid] = admitted[tgt]

# WOLD phrases that later roots shortened or covered (round 2, added)
P_LATER = {"5-45": "covered by dinner (the evening meal; three meals as roots, author 2026-10-16)",
           "3-18": "phrase: no [herd] 'one who herds' (3 syll; herd became a root, author 2026-10-16)"}

# roast/fry splits into two roots (author 2026-10-16): the lump was WOLD's combined item (3% of families lump without copies)
rf = concepts["wold:5-23"]
rf["concept"] = "roast (cook over a fire or in dry heat)"
rf["source"] += "; BQ02 (split)"
rf["note"] += "; roast/fry split (author 2026-10-16, deeplayer-02: ROAST/FRY 3.0% without copies)"
add("fry (cook in hot oil or fat)", "root", "", "action", rf["tier"], "WOLD-core; BQ02 (split)",
    "split from WOLD 5-23 'roast or fry' (author 2026-10-16); the frying pan is du [fry]", rank=rf["rank"] or None, key="wold:5-23-fry")

# deeplayer-02 boundary questions, as decided (author 2026-10-16: 16 of 17 split; claw joins tolin;
# the button takes both buttons, tinli stays "key"; turn-off stays with tapi; to milk and dare two roots)
BQ_DECIDED = {"19-45": "order, command"}
BQ_GLOSS = {  # the root gloss, where the decision widened or narrowed bq.tsv's
    "6-62": "button (on clothes; also a push-button)",
    "1-861": "put out, extinguish (a fire)",
    "9-211": "pound (in a mortar)",
    "5-87": "milk (an animal)",
}
BQ_NOTE = {"6-62": "takes both buttons; tinli stays 'key' (author 2026-10-16, option a)",
           "1-861": "'turn off (a device)' stays with tapi (author 2026-10-16, option b)",
           "5-87": "two roots by rung 4 (author 2026-10-16, option a); donbo tunlo is 4 syll",
           "9-211": "boundary with monpa 'crush' not measured (deeplayer-02 tested only payon 'hit'): open question"}
BQ_FIELD = {"1-37": "space", "1-861": "action", "3-585": "animal", "4-68": "body", "5-24": "action", "5-48": "action",
            "5-87": "action", "6-62": "thing", "7-26": "thing", "9-211": "action", "9-77": "thing", "10-17": "action",
            "10-53": "motion", "16-51": "mind", "21-42": "action"}  # (added)
deep02 = {r["wold_id"]: r for r in tsv("tests/deeplayer-02/bq.tsv")}
for wid, b in deep02.items():
    if wid in BQ_DECIDED:
        continue
    r = W[wid]
    if b["result"] == "two roots":
        g = BQ_GLOSS.get(wid, b["new_root_gloss"])
        head = re.split(r"[,(]", g)[0].strip()
        rk = rank_of(head) or (int(r["freq_rank"]) if r["freq_rank"].isdigit() else None)
        nt = f"WOLD {wid}; rung 4: {b['concepticon_pair']} {b['rate_no_copies']}% lump" + (f"; {BQ_NOTE[wid]}" if wid in BQ_NOTE else "")
        add(g, "root", "", BQ_FIELD[wid], tier_of(rk) or 1, "BQ02", nt, rank=rk, key="wold:" + wid)
    else:  # claw
        drop(f"{r['gloss']} (WOLD {wid})", "covered by tolin 'nail, claw' (one root by rung 4)", "BQ02",
             f"{b['concepticon_pair']} {b['rate_no_copies']}% lump, near 50 (author 2026-10-16)")
    admitted[wid] = "wold:" + wid

# deeplayer-02 loans, as decided (author 2026-10-16)
loans02 = {r["concept"]: r for r in tsv("tests/deeplayer-02/loans.tsv")}
L02 = {  # wold_id -> loans.tsv concept, root gloss and field (added)
    "3-662": ("dolphin", None), "3-47": ("mule", None), "3-592": ("parrot", "animal"), "3-78": ("camel", None),
    "3-816": ("cockroach", "animal"), "5-28": ("frying pan", None), "5-82": ("pepper", "thing"),
    "6-24": ("cotton", "nature"), "6-25": ("silk", None), "6-79": ("tattoo", None), "7-46": ("candle", "thing"),
    "8-68": ("tobacco", None), "8-82": ("coconut", None), "20-33": ("helmet", None), "23-23": ("injection", None),
    "23-53": ("mattress", "thing"), "23-54": ("tin can", None), "23-61": ("calendar", None),
}
L02GLOSS = {"pepper": "pepper (the spice)", "cotton": "cotton (plant and cloth)", "calendar": "calendar (the object)"}
for wid, (lc, fld) in L02.items():
    L, r = loans02[lc], W[wid]
    rk = rank_of(lc) or (int(r["freq_rank"]) if r["freq_rank"].isdigit() else None)
    d = L["decision"]
    if d == "loan":
        add(L02GLOSS.get(lc, lc), "loan", L["adapted"], "loan", tier_of(rk) or 1, "LOAN02",
            f"WOLD {wid}; panel {L['count']} / {L['regions']}; form fixed", rank=rk, key="wold:" + wid)
    elif d.startswith("root"):
        add(L02GLOSS.get(lc, lc), "root", "", fld, tier_of(rk) or 1, "LOAN02",
            f"WOLD {wid}; loan failed ({L['count']} / {L['regions']}): {d.split(':', 1)[1].strip()}", rank=rk, key="wold:" + wid)
    elif d.startswith("phrase"):
        drop(f"{lc} (WOLD {wid})", d, "LOAN02", f"loan failed {L['count']} / {L['regions']} (author 2026-10-16)")
    else:  # camel
        drop(f"{lc} (WOLD {wid})", "culture-bound: a regional animal, borrowed from its users' word", "LOAN02",
             f"loan failed {L['count']}; {d}")
    admitted[wid] = "wold:" + wid
for wid, r in W.items():
    if wid in admitted or r["class"] == "cov":
        continue
    cl = r["class"]
    label = f"{r['gloss'] or r['meaning']} (WOLD {wid})"
    if cl == "D":
        drop(label, "phrase or long tail: WOLD edge with an alternative (" + re.sub(r'.*alt:', 'alt:', r["note"])[:80] + ")",
             "WOLD-edge", "author 2026-10-16 option (b): the 33 edge items with an alternative stay out")
    elif cl == "BQ":
        if wid in BQ_DECIDED:
            continue
        b = deep02.get(wid)
        prop = f"proposed {b['result']}" + (f": {b['new_root_gloss']}" if b and b["result"] == "two roots" else "") if b else "not run"
        drop(label, f"pending: boundary question, deeplayer-02 unfinished ({prop})", "WOLD", "covered today by " + r["covered_by_or_phrase"])
    elif cl == "L":
        drop(label, "pending: loan panel, deeplayer-02 unfinished", "WOLD", r["note"][:120])
    elif cl == "P" and wid in P_LATER:
        drop(label, P_LATER[wid], "WOLD", "round 2 (added): " + r["covered_by_or_phrase"])
    elif cl == "P":
        drop(label, "phrase: " + r["covered_by_or_phrase"], "WOLD", r["note"][:120])
    elif cl == "C":
        drop(label, "culture-bound", "WOLD", r["note"][:120])
    elif cl == "X":
        drop(label, "long tail: too specific or specialist", "WOLD", r["note"][:120])
concepts["order, command"]["source"] += "; WOLD 19-45 BQ (decided: a root)"

# ===================================================== 8. the 47 walk-only WOLD meanings (added classification)
W47 = {  # wold_id -> (verdict, concept-or-reason)
    "1-28": ("covered", "cave (WALK G)"), "1-34": ("out", "long tail: bay, gulf (9/24 families; not a basic action, body part or household thing)"),
    "1-45": ("covered", "earthquake phrase (BAL)"), "1-841": ("covered", "coal (WALK G; embers = live coals)"),
    "1-89": ("covered", "coal (WALK G; charcoal = wood + coal)"), "1-831": ("root", "steam"),
    "2-56": ("covered", "ancestor (WALK G)"), "4-86": ("covered", "heal (BAL)"), "5-181": ("root", "swallow (food, drink)"),
    "5-43": ("covered", "lunch (ADD1, author 2026-10-16)"), "5-55": ("root", "flour"),
    "5-712": ("covered", "funti 'group' (bunch; 2 syll)"), "6-38": ("covered", "thread (BAL)"),
    "7-14": ("out", "long tail: tent (8/24 families; not in most households)"),
    "8-41": ("root", "harvest"), "9-14": ("root", "bend"), "9-15": ("root", "fold"), "9-18": ("covered", "chain (BAL)"),
    "9-83": ("covered", "statue (BAL)"), "9-32": ("root", "stretch"), "9-341": ("root", "hang, hang up"),
    "10-473": ("covered", "descend (PL-retro, author 2026-10-16)"),
    "10-92": ("covered", "descend, go down; land (PL-retro)"),
    "10-491": ("covered", "disappear (BAL)"), "11-27": ("covered", "destroy (BAL)"), "12-213": ("covered", "heap (BAL)"),
    "14-252": ("out", "phrase: piyi 'stay' / le (to last; 8/24 families; the WOLD match to endure was a different sense)"),
    "15-56": ("covered", "wino 'light' as a verb (shine; 2 syll)"), "15-851": ("covered", "warm (BAL)"),
    "16-35": ("out", "pending: sets pass (emotions; author 2026-10-16) - pity, mercy (9/24 families)"),
    "16-41": ("covered", "hate (BAL)"),
    "16-44": ("out", "pending: sets pass (emotions; author 2026-10-16: envy/jealousy) (12/24 families)"),
    "16-65": ("out", "long tail: loyal, faithful (5/24 families)"), "16-68": ("covered", "fraud (BAL) / trick (LAD)"),
    "16-69": ("covered", "forgive (BAL)"), "16-78": ("covered", "accuse/blame (BAL)"), "17-171": ("covered", "guess (BAL)"),
    "17-23": ("root", "mad, crazy"), "18-34": ("covered", "deny (WALK G)"),
    "18-37": ("root", "refuse, say no to"), "19-46": ("covered", "obey (BAL)"),
    "19-55": ("root", "stranger, a person one does not know"),
    "20-46": ("out", "phrase: neke nen 'give oneself' (3 syll) / bamo migi (surrender)"),
    "21-31": ("covered", "accuse (BAL)"), "21-35": ("out", "phrase or long tail: guilty (3/24 families; ibe [fault])"),
    "22-19": ("covered", "holy (BAL)"), "22-47": ("out", "phrase: [sign] (omen; 2 syll)"),
}
W47FIELD = {"1-831": "nature", "5-181": "action", "5-55": "thing", "8-41": "action", "9-14": "action", "9-15": "action",
            "9-32": "action", "9-341": "action", "17-23": "mind", "18-37": "sense", "19-55": "people"}
W47NOTE = {"8-41": "every farming household; named in the 2026-10-16 'everyone's modern life' entry; confirmed a root (author 2026-10-16)",
           "18-37": "the author separated deny and refuse; confirmed a root (author 2026-10-16)",
           "19-55": "'ewo su lugo' is 5 syll; SSA gap (balance-02); confirmed a root (author 2026-10-16)",
           "9-32": "basic action, no short phrase"}
assert len(W47) == 47, len(W47)
for wid, (v, x) in W47.items():
    r = W[wid]
    if v == "root":
        rk = None
        wr = walk_rest.get(x.split(",")[0]) or walk_rest.get({"17-23": "crazy", "18-37": "refuse (refusal)",
                                                               "9-341": "hang", "5-181": "swallow"}.get(wid, ""))
        if wr:
            rk = int(wr["rank"])
        add(x, "root", "", W47FIELD[wid], tier_of(rk) or 1, "WOLD-47",
            f"WOLD {wid}, {r['root_families']}/24 families" + (f"; {W47NOTE[wid]}" if wid in W47NOTE else ""), rank=rk, key="wold:" + wid)
    elif v == "out":
        drop(f"{r['meaning']} (WOLD {wid})", x, "WOLD-47")
    # covered: nothing to add

# walk rows past the stop that no other route admitted
w47roots = {"steam", "swallow", "flour", "harvest", "bend", "fold", "stretch", "hang", "crazy", "refuse (refusal)", "stranger"}
for c, r in walk_rest.items():
    if c in w47roots:
        continue
    cl = r["class"]
    why = {"G": "past the stop (walk stopped at rank 1342 under both raters)"}.get(cl) or CLASSNAME[cl] + " (past the stop)"
    drop(c, why, "WALK", r["gloss_or_phrase"][:90])
# calibration stretch (today's list), round-2 G not on the list: the composes entrants are recorded in step 4

# ===================================================== 9. the 14 day/month names etc. are recorded in step 2 (grammar)
# ===================================================== 10. pending items outside the files
drop("yebin 'call, phone or call to' (against liga 'phone')", "pending: ladder 1 with the concept list (author 2026-10-15, judge's repairs)", "LEX",
     "stays a root meanwhile; tinli's half was settled by the button split (author 2026-10-16)")
drop("spelling-alphabet words (alufa, saluli ...)", "outside the core: spelling alphabet, like units (author 2026-10-15)", "-", "not placed")
drop("@ and the dot", "covered by mon 'at' and mimi 'point' (author 2026-10-15)", "-", "")

# ===================================================== duplicates found by the checks (added)
remove("defeat", "covered by lose (a contest): the same sense (the ladder's own note reads 'lose a contest'); "
       "duplicate found by the sense check (added)", "LAD; check")

# excluded rows that a later decision superseded: keep the record, say so
SUPERSEDED = {"relative": "relative, family member", "parent": "parent", "deaf (WOLD 4-95)": "deaf",
              "mute (WOLD 4-96)": "mute, unable to speak", "dinner (WOLD 5-44)": "dinner", "lunch": "lunch",
              "cassava, manioc (WOLD 8-92)": "cassava", "millet, sorghum (WOLD 8-911)": "millet, sorghum"}
for e in excluded:
    if e["concept"] in SUPERSEDED:
        e["note"] = ("was: " + e["reason"] + ". " + e["note"]).strip()
        e["reason"] = "superseded: now the root '" + SUPERSEDED[e["concept"]] + "' (see concepts.tsv)"

# ===================================================== antonyms
pairs = []
for a, b in (l.rstrip("\n").split("\t") for l in open(P("data/antonyms.tsv")) if "\t" in l):
    if a == "concept" or not a:
        continue
    pairs.append((a, b, "antonyms.tsv"))
for k, c in list(concepts.items()):
    if c.get("_ant"):
        pairs.append((k, c["_ant"], "ladder"))
ADDED_PAIRS = [("accept, take what is offered", "refuse, say no to"), ("hate", "love"), ("decrease, become or make less", "increase"),
               ("wold:10-33", "wold:10-34"), ("wold:11-61", "wold:11-62"), ("lose (a contest)", "win"), ("daytime", "night"),
               ("here", "there"), ("always", "never"), ("bless, blessing", "curse"), ("heaven, paradise", "hell"),
               ("appear", "disappear, vanish"), ("comfortable, at ease", "pleasant"), ("keep, retain", "lose, misplace"),
               ("descend", "rise")]
ADDED_PAIRS = [p for p in ADDED_PAIRS if p != (("comfortable, at ease", "pleasant"))]
DECIDED_PAIRS = {("lose (a contest)", "win")}  # additions.tsv: antonym of yiyin "win" (author 2026-10-13)


def find(label):
    l = label.lower()
    if l in concepts:
        return concepts[l]
    for c in concepts.values():
        if c["concept"].lower() == l:
            return c
    base = l.split(",")[0].split(" (")[0]
    hits = [c for c in concepts.values() if c["concept"].lower().split(",")[0].split(" (")[0] == base]
    return hits[0] if len(hits) == 1 else None


unmatched = []
for a, b, src in pairs + [(a, b, "decided" if (a, b) in DECIDED_PAIRS else "added") for a, b in ADDED_PAIRS]:
    if re.match(r"^[\d^.\-]+$|senary|^10\^", a) or re.match(r"^[\d^.\-]+$|senary|^10\^", b):
        continue  # number confusion pairs (and senary), not antonyms
    A, B = find(a), find(b)
    if not A or not B:
        unmatched.append((a, b, src))
        continue
    tag = "" if src in ("antonyms.tsv", "ladder") else f" ({src})"
    for X, Y in ((A, B), (B, A)):
        ent = Y["concept"] + tag
        if ent.split(" (added)")[0] not in [e.split(" (added)")[0] for e in X["antonym"].split("; ") if e]:
            X["antonym"] = (X["antonym"] + "; " + ent).strip("; ")

# ===================================================== write
cols = ["concept", "route", "form", "field", "tier", "rank", "antonym", "source", "note"]
with open(os.path.join(HERE, "concepts.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(cols)
    for c in concepts.values():
        if c["route"] in ("loan", "kept loan"):
            c["field"] = "loan"  # the lexicon files every loan under "loan"
        c["source"] = "; ".join(dict.fromkeys(c["source"].split("; ")))  # one mention per tag
        w.writerow([str(c[k]).replace(chr(34), chr(39)) for k in cols])
with open(os.path.join(HERE, "excluded.tsv"), "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["concept", "reason", "source", "note"])
    for e in excluded:
        w.writerow([str(e[k]).replace(chr(34), chr(39)) for k in ("concept", "reason", "source", "note")])

# ===================================================== report
cnt = collections.Counter(c["route"] for c in concepts.values())
print("concepts", len(concepts), dict(cnt))
print("excluded", len(excluded))
first = collections.Counter(c["source"].split(";")[0].strip() for c in concepts.values())
print("by first source", dict(first))
print("unmatched antonym pairs", unmatched)

"""Offensive-word filter (2026-10-09, requested by the user).

Checks this language's words against offensive and taboo words of the world's most spoken languages,
so no word sounds like a slur, a curse or a taboo word somewhere.

  python offensive.py fetch      # stream Wiktionary data (kaikki.org) -> data/offensive.tsv
  python offensive.py check      # list our words that match, for review

Source: Wiktionary entries tagged vulgar, offensive, slur or derogatory, or filed under a taboo topic
(sex, genitalia, excrement, urine, death), via kaikki.org's per-language extracts. Each foreign
word's pronunciation is mapped into this language's sounds with names.py's mapping (no added vowels),
then compared with every word we have. blocked(form) is what words.py uses to skip a form.
"""
import csv, gzip, io, json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")
OUT = os.path.join(DATA, "offensive.tsv")
LANGS = ["English", "Chinese", "Hindi", "Spanish", "French", "Arabic", "Egyptian Arabic", "Bengali", "Portuguese",
         "Russian", "Urdu", "Indonesian", "German", "Japanese", "Marathi", "Telugu", "Turkish", "Tamil", "Vietnamese",
         "Tagalog", "Korean", "Persian", "Hausa", "Swahili", "Javanese", "Italian", "Punjabi", "Gujarati", "Thai",
         "Polish", "Yoruba", "Ukrainian", "Malay", "Amharic"]
STRONG = {"vulgar", "offensive", "slur", "ethnic"}
MILD = {"derogatory", "pejorative"}
TOPICS = {"Sex", "Sexuality", "Genitalia", "Prostitution", "Feces", "Excrement", "Urine", "Death"}
TOPIC_GLOSS = re.compile(r"^(?:to )?(?:corpse|death|dead|die|feces|faeces|excrement|shit|urine|urinate|piss|penis|vagina|vulva|"
                         r"anus|testicles?|semen|sexual intercourse|copulate|have sex|menstruation|genitals?)\b", re.I)
UA = {"User-Agent": "conlang-thought-experiment/0.1 (offensive-word screen; local use)"}

# --- pronunciation -> this language's sounds (names.py's mapping, tolerant, no added vowels) ----------
import names as N


def segs(ipa):
    ipa = re.sub(r"[/\[\]()‿͜͡]", "", ipa.split(",")[0]).strip().replace("ɡ", "g")
    out, i = "", 0
    while i < len(ipa):
        two = ipa[i:i + 2]
        if two in N.AFFRICATES:
            out += N.AFFRICATES[two]; i += 2; continue
        ch = ipa[i]
        if ch in N.VOWELS:
            out += N.VOWELS[ch]
        elif ch in N.CONS:
            out += N.CONS[ch]
        elif ch == " ":
            out += " "
        i += 1
    out = re.sub(r"([aeiou])\1+", r"\1", out)
    return out.strip()


def key(s):
    """Merge the contrasts a listener from another language most easily misses (voicing, e/i, o/u)."""
    return s.translate(str.maketrans("bdgeo", "ptkiu"))


# --- fetch ----------------------------------------------------------------------------------------------
def primary(entry):
    """True if the word's first sense is itself offensive, not just a rare extra sense of an ordinary word."""
    ss = entry.get("senses", [])
    return bool(ss) and bool(set(ss[0].get("tags", [])) & (STRONG | MILD) or TOPIC_GLOSS.search((ss[0].get("glosses") or [""])[0]))


def kind(entry, lang):
    tags = {t for s in entry.get("senses", []) for t in s.get("tags", [])}
    raw = list(entry.get("categories", [])) + [c for s in entry.get("senses", []) for c in s.get("categories", [])]
    cats = {c if isinstance(c, str) else c.get("name", "") for c in raw}
    if tags & STRONG or any(c.endswith((" vulgarities", " offensive terms", " ethnic slurs", " swear words")) for c in cats):
        return "strong"
    if tags & MILD or any(c.endswith(" derogatory terms") for c in cats):
        return "mild"
    if any(c.split(":", 1)[-1] in TOPICS for c in cats if ":" in c):
        return "topic"
    glosses = " ".join(s["glosses"][0] for s in entry.get("senses", []) if s.get("glosses"))
    if TOPIC_GLOSS.search(glosses):   # the bulk extracts carry no topical categories, so read the meaning
        return "topic"
    return None


def pronunciations(entry):
    out = []
    for s in entry.get("sounds", []):
        if "ipa" in s:
            tags = s.get("tags", [])
            if "Chinese" in str(entry.get("lang")) and not ({"Mandarin", "Cantonese"} & set(tags)):
                continue
            out.append(s["ipa"])
    if not out:
        for f in entry.get("forms", []):
            if "romanization" in f.get("tags", []):
                out.append(f["form"]); break
    if not out and re.fullmatch(r"[a-zA-Z]+", entry["word"]):
        out.append(entry["word"].lower())
    return list(dict.fromkeys(out))[:3]


def fetch():
    rows = []
    for lang in LANGS:
        page = urllib.request.urlopen(urllib.request.Request(
            f"https://kaikki.org/dictionary/{lang.replace(' ', '%20')}/index.html", headers=UA), timeout=60).read().decode()
        href = re.search(r'href="([^"]+\.jsonl)"', page).group(1)
        url = f"https://kaikki.org/dictionary/{lang.replace(' ', '%20')}/{href}.gz"
        n = 0
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=600) as r:
            for line in io.TextIOWrapper(gzip.GzipFile(fileobj=r), encoding="utf-8"):
                if '"tags"' not in line and '"categories"' not in line:
                    continue
                e = json.loads(line)
                if " " in e["word"] or e.get("lang") != lang and not (lang == "Chinese" and e.get("lang") == "Chinese"):
                    continue
                k = kind(e, lang)
                if not k:
                    continue
                gloss = next((g for s in e.get("senses", []) for g in s.get("glosses", [])), "")
                p = "yes" if primary(e) else "no"
                for ipa in pronunciations(e):
                    f = segs(ipa)
                    if f:
                        rows.append([lang, e["word"], ipa, f, k, p, gloss[:80].replace("\t", " ")]); n += 1
        print(f"{lang}: {n}", flush=True)
    rows = [list(r) for r in dict.fromkeys(tuple(r) for r in rows)]
    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["lang", "word", "ipa", "sounds", "kind", "primary", "gloss"])
        w.writerows(rows)
    print("wrote", len(rows), "rows")


# --- matching -------------------------------------------------------------------------------------------
def load():
    if not os.path.exists(OUT):
        return []
    return list(csv.DictReader(open(OUT), delimiter="\t"))


def match(ours, foreign):
    """How our form relates to a foreign word's sounds: 'exact', 'near', 'starts' or None."""
    f = foreign.replace(" ", "")
    if len(f) < 2:
        return None
    if ours == f:
        return "exact"
    if len(f) >= 3 and (key(ours) == key(f) or (f[-1] not in "aeiou" and key(ours) == key(f + "u"))):
        return "near"
    if len(f) >= 4 and key(ours).startswith(key(f)):
        return "starts"
    return None


CODES = {"English": "en", "Chinese": "zh", "Hindi": "hi", "Spanish": "es", "French": "fr", "Arabic": "ar",
         "Egyptian Arabic": "ar", "Bengali": "bn", "Portuguese": "pt", "Russian": "ru", "Urdu": "ur", "Indonesian": "id",
         "German": "de", "Japanese": "ja", "Turkish": "tr", "Tamil": "ta", "Vietnamese": "vi", "Tagalog": "fil",
         "Korean": "ko", "Persian": "fa", "Italian": "it", "Polish": "pl", "Ukrainian": "uk", "Malay": "ms"}
COMMON = 2.5   # Zipf frequency: about 1 in 3 million words of text, roughly what an adult speaker knows


def zipf(lang, word):
    """How common the foreign word is (wordfreq, Zipf scale), or None where there are no data."""
    try:
        import wordfreq
        return wordfreq.zipf_frequency(word, CODES[lang]) if lang in CODES else None
    except Exception:
        return None


def counts(r):
    z = zipf(r["lang"], r["word"])
    return z is None or z >= COMMON


_BLOCK = None


def blocked(form):
    """True if a candidate form exactly or nearly matches a common, strongly offensive word (main sense).
    Run with wordfreq installed, or every listed word counts as common and more forms are blocked."""
    global _BLOCK
    if _BLOCK is None:
        fs = [r["sounds"].replace(" ", "") for r in load() if r["kind"] == "strong" and r["primary"] == "yes" and counts(r)]
        exact = {f for f in fs if len(f) >= 2}
        near = {key(f) for f in fs if len(f) >= 3} | {key(f + "u") for f in fs if len(f) >= 3 and f[-1] not in "aeiou"}
        _BLOCK = (exact, near)
    return form in _BLOCK[0] or key(form) in _BLOCK[1]


def ours():
    out = []
    for name, col in (("lexicon.tsv", "gloss"), ("grammar.tsv", "gloss"), ("numbers.tsv", "value")):
        for r in csv.DictReader(open(os.path.join(DATA, name)), delimiter="\t"):
            out.append((r["form"], r[col], name.split(".")[0]))
    return out


def check():
    foreign = load()
    hits = []
    for form, gloss, src in ours():
        for r in foreign:
            m = match(form, r["sounds"])
            if m:
                z = zipf(r["lang"], r["word"])
                hits.append((form, gloss, src, m, r["kind"], r["primary"], r["lang"], r["word"], r["ipa"], r["gloss"],
                             "" if z is None else f"{z:.1f}"))
    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerow(["ours", "our gloss", "source", "match", "kind", "primary", "lang", "word", "ipa", "their gloss", "zipf"])
    w.writerows(sorted(hits, key=lambda h: (h[0], h[3], h[4])))


if __name__ == "__main__":
    {"fetch": fetch, "check": check}[sys.argv[1]]()

"""Part 1 of the coverage measurement: which concepts are common in modern life, per language.

  python3 concepts.py freq [LANG ...]    # top words with frequencies -> data/freq-LANG.tsv
  python3 concepts.py gloss [LANG ...]   # map each word to its senses via Wiktionary -> data/gloss-LANG.tsv
  python3 concepts.py build              # merge into one ranked concept list -> concepts.tsv

Sources:
  - wordfreq (subtitles, news, Wikipedia, social media, books; to ~2021) for 15 panel languages;
  - Leipzig Corpora Collection, *_community_2017 (web text) for Thai, Swahili, Hausa, Yoruba, Quechua;
  - Wiktionary via kaikki.org per-language extracts for each word's senses (English glosses).
Downloads are cached in ~/work/cache/coverage/. Each language counts once in the merge (N3).
"""
import collections, gzip, json, math, os, re, sys, tarfile, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
CACHE = os.path.expanduser("~/work/cache/coverage")
UA = {"User-Agent": "apupiwe-research/0.1 (coverage measurement)"}
N = 6000  # words per language

# code: (Wiktionary language name, source)
LANGS = {
    "zh": ("Chinese", "wordfreq"), "ja": ("Japanese", "wordfreq"), "ko": ("Korean", "wordfreq"),
    "vi": ("Vietnamese", "wordfreq"), "th": ("Thai", "leipzig:tha_community_2017"),
    "id": ("Indonesian", "wordfreq"), "fil": ("Tagalog", "wordfreq"), "hi": ("Hindi", "wordfreq"),
    "bn": ("Bengali", "wordfreq"), "ta": ("Tamil", "wordfreq"), "fa": ("Persian", "wordfreq"),
    "ar": ("Arabic", "wordfreq"), "tr": ("Turkish", "wordfreq"), "ru": ("Russian", "wordfreq"),
    "es": ("Spanish", "wordfreq"), "fr": ("French", "wordfreq"), "sw": ("Swahili", "leipzig:swa_community_2017"),
    "ha": ("Hausa", "leipzig:hau_community_2017"), "yo": ("Yoruba", "leipzig:yor_community_2017"),
    "qu": ("Quechua", "leipzig:que_community_2017"),
}
CONTENT = {"noun", "verb", "adj", "adv", "intj"}
class _Wordlike:
    """Letters (with combining marks, as in Indic scripts), apostrophes and hyphens; no digits."""
    def match(self, w):
        import unicodedata
        return bool(w) and unicodedata.category(w[0])[0] == "L" and all(
            unicodedata.category(c)[0] in "LM" or c in "'’ʼ-" for c in w)


WORDLIKE = _Wordlike()


def freq(code):
    name, src = LANGS[code]
    rows = []
    if src == "wordfreq":
        import wordfreq
        fd = wordfreq.get_frequency_dict(code)  # the stored list; word_frequency() would re-tokenize (needs MeCab)
        rows = [(w, p) for w, p in sorted(fd.items(), key=lambda x: -x[1])[:N * 3] if WORDLIKE.match(w)]
    else:
        corpus = src.split(":")[1]
        path = os.path.join(CACHE, f"{corpus}/{corpus}-words.txt")
        if not os.path.exists(path):
            with tarfile.open(os.path.join(CACHE, f"{corpus}.tar.gz")) as t:
                t.extract(f"{corpus}/{corpus}-words.txt", CACHE)
        counts = collections.Counter()
        for line in open(path, encoding="utf-8"):
            parts = line.rstrip("\n").split("\t")
            if len(parts) == 4 and WORDLIKE.match(parts[1]):
                counts[parts[1].lower()] += int(parts[3])
        total = sum(counts.values())
        rows = [(w, c / total) for w, c in counts.most_common(N * 2)]
    rows = rows[:N]
    os.makedirs(DATA, exist_ok=True)
    with open(os.path.join(DATA, f"freq-{code}.tsv"), "w") as f:
        f.write("word\tfreq\n")
        for w, p in rows:
            f.write(f"{w}\t{p:.3e}\n")
    print(code, len(rows), "words", flush=True)


SUBS = {"zh": "zh_cn", "ja": "ja", "ko": "ko", "vi": "vi", "th": "th", "id": "id", "hi": "hi", "bn": "bn", "ta": "ta",
        "fa": "fa", "ar": "ar", "tr": "tr", "ru": "ru", "es": "es", "fr": "fr"}  # OpenSubtitles 2018 (tl: mostly English, skipped)


def speech(code):
    """Speech-like frequencies: OpenSubtitles 2018 lists (hermitdave/FrequencyWords), cached in CACHE/subs."""
    if code not in SUBS:
        return
    counts = collections.Counter()
    for line in open(os.path.join(CACHE, "subs", f"{SUBS[code]}_50k.txt"), encoding="utf-8"):
        parts = line.split()
        if len(parts) == 2 and WORDLIKE.match(parts[0]):
            counts[parts[0].lower()] += int(parts[1])
    total = sum(counts.values())
    with open(os.path.join(DATA, f"sfreq-{code}.tsv"), "w") as f:
        f.write("word\tfreq\n")
        for w, c in counts.most_common(N):
            f.write(f"{w}\t{c / total:.3e}\n")
    print(code, "speech", min(N, len(counts)), "words", flush=True)


def kaikki(name):
    path = os.path.join(CACHE, f"kaikki-{name}.jsonl.gz")
    if not os.path.exists(path):
        page = urllib.request.urlopen(urllib.request.Request(
            f"https://kaikki.org/dictionary/{name}/index.html", headers=UA), timeout=60).read().decode()
        href = re.search(r'href="([^"]+\.jsonl)"', page).group(1)
        urllib.request.urlretrieve(f"https://kaikki.org/dictionary/{name}/{href}.gz", path + ".part")
        os.rename(path + ".part", path)
    return path


def clean(g):
    """A sense's English gloss -> a short concept label (first alternative, no notes)."""
    g = re.sub(r"\([^)]*\)|\[[^\]]*\]", "", g).split(";")[0].strip().lower()
    g = re.sub(r"\s+", " ", g)
    g = re.sub(r"^(to|a|an|the)\s+", "", g).strip(" .,:!?\"'")
    return g


STRIP = {  # marks Wiktionary writes and everyday text leaves out
    "ru": "\u0301\u0300", "ar": "".join(chr(c) for c in range(0x064B, 0x0653)) + "\u0670\u0640",
    "fa": "".join(chr(c) for c in range(0x064B, 0x0653)) + "\u0670\u0640", "ha": "ALL", "yo": "ALL", "qu": "ALL",
}


def norm(code, w):
    import unicodedata
    w = w.lower().strip("-")
    marks = STRIP.get(code)
    if not marks:
        return w
    d = unicodedata.normalize("NFD", w)
    d = "".join(c for c in d if not (unicodedata.category(c) == "Mn" and (marks == "ALL" or c in marks)))
    return unicodedata.normalize("NFC", d)


FORM_GLOSS = re.compile(r"\b(form|plural|spelling|stem|inflection|participle|tense|case|romanization|abbreviation|"
                        r"synonym|alternative|obsolete|misspelling|clipping|contraction) of\b", re.I)


def gloss(code):
    name, _ = LANGS[code]
    words = []
    for fn in (f"freq-{code}.tsv", f"sfreq-{code}.tsv"):  # text and, where there is one, speech
        if os.path.exists(os.path.join(DATA, fn)):
            words += [l.split("\t")[0] for l in open(os.path.join(DATA, fn)).read().split("\n")[1:] if l]
    words = list(dict.fromkeys(words))
    want = {norm(code, w) for w in words}
    senses = {}                      # lemma (lowercase) -> list of (pos, label)
    lemma_of = collections.defaultdict(list)  # surface form -> lemmas
    with gzip.open(kaikki(name), "rt", encoding="utf-8") as fh:
        for line in fh:
            e = json.loads(line)
            if e.get("lang") != name:
                continue
            w = norm(code, e["word"])
            pos = e.get("pos", "")
            labels = []
            for s in e.get("senses", []):
                tgt = s.get("form_of") or s.get("alt_of")
                gl = (s.get("glosses") or [""])[0]
                if tgt or "form-of" in s.get("tags", []) or FORM_GLOSS.search(gl):
                    if w in want:
                        for t in tgt or []:
                            lemma_of[w].append(norm(code, t["word"]))
                    continue
                lab = clean(gl)
                if lab:  # grammatical senses keep their share of the word's weight, then drop out in build
                    labels.append((pos, lab if pos in CONTENT else "#fn"))
            if labels:
                senses.setdefault(w, []).extend(labels[:4])
            if pos in CONTENT or labels:
                for fm in e.get("forms", []):
                    f = norm(code, fm.get("form", ""))
                    if f in want and f != w:
                        lemma_of[f].append(w)
    ai = {}  # AI glosses for frequent words the language's Wiktionary lacks (data/aigloss-LANG.tsv)
    aipath = os.path.join(DATA, f"aigloss-{code}.tsv")
    if os.path.exists(aipath):
        for l in open(aipath, encoding="utf-8"):
            if "\t" in l:
                w, labs = l.rstrip("\n").split("\t", 1)
                labs = [clean(x) if not x.strip().startswith("#") else x.strip() for x in labs.split("|")]
                labs = [x for x in labs if x and x not in ("?", "#name", "#foreign")]
                if labs:
                    ai[w.strip()] = labs[:4]
    out, unmatched = [], 0
    with open(os.path.join(DATA, f"gloss-{code}.tsv"), "w") as f:
        f.write("word\tlemmas\tsenses\n")
        for w0 in words:
            w = norm(code, w0)
            # the word's own entry wins; inflected forms fall back to their lemma
            lemmas = [w] if w in senses else [l for l in dict.fromkeys(lemma_of.get(w, [])) if l in senses]
            labs = []
            for l in lemmas:
                for pos, lab in senses[l]:
                    if lab not in labs:
                        labs.append(lab)
            if not labs and w0 in ai:
                labs = ai[w0]
            if not labs:
                unmatched += 1
            elif all(x == "#fn" for x in labs):
                labs = ["#fn"]
            f.write(f"{w0}\t{','.join(lemmas)}\t{' | '.join(labs[:4])}\n")
    print(f"{code}: {len(words) - unmatched}/{len(words)} words matched", flush=True)


SPEECH = True


def build():
    shares = {}
    for code in LANGS:
        path = os.path.join(DATA, f"gloss-{code}.tsv")
        if not os.path.exists(path):
            continue
        gl = {}
        for l in open(path).read().split("\n")[1:]:
            if l:
                w, _, labs = l.split("\t")
                gl[w] = [x for x in labs.split(" | ") if x]
        per_source = []
        for fn in (f"freq-{code}.tsv", f"sfreq-{code}.tsv"):
            fp = os.path.join(DATA, fn)
            if not os.path.exists(fp) or (fn.startswith("s") and not SPEECH):
                continue
            fr = dict(l.split("\t") for l in open(fp).read().split("\n")[1:] if l)
            sc = collections.Counter()
            for w, f in fr.items():
                labs = gl.get(w, [])
                wt = [1 / (i + 1) for i in range(len(labs))]
                for lab, x in zip(labs, wt):
                    if lab != "#fn":
                        sc[lab] += float(f) * x / sum(wt)
            total = sum(sc.values())
            per_source.append({k: v / total for k, v in sc.items()})
        # one vote per language: text and speech shares averaged
        keys = set().union(*per_source)
        shares[code] = {k: sum(s.get(k, 0) for s in per_source) / len(per_source) for k in keys}
    floor = 1e-7
    concepts = set().union(*[s.keys() for s in shares.values()])
    rows = []
    for c in concepts:
        vals = sorted(math.log10(s.get(c, 0) + floor) for s in shares.values())
        score = (vals[len(vals) // 2] + vals[(len(vals) - 1) // 2]) / 2  # median: one language's error can't lift a concept
        vals = [s.get(c, 0) for s in shares.values()]
        rows.append((score, sum(v > 0 for v in vals), c))
    rows.sort(reverse=True)
    with open(os.path.join(HERE, "concepts.tsv"), "w") as f:
        f.write(f"rank\tconcept\tlanguages\tscore\t# {len(shares)} languages, each counted once\n")
        for i, (s, n, c) in enumerate(rows, 1):
            f.write(f"{i}\t{c}\t{n}\t{s:.3f}\n")
    print(len(rows), "concepts from", len(shares), "languages")


if __name__ == "__main__":
    SPEECH = "--text-only" not in sys.argv
    sys.argv = [a for a in sys.argv if a != "--text-only"]
    cmd, args = sys.argv[1], sys.argv[2:] or list(LANGS)
    if cmd == "freq":
        for c in args:
            freq(c)
    elif cmd == "speech":
        for c in args:
            speech(c)
    elif cmd == "gloss":
        for c in args:
            gloss(c)
    elif cmd == "build":
        build()

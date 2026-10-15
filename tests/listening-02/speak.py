"""Say Apupiwe aloud with VOICEVOX (author, 2026-10-15: the free voice step of the listening test).

VOICEVOX is Japanese text-to-speech whose input can be given syllable by syllable (mora by mora):
consonant, vowel and pitch. Apupiwe's sounds are close to a subset of Japanese, so each syllable is
passed as one mora, final n as the Japanese moraic n, and the pitch is set by our rules, not Japanese
ones (reference 2.4, 2.6, 2.7): the first syllable of a content word or digit is high and the pitch
steps down after it; grammar words are low; each stressed syllable is a little lower than the one
before; a pause resets it. VOICEVOX sets the durations (Japanese timing; nothing is lengthened by us).

Nearest sounds (reference 2.10's harmless variants aside): l is said as Japanese r [ɾ], f as [ɸ]~[f],
y and w as Japanese y and w (yi and wu don't exist in Japanese; VOICEVOX is asked for them anyway).

Needs a running engine: voicevox-engine --host 127.0.0.1 --port 50021 (nixpkgs, unfree).

  python3 speak.py OUTDIR [SPEAKER]      # the word and sentence list below -> OUTDIR/*.wav
"""
import json, os, re, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import words as W

URL = "http://127.0.0.1:50021"
CONS = {"p": "p", "b": "b", "t": "t", "d": "d", "k": "k", "g": "g", "m": "m", "n": "n", "f": "f", "s": "s",
        "l": "r", "w": "w", "y": "y", "j": "y", "": None}   # inventory writes y as j
GRAMMAR = {r["form"] for r in W.read("grammar.tsv")}
DIGITS = {r["form"] for r in W.read("numbers.tsv") if r["kind"] == "digit"}
BASE, HIGH, STEP = 5.55, 0.40, 0.04   # VOICEVOX pitch is log-F0; HIGH ~ a fifth up, STEP = declination


def post(path, body, **q):
    qs = "&".join(f"{k}={v}" for k, v in q.items())
    req = urllib.request.Request(f"{URL}{path}?{qs}", data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    return urllib.request.urlopen(req, timeout=120).read()


def moras(word, stressed):
    out = []
    for i, s in enumerate(W.split(word)):
        c, v, n = W.INV.syl[s]
        out.append({"text": W.SYL[s], "consonant": CONS[c], "consonant_length": 0.0 if c else None,
                    "vowel": v, "vowel_length": 0.0, "pitch": 0.0, "_hi": stressed and i == 0})
        if n:
            out.append({"text": "n", "consonant": None, "consonant_length": None, "vowel": "N",
                        "vowel_length": 0.0, "pitch": 0.0, "_hi": stressed and i == 0})
    return out


def query(text):
    """Accent phrases for a sentence: one phrase per pause (comma or sentence end)."""
    phrases = []
    for chunk in re.split(r"[,.?!]", text.lower()):
        toks = re.findall(r"[a-z]+", chunk)
        if not toks:
            continue
        ms, level = [], BASE
        for t in toks:
            t = t.replace("r", "l")   # names keep their owner's spelling; said with the nearest sounds (11.2)
            stressed = t not in GRAMMAR or len(W.split(t)) > 1 or t in DIGITS
            for m in moras(t, stressed):
                ms.append(m)
            if stressed:
                level -= STEP
        phrases.append({"moras": ms, "accent": 1, "pause_mora": None, "is_interrogative": False})
    for i, p in enumerate(phrases[:-1]):
        p["pause_mora"] = {"text": "、", "consonant": None, "consonant_length": None, "vowel": "pau",
                           "vowel_length": 0.25, "pitch": 0.0}
    return phrases


def pitch(phrases):
    for p in phrases:
        top = BASE + HIGH
        for m in p["moras"]:
            if m.pop("_hi"):
                m["pitch"] = top
                top -= STEP
            else:
                m["pitch"] = BASE - 0.05
    return phrases


def say(text, speaker, out):
    ph = query(text)
    keep = [[m["_hi"] for m in p["moras"]] for p in ph]
    clean = [{**p, "moras": [{k: v for k, v in m.items() if k != "_hi"} for m in p["moras"]]} for p in ph]
    timed = json.loads(post("/mora_length", clean, speaker=speaker))   # VOICEVOX durations for our moras
    for p, hi in zip(timed, keep):
        for m, h in zip(p["moras"], hi):
            m["_hi"] = h
    q = {"accent_phrases": pitch(timed), "speedScale": 0.9, "pitchScale": 0.0, "intonationScale": 1.0,
         "volumeScale": 1.0, "prePhonemeLength": 0.2, "postPhonemeLength": 0.3, "pauseLength": None,
         "pauseLengthScale": 1.0, "outputSamplingRate": 24000, "outputStereo": False, "kana": ""}
    open(out, "wb").write(post("/synthesis", q, speaker=speaker))


# Words that failed in listening-01 or test hard sounds, then reference sentences.
WORDS = ["guyi", "guti", "wupi", "dunu", "gudu", "totu", "apu pi we", "lenu", "fenu", "sisa",
         "yi", "wu", "kin", "tin", "din", "pen", "ben", "fa", "sa"]
SENTENCES = [
    ("hello", "upe."),
    ("i-dont-know", "to mu lugo."),
    ("is-the-house-big", "min guyi gun kudu."),
    ("mara-said", "en mara sin oyi."),
    ("come-please", "so nun me obu."),
    ("are-you-coming", "min me obu, min."),
    ("about-30-people", "ewo fu ka yawu."),
    ("spelling-mara", "mayiku alufa lomeyo alufa."),
]

if __name__ == "__main__":
    outdir = sys.argv[1]
    speaker = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    os.makedirs(outdir, exist_ok=True)
    for w in WORDS:
        say(w + ".", speaker, os.path.join(outdir, f"word-{w.replace(' ', '-')}.wav"))
    for name, s in SENTENCES:
        say(s, speaker, os.path.join(outdir, f"sentence-{name}.wav"))
    print("wrote", len(WORDS) + len(SENTENCES), "files to", outdir)

"""Say Apupiwe aloud with Piper, given IPA directly (author, 2026-10-15: "move to something that can do
true ipa"; replaces the VOICEVOX attempt in speak.py, whose Japanese u sounded like "uh").

Piper's voices are built on IPA phonemes; text inside [[ ]] skips its text step and is said as the
phonemes given. Each Apupiwe word is turned into broad IPA: the sounds as written (y = j, g = ɡ), the
stress mark ˈ before the first syllable of content words, digits and two-syllable operators, none on
one-syllable grammar words (reference 2.4); commas and full stops kept as pauses. p t k are given
unaspirated (a harmless variant, 2.2), since the Spanish, Italian and Indonesian voices never learned
aspiration. The voice decides the melody; the stress mark is our only control over it.

  python3 speak_piper.py OUTDIR PIPER VOICEDIR      # every voice in VOICEDIR (*.onnx) -> OUTDIR/VOICE/*.wav
"""
import os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import words as W
from speak import WORDS, SENTENCES, GRAMMAR, DIGITS

IPA = {"g": "ɡ", "y": "j", "j": "j"}


def ipa_word(t):
    t = t.replace("r", "l")   # names keep their owner's spelling; said with the nearest sounds (11.2)
    syl = W.split(t)
    stressed = t not in GRAMMAR or len(syl) > 1 or t in DIGITS
    out = ""
    for i, s in enumerate(syl):
        c, v, n = W.INV.syl[s]
        out += ("ˈ" if stressed and i == 0 else "") + IPA.get(c, c) + v + n
    return out


def ipa(text):
    parts = re.findall(r"[a-z]+|[,.?!]", text.lower())
    return " ".join(ipa_word(p) if p.isalpha() else p for p in parts).replace(" ,", ",").replace(" .", ".")


def say(text, piper, model, out):
    subprocess.run([piper, "-m", model, "-f", out], input=f"[[ {ipa(text)} ]]", text=True, check=True,
                   capture_output=True)


if __name__ == "__main__":
    outdir, piper, voicedir = sys.argv[1:4]
    for f in sorted(os.listdir(voicedir)):
        if not f.endswith(".onnx"):
            continue
        name, model = f[:-5], os.path.join(voicedir, f)
        d = os.path.join(outdir, name)
        os.makedirs(d, exist_ok=True)
        for w in WORDS:
            say(w + ".", piper, model, os.path.join(d, f"word-{w.replace(' ', '-')}.wav"))
        for n, s in SENTENCES:
            say(s, piper, model, os.path.join(d, f"sentence-{n}.wav"))
        print(name, "done", flush=True)
    for w in ["guyi", "apu pi we"]:
        print(w, "->", ipa(w))
    for n, s in SENTENCES[:3]:
        print(s, "->", ipa(s))

"""Listening test 01 (2026-10-09): does the mishearing model's ranking match a human ear?

Picks the word pairs the model rates most confusable (content words, and grammar words that share
a slot), plus control pairs it rates very distinct; synthesises each word with a Spanish Piper
voice (respelt so it says our sounds, stress on the first syllable); writes the trials to the
user's vault and the answer key here. No added noise: the user adds noise when listening.

  python make.py OUTDIR VOICE   (needs numpy, kokoro-onnx with its model files in /tmp/kk, ffmpeg)

Version 2 (same day): the Spanish Piper voice read our spelling as Spanish text and "butchered" it
(user). Kokoro (kokoro-onnx v1.0) takes phonemes directly, so each word is given as exact IPA.
"""
import csv, itertools, os, random, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import words as W, build as B

OUT, VOICE = sys.argv[1], sys.argv[2]
from kokoro_onnx import Kokoro
import soundfile as sf
KOKORO = Kokoro("/tmp/kk/kokoro-v1.0.onnx", "/tmp/kk/voices-v1.0.bin")
rng = random.Random(1)
S, IDX = W.S, W.IDX


def p(a, b):
    """Model probability that word a is heard as word b (same syllable count), both directions summed."""
    sa, sb = W.split(a), W.split(b)
    if len(sa) != len(sb):
        return 0.0
    f = lambda x, y: float(__import__("numpy").prod([S[i, j] for i, j in zip(x, y)]))
    return f(sa, sb) + f(sb, sa)


lex = [r for r in W.read("lexicon.tsv") if r["field"] not in ("unit", "loan") and int(r["tier"]) >= 3]
two = [r for r in lex if len(W.split(r["form"])) == 2]
pairs = sorted(((p(a["form"], b["form"]), a, b) for a, b in itertools.combinations(two, 2)), key=lambda x: -x[0])
content, seen = [], set()
for sc, a, b in pairs:
    if a["form"] in seen or b["form"] in seen:
        continue
    content.append(("content", sc, a, b)); seen |= {a["form"], b["form"]}
    if len(content) == 20:
        break
grammar = W.read("grammar.tsv")
gl = {g["gloss"]: g for g in grammar}
gp = set()
for grp in B.GROUPS_STRICT.values():
    for x, y in itertools.combinations([g for g in grp.split() if g in gl], 2):
        gp.add(tuple(sorted((x, y))))
gpairs = sorted(((p(gl[x]["form"], gl[y]["form"]), {"gloss": x, "form": gl[x]["form"]}, {"gloss": y, "form": gl[y]["form"]})
                 for x, y in gp), key=lambda t: -t[0])[:6]
grammar_pairs = [("grammar", sc, a, b) for sc, a, b in gpairs]
low = [t for t in pairs[len(pairs) // 2:] if t[1]["form"] not in seen and t[2]["form"] not in seen]
controls = [("control", sc, a, b) for sc, a, b in rng.sample(low, 6)]
allpairs = content + grammar_pairs + controls


def ipa(form):
    """Exact phonemes: one IPA symbol per letter (g -> ɡ, y -> j), stress on the first syllable.
    Every word is said as a citation form, so one-syllable words are stressed too."""
    return "ˈ" + form.replace("g", "ɡ").replace("y", "j")


os.makedirs(OUT, exist_ok=True)
trials = []
for kind, sc, a, b in allpairs:
    for _ in range(2):  # each trial's word is picked at random, so the first answer says nothing about the second
        target = rng.choice((a, b))
        trials.append({"kind": kind, "model": f"{sc:.4f}", "a": a["form"], "b": b["form"], "target": target["form"],
                       "a_gloss": a["gloss"], "b_gloss": b["gloss"]})
while True:  # no pair on two trials in a row
    rng.shuffle(trials)
    if all({trials[i]["a"], trials[i]["b"]} != {trials[i + 1]["a"], trials[i + 1]["b"]} for i in range(len(trials) - 1)):
        break
for n, t in enumerate(trials, 1):
    t["n"] = n
    wav = os.path.join("/tmp/kk", f"t{n:02d}.wav")
    audio, sr = KOKORO.create(ipa(t["target"]), voice=VOICE, is_phonemes=True, speed=0.9)
    sf.write(wav, audio, sr)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-af", "apad=pad_dur=0.3", "-b:a", "96k",
                    os.path.join(OUT, f"{VOICE}-t{n:02d}.mp3")], check=True)
with open(os.path.join(HERE, f"key-{VOICE}.tsv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["n", "target", "a", "b", "kind", "model", "a_gloss", "b_gloss"], delimiter="\t",
                       lineterminator="\n")
    w.writeheader(); w.writerows(trials)
lines = ["# Listening test 01", "",
         "For each clip, write which of the two words you heard: **A** or **B**. Guess if unsure; don't replay more than once. Each clip's word was picked at random, so a pair can be the same word both times.",
         "Play them with whatever background noise you like (a fan, a busy room, music); note what you used at the bottom.",
         f"Voice: {VOICE} (Kokoro speech synthesiser, given each word's exact sounds). It is not a native speaker of the language.", ""]
for t in trials:
    a, b = sorted([t["a"], t["b"]])
    lines += [f"**{t['n']}.** ![[{VOICE}-t{t['n']:02d}.mp3]]", f"A: {a}  ·  B: {b}  ·  heard: ", ""]
lines += ["Noise used: ", ""]
open(os.path.join(OUT, f"listening-test-01-{VOICE}.md"), "w").write("\n".join(lines))
print(len(trials), "trials;", len(content), "content,", len(grammar_pairs), "grammar,", len(controls), "control pairs")
for kind, sc, a, b in allpairs:
    print(f"{kind:8} {sc:.4f}  {a['form']} ({a['gloss']}) / {b['form']} ({b['gloss']})")

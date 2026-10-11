"""Listening test 01 (2026-10-09): does the mishearing model's ranking match a human ear?

Picks the word pairs the model rates most confusable (content words, and grammar words that share
a slot), plus control pairs it rates very distinct; synthesises each word with a Spanish Piper
voice (respelt so it says our sounds, stress on the first syllable); writes the trials to the
author's vault and the answer key here. No added noise: the author adds noise when listening.

  python make.py OUTDIR VOICE   (needs numpy, mbrola with its voices, ffmpeg; VOICE e.g. it3)

Version 3 (same day). v1: a Spanish Piper voice read our spelling as Spanish text and "butchered" it
(author). v2: Kokoro took phonemes but its neural voices "sneak sounds that are not there into the
words" (author). v3: MBROLA diphone synthesis plays exactly the phonemes given, with the durations and
pitch given, and adds nothing. The Italian voice it3 lacks w+u and y+i (never recorded); the Spanish
voice es2 has them but softens g and d (the author heard guyi as "uyi"); so does the Mexican mx1 between
vowels, and its g before u has almost no release ("oooo-yeee"). The Indonesian voice id1 (used) has
real stops: a voice bar then a clear release for b, d, g, and silence then a burst for k.
"""
import csv, itertools, os, random, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import words as W, build as B

OUT, VOICE = sys.argv[1], sys.argv[2]
import shutil
MBROLA_DB = os.path.join(os.path.dirname(os.path.dirname(shutil.which("mbrola"))), "share", "mbrola", "voices")
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


DUR = dict(p=80, t=80, k=85, b=70, d=70, g=70, m=70, n=70, f=100, s=105, l=60, w=55, j=55)
Y = "jj" if VOICE.startswith(("es", "mx")) else "j"   # the voice's symbol for our y
VOWELS = {"id1": dict(a="V", e="e", i="I", o="Q", u="U")}.get(VOICE, {})   # Indonesian writes vowels in SAMPA
STRESSED = "1" if VOICE.startswith("it") else ""          # Italian voices record stressed vowels separately
BASE, PEAK = 105, 140   # Hz: the stressed first syllable is higher and the rest step down (language.md, Sounds)


def pho(form):
    """MBROLA input for one word in citation form: every phoneme with its length in ms and pitch points.
    Stress is pitch, not length: all vowels 110 ms, the last 140 ms (ordinary phrase-final lengthening)."""
    syl = W.split(form)
    # carrier phrase "oyi ___" ("say ___"): a word-initial stop after silence is heard only by its release,
    # which these voices barely produce before u (the author heard guyi as "uuuu-yeee"); after a vowel the
    # closure is a clear gap (g drops to 7% of the vowel's energy in id1)
    lines = ["_ 150", f"{VOWELS.get('o', 'o')}{STRESSED} 110 10 125 90 115", f"{Y} 55", f"{VOWELS.get('i', 'i')} 100 50 100"]
    if not W.INV.syl[syl[0]][0]:
        lines.append("_ 60")   # vowel-initial word: a short break so it doesn't merge with "oyi"
    held_n = 0
    for k, i in enumerate(syl):
        onset, vowel, coda = W.INV.syl[i]
        onset = {"y": Y, "j": Y}.get(onset, onset)   # the inventory writes our y as j
        last = k == len(syl) - 1
        if onset:
            lines.append(f"{onset} {DUR[onset.replace('jj', 'j')] + held_n}")
            held_n = 0
        v = VOWELS.get(vowel, vowel) + (STRESSED if k == 0 else "")
        if k == 0:
            lines.append(f"{v} 110 10 {PEAK} 90 {PEAK - 15}")
        else:
            f0 = BASE - 6 * (k - 1)
            lines.append(f"{v} {140 if last and not coda else 110} 50 {f0}")
        if coda:
            nxt = W.INV.syl[syl[k + 1]][0] if not last else None
            if nxt == "n":      # n + n is one long n (a geminate); some voices have no n-n diphone
                held_n = DUR["n"]
            else:
                lines.append(f"n {DUR['n'] + (30 if last else 0)}")
    lines.append("_ 150")
    return "\n".join(lines) + "\n"


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
    wav, ph = f"/tmp/kk/t{n:02d}.wav", f"/tmp/kk/t{n:02d}.pho"
    open(ph, "w").write(pho(t["target"]))
    r = subprocess.run(["mbrola", os.path.join(MBROLA_DB, VOICE, VOICE), ph, wav], capture_output=True, text=True)
    if r.returncode or "Warning" in r.stderr or "rror" in r.stderr:
        print("mbrola:", t["target"], r.stderr.strip()[:200])
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", wav, "-af", "loudnorm=I=-18,apad=pad_dur=0.3", "-b:a", "96k",
                    os.path.join(OUT, f"{VOICE}-t{n:02d}.mp3")], check=True)
with open(os.path.join(HERE, f"key-{VOICE}.tsv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=["n", "target", "a", "b", "kind", "model", "a_gloss", "b_gloss"], delimiter="\t",
                       lineterminator="\n")
    w.writeheader(); w.writerows(trials)
lines = ["# Listening test 01", "",
         "For each clip, write which of the two words you heard: **A** or **B**. Guess if unsure; don't replay more than once. Each clip's word was picked at random, so a pair can be the same word both times.",
         "Play them with whatever background noise you like (a fan, a busy room, music); note what you used at the bottom.",
         f"Each clip says **oyi** (\"say\") and then the word; listen for the word after **oyi**.",
         f"Voice: MBROLA {VOICE}, a diphone synthesiser that plays exactly the sounds it is given, nothing added. It sounds robotic; that's the price of precision.", ""]
for t in trials:
    a, b = sorted([t["a"], t["b"]])
    lines += [f"**{t['n']}.** ![[{VOICE}-t{t['n']:02d}.mp3]]", f"A: {a}  ·  B: {b}  ·  heard: ", ""]
lines += ["Noise used: ", ""]
open(os.path.join(OUT, f"listening-test-01-{VOICE}.md"), "w").write("\n".join(lines))
print(len(trials), "trials;", len(content), "content,", len(grammar_pairs), "grammar,", len(controls), "control pairs")
for kind, sc, a, b in allpairs:
    print(f"{kind:8} {sc:.4f}  {a['form']} ({a['gloss']}) / {b['form']} ({b['gloss']})")

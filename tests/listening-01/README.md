# Listening test 01 (2026-10-09)

**Question:** does the mishearing model's ranking match a human ear? No constructed language has measured this (research report, 2026-10-09).

**Design:** 32 word pairs: the 20 content-word pairs the model rates most confusable, the 6 most confusable grammar-word pairs that share a slot, and 6 control pairs it rates very distinct. Each pair is played twice; each time its word is picked at random, and no pair appears twice in a row (64 trials). The listener picks A or B (two-alternative forced choice). The audio is clean; the user adds background noise when listening (user's choice).

**Voice:** three tries on 2026-10-09.
1. A Spanish Piper voice read respelt words as Spanish text: "very much butchering" them (user).
2. Kokoro, given exact phonemes: its neural voices still "sneak sounds that are not there into the words" (user).
3. **MBROLA diphone synthesis** (used): it plays exactly the phonemes given, with the durations and pitch given, and adds nothing. Each word is written out by hand in `make.py`: stressed first syllable higher in pitch, stepping down, not longer; all vowels 110 ms, the last 140 ms. The Italian voice lacked w+u and y+i. The Spanish voice es2 had them, but the user heard **guyi** as "uyi": measured, its voiced stops have no closure or burst (a softened Spanish g). The Mexican Spanish voice **mx1** (used) has a ~50 ms closure and a clear release for b, d, g and k, and every sequence we need, with our y as its "jj" (the y of *mayo*). Loudness is normalised (it is quiet). Robotic, but nothing is inserted. The vault has a check page with known words (`00-check-the-voice.md`).

**Files:** `make.py` builds the test; `key-<voice>.tsv` is the answer key (the same for all three voices) (the listener shouldn't read it). The test page and clips are in the user's vault: `Language/listening-test-01/`.

**Scoring (when answers come back):** accuracy per pair type, and whether errors fall on the pairs the model ranks highest. Prediction: content and grammar pairs have more errors than controls, and within them, more confusable pairs have more errors. If controls do as badly, or the ranking doesn't hold, the model needs real listener data before it chooses more words.

# Listening test 01 (2026-10-09)

**Question:** does the mishearing model's ranking match a human ear? No constructed language has measured this (research report, 2026-10-09).

**Design:** 32 word pairs: the 20 content-word pairs the model rates most confusable, the 6 most confusable grammar-word pairs that share a slot, and 6 control pairs it rates very distinct. Each pair is played twice; each time its word is picked at random, and no pair appears twice in a row (64 trials). The listener picks A or B (two-alternative forced choice). The audio is clean; the user adds background noise when listening (user's choice).

**Voice:** three tries on 2026-10-09.
1. A Spanish Piper voice read respelt words as Spanish text: "very much butchering" them (user).
2. Kokoro, given exact phonemes: its neural voices still "sneak sounds that are not there into the words" (user).
3. **MBROLA diphone synthesis** (used): it plays exactly the phonemes given, with the durations and pitch given, and adds nothing. Each word is written out by hand in `make.py`: stressed first syllable higher in pitch, stepping down, not longer; all vowels 110 ms, the last 140 ms. The Italian voice lacked w+u and y+i. The Spanish voice es2 had them, but the user heard **guyi** as "uyi": measured, its voiced stops have no closure or burst (a softened Spanish g). The Mexican Spanish voice mx1 had real stops after silence, but its g before u has almost no release; the user still heard guyi as "oooo-yeee". The **Indonesian voice id1** (used) has true stops (a voice bar then a clear release for b, d, g; silence then a burst for k), pure vowels and our consonants; it writes vowels in SAMPA (a=V, o=Q, i=I, u=U) and lacks n-n, so a doubled n is one long n. Loudness is normalised. Even so, a word-initial g before u has almost no release in any voice (the user still heard guyi as "uuuu-yeee"), so every word is said in the carrier **oyi ___** ("say ___"): after a vowel the closure is a clear gap (g drops to 7% of the vowel's energy). Vowel-initial words get a 60 ms break after the carrier.

**Files:** `make.py` builds the test; `key-<voice>.tsv` is the answer key (the same for all three voices) (the listener shouldn't read it). The test page and clips are in the user's vault: `Language/listening-test-01/`.

**Scoring (when answers come back):** accuracy per pair type, and whether errors fall on the pairs the model ranks highest. Prediction: content and grammar pairs have more errors than controls, and within them, more confusable pairs have more errors. If controls do as badly, or the ranking doesn't hold, the model needs real listener data before it chooses more words.

**Excluded trials (2026-10-09):** with the carrier, the user hears "oyi" but guyi still as "uuuu-yeee": the voices give the closure before g but no release burst before u. Trials 26 and 37 (wupi/guti) and 40 and 53 (dunu/gudu) are skipped on the test page and excluded from scoring. Any other clip the user marks as wrong is excluded too.

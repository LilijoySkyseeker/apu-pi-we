# Listening test 01 (2026-10-09)

**Question:** does the mishearing model's ranking match a human ear? No constructed language has measured this (research report, 2026-10-09).

**Design:** 32 word pairs: the 20 content-word pairs the model rates most confusable, the 6 most confusable grammar-word pairs that share a slot, and 6 control pairs it rates very distinct. Each pair is played twice; each time its word is picked at random, and no pair appears twice in a row (64 trials). The listener picks A or B (two-alternative forced choice). The audio is clean; the user adds background noise when listening (user's choice).

**Voice:** version 1 used a Spanish Piper voice reading respelt words; the user reported it "very much butchering" them, because it guesses pronunciation from spelling. Version 2 uses Kokoro (kokoro-onnx v1.0, model files from its GitHub release in /tmp/kk), which takes phonemes directly: each word is given as exact IPA (one symbol per letter, stress on the first syllable, every word in citation form). The test is built in three voices with identical trials (Spanish ef_dora, Italian if_sara, American English af_heart); the user picks the voice that sounds right on a sample page (`00-choose-a-voice.md`) and takes that one. It is still a synthesiser, not a speaker of the language.

**Files:** `make.py` builds the test; `key-<voice>.tsv` is the answer key (the same for all three voices) (the listener shouldn't read it). The test page and clips are in the user's vault: `Language/listening-test-01/`.

**Scoring (when answers come back):** accuracy per pair type, and whether errors fall on the pairs the model ranks highest. Prediction: content and grammar pairs have more errors than controls, and within them, more confusable pairs have more errors. If controls do as badly, or the ranking doesn't hold, the model needs real listener data before it chooses more words.

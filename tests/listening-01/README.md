# Listening test 01 (2026-10-09)

**Question:** does the mishearing model's ranking match a human ear? No constructed language has measured this (research report, 2026-10-09).

**Design:** 32 word pairs: the 20 content-word pairs the model rates most confusable, the 6 most confusable grammar-word pairs that share a slot, and 6 control pairs it rates very distinct. Each pair is played twice; each time its word is picked at random, and no pair appears twice in a row (64 trials). The listener picks A or B (two-alternative forced choice). The audio is clean; the user adds background noise when listening (user's choice).

**Voice:** Piper TTS, Spanish `es_ES-davefx-medium` (downloaded to /tmp/lt by hand; Hugging Face rhasspy/piper-voices). Words are respelt for it (hard g, w as u, an acute accent on the first vowel to put stress there). A Spanish voice says our pure vowels and one-letter-per-sound spelling well; Spanish softens b, d, g between vowels, which the language allows as a harmless variant. It is a synthesiser, not a speaker of the language.

**Files:** `make.py` builds the test; `key.tsv` is the answer key (the listener shouldn't read it). The test page and clips are in the user's vault: `Language/listening-test-01/`.

**Scoring (when answers come back):** accuracy per pair type, and whether errors fall on the pairs the model ranks highest. Prediction: content and grammar pairs have more errors than controls, and within them, more confusable pairs have more errors. If controls do as badly, or the ranking doesn't hold, the model needs real listener data before it chooses more words.

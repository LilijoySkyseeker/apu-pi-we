# Round-trip test 01: Japanese → Apu Pi We → Japanese

Written 2026-10-10, before any text existed.

**Question:** does meaning survive when English is neither the source nor the
target? Two things are being probed:
1. **English leaks:** roots that silently carry an English word's range, so
   two Japanese meanings collapse into one root (e.g. 時間 "time" vs 回
   "occasion", which were one root until today).
2. **Distinctions English lacks:** dropped arguments, sentence-final stance
   particles (ね, よ), giving/receiving direction (あげる/くれる/もらう),
   hearsay and inference (そうだ, らしい), politeness shifts, ている aspect.

## Setup

1. A fresh agent writes a natural casual conversation **directly in
   Japanese**, not translated from English, told nothing about the
   hypothesis (`source.ja.txt`).
2. A fresh agent translates it into Apu Pi We using only the rules and data
   files (`translation.md`).
3. A fresh agent who has never seen the source translates the Apu Pi We back
   into Japanese (`back.ja.md`).
4. A fresh judge compares the source with the back-translation, line by line
   (`scores.md`).

## Scoring (fixed in advance)

- Meaning per line: 2 = same, including who did what and stance; 1 = gist,
  with a real piece lost; 0 = wrong or missing.
- For every loss, the judge names the cause:
  - **L, language:** Apu Pi We has no way to say it.
  - **T, translator:** a way exists but wasn't used.
  - **E, English leak:** a root was chosen through its English gloss and
    carried the wrong range.
- Separately: list each Japanese distinction from point 2 that occurred, and
  whether it survived.

Claude writes the English summary (`analysis.md`).

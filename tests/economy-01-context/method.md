# Economy test 01: does context get to take over?

Written 2026-10-10, before the source or translation existed.

**Question:** in casual talk between people who share context, how much does
Apu Pi We force the speaker to say that English leaves to context, and the
reverse?

**Why:** the first-principles yardstick (`~/research/Language/language-first-principles-2026-10.md`)
says a best language "can pick out any meaning without context, and lets
context take over whenever it's available". A first review found Apu Pi We
strong on the first half and weak on the second.

## Setup

1. A fresh agent, told nothing about the hypothesis, writes a natural casual
   conversation between friends (`source.txt`).
2. A second fresh agent, also blind to the hypothesis, translates it strictly
   by `docs/language.md`, `data/grammar.tsv`, `data/lexicon.tsv` and
   `data/compounds.tsv` (`translation.md`). Missing vocabulary goes in
   [brackets] and isn't counted.
3. Claude tallies, using only the categories below.

## Counting rules (fixed in advance)

**Forced by Apu Pi We, left to context by English (F):**
- F1: a subject or object stated where the English omitted it.
- F2: a name or noun repeated where English used a pronoun, because the
  wan/yi rule wouldn't reach.
- F3: the name article **en**.
- F4: any other word a rule requires that carries something English left
  to context.

**Forced by English, left out by Apu Pi We (R):**
- R1: tense marking on a verb where Apu Pi We leaves time unmarked.
- R2: articles (the/a) and plural marking with no Apu Pi We counterpart.
- R3: gender in pronouns.
- R4: any other obligatory English marking with no counterpart.

**Not counted:** speech-act particles (English marks the same thing with word
order or intonation, so it's a different encoding, not context), bracketed
missing words, and translation errors (listed separately).

**Also measured:** total syllables in each language, per line and overall.

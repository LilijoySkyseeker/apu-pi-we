# Comma test 01: what breaks when commas are dropped?

Written 2026-10-10 before running. Principle (user): there should be a precise,
unambiguous way to say something, not that it must always be used. So the
question isn't "are commas required" but "which comma-carried distinctions
break in chat-style text, where commas (and voice typing's missing commas)
can't be relied on".

## Texts (existing translations, updated to current rules)

1. Economy test 01 v2: casual English chat.
2. Multilang stage 2 English: persuasive narrative.
3. Retest Hindi–Urdu: hierarchical narrative with many clauses.

Updated to current rules before use: **lon** → **to** "I", **to** "rather" →
**tason**, confidence tenths → sixths (7→4, 8→5, 9→5, 5→3, 10→6).

## Design (A/B)

For each text, two fresh back-translators, prompted in the source's
language, with the current grammar:
- **A:** the text with commas, one sentence per line.
- **B:** the same text with every comma removed and no final full stops, one
  message per line (chat style).

A judge compares source, A and B line by line and lists every line where B's
reading differs from A's because a comma was missing, classified as: address
at the start, address at the end, stance word at the end, topic opener, fronted
clause, recipient/long object, subject with a clause, other.

Before running, Claude counts the comma uses per category in each text, so
exposure is known.

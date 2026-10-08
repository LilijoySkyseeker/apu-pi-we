# Name recognition test 01

**Question:**
- Can people recover real names after adaptation into the language's sounds?
- For broken-up consonants, is an added vowel that copies a nearby vowel ("echo") or a fixed **u** ("default") easier to see through? The literature has no comparison (`research/notes/names-and-loans.md`).

**Method:**
- 44 well-known first names and places, from 20+ languages, adapted by `tools/names.py`.
- Two blind readers each got the adaptation rules and one version, and guessed the original names.
- Scored by Claude from the side-by-side lists.

**Result:**
- **Echo: 42/44.** Missed Björk (*beyeleke*) and João (*suwanwa*).
- **Fixed u: about 43.5/44.** Got both of those; Wojciech was given as its diminutive Wojtek (half credit).
- **None of the 44 adapted names sounds like an existing word.** Added vowels make most names longer than roots.

**Decision:** the added vowel is always **u**. A fixed vowel marks itself as "not in the original", so the listener can strip it. This is the Japanese practice. Names also get a minimum of two syllables (Ben → *BEnu*). And names take the article **en** (`docs/language.md`), so a name that does collide with a word is still unambiguous.

**Caveats:**
- The readers are AI models with wide knowledge of world names. Human recognition would be lower.
- One reader per version.
- I scored it myself, not a separate judge. The calls were all clear-cut except Wojtek.

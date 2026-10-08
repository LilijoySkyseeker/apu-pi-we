# Back-translation test 01: analysis

**Setup (2026-10-08):**
- A fresh agent got only `docs/language.md`, `grammar.tsv` and `lexicon.tsv` as they stood after the first-principles review, plus the language text of stress tests 001 and 002 with glosses and English removed (`source.txt`). It translated the text back into English (`backtranslation.md`).
- A second fresh agent scored each of the 32 segments against the original English (`reference.txt`) for content and for force/tone, from 0 to 2 (`scores.md`).

## Result

- **Content: 55/64 (86%).**
- **Force and tone: 58/64 (91%).**
- No segment lost its core meaning, and 14 of 32 lost at least one point.
- Who did what to whom, negation, the speech acts and the sarcasm marker all came through.

## Where the 15 lost points came from

| Cause | Points | Segments |
|---|---|---|
| **Vocabulary gaps** in the original translation (no word for offend, disgust, panic, system, react, retreat) | 6 | B3, B11, B20, B22, B23, B25 |
| **Translator's choice:** the commander was never introduced as a woman, so the ungendered **lu** became "he" | 3 (shared with the row above) | B8, B11, B22 |
| **One curse word** flattens three kinds of profanity | 3 | A3, A4, B25 |
| **Grammar:** a repeated pronoun can't mark a reflexive when the subject is a noun | 1 | B18 |
| **Register:** deadpan comedy, a breathless fragment | 2 | A2, B10 |
| **Reader's English bias:** an in-place question word rendered as English incredulity ("say *what*?") | 1 | B4 |

Two scores are arguable. In A2 the reader's "you need a little stick knowledge so you can know first it isn't your daughter" looks to me like the original's logic, not its reversal. In B4 the language did its job; the English rendering added the incredulity. I'm keeping the judge's scores as given.

So the grammar itself cost about one point. Most losses came from a small vocabulary and from choices made while translating into the language.

## What the reader found missing from the reference

All of these are now fixed in `docs/language.md`:
- word roles come from position
- verb + verb: object versus manner
- **Avu** "do" versus "make"
- the uses of **la**
- prepositions taking clauses
- **fi** alone
- scene-setting phrases first
- degree words before what they modify
- order of two objects
- importance, not animacy, decides **lu**/**tan**
- narrative time set once
- quotes and dashes in writing
- how the curse word behaves
- gender as a modifier
- a reflexive word **ku**
- a list of established compounds

The reader also caught two mistakes of mine in text 002: **ZUvo u** for **u ZUvo**, and an indirect question missing **yo**.

## How much to trust this

- **The reader and the judge are both AI models, not human learners.** Models are good at guessing from context, so a human learner would probably lose more.
- **Leak:** several test phrases appeared as examples in `language.md` ("alien", "step zero", "meditate"). The reader said those readings depended on the examples. Future tests should use texts whose phrases aren't in the reference.
- **Small sample:** 32 segments from two texts.

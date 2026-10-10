# Economy test 01: analysis

Method fixed in advance: `method.md`. Source written blind by one agent,
translated blind by another (`translation.md`), tallied by Claude.

## Totals

- **Syllables:** English ~284, Apu Pi We ~436, ratio **~1.5**. The English
  count is a heuristic, roughly ±5%. English fillers the translation dropped
  ("honestly", "by the way", "uh", "ha"...) are about 16 syllables, which
  flatters Apu Pi We slightly.
- **Speaking time:** CV-syllable languages are spoken faster (Japanese and
  Spanish ~7.8 syllables/s against English ~6.2; Pellegrino et al. 2011). If
  Apu Pi We behaves like them, the time cost is closer to **~1.2×** than 1.5×.
  That's an estimate; nobody has spoken it at speed.

## Where the extra syllables come from (rough)

| Share | Cause | Design or temporary? |
|---|---|---|
| ~40% | Everyday words with no root, built as phrases: landlord, neighbour, pipes, flooded, cheaper, rent, texted, park, driveway, block, yelled | Temporary. The seed lexicon is 453 roots; the language's own rule promotes frequent phrases to roots |
| ~30% | Base word length: every content word is 2+ syllables where English uses one (time, house, come, know, car) | Design |
| ~23% | Forced by the rules where English left it to context (F, below) | Design |
| ~9% | Times and days: 24-hour digit reading ("seven" → **fi mape po po**), weekday as "day of 6" | Design |

## Forced vs left out (counts, per method.md)

**Apu Pi We forced, English left to context: 18 items (+2 at no cost).**
- F1, subject or object added (6): "what time again?" became a full clause
  with **din obu**; "clean" needed an object (**guyi**); "Mine" became the
  full echoed phrase; **me** with **fon**, since rule 11 doesn't let advice
  drop its subject; "maybe after" became **sun obu wo doku**; "See you
  Saturday" needs **lon**.
- F2, a noun where English used a pronoun (7): **batu ben**, **batu**,
  **musu kige**, **waka**, the dip named twice, the neighbour named twice.
- F3, **en** (4).
- F4 (1): "after" needs an object (**wo doku** "after working").
- No cost: **pen**/**din** forced the inclusive/exclusive choice twice; it
  changes the word, not the length.

**English forced, Apu Pi We left out: ~32 items.**
- R1, tense (10). R2, articles and plurals (10). R3, gender in pronouns (12).
- R4, verb agreement (about 10), not tallied exactly.

**Reading:** Apu Pi We forces *fewer* things than English. But what it forces
is expensive (whole words and phrases), while what English forces is cheap
(endings, one-syllable words, a he/she choice that costs nothing).

## Findings, strongest first

1. **No pronoun for an event or a statement.** "Didn't *that* happen?",
   "*it* was bad", "I told him *that*": each needed a noun (**batu**
   "problem", **musu kige** "the same thing"). In casual talk people point at
   events and claims constantly. This gap isn't documented, and it isn't a
   context problem the rules chose; the slot is simply missing.
2. **bu "the most recent thing" misfires in conversation.** In casual talk,
   "it" means the *topic*, not the last thing mentioned. **bu** would have
   meant the house, the pipes, the water, the chips or the spinach. The dip was
   named twice.
3. **The wan/yi rule makes the speaker do bookkeeping.**
   - Marcus is **wan**, then **yi** once the landlord becomes a subject, then
     **wan** again.
   - The neighbour, mentioned but never a subject, had to be named in full
     twice (**no nume gelu**, 5 syllables for "he").
   - The translator said reference "cost the most thought". This is evidence
     for the drift prediction already on the watch list: **wan** drifting
     toward "the topic".
4. **No rule for fragments.** "What time again?", "Maybe after, like ten?"
   and "See you Saturday" are normal casual speech, but the rules only
   describe full clauses. So the translator rebuilt full clauses. Rule 11
   (subjects drop only after **yen**/**un** or in instructions and requests)
   is strict for casual talk.
5. **Vocabulary gaps dominate the raw cost, but they're the cheapest to
   fix**, and fixing them is already the language's process.

## Side findings

- `tools/names.py` prints Christopher → *kilisatafala*, but the doc's rule and
  example give **kulisutafalu**. The tool and the doc disagree.
- Translation losses (not counted): "bailed" became "can't", "weird about it"
  became "angry", fillers dropped.
- The translator's nine ambiguous-rule notes are at the end of
  `translation.md`.

## Limits

- One conversation, one AI translator. A fluent human might find shorter
  phrasings.
- The English syllable count is heuristic.
- The speaking-time estimate assumes Apu Pi We is spoken as fast as Japanese
  or Spanish, which is untested.

## Follow-up

- 2026-10-10: finding 1 fixed. **tan**/**ben** stand alone for events and
  statements (`docs/language.md` rule 6).
- 2026-10-10: finding 2 fixed. **bu** = the thing being talked about,
  resolved by context; **ben** alone = "that one".
- 2026-10-10: finding 3 fixed. **wan**/**yi** follow the topic, resolved by
  context.
- 2026-10-10: finding 4 fixed. Rule 11 now lets anything context supplies
  be left out, fragments included.

## Retest after the four fixes (2026-10-10)

Same source. A fresh agent translated it under the new rules
(`translation-v2.md`). Two more fresh agents back-translated v1 (with the
old `language.md`) and v2 (with the new one), never seeing the English
(`back-v1.md`, `back-v2.md`). A judge scored both against the source
without knowing which was which (`scores.md`).

| | v1 (old rules) | v2 (new rules) |
|---|---|---|
| Syllables | 436 | 385 (−12%) |
| Ratio to English (~284) | ~1.54 | ~1.36 |
| Meaning, blind judge | 42/44 | 44/44 |
| Reference errors | 0 | 0 |

- **Leak:** four of the new rule's examples are lines from this test (2, 12,
  17, 22). Excluding those lines, the saving is −10%.
- **Clarity held.** Every pronoun and left-out word in v2 was resolved
  correctly by a reader who had only the rules. v1's two lost points weren't
  reference problems (turn 8 "should" read as "has to"; turn 20 "block" lost).
- **Noise:** v1 and v2 had different translators. Some line-level swings are
  translator choices: turn 19 is +6, turn 20 is −11, partly from **tapi**
  "close" for "block". The direction is clear; the exact percentage isn't.
- **The rest of the gap** is the part these fixes didn't target: missing
  everyday words, the two-syllable minimum, and clock times.
- **New ambiguities the translator raised** (`translation-v2.md`): what
  counts as "nearer" for **tan**/**ben**; when a newly introduced person
  takes **wan**. Both were left loose on purpose (Restraint). Also: "ha"
  can't be written, since there is no h.

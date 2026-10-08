# Roadmap: what a full language needs

Written 2026-10-08, before going further, to catch anything that could force a change to the foundation.

## What "full" means here

A natural language took thousands of years and millions of speakers to build. A thought experiment can't enumerate 40,000 words. So "full" means **generative completeness**:

1. **Any text can be translated without inventing new grammar.**
2. **Any concept can be named by rule:** a core vocabulary, plus a derivation system and a borrowing system that can coin the rest predictably.
3. **The phonology can carry a lexicon of natural-language size** (tens of thousands of words) at a natural speaking pace without becoming confusable.

Rough targets, from memory and to verify:
- A 20-year-old English speaker knows about 42,000 lemmas (Brysbaert et al. 2016).
- About 2,000–3,000 word families cover around 95% of conversation (Nation).

So the target is a core of about 2,000–3,000 roots, plus rules that generate everything else.

## A. Could change the foundation: settle these before building more

| # | Challenge | Why it might change the foundation | Cheap check |
|---|---|---|---|
| A1 | **Lexicon at scale.** Can 15 consonants, 5 vowels and (C)V(n) syllables carry ~3,000 roots plus compounds? | If two-syllable space runs out, roots go to three syllables and the language gets slower. Might argue for more sounds or more syllable types. | Run the optimizer up to 3,000 synthetic roots; measure length, confusability and information per second. |
| A2 | **Derivation system.** How are leader, teacher, library, tool, -ness, un- made? | Everything is currently built from free compounds, which are long (**NIte GOni** is 4 syllables) and opaque (the blind reader couldn't decode "person sky" = alien). A systematic set of heads or derivation particles shapes the whole lexicon. | Design the pattern; test it by coining 100 modern words and back-translating them blind. |
| A3 | **Numbers.** Digits are 2 syllables each. | Modern life is number-heavy: phone numbers, prices, dates, measurements. A 10-digit phone number is 20 syllables. One-syllable digits may now fit, since the syllable split is gone. | Rerun the confusion model on 1-syllable digit sets; compare length and robustness. |
| A4 | **Names and international vocabulary.** | Modern Earth has billions of personal names, places, brands, species and chemical names. (C)V(n) syllables distort them heavily ("Christopher" → something like *kurisutofa*). Many languages keep a looser loan phonology for names. | Adapt 50 real names from many languages; judge recognisability; decide whether names get extra sounds or codas. |
| A5 | **Prosody: focus and fast speech.** | Stress is fixed, so English-style contrastive stress ("*I* didn't take it") is unavailable; focus needs another device (pitch, a particle, or word order). Fast speech also reduces unstressed syllables, and the unstressed grammar words (**vun**, **van**, **vin**…) could merge if their vowels reduce. May require "syllable-timed, no vowel reduction" or more distinct grammar words. | Specify focus; rerun the confusion model with vowels made more confusable in unstressed position. |
| A6 | **Politeness and social register.** | Every society softens requests and marks respect. The research found that when a language gives politeness no channel of its own, people repurpose hedges, evidentials and question forms for it, which would corrupt the confidence and speech-act systems. A dedicated channel protects them. | Design a small politeness or deference system; test that it doesn't overlap the confidence and speech-act markers. |
| A7 | **Deep embedding.** | Relative clauses have no end marker, so "heavy goes last" is the only defense. Legal, scientific and technical prose nests clauses that can't all go last. May need a clause-closing particle. | Translate a dense legal or scientific paragraph; see whether "heavy last" holds. |

## B. Big, but buildable on the current foundation

- **B1. Core vocabulary to ~2,000–3,000 roots,** chosen from cross-linguistic concept and frequency data (e.g. Concepticon), not English intuition. Includes modern domains: machines, computing, medicine, money, law, science.
- **B2. Grammar not yet designed:**
  - comparison ("than", superlatives)
  - conditionals and counterfactuals ("if … would have …")
  - modality: obligation and ability must stay separate from the confidence numbers
  - alternative questions ("tea or coffee?")
  - inclusive vs exclusive "or"
  - quantity: approximation, ranges, fractions, decimals, percentages, units, dates, clock time
- **B3. Concepts that differ across cultures,** built compositionally so no culture's carving is forced on others:
  - kinship (maternal vs paternal uncle = "mother's brother" vs "father's brother")
  - colour terms
  - spatial frames: left/right and north/south both available
- **B4. Conversation routines:** greetings, thanks, leave-taking, address terms, turn-taking, backchannels.
- **B5. Writing system:** script choice, numerals, punctuation, how names are written (original spelling vs adapted).
- **B6. Art and play:** poetry (fixed stress makes meter easy; five vowels make rhyme abundant), puns, song. Deliberately unambiguous languages lose wordplay; this one keeps harmless ambiguity, so it shouldn't.

## C. How we know it works

- **C1. Fresh, unleaked back-translation tests** across genres (conversation, instructions, story, technical, legal), rerun after changes as a regression check.
- **C2. Real people:** the user reading aloud is the only human data so far. Pronounceability and listening tests with humans would replace the model's guesses.
- **C3. A grammar checker,** optional. A small parser that flags rule violations would have caught the translator's own mistakes (**ZUvo u**, a missing **yo**). Build it only if hand-checking keeps failing.

## D. Thought-experiment questions: interesting, not blocking

- **D1. Change over time.** A native language changes: grammar words erode, numbers in the confidence system cluster, obviation might weaken. Which features are stable under transmission? Iterated-learning research (Kirby and others) is the relevant evidence.
- **D2. Dialects.** Eight billion speakers would split into dialects. What in the design slows divergence?
- **D3. Acquisition.** Are any features unlearnable for children? Obviation, logophors and numeric confidence are learned late, but late isn't never.

## Recommended order

A1 → A3 → A5 → A2 → A4 → A6 → A7, then B and C together. D runs alongside, whenever it's interesting.

A1, A3 and A5 are cheap checks with the existing tools, and they test the sound system everything else sits on. A2 and A4 decide how the vocabulary grows. A6 and A7 are grammar additions best tested by targeted texts.

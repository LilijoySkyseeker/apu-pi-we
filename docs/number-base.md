# Number base: why 6 (superseded)

> **Superseded 2026-10-09.** The author ruled that base 10 stays the default in reality, and the language switched to base 10 (`language.md`, rule 10). This file records the base-6 decision and its evidence. Its transmission result still explains why digits 0–5 are one optimized syllable each; 6–9 got two syllables because no robust one-syllable forms were left. *(2026-10-12: the test's figures were for ideal sets, not the adopted digits; see the correction under the table.)*

Decided 2026-10-08. The author chose premise 2: legacy conventions, including the decimal world, are void, as they already were for every other part of the language. So the base was chosen on merits. Evidence: `research/notes/base-cognition.md`, `base-mathematics.md`, `base-typology.md`, plus the transmission test below (`tools/base_test.py` (removed 2026-10-09 as single-use; in git history)).

## The deciding test: transmission through noise

For each base, the optimizer found the best set of one-syllable digit words under the language's sound rules. Then it estimated how likely a number is to be heard with a wrong digit. This is the error that silently changes a value, measured at −6 dB with the Miller & Nicely data.

| Base | P(a digit heard as another digit) | 10-digit-ID equivalent: digits | P(at least one wrong digit) |
|---|---|---|---|
| 6 | 0.0002 | 13 | 0.26% |
| 8 | 0.0015 | 12 | 1.8% |
| 10 | 0.0024 | 10 | 2.3% |
| 12 | 0.0044 | 10 | 4.3% |

With only six digit words, each can be made very different from the others. That more than pays for the 29% more digits base 6 needs. Two-syllable digits are near zero in every base, but they double the length. Base 6 gets near-two-syllable reliability at one syllable per digit. So the language drops the long/short digit forms: each digit has a single one-syllable word.

**Senary's own digit scheme** (one vowel for all digits; the consonant carries the digit) scored 0.087, about 400 times worse than the optimized set. Distinctions carried by consonant alone are fragile. So the language takes senary's base and structure but not its digit sounds.

**Correction 2026-10-12 (review: fact-check internal-test table, defence, verdict "re-run or withdraw").** Rerun of `base_test.py` (from git `a3071f4`) with today's `confusion.py` and `build.Inventory`, both unchanged since then; scratch scripts outside the repo.
- **The table reproduces exactly** (base 6: 0.00020 per digit, 0.26% per 10-digit ID; base 10: 0.00235, 2.3%). The model didn't change.
- **But it scored ideal, unconstrained sets** (base 6: **ma ku ga li fe bu**), not the digits the language took. **ku**, **li**, **bu** were already grammar words. The adopted 0–5 came from `build.py numbers3`, which also excluded grammar-word forms and their drift keys, penalised closeness to grammar words, and required distinct first consonants and drift keys.
- **Adopted 0–5 (po fi sa ka da te): 0.0185 per digit** (0.0187 renormalised over the inventory), about 90× the published 0.0002 and 8× the ideal ten-digit set the test rejected. This is the defence's 0.0185. Worst pairs: ka→sa 0.028, sa→ka 0.021, po→ka 0.011, sa→da 0.011, ka→te 0.010.
- **Today's 0–9 (po fi sa ka da te ufo oma kefi mape): 0.011 per digit, ≈10.6% chance of at least one wrong digit in a 10-digit ID**, if digits are equally frequent. 6–9 are ≈0 against each other. A one-syllable digit heard as a two-syllable one (or a lost syllable) isn't modelled at all, so 6–9's real risk is unmeasured.
- Senary's scheme (0.087, figure not re-run) is then about 5× the adopted set, not 400×.
- So "0–5 kept their optimised forms" (header) and "six one-syllable digits far more robust than ten" don't describe the language's digits. The comparison would need each base re-run under the same grammar-word constraints; not done, since base 6 is superseded. All figures are from the unvalidated model (rationale §3.2): relative at best, and a human listening test outranks them.

**Caveat:** this is the confusion model's own estimate. It doesn't simulate a noise burst deleting a whole syllable, so digit strings are read in fixed groups of four, which makes a missing digit noticeable.

## Everything else

| Factor | Favours | Strength |
|---|---|---|
| Transmission (above) | 6 | strong in the model |
| Facts to memorise: multiplication 10 / 36 / 55 for bases 6 / 10 / 12 | 6 | moderate: learning depends on the number of items (Logan & Klapp 1991) |
| Fractions: ½, ⅓, ¼, ⅙ exact | 6 and 12 tie; 10 loses ⅓ | strong (arithmetic) |
| Divisibility tests | 6 (easy tests up to 10) | moderate |
| Number length: digits are 1.29× decimal | 10, 12 | strong |
| Precision: two digits = per-36 (2.8% steps) vs per-100 | 10, 12 | strong; base 6 uses three digits (per-216) where decimal uses two |
| Working memory: span ≈ what fits in ~2 s of speech | short words beat small bases | moderate. One-syllable digits keep base 6 near decimal-with-two-syllable-digits. |
| Regular number words help children | none: it's about regularity, not base | strong; the language is fully regular |
| Fingers | 10 weakly; one hand = 0–5 fits 6 | weak |
| Large-scale precedent | none: no large society ever used 6 or 12 for everything | it's a thought experiment, so noted, not decisive |

## Base 12, the runner-up

Base 12 has the best fractions and the shortest numbers. But 12 one-syllable digits are much more confusable (4.3% per ID), and two-syllable digits would make its numbers longer than base 6's. It also has the largest table to learn.

## Drift notes for base 6

- Frequent numbers from 6 to 35 are compounds ("six one"), so they are where fusion and irregularity would start (`research/notes/base-typology.md`). The juncture rules and stressed place words keep the joints audible.
- Speakers will want a quick everyday counting form, as Komnzo shows. The one-syllable digits are already that form.
- Under premise 2 there is no contact language with another base, which is the main documented cause of base change.

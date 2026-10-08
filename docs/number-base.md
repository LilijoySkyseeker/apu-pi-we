# Number base: why 6

Decided 2026-10-08. The user chose premise 2: legacy conventions, including the decimal world, are void, as they already were for every other part of the language. So the base was chosen on merits. Evidence: `research/notes/base-cognition.md`, `base-mathematics.md`, `base-typology.md`, plus the transmission test below (`tools/base_test.py`).

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

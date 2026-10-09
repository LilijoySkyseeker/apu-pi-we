# Measurement

The language's measurement system is the senary system, carried over on 2026-10-08 at the user's request ("it's strong as is").

## How the two repos divide the work

| Repo | Owns | Source of truth |
|---|---|---|
| `~/work/repos/senary` | the quantities: unit definitions, exact values, constants, the calendar's arithmetic | `src/senary_tables.py` |
| this repo | the words: unit names, number words, how measurements are said | `data/units.tsv`, `data/numbers.tsv`, this file |

Neither repo copies the other's job. If senary changes a definition, nothing here changes unless a unit is added or removed. If this repo renames a word, senary's numbers are unaffected. Senary's own words (Kena, Nira…) were declared placeholders in its README; this language's words replace them in speech.

## Unit words

Each senary name was kept only if, after adapting sounds the language lacks (r → l, v → w, z → s), it was no more confusable than the 90th percentile of ordinary words, and passed the drift and juncture rules. One name survived: *Wela*. The rest were re-picked by the optimizer. The worst original was *fuka* "pressure", about 270 times as confusable as a typical word, mostly with *futa* "woman". Built by `tools/units.py` (removed 2026-10-09 as single-use; in git history).

| Quantity | Word | Senary name | Size |
|---|---|---|---|
| time | **nane** | Kena | 0.3086 s (a day is 6⁷ of them) |
| length | **ano** | Nira | 1.530 m |
| mass | **fomi** | Woba | 1.513 kg |
| charge | **yoke** | Vema | 0.7592 C |
| temperature interval | **sigi** | Buda | 2.031 K |
| angle | **meno** | Faga | 1 turn |
| frequency | **kanwi** | Beva | 1 cycle per Kena (3.24 Hz) |
| force | **sandu** | Wida | 24.30 N |
| pressure | **ogen** | Fuka | 10.38 Pa |
| energy | **kisu** | Koda | 37.19 J |
| power | **geye** | Noza | 120.5 W |
| voltage | **kewen** | Kiwa | 48.99 V |
| resistance | **gansu** | Nawa | 19.92 Ω |
| capacitance | **wela** | Wela | 0.01550 F |
| inductance | **kokan** | Fiba | 6.147 H |
| magnetic flux density | **sobon** | Bora | 6.457 T |
| temperature scale | **tilo** | Vona | reading = T/Buda − 134.5 |
| information | **noyon** | Vuta | one senary digit (ln 6 natural units) |
| count of entities | **senan** | Kuza | 6³⁴ entities (the mole's role) |
| particle mass | **masin** | Neta | 6⁻³⁴ of the mass unit |

Unnamed quantities are compounds of unit words, following the usual head-first rule: velocity = length per time.

## Saying a measurement

The unit comes first and the number follows, like any counted noun:
- **ano te** = 5 length units.
- **fomi sa nobi** = 2·6 = 12 mass units.

**Scale words are number words.** There are no separate prefixes:
- 6⁴ **yiyo**, 6⁸ **gife**, 6¹² **yuli**
- 6⁻⁴ **kufe**, 6⁻⁸ **bafo**

So **ano te yiyo** = 5 × 1296 length units (about 9.9 km). This is senary's 6⁴ ladder, said with this language's words.

Beyond those, **unun** "power" + exponent: **ano te unun guti nobi** = 5 × 6⁻⁶ length units.

## Protecting against plausible wrong values

A misheard digit gives a wrong number. A misheard *scale* word gives a wrong number of the right shape, off by 6⁴ or more, which is the error most likely to go unnoticed (senary's error-size principle). So each down-scale word was built as an "antonym" of its up-scale partner (**yiyo** / **kufe**, **gife** / **bafo**), which gives those pairs the strongest confusion weighting the optimizer has.

## Time and calendar

**Provisional.** The user is reworking senary's calendar and timing (2026-10-08), which are currently anchored to Earth's day and year, in a separate session. Everything in this section follows senary as it stood at r19. Nothing else in the language should build on it until the rework lands; then re-read `src/senary_tables.py` and update the words here.

- The day is 6⁷ **nane**. Time of day is said as the fraction of the day, digit by digit after the point: **mon mimi ka da ka** "at .343 of the day" = 15:00. Each further digit is six times finer, and seven digits give the exact time unit.
- **aya** "watch" = 6⁶ nane = a sixth of a day (4 h), for everyday durations.
- Leap years follow senary's 314/1296 accumulator rule (see `src/senary_tables.py`, `is_leap`).
- **Not designed yet:** a week (6 days would be the natural choice) and month names.

## Not carried over

- **Senary's spoken numerals** (consonant = digit, vowel = role) tested about 400× more confusable than this language's digits (`docs/number-base.md`).
- **Its unit names**, for the reasons above.
- **Its process machinery** (generated specification, mutation tests). That stays in the senary repo, where the arithmetic lives.

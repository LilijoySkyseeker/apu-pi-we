# Senary vocabulary

Apu Pi We's own numbers are base 10, and everyday measurement uses today's units with borrowed names (`language.md`, rules 9–10). Since 2026-10-09 senary is a topic the language can talk about, for the user's worldbuilding among other things, not a system built into it (user's ruling). This file holds the words for it. From 2026-10-08 to 2026-10-09 senary was the language's own measurement system; the sections below were written then and still describe how senary is said.

**Numbers in this file are senary.** In speech, put **senali** before a senary number whenever it isn't obvious (**senali sa po** = 20₆ = 12). The base-6 place and scale words (**nobi** 6, **miko** 36, **niyu** 216, **yiyo** 6⁴ …) are used only for senary.

## How the two repos divide the work

| Repo | Owns | Source of truth |
|---|---|---|
| `~/work/repos/senary` | the quantities: unit definitions, exact values, constants, the calendar's arithmetic | `src/senary_tables.py` |
| this repo | the words: unit names, number words, how measurements are said | `data/units.tsv`, `data/numbers.tsv`, this file |

Neither repo copies the other's job. If senary changes a definition, nothing here changes unless a unit is added or removed. If this repo renames a word, senary's numbers are unaffected. Since senary r22 (2026-10-09) senary itself uses this language's words for every unit and prefix, and derives its written symbols from them (first two letters: **ano** → An; **sigi** takes Sg so it can't be read as SI). Its old working labels (Kena, Nira…) survive only in its pre-r22 history.

## Unit words

Each senary name was kept only if, after adapting sounds the language lacks (r → l, v → w, z → s), it was no more confusable than the 90th percentile of ordinary words, and passed the drift and juncture rules. One name survived: *Wela*. The rest were re-picked by the optimizer. The worst original was *fuka* "pressure", about 270 times as confusable as a typical word, mostly with *futa* "woman". Built by `tools/units.py` (removed 2026-10-09 as single-use; in git history).

| Quantity | Word | Senary's working label before r22 | Size |
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
- **fomi sa nobi** = 2·6 = 12 mass units (senary place words).

**Scale words are number words.** There are no separate prefixes:
- 6⁴ **yiyo**, 6⁸ **gife**, 6¹² **yuli**
- 6⁻⁴ **kufe**, 6⁻⁸ **bafo**, 6⁻¹² **genwi** (coined 2026-10-09 so the set is symmetric)

So **ano te yiyo** = 5 × 1296 length units (about 9.9 km). Senary writes the same words as prefixes: yiyoAn.

**One generative rule, six shortcuts.** Any power at all is **unun** "power" + exponent: **ano te unun guti nobi** = 5 × 6⁻⁶ length units. The six scale words are shortcuts for the range where a wrong scale still looks believable; past 6^±12 a slip is absurd and gets noticed, so the plain rule is enough there (senary writes 6ⁿ). This replaced senary's generative prefix ladder in r22, agreed with the user on 2026-10-09: it needed no second set of digits, and direction is carried by a whole word instead of one vowel. Add more named steps if 6^±16 to 6^±24 keep coming up.

## Protecting against plausible wrong values

A misheard digit gives a wrong number. A misheard *scale* word gives a wrong number of the right shape, off by 6⁴ or more, which is the error most likely to go unnoticed (senary's error-size principle). So each down-scale word was built as an "antonym" of its up-scale partner (**yiyo** / **kufe**, **gife** / **bafo**, **yuli** / **genwi**), which gives those pairs the strongest confusion weighting the optimizer has.

## Time and calendar

Senary's r20/r21 rework (2026-10-09) supplies the concepts: one continuous count of standard days from an epoch, local time as a view of it, an Earth calendar whose date is the number of days elapsed in the year, body time for anything about a body. Senary owns the arithmetic (`src/senary_tables.py`, Specification §11). The words below are this repo's alone; senary's names (Bana and the rest) are not used.

**The one idea speakers need:** every time point is an *amount elapsed* since the start of the thing that contains it. The clock is the part of the day that has passed; the date is the days of the year that have passed; the year is the years since year 0. So all three are said with the label rule (noun + **pi** + digits, digit reading), and a zero is a real value: the first day of the year is **dili pi po po po po**.

| Concept | Said | Notes |
|---|---|---|
| day (standard or local) | **dili** | one word; on Earth they are the same length to 1 part in 10⁸ |
| clock time | **mon mimi ka da ka** "at .343" = 15:00 | the fraction of the day; speakers give as many digits as they need |
| date | **dili pi po te ka sa** "day 0532" | always four digits, zeros kept; first two digits are the block |
| date and clock together | **dili pi po te ka sa mimi da** "day 0532.4" | the clock *is* the fraction of the date, so it is one number |
| year | **fawu pi fi ka ka** "year 133" | counted from the Moon-landing year; year 133 began March 2026 |
| week | **nelon** (new root) | six local days; which are for rest is local custom |
| day of the week | **dili pi ka** "day 3" | one digit, 0–5; a date always has four, so the two can't be confused |
| block | **boyo** (new root) | 36 days, the first two digits of the date: **boyo pi te** "block 05" |
| watch | **aya** | 6⁶ nane, a sixth of a day (4 h); **aya pi ka** = the watch from noon to 16:00 |
| leap year | **fawu netu** "long year" | senary's 314/1296 rule |
| local time / local day | **muyi pi kemu** / **dili pi kemu** "time / day of the place" | the default; nobody says it unless comparing places |
| the count | **sunbu pi muyi** "the count of time" | for records and machines; rarely spoken |
| body time | **muyi pi gawo** "time of the body" | |
| age | **nume** "live" + a duration: **lon nume fawu te nobi** "I have lived 30 years" | an age *is* lived body time, which is what the verb says |
| seasons | **muyi** + quality: **muyi tikun** "hot time", **muyi weki** "cold time", **muyi pi gegi** "time of rain" | local, as senary says; each place names its own |

**Relative time** uses the existing anchor-plus-offset rule; with no anchor, the anchor is now: **wo nelon fi** "after one week" = next week, **ya boyo fi** "a block ago", **nelon tan** "this week".

**Durations** are counts of any unit: **nin aya sa** "for two watches", **nane yiyo te** "5 × 6⁴ nane" (about 33 minutes), **dili nobi fi** "seven days".

**Why two new roots and no more.** *Week* and *block* name calendar-aligned periods that modern life is organised around (rest days, rent, wages, billing), and every language that has such periods has a short word for them. A phrase like **dili nobi** "six days" can't say "this week" as opposed to "the next six days". Everything else is a phrase built from existing words.

**Deliberately without words** (concept is senary's; add a word if texts keep needing it): the epoch (say "year 0" or describe the Moon landing), the zero meridian, the traveller's view, solar longitude, lunar month (there is none; the Moon's phase is just **dunan**'s look). Body time and the count are phrases, and stay phrases unless they turn out to be frequent.

## Not carried over

- **Senary's spoken numerals** (consonant = digit, vowel = role) tested about 400× more confusable than this language's digits (`docs/number-base.md`).
- **Its unit names and prefix ladder**, for the reasons above. Senary now uses this language's words instead.
- **Its process machinery** (generated specification, mutation tests). That stays in the senary repo, where the arithmetic lives.

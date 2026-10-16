# Regional balance of the vocabulary decisions (balance-01)

A one-off count, decided by the author 2026-10-15 (Globasa review row 8, `research/notes/globasa.md` item 10; goal N3 "don't weight cultures by size", C1 "fair to every culture"). This file counts and doesn't judge. A separate reviewer does the interpretation. My own reading is kept apart in the last section.

## Question

Did any region of the 20-language panel win the vocabulary decisions more often than its share of the panel? The decisions checked are which loans passed, which boundaries were drawn and which concepts made the ~1,500 list.

Regions as in `tests/coverage-01/part3/loanwork/emit.py`: EA (zh ja ko), SEA (vi th id tl), SA (hi bn ta), WA (fa ar tr), EU (ru es fr), SSA (sw ha yo), AM (qu). English is not a panel language. A region's panel share is its languages / 20: SEA 0.20, AM 0.05, the other five 0.15 each.

## Method

Everything comes from files already in the repo; nothing new was collected. `balance.py` does all the counting and writes the TSVs next to this file:

```
direnv exec /home/agent/work/repos/universal-language python3 tests/balance-01/balance.py
```

It runs in about 4 s.

### 1. Loans

- **Columns:** the hand panel files `coverage-01/part3/loanwork/c01–c11.txt` (109 coverage candidates) and `older.txt` (14 older lexicon loans re-run), parsed with `emit.parse`, plus `verified.tsv`.
- **What counts as a column:** a column counts when it is marked y or b and is not a memory-only column that `verified.tsv` rejects. This is `deciding.py`'s with-memory count, which is the count `loans-final.tsv` and `loans-rerun.tsv` report.
- **Two-shape rule:** for sauce (salsa form) and channel (kanal form), the other shape's columns are dropped. `loans-final.tsv` records this only as a note, so the columns come from each entry's text.
- **Check:** all 123 recomputed counts match the recorded count/regions (`loans-check.tsv`). For sauce and channel the recorded figure is the pre-rule count, and the rule's result (12, 7) matches the note.
- **Passing:** the recorded final verdict. That is `loans-final.tsv` "pass…" or "loan as a currency only" (pound), giving 63, and `loans-rerun.tsv` "pass", giving 8. The total is **71 panel loans**. mile, pope and mosque pass the count but were decided otherwise, so they are left out of both the passing and the failing sets.
- **Other lexicon loans, counted apart:**
  - `.com` and hashtag come from `tests/symbols-01/panel.tsv`, using sourced columns as that test counts them. Both reproduce (14/6, 13/5).
  - The eight metric loans have no ✓/✗ panel file. kilometre uses the `tests/lexicon-ladder-01/loans.md` table (Wiktionary columns only). kilo uses the 12 languages named in the design log, 2026-10-13. For metre, centimetre, millimetre, gram, kilogram and litre I read `part3/metric-panel.txt` myself **(added)**: every listed form counts as cognate except Mandarin 米/克/升/毫米.
- **Per loan** (`loans-per-loan.tsv`): the counted columns per region. A region is **decisive** when removing all of its columns makes the loan fail (under 12 columns or under 4 regions).
- **Per region** (`loans-by-region.tsv`):
  - the region's share of all counted columns, against its panel share;
  - **columns per language slot**, which is its columns / (its languages × loans) and corrects for region size **(added)**;
  - how often it is decisive;
  - how often it has no column at all.

  The same counts are given for the 49 candidates that failed the count **(added)**.
- **Source of the adapted form** (`loans-median-positions.tsv`, `loans-median-by-region.tsv`): the panel records which languages backed each variant only in the entries' free text. Where an entry names the languages at a contested position (a vowel, a final consonant, a tie, or which shape or family was taken), I copied the languages whose variant the median took (won) and those whose variant lost **(added: my reading of the text; 47 of the 81 loans name languages)**. Entries that name only the losers count only as losses.

### 2. Boundaries

- **Decisions:** the 20 lump/split decisions the design log grounds in modern use. These are moon/month and word/language; "The remaining boundary cases" (protect/keep, ask/request, day/daytime, law/rule, need/should, power/strength, live/life, leg/foot, tree/wood, and the deleted 20–50% band's hear/listen, see/look, paper/book, land/country, take/get, arm/hand); and the religion entries (soul/spirit, ghost/spirit, devil/demon).
- **Not included:** the `ladder.tsv` split/merge rows. They are English-homonym splits (party, letter, match) and by-eye merges, not modern-use decisions. `pending-splits.md` only lists which uses wait for forms.
- **Per language:** `boundary.py`'s output isn't recorded except as design-log summaries, so `balance.py` re-runs its own functions unchanged on the coverage data. Each language comes out as one of:
  - **lump**: the top word for one meaning also carries the other;
  - **lump+sep**: it lumps, but a separate word reaches 10% of the lumped word's frequency, which is signal 3, separating in modern use;
  - **split**;
  - **no data**.
- **Whose pattern the decision followed** **(added)**:
  - A split follows the languages that split or lump+sep, and goes against those that only lump.
  - A lump follows the languages that lump.
  - live/life is left out of this tally **(added)**: its labels are a verb and a noun, so the script's "split" there is a word-class difference. The decision rests on any root taking any role, not on modern use.

### 3. The concept list

- **Shares:** per-language concept shares, recomputed exactly as `coverage-01/concepts.py build()` does but not written. Each language counts once, text and speech are averaged, and the final score is the median of log shares. Check: all top 4,000 scores in `concepts.tsv` are reproduced.
- **Region score:** the mean of its languages' log shares **(added)**.
- **Correlation** (`concepts-correlation.tsv`): Spearman correlation with the final score over the top 3,000 labels that aren't grammar, name or junk labels **(added: the cut)**. Three versions are given:
  - for the region's mean;
  - for each language;
  - for the final ranking recomputed without the region (lower = the region moves the ranking more).
- **Each region's own top 300 and top 1,000 content labels** (`concepts-region-top.tsv`) are sorted into four statuses:
  - **on the list:** a root today, in `part2b/roots-1500.txt` or in `part3/additions.tsv`;
  - **covered by a phrase:** per `merged.tsv`;
  - **content not on the list:** merged, uncovered, not chosen;
  - **below the merge cut:** the label never reached the merged top ~4,000.

  Many below-cut labels are multi-synonym gloss strings ("house, home") from the AI-glossed or thin-Wiktionary languages, which never match a canonical label. They are counted in their own column, and `share_missing_of_merged` leaves them out.
- **Children's first words:**
  - `wordbank-deep.tsv`: for the deep-layer concepts in `part3/wordbank-final.tsv`, the number of non-European Wordbank checklists that have them, from `part3/nonwestern/items.pkl`: EA = Mandarin, Cantonese, Japanese, Korean; WA = Persian, Turkish, Hebrew; SSA = Kiswahili, Kigiriama. The European count is the total in `wordbank.tsv` minus that.
  - `wordbank-nonwestern-by-region.tsv`: the 192 non-European-only items by checklist region and by whether Apupiwe has a word for them (column `apupiwe_now`).

## Results

### 1. Loans (71 passing panel loans)

| Region | langs | cognate columns | share (panel share) | columns per language slot | decisive | region absent |
|---|---|---|---|---|---|---|
| EA | 3 | 135 | 0.123 (0.15) | 0.63 | 13 | 8 |
| SEA | 4 | 219 | 0.199 (0.20) | 0.77 | 24 | 1 |
| SA | 3 | 187 | 0.170 (0.15) | 0.88 | 21 | 1 |
| WA | 3 | 189 | 0.172 (0.15) | 0.89 | 22 | 1 |
| EU | 3 | 197 | 0.179 (0.15) | **0.92** | 23 | **0** |
| SSA | 3 | 128 | 0.116 (0.15) | 0.60 | 10 | 12 |
| AM | 1 | 47 | 0.043 (0.05) | 0.66 | 3 | 24 |

- **All 81 lexicon-bound loans** (adding `.com`, hashtag and the eight metric units): the same order and almost the same figures. EU 0.93 per slot and never absent; SSA 0.60; EA 0.63.
- **Decisive:** 6 of the 71 sit at exactly 12 columns (lamp, tomato, sauce, design, restaurant, chemistry), and there every region with a column is decisive. The rest of the decisive counts are 4-region passes.
- **Absent regions:**
  - EA is absent from doctor, sugar, bank, machine, bomb, cigarette, chemistry and cinema (Sino forms).
  - SSA is absent from motorcycle, lamp, sauce, balcony, code, website, design, restaurant, vaccine, profile, medal and mask.
- **The 49 candidates that failed the count:** EU still has 0.83 columns per slot and is absent from 2. EA has 0.29 (absent from 27) and SSA 0.24 (absent from 24).

**Source of the adapted form** (contested positions in 47 loans; won/lost = language-positions):

| Region | won | lost | win rate | won per language |
|---|---|---|---|---|
| EA | 24 | 31 | 0.44 | 8.0 |
| SEA | 60 | 50 | 0.55 | 15.0 |
| SA | 47 | 49 | 0.49 | 15.7 |
| WA | 61 | 41 | **0.60** | 20.3 |
| EU | 64 | 42 | **0.60** | 21.3 |
| SSA | 27 | 35 | 0.44 | 9.0 |
| AM | 15 | 12 | 0.56 | 15.0 |

### 2. Boundaries (19 decisions with a modern-use reading; live/life left out)

| Region | language-decisions followed | against | no data | share followed |
|---|---|---|---|---|
| EA | 34 | 1 | 22 | 0.97 |
| SEA | 50 | 4 | 22 | 0.93 |
| SA | 19 | 1 | 37 | 0.95 |
| WA | 17 | **9** | 31 | **0.65** |
| EU | 39 | 3 | 15 | 0.93 |
| SSA | 22 | 5 | 30 | 0.81 |
| AM | 1 | 1 | 17 | 0.50 |

- **Lumpers the splits overrode** (`boundaries-per-decision.tsv`), each only lumping with no separate word:
  - fa: moon/month, day/daytime, hear/listen, take/get, arm/hand, ghost/spirit
  - tr: moon/month, day/daytime, leg/foot
  - tl: moon/month, day/daytime
  - sw: moon/month, tree/wood, arm/hand
  - ha and qu: moon/month
  - id: arm/hand
  - ru: arm/hand
  - vi: hear/listen
  - yo: law/rule
  - zh: ask/request
- **The two lump decisions:**
  - live/life: the script finds no language lumping, since the labels are a verb and a noun.
  - devil/demon: the script finds lumps in bn, zh and ko, but 15 languages have no data.
- **Data gaps:** WA, SA and SSA have the most no-data cells, so their shares rest on fewer readings.
- **Moon/month cross-check:** for moon/month the script's lump+sep set (ko th id hi ru yo) differs from the design log's hand reading (zh ko ja yo ru). The script's own docstring warns that its glosses are approximate.

### 3. The concept list

**Rank correlation with the final (median) score**, over the top 3,000 content labels:

| Region | region mean vs final | mean of its languages | per language | final without the region |
|---|---|---|---|---|
| EA | 0.862 | 0.745 | zh .77 ja .73 ko .73 | 0.920 |
| SEA | 0.865 | 0.694 | vi .62 th .74 id .71 tl .70 | 0.956 |
| SA | 0.815 | 0.624 | hi .69 bn .64 ta .54 | 0.968 |
| WA | 0.881 | 0.723 | fa .79 ar .63 tr .74 | 0.939 |
| EU | **0.897** | **0.795** | ru .70 es .83 fr .85 | **0.918** |
| SSA | 0.799 | 0.574 | sw .68 ha .63 yo .41 | 0.978 |
| AM | 0.457 | 0.457 | qu .46 | 0.990 |

**Each region's own top 1,000 content labels** (top 300 in `concepts-region-top.tsv`):

| Region | on list | phrase | content not on list | below merge cut (multi-synonym) | missing share of merged | not on list incl. below cut |
|---|---|---|---|---|---|---|
| EA | 853 | 13 | 79 | 55 (10) | 0.084 | 0.134 |
| SEA | 913 | 16 | 61 | 10 (1) | 0.062 | 0.071 |
| SA | 751 | 13 | 62 | 174 (130) | 0.075 | 0.236 |
| WA | 877 | 10 | 51 | 62 (41) | 0.054 | 0.113 |
| EU | 883 | 9 | 75 | 33 (12) | 0.078 | 0.108 |
| SSA | 711 | 12 | 64 | 213 (124) | 0.081 | 0.277 |
| AM | 400 | 6 | 45 | 549 (388) | 0.100 | 0.594 |

- **Top 300:** within the merged labels, between 0.3% (SSA) and 2.3% (EU) are missing; AM is 6.7%.
- **Examples** of each region's missing labels are in `concepts-region-top-missing-examples.tsv`:
  - EA: achievement, disaster, earthquake, baseball, staff;
  - SA: mango, bribe, plough, paddy, destiny;
  - SSA: wild animal, flour, census, theft, earring;
  - EU: month names, apartment, castle, concert;
  - WA: imam, martyr, menu.

**Children's first words.**

- **Deep-layer concepts (164 kept):** on average each one is on 80.5% of the 21 European checklists. It is on 79% of the 4 EA lists, 76% of the 3 WA lists and 71% of the 2 SSA lists. None of the 164 is on European lists alone.
- **Coverage gaps:** Wordbank has no checklist in a South Asian, South-East Asian or indigenous American language (its American lists are English and Spanish), and its Arabic file is unusable. 21 of its 30 languages are European.
- **Non-European-only items with no Apupiwe word** (as recorded in `wordbank-nonwestern.tsv`): 58 of 101 EA items, 41 of 77 WA items and 25 of 68 SSA items. An item can sit in more than one region.

## Limits

- **Loan candidates:** these were picked by an AI ladder pass over an English-glossed concept list (route "loan?"). Internationalisms that don't look like loans to an English reader never became candidates, so the loan counts measure who shares the candidates, not who shares loans in general.
- **Thin columns:** SSA's low loan figures partly reflect Hausa and Yoruba columns that stayed unsourced (`verified.tsv` "unknown"), not only words the languages lack. AM is one language.
- **Concept-list sources differ by language:**
  - wordfreq text: zh ja ko vi id tl hi bn ta fa ar tr ru es fr;
  - Leipzig web text: th sw ha yo qu;
  - subtitles added: 15 languages, but not tl sw ha yo qu;
  - AI glosses: th ha qu.

  Low correlations for SSA and AM can come from noisier data as well as from different concepts. The below-cut column is mostly gloss-format mismatch.
- **Boundary readings:** these use `boundary.py`'s automatic lump test, which the design log itself corrected by hand for moon/month. Many cells have no data.
- **Median positions:** these are my transcription of free text; a few entries (the circus blend, the motorcycle tie) are simplified to one position.

## Claude's reading

Short, and only mine; the reviewer decides.

- **Loans lean European in who supplies the votes, not in who decides.** Europe has a column in every passing loan, at 0.92 per slot against 0.60–0.66 for Africa, East Asia and Quechua. It also has 0.83 per slot even among the failures. Africa (SSA) and East Asia are the regions most often missing, both in passes and in fails.
- **The 4-region bar does its job.** It's what failed most Europe-shared candidates. Because of it, no region is decisive much more often than its size suggests.
- **The form's sound leans WA/EU at contested positions** (0.60 win rate against 0.44 for EA and SSA). That is mild, and the counts are small.
- **Boundaries:** the splits mostly went against Persian and Turkish lumps (fa 6, tr 3). Otherwise the decisions agree with nearly every language that has data. I see no single region being followed, but the no-data cells are many.
- **Concept list:** the median ranking tracks Europe slightly most (ρ 0.90 region, 0.80 per language). Europe and East Asia move it most when removed. Africa and Quechua track it least, partly through weaker data. Within the merged labels, each region's top concepts are about equally often missing (5–10%), so the list doesn't visibly drop one region's frequent concepts. The visible gaps are the ones Part 5 already found: home cooking and farming.
- **The deep layer** relies on Wordbank, which is 21/30 European and has no South Asian, South-East Asian or American checklist. That is the most clearly one-sided input in the pipeline, even though the 164 concepts it kept also appear on most of the few non-European lists.

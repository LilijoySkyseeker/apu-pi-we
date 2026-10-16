# Concept list extension by the stop rule (coverage-02)

Task: `PROMPT.md`. It applies the author's 2026-10-15 decisions ("How many roots: a stop rule, not a number" and the 51 agreed additions; `docs/design-log.md`). Proposals only: nothing outside this folder changed and nothing is committed. Choices of mine are marked **(added)**.

## Progress

- [x] 0 candidate table built (`candidates.py` → `candidates.tsv`)
- [x] 1 agreed additions classified (`additions.tsv`)
- [x] 2 walk classified (`src/walk-manual.tsv` → `walk.tsv`, via `assemble.py`)
- [x] 3 stop-rule table (below); calibration stretch (`calibration.tsv`, added)
- [x] 4 drop proposals for today's list (`drops.tsv`)
- [x] 5 README write-up

Rerun from the repo root (under a second each):

```
direnv exec . python3 tests/coverage-02/candidates.py   # needs tests/balance-02/concepts_fix.py inputs
direnv exec . python3 tests/coverage-02/assemble.py     # rebuilds walk.tsv, calibration.tsv; prints the table
```

## Method

- **Ranking.** `candidates.py` recomputes balance-02's corrected ranking (the head rule, `concepts_fix.py`, imported read-only) and ranks canonical content concepts by their best label, as balance-02 did (2,331 canonicals). For each one it records what today's list says: an existing root (`data/lexicon.tsv`, via the merge's cover field), `roots-1500.txt` (first-word or frequency segment), `additions.tsv`, the `ladder.tsv` status, `loans-final.tsv`, `religion.tsv`, the balance-02 entrant judgement, a listed phrase in `compounds.tsv`, or the merge's own cover.
- **The list edge.** The frequency segment of `roots-1500.txt` is the first 748 uncovered canonicals. Under the corrected ranking, the 748th is **priority, canonical rank 1242**. The walk starts at 1243.
- **Skips.** A concept is skipped (class `-` in `walk.tsv`) when it is on the list, has a root, is a listed phrase, or the merge covered it (resemble = **fun** "like"; burden = the agreed **load**).
- **Classes.** These are the prompt's G P L C N A. Two working criteria are mine **(added)**:
  - **P** means a phrase of at most two content words (plus grammar words, a derivation with **no/gen/du/pu**, or **su** negation) that a listener would read right without having learned it. A concept on the list but without a form yet is written in brackets: **[care]**.
  - **A** means the English label pools senses that are unrelated in most languages, so the rank isn't one concept's.
  - A row whose class could reasonably be G is marked `alt:G` in its note. The share is reported both ways.
- **Stretches.** These are 100 canonical ranks each, starting at the edge (1243–1342, 1343–1442). The share's denominator is the classified candidates in the stretch, not the 100 ranks: skips are not candidates **(added)**. Counting skips as non-G only lowers the shares.
- **Calibration (added).** I classified the list's own last stretch (1143–1242: today's frequency-segment items and the entrants there) by the same criteria. This checks whether the rule measures the ranking or my strictness.
- **Rater.** All classification is mine (one model, no second reader). The P/G line is the judgement the result depends on (see question 1).

## Results

### 1. The agreed additions (`additions.tsv`)

The 51 "genuinely missing" entrants already include holy, so "51 plus holy" is 51 concepts, not 52.

| Route | Count | Concepts |
|---|---|---|
| root | 28 | fact, accept, fate, influence, holy (author), avoid, suitable, guess, disappear, explode, thread, waste, forgive, load, disaster, decrease, statue, characteristic, obey, heal, hate, cruel, chain, bell, kindness, fraud, endure, substitute |
| boundary question | 13 | common, status, partner, environment, destroy, accuse, warm, celebrate, include, blame, contain, attend, achieve |
| built phrase (proposed) | 10 | heap, unique, exceed, participate, familiar, earthquake, nonsense, obstacle, summary, shelter |

- No addition is a loan candidate.
- The 10 phrase routes are my proposals. The author agreed to add these concepts, and each has a ready short phrase. If the list's precedent applies (ladder 2.3 gave frequent composable concepts roots: breakfast, kitchen), they are roots too.

### 2–3. The walk and the stop rule (`walk.tsv`)

| Stretch (canonical rank) | Candidates | G | G share | G incl. alt:G | P | A | L | N | C |
|---|---|---|---|---|---|---|---|---|---|
| 1143–1242 (calibration: today's list) | 79 | 30 | **38%** | 44% | 22 | 15 | 2 | 9 | 1 |
| **1243–1342** (stops here) | 41 | 10 | **24%** | 37% | 19 | 8 | 1 | 3 | 0 |
| 1343–1442 (trend) | 51 | 11 | **22%** | 35% | 22 | 14 | 3 | 0 | 1 |

- **Where it stops.** The rule stops at the end of the first stretch, **rank 1342**. G is under 50% there on either reading.
- **What it adds.** 10 G concepts: ancestor, coal, wild, cave, inherit, comfortable, depend, deny, pattern, revenge.
- **The trend stretch.** It has 11 more G (bay, fold, crazy, bend, hang, bribe, surround, stretch, bet, pity/mercy, loyal). These are not added by the rule.
- **Calibration.** The same criteria give 38% on the list's own last stretch. By the rule's own measure, the knee in general concepts lies at or before today's edge, not near 2,000.
- **What could flip it.** The result turns only on P. If every P counted as G (the ladder 2.3 precedent), the first stretch would be 29/41 = 71%, and the walk would go on.

**Totals (approximate, added).**
- Today: 520 roots in the lexicon, plus about 880 new forms in `ladder.tsv` and `additions.tsv`.
- Add the 28 root-route additions, up to 13 boundary questions, and the 10 walk G.
- The seed comes to about **1,440–1,460** roots before any drops. That is near the decision's rejected option (c) "a fixed ~1,550", reached through the rule and not by fiat.

**Loan candidates for the panel:**
- automatic (in the stopping stretch);
- perfume, gay and football (trend stretch);
- rose (calibration, alt).

### 4. Drop proposals for today's list (`drops.tsv`)

A scan, not a full reclassification of all 983 items.
- **Religion rows that contradict a decision:**
  - The 2026-10-13 decision "Religion made consistent" keeps angel, bishop, prophet and church as each tradition's own borrowed words. `roots-1500.txt` and `ladder.tsv` still list them as roots. The same holds for idol, which `religion.tsv` makes a phrase.
  - saint becomes **ewo [holy]** once holy is a root.
- **C/N long tail:** knight, senator, lieutenant, colonel, statistics, psychology, circuit, orbit, formula, sphere.
- **A (pooled ranks, one sense kept):** compound, grade, trial, single, term, deposit, review, promotion, medium, background.
- **P:** receipt, passenger, available, priority.
- **Housekeeping, not decisions.** The 14 day and month names, last night, the 93 "covered:" and the 36 "merge:" ladder rows sit in `roots-1500.txt` but are not roots. They should be counted out of any root total.

## Questions for the author

1. **The P line (decides the outcome).**
   - The stop rule counts "a short clear phrase covers it" as non-G. Ladder 2.3 and the ladder pass gave frequent composable concepts roots (breakfast "pasu pi leso possible; frequent, root per ladder 2.3").
   - Read as the decision words it, the walk stops at 1342 and adds 10 roots. Read with the precedent, it continues.
   - Which reading holds at this frequency? Recommendation: the decision's wording. The calibration shows the list's last stretch already under 50%. Add-back trigger: the human test the decision names.
2. **Deep-layer gaps the frequency walk can't catch.**
   - The design log names harvest and plough among the 51; they aren't among them. In the corrected ranking, harvest is canonical rank 1460 and plough 1774, past the stop.
   - balance-02's SSA and Quechua gaps are wild animal, stranger, mercy, jealousy, cotton, bribe, deny, flour, powder, rub, cure, heritage, harvest, plough, sprout, candle, thigh, vein, reed, trunk, ancestor and calendar. They qualify (or not) by the deep-layer test ("a thing found in households across cultures"), not by frequency.
   - Should they get a separate deep-layer pass? The walk already reaches ancestor, wild, deny and inherit; stranger, mercy and bribe sit just past the stop.
3. **Boundary calls among the additions:**
   - common: "shared" vs "ordinary".
   - status vs rank/position (on the list).
   - partner (business / romantic / companion).
   - environment vs nature.
   - destroy vs **alun** "break".
   - accuse + blame: one root or two.
   - warm vs **tikun** "hot" (lump rate).
   - celebrate vs festival.
   - include + contain: one root, or **ibe** + **bese**.
   - attend.
   - achieve vs **wonku** "reach" and success.
4. **Phrase routes for 10 agreed additions** (heap, unique, exceed, participate, familiar, earthquake, nonsense, obstacle, summary, shelter): phrases or roots? Shelter ties to the pending keep/protect split. After it, **pu kuwi** reads "place that protects", which fits shelter, and warehouse moves to the new keep root.
5. **Boundary calls in the walk G:**
   - coal vs charcoal (one root?).
   - depend vs **gewan** "trust, rely on".
   - deny vs refuse (rank 1490).
   - pattern vs design/form.
   - comfortable vs pleasant (on the list).
   - wild without the "savage" sense.
6. **Loan candidates to the panel later:** automatic (stopping stretch); perfume, gay, football (past the stop; only if the walk is extended).
7. **Drops:**
   - Update `ladder.tsv`/`roots-1500.txt` for the religion rows (angel, bishop, prophet, church, idol, saint) that contradict the 2026-10-13 decision.
   - Take up the other drop proposals case by case.
8. **Uncertain:**
   - One rater classified everything. If the author doubts the stop, a blind reclassification of the two stretches by Codex would show whether the P/G line is mine or the data's. This is not done here: it would add a step.
   - Noticed in passing: `docs/language.md` is older than `spec/reference.toml` (it still shows **fu**, **gan**, **mu**; the reference has **fun**, **nan**, **su**). Is a `spec.py build` pending?

## Round 2 (the phrase line, author 2026-10-16)

Task: `PROMPT.md` "Round 2"; decision (b) "When a phrase covers a concept" (`docs/design-log.md`, last entry). Round-1 files above stay as they were; round 2 writes `walk-r2.tsv` (round 1's `src/walk-manual.tsv` + `src/r2-overrides.tsv` + `src/walk-r2-extra.tsv`, via `assemble_r2.py`) and `stretches-blind.tsv`.

### Progress (round 2)

- [x] r2-1 round-1 P rows of 1243–1442 reclassified (`src/r2-overrides.tsv`); the calibration stretch too (`src/r2-calib-overrides.tsv`, added)
- [x] r2-2 walk continued: the rule fires at once (1342); trend stretch 1343–1442; one more stretch 1443–1542 classified (`src/walk-r2-extra.tsv`, added: the result sits near 50%)
- [x] r2-3 `assemble_r2.py` → `walk-r2.tsv`, `calibration-r2.tsv` (merged sources in `src/r2/`)
- [x] r2-4 `stretches-blind.tsv`
- [x] r2-5 write-up (below)

Rerun: `direnv exec . python3 -B tests/coverage-02/assemble_r2.py` (also rebuilds the round-1 files, unchanged).

### Method (round 2)

- **The new line.** P only if the phrase is at most 3 syllables or is the compound the world itself uses. Roots have 2 syllables (500 of 520) and grammar words 1, so in practice: one root alone (in a plain or extended sense) or one root + one grammar word (**no**, **gen**, **du**, **pu**, **su**, **pi**, **nan**, **ten** …). A concept on the list without a form yet (**[care]**) counts as 2 syllables **(added)**: new roots come out at 2.
- **World compounds.** Where a longer phrase is kept as P, the note names the languages that build it the same way. These are my calls from known forms, not a panel count **(added)**; none of them falls in the stopping stretch, so the stop doesn't depend on them.
- **Unchanged.** Every other class (G, A, L, C, N, skips), the stretch boundaries and the denominator (classified candidates, skips out) stay as in round 1. Kept P rows carry the note "r2: P (phrase at most 3 syllables)"; changed rows say "r2: was P …".
- **Months.** August (1478) is skipped as an existing decision (months and weekdays are **dunan/dili mena** + number).

### Results (round 2)

| Stretch (canonical rank) | Candidates | G | G share | G incl. alt:G | G share without A (added) | P | A | L | N | C |
|---|---|---|---|---|---|---|---|---|---|---|
| 1143–1242 (calibration: today's list) | 79 | 37 | 47% | 53% | 58% | 15 | 15 | 2 | 9 | 1 |
| **1243–1342** (stops here) | 41 | 17 | **41%** | 46% | 52% | 12 | 8 | 1 | 3 | 0 |
| 1343–1442 (trend) | 51 | 23 | **45%** | 49% | 62% | 10 | 14 | 3 | 0 | 1 |
| 1443–1542 (second trend stretch, added) | 59 | 20 | **34%** | 36% | 43% | 23 | 12 | 1 | 3 | 0 |

Round 1 for comparison: 24% / 22% (calibration 38%).

- **Where it stops.** Still at the end of the first stretch, **rank 1342**. The new line lifts the share from 24% to 41%, not past 50%.
- **What it adds.** **17 G** (round 1: 10). The 7 new ones are discrimination, attitude, worthy, welfare, infection, urgent, ceiling. With round 1's: ancestor, coal, wild, cave, inherit, comfortable, depend, deny, pattern, revenge.
- **Trend.** 45% (23 G), then 34% (20 G). No climb towards 50% further down.
  - 1343–1442 G: bay, fold, illusion, crazy, torture, artificial, bend, hang, bribe, cannon, steam, canal, weed, surround, stretch, suffer, leak, guilty, stranger, bet, pity/mercy, castle, loyal.
  - 1443–1542 G: impression, accent, harvest, cage, wire/cable, virtue, tent, abuse, refuse, dam, excess, semen, envy/jealousy, swallow, powder, conspiracy, entrust, funeral, flour, generous.
- **Calibration.** The list's own last stretch is at 47% under the new line, just under 50%. The edge of today's list and the knee are about the same place.
- **How close it is.** The stop fires by 4 concepts. 21 of 41 would pass.
  - The softest P rows are a single existing root in a stretched sense: shine = **wino**, overcome = **yiyin**, appoint = **waka**, reasonable = **kidun**, neighbourhood = [district], extraordinary = [special]. If a rater says four of them aren't covered, the first stretch reaches 51% and the walk goes on.
  - A (artefacts) count as non-G candidates, as the decision lists them. Taken out of the denominator, the shares are 52%, 62%, 43%: the walk would stop at **1542**, with 60 G.
  - So the blind second rating decides more than the line does.

**The phrase routes of the 10 agreed additions under the new line (added).**
- Roots now: heap (**musu fanmu**, 4), nonsense (**apu su yofu**, 5), obstacle (**musu gi bamo**, 5).
- Phrases still: unique (**ga ni**, 2), participate (**yidu kin**, 3), familiar (**pi lugo**, 3), summary (**gen eten**, 3), shelter (**pu kuwi**, 3, after the keep/protect split), exceed (the comparison **ke … se**), earthquake (the world's compound "earth-shake": zh dizhen, ja jishin, de Erdbeben, ru zemletryasenie, hi bhūkamp).

**Totals (approximate, added).** The round-1 total was about 1,440–1,460 roots. Add 7 walk G and 3 addition roots: about **1,450–1,470**. If A leaves the denominator, about 1,500–1,510 (stop at 1542).

### Questions for the author (round 2)

Round 1's questions 2 (a deep-layer pass), 6 (perfume, gay, football), 7 (drops) and 8 stand. Question 1 is answered by decision (b). Question 4 is answered above under the new line.

1. **Do artefacts count in the denominator?**
   - The decision lists artefacts among the non-G candidates, so I counted them: stop at 1342, 17 G.
   - Without them: stop at 1542, 60 G.
   - Argument for leaving them out: an A row is a pooled English label, not a concept. Its senses sit elsewhere in the ranking or on the list.
   - Recommendation: keep the decision's wording and let the blind rater's A calls show whether mine are too generous. Add-back trigger: the rater marks most of my A rows as one concept.
2. **Stretched single roots as P.**
   - Are these covered: shine = **wino**, overcome = **yiyin**, appoint = **waka**, reasonable = **kidun**, neighbourhood = [district], extraordinary = [special]?
   - They are 2 syllables, so the line admits them. Four G among them would flip the stop.
3. **Lunch vs breakfast.**
   - Lunch is P by the world-compound clause ("midday meal" in zh, ja, de, tr, sw, id, hi).
   - Breakfast has a root (ladder 2.3), though it too is a compound in many languages.
   - Keep both as they are, or make them match?
4. **World-compound calls are mine, from memory:** useless, lunch, violation ("break the law"), export, import, decade, cooperate, organism. Only useless, lunch and violation fall in the walk's stretches, and none in the stopping stretch. Check them only if the walk is extended.
5. **Boundary calls among the 7 new G:**
   - discrimination (alt:N, a social-policy term).
   - attitude vs opinion and view (on the list).
   - worthy: one root "worth, deserve" with merit (on the list)?
   - welfare vs health (on the list); the state-welfare sense is N.
   - infection vs virus and **simi** "sick".
   - urgent vs emergency (on the list).
   - ceiling vs **kuwun** "roof": Arabic *saqf* and Hindi *chhat* lump them, Russian and Spanish split them; the lump rate is needed (rung 4).
   - Round 1's question 5 (coal/charcoal, depend vs **gewan**, deny vs refuse, pattern, comfortable, wild) stands.
6. **Boundary calls past the stop,** only if the walk goes on:
   - Trend stretch: illusion vs dream; cannon (alt:N); weed (alt:P, built in many languages but not one way); guilty vs fault; stranger vs foreign; castle (alt:C, or [palace]); pity vs mercy.
   - Second trend stretch: wire and cable one root (1471, 1544); refuse with deny; envy vs jealousy; powder vs **awin** "dust"; funeral vs bury (1695); excess, or a degree word "too" in the grammar; harvest vs **fanmu** "gather".
7. **Loan candidates for the panel:** automatic (stopping stretch, unchanged); perfume, gay, football (trend stretch, unchanged); rhythm (1443–1542, new).
8. **The blind file.**
   - `stretches-blind.tsv` has all 200 ranks of 1243–1442, as asked. 108 of them are already on the list (skips; spy, Thursday …).
   - Tell the rater to mark them "on the list", or filter them out before the run. Only the 92 candidates are compared.
   - The rater needs the class definitions and the new line, but not my notes.

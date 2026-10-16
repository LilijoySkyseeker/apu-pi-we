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

Task: `PROMPT.md` "Round 2"; decision (b) "When a phrase covers a concept" (`docs/design-log.md`, last entry). Round-1 files above stay as they were; round 2 writes `walk-r2.tsv` (from `src/walk-r2-manual.tsv` via `assemble_r2.py`) and `stretches-blind.tsv`.

### Progress (round 2)

- [ ] r2-1 reclassify round-1 P rows of 1243–1442 under the new line (`src/walk-r2-manual.tsv`)
- [ ] r2-2 continue the walk from 1443, stretch by stretch, until the rule fires + one trend stretch
- [ ] r2-3 `assemble_r2.py` → `walk-r2.tsv` and the table
- [ ] r2-4 `stretches-blind.tsv` (1243–1442, rank + concept)
- [ ] r2-5 README round-2 write-up (table, totals, questions)

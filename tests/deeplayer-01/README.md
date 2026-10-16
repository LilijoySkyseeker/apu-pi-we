# Deep-layer pass over the WOLD meaning list (deeplayer-01)

Task: `PROMPT.md`. Decision: "Modern life means everyone's, and a second entry route for roots" (author, 2026-10-16; `docs/design-log.md`, last entry; `docs/vocabulary-method.md` §0). Proposals only: nothing outside this folder changed, nothing committed. Choices of mine are marked **(added)**; every class in `pass.tsv` is my reading (one rater).

## Progress

- [x] 1 WOLD list fetched (`src/parameters.csv`, `src/forms.csv`, `src/languages.csv` from lexibank/wold CLDF) and per-meaning evidence computed (`evidence.py` → `evidence.tsv`)
- [x] 2 coverage index built (`build_index.py` → `coverage-index.tsv`, `candidates.tsv`) and each meaning matched by hand (`src/match.tsv`)
- [x] 3 uncovered meanings classified D/P/C/L/X (+ BQ, added) in `src/match.tsv`
- [x] 4 `pass.tsv` assembled (`assemble.py`)
- [x] 5 README write-up (per-field table, D list, questions)

Rerun from the repo root, each under a few seconds: `direnv exec . python3 tests/deeplayer-01/evidence.py`, then `build_index.py`, then `assemble.py` (prints the table). `view.py FIELD` and `g.sh REGEX` were the hand-pass aids.

## Method

- **The list.** WOLD's 1,460 core meanings (`Core_list=yes`; the CLDF has 354 more one-language extras, left out), 24 fields, label kept as WOLD writes it (`the plough`, `to sow`).
- **Evidence per meaning** (`evidence.tsv`). Over WOLD's 41 languages in 24 families: languages and families with any word; **root families (added)**, families with at least one language whose word is native (borrowed score 4–5) and unanalyzable; languages whose every word is borrowed. Nearly every meaning has *a* word in every language (WOLD asks for one), so "how many have a word" doesn't separate anything; "how many families have their own simple root" does, and that is what I used as the "many families" evidence. `freq_rank` is the coverage-02 rank of the head word where one matched (label match only, approximate).
- **Coverage.** Matched against `data/lexicon.tsv`, `data/compounds.tsv`, `data/grammar.tsv` and `numbers.tsv`, the reference's constructions (day after tomorrow, yes/no by echo), coverage-01 `ladder.tsv` / `additions.tsv` / `pending-splits.md` / `religion.tsv`, coverage-02 (`candidates.tsv` status, `additions.tsv`, round-1 `walk.tsv`, and the round-2 files as they stood: `src/r2-overrides.tsv`, `src/r2-calib-overrides.tsv`, `src/walk-r2-extra.tsv`) and balance-02 `concepts-entrants.tsv`. Every match was sense-checked by hand; ladder entries whose sense differs were not counted (ladder *cross* is the verb, *club* the society, *pound* the currency, *sink* the basin).
- **Classes.**
  - **cov**: an existing root, compound, grammar word or construction, a decided list item, the kinship rule (method §3.1: everything beyond mother, father, parent, child, sibling, spouse is composed), or a pending coverage-02 proposal (47 meanings; see question 7).
  - **D**: passes the deep-layer test (basic action or state, body part, household thing across cultures, or own root in many families) and no ≤3-syllable phrase or world compound covers it. **Tiers (added):** *core* = own root in at least 15 of 24 families and no alternative class seriously in play; *edge* = the rest (fewer families, or noted `alt:` X/P/C/L).
  - **BQ (added)**: an existing word may already cover it; the lump/split ladder decides (root or no root).
  - **P**: a phrase of at most 3 syllables, or the world's usual compound (sources cited in the note). Words in brackets are on the list without a form yet: **[bubble]**.
  - **C**: one region's crop, animal, institution or being; **L**: a widespread shared form, for the panel; **X**: too specific or specialist.

## Results

### Per field (`pass.tsv`)

Sorted by D + BQ. "Not covered" = everything but cov.

| Field | Meanings | cov | D | BQ | P | C | L | X | not covered |
|---|---|---|---|---|---|---|---|---|---|
| The body | 158 | 99 | 30 | 2 | 10 | 0 | 0 | 17 | 37% |
| Animals | 116 | 59 | 15 | 1 | 8 | 12 | 5 | 16 | 49% |
| Food and drink | 81 | 53 | 10 | 3 | 7 | 4 | 2 | 2 | 34% |
| Agriculture and vegetation | 74 | 26 | 11 | 0 | 6 | 9 | 2 | 20 | 64% |
| Clothing and grooming | 59 | 25 | 8 | 1 | 4 | 4 | 3 | 14 | 57% |
| Motion | 82 | 56 | 7 | 2 | 1 | 2 | 0 | 14 | 31% |
| The physical world | 75 | 55 | 6 | 2 | 2 | 1 | 0 | 9 | 26% |
| Basic actions and technology | 78 | 47 | 6 | 2 | 3 | 3 | 0 | 17 | 39% |
| Speech and language | 41 | 31 | 6 | 0 | 0 | 0 | 0 | 4 | 24% |
| Possession | 46 | 37 | 4 | 0 | 5 | 0 | 0 | 0 | 19% |
| Kinship | 85 | 80 | 3 | 0 | 2 | 0 | 0 | 0 | 5% |
| The house | 47 | 27 | 2 | 1 | 3 | 2 | 1 | 11 | 42% |
| Emotions and values | 48 | 45 | 1 | 1 | 0 | 0 | 0 | 1 | 6% |
| Spatial relations | 75 | 71 | 1 | 0 | 0 | 0 | 0 | 3 | 5% |
| Sense perception | 49 | 44 | 1 | 0 | 2 | 0 | 0 | 2 | 10% |
| Cognition | 51 | 49 | 1 | 0 | 1 | 0 | 0 | 0 | 3% |
| Social and political relations | 36 | 34 | 0 | 1 | 0 | 0 | 0 | 1 | 5% |
| Warfare and hunting | 40 | 27 | 1 | 0 | 1 | 0 | 1 | 10 | 32% |
| Law | 26 | 16 | 0 | 1 | 0 | 0 | 0 | 9 | 38% |
| Modern world | 57 | 46 | 1 | 0 | 0 | 0 | 4 | 6 | 19% |
| Quantity | 39 | 39 | 0 | 0 | 0 | 0 | 0 | 0 | 0% |
| Time | 57 | 56 | 0 | 0 | 1 | 0 | 0 | 0 | 1% |
| Religion and belief | 26 | 20 | 0 | 0 | 1 | 5 | 0 | 0 | 23% |
| Miscellaneous function words | 14 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0% |
| **All** | 1,460 | **1,056** | **114** | **17** | **57** | **42** | **18** | **156** | 27% |

**D = 114 rows = 108 new roots** (6 rows share a root: widow/widower, jewellery/jewel, gourd/pumpkin, plant/sow, weave/plait, lame/limp): **51 core, 57 edge**. Up to 17 more from BQ, and any L that fails the panel falls back to a root or a phrase.

**Where today's list is thin.** The abstract and grammatical fields are done (quantity, time, function words, cognition, spatial, emotions, social: 0–6% open). The gap is the material life the frequency corpora under-sample, the urban lean the decision named:
- agriculture (64% open: plough, hoe, sow/plant, ditch, trunk, the staples),
- clothing and its making (57%: sew, weave, wool, leather, beads),
- animals (49%: nest, flea, tick, wasp, lizard, crow, eagle),
- the house (42%: shelf, brick, hearth, chimney, floor, mat),
- basic actions and tools (39%: axe, saw, nail, clay, rub),
- food preparation (34%: roast/fry, bake, peel, sieve, knead, dough, mortar),
- the body (37%, but mostly finer parts: elbow, wrist, thigh, hip, heel, rib, jaw),
- weather/seasons are nearly covered (dew, rainbow, freeze, autumn are the gaps).

### The D list

Core (own root in ≥15 of 24 families):
- **Body:** beard, jaw, snot, beak, elbow, thigh, heel, kidney, waist, hip, hiccup, bury, itch, pus, lazy, naked.
- **Physical world:** cliff; dew; firewood (BQ vs **kima** "wood"); freeze.
- **Motion:** wrap, sink (go under), float, crawl.
- **Agriculture:**
  - plant/sow, one root (BQ: or **pinfe** "plant" as a verb);
  - mushroom.
- **Food:**
  - roast/fry, one root as WOLD lumps them (BQ: or apart; bake is a BQ under it);
  - peel, sieve/strain, knead, mortar (for pounding).
- **Speech:** whistle, scold, drum.
- **Clothing:** leather (BQ vs **unne** "skin, hide"), weave (also plait), sew, bead.
- **Possession:** stingy.
- **Tools:** axe; rub (BQ vs **sumin** "scratch"); clay.
- **Spatial:** hook (fishhook too).
- **Animals:** nest; eagle (BQ: hawk with it?); crow; scale (of fish or snake); flea; wasp; lizard; tick.

Edge (fewer families, or a phrase/X/C/L reading is in play; the `alt:` note in `pass.tsv` gives it):
- **Body:** blood vessel, rib, eyebrow, gums, wrist, ankle, scar; blink, palm, nipple, drown, a cold, bruise, lame/limp.
- **Kinship:** orphan; widowed person (one sex-neutral root, gender as a modifier).
- **Physical world:** swamp, rainbow.
- **Agriculture:** plough, hoe, ditch, tree trunk, palm tree, gourd/pumpkin (one root), bamboo.
- **Food:** famine, choke, jug/water jar, dough, chili.
- **Clothing:** wool, jewellery, braid.
- **House and tools:** shelf, brick, tap/faucet, saw, nail (the fastener; **tolin** is the finger nail).
- **Motion:** roll, squat.
- **Possession:** lend, borrow (method §3 already names lend/borrow as a pair to keep apart), weigh.
- **Speech:** whisper, boast, flute.
- **Other:** spear, greedy, pinch, betray.
- **Animals:** livestock, pigeon/dove, shell, whale ("big fish", zh *jingyu*, builds a known-wrong belief, C4), snail, shrimp, termite.

### Boundary questions (BQ, 17)

Each could be no root if the existing word's lump holds:
- well → **spring (water)**;
- put out a fire → **tapi** (turn off);
- hawk → [eagle];
- claw → **tolin**;
- shiver → **susin**;
- bake → [roast];
- scrape → **sumin**;
- to milk → **tunlo** as a verb;
- clothes button → **tinli** (device key/button);
- floor surface → **sison** (storey);
- pound in a mortar → **payon**;
- mat → carpet;
- twist → **duko**;
- chase → **lefan**;
- dare → brave;
- order/command → the INSTRUCT act or **wungu**;
- murder → **omen** "kill".

### Loan candidates for the panel (L, 18)

dolphin, mule, parrot, camel, cockroach, frying pan, black pepper, cotton, silk, tattoo, candle, tobacco, coconut, helmet, injection, mattress, tin can, calendar (the object). Each note says what it becomes if it fails (mostly D or P).

### Phrases (P, 57) and culture-bound (C, 42)

- **P, with the forms in `pass.tsv`:**
  - young animals as *animal + **tiwu*** (**dunsa tiwu** "calf", as ja *koushi*);
  - places and tools from verbs: **pu noso** "stable", **pu inke** "mill", **du inke** "pestle", **pu lumi** "hearth";
  - ≤3-syllable negations: **su bubin** "unripe", **su sonfa** "bald", **su nawi** "fast";
  - world compounds: **linma kudu** "thumb", **unne pi funo** "eyelid", **pasu pi kegin** "dinner".
- **C:** the regional animals (kangaroo, jaguar, moose …), regional crops (barley, rye, oats, fig, olive), tradition-bound items (altar, preach, veil, initiation), and two staples I'm unsure of (question 3).

### Found in passing

- **"order" (command or sequence) has no entry anywhere.** coverage-02 ranks it 76, and its status there is empty. This pass marks the command sense a BQ (19-45).
- **The design log names harvest and plough among the 51 additions (2026-10-15); they aren't among them.** coverage-02 noticed this. Harvest is a walk G; plough is D here.
- **The ladder's "relative" is now over the phrase line.** It is covered as **ewo pi yonyo** (5 syllables). Under the 2026-10-16 line it no longer counts as covered, so it should go back to the walk.
- **The spider phrase fits a centipede better.** `compounds.tsv` gives spider as "small animal of many legs", which describes a centipede more than a spider.
- **Some everyday words have no root and aren't on the WOLD list:** "to shave" (needed for razor), "to fish", "to herd".
- **"through" has no relation word.** I covered it with "pass", but it's a grammar question.

## Questions for the author

1. **How much of D to take?**
   - **Problem:** the decision says passing meanings get roots whatever their rank. The test is pass/fail, but the evidence is graded: 51 core vs 57 edge.
   - **Example:** *elbow* (17/24 families have their own root) vs *betray* (6/24, 11 loans).
   - **Options:**
     - (a) all 108;
     - (b) core 51 plus the 24 edge items with no alternative noted (orphan, plough, hoe, wrist, ankle, rib, gums, lend, borrow, flute, shelf, brick …), so ~75;
     - (c) core only.
   - **Recommendation:** (b). The 33 edge items with an `alt:` go to their alternative (mostly X or a phrase). Add-back trigger: a human test where speakers reach for one of them.
2. **The 17 BQs.**
   - Each is a lump/split call for ladder 1 (rung 4 lump rates, `tools/clics_rates.awk`).
   - **Recommendation:** run the rates for these 17 pairs as one batch, rather than deciding by hand. Not done here, so as not to add a step.
3. **Multi-region staples: C or D?**
   - **Problem:** "C" means one region's crop. Cassava is a staple across Africa, South and Southeast Asia and South America, and millet/sorghum across Africa and South Asia. Rice has a root and maize is on the list.
   - **Options:** (a) C, borrowed; (b) D.
   - **Recommendation:** (b) for cassava and millet/sorghum, by the "everyone's modern life" correction. Water buffalo stays C.
4. **A pattern for young and sexed animals.**
   - **Problem:** WOLD has 13 such meanings (calf, lamb, foal, kid, bull, mare, rooster …).
   - **Proposal:** the kinship pattern, *animal + **tiwu*** for young and *+ **lowu**/**futa*** for sex, stated once in the reference, with no roots.
   - **Recommendation:** adopt it.
5. **deaf and mute vs blind.**
   - **Problem:** blind is a root on the list, while **su nulu** "deaf" and **su oyi** "mute" (3 syllables) pass as phrases under the new line.
   - **Options:** (a) keep the phrases; (b) give all three roots for parity.
   - **Recommendation:** (a), with blind reviewed in the existing-lexicon pass.
6. **18 loans to the panel.**
   - These are the L list above.
   - **Recommendation:** batch them with the next panel run. Cotton and candle are on the balance audit's gap list.
7. **47 meanings are covered only by pending coverage-02 proposals.**
   - **Problem:** this includes walk G items from its trend and round-2 stretches (bay, bend, fold, hang, stretch, pity, loyal, crazy, steam, flour, harvest, tent, stranger, swallow, guilty, refuse, envy, descend). If the stop rule ends the walk before them, they aren't covered.
   - **Recommendation:** count them once, here or there. If the walk stops short, classify them here. Their own-root counts run from 3 to 19 of 24 (median about 11), so roughly a third would be core, a third edge, and the rest phrase or X. Not done here, since the walk's outcome is still open.
8. **"order, command" (rank 76) has no entry.**
   - **Problem:** the BQ above is whether the INSTRUCT act (+ **iko**) carries it or it needs a root. "Order" in the sense of sequence is a separate gap.
   - **Recommendation:** a root for "command, order", since it is frequent and action-relevant.

Caveats:
- One rater. A blind second classification of the D/X line (Codex, as the coverage-02 decision did for its stretches) would show how much is mine.
- WOLD's sample has 8 Indo-European languages of 41. Root-family counts limit that skew, but "unanalyzable" is the contributors' judgement.
- Doghouse flag, once: the decision asked for this route. The edge tier and its add-back trigger are there to keep it from turning into a word-collecting exercise.

## Blind second rater (Codex, 2026-10-16) and the author's decision

Codex rated the 327 uncovered D/B/P/X meanings blind (`CODEX-PROMPT.md`, `codex-blind.tsv`). It rated all 51 core-D meanings strong; below that it was more generous (53 edge-D and 42 X rated strong). Tie-break by the strong tier's own measure (native single-root words in at least 15 of 24 families): 20 disputed meanings meet it and were rated strong by Codex: foam, weave/plait, boil (bubble), spin, howl, sinew/tendon, vulture, gnat, lame, tree trunk, groan, spleen, spindle, hollow out, pinch, palm tree, bore (drill), mould, carve, spear. Author (2026-10-16): add them. WOLD route total: 51 core + 24 clear edge + 20 = ~95 roots.

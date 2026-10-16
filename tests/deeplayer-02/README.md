# Deep-layer follow-ups: the 17 boundary questions and the 18 loan candidates (deeplayer-02)

Task: `PROMPT.md`, two follow-ups to `tests/deeplayer-01/` (design log, 2026-10-16 entries). Proposals only: nothing outside this folder changed, nothing committed. Choices of mine are marked **(added)**.

## Progress

- [x] 1 BQ pairs mapped to Concepticon glosses; CLICS4 rates computed (`bq_rates.py` → `bq-rates.tsv`)
- [x] 2 BQ decisions by ladder 1 (`bq.tsv`)
- [x] 3 loan panel judgments (`loanwork/panel.txt`, Wiktionary tables in `loanwork/wikt-raw.txt`)
- [x] 4 loan verdicts, adapted forms, collisions, offensive check (`loans.py` → `loans.tsv`)
- [x] 5 README write-up

Rerun from the repo root, a few seconds each:
- `direnv exec . python3 tests/deeplayer-02/bq_rates.py DIR`, where DIR is the `cldf/` folder of CLICS4 v1.0 (Zenodo 19608447). It is unpacked in this session's scratchpad, not the repo. MOON/MONTH reproduces balance-02's 69.9.
- `direnv exec . python3 tests/deeplayer-02/loans.py`

## Part 1: the 17 boundary questions

### Method

- **Ladder 1, in order** (vocabulary-method §0):
  - **Rung 1:** no international standard fixes the everyday boundary for any of the 17. Criminal law (murder) is national, and building vocabularies (floor/storey) are technical, so both are outside the rung's scope (author, 2026-10-13).
  - **Rung 2:** no pair involves a known-wrong belief.
  - **Rung 3:** it can only add a distinction. So it matters only where rung 4 lumps, which is claw/nail alone. I checked it there; see the table.
  - **Rung 4** decided the rest.
- **Rates.** `bq_rates.py` is `tests/balance-02/clics_rates.py` with the 17 pairs plus 7 side pairs. The method is unchanged:
  - A language lumps a pair when one segment string is listed under both concepts.
  - The rate is the mean over families of the share of each family's languages that lump.
  - The range is a bootstrap of 2,000 family resamples.
- **A narrower "no copies" rule (added).** Some sources list one broad item under both concepts of a pair: IDS and WOLD's "SPRING OR WELL" and "ROAST OR FRY", and "CLAW OR NAIL" and "EAGLE OR HAWK" in 11 and 7 sources. Those rows are copies, not evidence that the language lumps the pair.
  - balance-02 dropped every form with any `ConceptInSource`. That also drops plain relabels ("HIT" for STRIKE, "TURN" for TURN (SOMETHING)) and broad items found on one side only.
  - Here a language loses only the broad item that appears under both concepts.
  - Where the two figures differ, the copy-free one decides, since the copied figure is an upper bound (§3).
- **Flags:**
  - **near 50:** the rate is within 5 points of 50.
  - **no CLICS coverage:** a concept is missing from CLICS.

### Results (`bq.tsv`, `bq-rates.tsv`)

| WOLD meaning | Existing word | Concepticon pair (families) | Rate % (95% range) | Result |
|---|---|---|---|---|
| well | spring (water), list | WELL / SPRING (OF WATER) (19) | 3.6 (1–8); 82.5 with copies | **two**: new root "well" |
| put out a fire | **tapi** "close" | EXTINGUISH / SHUT (59) | 0.1 (0–0) | **two**: "put out, extinguish" |
| hawk | [eagle] | HAWK / EAGLE (49) | 13.3 (6–22) | **two**: "hawk" |
| claw | **tolin** "nail" | CLAW / FINGERNAIL (78) | 53.9 (44–63), **near 50**; 62.1 with copies | **one**: **tolin** "nail, claw" |
| shiver | **susin** "shake" | SHIVER / SHAKE (69) | 7.2 (3–13) | **two**: "shiver, tremble" |
| bake | [roast/fry] | BAKE / ROAST (53) | 17.0 (9–26); BAKE / FRY 16.1 | **two**: "bake" |
| scrape | **sumin** "scratch" | SCRAPE / SCRATCH (24) | 10.0 (2–20) | **two**: "scrape" |
| to milk | **tunlo** "milk" | DRAW MILK / MILK (56) | 0.3 (0–1) | **two**: "milk (an animal)" |
| button (clothes) | **tinli** "key, button" | BUTTON / KEY (43) | 0.0 (0–0) | **two**: "button (on clothes)" |
| floor (surface) | **sison** "storey" | **no CLICS coverage** (no storey concept) | panel stand-in: 2 of 16 lump | **two**: "floor (surface)" |
| pound in a mortar | **payon** "hit" | POUND / STRIKE (66) | 11.0 (6–18); POUND / BEAT 15.6 | **two**: "pound, crush" |
| mat | carpet, list | MAT / RUG (26) | 19.6 (7–33) | **two**: "mat (woven)" |
| twist | **duko** "turn" | TWIST / TURN (SOMETHING) (49) | 1.0 (0–2) | **two**: "twist, wring" |
| chase | **lefan** "follow" | PURSUE / FOLLOW (55) | 22.5 (14–32) | **two**: "chase, pursue" |
| dare | brave, list | DARE / BRAVE (35) | 7.8 (2–15) | **two**: "dare" |
| command | **wungu** "lead"; INSTRUCT act | COMMAND / LEAD (GUIDE) (51) | 0.0 (0–0) | **two**: "command, order (someone)" |
| murder | **omen** "kill" | MURDER / KILL (56) | 26.3 (16–37) | **two**: "murder" |

**One lumps, 16 split:**
- **claw/nail lumps.** Rung 3 can only add a split, and context (whose nail) separates the two, so it adds nothing here.
- **The 16 splits are new roots, before the phrase line.** **To milk** is the weakest: 12 of 24 root families in WOLD, and the 4-syllable phrase **donbo tunlo** "squeeze milk" is how zh 挤奶 and ko 젖을 짜다 say it (question 4).
- **Floor has no CLICS coverage.** Concepticon has no storey concept (its STORY means "tale"). As a stand-in **(added)**, I used the panel's Wiktionary tables for floor ("bottom part of a room") and storey ("floor, level"), 16 languages in each:
  - Only es *piso* and sw *sakafu* use the same first-listed word for both.
  - id *lantai*, hi *tal* and bn *tal* also appear in both lists.
  - The other 11 split cleanly.
  - This stand-in is not family-balanced.
- **Device push-button and turn-off aren't measured.** Neither has a Concepticon concept (questions 3 and 5).

### Found in passing

- **The roast/fry lump that deeplayer-01 took over from WOLD is a list artifact.**
  - With copies, ROAST / FRY lumps 94.0% across 66 families.
  - Without them it lumps 3.0%, across only 5 families. IDS and WOLD both ask for "roast or fry" as one item.
  - The core root "roast, fry" (author, 2026-10-16) rests on WOLD's question, not on languages (question 1).
- **balance-02's copy rule was broader than it said.** It also dropped relabelled forms (HIT, TURN). Its leg/foot "no copies" figure (23%) may move under the narrower rule. Not rerun here.

## Part 2: the 18 loan candidates

### Method

The loan panel exactly as `tests/coverage-01/part3/loans.md` describes it, with its author's decisions:
- **Everyday loans count beside a formal word, with a source.** Memory columns count only once sourced, with no Quechua assumption.
- **Shapes.** Two shapes are one when their adapted forms keep the same consonants, read as the rerun did: the source's shapes, where a borrower's own sound changes don't make a new shape.
- **Five-times rival rule.** A loan doesn't count when a rival for the same concept is at least five times as frequent. A broad rival (needle, smoke) doesn't trigger it.
- **Thin deciding columns fail.**
- **Median ties** go to the variant used in more regions, then the shorter one.
- **Pass rule (author, 2026-10-15):** at least **12 of 20** languages, across at least **5 of the 7** regions.
- **Sources** (`loanwork/panel.txt`):
  - Wiktionary translation tables for the sense, fetched 2026-10-16 with `tests/lexicon-ladder-01/panel.py` (`loanwork/wikt-raw.txt`).
  - The foreign word's own entry (kaikki dumps).
  - OpenSubtitles 50k lists (hi bn ta and the rest) and the Leipzig 2017 corpora (sw ha yo qu) in `~/work/cache/coverage`.
  - Japanese katakana words are missing from its subtitle list, so the Japanese column rests on Wiktionary.
- **Each pass was then checked:**
  - adapted with `tools/names.py`;
  - checked for collisions against `data/lexicon.tsv`, `grammar.tsv`, `numbers.tsv`, the 11.5 spelling words, and content keys (incl. `senary.tsv`, `compounds.tsv`);
  - checked with `tools/offensive.py`.
- **Each failure goes to a root or a phrase:**
  - **Root:** it passes the deep-layer test (a household thing across cultures, or named in many families), and no phrase of 3 syllables or fewer, and no world compound, covers it.
  - **Phrase:** otherwise.
  - "Root families" is deeplayer-01's count: families with a native, unanalyzable word, out of 24.

### Results (`loans.tsv`)

| Loan | Count / regions | Verdict | Form or fallback |
|---|---|---|---|
| tobacco | 13 / 6 (no AM) | **pass** | ***tabaku*** (no collision; `blocked` false, `matches` false) |
| calendar (object) | 13 / 6 (no WA) | **pass** (thin) | ***kalendalu*** (no collision; `blocked` false, `matches` false) |
| tattoo | 8 / 4 | fail | phrase **[pattern] pi unne** "skin pattern" |
| helmet | 7 / 4 | fail | phrase **[hat] gufu** "hard hat" (the world's "safety/iron hat") |
| injection | 6 / 3 | fail | phrase **[needle] pi [medicine]** |
| dolphin | 5 / 3 | fail | phrase **[pig] pi puya** "sea pig" (zh, ja kanji, vi) |
| coconut | 5 / 2 | fail | phrase **[palm tree] pi tanun** "palm fruit" (ja, ko); COCONUT / PALM 5.2% |
| mule | 4 / 2 | fail | phrase from horse + [donkey] |
| parrot | 4 / 2 | fail | **root** "parrot" (13/24 root families; no world compound) |
| mattress | 4 / 2 | fail | **root** "mattress" (household; or widen **soti** "bed", a roadmap candidate) |
| frying pan | 3 / 2 | fail | phrase **du [roast/fry]** "frying tool", 3 syllables (as ar *miqlāh*, sw *kikaango*) |
| cotton | 3 / 3 | fail | **root** "cotton" (clothing across cultures; 11/24) |
| candle | 3 / 2 | fail | **root** "candle" (household light across cultures; 8/24) |
| silk | 2 / 2 | fail | phrase **demi pi enna** "worm cloth" (2/24, not everyday everywhere) |
| pepper (black) | 2 / 2 | fail | **root** "pepper, the spice" (in kitchens everywhere; chili is the decided phrase "[pepper] tikun"; PEPPER / CHILI 14.8%) |
| camel | 2 / 2 | fail | neither: **C**, borrowed from its users' word (3/24, four unrelated loan shapes) |
| tin can | 2 / 1 | fail | phrase **nansa pi [metal]** "metal box" (vi, ar) |
| cockroach | 1 / 1 | fail | **root** "cockroach" (household pest across cultures; 9/24) |

**Summary:** 2 loans, 6 roots (parrot, mattress, cotton, candle, pepper, cockroach), 9 phrases, 1 culture-bound (camel).

**Why most fail.** The world borrows these words, but from different sources:
- mule: *mula* vs *baghl*;
- pepper: *piper*, *filfil*, *pimienta* and *marica*;
- silk: *harīr* vs *abrīsham*;
- coconut: *coco* vs *nārikela*;
- mattress: *matras* vs *tošak*.

East Asia mostly uses Sino words. Apart from the two passes, only tattoo reaches 8 counted languages.

## Questions for the author

1. **roast/fry: one root or two?**
   - **Problem:** the 2026-10-16 core root "roast, fry" lumps the two because WOLD asks for them as one item. CLICS without the copies gives 3% over 5 families, too thin to decide by itself. From memory, the panel mostly splits them: zh 烤/炒, hi *bhūnnā/talnā*, ar *šawā/qalā*, sw *choma/kaanga*, es *asar/freír*; ru *žarit'* lumps.
   - **Options:** (a) keep one root; (b) two roots, roast and fry; (c) check the panel properly first.
   - **Recommendation:** (c), then most likely (b). The frying-pan phrase **du [fry]** works either way.
2. **claw in tolin.**
   - The rate is near 50 (53.9 without copies, 62.1 with; 80% of resamples ≥50).
   - **Recommendation:** one root, reglossed **tolin** "nail, claw". Add-back trigger: a test where claw and fingernail get confused in use.
3. **The device button and tinli.**
   - **Problem:** the clothes button splits from **tinli** "key" (0/43 families; the cold review's A4 F11 found the same). Where the push-button goes isn't measurable: CLICS has no concept for it. In the panel's tables, 8 of 16 languages use the same first-listed word for the push-button and the clothes button (ja hi bn fa ar tr es fr).
   - **Options:** (a) the new root "button" takes both buttons and **tinli** stays the lock key; (b) **tinli** keeps "key, push-button" and the new root is the clothes button only.
   - **Recommendation:** (a). It also settles the open roadmap item on **tinli** (key/button).
4. **Concepts CLICS can't measure across word classes (to milk, dare).**
   - **Problem:** CLICS compares exact strings, so it sees a lump only when the noun and verb are the same word, as in English *milk*. A language that derives the verb counts as splitting. In this language any word takes any role, so **tunlo** "milk" as a verb and "brave" as a verb are the lumped readings.
   - **Options:** (a) accept rung 4 (two roots); (b) to milk as the phrase **donbo tunlo** "squeeze milk" (zh, ko, sw *kama*); dare as "brave" used as a verb.
   - **Recommendation:** (a) for dare (7.8%, and the verb reading of brave is "be brave", not "dare"). For to milk, (b) if the author accepts "squeeze milk" as the world's compound, else (a).
5. **put out vs turn off.**
   - **Problem:** the new root "put out (a fire)" splits from **tapi** "close". But **tapi** also covers "turn off (a device)" (language.md 11.4). Many languages say turn-off with their extinguish verb (fr *éteindre*, es *apagar*, ja 消す, ru *gasit'*; from memory). There's no Concepticon concept for turn-off.
   - **Options:** (a) the new root also takes turn-off; (b) leave turn-off with **tapi**.
   - **Recommendation:** (b) for now; it's already in the reference. Add-back trigger: a test where **tapi** for a light reads as "close".
6. **tobacco rests on the shape reading.**
   - **Problem:** 6 of its 13 columns are nasalised or reduced borrowings of Portuguese *tabaco*: id *tembakau*, hi *tambākū*, fa *tanbâku*, sw *tumbaku*, bn *tāmāk*, ko *dambae*. Under the rerun's reading (the source's shape counts) it passes 13/6. Under a strict comparison of adapted consonants, *tabak* has 7 and *tanbak* 4, and it fails.
   - **Recommendation:** pass, as the rerun read rupee and dollar. If the author reads shapes strictly, tobacco gets a root (household across cultures? arguable) or the phrase "smoke leaf" (vi *thuốc lá*, ta *pukaiyilai* "smoke leaf").
7. **The rival rule at its edge (tattoo).**
   - **Problem:** Korean 문신 against 타투 is 5.0 times, and Persian *xâlkubi* against *tatu* is 5.4. Both fall on the rule, and tattoo fails at 8/4. Letting both through still gives only 10/5, so the verdict doesn't depend on it.
   - **Recommendation:** none needed. Noted because 5.0 is the line itself.
8. **calendar is thin.**
   - **Problem:** 13/6, but ta, hi, qu and yo rest on 2–4 tokens each. No single column decides (each removal leaves 12 across 5 or 6 regions), but two together would.
   - **Options:** (a) pass; (b) treat it as a thin pass and fall back to its phrase.
   - **Recommendation:** (a). The rule asks for solid evidence only where one column decides.
9. **camel is neither root nor phrase.**
   - It's a regional animal borrowed in four unrelated shapes (*jamal*, *luòtuó*, *ūṣṭra*, *deve*).
   - **Recommendation:** culture-bound (C), like kangaroo, borrowed from the users' own word. The task asked for root or phrase, so this departs from it, and I'm flagging it.
10. **pepper or chili as the root.**
    - **Problem:** chili was decided as the phrase "[pepper] tikun", which needs a pepper word, and pepper fails the panel. The world builds in both directions:
      - black pepper from chili: hi *kālī mirc*, tr *karabiber*, th *phrík thai*;
      - chili from pepper: en *hot pepper*, ar *filfil ḥārr*, fa *felfel-e tond*.
    - **Options:** (a) pepper a root, chili stays "[pepper] tikun"; (b) chili a root (13/24 root families, stronger evidence), pepper "black chili" **[chili] tago**.
    - **Recommendation:** (a), since it keeps the decided chili phrase. (b) has the better family evidence.
11. **The narrower copy rule.**
    - Adopt it for later rung-4 runs, and rerun balance-02's leg/foot "no copies" figure under it?
    - **Recommendation:** yes. The broad rule drops relabels that carry real evidence.

Caveats:
- One rater for the panel judgments and the deep-layer calls.
- Phrase forms use words with no form yet ([pig], [hat], [needle], [medicine], [metal], [pattern], [palm tree], [donkey]); they're shapes, not final forms.
- No new root was given a form: forms come from `tools/words.py add-content` at adoption.

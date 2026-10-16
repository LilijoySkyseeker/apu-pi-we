# Concept list 01: the final concept list for the ~1,500-root placement

Task: `PROMPT.md`. Round 1 consolidated every concept decision from 2026-10-13 to the end of `docs/design-log.md` into one list. Round 2 (author, 2026-10-16) folds in the author's answers and deeplayer-02, fixes two data files, and adds the sets pass.

Nothing is committed. Outside this folder, only `data/antonyms.tsv` and `tests/coverage-01/part3/religion.tsv` changed, as round 2 allowed. Choices of mine are marked **(added)**.

## Progress

- [x] Round 1: read the log and the inputs; `build.py` → `concepts.tsv`, `excluded.tsv`; checks; questions
- [x] R2.1 fold deeplayer-02 and the approved answers into `build.py`; rebuild
- [x] R2.2 fix `data/antonyms.tsv` stale glosses and `religion.tsv` notes
- [x] R2.3 sets pass → `sets.md` (rates: `sets_rates.py` → `sets-rates.tsv`)
- [x] R2.4 this README

Rerun (about a second): `direnv exec /home/agent/work/repos/universal-language python3 tests/conceptlist-01/build.py`. It prints the totals.

## Files

- **`concepts.tsv`** has one row per concept that gets a content form in the placement. Its columns:
  - `concept`: the sense gloss.
  - `route`: one of
    - **root**;
    - **loan**: new, with its form fixed by the panel;
    - **kept loan**: from the lexicon;
    - **loan candidate**: the standard words, which wait on the loan panel (author 2026-10-16); if one fails, it becomes a root or a phrase.
  - `form`: today's form. A root's form moves in the placement; a loan keeps its form.
  - `field`: the lexicon's field names.
  - `tier`, `rank`.
  - `antonym`: new pairs are marked "(added)".
  - `source`: the first tag is what admitted the concept; "also …" tags are later confirmations.
  - `note`.
- **`excluded.tsv`** has every concept considered and not given a root or loan, with the reason. Rows marked `pending:` wait on unfinished work.
- **`build.py`** is the single generator. Every hand decision is a table in it, citing its log entry.
- **`sets.md`** is the sets pass, as proposals.
- **`sets_rates.py` → `sets-rates.tsv`** holds the CLICS rates it cites. They need CLICS4's `cldf/` folder, kept outside the repo, as deeplayer-02 does.

**Source tags.**

| Tag | What it is |
|---|---|
| LEX | `data/lexicon.tsv` |
| LAD | coverage-01 ladder pass (`part3/ladder.tsv`, roots-1500) |
| WB | first-word filter (`wordbank-final.tsv`) |
| LOAN | `loans-final.tsv` / `loans-rerun.tsv` |
| REL | religion decisions |
| ADD1 | coverage-01 `additions.tsv` |
| BAL | balance-02's 51 additions and their boundaries |
| WALK | walk round 2, G rows up to rank 1342 |
| PL | phrase line on the four named items |
| **PL-retro** | the phrase line applied to older phrases (round 2) |
| **SUBJ** | school subjects (round 2) |
| WOLD-core / -edge / -codex | the WOLD decisions of 2026-10-16 |
| WOLD-47 | the 47 walk-only meanings, classified in round 1 **(added)** and confirmed |
| **BQ02** | deeplayer-02 boundary questions, as decided (round 2) |
| **LOAN02** | deeplayer-02 loan panel, as decided (round 2) |
| DROP | the 2026-10-16 drops |

## Totals

**1,542 concepts get a content form** (round 1: 1,505):
- **1,457 roots.**
  - 478 keep today's form, which moves in the placement.
  - 979 are new.
- **85 loans.**
  - 18 kept from the lexicon.
  - 63 new with forms: round 1's 61, plus *tabaku* and *kalendalu*.
  - 4 loan candidates pending the panel: planet, temperature, oxygen, mass.

| Source (first tag) | Roots, today's form | Roots, new | Loans | Total |
|---|---|---|---|---|
| LEX | 478 | 6 (failed loans) | 18 kept | 502 |
| LAD (incl. WB, LOAN) | – | 741 | 60 + 4 candidates | 805 |
| LOAN (pound, a currency) | – | – | 1 | 1 |
| ADD1 | – | 28 | – | 28 |
| BAL | – | 46 | – | 46 |
| WALK | – | 17 | – | 17 |
| PL-retro | – | 13 | – | 13 |
| SUBJ (biology; the other four were already roots) | – | 1 | – | 1 |
| WOLD-core (fry split from roast) | – | 52 | – | 52 |
| WOLD-edge | – | 24 | – | 24 |
| WOLD-codex | – | 19 | – | 19 |
| WOLD-47 | – | 11 | – | 11 |
| BQ02 | – | 15 | – | 15 |
| LOAN02 | – | 6 | 2 | 8 |
| **Total** | **478** | **979** | **85** | **1,542** |

- **By route:** the frequency route gives 1,413 (LEX, LAD, LOAN, ADD1, BAL, WALK, PL-retro, SUBJ), and the deep-layer route 129 (WOLD, BQ02, LOAN02).
- **Tiers:**

  | Tier | 5 | 4 | 3 | 2 | 1 |
  |---|---|---|---|---|---|
  | Concepts | 15 | 67 | 328 | 679 | 453 |

  The cut points were accepted (author 2026-10-16).

**Excluded: 671** (round 1: 709).

| Reason | Count |
|---|---|
| Phrase (incl. "phrase or long tail" 31) | 220 |
| Long tail (incl. "culture-bound or long tail" 19) | 178 |
| Covered by another word | 71 |
| Culture-bound | 55 |
| Artefact (pooled English label) | 52 |
| Grammar or construction | 36 |
| Past the walk's stop (G 32, L 4) | 36 |
| Dropped (mixed senses) | 10 |
| Superseded by a later root | 8 |
| **Pending** | **4** |
| Outside the core (spelling alphabet) | 1 |

The 4 pending rows:
- automatic (loan panel);
- pity and envy (the sets pass; `sets.md` §11 proposes roots);
- **yebin** against **liga** (ladder 1).

There are no open-question rows left.

## What round 2 changed

**1. deeplayer-02 boundaries** (`bq.tsv`, author 2026-10-16): **15 new roots.**
- The roots:
  - well (dug water source);
  - put out, extinguish (a fire);
  - hawk;
  - shiver, tremble;
  - bake;
  - scrape;
  - milk (an animal);
  - button (on clothes, also a push-button);
  - floor (the surface walked on);
  - pound (in a mortar);
  - mat;
  - twist, wring;
  - chase, pursue;
  - dare;
  - murder.
- order/command was already a root. Claw joins **tolin**, reglossed "nail (of a finger or toe), claw".
- **tinli** is reglossed "key (for a lock)": the new button root takes both buttons (option a). Turn-off stays with **tapi** (option b).
- **Roast/fry splits into two roots:** "roast (cook over a fire or in dry heat)" and "fry (cook in hot oil or fat)".
- The lexicon glosses of **tolin** and **tinli** change at adoption, not here.

**2. deeplayer-02 loans** (`loans.tsv`):
- **Loans:** tobacco *tabaku* and calendar *kalendalu*.
- **Roots:** parrot, mattress, cotton, candle, pepper (the spice), cockroach.
- **Phrases:** dolphin, mule, frying pan, silk, tattoo, coconut, helmet, injection, tin can.
- **Culture-bound:** camel.

**3. The phrase line, applied retroactively. 13 roots:**
- century, kingdom, childhood, patient (sick person), throne, corpse, giant, plain (land), salary, delicious, fill, acquaintance;
- descend, which also covers WOLD's descend and land (both were "out" in round 1).

**3 stay phrases as the world's compound** **(added reading)**:
- welcome ("good come": *bienvenido*, *willkommen*, *hoş geldiniz*; a routine);
- library ("book house": zh, ja, tr, fa, hi);
- prime minister ("chief minister": hi, sw, id, ja, tr).

My test: a compound of two content words that most panel languages use. A derivation by affix (king-*dom*, child-*hood*) isn't one, so kingdom and childhood became roots.

**4. Other answers applied:**
- **School subjects:** chemistry, physics, history and mathematics were already roots, now tagged SUBJ; biology is new.
- **General (army rank):** dropped as a military rank.
- **Mayor, governor and minister:** kept.
- **Sofa:** borrowed (culture-bound).
- **Planet, temperature, oxygen and mass:** marked "loan candidate".
- **Confirmed:**
  - harvest, refuse and stranger are roots;
  - defeat = lose (a contest);
  - none of the pooled-sense items is kept;
  - saint is "holy person";
  - emergency stays a root;
  - the 17 operators stay out;
  - the added antonym pairs are kept.

**5. Small fixes found while rebuilding** **(added)**:
- **supper** (WOLD 5-45) is now covered by dinner.
- **herder** is the phrase **no [herd]** (3 syllables), since herd became a root.
- **Fields:** axe, drum, flute and nail (fastener) were filed as actions and are now things; clay is now nature.
- **Source tags:** chemistry's source listed ADD1 three times; each tag is now listed once.
- **New antonym pair:** descend ↔ rise.

## Data fixes (outside this folder)

**`data/antonyms.tsv`: four stale glosses corrected.**

| Was | Now | Why |
|---|---|---|
| "live, be alive or dwell" | "live, be alive, dwell; life" | the lexicon's current gloss |
| "ask" | "ask (a question)" | the lexicon's current gloss |
| "day, daytime or 24 hours" ↔ night | "daytime" ↔ night | the sense the pair was made for (split 2026-10-13) |
| sun ↔ "month; moon" | sun ↔ "moon" | the sense the pair was made for (split 2026-10-13) |

- **Why daytime and moon (added):** both now name the split-off sense, which has no form yet. The lexicon's current glosses, **dili** "day (24 hours)" and **dunan** "month", aren't opposites of night and sun. Every reader matches pairs by exact gloss and skips a gloss it doesn't find, as it already does for the senary rows. The placement will apply both pairs to the new roots once they're placed.
- **No reader loses a pair:** the stale glosses matched nothing before either. `words.py move` doesn't use the file for weighting, and `tools/build.py` can't match multi-word glosses (below).
- **The number and senary pairs stay in the file.**
  - `tests/coverage-01/part4/placement.py` reads every row and weights matched pairs at 30, and `tools/build.py` does the same. So the number rows (6–10^9) are live confusion weights for the number words.
  - `tools/site.py` already filters them out of the dictionary's opposites. Moving them out would change the placement.
  - The senary rows match nothing in the lexicon and are inert.
- **One problem found (not fixed):** `tools/build.py` line 285 splits rows on any whitespace (`l.split()`), so a row with a multi-word gloss gives a tuple of more than two and `for a, b in ants` fails to unpack (most rows have one). The file's other readers split on tabs. `tools/build.py` is the old full rebuild, so this only matters if it is run again.

**`tests/coverage-01/part3/religion.tsv`: six notes rebuilt** from the file's git history (bless, miracle, saint, heaven, hell, sin). Two edits had been appended onto the old notes ("… too rare for a root", "… borrowed; the sky is yaye; the sky is yaye"). Each note now states the decision and its evidence once.

## Checks

1. **No duplicate senses.**
   - No two glosses are the same. Every gloss word shared between rows was listed, and the new rows were read by hand.
   - Near pairs kept on purpose:
     - well vs spring (water source);
     - floor vs storey;
     - hawk vs eagle;
     - murder vs kill;
     - fry, roast and bake vs cook;
     - mat vs carpet;
     - patient (sick person) vs patient, enduring;
     - acquaintance vs stranger vs friend;
     - pound (in a mortar) vs **monpa** "crush" (open question 2).
   - **One form collision** remains: the loan *league* **liga** against the root **liga** "phone". The root moves (rule of 2026-10-13).
2. **Every lexicon root is accounted for.** 519 rows = 502 in `concepts.tsv` + 17 operators excluded.
   - None was merged or dropped.
   - **tolin** widened to "nail, claw" and **tinli** narrowed to "key".
3. **Every logged decision is applied.** The round-1 table below, with the round-2 rows added.

| Decision (design log) | Applied where |
|---|---|
| Loans re-formed; metric units one set (10-13) | LEX kept loans: metre … litre, **kilometulu** |
| Currencies stay loans; **dolalu** | LEX kept loans: dollar, euro, yuan, rupee **lupiya** (rerun) |
| Seven loans → phrases, superseded in part by the audit | train, hospital, bicycle and electricity are LAD roots; percent is an ADD1 root; licence and contact stay phrases (not on the list) |
| Base vocabulary ~1,500: today's roots + first words + frequency | LEX + LAD |
| Moon/month | moon (ADD1); **dunan** = month (LEX) |
| Religion: shared concepts core, tradition words borrowed | church, mosque, pope, bishop, angel and prophet excluded as culture-bound (REL); religion is a root |
| soul, ghost, miracle, devil core | LAD roots + ghost (ADD1) |
| Word/language | word (ADD1); **apu** = language |
| Loan panel rules; coverage loans | 60 of the 62 panel passes are loans (tea and chemistry became roots by later decisions); pound a currency only; mile out; 38 of the 43 failures become native roots, the other 5 are borrowings by the first-word filter (giraffe, yogurt, sofa, pasta, zebra) |
| Remaining boundary cases | keep, request, lose (a contest), daytime, rule (ADD1); **nume** = life; **wupi**, **lula** narrowed (LEX); the band pairs keep two roots |
| Religion re-check / made consistent | bless, sin, hell, heaven, holy person and wonder are roots (miracle is built from wonder); holy/sacred is a root (BAL); idol is a phrase |
| Audit corrections | minute, second, hour, photo and degree are native roots (LEX step) |
| First-word filter | WB: 164 keep as roots (7 of them failed loans) and 23 as loans; 47 built, borrowed, duplicate or tradition are excluded |
| Percent root; inventory 2 (always, often, sometimes, never, later) | ADD1 |
| kilo everyday | LEX kept loan |
| Scope of two rules (**muyi** whole, a root for "period") | LEX **muyi**; LAD period |
| Older loans re-run | email kept; police becomes a native root; rupee **lupiya**; the other failures become native roots |
| Spelling alphabet | excluded as outside the core |
| Symbol names | **komu** and **asutagu** kept loans; @ = **mon**, dot = **mimi**; DIVIDE and LINE are LAD roots (divide, line) |
| No loan for mama | **mole** stays (LEX) |
| here / there | ADD1 |
| Large numbers stay native | LEX number roots (**munno tonen siwin**) |
| Tea gets an invented root | LAD step (route root) |
| tinli/yebin through ladder 1 | tinli settled by the button split; yebin pending |
| Short-word layer applied | the 17 operators stay out; the 26 digit-initial roots move anyway |
| Stop rule; the 51 added (holy a root) | BAL |
| Loan rule 5 of 7 regions | chemistry a root (now also a school subject) |
| Rates use "each" | rate (LAD root); ratio merged into rate |
| parent; mother and father stay; lie | parent and lie (ADD1/LAD 884.b); **mole**, **wede** (LEX) |
| Phrase line (b) | walk G; heap, nonsense, obstacle; receipt, available, priority roots; passenger a phrase |
| Everyone's modern life; WOLD route | WOLD |
| Walk stops at 1342 | WALK: 17 roots; G past the stop excluded |
| Three meals; sets pass planned | breakfast (LAD), lunch and dinner (ADD1); supper covered by dinner; sets pass in `sets.md` |
| Boundaries for the walk's concepts | WALK glosses: coal (charcoal built), depend, deny, pattern, comfortable, wild, ceiling, infection (virus stays a loan), urgent, attitude (opinion becomes a phrase), worthy (covers merit), welfare, discrimination |
| Boundaries for the 51; phrase or root | BAL: common split (shared = **pi we**), accuse+blame and include+contain one root each, attend/earthquake/shelter phrases, festival a phrase, unique, exceed, participate, familiar, summary roots |
| WOLD strong + clear edge; 20 more | WOLD-core 51 (+ fry, split), WOLD-edge 24, WOLD-codex 19; the other edge items excluded |
| WOLD follow-ups | cassava, millet/sorghum, deaf, mute (blind kept), order/command, relative, spider, shave, fish, herd (ADD1); young and sexed animals built; the 47 classified (WOLD-47) |
| "Through" = verb chain with "pass" | pass (LAD root) |
| Drops (10-16) | knight, senator, lieutenant, colonel culture-bound; statistics, psychology, circuit, orbit, formula, sphere long tail; the 10 mixed-sense items excluded; day and month names and last night excluded; receipt, available, priority roots; passenger a phrase |
| **WOLD boundaries and loans; the list's questions (10-16, round 2)** | BQ02 (15 roots; claw in **tolin**; **tinli** "key"; turn-off stays **tapi**); roast and fry two roots; LOAN02 (2 loans, 6 roots, 9 phrases, camel culture-bound); PL-retro (13 roots, 3 world compounds); SUBJ; general dropped, civic offices kept; sofa borrowed; defeat merged; harvest, refuse, stranger roots; pity and envy to `sets.md`; no pooled sense kept; saint = holy person; emergency kept; standard words loan candidates; operators out; tier cuts; added antonyms kept; data defects fixed (above) |

Not concept-list decisions, so nothing to apply here: grammar, sound, model, offensive, listening, process and documentation entries.

## Open questions for the author

1. **The sets pass** (`sets.md`): one proposal per set. Most say "no change"; these add or rebuild something:
   - **times of day:** a root for dusk, for parity with dawn;
   - **seasons:** all six built as **[season] + mark**, which overrides the phrase line for summer and winter;
   - **colours:** the five non-basic colours all built as mixtures;
   - **weather:** a root for cool, for parity with warm;
   - **emotions:** roots for surprise, "pity, compassion" and "envy, jealousy" (one root);
   - **kin:** name **pani** and **loyen** as the older/younger modifiers;
   - **numbers:** fractions are a grammar question.
2. **pound (in a mortar) vs monpa "crush".**
   - **The gap:** deeplayer-02 tested pound only against **payon** "hit". Against crush, CLICS has 2 families: 5.8%, too thin to decide. POUND/GRIND is 2.7% over 51 families.
   - **What I did:** kept the split as decided and narrowed the gloss to "pound (in a mortar)".
   - **Confirm**, or merge it into **monpa**.
3. **My world-compound calls on the retroactive phrase line.**
   - welcome, library and prime minister stay phrases; kingdom and childhood are roots (derivation is not a compound).
   - **Confirm**, or reverse any of them.
4. **WOLD phrases over 3 syllables.** deeplayer-01's P class was never put through the phrase line. These remain phrases: untie **benbi manfu**, hire **neke doku**, earn **dunu nimo**, stinking **kanko yomo**, draw water **yidu osa** (4 syllables each).
   - **My reading:** each is how most languages build it (the pass notes "most languages derive it"), so they meet the line as the world's compound.
   - **Confirm**, or send them through the line as roots.
5. **To the roadmap** (`docs/` was out of bounds here):
   - fractions (section 9);
   - the `tools/build.py` whitespace split;
   - the lexicon regloss of **tolin** and **tinli** at adoption;
   - the ladder rows for church, angel, bishop, prophet and idol, still never updated after 2026-10-13.

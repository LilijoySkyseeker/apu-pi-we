# Concept list 01: the final concept list for the ~1,500-root placement

Task: `PROMPT.md`. It consolidates every concept decision logged from 2026-10-13 to the end of `docs/design-log.md` into one list. Proposals only: nothing outside this folder changed, nothing is committed. Choices of mine are marked **(added)**.

## Progress

- [x] 1. Read the design log (2026-10-13 → end) and vocabulary-method §0
- [x] 2. Inventory inputs
- [x] 3. Build script `build.py` → `concepts.tsv`, `excluded.tsv`
- [x] 4. Checks
- [x] 5. README results and open questions

Rerun (about a second): `direnv exec /home/agent/work/repos/universal-language python3 tests/conceptlist-01/build.py`. It prints the totals.

## Files

- `concepts.tsv` has one row per concept that gets a content form in the placement. Its columns:
  - `concept`: the sense gloss.
  - `route`: root, loan, or kept loan.
  - `form`: today's form. A root's form moves in the placement; a loan keeps its form.
  - `field`: the lexicon's field names.
  - `tier`, `rank`: rank is the corrected canonical rank from coverage-02 `candidates.tsv`, where there is one.
  - `antonym`: from `antonyms.tsv` and the ladder. New pairs are marked "(added)", and the one pair taken from a decision is marked "(decided)".
  - `source`: the first tag is what admitted the concept; "also …" tags are later confirmations.
  - `note`.
- `excluded.tsv` has every concept that was considered and not given a root or loan, with a reason. Rows marked `pending:` wait on unfinished work, and rows marked `open question` wait on the author.
- `build.py`: all hand decisions are tables in it, each citing its log entry.

**Source tags.**

| Tag | What it is |
|---|---|
| LEX | `data/lexicon.tsv` |
| LAD | coverage-01 ladder pass (`part3/ladder.tsv`, roots-1500) |
| WB | first-word filter (`wordbank-final.tsv`) |
| LOAN | `loans-final.tsv` / `loans-rerun.tsv` |
| REL | religion decisions |
| ADD1 | coverage-01 `additions.tsv` |
| BAL | balance-02's 51 additions and their 2026-10-16 boundaries |
| WALK | walk round 2, G rows up to rank 1342 |
| PL | the 2026-10-16 phrase line |
| WOLD-core / -edge / -codex | the WOLD decisions of 2026-10-16 |
| WOLD-47 | the 47 walk-only meanings, classified here **(added)** |
| DROP | the 2026-10-16 drops |

## Totals

**1,505 concepts get a content form:**
- **1,422 roots.**
  - 478 keep today's form, which moves in the placement.
  - 944 are new.
- **83 loans.**
  - 18 kept from the lexicon.
  - 61 new, with panel forms.
  - 4 standard forms that don't have forms yet.

The placement places 1,422 roots around 83 fixed loans. 709 concepts are excluded, of which 38 are pending and 17 are open questions.

| Source (first tag) | Roots, today's form | Roots, new | Loans | Total |
|---|---|---|---|---|
| LEX (today's lexicon) | 478 | 6 (failed loans: hour, minute, second, photo, degree, police) | 18 kept | 502 |
| LAD: first words (with WB) | – | 164 | 23 | 187 |
| LAD: frequency segment | – | 545 | 37 + 4 standard | 586 |
| LAD/LOAN: 31 failed loans → native root, plus tea and chemistry | – | 33 | – | 33 |
| LOAN (pound, a currency only) | – | – | 1 | 1 |
| ADD1 (coverage-01 additions: splits, inventory 2, here/there, meals, parent, WOLD follow-ups …) | – | 28 | – | 28 |
| BAL (balance-02's 51, after boundaries) | – | 46 | – | 46 |
| WALK (round 2 G, ranks 1243–1342) | – | 17 | – | 17 |
| WOLD-core | – | 51 | – | 51 |
| WOLD-edge (no alternative) | – | 24 | – | 24 |
| WOLD-codex (20 added; 9-75 weave/plait shares weave's root) | – | 19 | – | 19 |
| WOLD-47 (walk-only meanings, deep-layer test, added) | – | 11 | – | 11 |
| **Total** | **478** | **944** | **83** | **1,505** |

- **Frequency route.** 1,400 concepts.
- **Deep-layer route.** 105: 94 WOLD plus 11 of the 47.
- **Against the design log's estimate.** The log expected "~1,450–1,470" from the frequency route. That figure was coverage-02's rough count. It did not subtract the first-word filter's 47 non-roots, the 2026-10-16 drops, the religion rows, or the merges found here, so 1,400 isn't a contradiction.

**Excluded (709) by reason:**

| Reason | Count |
|---|---|
| Phrase | 211 |
| Long tail | 183 |
| Covered by another word | 69 |
| Artefact (pooled English label) | 52 |
| Culture-bound | 48 |
| Pending | 38 |
| Grammar or construction | 36 |
| Past the walk's stop | 36 |
| Open question | 17 |
| Dropped (mixed senses) | 10 |
| Superseded by a later root | 8 |
| Outside the core (spelling alphabet) | 1 |

By source:

| Source | Excluded |
|---|---|
| WOLD | 316 (incl. 30 edge with an alternative, 11 from the 47) |
| LAD | 125 |
| WALK | 123 |
| BAL | 49 |
| WB | 47 |
| DROP | 21 |
| LEX | 18 (the 17 two-syllable operators + tinli/yebin) |
| Other | 10 |

**Tiers.** Tier 5: 15, tier 4: 67, tier 3: 327, tier 2: 671, tier 1: 425.
- **Today's roots** keep the lexicon's tier.
- **New concepts** take their tier from the corrected rank. The cut points are mine **(added)**, set from where today's roots sit in the corrected ranking (tier medians 10 / 74 / 302 / 520 / 900): ≤25 → 5, ≤150 → 4, ≤450 → 3, ≤900 → 2, beyond → 1.
- **First words** get at least tier 2, as `part4/placement.py` does.
- **Deep-layer-only concepts** (WOLD) take their tier from the rank of their head word where WOLD's label matched one (`pass.tsv` `freq_rank`, the walk's rank for the 47). Otherwise they are tier 1: by construction they are rare in the frequency data, and tier only weights how hard the placement works to keep a word apart.

**Fields** **(added)**: the ladder's extra fields are mapped to the lexicon's:

| Ladder field | Lexicon field |
|---|---|
| home, clothing, transport, tech, food | thing |
| food, raw produce | nature |
| place | space |
| society | people |
| money, work, art, religion | abstract |
| health | body |

- Person nouns go to people, verbs to action and qualities to quality, by hand lists in `build.py`.
- WOLD fields are mapped the same way, with part of speech fixed by hand.
- Every loan is filed under "loan", as the lexicon does.

## Checks

1. **No duplicate senses.**
   - No two rows share a gloss. Every gloss word shared between rows was listed and read by hand (the script's base-word scan).
   - **One duplicate was found and merged:** ladder **defeat**, whose own note says "lose a contest", is the same sense as **lose (a contest)**, split from **agi** (2026-10-13). It is now excluded as covered (question 3).
   - **Near pairs kept on purpose:**
     - party (gathering) vs celebrate;
     - match, contest / race / competition / lose (a contest);
     - level, degree vs degree (°);
     - nail (fastener) vs **tolin** (fingernail);
     - sink (go under) vs sink (basin);
     - plant/sow vs **pinfe** "plant";
     - boil (abscess) vs **binla** "boil".
   - The English-ambiguous labels carry sense glosses: the `GLOSS` table **(added)**, from the ladder notes.
   - **One form collision:** the loan *league* **liga** and the root **liga** "phone". By the 2026-10-13 rule (loans keep their forms, roots move) the root moves. The same rule covers *gas* **gasu** vs "idea" and *lamp* **lanpa** vs "cloud".
2. **Every lexicon root is accounted for.** 519 rows = 502 in `concepts.tsv` + 17 excluded.
   - **Kept:** 478 roots with today's form; 18 loans kept; 6 failed loans re-routed to native roots, with their loan forms retired (loans-rerun).
   - **Excluded:** the 17 two-syllable operators (**genso wanme inwun wemen konsin buntu tason nedin mesun manni buni donon lanno anko nuwen kiyo mena**), which `part4/placement.py` keeps fixed as part of the short-word layer.
   - **Merged:** none. Splits narrowed **dunan apu kuwi mido agi dili wabun** (already narrowed in the lexicon), and **nume** absorbed **pata** earlier.
   - **Dropped:** none.
   - `excluded.tsv` also records the pending ladder-1 check of **tinli**/**yebin**. Both stay roots meanwhile.
3. **Every logged decision is applied.** Each concept-list decision from 2026-10-13 to the end of the log, and where it is applied:

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
| tinli/yebin through ladder 1 | pending (excluded.tsv) |
| Short-word layer applied | the 17 operators stay out; the 26 digit-initial roots move anyway |
| Stop rule; the 51 added (holy a root) | BAL |
| Loan rule 5 of 7 regions | chemistry becomes a root; sofa is open (question 1) |
| Rates use "each" | rate (LAD root); ratio merged into rate |
| parent; mother and father stay; lie | parent and lie (ADD1/LAD 884.b); **mole**, **wede** (LEX) |
| Phrase line (b) | walk G; heap, nonsense, obstacle; receipt, available, priority roots; passenger a phrase; the composes entrants and ladder phrases checked (question 2) |
| Everyone's modern life; WOLD route | WOLD |
| Walk stops at 1342 | WALK: 17 roots; G past the stop excluded |
| Three meals; sets pass planned | breakfast (LAD), lunch and dinner (ADD1); sets pending (question 13) |
| Boundaries for the walk's concepts | WALK glosses: coal (charcoal built), depend, deny, pattern, comfortable, wild, ceiling, infection (virus stays a loan), urgent, attitude (opinion becomes a phrase), worthy (covers merit), welfare, discrimination |
| Boundaries for the 51; phrase or root | BAL: common split (shared = **pi we**), accuse+blame and include+contain one root each, attend/earthquake/shelter phrases, festival a phrase, unique, exceed, participate, familiar, summary roots |
| WOLD strong + clear edge; 20 more | WOLD-core 51, WOLD-edge 24, WOLD-codex 19; the 28 other edge items excluded |
| WOLD follow-ups | cassava, millet/sorghum, deaf, mute (blind kept), order/command, relative, spider, shave, fish, herd (ADD1); young and sexed animals built (WOLD P rows excluded); the 47 classified (WOLD-47) |
| "Through" = verb chain with "pass" | pass (LAD root) |
| Drops (10-16) | knight, senator, lieutenant, colonel culture-bound; statistics, psychology, circuit, orbit, formula, sphere long tail; the 10 mixed-sense items re-checked (none kept, question 6); the 14 day and month names and last night excluded; receipt, available, priority roots; passenger a phrase |

Not concept-list decisions, so nothing to apply here: grammar, sound, model, offensive, listening, process and documentation entries.

## Open questions for the author

1. **sofa and chemistry (5-of-7 rule, 2026-10-15: "roots or phrases").**
   - **The conflict:** the first-word filter (2026-10-13) had already made sofa a borrowing (culture-bound seating), so the 2026-10-15 entry and the filter disagree. Here sofa is excluded (open), and chemistry is a root, since no phrase meets the phrase line.
   - **A wider inconsistency:** physics (failed loan → native root, 2026-10-13) and chemistry are fields of study, like psychology and statistics, which the 2026-10-16 drops sent to the long tail.
   - **Options:** physics and chemistry roots (as here), or both long tail.
2. **Is the phrase line retroactive?** It decided the walk and four named items. Applied to older phrases, these are over 3 syllables and not world compounds:
   - **ladder "covered" rows:** century, kingdom, welcome, library (the ladder claims a world compound), childhood, patient (sick person), throne, corpse, giant, plain (land), prime minister;
   - **balance-02 "composes" entrants:** salary, delicious, fill, descend, acquaintance.
   - They are excluded here pending a decision. Gendered, kinship, season and colour phrases are held by decided rules or the sets pass and are not in this list.
   - Recommendation: apply the line, which gives roots to most of the 16. Each is a general concept the author's C1 cost rule favours.
3. **defeat = lose (a contest).** Merged as a duplicate (added). Confirm, or keep "defeat" as the transitive "beat someone" (now covered by **yiyin** "win (over)").
4. **The 47 walk-only WOLD meanings (my classification, added).**
   - **Roots:** steam, swallow, flour, bend, fold, hang, crazy (all ≥15 families); stretch and stranger (edge, with no short phrase); harvest (6/24 families, but farming households everywhere, and named in the 2026-10-16 entry); refuse (6/24, kept because the author separated deny and refuse).
   - **Out:** bay, tent, loyal, guilty, surrender, omen, descend/land (**deba** as a verb), "to last".
   - **Pending:** pity and envy, which go to the sets pass.
   - **Confirm:** harvest, refuse and stranger especially.
5. **Military and political titles.** The drops covered knight, senator, lieutenant and colonel. general (army rank) is the same class and is kept here. So are governor, mayor and minister. Drop it (and them)?
6. **The 10 mixed-sense items** (compound, grade, trial, single, term, deposit, review, promotion, medium, background).
   - My reading: no sense passes alone. The reasons per sense are in `excluded.tsv`.
   - The closest calls are "single" = unmarried (**su bedan**, 3 syllables) and "grade" = a school mark.
7. **saint.**
   - coverage-02 `drops.tsv` proposed **ewo [holy]**, but that phrase is 4 syllables, over the line. "Holy person" stays a root by the 2026-10-13 audit (item 3).
   - **Confirm:** a root next to "holy".
8. **emergency** stays a root. The 2026-10-16 note "an emergency in speech is **yo yo**" reads as the speech act, not the noun ("a medical emergency").
9. **WOLD's "20 more"** are 19 new roots. 9-75 weave/plait is weave's own root, and "boil (bubble)" in the README/log is WOLD 4-856 *boil, abscess*, not boiling (**binla**).
10. **Standard forms.**
    - planet, temperature, oxygen and mass are routed as loans from the standard (ladder 2 rung 1) but have no forms.
    - **Decide:** do they need the panel, or `names.py` on the standard name only?
    - Coverage-02's calibration rated oxygen N (long tail).
11. **The 17 two-syllable operators** are left out of the placement, following `placement.py`'s FIXED set, a choice not found in the log.
    - Some are ordinary adverbs: **manni** "usually", **tason** "rather", **nedin** "almost", **anko** "until".
    - The roadmap plans renaming **manni**/**konsin**.
    - **Confirm:** they stay with the short-word layer.
12. **Tiers.**
    - Today's roots keep their hand-set lexicon tiers rather than taking the corrected rank. Deep-layer-only roots are tier 1.
    - **Confirm both,** or re-tier everything from the rank.
13. **Pending work that can still add concepts.**
    - **deeplayer-02** is unfinished.
      - **BQs:** 16 open. Its table proposes two roots for 15 and one for claw (**tolin**); order/command is already decided.
      - **Loans:** the 18 haven't been run. Those that fail become roots or phrases.
      - **automatic:** the walk's loan candidate also waits on the panel.
    - **The sets pass:** seasons (spring, summer, autumn, winter are phrases today), colours (brown, pink), emotions (pity/mercy, envy/jealousy), weather, kin pairs, day and month names.
    - **tinli/yebin** through ladder 1.
    - Together these could add roughly 20–50 roots.
14. **Data defects found** (not edited: outside this folder).
    - `data/antonyms.tsv` has stale glosses: "day, daytime or 24 hours", "live, be alive or dwell", "ask" and "month; moon". I mapped the last to sun ↔ moon. It also holds number and senary confusion pairs, which aren't antonyms.
    - `religion.tsv`'s note column has text merged from other rows (bless, heaven, hell, sin).
    - The ladder rows for church, angel, bishop, prophet and idol were never updated after the 2026-10-13 religion decision.
15. **Added antonym pairs (marked):**
    - accept ↔ refuse, hate ↔ love, decrease ↔ increase;
    - sink ↔ float, lend ↔ borrow;
    - here ↔ there, always ↔ never;
    - bless ↔ curse, heaven ↔ hell;
    - appear ↔ disappear, keep ↔ lose (misplace).
    - **Keep or trim?** In the placement, antonym pairs are pushed apart with weight 30.

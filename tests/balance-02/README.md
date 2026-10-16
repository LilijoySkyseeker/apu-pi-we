# Balance audit follow-ups (balance-02)

Three follow-ups to the regional-balance audit (`tests/balance-01/`, Codex's reading in `codex-reading.md`), decided by the author 2026-10-15 (design log, "Regional balance audit: fix the instruments, recheck overrides, make the regional rule bind"). Task: `PROMPT.md`. Proposals only: nothing outside this folder was changed. Every choice of mine is marked **(added)**.

## Progress

- [x] 1 concept matching: `concepts_fix.py`; entrants judged in `concepts-entrants.tsv`.
- [x] 2 boundary overrides: `boundary_check.py` (`boundaries-recheck.tsv`), `clics_rates.py` (`clics-rates.tsv`).
- [x] 3 binding regional rule: `loan_rules.py` (`loans-rules.tsv`, `loans-rules-flips.tsv`).
- [x] README write-up.

Re-run everything from the repo root (each script takes a few seconds; `clics_rates.py` needs the CLICS4 archive, see part 2):

```
E="direnv exec /home/agent/work/repos/universal-language"
$E python3 tests/balance-02/concepts_fix.py
$E python3 tests/balance-02/boundary_check.py
$E python3 tests/balance-02/loan_rules.py
$E python3 tests/balance-02/clics_rates.py DIR   # DIR = cldf/ of CLICS4 v1.0 (Zenodo 19608447), unzipped
```

## 1. Concept matching

**Question.** Gloss labels that are strings of synonyms ("house, home", "fate, destiny") never merged with the one-word labels other languages use, so their weight was lost to the concept they name. How does the ranking change when they are merged, and what enters or leaves the ~1,500 list?

**What the defect is.** The " | " in the gloss files already separates a word's senses, and `concepts.py build` splits on it. The synonyms that didn't merge sit *inside* one sense, joined by commas: Wiktionary's first gloss, which `clean()` keeps whole ("marriage, wedding", "accusation, charge, allegation"). It is bigger than balance-01's below-cut counts suggested. 39,488 language-label pairs have a comma, and they carry 2% (Mandarin) to 58% (Tamil) of a language's weight (`concepts-comma-weight.tsv`): over 30% in 10 of the 20 languages, Europe's included (ru 45%, fr 31%). Because the ranking is the median over 20 languages, a concept whose weight is split across "fate", "fate, destiny" and "destiny, fate" can fall to the floor score (median share zero) though every language has it. Before the fix, 1,446 labels had a score above the floor. After it, 2,269 do.

**Method.**
- **Split and map.** Each comma label is split into its parts, with leading "to/a/the" dropped. A part is *known* when it is a label in `merged.tsv` or `merged-add.tsv`, the merged label set.
  - If every known part has the same canonical concept, the parts are synonyms, and the weight goes to the first known part's label (17,154 pairs).
  - If the known parts have different canonicals, the merge itself judged them distinct senses ("life, soul"; "see, to find"). They are not merged: the weight goes to the first known part only, the gloss's head word, and the later words get nothing (10,443 pairs). **This is the sense check (added).**
  - If no part is known, the label is left as it was (11,891 pairs, mostly Quechua and long definitions).
- **Rerun.** Then `concepts.py build`'s ranking is rerun unchanged: per language, text and speech averaged, the median of log shares. The result is in `concepts-fixed.tsv` (same columns as `concepts.tsv`). Check: without the fix the script reproduces `concepts.tsv`'s top 4,000 exactly.
- **Canonical ranking.** Canonical concepts are ranked as the merge ranked them, by their best label's rank. Spearman correlation is over the 2,335 canonical content concepts.
- **Regional correlation.** Recomputed exactly as balance-01 did, with the same top 3,000 labels and its tie-break. It reproduces balance-01's table to the third decimal.
- **The ~1,500 list.** `part2b/roots-1500.txt` is 235 first-word concepts, then 748 frequency candidates: canonicals in rank order with no root covering them. I rebuilt that frequency segment the same way from both rankings **(added)**. The rebuild of the original matches 739 of the 748. Entrants and leavers are the difference between the two rebuilds.
- **Sensitivity (added).** Two variants are run alongside:
  - *split*: distinct-sense parts share the weight by gloss order, as `concepts.py` weights a word's senses;
  - *canon*: on top of the fix, every merged label's share is summed into its canonical before the median. This is the same defect one level up: "big" alone ranks 1,692, because "big", "large" and "great" also don't combine across languages.

**Results.**

| Ranking | Spearman vs original (all canonicals) | over the original top 1,500 | enter / leave the list's frequency segment |
|---|---|---|---|
| fix (head rule) | **0.917** | 0.849 | 95 / 95 |
| split variant | 0.902 | 0.832 | 107 / 107 |
| canon-summed variant | 0.880 | 0.767 | 119 / 119 |

75 entrants are the same under all three rules, so the list of entrants doesn't hang on the sense rule.

Rank correlation with the final score, as balance-01 (`concepts-correlation.tsv`):

| Region | region mean vs final (before → after) | mean of its languages | final without the region |
|---|---|---|---|
| EA | 0.862 → 0.832 | 0.745 → 0.710 | 0.920 → 0.959 |
| SEA | 0.865 → 0.843 | 0.694 → 0.635 | 0.956 → 0.973 |
| SA | 0.815 → **0.851** | 0.624 → **0.710** | 0.968 → 0.968 |
| WA | 0.881 → 0.870 | 0.723 → 0.744 | 0.939 → 0.965 |
| EU | 0.897 → 0.893 | 0.795 → 0.816 | 0.918 → 0.955 |
| SSA | 0.799 → 0.754 | 0.574 → 0.563 | 0.978 → 0.977 |
| AM | 0.457 → 0.467 | 0.457 → 0.467 | 0.990 → 0.989 |

- **What changes.** South Asia gains most (Hindi .69 → .78, Tamil .54 → .68). No region's removal moves the ranking much any more: every leave-one-out figure is now at least 0.955, where Europe's and East Asia's were 0.918 and 0.920.
- **What doesn't.** Europe still tracks the final ranking most closely, so that lean wasn't an artefact. Sub-Saharan Africa still tracks it least.
- **Ties (added caveat).** Over half of balance-01's top 3,000 tie at the floor score, so these correlations partly depend on how ties are broken. Breaking ties by language count instead of alphabetically gives much lower figures for every region (EA 0.60, EU 0.66), though the regions keep the same order.

Each region's own top 1,000 content labels (`concepts-region-top.tsv`):

| Region | below the merge cut (before → after) | not on list, share of merged (before → after) |
|---|---|---|
| EA | 55 → 17 | .084 → .077 |
| SEA | 10 → 3 | .062 → .068 |
| SA | **174 → 3** | .075 → .073 |
| WA | 62 → 1 | .054 → .064 |
| EU | 33 → 5 | .078 → .062 |
| SSA | **213 → 22** | .081 → **.091** |
| AM | **549 → 284** | .100 → **.116** |

- **The defect is gone for SA and SSA.** It accounts for about half of AM's below-cut labels.
- **What is left for AM.** Quechua-only single labels the merge never reached: corpus artefacts (Julian, Gregorian, Inca emperor, Peruvian, Andes) and a real farming layer (farmland, sowing, fertilize, storehouse, dried corn, tame, baby animal).
- **The gaps that show now.** Once merged, Sub-Saharan Africa and Quechua show the most frequent concepts with no word:
  - SSA: wild animal, stranger, mercy, jealousy, cotton, bribe, deny, flour, powder, rub, cure, heritage;
  - AM: harvest, plough, sprout, candle, thigh, vein, reed, trunk, ancestor, calendar.

  This is the same home-cooking and farming gap that Part 5 found.

**Entrants** (`concepts-entrants.tsv`; my reading of each, **added**). Of the 95:
- **51 are genuinely missing.** About half are everyday and half formal or news words.
- **11 compose from today's roots** with no phrase listed yet: salary *nimo pi doku*, stupid *mu gole*, forbid *mu efon*, fill *muge kete*, decade *yawu fawu*, descend *isi deba*, delicious, funny, current, acquaintance, cooperate.
- **11 are already covered** by a root or phrase in the data files: hill **genne**, fun **luse**, yell **oyi dibon**, task **doku**, vision **nagu**, assistant **no yema**, develop **guge**, duty **keya**, primary **bawe**, superior **tisan**, text **kemin**.
- **18 are artefacts.** These are English homonyms that pool unrelated senses: staff (stick + personnel), charm (allure + amulet), decline (decrease + refuse + grammar), remainder (pulls in "remains" = corpse), deputy (vice + member of parliament), and also wonder, apply, acting, track, trace, fixed, fit, active, occupy, effective, civil, associate, deliver.
- **4 are rebuild noise:** lack, link, merit, medal are on the list already.

The missing everyday concepts worth a decision:
- **Feelings and morals:** hate, forgive, kindness, cruel, blame, fraud, fate.
- **Actions:** accept, avoid, guess, disappear, destroy, explode, celebrate, heal, obey, endure, decrease.
- **Things and events:** warm, thread, chain, bell, earthquake.
- **holy / sacred.** The 2026-10-13 religion decision made *sacred* a phrase as "too rare", at rank 3,982 (`religion.tsv`). That rank was the label "holy, sacred" alone. Merged, holy is canonical rank 588, in 17 languages. This is the same error the author already corrected for **bless** (4,731 → 1,138).

**Leavers** (95, all on the list today): spy, Thursday, cabinet, steel, tower, gene, continent, diamond, pilot, womb, grandchild, plastic, passport, mud, valley, vaccine, tunnel, software, parent, pink, piano, pope, mosque and others (`concepts-list-changes.tsv`). They fall from canonical ranks 857–1,235 to about 1,240–1,610: just past the cut, not out of range. Three are month or day names, which are phrases anyway (ladder, 8.3.3).

**Proposal.** Treat the 51 missing entrants, the everyday ones first, as candidates for the ladder pass, like the other candidates. Don't drop leavers on this evidence alone: the 1,500 is a knee in the coverage curve, not a hard cut. Separately, flag the *sacred* decision for a second look.

## 2. The boundary overrides

**Question.** balance-01 counted nine lumps in Persian and Turkish that a 2026-10-13 decision split. For each pair, was there evidence of a cost from languages that lump? Ladder 1 rung 3, safeguard 1, requires that evidence: "a language that never lumped two meanings can't show what lumping them costs". Where the evidence is thin, what does rung 4, the family-balanced fallback, give?

**Method.**
- **Recorded evidence.** I read the design log (2026-10-13: "Moon and month", "The remaining boundary cases", the religion entries), `vocabulary-method.md` §0, `research/notes/colexification.md` and `part3/religion.tsv`.
- **The data, re-read.** `boundary_check.py` reruns `boundary.py`'s own test unchanged, twice: as recorded, and with the part 1 comma fix. With the fix, "leg, the lower limb…" matches "leg", which makes Turkish *bacak* visible. I then read each language's words by eye, as `boundary.py`'s docstring asks **(added)**. The automatic "separate word" is often a gloss error (Thai มา "come", Indonesian *kamar* "room", Russian плечо "shoulder", Vietnamese *kim* "needle"), and the comma split adds noise of its own ("arm" = weapons).
- **Rung 4 rates.** These are recomputed from CLICS4 v1.0 forms (Zenodo 19608447, downloaded with a generic User-Agent, kept outside the repo). The method is the family-balanced rate of `tools/clics_rates.awk`, with 2,000 family bootstraps. It reproduces the note's LEG/FOOT 53.1 exactly, and ARM/HAND and MOON/MONTH within 0.3 points.
- **Copied forms removed (added).** A "no copies" variant drops the forms CLICS copies from a broad gloss ("FOOT OR LEG"). This is the inflation the colexification note warns of.

| Pair (overridden) | Rung that decided (recorded) | Lumper evidence recorded | Lumper evidence in the data, read by eye | Rung 4: CLICS4 family-balanced | Verdict |
|---|---|---|---|---|---|
| moon/month (fa, tr) | **rung 1** (calendar month), rung 3 agreeing | yes: 5 of 12 lumpers separate (zh ko ja yo ru) | the same five; fa ماه and tr *ay* are pure lumps | 69.9% (60–79), one word, but rung 1 comes first | **adequate** |
| day/daytime (fa, tr) | **rung 1** (the 24-hour day, named in rung 1's scope note) | none (not needed under rung 1) | fr *journée*; tr *gündüz* exists but is 4% of *gün*; fa روز is a pure lump | 52.9% (35–71; only 25 families) | **adequate under rung 1.** As a rung-3 case it would be thin, and rung 4 is a coin flip. |
| hear/listen (fa) | rung 4 in effect: the 20–50% band was deleted and the pair kept two roots | none per pair | ha *saurara* is the only clear one; tr *dinlemek* is in the data, so tr splits | 45.7% (36–55); 18% of resamples ≥50% | **thin; rung 4 gives two words** (the same outcome, near the line) |
| take/get (fa) | rung 4, as hear/listen | none | **fa itself separates:** برداشت *bardāštan* at 15% of گرفتن | 23.2% (15–33) | **not an override** (fa is lump+sep); rung 4 gives two words |
| arm/hand (fa) | rung 4, as hear/listen | none | none genuine (the vi *kim* and ha *hannunsa* readings are gloss errors) | 35.1% (28–43); without copies 27.6% (WALS 37%) | **thin; rung 4 gives two words** (the same outcome) |
| ghost/spirit (fa) | religion decision: "most languages have a separate word", which is evidence from splitters | none from lumpers | fa روح is a lump (جن "jinn" is a different being); tl *multo* separates | GHOST/SPIRIT 7% (4 families only); GHOST/SOUL 22.0% (14–32; 58 families) | **thin; rung 4 gives two words** on weak data (the same outcome) |
| leg/foot (tr) | rung 3: "modern use keeps them apart" | none per language | **tr itself separates:** *bacak* "leg" at 20% of *ayak* (hidden by the comma defect). tl *binti* separates too. fa پا is a pure lump (قدم is "step"). | 53.1% (46–60), but 23.4% (17–30) without copied forms | **not an override** (tr is lump+sep). Rung 4 can't settle it: 23–53%. |

- **The tally.** Of the nine Persian and Turkish overrides, two dissolve on reading the data: tr leg/foot (*bacak*) and fa take/get (*bardāštan*). Four were never modern-use decisions: moon/month and day/daytime for both languages go by the standard, rung 1. Three rest on thin lumper evidence (fa hear/listen, arm/hand, ghost/spirit), and for each the family-balanced fallback gives the same answer, two words. **No decision changes.**
- **What the audit found missing.** The *recording* is missing, not the outcome. The 2026-10-13 log entry says "modern use decides" for the band pairs without naming any lumper evidence. Rung 4 is what actually carries them.
- **leg/foot.** The decision stands either way: Turkish and Tagalog separate, and the copy-free rate is under 50%. If the author wants rung 4 alone to decide it, the CLICS figure needs a choice: the 53% that includes copies (the note's † rule calls it an upper bound) or the 23% without them, which leans toward splitters, because the dropped "FOOT OR LEG" sources are mostly lumpers.

**Moon/month, script against hand.** The hand reading in the design log (zh ko ja yo ru separate) is right.
- **Where the script is wrong.** Its th and id separations are gloss errors: Thai มา "come" (Thai's real moon word จันทร์ is 3% of เดือน, and mostly "Monday"), and Indonesian *kamar* "room". Hindi isn't an everyday lumper: चाँद "moon" and महीना "month" are the everyday words, and the lump is the literary माह.
- **What the script misses.** It misses zh and ja because their 月 is glossed as a function word (zh) or as "moon" only (ja, where ヶ月 is #fn).
- **Agreed.** Both readings agree on ko, ru and yo.

## 3. A regional rule that binds

**Question.** The loan rule is "≥12 of 20 across ≥4 of 7 regions". The regional part can never bind: the three largest regions hold 10 languages, so any 12 languages span at least 4 regions. Which rules would bind and serve N3/C1? The goal's wording for what they serve is B5: "convergence across unrelated languages… keeps the language fair to every culture", and L4: "only when the world already shares its form". For each rule, what flips among the loans judged so far?

**Method.**
- **The loans.** All 189 loans judged so far, with the columns each test counted:
  - 109 coverage candidates and 14 older lexicon loans, plus the 8 metric units: balance-01's `loans-per-loan.tsv`, which matches `loans-final.tsv` and `loans-rerun.tsv`;
  - the 18 symbol forms in `tests/symbols-01/panel.tsv`;
  - the 40 imitative and nursery forms in `tests/imitative-01/panel.tsv` (sourced columns, as each `emit.py` counts).
- **What changes.** Each rule keeps "≥12 of 20" and replaces only the regional part, so it can only fail a loan, never pass one. 89 loans reach 12/20 today.
- **Families (added).** Rule B uses Glottolog top-level families: Sino-Tibetan, Japonic, Koreanic, Austroasiatic, Tai-Kadai, Austronesian (id tl), Indo-European (hi bn fa ru es fr), Dravidian, Afro-Asiatic (ar ha), Turkic, Atlantic-Congo (sw yo), Quechuan. That is 13 families, and Indo-European has 6 of the 20 languages.

| Rule (added) | Flips (pass → fail) | of which adopted today |
|---|---|---|
| R0 now: ≥4 of 7 regions | 0 | – |
| **A. Regional depth:** ≥5 regions where at least 2 of the region's languages share the form (at ≥4 regions it never binds either: 0 flips) | 13: motorcycle, sofa, lamp, sugar, toast, T-shirt, pound, cigarette, chemistry, gene, vaccine, .com, hashtag | 12 (sofa already failed on thin columns) |
| **B. Families:** ≥7 of the 13 families, a majority, each family once | 7: doctor, project, design, restaurant, cigarette, chemistry, platform | **5**: doctor, design, restaurant, cigarette, chemistry (project and platform already failed) |
| **C. No single region decides:** the rest of the panel still reaches 60% without any one region | 22: doctor, sofa, lamp, tomato, sauce, sugar, toast, T-shirt, office, program, project, beer, code, design, restaurant, cigarette, campaign, chemistry, platform, kilo, hashtag, mama | 18 |
| **D. Spanish and Quechua count once** (loans.md pattern 2: the assumed Spanish loan "gives Spanish two votes") | 5: lamp, tomato, project, restaurant, campaign | 3: lamp, tomato, restaurant |

Per-loan detail is in `loans-rules.tsv`, and the flips with region and family counts are in `loans-rules-flips.tsv`.
- **Sensitivity.** B at 8 families flips 14 (adding lamp, sugar, bank, program, machine, code and *mama*). B at 6 flips none.
- **Not computed: "spread only through one colonial language".** The panel columns don't record the donor language, so it can't be computed. D is its narrow, recordable case.

**Reading the options.**
- **A** rewards depth inside a region. It punishes exactly the regions whose columns are thin for sourcing reasons, Hausa and Yoruba (balance-01's limits), so it would sharpen an instrument bias. It also fails *.com* and *hashtag*.
- **B** removes the loans whose spread is one lineage (Indo-European) plus contact languages. Doctor's 13 columns are 6 Indo-European languages plus Austronesian, Dravidian, Arabic, Turkish and two Bantu/Atlantic-Congo languages, with no East Asia and no Quechua. The flips are the loans balance-01 showed East Asia and Africa missing from.
- **C** is the strictest. In effect it raises the bar to about 14, and it fails *mama* and hashtag too.
- **D** fixes one recorded double vote and nothing else.

**Recommendation: B, at least 7 of the 13 families, replacing "4 of 7 regions".**
- **Why it fits.** It binds: 5 adopted loans flip. It measures what the regional clause was meant to measure, sharing across *unrelated* languages (B5). It is the same family balancing that ladder 1 rung 4 already uses, so it adds no new kind of rule. It counters the Indo-European multi-vote behind the European lean balance-01 found, without quotas (N3) and without penalising thinly sourced regions.
- **What it costs.** The five flipped concepts go down ladder 2: doctor, design, restaurant, cigarette and chemistry would take native roots or phrases. loans.md already lists "food house" for restaurant.
- **Add-back trigger** for the region clause: a passing loan whose families are many but all in one region.

## For the author

1. **Concept list.**
   - The comma defect was large: 2–58% of each language's weight, Europe's included.
   - Fixing it moves the ranking modestly (Spearman 0.917) and evens out the regions' pull on it, with South Asia gaining most. Europe still tracks the ranking most closely.
   - **Decide:** whether the 51 genuinely missing entrants go to the ladder pass (the everyday ones are listed in part 1), and whether **sacred** gets a second look (rank 3,982 → 588 once merged, the **bless** pattern).
   - The leavers can stay; they are just past the cut.
2. **Boundaries.**
   - No decision changes. Moon/month and day/daytime rest on rung 1. Turkish leg/foot and Persian take/get were not overrides: both languages separate, which the comma defect hid.
   - Persian hear/listen, arm/hand and ghost/spirit had thin lumper evidence, but rung 4 gives two words for each.
   - What's missing is the *record*: the band pairs went to rung 4, not to modern use.
   - Moon/month: the hand reading is right.
3. **Loan rule.** Recommended: **≥12 of 20 across ≥7 of 13 language families.** 5 adopted loans would lose their loan status: doctor, design, restaurant, cigarette, chemistry. The alternatives are A (depth, 12 adopted flips), C (no region decides, 18) and D (Spanish-Quechua once, 3).
4. **Flag, once.** The regional clause decides nothing today. Deleting it and keeping 12/20 changes no verdict, and is the five-steps answer. The author asked for a binding rule, so B is offered; its add-back trigger is in part 3.
5. **To track in the roadmap** (not edited here):
   - `boundary.py` has the same comma defect (Turkish *bacak*, *dinlemek* were invisible);
   - `concepts.py` ranks synonyms separately across languages, which is the canon-summed variant above ("big" ranks 1,692 alone);
   - balance-01's correlations depend on how floor ties are broken.

## Limits

- **My judgement.** The sense check, the entrant judgements, the eye readings of the boundary words and the family assignments are mine.
- **The head rule** can still pick a homonym's wrong sense, when the first known word is ambiguous. The 18 artefacts are the visible cases.
- **CLICS rates** for day/daytime (25 families) and ghost/spirit (4 families) are thin.
- **The loan rules** are tested only on loans already nominated, and nomination was English-led (balance-01, Codex). No rule here fixes that.

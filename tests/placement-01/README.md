# Placement 01: all content forms for the final concept list, placed together on model v2

Task: `PROMPT.md`. Proposals only: nothing in `data/` or `docs/` changed, nothing committed. **added** marks my choices.

## Progress

Resumable: every step writes `state/*.json` atomically (tmp + rename) and resumes from it; rerun the same command.

- [x] 0. read inputs and the design log from 2026-10-13
- [x] 1. `bigrams.py` → `bigrams.tsv` (grammar word + content word counts, for the haplology rule)
- [x] 2. `place.py medians` → `state/medians.json`
- [x] 3. `place.py start` → `state/A.json` (today's valid roots kept, the rest added one at a time); `start --no3` → `state/A-no3.json`
  - first try (3,000 random three-syllable candidates per word) was too slow; kept as `state/A-old-k3000.json`, not used
- [x] 4. `place.py descend SEED` → `state/C-{1,2,3}.json`; `descend SEED --no3` → `state/C-no3-{1,2}.json` (12 sweeps each, ~50 min)
- [x] 5. `report.py` → `report.txt`, `forms.tsv`; `report.py --no3` → `report-no3.txt`, `forms-no3.tsv`; `keepcheck.py`
- [x] 6. results below

Commands (from this folder): `direnv exec ../.. python3 place.py start`, `… place.py descend 1`, `… report.py`.

## Headline

| | today (519 words) | one at a time (A) | joint (C, proposed) | joint, two syllables only (sensitivity) |
|---|---|---|---|---|
| robust score R (1.0 = random lexicon of the same size) | **0.394** | 0.114 | **0.061** | 0.186 |
| J (robust confusion + length effort) | – | 33.9 | **27.8** | 38.2 |
| three-syllable roots | 0 | 617 | **663** (45%) | 0 |
| near pairs, robust (above today's 99th pct) | 1,249 of 125k pairs | 4,037 of 586k | **3,247** of 586k | 11,713 of 1.11M |
| near pairs, best variant | 1,249 | 3,868 | 3,157 | 11,017 |
| B2 margin (single-feature neighbours that are words), roots | 0.14% (4/2,789) | 0.06% | **0.00%** (0/9,968) | 0.00% (0/8,635) |
| p-initial roots | 15 of 478 | 36 | **37** of 1,457 | 66 of 1,457 |
| today's roots moved | – | 104 (forced) | **357** of 478 (104 forced) | 262 (104 forced) |
| offensive.matches (tie-break only) | 76 of 478 | 112 | **114** of 1,457 | 148 |
| seeds agreeing on a root's form | – | – | 14% (206 of 1,457) | 52% |

R for runs with three-syllable roots is flattered: the random baseline puts every root at two syllables. J compares C with the two-syllable run fairly (same units): 27.8 vs 38.2.

Checks on C: unique drift keys, no senary key, every later syllable has an onset, no blocked form, **haplology + digit check passed** (no root starts with **mu ni sa de wo ma** or a banned grammar syllable). `juncture.py` on the result (run on a copy of the lexicon, `report.py`): exit 1, **every problem is in fixed words**: digit + word **de nun / de no** ~ the loan **denu** "gene" (starts with digit 3), and six grammar -n pairs (**ta/tan, fo/fon, yo/yon, ka/kan, ya/yan, fi/fin**) from the short-word layer. Check 3 (-n + vowel) passes. Full numbers and lists: `report.txt`, `report-no3.txt`.

## For the author

1. **Three syllables for 45% of roots.** Under the inherited length term (EFFORT 0.02 per extra syllable × frequency), at 1,457 roots the two-syllable space is crowded enough that a three-syllable form is cheaper for almost every tier-1 root (420 of 429), a third of tier 2 (233 of 632) and every number word. All 663 are open syllables, 502 vowel-initial (V.CV.CV): the length term charges 0.4 for a final -n and gives −0.1 for a vowel start, and the three-syllable space is empty enough that the length term alone picks among forms. They carry a quarter of the model's frequency weight (less of running text; tier weights are flatter than Zipf). Rule 5 asked for this trade-off, but the result reshapes the lexicon; the two-syllable-only run (`forms-no3.tsv`) is the alternative, at J +38%. **Not a v2 effect** as far as I can tell: v1's random-lexicon confusion is ~1.5× v2-best's (189 vs 123 for the full list), so v1 would push at least as hard (inferred, not run). The weight to revisit is EFFORT (or a cap: three syllables only for tier 1).
2. **Number words go to three syllables** (all but 10): 6–9 **dinome wiwali unune imasi**, 100 **mekole**, 1000 **mogawe**, POINT, MINUS, POWER, 10^6, 10^9, and the number-field roots (average, sum, amount, rate, percent, pair); only 10 keeps **yawu**. The ×10 weight for *any* pair with a number word (placement.py; build.py's original also had ×30 number–number) was set for 500 words; against 1,555 it outweighs the effort. Putting 7 back at **oma** alone costs +20% of J. Digits 0–5 are one syllable and 6–9 would be three, with no shared pattern. Needs a decision (fix 6–9 and 10/100 at two syllables, or rescale ×10).
3. **The language's name moves**: **apu** "language" → **sote** (unforced; keeping **apu** costs +0.19% of J). The log says the name is settled after this placement; I'd lock it.
4. **Most unforced moves are arbitrary.** Three seeds agree on 14% of forms (two-syllable run 52%). 253 of today's roots moved without a rule forcing them. Keeping a frequent root costs little one at a time (`keepcheck.py`): house **guyi** +0.05%, want **momu** +0.15%, language **apu** +0.19%, work **doku** +0.25%, many **feli** +0.47%, food **pasu** +0.49%, good **upe** +0.71%, big **kudu** +0.90%, think **pume** +1.43%, can **lenu** +2.25%. Recommendation: rerun with a keep term, as the short-word rebuild did (Decision 2, keep 0.01).
5. **Frequent words whose form reads oddly** (C): can **lenu → utu** (tier 5 now a bare V.CV), good **upe → uba**, thing **musu → ado** (forced: **mu** is 0), do **muge → nufi** (forced), know **lugo → yuse** (forced: **lu** OR), think **pume → kune**, place **kemu → fela** (forced: **ke** MORE), time **muyi → fipa** (forced), 7 **oma → wiwali**.
6. **Antonym pairs**: none is a near pair (the closest, near/far **gelu~linu**, is 6e-5 best variant, a third of the near-pair threshold). Today's worst, stand/sit **kolu~goyu** (3e-3), is fixed: **wiyu~doyu**. Next: tell/ask **iko~mido**, start/end **duko~fuki**, fast/slow **yeyan~ledon**, buy/sell **ugowu~ewuwo**.
7. **Near pairs among frequent words** (robust, both tier ≥ 3): grind/market **bute~wupe**, tree/world **wati~wabi**, bark/coffee **tase~kafe** (loan), head/sibling **tefu~pesu**, fire/relationship **nusu~mosu**, start/village **duko~wuko**, fear/past **nupa~nuda**, life/crime **nume~nuye**, need/okay? **wuli~buni** (operator). The worst pair overall is between two fixed words: **kilo** (loan) ~ **kiyo** (operator), 2.9% robust; also **komu~kodu** (loans) and near/gene **gelu~denu**.
8. **p-initial roots stay rare**: 37 of 1,457 (2.5%), 66 (4.5%) in the two-syllable run, against ~7% if onsets were even. Two causes: the haplology rule bans **pi** and **pon**, and v2 makes p costly (p/b voicing, f/p, the no-p listener group). In the two-syllable run p is the rarest onset (t 128 … p 66).
9. **The haplology threshold** (≥10 of 930 grammar + content bigrams) bans 22 first syllables: **dan don fan fun gen gi gun ke la lu mon nan no pi pon se sin su to wan we yen**. **le** (ONGOING), named in the 2026-10-15 decision, stands before a content word only twice in the corpus, so it isn't banned. 16 loans and 3 operators start with a banned or digit syllable and keep their forms (rule 2): `report.txt`.
10. **Offensive matches**: 114 roots (7.8%) against a base rate of 12% of valid forms; the 2% tie-break can't do more. Today's roots: 76 of 478.

## Method

| part | source |
|---|---|
| 1,538 concepts with a form or to place: 1,457 roots (all re-placed), 81 loans (fixed), plus 17 operators from `data/lexicon.tsv` (fixed) | concepts.tsv; rule 2 |
| 4 loan candidates (planet, temperature, oxygen, mass) left out | **added**: no form until the panel decides; a failed one goes through `words.py add-content` |
| number words (6–9, 10, 100, 1000, 10^6, 10^9, POINT, MINUS, POWER) placed as roots | concepts.tsv ("placed with the roots"); **added** reading of rule 2: "digits fixed" = the one-syllable digits 0–5 |
| objective: per variant conf_v = Σ W_ij f_i P_v(i→j), same length only, first syllable `S_initial`, later syllables `S_internal`; R = mean of the worst 12 of 48 of conf_v / med_v | rule 1; confusion2.variants() (48) |
| med_v: median over 200 random lexicons (every root at a random valid two-syllable form, loans and operators fixed) | shortwords-03 method; **added**: 200 draws (they took 20 s) |
| J = med_best × R + EFFORT Σ f_i (length_i − 2) | **added**: med_best puts R back into the units the effort term was set in. Exact robust score at every step, no approximation needed (a word's 48 cost grids take 0.03 s) |
| W: same field ×3, antonym ×30, any pair with a number word ×10; f = TIER_FREQ | rule 1, placement.py |
| antonyms: `data/antonyms.tsv` + the concepts.tsv antonym column (150 pairs) | **added**: the column has 71 pairs the file lacks |
| hard rules: unique drift key incl. senary; not `offensive.blocked`; first syllable not a digit or a banned grammar syllable; later syllables have an onset; juncture.py check 3 (no X and nX both words, since grammar -n pairs exist) | rules 2–3; juncture checks 1 and 2 concern digits and grammar words only |
| haplology: grammar word's syllable banned as a first syllable if it stands right before a content word ≥ 10 times in the corpus | design log 2026-10-15; **added**: `adjacency.tsv` counts only short + short, so `bigrams.py` recounts the same corpus (reference examples + UDHR, new forms) for short + content; threshold ≈ 1% of the 930 such bigrams |
| C3 tie-break: among forms whose marginal J is within 2% of the best, prefer one without `offensive.matches` | rule 4, words.py `pick` |
| three-syllable forms: considered when the best two-syllable marginal exceeds 0.9 × the one-syllable effort; 400 candidates per word, half V.CV.CV, half any valid form, plus the current form | **added**: 2.3M forms can't be gridded per word; the space is sparse enough that the length term decides |
| A: today's valid roots kept, the rest placed one at a time in list order (what words.py would do); C: coordinate descent over all roots from A, random order per sweep, 12 sweeps, seeds 1–3, lowest J kept | strategy C of part4/placement.py; **added**: seeds and sweep cap (moves fell to 14–36 per sweep, not zero: the three-syllable candidates are resampled) |
| two-syllable-only run | **added**: comparison for item 1 |
| today's score: all 519 words of `data/lexicon.tsv`, random baseline of 519 | **added**: the "517" of the prompt is an older count |
| near pairs: same-length pairs, symmetric P(i→j)+P(j→i), best variant and robust (worst-quarter mean), threshold today's 99th percentile | part4/placement.py; robust version **added** |
| B2: neighbours by voicing, e/i, o/u, m/n, f/p, l/y/w, ±final n in any syllable; "real" = any content form | unknown-unknowns.md #9 (today: 0.14% here vs 0.2% there, on an older lexicon) |

## Files

`bigrams.py` → `bigrams.tsv`; `place.py` (rules, objective, placer, start, descend); `report.py` → `report.txt`, `forms.tsv` (C-3), `report-no3.txt`, `forms-no3.tsv` (C-no3-2); `keepcheck.py` (cost of keeping a frequent root); `state/` (A, C and medians, resumable); `logs/`. `forms.tsv`: concept, old form, new form, field, tier, route; the 17 operators at the end.

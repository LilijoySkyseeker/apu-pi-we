Task: apply a stated test to the 235 first-word concepts that the coverage study admitted as new Apupiwe roots on the children's-word checklists (Wordbank) alone. Decided by the author 2026-10-13 after a decision audit found culture-bound childhood items (pacifier, stroller, crayon) admitted as roots while rare but shared concepts were cut.

Repository: /home/agent/work/repos/universal-language/
Input: the first 235 lines of tests/coverage-01/part2b/roots-1500.txt. Context: tests/coverage-01/wordbank.tsv (Wordbank checklist counts and categories, 30 languages), tests/coverage-01/concepts.tsv (adult frequency rank across 20 languages; note it undercounts home life, which is why Wordbank was added, and some labels are split, e.g. fridge vs refrigerator), docs/vocabulary-method.md §0 and §1 (the deep-layer criterion is convergence of independent signals), the "culture-bound concepts" rule in §0 (what belongs to one culture comes from that culture's own words through borrowing), research/notes/concept-sources.md (how CLICS4 lineage coverage was computed), docs/goal.md (N3: don't weight cultures by size).

The test. Keep a concept as a root if any of these holds, and say which:
1. a basic action or state (lick, wipe, sweep, hug, sleepy…);
2. a body part;
3. a thing, food, animal or place found in ordinary households or surroundings across most cultures today (scissors, bucket, broom, stairs, pot, beans, maize; not region-bound species or dishes);
4. named across many language families: CLICS4 area-balanced lineage coverage, where the concept is in CLICS (fetch the CLICS4 CLDF data from its public release if needed; cite the figure).
Otherwise mark it **culture-bound**: a thing tied to some cultures' childhood, food, climate or institutions (stroller, crayon, pacifier, bib, potty, snowman, fire truck, lollipop, pancake, porridge…). Culture-bound concepts are said with a borrowing or a phrase, not a core root. Also flag concepts that duplicate an existing root or another entry, or that the loan panel already decided (tests/coverage-01/part3/loans-final.tsv).

Output tests/coverage-01/part3/wordbank-filter.tsv: `n  concept  verdict  criterion  evidence  note` (verdict keep / culture-bound / duplicate / loan), one row per concept in input order, appending in chunks of 40; resume after the last row if the file exists. Be consistent: apply the same standard to every concept, and when unsure say so in the note rather than guessing. Do the work yourself, no background helpers. When done, reply with counts per verdict and the culture-bound list.

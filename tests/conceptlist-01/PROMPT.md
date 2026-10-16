Task: consolidate the final concept list for the ~1,500-root placement, applying every decision logged so far. Repo /home/agent/work/repos/universal-language. Work in tests/conceptlist-01/; don't edit data/ or docs/; don't commit. Progress section in README.md (resumable; the host has crashed before). Do the work yourself. Dev shell for tools (`direnv exec /home/agent/work/repos/universal-language python3 …`). No web needed. Mark choices of yours "added".

Read docs/design-log.md from 2026-10-13 to the end (the source of truth for every decision), docs/vocabulary-method.md §0, and these inputs:
- today's lexicon: data/lexicon.tsv (roots and loans), data/compounds.tsv, data/antonyms.tsv;
- the coverage list: tests/coverage-01/part2b/roots-1500.txt, tests/coverage-01/part3/ladder.tsv, additions.tsv, pending-splits.md, religion.tsv, loans-final.tsv, loans-rerun.tsv, wordbank-final.tsv;
- the balance fix: tests/balance-02/ (concepts-entrants.tsv; the 51 additions);
- the walk: tests/coverage-02/ (round 1 additions.tsv; round 2 walk-r2.tsv, its G rows, and the phrase-route reclassifications);
- the WOLD pass: tests/deeplayer-01/pass.tsv (core D, the 24 edge D with no alternative, the 20 added after Codex's check: listed in its README), plus the 47 meanings covered only by the walk's proposals (classify each by the deep-layer test);
- the drops and re-checks decided 2026-10-16 (pooled senses compound, grade, trial, single, term, deposit, review, promotion, medium, background: keep a sense only if it passes alone; receipt, passenger, available, priority by the phrase line);
- tests/deeplayer-02/ if it has finished (17 boundary questions, 18 loans); if not, list those items as pending.

Output:
1. tests/conceptlist-01/concepts.tsv: one row per concept that gets a content form in the placement: concept (sense gloss, unambiguous), route (root / loan / kept loan), today's form if any (roots move; loans keep their forms), field (the lexicon's field names), tier (1–5, from the corrected ranking where available; deep-layer-only concepts: say how you set it), antonym (where a pair exists: existing antonyms.tsv plus obvious new pairs, marked added), source (which decision or list admitted it).
2. tests/conceptlist-01/excluded.tsv: concepts considered and not given a root, with the reason (phrase: give it; long tail; culture-bound; dropped; covered by …).
3. README.md: totals by route and source; checks (no duplicate senses; every lexicon root either kept, merged or dropped with a reason; every logged decision applied: list them with where); and **open questions for the author** (anything undecided or contradictory). Reply with the totals and the open questions.

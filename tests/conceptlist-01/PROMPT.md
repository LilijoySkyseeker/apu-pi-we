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

## Round 2 (author, 2026-10-16)

The author approved every open question and the deeplayer-02 calls: read the last two design-log entries ("WOLD boundaries and loans, and the consolidated list's questions", and before it the drops and boundary batches). Then:
1. **Rebuild** concepts.tsv and excluded.tsv with everything folded in: deeplayer-02's boundary results (bq.tsv) and loans (loans.tsv) as decided; roast and fry as two roots; the retroactive phrase line; school subjects; civic offices kept, military ranks dropped; standard words as loan candidates pending the panel (mark them); the antonym pairs kept. Keep build.py the single generator.
2. **Fix the data defects** you found: in data/antonyms.tsv correct stale glosses to the lexicon's current glosses (keep the file's format; move the number-confusion pairs out only if a tool doesn't read them: check tools/ and tests/coverage-01/part4/placement.py first and say what you did), and the garbled notes in tests/coverage-01/part3/religion.tsv. You may edit those two files.
3. **The sets pass, proposals only** (design log 2026-10-16, "sets are handled as sets"): list the sets (meals, times of day, days of the week, months, seasons, compass directions and left/right, kin, body parts, colours, weather, emotions, senses, numbers-adjacent words, opposites), and for each: its members, how each is covered today (root / phrase / loan / missing), whether the set is complete and on one level, and a proposal where members disagree (e.g. envy/jealousy, pity/mercy, seasons beyond the temperate four: wet and dry season, day and month names). One proposed decision per set. Write sets.md.
Report: new totals, what the fixes changed, and the per-set proposals in a short table. Don't commit.

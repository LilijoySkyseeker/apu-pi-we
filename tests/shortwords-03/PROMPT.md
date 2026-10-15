Task: rerun the short-word rebuild dry run on today's setup, so the author can make "Decision 2" (full rebuild, a middle option, or the minimal patch) and settle whether to keep the name **apu pi we**. Repo: /home/agent/work/repos/universal-language. Work in tests/shortwords-03/ (new); reuse tests/shortwords-02/ code by copying or importing it, don't edit shortwords-02's results (it's the record of the first dry run).

Read first: tests/shortwords-02/README.md (the dry run: method, rules, options, findings, the decisions it left), and the last entries of docs/design-log.md from 2026-10-14 on (what changed since). Changes to apply:

1. **Offensive filter, tiered** (design log 2026-10-15): `offensive.blocked(form)` is now the hard list (5 one-syllable forms: ku kun lan lun lon, plus REJECTED); those forms are illegal. Every other match is `offensive.matches(form)`, a tie-break only (goal C3): use it as the small soft penalty the dry run called "C3 mode". There is no "hard" offensive mode any more.
2. **Mishearing model:** `tools/confusion2.variants()` now returns 50 variants (two listener groups added: face-to-face `src-av` and low-pass `src-lp`, both built as study deltas on mix4; research/notes/confusion-data.md §8.5, §9.5). Use all 50 for the robust score (CVaR 0.25, normalised by random-layer medians, as before).
3. **Positions:** tests/shortwords-02/positions.py had a bug (GF "command not parsed" counted as a parse; quote marks in frames), fixed in the code on 2026-10-15. Rerun its substitution step (slow: ~30 min on 14 cores; results into tests/shortwords-03/) and use the new substitution.tsv, frames and adjacency.
4. **Frequencies:** unchanged (checked 2026-10-15, tests/grammar-rebuild/codex/).

Runs (keep the dry run's annealing settings and seed counts unless you have a reason, and say it):
- **full** rebuild (C3 mode).
- **middle** options: the keep-penalty sweep (at least 0.02 and 0.04, plus one more point if the curve needs it).
- **minimal patch** (every merger pair removed).
- Each of the above **twice**: free, and with the name locked (**pi** = OF and **we** = ALL keep their forms; **apu** is a content word and isn't in this layer). Report the cost of the lock.
- **Checks the dry run skipped** (research/notes/confusion-data.md §6.5, §6.6; tests/shortwords-02/README.md "Not done"): one-at-a-time sensitivity of the winning layers to the model's main parameters, and a hold-out check (optimise on half the variants, score on the other half; report whether the ranking of options survives).
- **Drop test for the new listener groups** (design log: "if the variant changes no form in the short-word rerun, drop it"): for the recommended option, rerun without src-av, and without src-lp, and report how many forms change.

Report in tests/shortwords-03/README.md, in the dry run's format: a headline table (option, words changed, robust score, merger pairs, offensive tie-break matches, the name), the old → new forms table, pairs fixed, operators that would need renaming (**mesun**, **mena** share **me**'s position), digit/content clashes, the checks' results, the drop test, and a short "for the author" section with Decision 2's options and a recommendation, plus the name question. Mark every choice of yours as "added" with its reason. Keep a Progress section at the top (resumable).

Run tools in the dev shell: `direnv exec /home/agent/work/repos/universal-language python3 …`. Change no file outside tests/shortwords-03/. Don't commit. Do the work yourself (no background helpers). No web access is needed; if you use it, use a generic User-Agent and never the owner's email or name. When done, reply with the headline table, the name-lock cost, the checks' verdicts, the drop-test result and your recommendation.

# Cold adversarial review (2026-10-11 to 10-12)

The author asked for the language to be reviewed against its goal (`docs/goal.md`) by agents who had never seen its design notes, then defended, then judged. The verdict (`reports/C-verdict.md`) is **keep with repairs**; the repair batch that followed is logged in `docs/design-log.md` ("Review repairs", from 2026-10-12) and its open items are in `docs/roadmap.md`.

## How it was run

- **Cold packets.** Each reviewer saw only what its role needed, with the name removed and no links to notes, site or repo: the goal alone (designers A1, A2, A8), the goal plus the reference, word lists, lessons and the UDHR translation (A3, A4, A5, A7), or the goal plus the rationale and research notes (A6). The packets themselves aren't kept here; they were copies of the repo's files at the time.
- **Roles.** A1, A2: design the best language from the goal alone (opus, sonnet). A8: the same, prompted and reporting in Chinese (opus). A3: compare the three designs with the built language. A4: typology (is it built from what many languages share?). A5: complexity (what could go). A6: fact-check every cited claim (52 claims; helpers' batches in `reports/A6-helper-*`). A7: what native speakers would change (fable). B: the defender, with the full repo. C: the judge, cold, reading A and B (fable).
- **Isolation.** Every prompt ends with `prompts/_checkpoint.md` (work in checkpoints so an interrupted agent resumes; never open another reviewer's report). `audit.py` checked each agent's transcript for files read outside its packet and fetches that mention the language. A5's first run opened A1's report; it is kept as `A5-complexity-run1-contaminated.md` and wasn't used.
- **Later prompts in `prompts/`:** G2 (formal grammar phase 2), LX (the lexicon ladder screening, output in `tests/lexicon-ladder-01/`), RB1 (applying the held decisions in one batch).

The author's own words, from which the goal was written, are kept privately and are not part of the repo.

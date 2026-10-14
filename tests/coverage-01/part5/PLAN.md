# Part 5: regional rebalance (author, 2026-10-13; started 2026-10-13 after the usage reset: stages 1 and 6 running)

Why: the 20 texts that set the ~1,500-root size lean European (bias audit). Main question: does the concept list carry a European blind spot (concepts the new texts need that our list ranks too low or lacks)? Second: does the curve flatten near 1,500 for every region?

Stages (run by the main session, each stage started when the previous reports):
1. Collect texts 21–36: `prompts/texts2.md`.
2. Translate texts 21–36 at base / 1000 / 1500 / 2000 with the current root lists (`part2b/roots-N.txt`) and the same method as part2b (`prompts/translate2.md`, four agents, texts split 21–24, 25–28, 29–32, 33–36; outputs into part2b/ap-N/).
3. Back-translate texts 21–36, one cold agent per size (`prompts/back2-base.md` pattern; outputs into part2b/back-N/).
4. Score texts 21–36 (`prompts/score2-a.md` pattern, two agents); append to part2b/scores-c.tsv / scores-d.tsv.
5. Report in RESULTS.md: the curve per panel region (all 36 texts), and the list of concepts the new texts needed that the root lists lack or rank low (from the translators' notes and the scorers' "lost" notes).

6. Non-European checklist comparison (author, 2026-10-13): Wordbank's non-European checklists (Kiswahili, Kigiriama, Mandarin, Cantonese, Korean, Persian, Turkish, Hebrew; also Arabic if usable) against the European ones: list everyday concepts on the non-European lists that the European ones lack or rarely have, and check each against the root lists. Data: ~/work/cache/coverage/wordbank/*.csv (uni_lemma, category, definition, gloss). One agent; output part3/wordbank-nonwestern.tsv and a short note in RESULTS.md. Independent of stages 1–5: start it with stage 1.

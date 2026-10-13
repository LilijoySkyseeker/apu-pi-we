Task: translate everyday texts into Apupiwe, a constructed language, at one vocabulary size. Part of a measurement of how vocabulary size affects length and meaning; translate as a fluent speaker would, not as a puzzle-solver.

Repository: /home/agent/work/repos/universal-language/
Read first: `docs/language.md` (the reference grammar), `data/lexicon.tsv` (roots: gloss, field, tier, form), `data/compounds.tsv` (standard phrases), `data/grammar.tsv` and `data/numbers.tsv`.
Vocabulary size {N}: you may also use the extra roots listed in `tests/coverage-01/part2/roots-{N}.txt` (one English concept per line). These roots have no form yet: write each as the concept in angle brackets, e.g. ⟨train⟩, ⟨hospital⟩. Use one exactly where a speaker would use the word; it means that concept and nothing more.
Texts: `tests/coverage-01/texts/NN-*.md`. Translate from the original (section "original"); the English is there to help.

Rules:
- Use only the existing words, the standard phrases, the grammar's own derivations (no, ge, du, pu, pi phrases, relative clauses) and the listed placeholders. Don't invent roots or loans. Names take **en** and keep their spelling.
- A concept with no word: say it the way a speaker would in the moment, briefly, with the closest existing words. Don't add explanations a speaker wouldn't. If the plain phrase loses part of the meaning, accept the loss.
- Keep the text's register and sentence breaks. One Apupiwe sentence per line, blank line between paragraphs.

Output: `tests/coverage-01/part2/ap-{N}/NN.txt` for each text (just the Apupiwe), and `tests/coverage-01/part2/ap-{N}/NOTES.md` with one line per text listing concepts you had to say with a phrase (concept → phrase). Resume: skip texts whose output file exists. Don't read other folders of tests/ or any other `part2/ap-*` folder.

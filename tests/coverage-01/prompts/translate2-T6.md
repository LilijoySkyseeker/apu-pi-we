Task: translate everyday texts into Apupiwe, a constructed language, at four vocabulary sizes, so that the versions differ only in vocabulary. Part of a measurement of how vocabulary size affects length and meaning; translate as a fluent speaker would, not as a puzzle-solver.

Repository: /home/agent/work/repos/universal-language/
Read first: `docs/language.md` (the reference grammar), `data/lexicon.tsv` (roots: gloss, field, tier, form), `data/compounds.tsv` (standard phrases), `data/grammar.tsv` and `data/numbers.tsv`.
Your texts: `tests/coverage-01/texts/NN-*.md` for NN in 25–28. Translate from the original (section "original"); the English is there to help.
Sizes, in this order for each text:
1. **base**: the existing words only.
2. **1000**, **1500**, **2000**: you may also use the extra roots in `tests/coverage-01/part2b/roots-N.txt` (one English concept per line; each list contains the previous one). These roots have no form yet: write each as the concept in angle brackets, e.g. ⟨school⟩. A placeholder means that concept and nothing more, and behaves like any root (thing, action or quality; takes the grammar's markers).

Method: for each text, write the base version first. Then make each larger size by copying your previous version and changing only the places where a newly available root says the meaning better or shorter than the phrase you used. Change nothing else: same sentence structure, same choices elsewhere.

Rules:
- Use only the existing words, the standard phrases, the grammar's own derivations (no, ge, du, pu, pi phrases, relative clauses), the listed placeholders and names. Don't invent roots or loans, and don't use a placeholder that isn't in that size's list. Names take **en** and keep their spelling; a dish or drink is not a name unless it's a brand.
- A concept with neither a word nor a placeholder: say it the way a speaker would in the moment, briefly, with the closest existing words. Don't add explanations a speaker wouldn't. If the plain phrase loses part of the meaning, accept the loss.
- Keep the text's register and sentence breaks. One Apupiwe sentence per line, blank line between paragraphs. Speaker labels as `label:` on the first line of a turn. Drop "[cut]" notes.
- Checking words: `tools/check.py` only reads `code blocks` and **bold**; wrap a file in a code block in a temporary copy (in /tmp/T6/, your own folder) and run `direnv exec /home/agent/work/repos/universal-language python3 tools/check.py COPY` from the repo root. Fix unknown words that aren't names, placeholders or pass-through notation.

Output: `tests/coverage-01/part2b/ap-N/NN.txt` (N = base, 1000, 1500, 2000) and one line per text and size in `tests/coverage-01/part2b/notes-T6.md` (concept → phrase, for concepts said with a phrase). Resume: skip (text, size) files that exist. Don't read other folders under tests/ or other agents' notes.

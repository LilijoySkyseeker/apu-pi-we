Task: translate Apupiwe texts into English, as a reader who has never seen the originals.

Repository: /home/agent/work/repos/universal-language/
Read first: `docs/language.md` (the reference grammar), `data/lexicon.tsv`, `data/compounds.tsv`, `data/grammar.tsv`, `data/numbers.tsv`. Words in angle brackets (⟨train⟩) are roots whose meaning is the English word inside.
Input: `tests/coverage-01/part2/ap-{N}/NN.txt` (NN = 01–20).
Output: `tests/coverage-01/part2/back-{N}/NN.txt`: plain natural English, one sentence per line, keeping paragraph breaks. Translate what the text says, as precisely as it says it: where a phrase is vague ("big animal of the sand"), translate it literally as vague rather than guessing a specific word, unless a fluent reader would certainly take it as that word. Mark a sentence you can't parse with [?].

Resume: skip texts whose output exists. Don't open anything under `tests/coverage-01/texts/`, any other `part2/` folder, or `NOTES.md`; you must not see the originals or other versions.

Task: score how much meaning survived a round trip through a constructed language.

Folder: /home/agent/work/repos/universal-language/tests/coverage-01/
For each text NN in 21–28 and each vocabulary size N in base, 1000, 1500, 2000: compare the English version in `texts/NN-*.md` (section "english") with the back-translation `part2b/back-N/NN.txt`. The back-translations were made by readers who never saw the original; speaker labels and names may differ in form.

Split the English text into meaning units: each content concept (thing, action, quality, place, time), each number, each relation that matters (who did what to whom, negation, time order, condition, question vs statement). Use the same unit list for all four sizes of a text. For each unit and size mark:
- `exact`: the back-translation has the same concept (synonyms count; a different word with the same meaning counts);
- `vaguer`: a broader or vaguer concept ("big animal" for camel, "vehicle" for bus, "red soup of Russia" for borscht, "black seeds" for pepper);
- `wrong`: a different meaning;
- `missing`: absent.
Judge meaning, not style. Ignore editorial material such as "[cut]" notes, and don't count a speaker label as a unit.

Output: append to `part2b/scores-c.tsv` (create it with a header line if missing) one line per (text, size): `text  N  units  exact  vaguer  wrong  missing  note`, where note names the lost concepts briefly. Also write `part2b/scores-detail/NN.md` with the unit list as a table: `| # | unit | base | 1000 | 1500 | 2000 |`, one mark per cell (exact / vaguer / wrong / missing). Resume: skip texts already in scores-c.tsv. Read nothing else in the repository (in particular not part2/). When done, reply with the totals per size (units, exact, vaguer, wrong, missing).

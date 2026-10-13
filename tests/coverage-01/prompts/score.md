Task: score how much meaning survived a round trip through a constructed language.

Folder: /home/agent/work/repos/universal-language/tests/coverage-01/
For each text NN (01–20) and each vocabulary size N in {SIZES}: compare the English version in `texts/NN-*.md` (section "english") with the back-translation `part2/back-N/NN.txt`.

Split the English text into meaning units: each content concept (thing, action, quality, place, time), each number, each relation that matters (who did what to whom, negation, time order, condition, question vs statement). For each unit mark:
- `exact`: the back-translation has the same concept (synonyms count; a different word with the same meaning counts);
- `vaguer`: a broader or vaguer concept ("big animal" for camel, "vehicle" for bus, "sick place" for hospital is exact only if a reader would certainly say "hospital");
- `wrong`: a different meaning;
- `missing`: absent.
Judge the meaning, not the style.

Output `part2/scores.tsv` with columns: text, N, units, exact, vaguer, wrong, missing, then a free note naming the lost concepts (e.g. "vaguer: camel, desert; missing: scholars"). Also `part2/scores-detail/NN-N.md` with the unit list and marks. Resume: skip (text, N) pairs already in scores.tsv. Score each text's sizes side by side so the marking is consistent across sizes.

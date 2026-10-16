You are a second, independent rater for a constructed language's vocabulary (Apupiwe). Don't read anything under tests/ except tests/coverage-02/blind-candidates.tsv, and don't read docs/design-log.md. You may read data/lexicon.tsv (roots: gloss, field, tier, form), data/compounds.tsv, data/grammar.tsv and docs/vocabulary-method.md §0.

blind-candidates.tsv lists 92 concepts (rank, concept: an English label from a frequency ranking over 20 languages; some labels pool unrelated English senses). Classify each into exactly one class:
- G: a general concept (shared across cultures) that needs its own root.
- P: covered already: either an existing root used plainly or in a natural stretched sense, or a phrase of at most 3 syllables (roots are 2 syllables, grammar words 1, so: one root, or one root plus one grammar word), or the compound the world's languages themselves commonly use for it. Give the root or phrase.
- C: culture-bound (belongs to one culture or tradition; left to borrowing).
- L: a loan candidate (the world may already share one form for it, e.g. technical or international words).
- N: a name or specialist term.
- A: an artefact of the data: the English label pools unrelated senses, or it isn't a concept.
Judge from what speakers need, not from English. Output only a TSV with header rank<TAB>concept<TAB>class<TAB>root_or_phrase<TAB>note, one line per concept, in input order.

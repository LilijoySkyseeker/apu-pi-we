Task: take each candidate concept for Apupiwe's new roots through the word-decision ladders, so the concept list can be settled before any word forms are made.

Repository: /home/agent/work/repos/universal-language/
Read first: `docs/goal.md` (criteria ids), `docs/vocabulary-method.md` §0 (the two ladders) and §3 (boundaries), `data/lexicon.tsv` (today's roots: gloss, field, tier, form), `data/compounds.tsv`, `data/grammar.tsv`, `data/numbers.tsv`, and section 9 of `docs/language.md` (numbers, dates, measurement) plus 11 (names, loans).
Input: `tests/coverage-01/part2b/roots-1500.txt`, 983 concepts in priority order (the first 235 are children's first words found in at least half of 30 languages; the rest are ranked by frequency in modern text and speech across 20 languages). `tests/coverage-01/merged.tsv` and `merged-add.tsv` hold the source labels behind each canonical concept (column 3), if you need to see what a concept covered.

For each concept write one line to `tests/coverage-01/part3/ladder.tsv` (tab-separated, header first):
`n  concept  status  route  field  tier  antonym  note`
- **status**: `keep` (needs a word of its own); `grammar` (the grammar already says it: month and weekday names are **dunan mena N** / **dili mena N**, ordinals use **mena**, numbers, pronouns, question words…); `name` (a proper name or nationality); `covered:FORM` (an existing root or standard phrase already says exactly this; give it; a merely broader word doesn't count); `merge:CONCEPT` (the same concept as another entry in the list); `split` (the label hides two common concepts, e.g. fan = cooling device / admirer; say which in the note; keep the line for the first sense and add a line `n.b` for the second).
- **route** (for keep): `standard` (an international standard fixes the concept or its form, e.g. SI units, ISO codes; name it in the note); `loan?` (plausibly named with one shared international form in most of the world's languages, e.g. taxi, radio, chocolate; it will be tested against a 20-language panel); `root` (otherwise: a new word of its own).
- **field**: one of today's fields (abstract, action, animal, body, color, mind, motion, nature, number, people, quality, sense, size, space, taste, thing, time) or a new one if none fits (food, home, work, money, tech, health, society…).
- **tier**: 1–5, how frequent the concept is in everyday speech compared with today's roots (5 = among the most frequent words, like "go", "eat"; 3 = common, like "house", "rain"; 1 = specialised). Today's spread is 15 / 43 / 176 / 237 / 46 at tiers 5–1.
- **antonym**: an existing root's gloss or another concept in the list that is its direct opposite, else empty.
- **note**: a few words; for `covered`, `merge` and `grammar`, the reason.

Judge boundaries by the ladder: a concept stays separate unless an existing word already carries it in ordinary use; don't merge just because English has one word, and don't split just because English has two. Be conservative with `covered`: the coverage study wants a root for every concept common in modern life (a phrase is a fallback, not a substitute).

Work in chunks of 100 concepts, appending each chunk to ladder.tsv. Resume: if the file exists, continue after its last `n`. Read nothing else under tests/. When done, reply with counts per status and route, and the loan candidates as one list.

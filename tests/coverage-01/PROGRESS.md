# Coverage measurement (coverage-01): progress

Plan agreed with the author 2026-10-13 (`docs/vocabulary-plan.md`, "Coverage of modern life"): Part 1 modern concept list, Part 2 coverage curve (placeholder roots at 500/1,000/1,500/2,000; cold AI back-translation, the author judges ~5 texts), Part 3 boundary cases (rung 3 signals), Part 4 new roots in one batch.

Resume: read this file, then continue at the first unchecked step. Downloads are cached in `~/work/cache/coverage/` (Leipzig `*_community_2017`, kaikki `kaikki-LANG.jsonl.gz`). Run with `direnv exec ~/work/repos/universal-language python3 concepts.py …` from this folder.

## Part 1: modern concepts

- [x] `concepts.py freq`: top 6,000 words per language (wordfreq frequency dicts for 15; Leipzig community 2017 for th, sw, ha, yo, qu).
- [x] `concepts.py gloss`: senses from Wiktionary; own entry beats lemma lookup; grammatical senses take their weight share and drop out; marks Wiktionary writes but text omits are stripped (ru stress, ar/fa harakat, ha/yo/qu all combining marks).
- [x] `concepts.py build`: per-language shares, median of log shares across the 20 (one language's error can't lift a concept). 60,827 labels.
  - Share of running text matched: zh 94, ja 96, ko 91, vi 98, th 68, id 93, fil 87, hi 94, bn 79, ta 80, fa 92, ar 92, tr 94, ru 99, es 99, fr 99, sw 91, **ha 36**, yo 83, **qu 44** (%).
  - Known noise: homographs take Wiktionary's first-listed sense (sw *la* → "eat"); vi/th tokenisation splits compounds; qu is agglutinative.
- [x] AI glosses for the frequent unmatched words in ha, qu, th (now th 89, ha 93, qu 78 % of text matched; 61,120 labels) (small dictionaries): background agents write `data/aigloss-{ha,qu,th}.tsv` (resumable; `prompts/aigloss.md`). Then rerun `gloss ha qu th` and `build` (the fallback is wired in).
- [x] AI pass over the top ~3,000 labels: merge synonyms ("big"/"large"), drop artifacts, mark grammar concepts, and mark which are already covered by a root, a compound or a grammar word. Prompt `prompts/merge.md` with {TOP} = 4000; output `merged.tsv`, `canon.txt`. `existing.tsv` = current words (lexicon, compounds, grammar, numbers).

## Part 2–4

- [x] Part 2 texts (20 saved; 12 original languages; 18 English versions are the collector's own translations, talk texts are scripted Peace Corps course dialogues 1991–2013; details in texts/LOG.md): collected 20 openly licensed everyday texts (5 talk, 5 chat, 5 news, 5 howto; ≥8 original languages) into `texts/`, log `texts/LOG.md`, resumable.
- Part 3 first look (2026-10-13): moon/month in modern frequency data — one word in id, fil, fa, tr, th, sw, ha, qu, ko(달; months counted with 월); zh splits in use (月亮/月份); split from the start in ar, es, fr, hi, bn, ta, vi.
- Part 2 prompts written: `prompts/translate.md` (per N; placeholders ⟨concept⟩ from `part2/roots-N.txt`), `prompts/back.md` (cold reader, one agent per N so no reader sees two versions of a text), `prompts/score.md` (exact / vaguer / wrong / missing per meaning unit; vaguer counts as a loss, fixing test 05's "big animal of the sand" = camel leniency).
- [x] Make `part2/roots-N.txt` for N = 1000, 1500, 2000 from `merged.tsv`: current roots + top uncovered content concepts by rank until the total is N (N = current ≈ 500 needs no file).
- [ ] Translate (4 sizes) → back-translate (4 agents) → score → syllable counts → author sheet (~5 texts, two sizes).
- Merge result: top 4,000 labels → 2,146 distinct content concepts (merging aggressive, so on the low side); 493 covered by a root, 1,653 candidates (phrase-only counts as a candidate). Roots today 517. roots-1000 = 483 extra (to rank 951), roots-1500 = 983 (to 1951), roots-2000 = 1,483 (to 3357). Top missing: world, school, government, question, news, company, history, song, state, team, age, son…
- Running: translators ap-base, ap-1000, ap-1500, ap-2000 (background agents, resumable by file). Next: one cold back-translator per size (`prompts/back.md`), then scoring (`prompts/score.md`), syllable counts, author sheet.
- [x] ap-base translated (notes: speaker labels kept; dishes as names with en; most missing: food/drink, money/commerce, institutions/roles, transport, weather). back-base done (1 sentence [?]; reader resolved coffee, tea, soup, tram, butter from context, kept "red drink", "sweet ice" literal).
- Tool gap found: `tools/check.py FILE` only reads code blocks and **bold**, so plain .txt always passes. Translators wrapped files themselves. Fix later (a plain-text mode) if it bites again.
- [x] ap-1000 translated (117 placeholders used); back-1000 running.
- Grammar findings from the translators (for the author later): (1) only **pi** can attach inside a noun phrase, so "tea with lemon", "medicine to drink" need a relative clause; (2) a phrasal derived word (**du siten**) swallows a following describing word, so "the hot pan" can't be **du siten mawun tikun**; (3) a name containing a grammar word (Spanish "Cuerpo de Paz": **de**) breaks the name rule; (4) common nouns used as titles before names (**⟨station⟩ en mikunigaoka**).
- [x] ap-2000 translated; back-2000 running. More findings: Indonesian title "Bu" in a name hits grammar word **bu** (name rule, finding 3); no single word for "never"/"often" (grammar: **mon gimu we … mu**, **mon gimu feli**); some list concepts are ambiguous (interest, capital, table, fan).
- [x] ap-1500 translated; back-1500 running. Names with grammar words: Bu Pawiro (bu), Cuerpo de Paz (de), Sauti ya Amerika (ya), Arabic letter ya.
- [x] All four back-translations done. Lengths (measure.py): base 5,190 syllables; 1000 95%; 1500 95%; 2000 92%. Placeholder uses 272 / 353 / 411 (117 / 169 / 202 distinct). Caveat: each size had its own translator agent, so style varies between sizes.
- [ ] Scoring: two agents (texts 01–10 → part2/scores-a.tsv, 11–20 → scores-b.tsv; details part2/scores-detail/NN.md). Then the author sheet.
- [x] Scoring done: `RESULTS.md` (copied to the author's notes). Exact 89.6 / 89.9 / 90.9 / 92.4 %; length 100 / 95 / 95 / 92 %. Waiting on the author: their judging sheet (`~/research/Language/apupiwe-coverage/judging-sheet.md`, texts 01 05 09 15 19, A = base, B = 2000) and the next-step decision.

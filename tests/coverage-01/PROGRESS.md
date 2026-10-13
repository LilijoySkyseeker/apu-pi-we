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
- [ ] AI pass over the top ~3,000 labels: merge synonyms ("big"/"large"), drop artifacts, mark grammar concepts, and mark which are already covered by a root, a compound or a grammar word. Prompt `prompts/merge.md` with {TOP} = 4000; output `merged.tsv`, `canon.txt`. `existing.tsv` = current words (lexicon, compounds, grammar, numbers).

## Part 2–4

- [ ] Part 2 texts: background agent collecting 20 openly licensed everyday texts (5 talk, 5 chat, 5 news, 5 howto; ≥8 original languages) into `texts/`, log `texts/LOG.md`, resumable.
- Part 3 first look (2026-10-13): moon/month in modern frequency data — one word in id, fil, fa, tr, th, sw, ha, qu, ko(달; months counted with 월); zh splits in use (月亮/月份); split from the start in ar, es, fr, hi, bn, ta, vi.

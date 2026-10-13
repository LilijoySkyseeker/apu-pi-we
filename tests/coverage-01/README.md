# Coverage measurement (coverage-01)

**Question:** how many roots does the base vocabulary need, and which ones? Agreed with the author 2026-10-13 (`docs/vocabulary-plan.md`, "Coverage of modern life"): seed the best base, then leave the language to its speakers; every concept common in modern text and speech gets a root; the size comes from measurement, not a chosen number. It replaces the cold review's "grow the core" repair (`research/reviews/cold-review-2026-10/reports/C-verdict.md`, A3 4.1).

`PROGRESS.md` is the working log (resumable step by step); `RESULTS.md` and `guess/RESULTS.md` are the findings.

## Method, and why each choice

**Part 1: which concepts are common in modern life** (`concepts.py`).
- Word frequencies for the 20 panel languages (the same panel as the loan test, `tests/lexicon-ladder-01/`): `wordfreq` (subtitles, news, Wikipedia, Twitter, Reddit, books; to about 2021) for 15, Leipzig web corpora for Thai, Swahili, Hausa, Yoruba, Quechua. *Why:* the author's "modern texts and speech", across every region.
- Speech added in the rerun: OpenSubtitles 2018 lists for 15 languages, averaged with text per language. *Why:* the first run showed written corpora rank home life low (lemon at 8,103).
- Each word's senses come from Wiktionary (kaikki.org extracts); frequent words a small Wiktionary lacks (Hausa, Quechua, Thai) were glossed by an AI (`prompts/aigloss.md`). A word's own entry beats a lemma lookup; grammatical senses keep their share of the weight and drop out.
- **Each language counts once** and languages are combined by the **median** of log shares, so no single language, and no single sense error, can lift a concept (goal N3; safeguard 4 of the boundary rung).
- The top 4,000 labels were merged into canonical concepts and marked as covered or not by today's words by an AI pass (`prompts/merge.md`, output `merged.tsv`, `merged-add.tsv`, `canon.txt`).
- **The deep layer:** children's first words from Wordbank (30 languages, `wordbank.tsv`; concepts on at least half the lists, `wordbank-merged.tsv`). *Why:* the plan chooses basic concepts by convergence and child vocabulary, not by modern frequency (safeguard 3), and the first run's losses were home objects.

**Part 2: how many roots** (`part2/` first run, `part2b/` rerun).
- 20 openly licensed everyday texts (`texts/`: talk, chat, news, how-to; 12 original languages).
- Each translated at today's vocabulary and with 1,000, 1,500 and 2,000 roots. Extra roots are placeholders (⟨school⟩) taken in order from the candidate list, so sizes can be compared before any forms exist.
- Back-translated by a cold reader per size (no reader sees two versions of a text), scored per meaning unit as exact / vaguer / wrong / missing. **Vaguer counts as a loss**, fixing the leniency of vocabulary test 05 ("big animal of the sand" counted as camel).
- Rerun: one translator per text makes all four sizes by editing its own previous version, so only vocabulary differs (the first run's per-size translators added noise as big as the effect).
- Length: syllables per text (`part2/measure.py`; a placeholder counts as two).

**The human check** (`guess/`): the author (an American English speaker) and a cold AI reader guessed 30 phrases translators used for missing words. The author got 19 (+4 hedged), the AI 28: AI readers resolve about a third of what a person misses, so AI-scored round trips understate the meaning lost to missing words.

## Rerun

From this folder, with `E="direnv exec ~/work/repos/universal-language"`: `$E python3 concepts.py freq; $E python3 concepts.py speech; $E python3 concepts.py gloss; $E python3 concepts.py build` (downloads are cached in `~/work/cache/coverage/`; the kaikki, Leipzig, OpenSubtitles and Wordbank sources are public). The AI steps run from the prompts in `prompts/`. `data/` and `concepts.tsv` are regenerated and not committed.

## Limits

- The English versions of 18 texts are the collector's own translations; the talk texts are scripted course dialogues (1991–2013).
- All translation and back-translation is by AI; see the human check above.
- Merging concepts and marking coverage are AI judgments, spot-checked.
- Wordbank's languages lean European; Quechua's corpus is thin and full of names.

# Roadmap

Where the project is and what comes next. Decisions and their reasons are in `design-log.md`; this file is the queue. Updated 2026-10-13.

**Why the project is public:** to share it because it's cool, with people who don't want a git repo or a markdown file. Others using or contributing is a happy surprise, not a goal. It will later live on the author's own site, skyseekerlabs.net. So: a plain static site that can move by copying a folder, and no adoption or governance machinery.

## Done (2026-10-10 to 10-12)

- Spec as structured source: `spec/reference.toml` → `docs/language.md` (`tools/spec.py`), every rule anchored (`#r-4-2-4`); lessons tag the rules they teach and `spec.py lessons` flags lessons whose rules changed.
- Static site (`tools/site.py`, GitHub Pages).
- The goal (`goal.md`), then a cold adversarial review against it (`research/reviews/cold-review-2026-10/`): **keep with repairs**.
- Formal grammar in GF, phase 2 (`formal-grammar.md`, `grammar/`): every reference example parses with its intended reading; the UDHR parses.

## Now: the review-repair batch (from 2026-10-12)

The author works through the judge's repair list one decision at a time; each decision is in `design-log.md` under "Review repairs". Changes are committed but **not pushed until the batch ends**, so the public site doesn't churn.

Done so far: senary words out of the core; "never" rules restated as the reference variety; evidence corrected; **kiyo**; "there is" = **ibe**; manner as a **fu** phrase; "not yet" = **le mu**; labels with **mena** (and the neighbour guard); **kon bo** "maybe"; the word-decision ladders; **mu … fa** as one negation; casual bare-verb commands; **sin le**; a base of about 1,500 roots; moon and month split; word and language split; the boundary cases (live/life merged; keep, request, lose a contest, daytime, rule split off; the 20–50% band rule deleted); **en** for names, free borrowing without a marker; loans re-formed or replaced (L4); metric units as one set; no fusing and no designed shortening; seed-then-release vocabulary; boundaries measured against modern use.

### In progress: vocabulary coverage (`tests/coverage-01/`)

Measured: the base will be about 1,500 roots (decided 2026-10-13). Next: run the boundary cases (Part 3: moon/month, word/language, religion, the 20–50% band), and make the new roots in one batch (Part 4). See `tests/coverage-01/README.md`.

### In progress: other auxlangs, compared (author, 2026-10-13)

A background deep dive into the design, engineering and principles of other international auxiliary and engineered languages, and what happened to them, to learn what to do and what not to do. Output `research/notes/auxlangs.md`; findings that bear on a decision get queued here.
- Widened (author, 2026-10-13): the first survey list was too mainstream. Also cover less-known designs, and read two essays that track this project's direction: Jörg Rhiemeier, [auxlang design](https://www.joerg-rhiemeier.de/Conlang/auxlang-design.html), and [vecderg, auxlangs 2](https://www.vecderg.com/articles/auxlangs2). Opinions aimed at adult learners weigh less here (the language is built for natives, C2).
- **Survey done** (2026-10-13, `research/notes/auxlangs.md`). **Not yet reviewed:** these are the survey's findings, not decisions; review queued for the author below. Findings that bear on decisions (details in §2 and §3.4 of the note):
  - Five grammar-word pairs differ only in voicing (**bu/pu, bi/pi, ke/ge, pen/ben, din/tin**), plus three root pairs; many languages lack the contrast and natives of a designed language are bilingual (Esperanto, Hebrew). Consider an "L1 merger" key (voicing) beside the drift keys.
  - Apply the L4 panel test to a loan's *adapted* form (is **intelunetu** recognised?), not only to the source word.
  - Where a pause is the only cue to structure (language.md §4.6), keep a segmental alternative like **kiyo**; include such sentences in any listening test.
  - Watch list (`drift.md`): derivation markers widening (Elefen), roots growing a verb class (Esperanto, Jansen 2013), frequent optional particles hardening (Tok Pisin).
  - When the freeze returns: freeze only grammar words and base roots, after the dictionary and lessons are usable (Lojban froze too early).
  - Fact-check C44 may be too strong: a 1959 USAF report on the ICAO alphabet argues that longer words survive a noise burst (spelling words, not digits).
- **Globasa in depth** (author, 2026-10-13: "a lot of ideas we should steal"): research done, `research/notes/globasa.md` (64 ideas judged; data from its dictionary in `research/notes/globasa-data.py`). **Not yet reviewed:** its recommendations are the study's, not decisions. Review queued for the author below.
- **Sound symbolism as a tie-breaker:** researched (`research/notes/sound-symbolism.md`): robust only for shape (bouba/kiki) and size; small effects; no *r* in Apupiwe. Decide at the final placement: a narrow tie-break for ~10–20 size and shape words (now movable), or nothing.
- **"We don't know what we don't know"** (author, 2026-10-13): after the surveys, an idea-generation pass looking for considerations and unusual ideas nobody has raised yet. It may find nothing. Scheduled for midnight 2026-10-14, on a different model (Fable) for different blind spots; prompt `research/notes/unknown-unknowns-prompt.md`, output `research/notes/unknown-unknowns.md`.

### Queued for the author

**Order (author, 2026-10-13):** (1) resolve the decision audit's re-evaluations below; (2) inventory 2; (3) review the mishearing-model research (aspiration, word junctions) as a whole.

- **Re-evaluations from the decision audit** (`research/reviews/decision-audit-2026-10-13.md`), in order: (1) ~~the 235 first-word roots~~ done 2026-10-13 (`tests/coverage-01/part3/wordbank-final.tsv`); (2) ~~built words vs roots for modern technology~~ reconciled 2026-10-13; (3) ~~religion consistency~~ done 2026-10-13; (4) percent on unstressed **pi**; (5) **kilo** as the world's short form for kilogram, and a recorded panel for the metric units; (6) re-run the 22 older loans under the new panel rules (email, police); (7) how strong ladder 1 rung 1 is (does **muyi** split, since ISO 8601 defines instant and interval?) and which layer the frequency rule governs; (8) L4's wording in `goal.md` after the borrowing decisions.

- **Mishearing model v2** (author, 2026-10-13: do it before the final placement): replace the guessed parts of `tools/confusion.py` (approximants, vowels, final -n, onset vs none) with published multi-L1 perception data, and choose forms robust across plausible model variants. Research done (`research/notes/confusion-data.md`, data in `research/notes/confusion-data/`, parameters in `model-v2-params.tsv`): v1's only data source (Miller & Nicely 1955) is the low outlier for voicing (its 2005 repeat transmits voicing at 0.37 vs 0.81; voicing was the worst feature for all eight listener groups in Cooke et al. 2010). Next: implement v2 in `tools/confusion.py` with the robustness method (§6: ~32 sampled variants plus extremes, optimize the mean of the worst quarter). Reviewed as a whole after the audit's re-evaluations and inventory 2. Two questions in it: **aspiration** (about 30% of first-language speakers, Mandarin, Cantonese, Korean, hear aspiration rather than voicing; should the reference pronounce p, t, k aspirated?) and **word junctions** (*pi a* / *pi ya*, *pan a* / *pa na* may be near-mergers; no published rates).
- **Short-word layer:** desk analysis done (`tests/shortwords-01/README.md`): 16 pairs collapse under common mergers. Recommended: rebuild the whole layer with corrected rules (positions by real co-occurrence, voicing / f=p / glide mergers, onsets for every grammar word, digits included, operator juncture), as a dry run first, after model v2. Before it: settle the grammar-word inventory (words to add or delete).

- **Loan panel for the coverage concepts:** decided 2026-10-13 (`tests/coverage-01/part3/loans-final.tsv`: 62 loans pass, plus pound as a currency; 43 fail and take native roots). Left for the forms step: apply the tie rule, and test shared short forms for long loans (television: *TV*/*tele*).
- **Review and decide the auxlang survey findings** (author, 2026-10-13). Go through `research/notes/auxlangs.md` with the author one decision at a time: its findings listed above under "Survey done" (voicing pairs among grammar words, testing loans in their adapted form, segmental alternatives to pauses, the drift watch list, what to freeze and when, the ICAO note on fact-check C44), its ten lessons (§4), and the ideas from the Rhiemeier and vecderg essays not yet considered (§2). Nothing from the survey is applied until decided.
- **Review and decide the Globasa findings** (author, 2026-10-13). Go through `research/notes/globasa.md` with the author one decision at a time: the floorboard question (the study recommends keeping invented roots rather than drawing them from world languages), its ten ideas to adopt or adapt, and its three not to adopt. Nothing from the study is applied until decided. The study's list, most urgent first: (1) before Part 4 places forms, panel-test imitative and nursery forms (cat, duck, sheep, frog, bee, owl, kiss, knock; mama) as L4 loans; (2) in Part 4, no new root starts with the syllable of a grammar word that regularly precedes it (**mu**, **le**, **na**, **fe** …; 11 existing verbs such as **muge**, **lewe**, **nagu** listed for review only); (3) blind tests: a modifier of a modifier ("dark red shirt", no rule today) and a verb with no object ("the door closes" vs "she closes it"); (4) SI prefixes **kilo**/**mega**/**giga** as the number words (1,000 now has two forms); (5) the correlative grid as a check for never/often/always; (6) declared accent tolerance per sound; (7) an endearment/diminutive word; (8) text coverage of the most frequent roots as the learning order; (9) a one-off regional-balance audit of the ladders' winners.
- **Grammar gaps found by the coverage translators:** only **pi** attaches inside a noun phrase ("tea with lemon" needs a relative clause); a phrasal derived word swallows a following describing word ("the hot pan"); names containing a grammar word break the name rule (Cuerpo **de** Paz, Ibu Pawiro with **bu**, Sauti **ya** Amerika); no single word for "never" or "often".
- **From the lexicon ladder screening** (`tests/lexicon-ladder-01/`): new roots or phrases for hour, minute, second, degree and "picture" (now part of the coverage pass); police (borderline loan). (Counting an unshared currency is answered by free borrowing: a borrowed *baht* is counted like any word.)
- **Name-boundary regression** (RB1): under the 11.1 clarification a content word right after a name joins the name; the grammar is also stricter than the reference about pauses between joined verbs and inside noun lists.
- **Short-word layer (next after the concept list):** desk fixes: move **fa** (vs **sa**); the vowel-initial vs glide pairs (**un**/**wun**, **o**/**wo**, **en**/**yen**) and the same-slot bug in `build.py`; rename **manni**/**konsin** with the juncture rule; a digit-vs-grammar-word check. Then all ~1,500 content roots are placed together once (decided 2026-10-13, on the current confusion model).
- **Boundary candidates:** decided 2026-10-13 (design log; uses still in an old sense wait for the new forms, `tests/coverage-01/part3/pending-splits.md`).

### Judge's repairs not yet taken up

From `research/reviews/cold-review-2026-10/reports/C-verdict.md` §2 (area verdicts). Each goes to the author as its own question.

- **Core grammar:** list pronoun retention (**… mon bu**) as the precise oblique relative; one time root "later" (may come with the coverage roots); **tun** as the normal recipient marker when the thing is a pronoun or determiner; describe the type choice honestly (one coherent head-initial isolating type).
- **Vocabulary:** split **tinli** (key / button) and **yebin** (call / phone), English-shaped lumps; allow bare noun + noun as a loose compound with **pi**/**man** as the precise form.
- **Precision:** list **nen nen** as lexicalised; (**fon**/**de**/**yo** reviewed 2026-10-13: kept, each with its source in rationale 4.3); teach **sin**'s frame-relativity and the **to gun nuta** trap early in the lessons.
- **Sounds and word forms:** no grammar-word contrast may rest on a declared harmless variant; the empty-CV rule stated as an explicit constraint for new grammar words; a digit-vs-grammar-word confusion check; digits 0–5 included in the short-word rebuild (the listening test is deferred).
- **Evidence:** re-run or withdraw the base-transmission numbers; one frequency source per optional subsystem; where possible a rater who isn't a Claude model.

### Checks

- **The language's name is settled last** (author, 2026-10-13: the name doesn't have to be kept). **apu pi we** depends on the forms of "language" (**apu**), **pi** (in a voicing pair flagged by the auxlang survey) and **we**; after the short-word redo and the final placement, decide whether to keep or pin the name or let it follow the words. Renaming would also touch the repository, the site address and the README.

- **Culture-bound vocabulary beyond religion** (author, 2026-10-13): check holidays, food, titles, kinship, clothing, law and other domains for the same frequency bias found in religion, and apply the principle (shared concepts in the core; each culture names its own) where it fits.

- *(Done 2026-10-13: re-checked without the Bible-heavy sources, then made consistent, design log.)* **Religion core words rest on the skewed list** (bias audit, 2026-10-13): soul, miracle and devil became core partly by their coverage-frequency rank (533, 1,029, 1,070), from the same list the religion decision says over-ranks Christian terms because Bible translations dominate web text in smaller languages. Re-check them with that bias controlled (ranks with Bible-heavy corpora left out, or the panel count alone). Also check "religion" itself: as one category it is arguably a 19th-century European export (Japanese *shūkyō* was coined for it in the 1870s); see whether the panel languages' everyday words for it are old or modern coinages before it keeps a core root.

- **Coverage texts lean European** (bias audit, 2026-10-13): 11 of the 20 texts in `tests/coverage-01/texts/` are Spanish (3), French, Russian, Portuguese or English (2 each). None is in Korean, Vietnamese, Thai, Tagalog, Bengali, Tamil, Persian, Hausa, Yoruba or Quechua, so South-East Asia, South Asia and Africa have one language each and the Americas none. These texts measured the base size (about 1,500 roots) and which missing words cost meaning. Rebalance toward one or two per panel region before the next measurement, or note the skew where the size decision is cited. **Decided (author, 2026-10-13): rebalance now**, keeping the 20 and adding 16 from the missing regions, measured at the same four sizes; main question: concepts the list misses. Queued for 00:13 on 2026-10-14 (`tests/coverage-01/part5/PLAN.md`).

- **Gaps found by the ladder pass** (2026-10-13): "parent" has no root (only **mole yen wede**) while "sibling" has a sexless root; "lie, say what is untrue" has no root (needed for "liar").


### Small fixes (no decision needed)

- `tools/check.py` doesn't read plain `.txt` files (it only reads code blocks and bold); add a plain-text mode.
- RB1 leftovers: residual UDHR readings (Art 25.2, 26.2); the guide's root count; grammar function name `LabelNP` → `LabelQ`.

### Website: frozen at v1 (author, 2026-10-13)

The published site stays at v1 until the language is solid; then a v2 site is built from first principles, keeping v1's spirit. Work is committed on the branch `v2-work` and pushed there as a backup; `main` (which the site builds from) isn't touched until v2. The repo's reference and lessons stay in sync meanwhile. Known false statements on v1 are left as they are (no one is reading it yet) and are fixed in v2:

- Public-page fixes deferred during the batch: the Esperanto/creole sentence in "How it's built" (fact-check C15, C17, C18); `why.md` digit figures (0.26% / 2.3% describe a modelled ideal set); learn.md "ran out of short sounds"; clusivity "among the most stable" (Austronesian only).
- Re-check the UDHR translation against the batch's rules.
- Build v2 of the site from first principles.

## Later

- Formal grammar phase 3 (English concrete syntax) and phase 4 (every document checked by one command); `tools/parse.py` retires then.
- Senary gets its own vocabulary and page (a separate project; its words are reserved in `data/senary.tsv`).
- Human tests the review asked for: listening (B2), learner trial (B10), human readers for meaning (B1). Deferred 2026-10-13 until people beyond the author are involved (trigger: listeners or readers from at least three language families).

## Deliberately not built

Each with the trigger that would bring it back:
- wiki software: non-git people want to edit;
- contribution governance: a real group forms;
- CI: the build is stable and the repo is public;
- tools on the website (tabled 2026-10-11): a word-by-word gloss page is cheap and first in line; the parser in the browser waits until learners ask whether their sentences are grammatical; the name adapter until people ask how to say their name;
- YouTube transcripts as a frequency source (2026-10-13): the coverage rerun still misses common modern concepts.

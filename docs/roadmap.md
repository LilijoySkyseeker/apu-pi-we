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

Done so far: senary words out of the core; "never" rules restated as the reference variety; evidence corrected; **kiyo**; "there is" = **ibe**; manner as a **fu** phrase; "not yet" = **le mu**; labels with **mena** (and the neighbour guard); **kon bo** "maybe"; the word-decision ladders; **mu … fa** as one negation; casual bare-verb commands; **sin le**; a base of about 1,500 roots; loans re-formed or replaced (L4); metric units as one set; no fusing and no designed shortening; seed-then-release vocabulary; boundaries measured against modern use.

### In progress: vocabulary coverage (`tests/coverage-01/`)

Measured: the base will be about 1,500 roots (decided 2026-10-13). Next: run the boundary cases (Part 3: moon/month, word/language, religion, the 20–50% band), and make the new roots in one batch (Part 4). See `tests/coverage-01/README.md`.

### In progress: other auxlangs, compared (author, 2026-10-13)

A background deep dive into the design, engineering and principles of other international auxiliary and engineered languages, and what happened to them, to learn what to do and what not to do. Output `research/notes/auxlangs.md`; findings that bear on a decision get queued here.
- Widened (author, 2026-10-13): the first survey list was too mainstream. Also cover less-known designs, and read two essays that track this project's direction: Jörg Rhiemeier, [auxlang design](https://www.joerg-rhiemeier.de/Conlang/auxlang-design.html), and [vecderg, auxlangs 2](https://www.vecderg.com/articles/auxlangs2). Opinions aimed at adult learners weigh less here (the language is built for natives, C2).
- **Globasa in depth** (author, 2026-10-13: "a lot of ideas we should steal"): its design, vocabulary method, grammar, tooling and community, each idea judged against the goal. Output `research/notes/globasa.md`.
- **Sound symbolism as a tie-breaker:** researched (`research/notes/sound-symbolism.md`): robust only for shape (bouba/kiki) and size; small effects; no *r* in Apupiwe. Decide at the final placement: a narrow tie-break for ~10–20 size and shape words (now movable), or nothing.
- **"We don't know what we don't know"** (author, 2026-10-13): after the surveys, an idea-generation pass looking for considerations and unusual ideas nobody has raised yet. It may find nothing.

### Queued for the author

- **Grammar gaps found by the coverage translators:** only **pi** attaches inside a noun phrase ("tea with lemon" needs a relative clause); a phrasal derived word swallows a following describing word ("the hot pan"); names containing a grammar word break the name rule (Cuerpo **de** Paz, Ibu Pawiro with **bu**, Sauti **ya** Amerika); no single word for "never" or "often".
- **From the lexicon ladder screening** (`tests/lexicon-ladder-01/`): new roots or phrases for hour, minute, second, degree and "picture" (now part of the coverage pass); police (borderline loan); how to count a currency or unit the world doesn't share (baht, naira).
- **Name-boundary regression** (RB1): under the 11.1 clarification a content word right after a name joins the name; the grammar is also stricter than the reference about pauses between joined verbs and inside noun lists.
- **Short-word layer (next after the concept list):** desk fixes: move **fa** (vs **sa**); the vowel-initial vs glide pairs (**un**/**wun**, **o**/**wo**, **en**/**yen**) and the same-slot bug in `build.py`; rename **manni**/**konsin** with the juncture rule; a digit-vs-grammar-word check. Then all ~1,500 content roots are placed together once (decided 2026-10-13, on the current confusion model).
- **Shared meanings** (moon/month, word/language): decided by the modern-use rung (Part 3 of the coverage measurement).
- **Boundary candidates** from the ladder screening (`tests/lexicon-ladder-01/boundaries.md`), strongest first: religion (**lite pi nosen**, theistic); **nume**/**pata** live/life (merge?); **kuwi** keep/protect; **apu** word/language; **mido** ask/request; **agi** lose; **dili** day/daytime/24 hours; **wupi** need/should; **wabun** rule/law; **lula** power; **bendo**/**pifo** and **gala**/**kima** (merge?); the 20–50% band; **dunan** (keep). These go through Part 3's modern-use signals.

### Judge's repairs not yet taken up

From `research/reviews/cold-review-2026-10/reports/C-verdict.md` §2 (area verdicts). Each goes to the author as its own question.

- **Core grammar:** list pronoun retention (**… mon bu**) as the precise oblique relative; one time root "later" (may come with the coverage roots); **tun** as the normal recipient marker when the thing is a pronoun or determiner; describe the type choice honestly (one coherent head-initial isolating type).
- **Vocabulary:** split **tinli** (key / button) and **yebin** (call / phone), English-shaped lumps; allow bare noun + noun as a loose compound with **pi**/**man** as the precise form.
- **Precision:** list **nen nen** as lexicalised; mark **fon**/**de**/**yo** as candidates for deletion (add-back: a human-read corpus where warnings or commitments are misread without them); teach **sin**'s frame-relativity and the **to gun nuta** trap early in the lessons.
- **Sounds and word forms:** no grammar-word contrast may rest on a declared harmless variant; the empty-CV rule stated as an explicit constraint for new grammar words; a digit-vs-grammar-word confusion check; digits 0–5 decided after the listening test.
- **Evidence:** re-run or withdraw the base-transmission numbers; one frequency source per optional subsystem; where possible a rater who isn't a Claude model.

### Checks

- **Speakers' own borrowings** (author, 2026-10-13): real use will import words from speakers' languages with their original sounds. Check that the grammar, sounds and spelling handle such words (names already keep their spelling with **en**; ordinary words have no rule yet).

### Small fixes (no decision needed)

- `tools/check.py` doesn't read plain `.txt` files (it only reads code blocks and bold); add a plain-text mode.
- RB1 leftovers: residual UDHR readings (Art 25.2, 26.2); the guide's root count; grammar function name `LabelNP` → `LabelQ`.

### Before the batch is pushed

- Public-page fixes deferred during the batch: the Esperanto/creole sentence in "How it's built" (fact-check C15, C17, C18); `why.md` digit figures (0.26% / 2.3% describe a modelled ideal set); "most families lump apu" (about half, 40–61%); learn.md "ran out of short sounds"; clusivity "among the most stable" (Austronesian only).
- Re-check the UDHR translation against the batch's rules.
- Rebuild the site and check it.

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

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

Done so far: senary words out of the core; "never" rules restated as the reference variety; evidence corrected; **kiyo**; "there is" = **ibe**; manner as a **fu** phrase; "not yet" = **le mu**; labels with **mena** (and the neighbour guard); **kon bo** "maybe"; the word-decision ladders; loans re-formed or replaced (L4); metric units as one set; no fusing and no designed shortening; seed-then-release vocabulary; boundaries measured against modern use.

### In progress: vocabulary coverage (`tests/coverage-01/`)

Measuring how many roots the base needs, and which, from modern text and speech in 20 languages plus children's first words. First run done; a cleaner rerun is running. Then: set the size with the author, run the boundary cases (Part 3: moon/month, word/language, religion, the 20–50% band), and make the new roots in one batch (Part 4). See `tests/coverage-01/README.md`.

### Queued for the author

- **Grammar gaps found by the coverage translators:** only **pi** attaches inside a noun phrase ("tea with lemon" needs a relative clause); a phrasal derived word swallows a following describing word ("the hot pan"); names containing a grammar word break the name rule (Cuerpo **de** Paz, Ibu Pawiro with **bu**, Sauti **ya** Amerika); no single word for "never" or "often".
- **From the lexicon ladder screening** (`tests/lexicon-ladder-01/`): new roots or phrases for hour, minute, second, degree and "picture" (now part of the coverage pass); police (borderline loan); how to count a currency or unit the world doesn't share (baht, naira).
- **Name-boundary regression** (RB1): under the 11.1 clarification a content word right after a name joins the name; the grammar is also stricter than the reference about pauses between joined verbs and inside noun lists.
- **Short-word layer:** desk fixes (fa vs sa, **manni**/**konsin** renames, a same-slot bug in `build.py`) and planning a human listening test, the review's first priority.
- **Shared meanings** (moon/month, word/language): decided by the modern-use rung (Part 3 of the coverage measurement).

### Before the batch is pushed

- Public-page fixes deferred during the batch: the Esperanto/creole sentence in "How it's built" (fact-check C15, C17, C18); `why.md` digit figures (0.26% / 2.3% describe a modelled ideal set); "most families lump apu" (about half, 40–61%); learn.md "ran out of short sounds"; clusivity "among the most stable" (Austronesian only).
- Re-check the UDHR translation against the batch's rules.
- Rebuild the site and check it.

## Later

- Formal grammar phase 3 (English concrete syntax) and phase 4 (every document checked by one command); `tools/parse.py` retires then.
- Senary gets its own vocabulary and page (a separate project; its words are reserved in `data/senary.tsv`).
- Human tests the review asked for: listening (B2), learner trial (B10), human readers for meaning (B1).

## Deliberately not built

Each with the trigger that would bring it back:
- wiki software: non-git people want to edit;
- contribution governance: a real group forms;
- CI: the build is stable and the repo is public;
- tools on the website (tabled 2026-10-11): a word-by-word gloss page is cheap and first in line; the parser in the browser waits until learners ask whether their sentences are grammatical; the name adapter until people ask how to say their name;
- YouTube transcripts as a frequency source (2026-10-13): the coverage rerun still misses common modern concepts.

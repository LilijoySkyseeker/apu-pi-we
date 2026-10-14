# Working on Apupiwe

Apupiwe (in the language **apu pi we**) is a thought experiment in the best human language, and a real language its author learns and shares. Read `docs/goal.md` first: every rule and word answers to it.

## Where things are

- **Standard:** `docs/goal.md` (P, B, C, L, N items; cite them by id).
- **The language:** `spec/reference.toml` is the source; `docs/language.md` is generated from it (`tools/spec.py build`, `check`). Every rule has an anchor (`#r-4-2-4`).
- **Formal grammar:** `grammar/` (GF; design in `docs/formal-grammar.md`). `tools/gf_check.py` must pass: every reference example parses with its intended reading.
- **Words:** `data/lexicon.tsv` (roots), `data/compounds.tsv` (standard phrases), `data/grammar.tsv`, `data/numbers.tsv`, `data/roles.tsv` (two features the grammar needs); `data/senary.tsv` is reserved, outside the core.
- **Lessons:** `docs/learn.md`, tagged with the rules they teach (`[§4.2.4](language.md#r-4-2-4)`); `tools/spec.py lessons` fails when a tagged rule changed since the last review (`--ack` after checking).
- **Why:** `docs/design-log.md` (every decision, newest last, with reasons, alternatives and add-back triggers), `docs/rationale.md`, `docs/vocabulary-method.md` (the word-decision ladders, §0), `docs/drift.md`, `research/`.
- **What's next:** `docs/roadmap.md`.
- **Tests:** `tests/NAME/`, each with a README (question, method, results) or results file; long multi-agent runs keep a resumable `PROGRESS.md`.

## How decisions are made

- The author decides anything that shapes the language. Agents research, draft and recommend. Present each decision in full: the problem, an example, the options and a recommendation, one at a time.
- Design by the goal's order: question every requirement and name its source (a person or a concrete external constraint); prefer deleting a part, with the trigger that would bring it back; simplify only what survives; automate last.
- Log every decision in `design-log.md`: what was decided, by whom, why, what was rejected, and where it changed the reference, lessons or grammar. Keep the reasoning in the repo, not only in a chat.
- Track all open work in `docs/roadmap.md`, with its source: queued questions, review findings not yet taken up, small fixes. Anything found along the way (a gap a test turns up, a question tabled for later) goes there when it's found, not only into a chat, a working folder outside the repo, or a report. When work is done, move it to "Done" and log the decision.

## Changing things

- Branches: `main` is the published v1 site (GitHub Pages builds on every push to it). Until v2, work goes on `v2-work` and is pushed there; don't push to `main` (author, 2026-10-13).
- After changing the spec: `spec.py build`, `spec.py check`, `spec.py lessons`, `gf_check.py`; regenerate the grammar lexicon with `tools/gf_lexicon.py` after word changes; `tests/udhr-01/make_page.py` rebuilds the declaration page.
- New words: go down the ladders (`vocabulary-method.md` §0); a new root's form comes from `tools/words.py add-content` (with `--avoid` for freed forms and `--after`/`--before` for fixed neighbours), never by hand. Loans only where the world shares the form (L4, panel test).
- Public pages follow `docs/style.md` (plain human voice); working notes can be terse.
- Tools run in the Nix dev shell: `direnv exec . python3 tools/…`.

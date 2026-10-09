# Universal language

A thought experiment: design the best universal human language for modern Earth from first principles. It's imagined as a native language that children grow up speaking. The goal is faithful transmission of thought, at a cost speakers will actually pay.

The language has no name yet.

## Layout

- [docs/language.md](docs/language.md): the language as it stands now. Start here.
- [docs/design-log.md](docs/design-log.md): decisions in order, with reasons.
- [docs/roadmap.md](docs/roadmap.md): what a full language still needs, and in what order. [docs/vocabulary-plan.md](docs/vocabulary-plan.md): the agreed plan for building the vocabulary.
- [docs/drift.md](docs/drift.md): how the language would change over generations, and how the design pre-empts it.
- [docs/number-base.md](docs/number-base.md) and [docs/measurement.md](docs/measurement.md): why base 6, and how measurements are said. The measurement system itself (definitions, values) lives in the sibling repo `~/work/repos/senary`; this repo owns only the words.
- [research/](research/): evidence. `where-communication-fails.md` is the main report; `notes/` holds the raw research notes behind it and later rounds.
- [data/](data/): `grammar.tsv` (grammar words), `lexicon.tsv` (roots and numbers), `antonyms.tsv`.
- [texts/](texts/): stress-test translations, each with findings.
- [tools/](tools/): `confusion.py` (mishearing model built on Miller & Nicely 1955), `build.py` (drift-aware rebuild of all words; scale and digit checks), `words.py` (add words without moving existing ones; count syllables), `convert.py` (carry texts over to renamed words), `juncture.py` (word sequences that sound like other words), `base_test.py` (which number base survives noise best), `units.py` (unit words for the senary units), `lexicon.py` (the historical v0 generator).

## Tools

The tools need Python with numpy. On NixOS:

    cd tools
    nix-shell -p 'python3.withPackages(ps: [ps.numpy])' --run 'python3 words.py add-content river field 2'
    nix-shell -p 'python3.withPackages(ps: [ps.numpy])' --run 'python3 words.py syllables "pin me NAgu DINbu LUmi"'

## Related

The measurement system is the senary system, which lives in the sibling repo `~/work/repos/senary`. That repo owns the quantities: unit definitions, exact values, constants and the calendar's arithmetic, with `src/senary_tables.py` as the source of truth. This repo owns the words (`docs/measurement.md`, `data/units.tsv`, `data/numbers.tsv`). Senary's calendar and timing are being reworked, so the time words here are provisional.

# Apu Pi We, a universal language

A thought experiment: design the best universal human language for modern Earth from first principles. It's imagined as a native language that children grow up speaking. The goal is faithful transmission of thought, at a cost speakers will actually pay.

The language is called **apu pi we**, "everyone's language". **Status:** still in design; nothing is frozen until the user starts learning it.

## Layout

- [docs/language.md](docs/language.md): the language as it stands now. Start here. It is generated from [spec/reference.toml](spec/reference.toml), the source of truth: edit the spec, then run `tools/spec.py build` (`check` verifies they match; `examples` lists every example with its rule id).
- [docs/rationale.md](docs/rationale.md): why each part is the way it is, how it was made, and how to rebuild or change it. Read this before changing anything.
- [docs/design-log.md](docs/design-log.md): decisions in order, with reasons.
- [docs/roadmap.md](docs/roadmap.md): what happens next (consistency pass, structured spec, static site, going public). [docs/grammar-rebuild-spec.md](docs/grammar-rebuild-spec.md): how one-syllable grammar forms are assigned. [docs/vocabulary-plan.md](docs/vocabulary-plan.md) and [docs/vocabulary-method.md](docs/vocabulary-method.md): the agreed plan and the decision procedure for building the vocabulary.
- [docs/drift.md](docs/drift.md): how the language would change over generations, and how the design pre-empts it.
- [docs/learn.md](docs/learn.md): how to learn the language, for English speakers.
- [docs/measurement.md](docs/measurement.md): words for the senary measurement system, which the language can talk about. [docs/number-base.md](docs/number-base.md): why the language was base 6 until 2026-10-09 (superseded).
- [research/](research/): evidence. `where-communication-fails.md` is the main report; `notes/` holds the raw research notes behind it and later rounds.
- [data/](data/): `grammar.tsv` (grammar words), `lexicon.tsv` (roots and numbers), `antonyms.tsv`.
- [texts/](texts/): stress-test translations, each with findings.
- [tools/](tools/): `confusion.py` (mishearing model built on Miller & Nicely 1955), `build.py` (drift-aware rebuild of all words; scale check), `words.py` (add words without moving existing ones; count syllables), `check.py` (flag unknown words in language text), `juncture.py` (word sequences that sound like other words), `names.py` (adapt foreign names), `concepts.py` (rank concepts by lineage coverage), `clics_rates.awk` (family-balanced lumping rates). Single-use tools were removed on 2026-10-09; they are in git history.

## Tools

The tools need Python with numpy. On NixOS:

    cd tools
    nix-shell -p 'python3.withPackages(ps: [ps.numpy])' --run 'python3 words.py add-content river field 2'
    nix-shell -p 'python3.withPackages(ps: [ps.numpy])' --run 'python3 words.py syllables "min me nagu dinbu lumi"'
    nix-shell -p 'python3.withPackages(ps: [ps.numpy])' --run 'python3 names.py maɹkəs dʒɛs'   # names and loans, given in IPA

## Related

The language's numbers are base 10 and its everyday units are today's, with borrowed names. The senary measurement system lives in the sibling repo `~/work/repos/senary`, which owns its quantities; this repo supplies its words (`docs/measurement.md`, `data/units.tsv`, the senary rows of `data/numbers.tsv`), so senary stays usable, for worldbuilding among other things.

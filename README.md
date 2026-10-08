# Universal language

A thought experiment: design the best universal human language for modern Earth from first principles. It's imagined as a native language that children grow up speaking. The goal is faithful transmission of thought, at a cost speakers will actually pay.

The language has no name yet.

## Layout

- [docs/language.md](docs/language.md): the language as it stands now. Start here.
- [docs/design-log.md](docs/design-log.md): decisions in order, with reasons.
- [research/](research/): evidence. `where-communication-fails.md` is the main report; `notes/` holds the raw research notes behind it and later rounds.
- [data/](data/): `grammar.tsv` (grammar words), `lexicon.tsv` (roots and numbers), `antonyms.tsv`.
- [texts/](texts/): stress-test translations, each with findings.
- [tools/](tools/): `confusion.py` (mishearing model built on Miller & Nicely 1955), `words.py` (add words without moving existing ones; count syllables), `lexicon.py` (the historical v0 generator).

## Tools

The tools need Python with numpy. On NixOS:

    cd tools
    nix-shell -p 'python3.withPackages(ps: [ps.numpy])' --run 'python3 words.py add-content river field 2'
    nix-shell -p 'python3.withPackages(ps: [ps.numpy])' --run 'python3 words.py syllables "yun vun Aza BOzen NOwi"'

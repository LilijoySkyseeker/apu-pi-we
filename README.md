# Apu Pi We

Apu Pi We is a constructed language. Say it **AH-poo pee weh** ([ˈapu pi we]): stress only the first syllable, and say *we* like "wet" without the t. The name means "everyone's language".

The idea: the world's languages have each, separately, worked out the same answers to a lot of problems. Take those shared answers and build one language for children to grow up speaking. What would it look like? It's also meant to be a real language that people learn and use, and you can start today.

It is still being designed, so words and rules change.

**Website: https://lilijoyskyseeker.github.io/apu-pi-we/** has the lessons, the full reference and a searchable dictionary.

## How it's built

Every language has to solve the same problems: naming things, saying who did what to whom, asking, being polite, counting. Languages in families that never met have often landed on the same solutions. Apu Pi We starts from that. Where unrelated languages agree on what a language needs, it has it. Where they disagree on how to do it, it takes the simplest way. Languages are counted by family, not by number of speakers, so a solution found independently on different continents outweighs one that is merely spoken by many people.

The sounds are built on the world's most common system of five vowels, in syllables almost anyone can say. The basic words are the meanings named in the most language families, drawn from a database of over 3,000 languages, and the meanings people use most get the shortest words, with frequency measured across 15 languages.

The grammar had a different problem to solve. When children grow up speaking a language, they reshape it. They drop endings that add nothing, even out irregular forms, and wear down long words they use all the time. Children raised speaking Esperanto did this, and so did the first generations of creole speakers. So the grammar starts in the shape children push toward. Word order and small separate words carry the meaning, nothing is irregular, and the most-used words are already short. A native generation would find little left to wear away.

Where these goals pull against each other, clarity comes first, then predictability, then brevity.

## What it looks like

```
guyi   gun  kudu.
house  is   big
"The house is big."

kon te      wan  gun  mon  guyi.
sure 5/6    she  is   at   house
"She must be home."
```

A few things about it:

- Words never change shape. There are no verb endings, required plurals, genders or irregular forms.
- The most common meanings get the shortest words. Most grammar words are one syllable.
- You can say how sure you are with a number, in sixths: **kon te** is five out of six.
- There is always a precise way to say something, and you can skip it when context already makes it clear.
- The basic vocabulary comes from meanings that languages around the world share, and every word is checked against swear words in 34 major languages so it doesn't sound like one.

## What's in this repo

- `docs/learn.md`: the lessons, also on the website.
- `docs/language.md`: the full reference. It's generated from `spec/reference.toml`, so edit that and run `tools/spec.py build`.
- `docs/rationale.md`: why things are the way they are.
- `docs/design-log.md`: every decision, in order.
- `data/`: the word lists.
- `tools/`: Python scripts that make and check words and build the reference and the website.
- `tests/`, `texts/`, `research/`: translation tests, sample texts and the research behind the choices.

The tools need Python 3 with numpy. `parse.py` also needs lark, `site.py` needs markdown and `offensive.py` needs wordfreq. With Nix, `nix develop` (or direnv) gives a shell with all of them.

## Related

Senary, a base-six measurement system, is a sibling project. Apu Pi We has words for it (`docs/measurement.md`). It will be published here too.

## Contributing

This is a work in progress, but issues are welcome: questions, gaps you hit while using the language, or mistakes you spot. Anything you contribute is released under CC0 too.

## Licence

Public domain. Everything made for this project (text, data and code) is dedicated to the public domain under [CC0](LICENSE): use it for anything, no permission or credit needed. A few data files come from other projects and keep their own licences; see [data/SOURCES.md](data/SOURCES.md).

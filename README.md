# Apupiwe

Apupiwe is a constructed language. Say it **AH-poo-pee-weh** ([ˈapupiwe]): stress only the first syllable, and say the last one like "wet" without the t. In the language itself it's **apu pi we**, "everyone's language".

The idea: the world's languages have each, separately, worked out the same answers to a lot of problems. Take those shared answers and build one language for children to grow up speaking. What would it look like? It's also meant to be a real language that people learn and use, and you can start today.

It is still being designed, so words and rules change. It's designed by its author together with Claude, an AI assistant: Claude does most of the research, drafting and testing, and the author decides the questions that shape the language.

**Website: https://lilijoyskyseeker.github.io/apupiwe/** has the lessons, the full reference and a searchable dictionary.

## How it's built

Apupiwe is designed as [the best language for people who would grow up speaking it, while staying learnable for any adult](docs/rationale.md#11-what-the-project-is). [One rule shapes it](docs/rationale.md#12-how-decisions-get-made). Where unrelated languages agree on what a language needs, it has it. Where they disagree on how to do it, it takes the simplest way. [Agreement is counted by language family](docs/vocabulary-plan.md#decisions), not by number of speakers, so a solution found independently on different continents counts for more than one that is merely widespread.

[The basic meanings](docs/vocabulary-method.md#1-which-concepts-in-what-order) come from that rule. A database of over 3,000 languages shows which meanings the most families have a word for. It also shows [where they draw the lines between meanings](docs/vocabulary-method.md#3-where-boundaries-go-lump-or-split), such as whether "moon" and "month" share a word; in most families they do, and here they do too. [Meanings that modern life uses constantly](docs/vocabulary-plan.md#decisions), like "country", get words as well.

[The sounds](docs/rationale.md#2-sounds) are the ones most languages share: five vowels and thirteen consonants, in simple syllables almost anyone can say. Each word's sound is then chosen by [a model of how speech gets misheard](docs/rationale.md#32-the-mishearing-model-toolsconfusionpy), so that words likely to be confused sound far apart, and every word is [checked against swear words in 34 languages](docs/rationale.md#36-offensive-word-filter-toolsoffensivepy-dataoffensivetsv). [The meanings people use most get the shortest words](docs/grammar-rebuild-spec.md#goal), with frequency measured across 15 languages.

[The grammar](docs/rationale.md#4-grammar) comes from the same rule: the features unrelated languages keep arriving at, each in the simplest form any of them uses.

[Native speakers always change their language](docs/drift.md#whats-already-drift-resistant), so this one is built for it. The most-used words are already short, nothing is irregular, and words are chosen to stay distinct even after the sound changes speakers are likely to make. It also has to [live alongside the world's cultures](docs/design-log.md#coexisting-with-existing-cultures-author-2026-10-10). It carries local conventions such as clocks, calendars, units and names, and where they conflict it follows the international standard.

Underneath it all is one aim: getting meaning across correctly, at a cost speakers will actually pay. Some things are guarantees that must always hold, such as a precise way to say anything, even when everyday speech doesn't use it. Everything else is a cost, kept as low as possible for someone who speaks it all their life. [The goal](docs/goal.md) sets this out in full.

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
- You can say how sure you are with a number, in sixths: **pe ma** is five out of six.
- There is always a precise way to say something, and you can skip it when context already makes it clear.
- The basic vocabulary comes from meanings that languages around the world share, and every word is checked against swear words in 34 major languages so it doesn't sound like one.

## What's in this repo

- `docs/goal.md`: what the language is for; everything else answers to it.
- `docs/learn.md`: the lessons, also on the website.
- `docs/language.md`: the full reference. It's generated from `spec/reference.toml`, so edit that and run `tools/spec.py build`.
- `docs/rationale.md`: why things are the way they are.
- `docs/design-log.md`: every decision, in order.
- `data/`: the word lists.
- `tools/`: Python scripts that make and check words and build the reference and the website.
- `tests/`, `texts/`, `research/`: translation tests, sample texts and the research behind the choices.

The tools need Python 3 with numpy. `parse.py` also needs lark, `site.py` needs markdown and `offensive.py` needs wordfreq. With Nix, `nix develop` (or direnv) gives a shell with all of them.

## Related

Senary, a base-six measurement system, is a sibling project. Apupiwe has words for it (`docs/measurement.md`). It will be published here too.

## Contributing

This is a work in progress, but issues are welcome: questions, gaps you hit while using the language, or mistakes you spot. Anything you contribute is released under CC0 too.

## Licence

Public domain. Everything made for this project (text, data and code) is dedicated to the public domain under [CC0](LICENSE): use it for anything, no permission or credit needed. A few data files come from other projects and keep their own licences; see [data/SOURCES.md](data/SOURCES.md).

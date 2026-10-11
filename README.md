# Apu Pi We

Apu Pi We is a constructed language. The name means "everyone's language".

The idea: the world's languages have each, separately, worked out the same answers to a lot of problems. Take those shared answers and build one language for children to grow up speaking. What would it look like? It's also meant to be a real language that people learn and use, and you can start today.

It is still being designed, so words and rules change.

**Website: https://lilijoyskyseeker.github.io/apu-pi-we/** has the lessons, the full reference and a searchable dictionary.

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

The tools need Python 3 with numpy. `parse.py` also needs lark and `site.py` needs markdown.

## Related

Senary, a base-six measurement system, is a sibling project. Apu Pi We has words for it (`docs/measurement.md`). It will be published here too.

## Contributing

This is a work in progress, but issues are welcome: questions, gaps you hit while using the language, or mistakes you spot. Anything you contribute is released under CC0 too.

## Licence

Public domain. Everything made for this project (text, data and code) is dedicated to the public domain under [CC0](LICENSE): use it for anything, no permission or credit needed. A few data files come from other projects and keep their own licences; see [data/SOURCES.md](data/SOURCES.md).

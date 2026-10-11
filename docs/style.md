# Writing style for the public pages

The author (the language's creator) approved this voice on 2026-10-11. Their words: "I want the whole thing to feel human written, to feel like a competent human wrote it, because that is more enjoyable to read." Their complaint about the earlier text: "it often reads as the AI style of including what something is not, not just defining what it is."

## Voice

A competent human writer explaining a language to a curious English-speaking adult. Plain, direct, a little warm. "You" is fine. Think of a good grammar book or a well-written hobby website, not a product page or a chatbot answer.

## Do

- State the point in an ordinary sentence, then give an example, then move on.
- Say each thing once.
- Define what a thing *is*. Use a contrast or a negative only when a reader would otherwise very likely get it wrong, and then say it once, plainly.
- Write paragraphs of two to four sentences. Use a list only for real lists (sets of examples, parallel items). Use a table where a comparison really helps.
- Keep bold for Apupiwe words. Use italics sparingly for emphasis.
- Put a cross-reference at the end of a sentence in plain words ("more in lesson 7"), at most one per paragraph.
- Vary sentence length the way people do.

## Don't

- No bold lead-ins at the start of paragraphs or bullets ("**What you mean picks the form.** When..."). Fold the idea into a normal sentence or make it a heading if it really is one.
- No reflexive "X, not Y" / "rather than" / "instead of" framing. No "isn't just", "more than", "never wrong", "the key", "the real", "the first real switch", "note that", "in other words", "simply", "essentially", "crucially".
- No em dashes. No semicolon chains. No colon after every lead phrase.
- No rhythmic triplets, no restating a point in a summary sentence, no hype.
- No stacks of parentheses.

## When rewording existing text

- Examples are written `**apu words** "gloss"`; `tools/spec.py examples` and `tools/parse.py` read that pattern, so keep it.
- Rewording must not change a rule. Changing a rule is a design decision and goes in the design log.
- Headings are link targets; renaming one means fixing its links.

## Where it applies

The public pages: `docs/learn.md`, the reference (`spec/reference.toml`, which generates `docs/language.md`), `README.md`, `site/index.md` and the dictionary intro in `tools/site.py`. The working notes (rationale, design log, tests, research) are written for whoever works on the language next and don't follow it.

Everything in the repo, working notes included, reads as a public project: the creator is "the author", there are no paths on anyone's machine, and nothing assumes the reader's setup.

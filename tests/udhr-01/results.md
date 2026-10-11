# UDHR stress test (2026-10-11)

The author asked for the Universal Declaration of Human Rights as the site's first example page, adding words as needed. It doubles as the first long legal text.

**Method.** `terms.md`: terminology pass (92 concepts). `translation.md`: translated from `source.md` (English); `source-fr.md` (French, equally authentic) used for review. `notes.md`: translator's choices, revisions 2 and 3. Blind back-translations (`back-translation.md`, `back-translation-2.md`) by agents who never saw the original; scored per paragraph against English and French together (`scores.md`, `scores-2.md`: 2 = legal meaning kept, 1 = core kept, 0 = wrong). `relecture-fr.md`: review against the French, prompted and written in French so the reading isn't filtered through English. `make_page.py` builds `examples/01-udhr.md`.

| | v1 | v2 |
|---|---|---|
| Score | 89/116 (77%) | 104/116 (90%) |
| Paragraphs fully kept / core kept / wrong | 31 / 27 / 0 | 46 / 12 / 0 |
| Losses by cause: missing word / grammar / translator | 8 / 6 / 13 | 3 / 3 / 6 |

v3 fixed the six translator losses of v2. Revisions 4–8 applied the rules decided afterwards (pi is one noun, joined verbs, **li gun** "to be", nationality, **yenbo**, **kidun**, **anko**, **nuwen**, **ninsu**). Not re-scored since v2.

**New roots:** **dundi** respect/honour, **gigin** country/nation (design log).

**Language findings (open, for the author):**
1. Scope of a **pi** phrase next to a **yen**/**lu** list: whole list or nearest item? Undefined; the translation avoids it by repeating words. Most multi-readings came from it.
2. Scope of a phrase at the end of a clause over several joined verbs: all or the last? Undefined (Art 9's "arbitrary" first fell into it).
3. No way to say "be V-ed" with a right or duty: **li gun X** reads as "there is" (4.5), so "the right to be protected" makes the holder the protector (Art 25.2); "no one shall be V-ed" became "no one may V anyone".
4. Missing words, said with phrases that lose something: nationality (**ibe gigin**, Art 15, 16.1), justice/fair (**denku** "correct"), religion (**lite pi nosen**), principle, international (**lifin** "between"), rest (vs quit, Art 24), natural, competent; and the relation meanings without, against, until.
5. Unmarked past (Preamble 2) is by design: tense is optional.

**Parser.** Six constructions the reference allows were added to `tools/parse.py`, plus `--file`, and the double count of **li** + verb was merged. The translation now parses 152 sentences with one reading, 23 with several (equivalent or nonsensical alternatives), 2 not at all (a degree word inside a compared noun phrase; pronoun + manner word).

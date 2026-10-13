# Formal grammar: design (author approved GF, 2026-10-12; revised after the spike)

## Why

The same rule kept being written in several places (the reference, the lessons, the "Why" page, the parser), and they drifted apart: the lessons and the reference disagreed on where a manner word goes, and the parser couldn't see it. The author's decision (2026-10-12): build a formal grammar as the language's source of truth now, in Grammatical Framework (GF), as infrastructure no earlier language designer had.

## What GF gives

GF writes a grammar in two layers:

- **Abstract syntax:** the meanings the language can express, as typed trees (a clause, a noun phrase, a relative clause, a manner phrase…).
- **Concrete syntax:** how one language says each meaning. One concrete syntax is Apupiwe. A second is English, written with GF's Resource Grammar Library, which already knows English morphology and syntax.

So an Apupiwe sentence can be parsed into meaning trees, and each tree can be said in English mechanically. Tested on this machine: **guyi gun kudu** → "the house is big".

## What it checks

1. **Every sentence in every public document parses.** The reference's examples, the lessons, the "Why" page, the home page, the README and the declaration. A sentence that doesn't parse breaks a rule (or the grammar is missing one).
2. **Ambiguity is visible, counted two ways.** Readings that differ in *structure* (what attaches to what, where a clause ends) are counted separately from readings that differ only in a bare content word's *role* (thing, event or quality). The precise form has one structural reading; role readings are the ambiguity the language leaves to meaning on purpose. (The spike showed a single-tree rule can't work: a 14-word sentence can have 780 trees, almost all role readings.)
3. **Examples mean what their gloss says.** Key examples carry their intended meaning tree, and the check fails if the grammar doesn't produce it. The English the grammar generates from each tree, with brackets showing structure ("I watched [the person who came back] [in the morning]"), sits next to the hand-written gloss, so a mismatch is easy to see. It is a structural check, not an automatic gloss comparison.
4. **Rules and grammar point at each other** (deferred). Each grammar function carries the reference rule id it implements in a comment. A two-way check waits until a rule change misses its grammar function (add-back trigger); the spike didn't need it.

## How content words fit

Content words have no fixed word class: one word can be a thing, an event or a quality depending on how it's used. GF needs types, so the generated lexicon gives each root one function per role it can play (thing, event, quality), all with the same Apupiwe form. A bare content word then parses as each role it could fill, which is exactly the ambiguity the language intends; markers (**gun**, aspect words, **man**, **fu**) select one. The English side of each role comes from the word's gloss.

Two rules depend on a word's kind of meaning: **gun** + a word gives the undergoer's state only for action words, and verb + verb depends on whether the first verb takes an object. The lexicon gains one small column for these two features; it records meaning, not a word class, and is used only where a rule needs it.

## Parts

| Part | What | Source |
|---|---|---|
| `grammar/Apupiwe.gf` | abstract syntax: the meanings | written by hand, rule ids in comments |
| `grammar/ApupiweApu.gf` | Apupiwe concrete syntax | written by hand |
| `grammar/ApupiweEng.gf` | English concrete syntax, on the RGL | written by hand |
| `grammar/Lexicon*.gf` | the words | generated from `data/*.tsv` (never edited by hand) |
| `tools/check_all.py` | runs every check above on every document | new; replaces `tools/parse.py` once it covers the same ground |
| `flake.nix` | GF 3.12 (official binary, library paths patched) and the RGL release | so anyone can reproduce it |

## Spike result (2026-10-12)

`~/work/gf-spike/REPORT.md`: GF fits with caveats. 33/33 hard examples parse with the intended tree; 62% of the UDHR parses from the spike grammar; ≤0.12 s per sentence. Pauses, **kiyo**, slot order and the **pi**-list rule became grammar rather than post-filters. Costs: readings multiply with bare content words (any tool would), English good enough for structural checks only, tooling friction (compiled-only RGL, no Python bindings). Estimate: ~150–200 grammar functions; 3–5 sessions to parse the whole reference, 2–4 for English.

## Phases

1. **Toolchain** in the Nix setup; a smoke test.
2. **Core grammar:** the sentence template, noun phrase, relative clauses, particles, operators, numbers; generated lexicon; every reference example parses.
3. **English** concrete syntax; intended trees for the key examples; English shown next to every gloss.
4. **All documents** checked by one command.
5. **Later:** reference tables generated from the grammar; publishing refuses to go out while a check fails (automation last, once the checks have proven themselves).

`tools/parse.py` stays until phase 4 covers what it checks, then retires.

## What it doesn't do

- It doesn't decide meaning-level choices (whether a bare word is a thing or an event); those stay in the reference's prose, and the grammar shows the readings.
- It isn't a translator for general use. English is there to check glosses.

## Risks

- GF has a learning curve, and the grammar will take real work; phase 2 is the bulk.
- Generated English for content words in unusual roles can be clumsy (a gloss meant as a thing used as an event). Glosses in `lexicon.tsv` may need a little cleaning.
- The nixpkgs GF package is broken; the official binary is used instead. If it stops working, GF can be built from source with a small patch.

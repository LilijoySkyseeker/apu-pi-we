# Short-word layer, desk analysis (2026-10-13)

`analysis.py` checks every pair of short words (61 grammar words + digits 0–5) against mergers real speakers make: voicing (about a third of languages have no voicing contrast, WALS 4A), f = p (many languages lack /f/), a glide vs no onset (*wun* ~ *un*; also inserted automatically between vowels). Sources: cold review C §2 "word forms"; auxlang survey (natives of a designed language are bilingual, shaped by their other language).

## Findings

1. **The build tool's slot groups are too narrow.** Only 1 of its 336 same-slot pairs collapses under a merger (**un** "but" ~ **wun** "that"). Across all short words, 16 pairs do, and several share a position the groups don't model.
2. **Pairs that share a position and collapse under a merger** (the real risks):
   - **tin** (instruct) ~ **din** (we, not you): both open a sentence: *tin isi* "go!" / *din isi* "we're going". Voicing.
   - **bo** (some, unspecified) ~ **po** (0): both follow a noun: *ewo bo* "someone" / *ewo po* "no people". Voicing.
   - **pi** (of) ~ **bi** (very) ~ **fi** (1): all follow a noun before a word: *guyi pi kudu* / *guyi bi kudu* / *guyi fi*. Voicing, f = p.
   - **bu** (it) ~ **pu** (place-of): object position: *miya bu nawi* "see it eat" / *miya pu nawi* "see the eating place". Voicing.
   - **en** (name) ~ **yen** (and), **un** (but) ~ **wun** (that), **o** (focus) ~ **wo** (after) ~ **yo** (warn), **a** (you know) ~ **ya** (before), **yi** (obviative) ~ **wi** (even): a vowel-initial word after a vowel gets a glide in normal speech (*to en* → [toyen]), so these merge even for speakers who keep every contrast.
   - **pen** (we incl.) ~ **ben** (that), **ke** (more) ~ **ge** (result-of), **fu** (like) ~ **pu**: partial position overlap.
3. **Closest pairs by the confusion model** (no merger needed): **fa** (none) ~ **sa** (2) in the number slot (0.123, the review's first item), **fa** ~ **ka** (3), **ke** (more) ~ **fe** (also).
4. **Two-syllable operators that begin with a grammar word of the same position:** **wanme** (wan), **inwun** (in), **wemen** (we), **konsin** (kon), **mesun** (me), **manni** (man), **buni** (bu), **mena** (me).
5. **Vowel-only grammar words** (**a, o, en, in, un**) cause most of the glide problems; the review's designer A8 proposed that every grammar word have a consonant onset.

## Inventory for the rebuild (author, 2026-10-13)

The rebuild places these grammar words (data/grammar.tsv) plus:
- **added: MODMOD**, "the next word describes the previous modifier" (class: noun-phrase modifier position, after a content modifier): **demi wiwi** MODMOD **buda** "a dark-red cloth"; without it, every stacked modifier describes the noun (**demi wiwi buda** "a red, dark cloth"). Reference 5.1 gets the rule when the form exists.
- **kept, re-formed with a consonant onset: YOUKNOW (a)** "you see, as you know".
- **kept: EXCLAIM (ba)**, restored; every speech-act word's source is in rationale 4.3.
- Not changed by the inventory review: the other grammar words. Still open before the rebuild runs: the translators' grammar gaps (relation words inside a noun phrase; a derived word swallowing a following modifier; names containing a grammar word), which are rules rather than words unless the author decides otherwise.

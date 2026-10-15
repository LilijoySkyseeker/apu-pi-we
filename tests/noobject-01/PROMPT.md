You are reading a constructed language, Apupiwe. Its full reference grammar is docs/language.md and its words are in data/lexicon.tsv, data/grammar.tsv and data/compounds.tsv (all in this repository; read what you need). Don't read anything under tests/ except tests/noobject-01/blind.tsv, and don't read docs/design-log.md.

tests/noobject-01/blind.tsv has 16 short items (each one or two sentences; read each item on its own, as a small text). For each item, translate it into natural English the way a careful reader of the reference would understand it. Then, for the last sentence of the item, say in a few words who does what to whom (if anything is left unsaid, say what you take it to be), and how sure you are (sure / probably / could be either).

Output only a TSV with a header line "n<TAB>translation<TAB>who_does_what<TAB>sure", one line per item.

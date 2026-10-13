# Phrase guesses: author vs AI reader (2026-10-13)

30 phrases translators used for missing words, given word for word with their situation (`items.tsv`). The author (American English speaker) and a cold AI reader (blank sheet, `ai-guesses.tsv`) guessed independently.

| | right | hedged (right among options) | wrong |
|---|---|---|---|
| author | 19 | 4 (soup, screwdriver, doctor, mouse) | 7 |
| AI reader | 28 (cash → "banknote", bank card → "credit card" counted right) | 0 | 2 (doctor → nurse, printer → keyboard) |

The AI got right, where the author missed: fork (whisk), ice cream (shaved ice), wine (tea), bottle (glass), motorcycle (food truck), scrambled eggs (some egg dish), printer (pen/keyboard; the AI missed it too), plus the four hedges. Both missed printer.

**Reading:** the AI reader resolves about a third of the phrases a person misses or only half-gets. Round-trip scores read by AI understate the meaning lost to missing words; the real benefit of roots is larger than coverage-01 part 2 measured.

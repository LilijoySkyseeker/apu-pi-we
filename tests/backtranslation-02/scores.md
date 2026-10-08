# Back-translation fidelity scores (bt2)

Scored against /tmp/bt2_ref/reference.txt using each segment's committed "Reading". Name spellings ignored.

| Seg | Content | Tone | Loss (for any score < 2) |
|-----|:------:|:----:|---|
| S1  | 2 | 2 | |
| S2  | 2 | 2 | |
| S3  | 2 | 2 | |
| S4  | 1 | 2 | Content: "money for the bus" became "money for a car" (the purpose changed). |
| S5  | 2 | 2 | |
| S6  | 1 | 2 | Content: "my bus card" became "my car papers" (a different object). The hedge on the card survived as "probably (80%)". |
| S7  | 2 | 2 | |
| S8  | 2 | 2 | |
| S9  | 1 | 2 | Content: the phone number reads 0142 785 309 instead of 0412 785 309 (the 2nd and 3rd digits are swapped). |
| S10 | 2 | 2 | |
| S11 | 1 | 2 | Content: "the day after tomorrow" became "tomorrow after one o'clock". The reader noted the right reading but rejected it. |
| S12 | 1 | 2 | Content: "he took the card" became "he took the papers" (same root error as S6). |
| S13 | 1 | 2 | Content: "that card" became "those papers" (same root error as S6). |
| S14 | 2 | 2 | |
| S15 | 2 | 1 | Tone: "Of course he did" (wry, he was always going to) became "Ha! He's already taken care of it". The amusement survives but the "of course, predictably" stance is lost. |

## Totals

- **Content: 24 / 30**
- **Force and tone: 29 / 30**
- **Segments with any 0: 0**

The single bus-card→car-papers error accounts for 3 of the 6 content points lost (S6, S12, S13). Together with bus→car (S4), lexical gaps account for 4 of the 6.

## Recurring kinds of loss

1. **Modern objects were swapped for the nearest available concept.** The bus became a car (S4) and the bus card became car papers (S6, S12, S13). The lexicon apparently has no "bus" or "card", and "big cart" was read as car. Wallet → "money bag" (S1) is harmless.
2. **Time expressions are ambiguous.** "wo + number" was read as a clock time ("after 1") instead of a day offset (S11).
3. **Digit errors.** The phone number came back transposed (S9). The reader's gloss shows the digits arrived as 0-1-4-2, so this is either an encoding error or a misread number word. The back-translation alone can't tell which.
4. **Idiomatic stance markers.** "Of course" was flattened into a generic exclamation (S15).

## Specific questions

**(a) Were the S2 and S12 contrasts understood as contrasts?**
Yes, both were rendered as contrasts.
- **S2:** "I didn't take it. Tomasa took it." keeps the denial-plus-accusation. The stress on *I* isn't marked, but the contrast is unmistakable.
- **S12:** "He didn't take the money… He took the papers." keeps money vs. object. The contrasted item is wrong (papers, not card). The reader also found S12 contradicted S11 ("return the money"), but that tension is in the original English too, so it isn't a translation loss.

**(b) Were all the numbers correct?** No: 3 of 5 were correct.
- Count: 42 dollars ✓
- Clock time: three ✓
- Ordinal: second ring ✓
- Phone number: ✗ (0142 785 309 vs 0412 785 309)
- Day: ✗ ("tomorrow after one o'clock" vs "the day after tomorrow")

**(c) Was every pronoun resolved to the right person?**
Yes, in every committed Reading:
- S2 and S5: it = wallet
- S4, S9, S11, S12 (both clauses), S13: he = Tomas
- S14: him = Dad
- S15: he = Tomas

Two of these were fragile.
- **S12b:** the switch from wan to yi made the reader consider "an unknown third party".
- **S15:** the reader said that under the other rule reading, "he" would be Dad.

Both times the reader committed to the right person, but by judgment, not by a documented rule.

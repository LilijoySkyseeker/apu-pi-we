# Vocabulary test 01: does the seed carry everyday text?

**Method:**
- Two original passages in genres not yet tested: a trickster folk tale in the West African style, and a farming family's day.
- Translated with only the 409-root seed, paraphrasing where words were missing.
- A fresh blind reader got the reference and word lists.

**Result:**
- The meaning came through almost everywhere. Spider ("small animal with many legs"), hungry ("needs food"), tea ("water of leaf"), grandmother, neighbours, harvest, the radio ("thing for listening") and "together" (**nen nen**) were all recovered.
- **Lost to missing words, about 2–3 points:**
  - yams → "food";
  - goats → "cattle", from "horned animals";
  - rice → "grain";
  - basket → "bag" (minor).

  **That's more than the 1-point trigger**, so the seed grew (batch 2, `tools/seed_batch2.py`, since removed; in git history).
- **Translator errors:** two words used stale forms from an earlier rebuild: **Ate** "far" and **ban** "rather". The reader flagged both as unknown. This was the third such slip, which triggered `tools/check.py` (roadmap C3).

**Batch 2:**
- 29 roots from ranks 301–650 present in all six macro-areas: spider, turtle, basket, frog, chicken, fruit, lake, lightning, clothes, steal, hunt, count…
- 7 on-demand roots from this test: goat, tuber (yam), rice, field, boil, reach, gather.
- 12 built words and compounds: knife = "tool for cutting", axe = "tool for splitting", grey = "white dark", harvest = "gathering of food"…
- The lexicon is now 445 roots.

**Next:** fresh texts until two tests in a row lose under 1 point to missing words (the stop condition).

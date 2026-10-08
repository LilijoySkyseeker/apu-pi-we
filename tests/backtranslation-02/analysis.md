# Back-translation test 02: analysis

**Setup:** same method as test 01 (fresh reader with only `language.md`, `grammar.tsv`, `lexicon.tsv` and `compounds.tsv`; a fresh judge), on text 003, an original passage. One leaked example in the reference ("Tomas called him") was replaced before the test.

**Result:**
- **Content: 24/30 (80%).**
- **Force and tone: 29/30 (97%).**
- No segment scored 0.
- Every pronoun was resolved correctly, but two only by judgment.
- Both contrasts were understood with no focus device.

**Where the 7 points went:**

| Points | Cause |
|---|---|
| 4 | Modern vocabulary (bus → car, card → papers ×3) |
| 1 | Day offset read as a clock time |
| 1 | Translator's digit error in the phone number |
| 1 | "of course" idiom flattened |

Grammar caused no direct losses. It did produce two near-misses in pronoun reference (narration vs quotes; **yi** with three people), now fixed.

**Compared with test 01:** content 80% (was 86%), tone 97% (was 91%). The texts differ, so this is not a trend. Test 02 was built to stress numbers and modern objects, which is where it lost.

Fixes are listed in `texts/003-the-wallet.md`.

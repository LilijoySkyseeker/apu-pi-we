# Grammar-space rebuild: spec

Agreed with the user 2026-10-10. The language is still in design (freeze
lifted), so this is the cheapest time for it.

## Goal

Shortest forms for the most frequent meanings (Zipf). Today the most frequent
new operators (**fule**, **iwun**, **buni**, **wame**, **manni**, **genfo**)
have two syllables, while one-syllable slots are held by some of the rarest
grammar words (**san**, **o**, **a**, **yo** at 0.5; **fen**, **fon**,
**pa**, **sun** at 1 or less).

**Non-goals:** no change to sounds, syllable shape or content words; no new
meanings.

## Steps

1. **Candidates:** every grammar word, plus the two-syllable roots that work
   like grammar: **fule**, **genfo**, **wame**, **manni**, **iwun**,
   **buni**, **donon**, **tason**, **nedin**, **mesun**, **lanno**.
2. **Measured frequency** (`tests/grammar-rebuild/frequency.tsv`): each
   meaning's translation equivalents in several major languages, looked up
   with `wordfreq` and averaged (median, to damp polysemy). Meanings with no
   word equivalent (endings, particles some languages lack) are flagged as
   judgement.
3. **Constraints unchanged:** same-slot first consonant (`GROUPS_STRICT`),
   drift distinctness (`GROUPS_WIDE`), no final-n pairs, juncture rules,
   offensive filter and `REJECTED`.
4. **Stability penalty:** moving a form costs something, so only clear gains
   move. Fixed: **to** "I", digits 0–5.
5. **Review gate:** a table of promoted, demoted and unchanged words with the
   syllable saving goes to the user before anything is applied.
6. **Validation after applying:** `juncture.py`, `check.py` on every doc
   example, one blind round trip.
7. **Migration:** span-aware replacement in the docs (as for **lon** →
   **to**); tests and texts stay as records.

## Planning for future issues

- **Keep 2–3 one-syllable slots free** for the next high-frequency need.
- **Promotion rule:** a meaning earns a one-syllable form only when its
  measured frequency beats the rarest current holder. Rebuilds happen only in
  design; once the user starts learning, the freeze returns and natural
  clipping takes over (drift.md).
- **Record frequency sources** in `grammar.tsv` (new column).
- **No automatic check yet.** Trigger: the promotion rule gets missed again.

## Digits 6–9 (decided alongside: leave at two syllables)

The base-6 transmission test found six one-syllable digits far more robust
than ten (0.26% vs 2.3% wrong-digit rate on a 10-digit ID). A two-syllable
digit survives a noise burst that wipes one syllable (the ICAO lesson).
Confidence no longer uses 6–9. Add back if a spoken test shows number
readings too slow.

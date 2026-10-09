# Vocabulary plan (roadmap B1)

Agreed in discussion with the user, 2026-10-08. **Seed phase complete** (stop condition met by vocabulary tests 04 and 05); words are now added on demand.

## Goal and what it serves

The chain: vocabulary → "any concept can be named by rule" → a language that carries real text → the user's goals (learning, a good language, the thought experiment).

The user is mostly interested in the **method**, not the word list. So the deliverable is a decision procedure backed by evidence, plus a seed vocabulary that proves it works.

## Decisions

| Part | Decision | Source |
|---|---|---|
| Scope | Method plus a seed of the ~500–800 most frequent concepts; after that, words on demand. No 2,000–3,000 target. | user (chose Claude's recommendation) |
| Stop condition | Two fresh blind tests in a row lose under 1 point to missing words | Claude |
| Cultural neutrality | **Strong rigor**: concepts and their boundaries come from cross-linguistic data, not English or Claude's intuition | user |
| Order of building | Shared human experience first: concepts named across the most languages and learned earliest by children everywhere. Expansion follows the same criterion, so culture-specific distinctions arrive naturally as the vocabulary grows; there is no separate "richness" layer. | user (first principles of human experience) |
| Two layers (user, 2026-10-08) | **Modern text decides what's common and needed; base human existence stays the foundation.** The *deep layer* (body, family, perception, emotion, basic actions, basic nature, space, time, logic) is weighted by independent lineages, because independent invention there is evidence about humans. The *world layer* (objects, animals, plants, places, institutions, technology) is weighted by need in the modern world, measured by blind tests on modern urban texts from many cultures, not by a corpus pipeline. World-layer things are built words by default ("tool for talking far"), because technology churns and built words stay transparent; frequent ones may later be clipped into roots. Reason: the cross-linguistic concept lists were designed to document traditional vocabulary, and lineage weighting amplifies small-scale societies, so ranks past the deep core over-weight spear, canoe and scorpion. | user + Claude |
| Weighting | By independent lineages (language families and long-contact areas), not by speakers. Each lineage is one independent experiment in carving human experience; speaker counts measure which societies expanded. | user (no speaker weighting) + Claude (lineage weighting) |
| Target | Not pure neutrality (any vocabulary draws boundaries somewhere) but the efficient frontier: simplicity vs informativeness, weighted by how often humans need each distinction. Use the formal models only where published ones exist (colour, kinship, numbers, some spatial terms); elsewhere, the lineage-weighted majority. | Claude, agreed by user |
| The lens | What a language makes cheap shapes what its speakers notice (modest but real effects on attention and memory). Which distinctions are cheap is chosen per domain, with evidence, as already done for confidence, source, reference and inclusive "we". | user (language as lens) + Claude |
| Opposites and topic areas | Tagged for the optimizer, as now | existing method |
| Tooling | Existing tools only; one data-extraction script if a dataset needs it. No new pipeline. | Claude, per the "automate last" rule |

## Why there is no separate richness layer

The user's challenge (2026-10-08): richness isn't a different kind of thing, just more ideas. Build the base of shared human experience first, and richness arrives as it expands. That's right. One criterion orders everything: how widely a concept is shared across human languages and experience, weighed against what it costs to paraphrase. Distinctions only some cultures name rank lower because fewer languages name them, and they arrive when expansion reaches them. Claude's earlier separate richness layer with a 10% cap is deleted. Add back a separate priority only if tests show meaning lost specifically to missing culture-specific distinctions while common words are covered.

Cultural neutrality matters from the very first word in a different way: in where each concept's **boundaries** are drawn. Shared concepts are still carved differently: arm and hand as one word or two, siblings by sex or by relative age, blue and green. Those carving decisions come from cross-linguistic data, not English.

"How language works for humans" gives a second ordering signal besides frequency across languages: the order in which children everywhere learn words (cross-linguistic early-vocabulary data). Concepts children learn first in many languages are the core of shared experience.

## Steps

1. **Research** (sources to evaluate, not yet read):
   - Basic concept lists across traditions: Concepticon and the lists it links, Swadesh, Leipzig–Jakarta, NSM primes and molecules, WOLD.
   - Cross-linguistic concept frequency.
   - Colexification (CLICS): which meanings languages lump together and which they split.
   - Lexical-typology domains where languages carve the world differently: kinship, colour, space and frames of reference, motion, cutting and breaking, perception (including smell, e.g. Jahai), emotion (e.g. Jackson et al. 2019), time, possession, the body.
   - Cross-linguistic early vocabulary: which words children learn first across languages (e.g. Wordbank / CDI data).
2. **Decision procedure**, written down: for each concept, a root, a built word (marker), a compound with a relation word, a loan, or left to a phrase. Criteria: frequency, how many languages name it, paraphrase cost, and a colexification policy. The working proposal: split a lumped meaning when the lump causes action-relevant misunderstanding; otherwise follow the majority of languages.
3. **Seed:** apply the procedure to the concept data in order of shared experience. Output: a concept table with each decision and its evidence.
4. **Build** with the existing tools (`words.py`), tagging topic areas and opposites.
5. **Test:** fresh blind back-translations of **modern urban texts from many cultures** (markets, transit, offices, clinics, news), measuring loss to missing words. Missing world-layer concepts become built words unless frequent; continue until the stop condition holds.

## Doghouse guards

- The colexification (boundary) work is the part most likely to grow without limit. Each split or lump needs its evidence line in the concept table.
- If research shows a dataset can't be used without building a pipeline, report that and choose a cheaper source rather than building one.
- Add back the 2,000–3,000 target only if tests keep losing to missing words after the seed.

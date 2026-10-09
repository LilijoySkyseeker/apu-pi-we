# Vocabulary plan (roadmap B1)

Agreed in discussion with the user, 2026-10-08. Nothing in this plan has been built yet.

## Goal and what it serves

The chain: vocabulary → "any concept can be named by rule" → a language that carries real text → the user's goals (learning, a good language, the thought experiment).

The user is mostly interested in the **method**, not the word list. So the deliverable is a decision procedure backed by evidence, plus a seed vocabulary that proves it works.

## Decisions

| Part | Decision | Source |
|---|---|---|
| Scope | Method plus a seed of the ~500–800 most frequent concepts; after that, words on demand. No 2,000–3,000 target. | user (chose Claude's recommendation) |
| Stop condition | Two fresh blind tests in a row lose under 1 point to missing words | Claude |
| Cultural neutrality | **Strong rigor**: concepts and their boundaries come from cross-linguistic data, not English or Claude's intuition | user |
| Richness of meaning | Draw deliberately on distinctions some languages make and most don't, so the language can carry thoughts most single languages can't | user |
| Opposites and topic areas | Tagged for the optimizer, as now | existing method |
| Tooling | Existing tools only; one data-extraction script if a dataset needs it. No new pipeline. | Claude, per the "automate last" rule |

## Richness and the north star

The user's point is about expressiveness, not sound. It fits the north star rather than competing with it. A thought with no word has to be paraphrased, and paraphrase is where meaning gets lost. So a word for a distinction some culture has found worth naming makes that thought transmittable.

The limit is the same north star from the cost side: every word is something children must learn and something the confusion model must keep apart. So a richness concept earns a root only with:
- **evidence** that the distinction is real and used, from lexical typology or ethnography, not "untranslatable words" listicles;
- a **paraphrase cost** worth saving: it's long or lossy to say otherwise;
- a **cap**: richness roots stay a small share of the seed (proposed ≤ 10%) until tests show they're used.

## Steps

1. **Research** (sources to evaluate, not yet read):
   - Basic concept lists across traditions: Concepticon and the lists it links, Swadesh, Leipzig–Jakarta, NSM primes and molecules, WOLD.
   - Cross-linguistic concept frequency.
   - Colexification (CLICS): which meanings languages lump together and which they split.
   - Lexical-typology domains where languages carve the world differently: kinship, colour, space and frames of reference, motion, cutting and breaking, perception (including smell, e.g. Jahai), emotion (e.g. Jackson et al. 2019), time, possession, the body.
   - Evidence-backed lexicalized distinctions that are rare elsewhere (richness candidates).
2. **Decision procedure**, written down: for each concept, a root, a built word (marker), a compound with a relation word, a loan, or left to a phrase. Criteria: frequency, how many languages name it, paraphrase cost, and a colexification policy. The working proposal: split a lumped meaning when the lump causes action-relevant misunderstanding; otherwise follow the majority of languages.
3. **Seed:** apply the procedure to the concept data, plus capped richness candidates. Output: a concept table with each decision and its evidence.
4. **Build** with the existing tools (`words.py`), tagging topic areas and opposites.
5. **Test:** fresh blind back-translations of texts from varied cultures and genres, measuring loss to missing words; continue on demand until the stop condition holds.

## Doghouse guards

- The colexification and richness work are the parts most likely to grow without limit. Each richness root needs its evidence line in the concept table, and the cap holds until tests ask for more.
- If research shows a dataset can't be used without building a pipeline, report that and choose a cheaper source rather than building one.
- Add back the 2,000–3,000 target only if tests keep losing to missing words after the seed.

# Vocabulary plan (roadmap B1)

Agreed in discussion with the author, 2026-10-08. **Superseded in scope (author, 2026-10-13):** the seed grows to cover modern life, sized by measurement (see the end). **Seed phase complete** (stop condition met by vocabulary tests 04 and 05); words are now added on demand.

## Goal and what it serves

The chain: vocabulary → "any concept can be named by rule" → a language that carries real text → the author's goals (learning, a good language, the thought experiment).

The author is mostly interested in the **method**, not the word list. So the deliverable is a decision procedure backed by evidence, plus a seed vocabulary that proves it works.

## Decisions

| Part | Decision | Source |
|---|---|---|
| Scope | Method plus a seed of the ~500–800 most frequent concepts; after that, words on demand. No 2,000–3,000 target. | author (chose Claude's recommendation) |
| Stop condition | Two fresh blind tests in a row lose under 1 point to missing words | Claude |
| Cultural neutrality | **Strong rigor**: concepts and their boundaries come from cross-linguistic data, not English or Claude's intuition | author |
| Order of building | Shared human experience first: concepts named across the most languages and learned earliest by children everywhere. Expansion follows the same criterion, so culture-specific distinctions arrive naturally as the vocabulary grows; there is no separate "richness" layer. | author (first principles of human experience) |
| Two layers (author, 2026-10-08) | **Modern text decides what's common and needed; base human existence stays the foundation.** The *deep layer* (body, family, perception, emotion, basic actions, basic nature, space, time, logic) is weighted by independent lineages, because independent invention there is evidence about humans. The *world layer* (objects, animals, plants, places, institutions, technology) is weighted by need in the modern world, measured by blind tests on modern urban texts from many cultures, not by a corpus pipeline. World-layer things are built words by default ("tool for talking far"), because technology churns and built words stay transparent; frequent ones may later be clipped into roots. *(Reconciled 2026-10-13: frequent, established concepts get roots now, the planned clipping done up front; the built default stands for the long tail and new technology. Churn doesn't favour built words: words of both kinds follow their referents, e.g. *phone*, Chinese 电话.)* Reason: the cross-linguistic concept lists were designed to document traditional vocabulary, and lineage weighting amplifies small-scale societies, so ranks past the deep core over-weight spear, canoe and scorpion. | author + Claude |
| Weighting | By independent lineages (language families and long-contact areas), not by speakers. Each lineage is one independent experiment in carving human experience; speaker counts measure which societies expanded. | author (no speaker weighting) + Claude (lineage weighting) |
| Target | Not pure neutrality (any vocabulary draws boundaries somewhere) but the efficient frontier: simplicity vs informativeness, weighted by how often humans need each distinction. Use the formal models only where published ones exist (colour, kinship, numbers, some spatial terms); elsewhere, the lineage-weighted majority. | Claude, agreed by user |
| The lens | What a language makes cheap shapes what its speakers notice (modest but real effects on attention and memory). Which distinctions are cheap is chosen per domain, with evidence, as already done for confidence, source, reference and inclusive "we". | author (language as lens) + Claude |
| Opposites and topic areas | Tagged for the optimizer, as now | existing method |
| Tooling | Existing tools only; one data-extraction script if a dataset needs it. No new pipeline. | Claude, per the "automate last" rule |

## Why there is no separate richness layer

The author's challenge (2026-10-08): richness isn't a different kind of thing, just more ideas. Build the base of shared human experience first, and richness arrives as it expands. That's right. One criterion orders everything: how widely a concept is shared across human languages and experience, weighed against what it costs to paraphrase. Distinctions only some cultures name rank lower because fewer languages name them, and they arrive when expansion reaches them. Claude's earlier separate richness layer with a 10% cap is deleted. Add back a separate priority only if tests show meaning lost specifically to missing culture-specific distinctions while common words are covered.

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

## Words the tests found missing (noted 2026-10-10)

**Added 2026-10-10:** 22 roots: almost **nedin**, each **mesun**, suddenly **finbi**, late **yodun**, early **ganna**, trust **gewan**, love **wigen**, miss **sanku**, disappointed **kinbo**, hungry **monyu**, tired **fadun**, strange **lenya**, safe **sonli**, expensive **unwi**, cheap **tanbu**, room **fudon**, box **nansa**, storey **sison**, oil **yunen**, marry/wedding **bedan**, a right **sogan**, complain **tayin**; earlier the same day: even **genfo**, noon **minfi**, afternoon **duwun**, "it turned out" **donon**. Built words in `compounds.tsv`: landlord, neighbour, kitchen, warehouse, move house, park, yell, part-time work, free of charge. Lumped: law = **wabun** "rule". Left as phrases: formally, pessimistic, bothersome, pity, basin, gate, beard, queue, demand, criticise, block, flood, text, "sorry" as sympathy (**to feme bayi li me**). Loans added the same day, in their international form (**foto**, not English "photo"; **yulo** euro; **polisu**): email, photo, train, licence, electricity, degree, hospital, bicycle, battery, euro, yuan, rupee, police. Brands (Uber, WeChat, Alipay, LINE) follow the name rule. Not loans, because their form isn't shared internationally, so they're described: deadline, truck, screen, plug, socket, wire, elevator, petrol, air conditioning, spreadsheet, navigation, intern, driver, transport, stamp, photocopy.

**Added 2026-10-11 (UDHR):** respect/honour **dundi**, country/nation **gigin**, rest **yenbo**, fair/just **kidun**, until **anko**, without **nuwen**, oppose **ninsu** (design log).

The original list:

The normal process: these come from what tests actually needed. Each still
goes through the vocabulary method (root, built word or phrase; lump/split)
before it's added. Source in brackets: E = economy test 01, J = round-trip
Japanese, M1 = multilang stage 1 inventories, M2 = multilang stage 2 round
trips.

- **Function and stance words:** even (M1 ×9, M2), almost (M1), each (M1,
  M2 Vietnamese legal), suddenly (M1, M2), early (M2 Russian), late (E, M1,
  M2), "it turned out" (M2 Arabic), "as expected of you" (J), formally (M2
  Spanish).
- **Feelings and states:** trust (M2 Hindi), love, miss, disappointed (M1),
  "sorry" as sympathy, not apology (M1), hungry, tired (M1), pessimistic (M2
  Arabic), bothersome / can't be bothered (J), strange (M2 Hindi), "poor
  fellow" pity (M2 Hindi).
- **Everyday life:** cheap, expensive (E, M1), rent as a noun (E), landlord,
  neighbour (E, J, M2), kitchen (E), room (J), box (J), gate (M2
  Vietnamese), storey / floor of a building (M2 Mandarin), basin (M2
  Mandarin), oil (M2 English), midday / lunch (J, M2 Hindi), afternoon (J),
  wedding (M2 Hindi), beard (M2 Hindi), warehouse (M2 Hindi), queue (M2
  Arabic), part-time job (J, M2 Vietnamese), free of charge (J), law (M2
  Mandarin), a right / entitlement (M2 Spanish), safety (M2 Mandarin), dock
  someone's pay (M2 Hindi).
- **Verbs found flattened:** move house (J), park (E), flood (E), yell (E),
  text / message (E), demand (M2 Vietnamese), complain, criticise (M2
  Vietnamese), block (E, M2 English).
- **Loans used under the borrowing rule but not yet in the lexicon:** email,
  photo, photocopy, stamp, train, petrol, licence, spreadsheet, navigation,
  air conditioning, electricity, deadline, degree (°), truck, hospital,
  driver, intern, transport, bicycle, elevator, battery, plug, socket,
  screen, wire, euro, yuan, rupee, police, button, manga, Uber, WeChat,
  Alipay, LINE.

## Coverage of modern life (author, 2026-10-13)

The 2026-10-08 seed stopped too early: its stop condition used AI translators, who talk around a missing word far better than people (cold review, A3 4.1, A6). New scope:

- **Seed, then release.** Build the best base, then leave the language to its speakers (B9, N4). No process for promoting or fusing phrases (`vocabulary-method.md` §5.4).
- **Complete coverage.** Every concept common in modern text and speech gets a root, including concepts new to history (train, hospital). Phrases are for rarer concepts and for anyone who doesn't know a word yet.
- **Size by measurement.** Sample modern everyday text and speech (conversation, chat, news, instructions) in languages from every panel region, and measure added length and meaning lost at about 500, 1,000 and 1,500 roots, judged by people where possible. Expected 1,000–1,500; the measurement decides. Checks on growth: B2 (about 4,000 two-syllable forms exist; 500 are used) and B10.
- **Layers stay.** Deep-layer concepts are chosen by convergence across lineages and early child vocabulary; modern frequency picks the world layer and can't remove a deep-layer concept. Frequency is measured per language, each language counted once (N3).
- Each new root goes through the ladders (`vocabulary-method.md` §0). The seven phrase replacements of 2026-10-13 stand until the pass reaches them.

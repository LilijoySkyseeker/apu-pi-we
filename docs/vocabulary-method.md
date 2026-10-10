# Vocabulary method (roadmap B1, step 2): draft

The decision procedure for choosing concepts and drawing their boundaries. Built on the plan (`vocabulary-plan.md`) and four research notes: `concept-sources.md`, `colexification.md`, `efficient-semantics.md`, `early-vocabulary.md`. Seed size and the lump/split rule were agreed by the user on 2026-10-08. Colour awaits the colour-vision check. The seed decisions are recorded in `data/concepts.tsv` (built by `tools/seed.py` and `seed_batch2.py`, removed 2026-10-09 as single-use; in git history).

## 1. Which concepts, in what order

1. **Core pool: CLICS4 concepts ranked by area-balanced lineage coverage.** CLICS4 has 3,432 varieties in 247 families. Coverage is the share of each macro-area's families whose word lists name the concept, averaged over the six areas. Raw family counts would let New Guinea and the Americas dominate; area averaging corrects that.
2. **Only the top ~300 are data-backed.** Beyond about rank 300 the counts reflect which questionnaires reached which regions, not which concepts languages name, and the questionnaires descend from Buck's 1949 Indo-European dictionary. **Agreed (user, 2026-10-08):** the seed is therefore ~300 data-backed concepts plus the NSM primes not already covered, instead of the planned 500–800. Everything after that is added on demand from blind tests on texts from varied cultures and genres. Bring back the larger seed if the first tests lose more than 1 point to missing everyday words.
3. **NSM primes** (Goddard's 63–65) are a checklist for function and logic concepts the lists omit (WANT, BECAUSE, IF, MAYBE), not a frequency source. Their universality is contested.
4. **Children's early vocabulary** (Wordbank) is a second signal at the level of categories. It breaks ties near the top and admits social routines and interjections (hi, bye, no) that basic lists leave out. Onomatopoeia and baby words are left out. Add them back if tests lose points to missing interjections.

**The deep-layer criterion is convergence of independent signals** (agreed with the user, 2026-10-08). Three signals are used: breadth across lineages, what children learn first, and survival over long time spans. Each has its own bias: fieldwork questionnaires, a Western-skewed child sample, and Eurasian-heavy reconstructions. Where they agree, the biases largely cancel. Lineage breadth already integrates deep time, since every family descends from an ancestor thousands of years old. Time-stability, meaning the survival of *word forms* (Holman 2008, Pagel et al. 2007/2013), is used as a corroboration check, not a separate ranking. It mostly tracks frequency of use, says nothing about the world layer, and also preserves words that are stable but no longer central (louse, bark, ashes). Check run 2026-10-08: the seed already covered all of Holman's 40 most stable concepts and all but one of Pagel's 23 "ultraconserved" words (worm); the Leipzig–Jakarta list added grind. Both were added.

Dropped sources, each with a trigger to bring it back:
- Concepticon list counts: circular, since they reflect linguists' choices. Back if CLICS4 lacks a needed concept.
- NoRaRe and Dellert's measure: not lineage-balanced. Back if ties can't be broken.
- Lexibank: CLICS4 is its balanced subset. Back if a concept is missing.

## 2. What form each concept takes

For each concept, in order:
1. If the grammar or existing words already say it without loss, add **no** root.
2. If it's a doer, thing done or made, tool or place of an existing verb, it's a **built word** (`no`, `ge`, `du`, `pu`).
3. If it's in the core pool and languages typically use a single unanalysable word for it (WOLD simplicity), it's a **root**.
4. Otherwise it's a **compound with a stated relation** (`se`, `pi`, `li`, …).
5. **Loans** only for names and brands.

## 3. Where boundaries go (lump or split)

Applied in this order (`research/notes/colexification.md`; lineage rates from `tools/clics_rates.awk`):

1. **A published efficiency model exists** (colour, kinship, numerals): the model plus human need decide, per the agreed target.
   - **Colour (decided, verified 2026-10-08, `research/notes/colour-vision.md`):** six basic roots (black, white, red, yellow, green, blue). The support is from colour *naming*, not eye physiology. The best-example colours in 110 unwritten languages cluster near these six, and every system with more than five basic terms separates blue and green. The "opponent channels" argument doesn't hold: the elementary hues don't line up with the eye's channels (Webster et al. 2000). Lumping green and blue (57% in WALS, a sample of mostly small societies) is a coarser cut of the same perceptual space, driven by low need ("there simply are not that many natural blue objects", Gibson et al. 2017), not a perceptual error. So separate blue rests on need plus naming data. Other colours are compounds (grey = white + dark). Stopping at six is a deliberate root-budget choice; industrial languages often have about 11 basic terms (unverified). Add roots if tests show colour meaning lost.
   - **Kinship:** roots mother, father, child, sibling (no sex), spouse. Cheap optional modifiers for older/younger and male/female; everything else composed ("mother's sibling"). Kinship systems vary too much to copy: 410 systems among 487 languages.
   - **Numerals:** unchanged (base 6).
2. **Frequent alternatives in the same slot, where confusing them changes what the listener does → two roots.** This is the "action-relevant misunderstanding" test made concrete: left/right, buy/sell, lend/borrow, give/take. It agrees with the Goldilocks finding that languages avoid lumping meanings that compete in context.
3. **Otherwise, the family-balanced lump rate** (agreed by the user, 2026-10-08):
   - lumped by ≥ 50% → one root; the narrow sense is built when needed (e.g. moon/month);
   - 20–50% → two words, the less basic built transparently from the other;
   - < 20% → two unrelated roots (e.g. see/know 3%, eat/drink 7%, finger/toe 16%).

   The 50% and 20% cut points were proposed by the research agent and are arbitrary. Refine them only if tests show losses near a threshold. Where CLICS4 copies a broad meaning onto narrower ones (uncle, he/she, we), its rate is an upper bound; cross-check with WALS or Kinbank.
4. **A shared English word is not evidence for a lump** (2026-10-10). Two concepts that English happens to call the same thing (fly the insect / fly the verb, light / light) go through steps 1–3 like any other pair. The seed matched concepts to roots by English gloss and skipped this; glosses now carry a second gloss wherever the English is ambiguous.
5. **Never derive one meaning from another along a link only one family uses.** For example, don't build "know" from "see", which is an Indo-European habit.

Every decision gets an evidence line in the concept table.

## 3b. Observation, not theory (agreed with the user, 2026-10-08)

Some word boundaries encode a belief about how the world works: "the sun *rises*", *lunatic*, *influenza*, *malaria*, "catch a cold", whales grouped with fish. Others encode perception or need (blue/green, arm/hand). Only the first kind can be outdated.
- **Basic words describe what is experienced, not a theory of it.** "The sun appears", not "rises". An illness is named by its symptoms, not a supposed cause.
- **Theory-laden concepts are built compositionally from observational words**, so they can be rebuilt when knowledge changes without disturbing the basic layer. Current science gets no special status either: it changes too.
- **A lineage pattern that rests on a disproven belief gets no weight**, however common it is, and the concept table records why.
- **Metaphors are chosen deliberately**, not inherited (English "heartbroken" keeps the heart as the seat of emotion).

Perception-and-need boundaries are never "outdated". For them, science can only give a reason to pick a particular point on the efficient frontier. Colour is the test case: see `research/notes/colour-vision.md` once verified.

## 4. What to make cheap (the lens)

Already cheap by design: confidence, source of knowledge, reference, inclusive/exclusive "we", exact number (one-syllable digits).

To add:
- short roots for **both** spatial frames: left/right **and** the cardinal directions;
- **no** extra colour roots for the lens's sake (colour effects are small);
- smell vocabulary only if tests show it's missed.

**Evidence (verified 2026-10-08, `research/notes/lens.md`):** the lens acts on tracking, memory and communication, not perception. Exact number is well established; spatial frames covary with language but causation is contested; colour effects are modest and the perceptual claims fail replication; smell naming effects are large. The choices above stand.

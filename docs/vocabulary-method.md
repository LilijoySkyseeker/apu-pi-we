# Vocabulary method (roadmap B1, step 2): draft

The decision procedure for choosing concepts and drawing their boundaries. Built on the plan (`vocabulary-plan.md`) and four research notes: `concept-sources.md`, `colexification.md`, `efficient-semantics.md`, `early-vocabulary.md`. **Draft:** three points marked **[decide]** need the user before the seed is built.

## 1. Which concepts, in what order

1. **Core pool: CLICS4 concepts ranked by area-balanced lineage coverage.** CLICS4 has 3,432 varieties in 247 families. Coverage is the share of each macro-area's families whose word lists name the concept, averaged over the six areas. Raw family counts would let New Guinea and the Americas dominate; area averaging corrects that.
2. **Only the top ~300 are data-backed.** Beyond about rank 300 the counts reflect which questionnaires reached which regions, not which concepts languages name, and the questionnaires descend from Buck's 1949 Indo-European dictionary. **[decide]** The seed is therefore ~300 data-backed concepts plus the NSM primes not already covered, instead of the planned 500–800. Everything after that is added on demand from blind tests on texts from varied cultures and genres. Bring back the larger seed if the first tests lose more than 1 point to missing everyday words.
3. **NSM primes** (Goddard's 63–65) are a checklist for function and logic concepts the lists omit (WANT, BECAUSE, IF, MAYBE), not a frequency source. Their universality is contested.
4. **Children's early vocabulary** (Wordbank) is a second signal at the level of categories. It breaks ties near the top and admits social routines and interjections (hi, bye, no) that basic lists leave out. Onomatopoeia and baby words are left out. Add them back if tests lose points to missing interjections.

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
   - **Colour [decide]:** six basic roots (black, white, red, yellow, green, blue), as the lexicon already has. Most World Color Survey languages (57%) use one word for green and blue, so a separate blue is a deliberate break from the majority. The reason is need: precise colour talk rises with technology (dyes, signals, displays), and the agreed target weights need over head-count where a model exists. Other colours are compounds.
   - **Kinship:** roots mother, father, child, sibling (no sex), spouse. Cheap optional modifiers for older/younger and male/female; everything else composed ("mother's sibling"). Kinship systems vary too much to copy: 410 systems among 487 languages.
   - **Numerals:** unchanged (base 6).
2. **Frequent alternatives in the same slot, where confusing them changes what the listener does → two roots.** This is the "action-relevant misunderstanding" test made concrete: left/right, buy/sell, lend/borrow, give/take. It agrees with the Goldilocks finding that languages avoid lumping meanings that compete in context.
3. **Otherwise, the family-balanced lump rate [decide: thresholds]:**
   - lumped by ≥ 50% → one root; the narrow sense is built when needed (e.g. moon/month);
   - 20–50% → two words, the less basic built transparently from the other;
   - < 20% → two unrelated roots (e.g. see/know 3%, eat/drink 7%, finger/toe 16%).

   The 50% and 20% cut points were proposed by the research agent and are arbitrary. Refine them only if tests show losses near a threshold. Where CLICS4 copies a broad meaning onto narrower ones (uncle, he/she, we), its rate is an upper bound; cross-check with WALS or Kinbank.
4. **Never derive one meaning from another along a link only one family uses.** For example, don't build "know" from "see", which is an Indo-European habit.

Every decision gets an evidence line in the concept table.

## 4. What to make cheap (the lens)

Already cheap by design: confidence, source of knowledge, reference, inclusive/exclusive "we", exact number (one-syllable digits).

To add:
- short roots for **both** spatial frames: left/right **and** the cardinal directions;
- **no** extra colour roots for the lens's sake (colour effects are small);
- smell vocabulary only if tests show it's missed.

**Evidence caveat:** the effect sizes behind the lens (Russian blues, spatial frames, Pirahã and Mundurukú number, Jahai smell) were stated from memory in the research and are **unverified**. Verify them before relying on them for any further lens decision.

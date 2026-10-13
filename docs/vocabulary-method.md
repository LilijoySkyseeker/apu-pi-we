# Vocabulary method (roadmap B1, step 2): draft

The decision procedure for choosing concepts and drawing their boundaries. Built on the plan (`vocabulary-plan.md`) and four research notes: `concept-sources.md`, `colexification.md`, `efficient-semantics.md`, `early-vocabulary.md`. Seed size and the lump/split rule were agreed by the author on 2026-10-08. Colour awaits the colour-vision check. The seed decisions are recorded in `data/concepts.tsv` (built by `tools/seed.py` and `seed_batch2.py`, removed 2026-10-09 as single-use; in git history).

## 0. The word-decision ladders (author, 2026-10-12)

Every word decision is two decisions: where a meaning's boundaries go, and what form its word takes. Go down each ladder; the first rung that applies decides. Derived from `docs/goal.md`: hard limits hold first; C4 overrides agreement; the aim (B1) outranks the method (B5), which is evidence of what works and the default for everything else. Sections 1–5 below are how rung 4 and the form rungs are carried out.

**Ladder 1: where a meaning begins and ends**
1. **An international standard (L3):** use its boundaries, as currently defined by the field. A standard's name may carry an old belief in its origin (*oxygen* "acid-maker", *malaria* "bad air"); that doesn't count, because a borrowed name is a label, not a claim. Trigger to revisit: a standard known to be wrong and not revised by its field.
2. **A known-wrong belief (C4):** agreement among languages doesn't count; describe what is observed, without building today's theories into basic words.
3. **Lumping costs meaning in modern use (B1, B3):** split when the two meanings are frequent, come up in the same contexts, and either confusing them changes what people do (left/right, buy/sell) or context often fails to tell them apart. Science matters here only by telling what things actually are; a scientific distinction alone is not a reason to split. Measured on modern everyday text and speech (author, 2026-10-13), because the lumping data records older ways of life (months counted by the moon) and a lump survives whether or not it still works, since languages rarely split a word. Three signals: how often each meaning comes up; how often context fails to separate them; and whether languages that lump the two have started separating them in modern use (Mandarin keeps 月 for both but says 月亮 "moon" and 个月 "month"). Safeguards, so modern data doesn't hand the language to the most-written languages (N3):
   - Evidence that a lump costs meaning comes from languages that have the lump. A language that never lumped two meanings can't show what lumping them costs.
   - Modern data can only add a distinction. It never merges meanings the world's lineages keep apart, and never drops a concept they converge on.
   - Each language counts once: frequency is measured per language across the panel's regions, never pooled by corpus size or speakers. Where a language has too little modern data, the measurement says so and rung 4 stands.
4. **Otherwise, the world's languages (B5):** family-balanced lump rate ≥50% one word; 20–50% two, one built from the other; <20% two roots (section 3).
5. **A word of its own** only when saying it as a phrase would be a real cost (C1): frequent in modern text or basic experience.

**Ladder 2: what form the word takes**
1. **An international standard form (L3):** adapted to the sounds.
2. **A form the world shares (L4):** a loan only if it passes the panel test, adapted from the panel's median pronunciation, not from English. A language counts when the loan is what its speakers say every day, even beside a formal native word (spoken *doctor* in Tamil, *terebi* in Japanese), with a source for the column; occasional code-switching doesn't count (author, 2026-10-13).
3. **Built from existing words,** when the concept isn't frequent enough for a word of its own (ladder 1, rung 5) and the result is clear (section 5). A frequent concept gets its own root even if it's new to history: trains and hospitals are baseline concepts for a language made now. Anyone who doesn't know a word can still build a phrase for it.
4. **A new root** from `tools/words.py`: hard to mishear, drift-safe, length by frequency; sounding like an offensive word elsewhere only breaks ties (C3).

The existing lexicon gets one review pass against these ladders (pending; word/language and "religion" are known candidates; moon/month split 2026-10-13).

## 1. Which concepts, in what order

1. **Core pool: CLICS4 concepts ranked by area-balanced lineage coverage.** CLICS4 has 3,432 varieties in 247 families. Coverage is the share of each macro-area's families whose word lists name the concept, averaged over the six areas. Raw family counts would let New Guinea and the Americas dominate; area averaging corrects that.
2. **Only the top ~300 are data-backed.** Beyond about rank 300 the counts reflect which questionnaires reached which regions, not which concepts languages name, and many of the questionnaires (IDS, and through it WOLD and part of CLICS) descend from Buck's 1949 Indo-European dictionary. *(Corrected 2026-10-12 after the fact-check, C52: was "the questionnaires descend from Buck"; CLICS draws on many datasets, and Swadesh-type lists don't descend from Buck.)* **Agreed (author, 2026-10-08):** the seed is therefore ~300 data-backed concepts plus the NSM primes not already covered, instead of the planned 500–800. Everything after that is added on demand from blind tests on texts from varied cultures and genres. Bring back the larger seed if the first tests lose more than 1 point to missing everyday words.
3. **NSM primes** (Goddard's 63–65) are a checklist for function and logic concepts the lists omit (WANT, BECAUSE, IF, MAYBE), not a frequency source. Their universality is contested.
4. **Children's early vocabulary** (Wordbank) is a second signal at the level of categories. It breaks ties near the top and admits social routines and interjections (hi, bye, no) that basic lists leave out. Onomatopoeia and baby words are left out. Add them back if tests lose points to missing interjections.

**The deep-layer criterion is convergence of independent signals** (agreed with the author, 2026-10-08). Three signals are used: breadth across lineages, what children learn first, and survival over long time spans. Each has its own bias: fieldwork questionnaires, a Western-skewed child sample, and Eurasian-heavy reconstructions. Where they agree, the biases largely cancel. Lineage breadth already integrates deep time, since every family descends from an ancestor thousands of years old. Time-stability, meaning the survival of *word forms* (Holman 2008, Pagel et al. 2007/2013), is used as a corroboration check, not a separate ranking. It mostly tracks frequency of use, says nothing about the world layer, and also preserves words that are stable but no longer central (louse, bark, ashes). Check run 2026-10-08: the seed already covered all of Holman's 40 most stable concepts and all but one of Pagel's 23 "ultraconserved" words (worm); the Leipzig–Jakarta list added grind. Both were added.

Dropped sources, each with a trigger to bring it back:
- Concepticon list counts: circular, since they reflect linguists' choices. Back if CLICS4 lacks a needed concept.
- NoRaRe and Dellert's measure: not lineage-balanced. Back if ties can't be broken.
- Lexibank: CLICS4 is its balanced subset. Back if a concept is missing.

## 2. What form each concept takes

For each concept, in order:
1. If the grammar or existing words already say it without loss, add **no** root.
2. If it's a doer, thing done or made, tool or place of an existing verb, it's a **built word** (`no`, `ge`, `du`, `pu`).
3. If it's frequent in modern everyday use, or in the deep layer (section 1), it's a **root** (author, 2026-10-13: how other languages happen to build it no longer counts against a root; they compounded modern things because those arrived after their words had formed).
4. Otherwise it's a **compound with a stated relation** (`se`, `pi`, `li`, …).
5. **Loans** only where the world shares a form (language.md section 11); names and brands keep their own spelling.

## 3. Where boundaries go (lump or split)

Applied in this order (`research/notes/colexification.md`; lineage rates from `tools/clics_rates.awk`):

1. **A published efficiency model exists** (colour, kinship, numerals): the model plus human need decide, per the agreed target.
   - **Colour (decided, verified 2026-10-08, `research/notes/colour-vision.md`):** six basic roots (black, white, red, yellow, green, blue). The support is from colour *naming*, not eye physiology. The best-example colours in 110 unwritten languages cluster near these six, and most systems with more than five basic terms separate blue and green (not all: brown or purple can come first). The "opponent channels" argument doesn't hold: the elementary hues don't line up with the eye's channels (Webster et al. 2000). Lumping green and blue (57% in WALS, a sample of mostly small societies) is a coarser cut of the same perceptual space, driven by low need (few natural objects are told apart by blue; Gibson et al. 2017, paraphrased: the quote once given here wasn't found in the paper), not a perceptual error. So separate blue rests on need plus naming data. Other colours are compounds (grey = white + dark). Stopping at six is a deliberate root-budget choice; industrial languages have up to 11 basic terms, some 12 (Berlin & Kay). Add roots if tests show colour meaning lost. *(Corrected 2026-10-12 after the fact-check, C38: "every system" → "most", quote replaced by a paraphrase, term count checked.)*
   - **Kinship:** roots mother, father, child, sibling (no sex), spouse. Cheap optional modifiers for older/younger and male/female; everything else composed ("mother's sibling"). Kinship systems vary too much to copy: 410 systems among 487 languages (Kemp & Regier 2012; "too much to copy" is our inference, the paper finds the variety clusters near an efficient trade-off).
   - **Numerals:** base 10 (language.md section 9).
2. **Frequent alternatives in the same slot, where confusing them changes what the listener does → two roots.** This is the "action-relevant misunderstanding" test made concrete: left/right, buy/sell, lend/borrow, give/take. It agrees with the Goldilocks finding that languages avoid lumping meanings that compete in context.
3. **Otherwise, the family-balanced lump rate** (agreed by the author, 2026-10-08):
   - lumped by ≥ 50% → one root; the narrow sense is built when needed;
   - 20–50% → two words, the less basic built transparently from the other;
   - < 20% → two unrelated roots (e.g. see/know 3%, eat/drink 7%, finger/toe 16%; recomputed 2026-10-12 from CLICS4 v1.0 with `clics_rates.awk`: 2.9%, 7.2%, 15.7%, all clear of the 20% line; moon/month 69.6% robust; word/language 50.2% reproduces but is undecided by the rule, see `research/notes/colexification.md`).

   The 50% and 20% cut points were proposed by the research agent and are arbitrary. Refine them only if tests show losses near a threshold. Where CLICS4 copies a broad meaning onto narrower ones (uncle, he/she, we), its rate is an upper bound; cross-check with WALS or Kinbank.
4. **A shared English word is not evidence for a lump** (2026-10-10). Two concepts that English happens to call the same thing (fly the insect / fly the verb, light / light) go through steps 1–3 like any other pair. The seed matched concepts to roots by English gloss and skipped this; glosses now carry a second gloss wherever the English is ambiguous.
5. **Never derive one meaning from another along a link only one family uses.** For example, don't build "know" from "see", which is an Indo-European habit.

Every decision gets an evidence line in the concept table.

## 3b. Observation, not theory (agreed with the author, 2026-10-08)

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

## 5. How a new word is made

Moved here from the reference (2026-10-10), which now states only what words are.

1. **Say it with words you have.** A verb idea takes a derivation marker (**no**, **ge**, **du**, **pu**) and can bring its own relation phrases (**no isi se guyi** traveller). A noun idea links with **pi**, a verb or a relative clause. Most new concepts end here.
2. **A new root only when it's earned:** a basic concept that independent lineages converge on, a modern concept frequent enough that the phrase is a real cost, or a phrase that fails a blind test. Lump or split by section 3.
3. **The tools choose the sound:** `tools/words.py add-content GLOSS FIELD TIER [--antonym GLOSS] [--avoid FORMS]` picks the form least likely to be misheard as a related word, checks drift and juncture, skips offensive and hand-rejected forms, and pushes opposites apart. Forms are never hand-picked. Then run `tools/juncture.py`. A word that sits in a fixed frame (**dili mena ka**) is kept from echoing its neighbours where they touch: it may not start with the first or last syllable of a word it follows, or end in the first syllable of a word that follows it (`--after`, `--before`). Fixed pairs that echo are misheard as one word repeated or swallowed (haplology).
4. **Phrases aren't promoted or fused by design** (author, 2026-10-13). The base is seeded as fully as the coverage measurement says, then left to its speakers. Speakers will shorten frequent phrases the way people do: by dropping a word context carries, or by keeping first syllables, never by adopting an unrelated form (`drift.md` 9). Compounds stay separate words in speech and writing, as in Indonesian *rumah sakit* and Tok Pisin *haus sik*; the only one-word form is the language's name in other languages.
5. **Names keep their owner's spelling; loans are adapted** with `tools/names.py` (broad IPA in), and only where the world shares a form.
6. **No word may sound like a common offensive word** in the world's most spoken languages (`tools/offensive.py`, Wiktionary data, 34 languages, plus the `REJECTED` list).
7. **One-syllable grammar forms** go by measured frequency: a meaning earns one only by beating the rarest current holder (`grammar-rebuild-spec.md`).

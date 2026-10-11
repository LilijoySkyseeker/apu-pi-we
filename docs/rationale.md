# Why and how: the design rationale

Written 2026-10-10 so a later session (or person) can understand why each part of Apu Pi We is the way it is, rebuild it, and change it safely.

**How this differs from the other docs.** [language.md](language.md) says *what* the language is now. [design-log.md](design-log.md) records decisions in the order they happened, including dead ends. This file is organised by topic and gives, for each part of the design: the decision, **why** (with its source: the user, evidence, or Claude), **how** it was made (method, tool, parameters), and **how to change it** (which file, what else moves, the trigger that should make you change it). Where this file and language.md disagree, language.md wins and this file is out of date.

Source labels used below: **[user]** a ruling by the user; **[evidence]** research in `research/`; **[Claude]** Claude's own proposal, accepted by the user. Claude-sourced parts are the ones most worth questioning (the user's rule: Claude's own requirements are the most dangerous, because they sound reasoned).

---

## 1. Foundations

### 1.1 What the project is

| Part | Source | Why |
|---|---|---|
| A universal human language for modern Earth, designed from first principles, as a thought experiment | [user] 2026-10-08 | The user's goal. A fantasy/D&D use was dropped: designing for fantasy and for modern Earth are different tasks. A signed surface was dropped: text is the wrong medium to design signs. |
| Imagined as a **native** language that children grow up speaking, not an auxiliary language for adults | [Claude, adopted] | Removes every adoption question (which killed every real auxlang; see the conlang report) and leaves only human constraints: mouth, ear, memory, attention, child acquisition. Consequence: "easy for adult X-speakers" is not a criterion; what learners and native speakers *do* to a design is. |
| **North star:** faithful transmission of thought, *at a cost speakers will actually pay* | [Claude] first half; [evidence] second half (research round 1) | Decides conflicts. The cost clause was added because native speakers wear down any feature that doesn't do everyday work. |
| **The yardstick:** Reach, Economy, Clarity, Restraint, Gate | [user] 2026-10-10, built blind in `~/research/Language/language-first-principles-2026-10.md` | Makes "best" checkable. Its layer 5 adds what the north star lacked: *let context take over whenever it's available*. Restraint: *design only what speakers can't easily fix themselves*. Gate: an adult can learn it well enough to raise a native speaker. Since 2026-10-10 recent changes (omission, topic-based pronouns, usage bans removed) come from applying it. |
| Premise 2: legacy conventions are void, base included | [user] 2026-10-08; **amended** 2026-10-09 | Amendment [user]: "in reality, base 10 will functionally remain the default". The language is base 10 with today's calendar and units; senary is a topic it can talk about (§7). |
| Owned by Claude, the user along for the ride and learning | [user] | Claude drives and explains. The user's pushback is real review, not a request for reassurance. |

### 1.2 How decisions get made

These are the working methods; reuse them to keep changes consistent.

- **The user's five steps, in order** (from the user's global instructions): question the requirement and name its source → propose deletions, each with an add-back trigger → simplify what survives → speed up the feedback cycle → automate last. Every "add back if…" line in the docs is step 2's trigger.
- **Doghouse vs dog owner** [user]: trace each part up to what the user actually cares about; parts that only serve other parts go. Deleted on this basis: signs, D&D, B6 "art and play" (art grows from use), adoption work.
- **Insides for natives, boundary for every culture** [user, 2026-10-10]: native speakers still live in existing cultures (12-hour clocks in America, Sunday-first weeks, local names). So the language's insides (sounds, grammar, word-building) are optimised for native speakers, while where it meets culture (clocks, calendars, units, names, customs) it carries any culture's conventions and imposes none. English is the model: it carries both "9 pm" and "twenty-one hundred".
- **Tie-breaker at the boundary** [user, 2026-10-10]: carry every culture's convention where they can coexist (12-hour and 24-hour clocks); where they conflict and the language must pick one, follow the international technical standard (weekdays: ISO 8601, Monday = 1). "In cases of ambiguity, lean towards the more technically correct option."
- **Convergent function, free form** [user, 2026-10-10]: where unrelated languages independently converge on a *function*, the language needs it; where they split on the *form*, choose the cheapest form for native speakers. Count by lineages, not speakers. Example: respect is universal, graded pronouns are not (WALS 45), so the language gives respect a home (titles, **nun**) but no pronoun grades.
- **Evidence before design.** Each design area began with a research round (notes in `research/notes/`, labelled sourced / secondary / unverified). Tag claims honestly; several early "facts" were recalled and later corrected.
- **Blind tests over argument.** A change that matters is tested by a fresh AI agent that hasn't seen the reasoning: it translates or back-translates, and a separate judge scores against rules fixed in advance (`tests/*/method.md` or the analysis files). Run `tools/check.py` on any text first: hand translations repeatedly used stale words.
- **One problem at a time, with the user choosing between options.** For each finding: options with trade-offs, Claude's recommendation, the user's choice, the rejected options and an add-back trigger logged.
- **Words are stable; the core is frozen** (2026-10-09) [Claude, agreed]: an existing word or rule changes only when real use or a test shows a problem. Why: the user is learning the language, and the conlang record shows churn loses learners (Ido) while a frozen core survives (Esperanto). Known accepted flaws: **lon** "I" (a Vietnamese vulgarity) and two-syllable digits 6–9.

---

## 2. Sounds

| Decision | Why | How it was made | To change it |
|---|---|---|---|
| Vowels **a e i o u** | [evidence] the most common and most dispersed 5-vowel system (vowel dispersion, Liljencrants & Lindblom 1972) | — | Any vowel change rebuilds all words (`build.py build`), breaking the freeze. |
| 13 consonants **p b t d k g m n f s l w y**; only three places (lips, tongue tip, back) | [evidence] Miller & Nicely 1955: place of articulation is the cue noise destroys first; voicing and nasality survive to −12 dB | Inventory compared at a 3,000-root scale (`build.py scale`): the inventory must leave room for that many distinct two-syllable words | `build.py` `FULL`. |
| **/v/ and /z/ deleted** | [evidence] rare worldwide (PHOIBLE: 27% and 30%), /v/ confusable with /b/ and drifting toward /w/, /s/–/z/ merging; founders' sounds win (Hebrew) so rare sounds are at risk | `build.py scale`: removing /z/ cost almost nothing at 3,000 roots | Re-add in `FULL`; rebuild. |
| Syllables **(C)V(n)**; vowel-only syllables only word-initially; **n** the only coda | [evidence] CV is universal and robust; one coda keeps words short without clusters | — | `Inventory` in `build.py`. |
| No tones | [Claude] | Leaves pitch for intonation and emotion; tones are hard for adult learners (Gate) | — |
| **Stress on the first syllable** of every content word; grammar words unstressed; stress is **higher pitch, not length** | [evidence] fixed initial stress marks word beginnings (Finnish, Hungarian); listeners hear lengthening as word *ends*. The user asked to weigh drift; the drift risk of initial stress (later syllables eroding) is handled by drift-proofing (§3.3) | Challenged by the user ("should stress be fixed?"), kept after research (`research/notes/stress-and-sound-change.md`) | — |
| **Declination**: stressed peaks step down across a phrase, reset at a comma or full stop | [user's reading test] runs of two-syllable words made the voice "bounce" | Specified from how nearly all languages already behave | — |
| Harmless variants declared in advance (k/g → ch/j before i/e, nasal vowels, soft middle consonants) | [evidence] Gurevich 2004: 92% of 230 lenitions merged nothing | The vocabulary is built so these never merge two words (§3.3) | — |

---

## 3. How word forms are chosen

This is the language's most distinctive machinery. Root **sounds are arbitrary on purpose**; logic lives in how words combine (§5).

### 3.1 Why arbitrary roots
[evidence + Claude] Languages whose sounds encode meaning (Wilkins 1668: *Tida* redness / *Tide* greenness; Ro; Solresol's mirror-image opposites) turn one misheard sound into a plausible neighbouring meaning that context can't catch, and their categories go stale. Learning studies (Monaghan, Christiansen et al.) find arbitrary forms help learning individual words. So similar and opposite meanings get forms that sound **as different as possible**.

### 3.2 The mishearing model (`tools/confusion.py`)
- **Consonants:** Miller & Nicely 1955, Table III (−6 dB S/N), renormalised over our consonants. Real data, but English listeners.
- **Assumptions (marked `ASSUMPTION` in the code):** l/w/y confusions by place; missing vs weak onset; a vowel matrix where neighbours confuse most; `CODA_MISS = 0.08` (final n lost or added).
- A syllable's confusion = consonant × vowel × coda; a word's = the product over syllables.
- **Unvalidated** against real listeners. Listening test 01 tried; synthesisers couldn't produce reliable audio and the user stopped testing (2026-10-10). Treat model scores as relative, not absolute.

### 3.3 Drift-proofing (`docs/drift.md`, `build.py`)
[user asked to weigh drift heavily; evidence] A native language changes; the fast-changing layer is the one-syllable grammar words, which carry most of the precision machinery.
- **Content words** must stay distinct after predicted changes: later-syllable e/i and o/u merge, middle p/t/k voice, final -n is lost, s/z merge. Implemented as `Inventory.content_key`: two words with the same key can't coexist.
- **Grammar words** that can fill the same slot start with **different consonants** (`GROUPS_STRICT` in `build.py`), so vowel reduction can't merge them; words in the same wider position stay distinct after drift (`GROUPS_WIDE`, `grammar_key`).
- **No two grammar words differ only by a final -n** (it's the first thing to go).

### 3.4 Juncture (`tools/juncture.py`)
[Claude, idea from senary] Written tests can't hear word boundaries. Rules: no content word begins with a one-syllable digit's syllable (so "digit + grammar word" can't sound like a content word); no -n pairs; no grammar word ending in -n before a vowel-initial word that would be heard as another word. Run after any addition.

### 3.5 The optimiser (`tools/words.py add-content`)
For a new root it tries every two-syllable form not taken (after drift keys) and minimises:
- confusion with every existing two-syllable word, **weighted by meaning**: ×30 antonyms (`--antonym`, recorded in `data/antonyms.tsv`), ×10 number words, ×3 same semantic field, ×1 other;
- weighted by frequency (`TIER_FREQ` tiers 1–5) in both directions;
- plus a length penalty (`EFFORT = 0.02`) so frequent words stay short.

It excludes digit-initial syllables and **offensive matches** (§3.6). **Forms are never hand-picked.** `add-grammar` does the same for one-syllable words but doesn't enforce the same-slot rule; only `build.py build` does (and a full rebuild breaks the freeze).

### 3.6 Offensive-word filter (`tools/offensive.py`, `data/offensive.tsv`)
[user] 2026-10-09: no word should sound like an offensive word, or clash in a taboo topic, in major languages.
- **Data:** Wiktionary via kaikki.org extracts for 34 of the most spoken languages: entries tagged vulgar/offensive/slur/derogatory, plus taboo meanings (sex, genitals, excrement, urine, death) read from glosses. 32,910 pronunciations, each mapped into our sounds with the names.py mapping.
- **Matching:** exact; near (voicing and e/i, o/u merged); prefix. **Ranking:** only words whose *first* sense is offensive and that are common (wordfreq Zipf ≥ 2.5) block a form. Run tools with `ps.wordfreq`, or every listed word counts as common.
- **Review is by hand.** Most raw hits are noise; one-syllable grammar words match *something* in 34 languages almost always. Six words moved (lanu→lenu, nega→lasu, pisan→tisan, webo→yawu, ku→nun, ano→ago); lon/pi/go kept because no free one-syllable form exists.
- Refresh with `python offensive.py fetch` (a few minutes, ~1 GB streamed); review with `check`.

---

## 4. Grammar

### 4.1 Six principles (language.md)
| Principle | Source | Why |
|---|---|---|
| 1. The common case costs nothing | [evidence] Zipf's law of abbreviation; research round 1 | Statements, ordinary belief, unknown source, the topic and unspecified time are unmarked; only departures cost a word. |
| 2. Heads first; position carries role (SVO, modifiers after) | [Claude + evidence] | A listener who loses a word still knows who did what; fixed order is among the most stable features (Dediu & Cysouw 2013). Native Esperanto, Hebrew and creoles all moved to SVO without inflection. Since omission (rule 11), the guarantee holds only for what is said. |
| 3. Operators cover what follows | [Claude] | One scope rule for NOT, confidence, source, ONLY, degree. |
| 4. Heavy goes last | [evidence] processing (end weight) | Relative clauses have no end marker, so nothing may follow them in their phrase. |
| 5. Doubling widens or strengthens | [Claude] | A built-in renewal path: when a word wears down, its double takes over (**mu mu**, **nun nun**) inside the system. |
| 6. Every social pressure gets its own outlet | [evidence] drift items 1–2 | Emphasis (**ba**, **bi**) and politeness (**nun**) have their own words so they don't wear down the precision words. Since the Restraint review this is a design plus a *prediction*, not a usage ban. |

### 4.2 The grammar-word layer
- **One syllable, unstressed, 64 words; the space is full** (with 13 consonants, 5 vowels, ±n, minus digits, same-slot and -n rules). New grammar words must be two syllables. This is why digits 6–9 are two syllables.
- **Why particles, not inflection:** [evidence] native speakers of designed languages drop redundant mandatory morphology (Bergen 2001); isolating languages are where all successful auxlangs and creoles converged. Fusion of particles later is harmless because same-slot words differ by consonant.

### 4.3 Speech acts, confidence, source
- **Speech-act particle first** (**min so tin fon de yo a ba**) [evidence, research round 1]: urgency and act carried by melody alone fail in noise and across cultures; aviation and medical reports show hints where warnings were needed. Initial position tells the listener the sentence's shape early (like Spanish ¿).
- **Confidence as a number** (**kon** + 0–6, sixths) [evidence + user]: number-anchored probability was the strongest finding against miscommunication of stance (words like "likely" span huge ranges). Sixths match the ~7 bands forecasters can use (Friedman et al. 2018). The user switched to tenths on 2026-10-09 for familiarity and back to sixths on 2026-10-10: they fit the research, almost every value is one syllable, and exact percentages remain sayable with **pasentu**. Optional. Watch list: collapsing to favourite values.
- **Source (evidentiality) optional** (**o fen san**) [evidence]: the case for obligatory evidentials was mixed to negative; Láadan made them obligatory and failed. Every marked dimension has an "unspecified" value (**bo**) so nothing forces false precision.
- **No yes/no; echo answers** [evidence]: answers to negative questions are a documented failure ("yes" means opposite things across languages). Acknowledgement ladder from aviation: **mm** heard, echo understood, **de** will do.

### 4.4 Reference
- **wan / yi follow the topic** (2026-10-10) [user, from economy test 01]: **wan** = the person being talked about, **yi** = another, non-topic one, as Algonquian obviation does natively. Replaced a mechanical "most recent subject" rule [Claude, 2026-10-08] that made casual speakers keep score. The old rule rested on Hudson Kam & Newport (learners regularise *random* variation); topic-based reference isn't random.
- **bu** = the thing talked about; **ben** alone = "that one" (non-topic), **tan/ben** alone = an event or statement (as demonstratives do in nearly every language, Diessel 1999).
- **pen / din** inclusive/exclusive "we" [evidence]: among the most stable distinctions (Greenhill et al. 2017) and English's "we" is a real ambiguity. **sun** logophor for reported speech. **nen** self.
- Add-back trigger for a mechanical rule: a blind test shows listeners losing track where one would have caught it.

### 4.5 Omission (rule 11)
[user, yardstick layer 5] Anything context supplies may be left out, including verbs; fragments are grammatical (as in Mandarin, Japanese, Korean). Economy test 01: the language was ~1.5× English's syllables; the four fixes (tan/ben alone, bu topic, wan/yi topic, omission) cut 12% with meaning 44/44 on retest.

### 4.6 Smaller rules worth knowing the reason for
- **Tense optional, aspect particles** (**sin le win**) [evidence]: native speakers and creoles keep preverbal aspect, drop compound tenses.
- **Three modalities kept apart** (ability **lenu**, obligation **keya/wupi**, permission **efon**); epistemic "must/might" is confidence [evidence]: English *must/may* each mean two things.
- **Conditions use confidence** (**don kon po** = counterfactual) [Claude]: no new grammar words needed.
- **Clause attachment** (rule 15) [blind test on contract language, `backtranslation-04-nesting`]: position decides attachment; commas mark pauses where a phrase could run on. No clause-closing word; add a two-syllable one if attachment fails in a test.
- **Comparison "more X from Y"** (**ke … se**) [Claude]: reuses existing words.
- **Time: anchor + offset, offset names its unit** [evidence]: relative-time metaphors ("move the meeting forward") are a documented ambiguity.

### 4.7 Politeness (`research/notes/politeness.md`)
[evidence] Politeness creeps into hedges and questions and erodes them; polite pronouns cycle every 150–300 years. So: one particle **nun** with no truth meaning, repeatable; no polite pronouns or speech levels (address words can be replaced, pronouns can't); **yo yo** emergency suspends it. The crew-resource pattern "problem, act, what we need" is the model. Routines optional.

---

## 5. Words and vocabulary

### 5.1 Word building (`tests/wordbuilding-ab-01`)
Four markers **no** (doer), **ge** (thing done/made), **du** (tool), **pu** (place) [evidence: the most widespread derivations; analytic languages all grow such heads from nouns]. Blind A/B: markers 71/76 vs generic heads 69/76; kept because shorter, and generic heads erode into markers anyway. Patient person = **ewo gun** + verb (**ge** was read as a thing). Noun bases link with **pi** or a verb, never a bare relation phrase (rule 8 would attach it to the verb). Bare noun+noun leaves the relation to guesswork (Štekauer; the blind test), so only for gender and listed compounds.

### 5.2 How a new word is made (language.md)
Say it with words you have → a new root only when earned (convergent basic concept, frequent modern concept, or a phrase failing a blind test) → the tools choose the sound → frequent phrases may be clipped later → names and technical words are adapted, not coined → offensive filter.

### 5.3 Which concepts get roots (`docs/vocabulary-method.md`, `vocabulary-plan.md`)
Two layers [user + Claude, 2026-10-08]:
- **Deep layer (base human experience):** convergence of independent signals: area-balanced lineage coverage in CLICS4 (`tools/concepts.py`; New Guinea and the Americas would dominate raw counts), children's early vocabulary (Wordbank), time-stability as a check (Holman 2008, Pagel 2007). The user rejected weighting by speaker numbers: weight by *lineage*. Only the top ~300 CLICS concepts are data-backed; the seed stopped there plus NSM primes.
- **World layer (modern need):** measured by blind tests on modern urban texts; built words by default. Prompted by the user noticing the lists' bias toward low-technology life.
- **Stop condition:** two tests in a row losing <1 point to missing words (met at test 05, 445 roots).

### 5.4 Where boundaries go: lump or split
In order: (1) a formal efficiency model where one exists (colour, kinship); (2) action-relevant same-slot alternatives get two roots (left/right, buy/sell); (3) **family-balanced lump rate** from CLICS4 (`tools/clics_rates.awk`): ≥50% one root, 20–50% one built from the other, <20% two roots; (4) a shared English word is not evidence; (5) never derive along a link only one family uses. The 50/20 cut points are arbitrary [Claude's research agent]; refine only on test evidence. Example: **apu** = word *and* language (50.2%); **dunan** = moon and month (69.6%).
- **Colour:** six roots (black, white, red, yellow, green, blue) from colour-naming data, not eye physiology; blue/green split rests on modern need. **Kinship:** mother, father, child, sibling, spouse; the rest composed (410 systems among 487 languages, too varied to copy).
- **Observation, not theory** [user's question, 2026-10-08]: basic words name what's experienced ("the sun appears", illness by symptoms); theory-laden concepts are composed so they can be rebuilt.
- **English leaks fixed** (2026-10-10): concepts had been matched to roots by English gloss, merging fly (insect)/fly (move) and three senses of "light", and **muyi** counted occasions. Now: **gekon** the insect fly, **gimu** occasion, pale = **mu buda** ("light, not heavy" was already **gamun**). Ambiguous glosses carry a second gloss (Kit advice), and the lump/split rule says a shared English word is not evidence (vocabulary-method §3.4).

### 5.5 Names, loans, borrowing (`tools/names.py`, `tests/names-01`)
- Names take the article **en** [evidence: Tagalog *si*, Māori *a*] so a name that sounds like a word can't be misread.
- Adaptation: nearest native sound, glide between vowels, an added **u** for a stranded consonant (never drop one), ≥2 syllables. Blind test: 43/44 world names recovered; the fixed vowel beat copying a neighbour because it marks itself as added.
- **Technical and international words are borrowed in their international form** [user, 2026-10-09; reworded 2026-10-10 by the coexistence tie-breaker]: "the most practical version is just using the existing words". In practice that is usually English, or Latin/Greek for sciences and SI units. Borrowing replaces describing, not native roots. Cost recorded: favours English speakers in sound, not meaning.

---

## 6. Writing (`research/notes`, human test 01)
- **Latin transliteration** [user]: costs nothing to type; computing runs on it. A native script is deferred.
- **All lowercase** [user's reading check]: l/I/1 collide in mobile fonts; **en** already marks names.
- **Stress unwritten** (predictable). Teaching capitals were dropped.
- **Three punctuation marks** (`,` `.` `" "`) [user + Claude doghouse review]: writing marks only what speech marks with the voice. ? ! were dropped because the opening particle says it earlier; the user's reading test showed end marks steer the voice too late. Triggers to bring each back are in language.md.
- **Words written apart until the sound changes** [user's fusion question].

---

## 7. Numbers, time, measurement

- **Base 10** [user, 2026-10-09]. History: base 6 was chosen first [Claude + evidence, `docs/number-base.md`]: a transmission test showed six one-syllable digits can be made far less confusable than ten (0.26% vs 2.3% wrong-digit rate for a 10-digit ID). The user ruled reality stays base 10; the 0–5 digits kept their optimised forms.
- **Digits 6–9 two syllables** (**ufo oma kefi mape**): no free robust one-syllable forms (only **fe**, **nu**; closed syllables collided with **fi**). Built as content words pushed apart from each other and from number words.
- **No teens or irregular tens** (15 **yawu te**, 50 **te yawu**) [evidence]: English *fifteen/fifty* is a classic confusion; regular numerals help children.
- **Digit reading** for identifiers in groups of three [evidence: aviation reads digits one by one].
- **Calendar:** today's (7-day **nelon**, **dunan** month = moon, 24-hour clock read as digits); months and weekdays by number [user]. Points in time are labels (**pi** + number).
- **Senary** is a topic [user]: its words live in `docs/measurement.md`, `data/units.tsv` and the senary rows of `numbers.tsv`; **senali** marks a senary number. Senary (`~/work/repos/senary`) owns quantities; this repo owns all words, and senary uses them verbatim (r22–r23). Keep senary usable: it may be used for worldbuilding.

---

## 8. The name

**apu pi we** "everyone's language" [Claude proposed, user approved]: any language is **apu pi** + whose it is, and this one belongs to no people or place. Required **apu** to cover "language" (CLICS4: 50.2% of families lump word/language). Rejected: **apu pi ewo** (reads as "human language" in general), an invented name (wouldn't follow the grammar).

---

## 9. Rebuilding or tweaking it

### 9.1 Environment
Python with numpy, on NixOS through nix-shell, run from `tools/`:

    nix-shell -p 'python3.withPackages(ps: [ps.numpy ps.wordfreq])' --run 'python3 words.py add-content GLOSS FIELD TIER [--antonym GLOSS]'

wordfreq is needed for the offensive filter's frequency ranking. `clics_rates.awk` needs the CLICS4 CLDF tables (download from Zenodo/clld; not kept in the repo).

### 9.2 What is generated vs hand-made
| Artefact | Made by | Rebuildable? |
|---|---|---|
| `grammar.tsv`, `lexicon.tsv` forms | `build.py build` (once, 2026-10-08), then `words.py` additions and logged moves | Yes, but a rebuild **re-assigns every form**; never do it on the frozen core. To reproduce today's forms, replay the additions in `design-log.md` order. |
| Concept list and tiers | `concepts.py` ranking + judgement (tiers are English intuition) | Partly; `data/concepts.tsv` has the evidence line per concept |
| `numbers.tsv` | digits 0–5 from the base-6 optimiser (`build.py numbers3`); 6–9 and place words via `words.py` | Yes |
| `offensive.tsv` | `offensive.py fetch` | Yes (Wiktionary changes over time) |
| Rules, principles | by hand, in language.md | — |
| Tests | fresh blind agents; prompts and scoring rules in each `tests/*/` folder | Re-run with new agents; never reuse a reader who has seen the docs |

### 9.3 Common changes and what they touch
- **Add a word:** `words.py add-content` (with `--antonym` for opposites and close alternatives) → `juncture.py` → `check.py` on any text using it → log it.
- **Move a word** (only with evidence): re-coin with the old form excluded (see the move script pattern in design-log "Offensive-word moves"), then update docs, `compounds.tsv`, and senary if it's a unit (senary's symbols are the first two letters).
- **Change a grammar rule:** edit language.md and learn.md, run a blind test that exercises it, log the rejected options and an add-back trigger.
- **Tune the model:** the assumptions in `confusion.py` and the weights in `words.py`/`build.py` change *future* words only; existing words don't move.
- **Change sounds or syllable shape:** requires a full rebuild; treat as a new language version.

### 9.4 Tests that exist
Back-translation 01–04 (fidelity, politeness, nesting), grammar coverage, word-building A/B, names, vocabulary 01–05, economy 01 (context), human reading 01 (the user aloud). Listening 01 was built but stopped: no available synthesiser (Piper, Kokoro, MBROLA in four voices) produced a reliable word-initial g before u, and the user stopped testing (2026-10-10). Its lesson for a rerun: use a human reader, or a cloud TTS that accepts IPA, with a carrier phrase.

---

## 10. Known weaknesses (what a successor should doubt first)

1. **Validated mostly by its own instruments:** the confusion model is scored against itself; blind readers are AI agents with world knowledge. One human has read it aloud; none has listened.
2. **English-centred:** listener data, test texts, readers, English glosses (ambiguous ones pinned with a second gloss since 2026-10-10), technical loans. "Universal" is a goal, not a result.
3. **The full one-syllable space:** every future grammar word costs two syllables.
4. **The watch list** (language.md, Open questions): confidence collapsing or used for emphasis, politeness taking over hedges, topic-based pronouns needing a mechanical fallback, aspect words unused.
5. **Frequency tiers and lump/split thresholds are judgement**, not data.

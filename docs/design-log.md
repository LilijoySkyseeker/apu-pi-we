# Design log

Started 2026-10-08. A thought experiment: design the best universal human language from first principles. Possible light use as D&D flavor; that use drives no decisions.

## Decisions so far

- **Framing:** a hypothetical *native* language (children grow up in it), not an auxiliary language for adults. Fixed constraints are human hardware only: mouth, ear, hands, eyes, working memory, child acquisition.
- **North star:** faithful transmission of thought. The listener reliably ends up with the thought the speaker meant, under real conditions (noise, inattention, interruption). Wins every conflict.
- **Working rule:** every feature traces to a human constraint or to the north star.
- **Done (assumed):** a working sketch (sounds, core grammar, enough words for sentences) that can keep growing.
- **Modalities:** one language, two surfaces. Design the underlying structure once; give it a spoken and a signed realization. Each surface does what its channel is good at (speech is sequential, sign is simultaneous).

## Directions in play (Claude's proposals, adopted by the user)

- Sound inventory chosen for perceptual distinctness (vowel dispersion theory).
- Grammar as deliberate error correction (agreement as checksum); adjustable redundancy.
- Shortest forms for the most frequent meanings (Zipf's law of abbreviation), by design.
- Evidentiality and confidence in the grammar. (Revised after research round 1: confidence core, evidentiality optional.)
- Spatial reference tracking (sign-language loci), possibly carried into speech as formal gesture.
- Maybe: a noisy-channel simulation to test confusability. Watch this for scope creep.

## Research touchstones

- Coupé et al. 2019, *Science Advances*: ~39 bits/s information rate across 17 languages. Speed is capped by the brain, not the mouth.
- Piantadosi, Tily & Gibson 2012, *Cognition*: ambiguity lets short words be reused when context disambiguates.
- Bellugi & Fischer 1972: a sign takes ~2× as long as a word, but propositions flow at a similar rate (sign is simultaneous).
- Liljencrants & Lindblom 1972: vowel dispersion.
- Prior art and what each optimized: Esperanto (learnability), Toki Pona (minimalism), Lojban (logical unambiguity), Ithkuil (density).
- Signing communities with hearing signers: Martha's Vineyard, Plains Indian Sign Language, Warlpiri sign; Nicaraguan Sign Language (children creating grammar).

## Research round 1: where communication fails (2026-10-08)

Full report: `research/where-communication-fails.md`.

Decisions taken from it:
- **North star amended:** faithful transmission *at a cost speakers will actually pay*. Native speakers wear down any feature that does too little everyday work, so every feature must pay its way in ordinary talk, not only in emergencies.
- **Don't fight ambiguity in general.** Target only the costly cases: context-free tokens (numbers, names), competing referents, speech act / urgency carried by melody alone, stance words without numbers, answers to negative questions, relative time metaphors, overloaded messages.
- **Confidence and source are separate.** Confidence gets number-anchored markers (strongest evidence of anything we found). Source of knowledge (evidentiality) becomes optional; the evidence for making it obligatory is mixed to negative. This revises Claude's own earlier pet idea.
- **Every marked dimension has an explicit "unspecified" value**, so the grammar never forces false precision.
- **Protocol vs grammar:** aviation/medical fixes (handoff templates, message-length caps) are procedures, not grammar. Keep the ones that work as everyday grammar (echo answers, received/understood/will-do, explicit speech-act particles); leave the rest out.
- **Sounds:** five vowels /i e a o u/; important contrasts carried by voicing, nasality, manner and vowels rather than place of articulation alone; numbers and names longer and confusion-tested.
- **Signs:** location and coarse movement carry the load; a small set of maximally distinct handshapes; fine handshape detail near the face.

## Open questions

- Will confirmation and speech-act markers survive being native grammar, or erode like everything else that's costly?
- How to test anything: confusion matrices for the lexicon (cheap, simulation-friendly) vs. meaning-gap tests with real people (expensive).

## Sound system v0 (2026-10-08)

- **Inventory size vs word length:** information rate is capped by the brain (~39 bits/s), so a big inventory buys nothing; pick a moderate set of very distinct sounds and accept slightly longer words.
- **Vowels:** /i e a o u/.
- **Consonants (15):** stops p b t d k g; nasals m n; fricatives f v s z; approximants l j(y) w. Only three places of articulation (lips, tongue tip, back), since place is the weakest cue in noise. Dropped: sh/s, ng/n, r/l, th/f, which are place-only or famously confusable pairs.
- **Syllables:** (C)V(n). Vowel-only syllables only word-initially. Only coda is -n.
- **Stress:** fixed on the first syllable, so word boundaries are audible.
- **No lexical tone:** pitch stays free for intonation and emotion; tone dies in whispering.
- **Keep "huh?"** as the open-repair word; natural languages already converged on it.
- **Lexicon rule (later):** no place-only minimal pairs among words that could appear in the same slot; whole-set confusion testing at the lexicon stage.
- Capacity check: 80 CV-type syllables, about 6 bits/syllable, in the natural range (Basque 4.8 to Vietnamese 8.0).

## Sign system v0

- **Locations:** few and far apart (face/head, chin/neck, chest, neutral space in front, non-dominant hand).
- **Handshapes:** the small "unmarked" set common to sign languages and learned earliest (Battison): flat B, fist A/S, index 1, spread 5, curved C, O. Fine distinctions only near the face.
- **Movement:** coarse (straight, arc, circle, repeated, contact).
- **Face:** carries grammar in parallel (speech act, confidence), as natural sign languages do.
- **Spoken and signed words:** share meanings and grammar, but each surface gets its own word forms; sign forms may be iconic. Not derived phoneme by phoneme from speech.

## Grammar core v0 (2026-10-08)

Erosion test: each feature is labeled with whether a natural language already has it. A natural precedent is evidence it survives being native.

- **Word shape tells category:** grammar words are one syllable, content words two or more. Analytic: every meaning a separate, unchanging piece; no fused endings. (Precedent: Mandarin, Vietnamese.)
- **Order: act word, then subject, verb, object (SVO), modifiers after their head.** Noisy-channel argument (Gibson et al. 2013, Psych Science): if one noun is lost, its role is still recoverable from which side of the verb it was on; SOV needs case endings to get that. Consistent head-first avoids center-embedding. No case marking, no agreement. Add-back trigger for agreement-as-checksum: confusion tests show roles getting lost.
- **Operators scope over what follows them.** Negation, confidence, source: at clause start they cover the clause; before a word they cover that word. One rule, so scope follows word order.
- **Speech-act word at the start.** Statement is unmarked; question, request, instruction, advice, intention, warning, non-literal each get a particle. Doubled warning = emergency. (Precedent: question particles in 61% of languages.)
- **Confidence = a number.** Confidence particle + a digit 0–10 ("7 in 10"). Anchored by construction, any precision. Unmarked = ordinary belief. Explicit "don't know how sure." Sign: one-handed digit held on the non-dominant hand during the clause. (No natural precedent: risk; likely erodes to a few common values, which still stay numeric.)
- **Source optional:** seen / told / inferred particles; unmarked = unspecified. (Precedent: 57% of WALS languages have some evidential.)
- **No yes/no words: echo answers.** Answer by repeating the verb, negated or not. Fixes negative-question answers and doubles as confirmation. (Precedent: Irish, Welsh, Finnish, Mandarin.)
- **Acknowledgment:** "mm" = heard, echo = understood, intention particle + verb = will do. No new words.
- **Reference slots:** third persons get slots 1, 2, 3 in order of introduction; slot pronouns are used only when referents compete, plain pronoun otherwise. Sign: slots are points in space (loci), and verbs move from subject's point to object's point. Speech may add the same pointing gesture. No grammatical gender. (Precedent: sign-language loci; spoken version untested: risk.)
- **Time:** tense optional; optional aspect particles (done / ongoing / about to); time words name an anchor plus an offset; no "move forward" metaphors.
- **Numbers:** base 10, because the signed surface counts on fingers; fully regular ("ten-one" for 11). Own sound rules, confusion-tested. Designed later.

## Grammar words and numbers v0 (2026-10-08)

Chosen by an optimizer (`tools/confusion.py`) using Miller & Nicely 1955 Table III (-6 dB) for 12 consonants; approximants, vowels, final -n and missing onsets are estimates. Meaning-flipping pairs (NOT vs anything, I/YOU, ALL/NONE, SEEN/TOLD, BEFORE/AFTER...) are weighted 10-30x. Result: ~3.5x lower expected confusion than a random assignment (11.8 vs 41.5). Grammar words are unstressed; content words stressed on the first syllable.

- Speech acts: Q ti, REQUEST gi, INSTRUCT nan, ADVISE vun, INTEND we, WARN lon, NONLITERAL sen
- Operators: WH den, UNSPEC ba, NOT mu, CONF so, SEEN bon, TOLD lun, INFER kan
- Pronouns: I gu, YOU a, WE(incl) zin, WE(excl) pon, HE/SHE/IT ne, SLOT1 san, SLOT2 yen, SLOT3 si
- Determiners: PLURAL en, THIS nin, THAT la, ALL vo, SOME sun, PART (some-not-all) ko, NONE fe
- Aspect: DONE i, ONGOING tun, SOON van
- Relations: OF yo, AT li, TO un, FROM ve, WITH wan, FOR fin, BEFORE te, AFTER gon
- Linkers: AND ga, OR ka, BUT non, IF bi, BECAUSE ken, THAT(complement) fu, WHO/WHICH(relative) win
- Numbers (two syllables, CV.CV): 0 noke, 1 yusi, 2 pano, 3 gefu, 4 wiye, 5 yazu, 6 nuvo, 7 bomi, 8 gawa, 9 kove, 10 suta, 100 munu, 1000 teku. ~500x less confusable than random.
- Weakest remaining pairs: UNSPEC/AND (ba/ga), DONE/AT (i/li), YOU/THAT (a/la).

## Devil's-advocate review of confidence and reference (2026-10-08)

User challenged #5 (numeric confidence) and #7 (numbered reference slots). Notes: `research/notes/numeric-confidence.md`, `research/notes/reference-tracking.md`.

**Confidence: kept, with changes.**
- Evidence it works: Canadian intelligence analysts on an out-of-10 scale were well calibrated; weather forecasters too (30% days rained 28.5%). Ordinary forecasters lose almost nothing at 7 levels; the best use ~11 (Friedman 2018), so 0–10 is the right ceiling. Separate "don't know" marker fixes the "50 = no idea" problem (Fischhoff & Bruine de Bruin 1999).
- Evidence against: numbers don't make people accurate; feedback does (LessWrong survey: "100%" claims right 44% of the time). Reframe: the feature transmits how sure the speaker *is*, which is the north star; it doesn't promise they're right.
- Changes: CONF means "chance this is true". Second digit for extremes (CONF 9 5 = 95%, CONF 9 9 = 99%), using the existing number words. Direction comes from negating the clause. Source particles cover how solid the grounds are (like ICD 203's likelihood vs confidence split).
- Remaining risk is social, not cognitive: unmarked statements may become the new vague hedge, since numbers can be checked.

**Reference: numbered slots dropped.**
- Capacity is fine (~4 items). But order-of-introduction numbering has no natural precedent, and optional marking fails because speakers don't notice their own ambiguity (Ferreira 2005; Keysar & Henly 2002).
- Replaced by three natural, attested mechanisms, triggered by structure, not by noticing ambiguity:
  1. **Obviation (obligatory once a second third person is active):** plain pronoun = the main character, obviative pronoun = anyone else. (Algonquian; obligatory there.)
  2. **Logophoric pronoun:** in reported speech or thought, a dedicated pronoun for the person whose words are reported. (West African languages, e.g. Ewe.)
  3. **Spatial pronouns (optional, for complex scenes):** "this-side one" / "that-side one", tied to pointing; identical to sign loci. Children master spatial reference late (5–10) in every modality.

Grammar words re-optimized (cost 12.3 vs random 42.7). The whole table reshuffled: many layouts are about equally good, so specific syllables are arbitrary within a good layout. Current table:
- Speech acts: Q yun, REQUEST fu, INSTRUCT gon, ADVISE to, INTEND zin, WARN ze, NONLITERAL san
- Operators: WH mi, UNSPEC wan, NOT na, CONF mon, SEEN kin, TOLD sun, INFER ven
- Pronouns: I e, YOU vun, WE(incl) nin, WE(excl) so, HE/SHE/IT lu, OBVIATIVE tan, LOGOPHOR gan, SIDE-A ku, SIDE-B sin
- Determiners: PLURAL in, THIS va, THAT nun, ALL len, SOME vi, PART kon, NONE bon
- Aspect: DONE fa, ONGOING gi, SOON yan
- Relations: OF on, AT yi, TO ke, FROM gen, WITH zo, FOR men, BEFORE fi, AFTER tun
- Linkers: AND gu, OR be, BUT fen, IF ti, BECAUSE win, THAT(comp) yo, WHO/WHICH(rel) mu
- Numbers unchanged.

## Lexicon v0 (2026-10-08)

Built by `tools/lexicon.py`; full list in `data/lexicon.tsv` (262 roots + 13 numbers).
- Syllable partition: 52 syllables reserved for grammar words, 108 for content words; content words never contain a grammar syllable.
- Confusion weights: antonyms 30x, same semantic field 3x, numbers 10-30x. Result: ~12x lower confusion than random (1.02 vs 11.96).
- Zipf: tier-5 concepts average 3.5 letters, tier-1 4.95.
- New grammar words: BE la (copula; subjectless = "there is"), MORE u, VERY we, LIKE wo. Adjectives are their own class; predicate use needs BE, so "house big" is always "the big house".
- Compounds are ordinary head-first phrases that became fixed: dragon = BOzen NOwi "snake fire".
- Numbers re-done inside the partition: 0 donma, 1 tugun, 2 suki, 3 wumun, 4 tumin, 5 nenon, 6 livan, 7 ayon, 8 digun, 9 enge, 10 newen, 100 tonvu, 1000 senni.
- To add in v1: roots for today / tomorrow / yesterday (frequent, already anchored to now).
- Signs: iconic forms; antonyms often become mirror-image movements, which conflicts with "keep antonyms far apart". Allowed only for large path reversals; to be tested.

## Moved to a git repo; stress test 001 (2026-10-08)

The project moved out of the Obsidian vault into this repo. `docs/language.md` is now the current reference; this log keeps the history.

- Words are now stable: `data/*.tsv` are the source of truth and `tools/words.py` adds new words into the best free form without moving existing ones.
- Stress test 001 (`texts/001-alien-stick.md`, a profane rant about hitting aliens with sticks): 131 syllables vs ~113 English; about equal speaking time given simpler syllables. Compounds covered every missing concept.
- Adopted from it: generic pronoun **pen**; **ban** rather, **bin** only, **wun** at least; **zan** while; **dun** exclaim plus one curse root **fezi**; standalone **san.** covers a whole turn; prepositional phrases attach to the main verb; a noun's modifiers precede its "of" phrase; verbs can modify nouns; roots for today/tomorrow/yesterday.
- Open: only 4 free grammar syllables remain.

## Stress test 002: the commander (2026-10-08)

Fiction excerpt with dialogue and inner states (`texts/002-the-commander.md`). 414 syllables vs ~337 English (+23%); about equal speaking time. Extra length comes from **on e** "my", the compound **NIte GOni** "commander", and explicit **Avu**; frequent compounds would clip into roots in real use, so no fix.

Worked: obviation replaced English's she/it animacy split; echo answers; reflexive = repeated pronoun; compositional question words; an in-world oath (**dun VOnnu NOwi** "Godfire") grew from the curse system.

Adopted: question words in place; **mi** in a **yo** clause = indirect question; clause-final **yun** = tag; **san** = sentence, **san san** = turn (replacing the pause-based standalone **san.**); noun + number = count, noun + **on** + number = label; causative **Avu** + result + object (relative clauses have no end marker, so heavy phrases go last); **la** + verb = resulting state; noun + noun is modifier, coordinate with **gu**; dropped subjects only for same-subject continuation and addressees; linkers may precede the act particle; **zan** + NP = during; name adaptation by confusion data (Lilith → **LIlifi**). Text 001 updated to the revised rules. 13 new roots, no new grammar words.

The user can only supply English texts. Claude will add tests built around things English expresses badly (evidentiality, inclusive/exclusive "we", confidence, reported speech) so the tests don't only probe English's quirks.

## First-principles review (2026-10-08)

The user asked for a step back using their five steps. Findings: the learning goal was working (two devil's-advocate rounds changed the design); three Claude-added parts were weak; nothing independently measured the north star.

Decisions (user approved):
- **Goal narrowed:** a universal human language for modern Earth, as design and thought experiment. **D&D dropped**: a fantasy language and a modern-Earth language are different tasks. The table kit idea goes with it.
- **Signs dropped:** text is the wrong medium to design them. Removed from the reference.
- **Syllable partition deleted.** Stress already marks where content words begin; the partition duplicated it and had exhausted the grammar-word space. Existing words are unchanged; new words may use any syllable. Add back if a listening test shows grammar words misheard inside content words.
- **Spatial pronouns ku/sin deleted:** never used, weakest evidence. Add back if a text has 3+ people that obviation and names can't keep apart.
- **The optimizer's scores are model-internal**, not real-world results. The reference now says so.
- **Base 10 re-sourced:** it was justified by sign-language finger counting; now by finger counting plus the decimal system modern Earth already uses.
- **Reference rewritten** around five principles (common case free; heads first and position carries role; operators cover what follows; heavy last; doubling widens) plus 12 rules they don't cover.
- **Next:** blind back-translation test to measure fidelity directly.

## Back-translation test 01 (2026-10-08)

First direct measurement of the north star (`tests/backtranslation-01/`). A fresh agent with only the reference and word lists back-translated texts 001 and 002; another scored them. Content 55/64 (86%), force and tone 58/64 (91%), no segment lost its core meaning. Most losses came from vocabulary gaps and translation choices; grammar cost about one point (reflexive). Caveats: AI reader and judge; some test phrases leaked into the reference as examples.

Fixes: 14 documentation gaps closed in `docs/language.md`; reflexive **ku** (reusing the freed spatial-pronoun syllable); roots answer, system, offend, disgust, panic; `data/compounds.tsv`; gloss "right" renamed "right.side"; text 002 corrected and revised.

## Roadmap (2026-10-08)

The user asked for the long-term sub-goals before going further, in case any would change the foundation. `docs/roadmap.md` defines "full" as generative completeness (any text translatable without new grammar; any concept nameable by rule; the phonology can carry a natural-size lexicon). Seven challenges could touch the foundation: lexicon scale, derivation, number length, names and loans, prosody (focus, fast speech), politeness, deep embedding. Recommended order: A1, A3, A5, A2, A4, A6, A7.

## Drift research; stress challenged (2026-10-08)

The user challenged fixed stress and asked that natural evolution be weighed heavily and pre-empted. Three research passes: stress and sound change, grammaticalization and drift, designed languages that went native (`research/notes/`). Synthesis in `docs/drift.md`. Proposals awaiting the user: keep initial stress but realize it as pitch; drift-aware word scoring; consonant-distinct grammar words; computable lu/tan rule; politeness outlet; consider deleting /v/.

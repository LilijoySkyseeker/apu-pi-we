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

## Drift-proofing applied; all words rebuilt (2026-10-08)

User approved all six proposals. Done:
- **Stress** is a pitch movement at the start of the first syllable, with no lengthening; the rhythm is syllable-timed with full vowels everywhere.
- **Inventory:** /v/ deleted (rare, confusable with /b/, merges with /w/). /z/ deleted after the scale check (A1) showed it bought under 1% length and 4% confusion at 3,000 roots. 13 consonants remain: p b t d k g m n f s l w y.
- **Drift-aware rebuild** (`tools/build.py`): all grammar and content words reassigned. Content words must stay distinct after predicted drift (later e/i and o/u merge, middle p/t/k voice, later -n lost, s/z merge). Grammar words that share a slot start with different consonants; words in the same wider position stay distinct after drift. Numbers re-placed as two open syllables. Old-to-new map: `data/rename-2026-10-08.tsv`. Texts and docs converted with `tools/convert.py`.
- **wan/yi** (formerly lu/tan): **wan** = the most recent person or animal that was a subject; **yi** = any other third person or thing. Plain "most recent subject" failed on text 002 ("her face darkened" made the face the referent), so animacy was added; obviation in Algonquian is also about animates.
- **Politeness particle ku** with no truth meaning. New principle 6: every social pressure gets its own outlet (emphasis: **ba**, **bi**, doubling; politeness: **ku**; negation renewal: **mu mu**).
- `words.py` moved onto the new inventory and drift rules.
- A3 (digit length) has data but no decision yet; see roadmap.

## Numbers: long and short forms (2026-10-08)

User chose option 3 for A3 (both forms), noting people will shorten numbers anyway. So each digit's short form is the first syllable of its long form: the clipping drift is designed in. Short forms (one syllable, stressed) are used after a counted noun, after **ga**, or after another number word; long forms when nothing predicts a number (alone, after **pi**, after a verb, digit strings). 10/100/1000 keep only long forms and anchor number phrases. Short forms avoid every grammar word that can stand next to a number (determiners, prepositions, linkers, predicate words, pronouns), stay apart from NOT, and no two differ only by voicing. Built by `tools/build.py numbers2`; old-to-new map in `data/rename-numbers-2026-10-08.tsv`.

## Stress test 003 and back-translation test 02 (2026-10-08)

Claude wrote an original passage (the user's supply of quotes ran out) aimed at emphasis, numbers, politeness, three-person reference and two undesigned probes. Blind result: content 80%, tone 97%, all pronouns right, contrasts understood with no focus device. Fixes: **bu** "it" for things; **yi** = next most recent different subject; speech tags don't count for tracking; time offsets name their unit and clock times are labels; if-clauses may precede the act particle; comparison (**ke … se**), "how much" (**WIfu yu**) and loanwords documented; numbers written with digits; roots hour, phone, car, card, bus, dollar (loan). Modern vocabulary is now the largest source of loss (roadmap B1).

## Base 6; senary review; juncture fixes (2026-10-08)

The user cloned an earlier project, senary (a base-6 measurement system designed "from first principles", the same intent as this language), and asked whether to combine. A subagent review (`research/notes/senary-review.md`) recommended borrowing ideas only, reading senary as worldbuilding with an opposite premise. The user clarified the shared intent, which exposed an inconsistency: this language voided legacy everywhere except the number base. The user chose premise 2 (legacy void).

Three research passes (cognition, mathematics, typology) found no direct human evidence choosing among 6, 10 and 12. A transmission test with this language's own tools decided it: with one-syllable digits, base 6 is about 9× less likely than decimal to mishear a digit in a long number, despite 29% more digits. Decision record: `docs/number-base.md`. Changes:
- Digits 0–5: **po fi sa ka da te**, one stressed syllable each, no long form. Place words 6 **NObi**, 36 **MIko**, 216 **NIyu**; groups 6⁴ **YIyo**, 6⁸ **GIfe**, 6¹² **YUli**; point **MImi**, minus **GUti**. Two readings (quantity; digit-by-digit in groups of four) from senary.
- Confidence becomes sixths: **kon** + 0–6, seven levels (matches the ~7 usable bands for ordinary forecasters).
- Juncture fixes (the senary review found them): no content word may begin with a digit syllable (10 content words moved); no two grammar words differ only by a final -n (10 grammar words moved). `tools/juncture.py` checks both and runs clean. Renames: `data/rename-base6-2026-10-08.tsv`.
- Senary's digit sounds were not adopted: its one-vowel scheme tested ~400× more confusable.

## Senary measurement system carried over (2026-10-08)

The user chose to carry senary's system over as is and to keep the repos separate: senary for the math, this repo for the language. Division of work: senary owns definitions and values (`src/senary_tables.py`); this repo owns the words (`data/units.tsv`, `data/numbers.tsv`, `docs/measurement.md`).
- Unit words: senary names were kept only if, after sound adaptation (r→l, v→w, z→s), they were no more confusable than the 90th percentile of ordinary words. Only *Wela* passed; adapted senary names were 10–270× more confusable than typical words (*fuka* "pressure" vs *futa* "woman"). Senary's README calls its names placeholders.
- Scale words are number words (6⁴ **YIyo** … and new fractional groups 6⁻⁴ **KUfe**, 6⁻⁸ **BAfo**, plus **Unun** "power"); up/down pairs weighted as antonyms (error-size principle).
- Time of day = fraction of the day, digit-read (15:00 = .343). "hour" re-glossed as **Aya** "watch" = 6⁶ NAne = a sixth of a day.
- Open: week and month names.

## Word building (A2) (2026-10-08)

Research (`research/notes/word-formation.md`): agent, action, result, place and instrument derivations are the most widespread; analytic languages grow a few near-grammatical heads; the opacity of "person sky" came from the missing relation, not the generic head. Design: four markers before a verb base: **no** doer, **ge** result/thing done-to, **du** tool, **pu** place. Noun bases must state their relation with a relation word. Blind A/B test (`tests/wordbuilding-ab-01/`): markers 71/76 vs generic heads 69/76, no real decoding difference. Kept for length and drift; **ge** narrowed to things after it misread "student" as "lesson"; persons acted on use **Ewo gun** + verb. The one-syllable grammar space is now full (69 of 70 slots), so future grammar words must be two syllables or compositional.

## Names and loanwords (A4) (2026-10-08)

Research (`research/notes/names-and-loans.md`) overturned the plan to give names a looser sound system. The Mara → *mala* collision came from r → l, not a final consonant; looser layers erode back to native sound rules (Japanese, Finnish); and collisions are common (about 1 in 20 two-syllable names lands on a word). Adopted:
- the personal article **en** before every name (one of the last two free one-syllable slots);
- deterministic adaptation (`tools/names.py`): nearest native sound, glides between vowels, consonants never dropped.
Blind test (`tests/names-01/`): 44 world names; an added fixed **u** recovered about 43.5/44, copying a nearby vowel 42/44. Adopted **u** (it marks itself as added), plus a two-syllable minimum for names. Texts 002 and 003 updated (Lilith → **en LIlifu**, Tomas → **en TOmasu**, Ben → **en BEnu**). The one-syllable grammar space now has one slot left (nu/nun, which clashes with AGENT after drift).

## Politeness (A6) (2026-10-08)

Research (`research/notes/politeness.md`): first officers hint even in high-risk situations (Fischer & Orasanu); hints are rated less polite than clear requests (Blum-Kulka); polite pronouns wear down on a 150–300-year cycle, so a politeness word will inflate (English *please*); speech levels are receding where they exist. Design:
- no polite pronouns and no speech levels;
- **ku** freely repeatable, with inflation sanctioned;
- respect through **ku** plus address terms;
- politeness never changes the act, and hints, questions, **fon** and low confidence numbers are never politeness;
- the problem / act / "we need" pattern;
- no **ku** expected in **yo yo**;
- routines: **Upe** greeting, **Upe Isi** farewell, **LOta** thanks (new root), **SEpi** sorry.

Not adopted: an escalation convention and an urgent register beyond **yo yo** (add back if a test shows urgency lost). Blind test (`tests/backtranslation-03-politeness/`): content 19/20, act and urgency 20/20, politeness 19/20; politeness never blurred an act.

## Deep nesting (A7) (2026-10-08)

Two blind rounds on contract language (`tests/backtranslation-04-nesting/`). Round 1: original nested sentences read fully correctly, but with plausibility doing work in three places. Added mechanical rules: relative clauses attach to the nearest noun; time/reason/condition clauses at the start belong to the main clause and at the end to the innermost clause; a pause goes wherever a phrase could run on (after a fronted clause, after a subject containing a clause, between a recipient and a long object). Round 2: five sentences, three plausibility-neutral, all correct. No clause-closing word adopted; add back if attachment fails in a test. **All seven foundation items (A1–A7) are now done.**

## Remaining grammar (B2) (2026-10-08)

All built from existing words; no new grammar words.
- **Conditions** use the confidence scale: **don** open, **don kon FI** unlikely, **don kon PO** counterfactual; no "would".
- **Modality** keeps three kinds apart: ability **LAnu**, obligation **KEya**/**WUpi**, permission **gun Efon** (new root "allow"). Epistemic "must/might" is always confidence.
- **Comparison and choices:** less = more of the opposite; equality with **fu**; which-question **… lu … yu?** vs yes/no **min … lu …**; exclusive or **lu X lu Y**.
- **Quantities:** about **fu** + number, range **se … tun**, at most **mu ke se**, part **X pi Y**, occasions **MUyi** + number.
- **Small words:** **WAme** "also" (new root) scopes like **na**; each other **nen nen**; don't **tin mu**; let's **so pen**; whether **min** inside **wun**; purpose **li** + verb.

Blind coverage test (`tests/grammar-coverage-01/`): 24/24. Dates and clock time stay provisional pending the senary calendar rework.

## Vocabulary research, step 1 (2026-10-08)

Four research passes (`research/notes/concept-sources.md`, `colexification.md`, `efficient-semantics.md`, `early-vocabulary.md`), with CLICS4, Concepticon, Lexibank, Glottolog and WALS downloaded and checked. Key findings:
- Lineage coverage is measurable only for the top ~300 concepts; beyond that, the data reflects Indo-European-framed questionnaires.
- CLICS4 lump rates need a family-balanced computation (`tools/clics_rates.awk`) and cross-checks where broad meanings were copied.
- Efficiency models are filters, not generators. Colour and kinship have usable results; there's no majority kinship system to copy.
- Early vocabulary ranks categories, not words, and adds routines.

Draft decision procedure in `docs/vocabulary-method.md`, with three points for the user: seed size (~300 + NSM primes instead of 500–800), lump/split thresholds, and colour (need over majority).

## Seed vocabulary built (B1 step 3) (2026-10-08)

`tools/concepts.py` ranks CLICS4's 1,740 concepts by area-balanced lineage coverage (`data/concept-ranking.tsv`). The seed is the top 300 plus the NSM primes: 330 rows in `data/concepts.tsv`, built by `tools/seed.py`, each with a decision and an evidence line.
- 172 were already in the lexicon.
- 37 are expressed by grammar and 13 by numbers.
- 20 are compounds: the kin terms by the kinship rule, arm and leg parts, boy/girl.
- 88 got new roots, tagged by topic area and opposites. These include the kinship roots sibling and spouse; arm, as a noted exception to the 20–50% band because no transparent derivation from "hand" exists; and the four compass directions (the lens).

Added principle (user, 2026-10-08): basic words describe observation, not theory; boundaries resting on disproven beliefs get no lineage weight.

## Vocabulary test 01, batch 2, checker (2026-10-08)

The first everyday-text test (`tests/vocabulary-01/`) lost about 2–3 points to missing words (yam, goat, rice), which fired the agreed trigger. Batch 2 (`tools/seed_batch2.py`) added:
- 29 roots from ranks 301–650 present in all six areas;
- 7 on-demand roots;
- 12 built words and compounds.

The lexicon is now 445 roots. The test also caught two stale word forms in Claude's translation, the third such slip, so `tools/check.py` (roadmap C3) now flags unknown words; it also found stale names in reference examples. Colour verified (`research/notes/colour-vision.md`): separate blue rests on naming data and need, not eye physiology.

## Two layers: deep human experience and the modern world (2026-10-08)

The user noticed batch 2 leaned towards small-scale, low-technology life (scorpion, spear, canoe). The cause is that cross-linguistic concept lists were built to document traditional vocabulary, and lineage weighting amplifies New Guinea and South America. Decision (user): **modern text decides what's common and needed; base human existence stays the foundation.**
- Deep layer: weighted by lineage.
- World layer: weighted by modern need, measured by blind tests on modern urban texts from many cultures. Built words by default.

Six creature roots from batch 2 were demoted to descriptions (spider, turtle, frog, bat, scorpion, grasshopper; now in `data/compounds.tsv`). The lexicon is now 439 roots.

## Vocabulary test 02: modern urban texts (2026-10-08)

Five original texts (Lagos, Seoul, Mumbai, São Paulo, Cairo; `tests/vocabulary-02-modern/`). Almost everything came through, including modern abstractions built from parts: expensive, government, meeting, laptop, nurse, prescription, blood pressure, protest. About 1–1.5 points were lost to missing words (City Hall → Parliament, bread → grain), so **city** and **bread** were added and "internet" registered as a loan. A noun's location now takes a relative clause. The stop condition is not met yet.

## Vocabulary test 03 (2026-10-08)

Recipe, machine instructions, race report, neighbour complaint, storm warning (`tests/vocabulary-03-modern/`): essentially all correct. About 1 point lost to a missing word (onion → potato), so **onion** was added. Losses to missing words are falling: 2–3, then 1–1.5, then about 1. A pronoun slip by Claude (recency rule vs the natural pull to the topic) is noted as an open issue to watch.

## Deep-layer criterion: convergence; time-stability as a check (2026-10-08)

The user asked whether stability over long time spans is the best measure of base human experience. Answer, agreed: it's strong corroboration, but lineage breadth already integrates deep time. Time studies measure word-form survival, which mostly tracks frequency, and the agreement of independent signals is the better criterion. Check: the seed already held all of Holman's 40 most stable concepts and all but one of Pagel's 23 ultraconserved words; **worm** and **grind** added.

## Seed phase complete (B1) (2026-10-08)

Vocabulary tests 04 and 05 (`tests/vocabulary-04-modern/`, `-05-modern/`) lost under 1 point and 0 points to missing words: two in a row, so the agreed stop condition holds. Loss to missing words across tests 01–05: 2–3, 1–1.5, about 1, under 1, 0. The lexicon stands at 445 roots. From here, words are added on demand. World-layer concepts are built from parts unless they're frequent; modern abstractions (government, prescription, allergy, orbit) have composed reliably.

## First-principles review 2 (2026-10-09)

Step back at the end of the seed phase. Findings:
- On track.
- The biggest weakness is that all ten blind tests used AI readers, which guess well from world knowledge. **No human has heard the language.**
- Three Claude-added parts flagged: AI-reader fidelity as the measure, the unvalidated confusion model, and the wan/yi recency rule.

Approved deletions:
- single-use tools: `lexicon.py`, `convert.py`, `seed.py`, `seed_batch2.py`, `units.py`, `base_test.py`;
- three dead functions in `build.py`;
- the three old-to-new word maps.

All are in git history (last present at commit 8c65afd); add back if a rebuild or rerun needs them. The user agreed to read sentences aloud as the first human check. Writing: the user chose to focus on the Latin transliteration for now (discussion below).

## Writing spec; teaching capitals dropped (2026-10-09)

The user's first reading check found three things:
- my description of stress as a "pitch rise" read as question intonation (now: the stressed syllable is higher, stepping down after it, not longer);
- questions need no rising tone;
- in a sans-serif mobile font, **lon** "I" looked like "Ion": l, I and 1 collide.

Decisions (user): the Latin transliteration is the script for now (it costs nothing to type; computing runs on it); all lowercase, names included; stress unwritten because predictable, so the **teaching capitals were dropped from all docs and texts**; digits 0–5 grouped in fours; punctuation with defined jobs (`,` `.` and quotes required; `?` `!` optional; `-` for compounds). A native script is deferred, with triggers.

## Punctuation cut to three marks; declination (2026-10-09)

Human test 01 showed end marks steer the voice, but too late; the opening word (**min**, **yo**, **ba**) already does it earlier, like Spanish ¿. Doghouse review (user approved): writing marks only what speech marks with the voice. So `,` `.` `" "` stay, and `?` `!` `-` `:` are deleted, with triggers. Texts and docs updated. The user's "bouncing" with runs of two-syllable words led to specifying **declination**: stress peaks step down across a phrase and reset at the next one. Two English phrases that the capitals-dropping script had lowercased by mistake ("No tones", "In an emergency") were restored.

## Time and calendar words (2026-10-09)

Senary's r20/r21 rework landed (the count from Tranquility, local time as a view, the date as days elapsed, the six-day week, body time). The user ruled that the words are 100% this repo's and senary is only the maths and concepts. Result (`docs/measurement.md#time-and-calendar`): one idea, "a time point is an amount elapsed, said as a label", covers clock, date, year and weekday with the existing label rule. Two new roots, **nelon** week and **boyo** block, because calendar-aligned periods can't be said as plain durations. Everything else is a phrase from existing words: leap year **fawu netu**, local time **muyi pi kemu**, body time **muyi pi gawo**, the count **sunbu pi muyi**, seasons **muyi** + quality, age **nume** + duration. No words for the epoch, zero meridian, traveller's view, solar longitude or lunar month; add one if texts keep needing it. **aya** "watch" kept as the everyday hour-like unit. Unit-word glosses in `lexicon.tsv` changed from senary's labels (Kena…) to the quantity (unit.time…), so nothing here depends on senary's names.

## Senary uses the language's words; prefixes become scale words (2026-10-09)

The user ruled that every senary name was temporary and asked for them to be redone with this repo's tools. Discussion: senary's goal was naming more logical than SI. SI's prefixes are arbitrary names with uneven steps; senary's were generative (a digit consonant per syllable, a/i for direction) but carried each digit on one consonant and the direction on one vowel, and amounted to a second numeral system. The language already has a generative rule (**unun** + exponent, in ordinary numbers) plus shortcut words for the range where a wrong scale is believable. The user agreed: senary r22 (PR #3, merged) uses this language's unit words and its six scale words as prefixes, writes 6ⁿ beyond that, and derives symbols from the words (sigi → Sg to avoid SI). **genwi** 6⁻¹² was coined as **yuli**'s opposite so the set is symmetric. Also: `compounds.tsv` lost a stale 7-day "week"; `clics_rates.awk` no longer crashes on pairs with no data.

## The name: apu pi we (2026-10-09)

The lexicon had no word for "language". CLICS4 shows word/language lumped in 47 of 71 families (50.2% family-balanced), meeting the one-root threshold, while tongue/language is 9.5% (mostly Indo-European). So **apu** covers both. Any language is named **apu pi** + whose it is; this one belongs to everyone: **apu pi we** "everyone's language". The user approved; in English, Apu Pi We. Rejected: **apu pi ewo** (reads as "human language" in general) and an invented name (wouldn't follow the grammar). Caution recorded: the casual clip "Apu" is tied to The Simpsons in English.

## How a new word is made; old compounds rebuilt (2026-10-09)

Prompted by the user's question about how logically words are coined and connected. The answer, now written into `language.md` ("How a new word is made"): the logic lives in composition, roots are arbitrary on purpose (sound-meaning schemes like Wilkins' turn one misheard sound into a plausible neighbouring meaning). Audit fixes:
- Pre-marker person compounds rebuilt: commander **no wungu**, coward **no nuta**, wizard **no wase**, warrior **no migi**, alien **no obu se yaye** (was **ewo yaye**, the type the blind test flagged).
- **musu se yaye** (meteorite) broke rule 8, since a bare relation phrase after a noun belongs to the verb. Noun bases now link only with **pi**, a verb or a relative clause: meteorite **no dosi se yaye**, dragon **dinbu pi lumi**.
- bedroom used **temu**, a word that doesn't exist: now **pu wopo**. frog had the same rule-8 problem: now **noso meli man lonfe yen niba**.
- meditate used **saba**, also not a word: now **goyu pume**, as the reference already said.
- Possibly redundant roots checked: LEARN/TEACH lumped in 9.2% of families (two roots stay); DIE/DEAD has no CLICS data (both stay).
Texts 001 and 002 keep their test-time vocabulary, with a note.

## B6 deleted (2026-10-09)

I proposed a B6 plan (lexicon counts for rhyme and alliteration, demonstration poems and songs, a poetics section). The user: "the whole point of the art of a language is something that evolves from real use; any attempt to plan that out is missing the point." Agreed and deleted. The only part with a claim on survival, "does the design block play?", is better answered by use than by a study. Add-back trigger: real use hits something the design blocks. The roadmap's untested claim that five vowels make rhyme abundant went with it.

## Base 10; borrowing; offensive-word filter (2026-10-09)

**Requirement change (user):** "in reality, base 10 will functionally remain the default. senary is a fun project, and this language can provide the words for it", but the language shouldn't be built around it; it must stay "somewhat compatible" because senary may be used in worldbuilding. Premise 2 is amended accordingly: the language's numbers are base 10 and its everyday units and calendar are today's.
- **Digits 6–9** have two syllables (**ufo oma kefi mape**). A search for one-syllable forms found only **fe** and **nu** free; allowing final -n added **fin**/**non**/**nun**, which collide with **fi** and each other. So 6–9 were built like content words, pushed apart from each other and from the number words. Place words: **webo** 10, **loki** 100, **munno** 1000, **tonen** million, **siwin** billion. Quantity reading has no teens or irregular tens.
- **Confidence** is now tenths, **kon** + 0–10 (user's choice, for familiarity).
- **Calendar:** **nelon** = week (7 days), **dunan** = month (MOON/MONTH lumped in 69.6% of families, CLICS4), months and weekdays by number (Monday = 1), 24-hour clock read as digits.
- **Senary** keeps all its words (now marked kind "senary" in `numbers.tsv`); a senary number is introduced with the loan **senali**. `measurement.md` is now "Senary vocabulary"; `number-base.md` is marked superseded.
- **Borrowing (user):** technical and international words are taken from English through the sound rules, on demand, with no list (option A). International unit symbols pass through in writing. First loans in the lexicon: **awuwa** hour, **minitu** minute, **sekandu** second, **kilamita**, **pasentu**, **senali**. Flag recorded once: this favours English speakers in sound, not in meaning.
- **Offensive-word filter (user):** `tools/offensive.py` streams Wiktionary (kaikki.org) for 34 major languages: entries tagged vulgar, offensive, slur or derogatory, plus taboo meanings (sex, genitals, excrement, urine, death) read from glosses: 32,910 pronunciations. Each is mapped into our sounds and compared with every word (exact, near after merging voicing and e/i, o/u, or prefix). Ranking keeps words whose *main* sense is offensive and that are common (wordfreq Zipf ≥ 2.5). The word tools now skip any form matching such a word; the new number words were coined through it. Existing words that match are listed for the user before anything moves.

## Offensive-word moves (2026-10-09)

Reviewed by hand from the filter's ranked list; user: "proceed as you see fit". Moved, with the tools, avoiding the old forms:
- **lanu** → **lenu** "can" (Hindi/Urdu/Punjabi *lan(d)* "penis")
- **nega** → **lasu** "bite" (German *Neger*, English n-word)
- **pisan** → **tisan** "high" (German *pissen*)
- **webo** → **yawu** "10" (Mexican Spanish *webo/huevo*, slang for testicle; coined hours earlier)
- **ano** → **ago**, the senary length unit (Spanish/Italian *ano* "anus"); senary r23 changed its symbol An → Ag (PR #4)
- **ku** → **nun** "polite" (Portuguese *cu* "arse", Vietnamese *cu* "penis"); **nun** was the one free form keeping the same-slot consonant rule.

Kept: **lon** "I" (Vietnamese *lồn*), **pi** "of" (Mandarin *bī*; its high tone doesn't match our low unstressed **pi**), **go** "anyone" (Persian *goh*). No free one-syllable form exists for them; moving them means rebuilding all 64 grammar words, which would break the user's learning and every text. Add back (a full grammar rebuild with the filter) if a speaker of those languages finds it a real problem. Also kept as mild or comic: **wiwi** red (*wee-wee*), **tana** like (Tagalog *tanga*), **badin** lung (Tagalog *bading*), **kono** die (Spanish hears *cono*, not *coño*).

## Conlang comparison; core frozen (2026-10-09)

Research report `research/reports/Conlang design principles compared.md` (22 languages). Findings: governance and community, not design, decided every planned language's fate; each tradition optimised one property and paid elsewhere; speakers drop obligatory per-utterance costs. Apu Pi We's native framing removes the adoption killers, and its isolating, optional-particle, arbitrary-root design matches where other languages and native speakers drifted. Five things no predecessor did: perceptual root choice, drift-proofing, an offensive-word screen, numeric confidence with a politeness outlet, fidelity testing. Three repeated habits: validating only with its own instruments, English-centred data, fast churn. Agreed with the user: (1) a human listening test of the model's most confusable pairs (no conlang has measured this); (2) freeze the core, change only on evidence from use; (3) a watch list in the open questions instead of fixes; no adoption work.

## Economy test 01; tan and ben stand alone (2026-10-10)

The user built a first-principles yardstick for "best language" in a separate conversation without reading this repo (`~/research/Language/language-first-principles-2026-10.md`): Reach, Economy, Clarity, Restraint, Gate. The first review rated Apu Pi We weakest on Economy, meaning context rarely gets to take over. `tests/economy-01-context/` tested that: a blind casual conversation, translated blind, counted by rules fixed in advance. It came out at ~1.5× English's syllables. Apu Pi We forces fewer things than English (18 vs ~32), but what it forces costs whole words. It found four problems, which are being handled one at a time with the user.

**#1, done: no pronoun for an event or statement.** **tan** and **ben** may now stand alone for a situation, event or statement (**tan** nearer, **ben** further), generalising **gi tan** "so". Demonstratives do this in nearly every language (English *that*, German *das*, French *ça*, Japanese *sore*; Diessel 1999 counts it among their four basic uses). A dedicated two-syllable word (the one-syllable space is full) or stretching **bu** were rejected. The nearer/further line is left loose for speakers to settle. After a recipient, use **tun** so the determiner can't attach to it. In the test, the rule saves 1–3 syllables per use.

Still open from the test: **bu** misfiring on conversational topics (#2), wan/yi bookkeeping (#3), no rule for fragments (#4), and `tools/names.py` disagreeing with the doc's name rule.

**#2, done: bu = the thing being talked about (user chose option C, 2026-10-10).** **bu** used to be the most recent thing mentioned. In the test, casual "it" meant the topic, so **bu** kept landing on the wrong noun. Now **bu** is resolved by context, as "it" is in every natural language, and the speaker names the thing if it could be unclear. **ben** alone covers "that one", a thing that isn't the topic (German *es* vs *das* divides the work the same way). This gives up the "speaker and listener can't disagree" guarantee for things. The yardstick's Clarity only asks that the language *can* be made unambiguous, and drift.md already predicts native speakers moving pronouns toward the topic. Rejected: keeping the mechanical rule (A); context alone without **ben** (B). Add back a mechanical rule if a blind test shows listeners losing track of **bu** where a mechanical rule would have caught it. #3 (wan/yi) is the same question for people.

**#3, done: wan/yi follow the topic (user, 2026-10-10).** **wan** = the person or animal being talked about; **yi** = another one who isn't the topic. Both are resolved by context; name someone if it could be unclear. This undoes drift item 4's mechanical rule, which rested on Hudson Kam & Newport (learners regularise what they can't predict). That study concerns random input. Topic-based reference isn't random, and children learn it everywhere, including Algonquian obviation, where the speaker chooses the proximate. The speech-tag detail is dropped, since it only existed for the mechanical count. **nen** and **sun** are unchanged. The punctuation table's reasons that cited pronoun tracking were updated; the marks stay. Add back a mechanical rule under the same trigger as **bu**.

**#4, done: leave out what context supplies (user, 2026-10-10).** Rule 11 used to allow a dropped subject only after **yen**/**un** or in instructions and requests. It now allows dropping anything the listener can supply from context: subject, object, a relation word's object, even the verb, so fragments are grammatical. Precedent: Mandarin, Japanese and Korean (no agreement, radical pro-drop), and fragment answers in every language. This is the yardstick's layer 5 ("anything context supplies can be left out"). Cost: principle 2's guarantee holds only for what is said. Add back a narrower rule if a blind test shows omissions being misread. In the test lines it saves 2–5 syllables per fragment. That closes the four findings of economy test 01; the `names.py`/doc mismatch is still open.

## names.py argument bug (2026-10-10)

Found in economy test 01: the translator ran `names.py` with a name and got Christopher → *kilisatafala*, not the doc's **kulisutafalu**. Root cause: any argument other than "default" silently selected the echo rule that lost names test 01, and the tool had no way to adapt a given name, so the demo list printed under the wrong rule. The adaptation logic itself was right. Fixed: `names.py IPA ...` adapts the given names, with no arguments it prints the test list, and the echo rule needs an explicit `--echo`. Non-IPA input stops with a hint. The tests' hand-adapted Marcus forms (**malukasu**, **malukusu**) differ; the tool gives **malukasu**. The echo rule is kept only to reproduce names test 01; it could be deleted if nobody reruns that test.

## Restraint review (2026-10-10)

Against the yardstick's Restraint criterion ("design only what speakers can't easily fix themselves"). A designer controls the code, not how people use it. Agreed with the user:
- **Usage bans became predictions.** "Confidence is never used for emphasis", "hints, questions, advice and low confidence are never used to be polite" and principle 6's closing "never" are now on the watch list. The code that protects these systems stays: **ba**/**bi** for emphasis and **nun** for politeness still give the pressures their own outlet. "Never a 'move forward' metaphor" was deleted, since a metaphor can't be banned.
- **The curse word gefo was deleted.** It was added after text 001, the user's own text with swearing, found no way to swear. Swearing gets its force from taboo, which a designer can't confer, and speakers coin swear words from taboo roots, which the lexicon has (**wento**, **bodu**, **kono**, **nosen**), with **ba**. Add back if speakers reach for a swear word and the language blocks them from making one. Texts 001 and 002 keep **gefo** as a record; the form is free again.
- **nun's renewal path** ("nun nun becomes the ordinary polite form") moved to drift.md as a prediction.
- **Kept:** the optional precision systems (tenths confidence, evidentials, eight speech acts, **sun**, inclusive/exclusive "we"), since they cost nothing unused and are on the watch list; the writing rules, which already have add-back triggers; sound and vocabulary design, which speakers can't easily fix later.

## Testing stopped; rationale written (2026-10-10)

The user stopped listening test 01: no available synthesiser produced a reliable word-initial g before u. The user asked for one document holding the why and how of every part, so a later session can replicate and tweak it: `docs/rationale.md`, organised by topic with sources ([user], [evidence], [Claude]), methods, parameters and what to touch when changing each part. language.md still wins where they differ.

## English leaks fixed (2026-10-10)

The user's review against the Language Construction Kit asked whether Apu Pi We is an English cipher. Verdict: grammar and sounds aren't English, but every root was defined by one English word, and the seed matched CLICS concepts to roots by English gloss, skipping the lump/split rule. Agreed fix (five parts, user):
1. **Leaks.**
   - The insect fly gets its own root, **gekon**: CLICS4 FLY (INSECT)/FLY (MOVE) is lumped in 22 families, under 10%.
   - Occasions get **gimu** (**gimu sa** "twice"). **muyi** stays "time, duration"; French, German, Spanish and Mandarin all split these.
   - "light, not heavy" already had its root, **gamun**; only the concept table pointed to **wino**. A duplicate coined by mistake this session was removed before use.
   - Pale colour is built, **mu buda** "not dark", per the six-colour-root rule. LIGHT (COLOR)/LIGHT (RADIATION) is lumped in 13 families.
   - The concept table's three rows record this.
2. **Pinned glosses.**
   - 51 ambiguous glosses now carry a second gloss fixing the sense, e.g. "hard, not soft", "like, enjoy", "kind, type", "second, of time", "bark, of a tree", "call, phone or call to".
   - `antonyms.tsv` was updated to match. The concept table's expression column still uses the old one-word glosses, as a record of the seed.
   - No form changed.
3. **No new rule:** vocabulary-method §3.4 now says a shared English word is not evidence for a lump.
4. A test that never touches English words: `tests/roundtrip-01-japanese/`.
5. **No automation.** Add back a `words.py` check that refuses a gloss already in use unless it carries a sense, if a new English-pun leak is found.

## The interpersonal layer: decisions before design (2026-10-10)

From multilanguage test 01, decided with the user step by step:
- **Decision rule** (user confirmed): where unrelated languages independently converge on a *function*, the language needs it; where they split on the *form*, choose the cheapest form for native speakers. Count by independent lineages, not by speakers.
- **Ability, not obligation** (user): the language must let speakers signal relationship and stance when they want, not force every sentence to declare it.
- **In words, not intonation** (user): speech and writing must carry the same meaning. Written English had to invent emoji and tone tags because the channel dropped intonation (Dresner & Herring 2010). The language already does this for speech acts (**min**, **yo**).
- **Left out** (forms that evolution split on): graded "you" (136 of 207 languages have none, WALS 45), gender (254 of 378 have none in pronouns, WALS 44), honorific vocabulary (a handful of languages), register vocabulary layers (they come from each language's borrowing history). Add-back triggers:
  - graded "you": speakers with an address slot and **nun** still can't avoid sounding rude;
  - gender: listeners lose track of who's who where topic, **yi** and names don't help;
  - honorific vocabulary: the title mechanism proves too blunt;
  - register layers: formal texts are misread as casual or the reverse.
- **Three rooms to design** (functions that converge): (1) a place for stance words; (2) a place for direct address, with titles that also work when referring to someone, which covers respect for third persons; (3) focus and contrast. Design the room and leave the content to speakers, except for the minimum needed to make each room usable.
- Missing words from all the tests are noted in `vocabulary-plan.md` for the normal process.

**Room 1 done: direct address and titles (user chose A + B + C, 2026-10-10).**
- (A) A name or title used to call someone goes first (before the speech-act particle) or last, set off by a pause.
- (B) Title + name is an ordinary noun phrase, usable in address and reference; respect for a third person rides on it.
- (C) **lanno**, a gender-neutral title of respect, works before a name or alone as "sir/madam". It's a dedicated outlet (principle 6): otherwise "old" or "leader" would be pressed into service, as Latin *senior* became *sir* and *señor*. Rejected: rules only, leaving titles to speakers (the room would start empty).
- Add-back trigger for a graded "you": speakers with **lanno**, address and **nun** still can't avoid sounding rude.

**Room 2 done: focus (user, 2026-10-10).** **fule** before a word or phrase means "this one, not another", and before the verb it insists the statement is true. **genfo** means "even" ("even if" = **genfo don**). Both belong to the operator family of **na** and **wame**, are optional, and leave word order alone. Stress can't survive writing, and moving words breaks principle 2, so a word is the only form that meets both the speech/writing rule and fixed order. The old focus trigger fired: 10 of 11 languages flagged focus, and the Spanish and English round trips lost contrast.
- The tool first picked **webo** for the focus word, a form hand-rejected on 2026-10-09 (Mexican Spanish slang). Hand-rejected forms weren't recorded where the tools check, so `offensive.py` now has a `REJECTED` set (lanu, nega, pisan, webo, ano, ku). This is automation added after an actual recurrence (step 5).

**Room 3 done: stance (user, 2026-10-10).** The end of the sentence, after a pause, is the stance position, generalising the **min** tag. Openers use the linker position at the start. Three seeds, for the jobs that converge most: **iwun** "as you know" (shared ground), **buni** "okay?" (softening, inviting agreement without asking), **donon** "it turned out" (counter-expectation). They exist so that **min**, **kon** and **ba** aren't pressed into stance (principle 6); the Japanese round trip showed four stance particles collapsing onto **min**. Everything else (fillers, reminders, insisting, half-memory checks) is left for speakers to grow in the slot. Rejected: the slot alone, with no seeds. Watch list: **min**, **kon** or **ba** pressed into stance anyway.

**The interpersonal layer is now designed:** address and titles (**lanno**), focus (**fule**, **genfo**), stance (**iwun**, **buni**, **donon**). That's six new words and three position rules. It's untested: the next multilanguage round trip should check it.

**Retest of the interpersonal layer and two follow-ups (user, 2026-10-10).** `tests/multilang-01/retest/`: the targets moved from lost or inferred to marked in the text. Japanese stance: 6 of 14 particles carried in-text, where before all collapsed onto **min**. Hindi–Urdu respect: 26 of 45 in-text, where before 0 of ~10. Spanish contrast: 6 of 8 in-text, 0 lost. Follow-ups:
- **lanno** now goes before any person word (name, role, kin word), and alone it can refer to someone clear from context. All three translators asked for this, and Hindi lost respect for unnamed people.
- Japanese っけ (half-remembered "wasn't it?") is **kon** + the **min** tag, documented as an example. **min** was doing its own job (checking); the missing part, uncertainty, already has **kon**. So the stance watch-list trigger didn't really fire.

**Tabled (2026-10-10), pending a first-principles review of how the language coexists with existing cultures:** five clarifications from the multilanguage translators, proposed but not yet written in:
1. **gun** at the start of any clause means "there is"; to say "(it) is X", keep the subject.
2. Clock times as four digits (`0900`), and digits in ordinary writing.
3. **a**/**ba** can go in front of another speech-act word (rhetorical or indignant questions).
4. **de** commits only the speaker or their group.
5. Labels under 100 use the counted form; years, clock times and identifiers are read digit by digit.

Item 2 is what prompted the review: a speaker in a 12-hour culture lives with 12-hour clocks.

## Coexisting with existing cultures (user, 2026-10-10)

Even native speakers live inside existing cultures: American 12-hour clocks, Sunday-first weeks, names like Denise. Principle: **the insides are built for native speakers; the boundary with culture carries any culture's conventions and imposes none.** These are different rules for different parts, not a trade-off between native and current speakers, because both live in the same cultures. Up for review under it: the 24-hour-only clock, Monday = day 1, name adaptation, and English as the only source of technical loans.

**Clock (user, 2026-10-10), the first item under the coexistence principle.** Both systems are carried:
- **24-hour:** four digits read one at a time (**po mape po po**).
- **12-hour:** hour and minutes counted, plus a part of the day with **pi** (**mape ka yawu pi yami** "nine thirty at night"). This is the form nearly every language uses for 12-hour times: *de la noche*, 午後, 晚上, *raat ke*. The part of the day drops when context supplies it.
- **New roots:** **minfi** noon, **duwun** afternoon. Midnight is "twelve at night".
- **Writing:** the local clock notation passes through like unit symbols, which also removes the colon problem.

Tabled item 2 is resolved by this.

**Weekdays (user, 2026-10-10): keep numbers, anchored to ISO 8601 (Monday = 1).** Named weekdays (option A) were rejected because the 7-day week is itself one culture's convention; borrowing English names (B) was rejected because it favours one culture. The user's tie-breaker, now a principle: carry every culture's convention where they coexist; where they conflict and one must be picked, follow the international technical standard. The learner guide already says Monday = 1.

**Names (user, 2026-10-10): keep the owner's spelling.** A personal name is written in its own Latin spelling or standard romanisation, lowercase after **en**, and said as close to the original as the speaker can, as most Latin-script languages do. The adapted form (`names.py`) is now the spoken fallback and stays the rule for loans. Places may keep an established adapted form beside the original. This fixes the costs the tests found: hard-to-recognise names, collisions, and the garbled 老周 → "Lao Dou". Also fixed in `names.py`: the two-syllable rule appended **u** without a glide (**tuu**, **beu** → **tuwu**, **beyu**). Documented ʋ → w.

**Confidence back to sixths (user, 2026-10-10).** **kon** + 0–6. Reasons: the 0–6 scale gives the ~7 bands forecasters can use (Friedman et al. 2018); every value except certainty (**kon ufo**) is one syllable, where tenths put the common values 7–9 on two-syllable digits; and it's flavour. **kon** is part of the insides (grammar), so the native-speaker rule governs it, not the boundary tie-breaker. Exact probabilities use a number and **pasentu**. Examples were updated: "must be home" = **kon te**; the half-memory and "maybe" examples = **kon ka**. Earlier tests and texts keep tenths as records.

**Coexistence pass finished, and the tabled clarifications written in (user, 2026-10-10).**
- **Loans:** now "borrowed in their international form", the form most languages share (usually English, or Latin/Greek for sciences and SI units). The rule is the same in practice, but English is no longer its stated source.
- **gun** at the start of any subjectless clause = "there is". "(It) is X" keeps its subject, the one exception to rule 11.
- **a**/**ba** can go in front of another speech-act particle (rhetorical and indignant questions), in the order a/ba, particle, nun.
- **de** commits only the speaker or their group; others' intentions are reported or stated with time words and **kon**.
- Labels under 100 are counted; years, 24-hour clock times and identifiers are read digit by digit.

The clock item was resolved earlier by the clock decision.

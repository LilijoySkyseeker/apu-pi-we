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

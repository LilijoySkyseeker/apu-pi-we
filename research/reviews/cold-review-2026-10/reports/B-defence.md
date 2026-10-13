# B: Defence of Apupiwe against the cold reviews

Scope: every finding rated high or medium in A3, A4, A5, A6 (impact high, medium or low-medium, including its internal-test table) and A7. Low findings are cited only where they bear on these. "Reference" means `docs/language.md`; "rationale" means `docs/rationale.md`; paths are relative to `/home/agent/work/repos/universal-language/`.

A note on what the reviewers saw. A3, A4, A5 and A7 had only the reference, word lists, learner guide and UDHR page. They didn't have the rationale, design log, tests or measurement.md, so some findings say "no reason is given" where one exists. I say so where it matters. Where the reason that exists is weak, I say that too.

## New evidence from the design's own tools

I ran `tools/confusion.py` (Miller & Nicely, −6 dB, the model every form was optimised with) on the pairs the reviewers named. Values are P(heard as b | said a) for one syllable.

| Pair | P | Pair | P |
|---|---|---|---|
| **sa** "2" → **fa** "none" | **0.120** | **fa** → **sa** | 0.039 |
| **wun** "that" → **un** "but" | 0.043 | **wo** "after" → **o** focus | 0.042 |
| **yen** "and" → **en** name | 0.042 | **la** plural ↔ **le** ongoing | 0.029 |
| **ka** "3" → **sa** "2" | 0.028 | **sa** → **ka** | 0.021 |
| **man** → **mon** | 0.027 | **po** ↔ **bo**, **pu** ↔ **bu**, **pi** → **bi** | ≈0.004 |
| **mu** ↔ **me** | 0.002 | **tin** ↔ **din**, **ka** ↔ **da**, **te** ↔ **de** | ≈0 |

Baseline: for content words, the nearest neighbour of the median word scores 0.0005, the 90th percentile 0.0014 and the worst word 0.036. So **sa → fa** is about 85× the 90th-percentile content pair and over 3× the worst one. The glide-only pairs are about 30× it.

Two more checks:
- The digits 0–5 under today's model have a mean P(heard as another digit) of **0.0185**. `docs/number-base.md` reports **0.0002** for the base-6 set. I couldn't reproduce that figure (`base_test.py` was deleted), so either the model changed after the test or the test measured something else. Either way, the published number doesn't match the tool in the repo.
- **un** (BUT) and **wun** (THAT.comp) are both in the `link` group of `GROUPS_STRICT` in `tools/build.py`, which requires different first consonants. The check counts "no consonant" as a consonant, so a glide-only pair passes it. That's a flaw in the drift-proofing check itself.

## Summary table

| # | Review · id | Finding (short) | Sev. | Response |
|---|---|---|---|---|
| 1 | A3 2.1 | Digits and short grammar words too close (fa/sa, sa/ka/da, po/bo) | H | **concede** (one side claim wrong) |
| 2 | A3 2.3 | Grammar carried by pauses; no relative-clause closer | H | partly |
| 3 | A3 3.1 | Senary measurement system (L3); distorts digits | H | partly |
| 4 | A3 2.2 | No future/irrealis marker | M | partly |
| 5 | A3 2.4 | Pragmatics prescribed, not left to use | M | partly |
| 6 | A3 2.6 | Vowel-only packing of grammar words; ban on reduction | M | partly |
| 7 | A3 4.1 | Lexicon too small (483 roots) | M | partly |
| 8 | A3 5.3 | Toki Pona-like phonotactic prior | M | partly |
| 9 | A3 5.4 | SVO without case untested | M | partly |
| 10 | A3 5.12 | Loans adapted from English; awuwa fails L4 | M | **concede** |
| 11 | A4 F1 | Loans: English forms, about half not world-shared (L4) | H | **concede** |
| 12 | A4 F2 | Confidence in sixths (kon + digit) | H | partly |
| 13 | A4 F3 | Senary system and calendar in the core (L3) | H | partly |
| 14 | A4 F4 | Oblique relatives strand the preposition | M | partly |
| 15 | A4 F5 | fa "none" without verbal negation (SAE) | M | partly |
| 16 | A4 F6 | Copula needed for adjectives; gun + verb is an SAE passive | M | **defend** |
| 17 | A4 F7 | Three rare reference systems stacked (clusivity, yi, sun) | M | partly |
| 18 | A4 F8 | One areal (isolating) type, undocumented | M | partly |
| 19 | A4 F9 | Pragmatics prescribed: "never hint", compulsory act particles | M | partly |
| 20 | A4 F10 | C1 method not shown; apu claim overstated | M | partly |
| 21 | A5 1 | Minimal-pair grammar words (ba/bi/bo/bu …) | H | partly |
| 22 | A5 2 | Parallel senary numbers + native unit roots | H | **concede** |
| 23 | A5 3 | Doubling is six memorised meanings | H | partly |
| 24 | A5 4 | Confidence/evidential/stance/politeness unattested in UDHR | M | **defend** |
| 25 | A5 5 | Comma/pause patch set | M | partly |
| 26 | A5 6 | gun-ellipsis and determiner "patch" rules | M | partly |
| 27 | A5 7 | sin has three frame-dependent readings | M | **defend** |
| 28 | A6 C21 | Friedman 2018 cited for sixths; rated wrong | high impact | partly |
| 29 | A6 C15 | Esperanto/Hebrew/creoles "all moved to" the design | low-med | **concede** |
| 30 | A6 C17 | Bergen 2001 overstated | medium | **concede** |
| 31 | A6 C18 | "All successful auxlangs" isolating | low-med | **concede** |
| 32 | A6 C19 | Melody-only speech acts fail; particle evidence | medium | partly |
| 33 | A6 C29 | "Function words replaced fastest" | low-med | partly |
| 34 | A6 C31 | Omission "including verbs" as in Mandarin/Japanese/Korean | medium | partly |
| 35 | A6 C32 | Polite pronouns cycle 150–300 years (no source) | medium | **concede** |
| 36 | A6 C36 | CLICS lump rates (apu 50.2%) not reproducible | medium | partly |
| 37 | A6 C44 | "ICAO lesson" for two-syllable digits | medium | **concede** |
| 38 | A6 C51 | Interface words / name spelling overclaimed | low-med | partly |
| 39 | A6 int. | Confusion model unvalidated (B2 has no external evidence) | high (gap) | **concede** |
| 40 | A6 int. | Base transmission test quoted as absolute | medium | **concede** |
| 41 | A6 int. | Economy test 01: AI readers | medium | partly |
| 42 | A6 int. | Multilanguage test 01 used as typology | medium | partly |
| 43 | A6 int. | Vocabulary tests 01–05: stop condition too early | medium | **concede** |
| 44 | A7 F1 | Optional markers will go categorical | H | partly |
| 45 | A7 F2 | The pause/comma is load-bearing | H | partly |
| 46 | A7 F3 | Grammar-word phonology fights reduction | H | **concede** |
| 47 | A7 F4 | pi overloaded; ordinals and dates rest on it | M | partly |
| 48 | A7 F5 | manni → man, konsin → kon by clipping | M | **concede** |
| 49 | A7 F6 | tin required; bare-verb commands are universal | M | partly |
| 50 | A7 F7 | Manner between verb and object will move | M | partly |
| 51 | A7 F8 | Positional existential gun won't survive subject drop | M | **concede** |

**Counts: concede 15, partly 33, defend 3** (51 findings).

---

## Detail

Grouped where several reviews make the same point. Each finding still gets its own response line.

### G1. Distinctness of digits and one-syllable grammar words (B2)

Findings: **A3 2.1** (H), **A3 2.6** (M), **A5 1** (H), **A7 F3** (H). Related to **A6 internal: confusion model** (#39).

- **A3 2.1: concede**, with one side claim corrected.
  - *Evidence for the reviewer:* by the design's own model, **sa → fa** is 0.120, the worst pair I measured, and both words follow a noun and can stand alone (reference 5.2: "A determiner may stand alone as a noun phrase: … **fa** 'none'"; 5.2: "A noun followed by a number is a count"). **to ibe totu fa / sa** is exactly the case. **sa/ka** are 2–3% under the same model. The digits were optimised against each other (`build.py numbers3`) and against grammar words' drift keys, but never scored by confusion against **fa**, whose key differs because the consonant differs.
  - *Where the reviewer is wrong:* "the template allows 140 monosyllables and only 67 are used, so 'ran out of short sounds' is false" ignores the constraints the design adds. These are: same-slot words differ in first consonant, no two grammar words differ only by final -n, juncture rules and the offensive filter. Rationale 4.2 says "the space is full (with 13 consonants, 5 vowels, ±n, minus digits, same-slot and -n rules)". The design log's correction of 2026-10-10 found that even the two "freed" slots (**san**, **pa**) were unusable. A7 F3(d) praises one of those constraints (the empty CV partner of every CVn word). "The real cause is senary" is half right: 0–5 kept forms optimised for a six-digit set (number-base.md says so), so 6–9 got what was left.
  - *Smallest fix:* move **fa** "none" to a form far from every digit, by the existing promotion rule (swap with the rarest one-syllable holder), or make "none" two syllables. Cost: one word, plus re-checking the texts. Also add a digit-vs-same-position grammar word confusion check to `juncture.py`. Rebuilding all ten digits (A3's direction) should wait for a human listening test (see #39), because the model that would choose the new digits is the one under question.
- **A3 2.6: partly.** The same-slot pairs A3 names are real: **la/le** is 0.029, and **wan la isi / wan le isi** sit in adjacent positions. **mu/me** is low by the model (0.002), and the design guards NOT with a ×10 weight (`build.py` line 208). A3's own counter-evidence (Japanese particles; slot does most of the work) is the right caveat. The "ban on reduction" ("every syllable keeps its full vowel", reference 2) is a norm, and B9 says the language doesn't try to control its change: concede that wording. The design's actual protection is structural (rationale 3.3: "same-slot words differ by consonant, so vowel reduction can't merge them"), and that holds for most pairs. *Fix:* restate full vowels and "grammar words keep their consonants" as the reference pronunciation, not a rule. Cost: none.
- **A5 1: partly.** The 19 vowel-only sets are mostly *across* slots: **ba** (act), **bi** (degree), **bo** (determiner), **bu** (pronoun) never compete for one position. That's the case the design accepts (`GROUPS_STRICT` only constrains same-slot words; drift.md's watch list names the cross-position pairs). So "a vowel slip swaps categories" overstates it, since the slot usually rules the wrong reading out. Concede where the slot doesn't: **la/le** (A3 2.6) and the glide pairs (A7 F3).
- **A7 F3: concede.**
  - *Evidence:* the glide-only pairs score worst after **sa/fa**: **wun→un** 0.043, **wo→o** 0.042, **yen→en** 0.042. **wun** "that" and **un** "but" are in the *same* strict group (`link`), and pass the check only because "no onset" counts as a consonant. That's a bug in the drift-proofing, not a design intent. The voicing pairs (**tin/din**, **pu/bu**) are near zero under noise (M&N: voicing survives), so A7's lenition route is the only risk there. drift.md's watch list already names **pi/bi** and **ke/ge**. The norm part ("grammar words keep their consonants", harmless variants "inside content words only") is a rule speakers can't obey, as A3 2.6 and A4 F22 also say.
  - *Smallest fix:* (1) treat onsetless vs glide as the *same* onset in `GROUPS_STRICT` and re-solve the link group. That moves **un** or **wun** by a swap within the full space. (2) Replace the consonant norm with A7's design constraint: no grammar-word contrast may rest on a declared harmless variant. Cost: one or two word moves now, and a slightly tighter optimiser later.

### G2. Pauses carrying grammar (B3, B4)

Findings: **A3 2.3** (H), **A5 5** (M), **A7 F2** (H).

- **Response to all three: partly.**
- *Defence:*
  - B4 is met formally. The comma is defined as the written pause (reference 3, 4.6), so both channels carry the same thing.
  - B3 asks only that a precise way exists. The pause is that way, and so is restructuring ("heavy goes last", reference 1.4 and 5.3: "use a new sentence").
  - The design tested this rather than assuming it. In `tests/backtranslation-04-nesting/analysis.md`, contract sentences with nested clauses came back fully correct in two rounds. In `tests/comma-01/results.md`, 0 of 67 lines lost meaning with every comma removed (85 comma uses).
  - The rationale (4.6) has an explicit add-back trigger: "add a two-syllable [closing word] if attachment fails in a test".
  - A5's "a second grammar bolted on" is overstated. Six of the eight pause positions in 4.6 are places where every language pauses (address, openers, stance tags, dates).
- *Concession:*
  - Every test reader was an AI with world knowledge, and comma-01 itself says "a topic opener never occurred". The nesting reader had the rules.
  - The evidence A3 and A7 cite is on point: speakers produce disambiguating breaks unreliably unless the ambiguity is salient (Allbritton et al. 1996; Kraljic & Brennan 2005), and texters drop commas.
  - "A pause closes … every relative clause still open" is the one structure with no word-level precise form other than rewording.
  - A7's B9 argument is the strongest. If natives will grow a closer anyway (Tok Pisin *ia*, Sankoff & Brown 1976), offering one now lets communities converge on it.
- *Smallest fix:* one optional two-syllable closer for relative clauses and phrasal derived words, with the pause kept as the casual form. This is the trigger the rationale already names, pulled early on the strength of the production literature. Cost: one word, and 2 syllables when used. One-syllable space isn't needed.

### G3. The senary system

Findings: **A3 3.1** (H), **A4 F3** (H), **A5 2** (H). Related: **A4 F2**, **A3 3.2** (sixths).

- **A5 2: concede.** The 20 unit roots and 9 senary number words plus **senali** (30 rows of `data/lexicon.tsv`, all tier 1) duplicate the SI loan names that reference 9.3 makes standard. The rationale gives one reason to keep them: "Keep senary usable: it may be used for worldbuilding" (§7). The goal's N6 now rejects exactly that ("not tailored to the projects that use it"), and the design log for 2026-10-11 records "Senary compatibility is dropped from the goal". So the parts have lost their source. *Fix:* move the 30 rows and measurement.md out of the core lexicon into the senary repo or an appendix word list. Add-back trigger: a speaker community using base-6 units. Cost: nothing in use; the senary repo keeps its words.
- **A3 3.1: partly.** Concede the deletion (as above). Dispute two parts:
  - *L3 framing.* L3 says which convention the language *follows*, and it follows SI and decimal (measurement.md: "Apupiwe's own numbers are base 10 … senary is a topic the language can talk about, … not a system built into it"). Words for a non-standard system don't breach L3, any more than English "dozen" does. The real charge is cost (C1, N6), and that holds.
  - *"Delete senary, therefore rebuild the digits."* The digits' problems (G1) stand on their own and should be fixed by evidence, not as a consequence of deleting senary. The path dependence A3 describes is real and documented (number-base.md: "0–5 kept their optimised forms"; 6–9 two syllables because "no robust one-syllable forms were left").
- **A4 F3: partly**, same reasons. "A senary calendar sits inside the core language" is a misreading: the calendar is today's (reference 8.3; rationale §7), and the senary calendar words live in measurement.md as vocabulary for a topic. The 30 lexicon rows are the part that is really inside, and they go.

### G4. Loans (L4)

Findings: **A3 5.12** (M), **A4 F1** (H).

- **Both: concede.**
  - L4 is a hard limit: "A word is borrowed only when the world already shares its form." The design's own record admits the practice: rationale 5.5 says "In practice that is usually English … Cost recorded: favours English speakers in sound". The design log for 2026-10-09 says "technical and international words are taken from English through the sound rules". **awuwa** "hour" has no world-shared form (A4's nine-language check: 0/9).
  - Partial mitigation: the policy predates the goal (L4 is from 2026-10-11), and the newest practice already applies a stricter test. The UDHR pass says "No loans: no candidate form is shared by all eight check languages" (design log, UDHR new roots).
- *Smallest fix:*
  - Re-run the 23 loans through that same eight-language test, or A4's 20-language panel.
  - Replace the failures (**awuwa**, **diguli**, **osupitalu**, **bayisikalu**, **kontakutu**, **ilekutulisiti**, **senali**) with native or built words. For example, hospital = **pu** + "heal", which the word-building rules already allow.
  - Re-adapt the survivors from the median form, not the English one (A4 suggests *kilometa*, *internetu*, *minutu*, *sekundu*).
  - Change rationale 5.5 to match L4.
  - Cost: about 7 replacements and 8 respellings during the design phase (the freeze is lifted). **awuwa** is tier 4, so learners pay for the change only if it comes late.

### G5. Confidence in sixths

Findings: **A4 F2** (H), **A6 C21** (high impact). Related: A3 3.2, A7 F13 (both low).

- **A6 C21: partly.** A6 rated it "wrong". I read the paper (Friedman et al. 2018, Table 1):
  - Untrained individuals lose **0.5%** in mean Brier score at seven equal bins, with a median of **0.2%, not significant**. Superforecasters lose 40%.
  - The paper's mean usable precision is 6.1 bins.
  - The design's research note transcribes this correctly (`research/notes/numeric-confidence.md`, lines 22–25). So "about 7 bands are what ordinary speakers can use without loss" is supported for the population the language serves.
  - What's wrong is the one-line rationale (4.3, 10). It drops the paper's own conclusion, that coarsening "consistently sacrifices predictive accuracy", and the loss for skilled users, who would want finer steps. The language has those finer steps anyway: half-steps (**kon te mimi te**) and **pasentu**.
  - *Fix:* reword the citation to "ordinary forecasters lose about 0.5% at seven bins; skilled ones lose more and can use half-steps or percent". Cost: none.
- **A4 F2: partly.**
  - *Concede:* no language grammaticalises numeric probability, so this departs from B5. Sixths are also a residue of base 6: confidence moved to tenths when base 10 returned, then back to sixths (design log 2026-10-09 and 2026-10-10).
  - *Defend:*
    - (a) The B3 evidence for numbers over words is verified (A6 C20: Budescu et al. 2014; Wintle et al. 2019).
    - (b) It's optional and unmarked by default (reference 6.1: "An unmarked statement is believed"), so its everyday cost is zero, against A4's "a large share of everyday sentences".
    - (c) Sixths are cheaper than tenths: 0–5 are one syllable, and in tenths 6–10 are two.
    - (d) The counterfactual **don kon po** is transparent irrealis ("if, and it isn't so"). Iatridou's "fake past" isn't available in a language with no tense, so A4's comparison doesn't transfer.
  - *Concede the real gap:* there is no documented vague "maybe". **kon ka** claims 50%.
  - *Smallest fix:* document **kon fu ka** "roughly even, maybe" using the existing **fu** "about" (reference 9.3). Cost: one sentence, no new word. Whether A4's 2–3 vague grade words would be better is an empirical question. A7 F13 predicts natives will lexicalise exactly that, which can be left to use (N4).

### G6. Optional markers, future, imperative, existential (what natives will do)

- **A7 F1: partly.**
  - *Defend the premise:* Hudson Kam & Newport's children regularised *unconditioned* random variation (A6 C24 notes the scope). Here the variation is conditioned by meaning, and the reference states the default reading when a marker is absent (A7 concedes "the reference mostly does").
  - *Concede:* **sin** becoming past is likely, and drift.md item 7 already predicts it ("**sin** done → past … mostly let it happen"). The consequence A7 finds, **mu sin** "not yet" merging with "didn't", isn't covered.
  - *Fix:* reword principles 1 and 7 as defaults, not "when precision matters". Add "not yet" to drift.md's watch list with a fallback (**mu … eda** "not now" or a dedicated two-syllable word when needed). Cost: wording.
- **A3 2.2: partly.**
  - *Defend:* the frame mechanism (reference 8.1) is the Mandarin/Yoruba pattern, and a future time word covers most future sentences.
  - *Concede:* there's no general "later/will". The lexicon has **eda** "now" but no "later" or "future" root (`data/lexicon.tsv`). "She'll come (some time)" needs **wo** used alone. The consistency pass raised exactly this ("How do you say plain future?", `tests/consistency-01/fresh-read.md` line 98). A3's creole and "tenseless language" evidence (Indonesian *akan*, Mandarin *huì/yào*) is right.
  - *Smallest fix:* one two-syllable time root "later, in the future", which slots into the existing frame rule with no grammar change. Leave a future particle to grammaticalise (A7 F1 predicts one from **momu**/**isi**). Cost: one root.
- **A7 F6: partly.**
  - *Defend:* B4 is the reason **tin** exists. A bare-verb command is distinguished only by intonation, and the decision rule is "in words, not intonation" (design log, interpersonal layer).
  - *Concede:* with omission now allowed (4.5), a subjectless bare verb is already ambiguous. Aikhenvald's bare-stem universal makes A7's prediction near-certain, and A4 F20 agrees.
  - *Fix:* accept a subjectless bare verb as a casual command, with **tin** as the precise form. That's the same "precise form exists" pattern as everything else. Cost: one sentence; B8 gains.
- **A7 F8: concede.** "gun with no subject means 'there is' only at the start …" (reference 4.7) is a positional rule that pro-drop will erode (Spanish *es dinero*). A5 6 flags the same rule as a patch. **mu gun pasu** "no food / (it's) not food" is the merge.
  - *Fix:* bless **ibe** "have" with no subject (or with **go**) as the existential, the Mandarin 有 / Haitian *gen* path, and let subjectless **gun** be plain "is". Cost: re-reading about 10 UDHR sentences, and a parser rule change.

### G7. Pragmatics and social words

Findings: **A3 2.4** (M), **A4 F9** (M).

- **Both: partly.**
- *Concede:* "Being polite never means hinting" (learn.md lesson 8, line 312) is a usage ban. The Restraint review of 2026-10-10 turned exactly these bans into watch-list predictions ("hints, questions, advice and low confidence are never used to be polite" → watch list). The learner guide wasn't updated. Delete it.
- *Defend the rest:*
  - A4's "7 obligatory illocution particles" misreads the reference. Reference 7.1 says "A statement has no particle", and 4.2 says only "A command needs **tin**, or **so** for a request". Advice, commitment and warning can all be said as statements (**pen wupi isi** "we need to go"), so **fon**, **de** and **yo** are optional.
  - A3's "prescribing which stance particles exist" misreads 7.2: "Other words used in this position are stance words too." The three seeds exist because the Japanese round trip collapsed four stance particles onto **min** (design log, Room 3). In the retest, stance carried in-text went from 0 to 6 of 14, and Hindi respect markers from 0 to 26 of 45 (`tests/multilang-01/retest/`). That's evidence, though from AI translators (see #42).
  - Separating politeness from the speech act serves B1, and A3 itself keeps **nun** and **lanno** on that ground.
- *Cost of fix:* one sentence deleted from learn.md.

### G8. Lexicon size and vocabulary evidence

- **A3 4.1: partly.** The method adds roots when a test shows loss (vocabulary-method §5). That process is still running: **dundi**, **gigin**, **yenbo** and **kidun** were added from the UDHR test. So the lexicon isn't capped. But concede the evidence: UDHR went from 77% to 90% after adding words, and its results list missing words still lost (nationality, justice, religion, principle, international, natural, competent; `tests/udhr-01/results.md`). The French review flags **lite pi nosen** "way of God" as excluding non-theistic religions (`relecture-fr.md` G4), which is A4 F11's point as well. A5 calls 524 roots "reasonably lean … right-sized" (contradiction, below). *Fix:* A3's measurement (syllables and paraphrase error at 500/1,000/1,500 roots on chat, news and instructions), with human readers if possible. Meanwhile add "religion" as a root or as "way of belief". Cost: test time; roots as earned.
- **A6 vocabulary tests 01–05: concede.** The stop condition ("two tests losing <1 point", met at 445 roots) was run with AI translators, who circumlocute expertly. The UDHR losses above show it fired early. *Fix:* drop the stop condition until a human or harder-register test supports it.

### G9. Typology and B5 leakage (A4)

- **A4 F4 (stranding): partly.**
  - *Defend:* this isn't English P-stranding by movement. The language has no movement (reference 1.2: "Words never move"), and the stranded word is just the general rule that a relation word may drop an object that context supplies (4.4: "**wo** 'after that'"). The extra rule cost is small, as A3 2.7 also says. **pi wan** for "whose" shows retention is already a known pattern.
  - *Concede:* it's a minority strategy in WALS 123A, and A4's retention form (**kemu man to nume mon bu**) isn't forbidden but isn't named as the clear form.
  - *Fix:* list retention as the precise form beside stranding. Cost: one example.
- **A4 F5 (fa): partly.**
  - *Concede:* the B3 gap is real. **mu … fa** has no stated reading. Negative indefinites without verbal negation are an SAE minority (WALS 115A, 11/206).
  - *Defend:* the world-majority form already works (**ewo bo mu …**), and **fa** is mainly a quantity word.
  - *Fix:* state that **mu … fa** is a single (concord) negation, which matches principle 5's "doubled **mu** … never means 'not not'" and the WALS majority. Cost: one sentence.
- **A4 F6 (gun): defend.** The headline misreads the reference. Adjective predication does *not* need the copula: reference 4.2 says "A bare noun followed by a word (**guyi kudu**, **ewo niba**) may be a description or a statement. Context decides", and 4.5 gives "**bi upe.** 'very good.'". **gun** is the clear form, as Mandarin's 很 is (rationale 10, last paragraph). That's already A4's own "direction". **gun** + action word as undergoer state is the copula > passive path that A7 F1 predicts natives would grow anyway, and it was chosen over a new passive word in a full grammar space (design log "gun + an action word"). Small concession: the feeler trap (**to gun nuta** "I am feared") is a learnability cost worth a learn.md warning.
- **A4 F7 (reference systems): partly.**
  - *Defend:* A5 counted **yi** 12 times and **sun** 3 in the UDHR, "doing real disambiguating work". Clusivity is among the most stable features (Greenhill 2017, verified by A6 C27).
  - *Concede:* "A newcomer is **yi** … until the speaker makes them the topic" (reference 10.3) reads as a rule. It should be a default. There is also no neutral "we".
  - *Fix:* reword the newcomer sentence. A neutral "we" would cost a word in a full space, so leave it, with an add-back trigger: speakers misusing **pen**/**din** in a corpus.
- **A4 F8 (isolating type): partly.**
  - *Defend:* the choice is documented. Rationale 4.2 says "Why particles, not inflection".
  - *Concede:* its stated support is two of A6's three wrong claims (C15, C18). The honest reason, "one coherent head-initial type, because majority-per-feature is incoherent" (A4's own words), isn't written anywhere.
  - Against A4's "favours adults": A7 judges the same profile the one natives push toward (contradiction, below).
  - *Fix:* replace the rationale sentence with A4's. Cost: wording.
- **A4 F10 (C1 not shown): partly.**
  - *Defend:* "almost no choice cites cross-linguistic evidence" reflects the packet A4 was given. The rationale cites evidence per decision, and A6 checked 52 such claims (24 verified, 0 fabricated).
  - *Concede:* the reference itself says "senses that most language families lump together: **apu**" (§14), and the rationale's own figure is 50.2%, i.e. "about half". A6 C36 couldn't reproduce the figure.
  - *Fix:* change "most" to "about half", and recompute (see C36).

### G10. Complexity (A5)

- **A5 3 (doubling): partly.** Principle 5 says "widens *or* strengthens". Taking that literally, **mu mu**, **nun nun**, **yo yo** (emergency is a stronger warning, not another act) and **feko feko** strengthen, and **genso genso** widens scope. "Never not-not" is a clarification that the rule strengthens, not a carve-out. **nen nen** "each other" is the real idiom: reflexive → reciprocal is a common path (A7 F15), but it can't be predicted from "widen or strengthen". *Fix:* list **nen nen** as a lexicalised double. Cost: none.
- **A5 4 (unattested machinery): defend.** The UDHR is legal register, as A5 itself cautions. The design has casual-register evidence A5 didn't see:
  - regression test 01, English chat and Indonesian workplace chat: "120 of 121 feature uses survived and none were misread";
  - the Japanese casual round trip: **a** ×3, **buni** ×2, **o**, **fe**, all read back right (`tests/grammar-rebuild/roundtrip/`);
  - the multilanguage retest (G7).

  The Restraint review kept these as "optional precision systems … since they cost nothing unused". The weakness is that all of these readers were AI (#41–42).
- **A5 6 (patches): partly.** **tun** for a recipient isn't a patch: it's ordinary dative marking, and A7 F9 predicts natives will generalise it. A5's direction (a bare determiner after a verb always counts as the thing) would itself be a new attachment rule. Concede the existential (see A7 F8 in G6). The bare noun + word ambiguity is the deliberate economy default (rationale 10, last paragraph).
- **A5 7 (sin): defend.** This misreads one meaning as three. Reference 8.1: "**sin** means done. With no frame set it reads as past. Inside a past frame it marks something already done by that time … inside a future frame it is 'will have'". "Done by the reference time" is one relative-tense meaning, the creole anterior (Bickerton). A learner who knows the frame rule predicts all three. Concede only the stipulation "**sin** and **le** don't combine". A7 F1 predicts natives will combine them (Guyanese *bin a*), and the reference could allow it as "had been doing".

### G11. Phonology prior and SVO (A3)

- **A3 5.3: partly.**
  - *Defend:* the shared forms A3 cites as evidence of a Toki Pona prior weren't chosen by hand. Rationale 3.5 says "Forms are never hand-picked". The v0 optimiser gave OF = **yo**, and the drift rebuild later assigned **pi**. **pi** was kept despite an offensive match "because no free one-syllable form exists" (rationale 3.6). The inventory came from `build.py scale` at 3,000 roots and Miller & Nicely.
  - *Concede:* the (C)V(n) / 13-consonant profile was Claude's choice, all four designers are Claude-family models, and A1's proposed test (word length and confusability at 13 vs about 20 consonants) hasn't been run.
  - *Fix:* run `build.py scale` with an extended inventory. Cost: compute only.
- **A3 5.4: partly.** It's true that no experiment tests SVO without case here. But the choice has independent support beyond the shared prior: Greenberg U41 (SOV languages usually have case), and Gibson et al. 2013's noisy-channel account. A4 scores it "Pass, justified" (contradiction, below). A8's artificial-language study is the right test, and it's expensive. Keep SVO pending that study.

### G12. pi, manni/konsin, manner slot (A7)

- **A7 F4: partly.**
  - *Concede:* A7's minimal pairs are real. **dili oma** "seven days" vs **dili pi oma** "Sunday", and **dunan yawu** vs **dunan pi yawu**, rest on one unstressed, frequent linker.
  - *Defend:* the design rejected a separate weekday head because **nelon pi ka** would collide (design log "dili pi + 1–7"). A7's alternative (number before the noun for labels) breaks the N-Num order A4 and A7 both praise.
  - *Fix:* none now. Add "**pi** reduction merging labels with counts" to drift.md's watch list, with the fallback of a stressed label word. Cost: none until it fires.
- **A7 F5: concede.** **konsin** is literally **kon** + **sin**, and both **konsin** and **kon** take a number (**konsin te** vs **kon te**). **manni** and **man** both come between a noun and a verb (**ewo manni niba** vs **ewo man niba**). Clipping of grammaticalising words is ordinary (*baimbai > bai*). *Fix:* re-coin both with `words.py --avoid`, and add a juncture rule: a two-syllable operator's first syllable may not be a grammar word in a compatible slot. Cost: two words, both tier 1–3.
- **A7 F7: partly.**
  - *Defend:* V-manner-O was chosen so that a word after the object always describes the object (design log, learner guide aligned). That's a deterministic rule, and the clear forms exist.
  - *Concede:*
    - V-Adv-O is a minority order (A4 F21).
    - Verb–object bonding is strong in acquisition.
    - learn.md lesson 14 contradicts the reference: it lists "who gets it, then what" (item 9) before "how" (item 10), where the reference has manner before objects (A3 3.8 and A4 F21 also catch this).
  - *Fix:* first fix learn.md. Whether to flip the default should be tested on which reading is more frequent after an object.

### G13. A6 claims and internal tests

- **C15, C18: concede.** Modern Hebrew stayed inflected, and Esperanto is agglutinative. Drop both sentences (drift.md "What's already drift-resistant"; rationale 4.1 and 4.2). The RUNBOOK already defers the fix. The decisions resting on them need the reason G9/F8 gives instead.
- **C17: concede.** Bergen's eight children show transfer more than nativisation, and they didn't keep aspect. Rationale 4.6 ("native speakers and creoles keep preverbal aspect") should cite creoles only.
- **C19: partly.** The incidents are real, and A6's own helper finds "evidence supports explicit lexical marking". "Melody alone fails in noise" is extrapolated. Keep the particle on the B4 argument (speech and writing must carry the same thing), and reword the citation.
- **C29: partly.** Concede the wording: pronouns are among the slowest items. The design applies one rule to all one-syllable words, so no rule changes.
- **C31: partly.** Concede that verb drop isn't licensed in Mandarin, Japanese or Korean main clauses. The rule's actual examples are fragments (**muyi yu? moti?**), and fragments exist in every language, which A6 itself notes for English. *Fix:* cite fragment answers, not those three languages.
- **C32: concede.** Delete "every 150–300 years" (rationale 4.7, drift.md item 2). The decision stands on WALS 45 (C41, verified).
- **C36: partly.** Concede: recompute the family-balanced rates with `tools/clics_rates.awk`, since 50.2% is on the cut line. Low stakes: under the method's own 20–50% band, "language" would be built from **apu**, so the name would change only in length.
- **C44: concede.** ICAO's two-syllable digits are for distinctness, not burst survival. The 6–9 decision really rests on "no free one-syllable form" (design log, base 10), so the ICAO line should go from grammar-rebuild-spec.
- **C51: partly.** Concede "most"/"major" overclaims. The choices match the majority of the languages cited.
- **Confusion model unvalidated (#39): concede.** It's disclosed in rationale §11.1 and §3.2, but B2 is a guarantee, and every form in the language was chosen with this model. My checks above show it also disagrees with its own published digit figure. *Fix:* a human listening test, following rationale 9.4's own lesson ("use a human reader … with a carrier phrase"), on the pairs in my table. Cost: recruiting listeners. This is the single most valuable test the project hasn't run.
- **Base transmission test (#40): concede**, and it's worse than A6 says: the current model gives the 0–5 set 0.0185, not 0.0002. *Fix:* re-run, or withdraw the absolute numbers from number-base.md and the rationale.
- **Economy test 01 (#41): partly.** The readers were AI. But regression test 01 also used Indonesian-prompted texts, and the comma and nesting tests point the same way. The finding "no loss detected" is what was claimed. Human readers are the fix.
- **Multilanguage test 01 (#42): partly.** It shouldn't be cited as typology (rationale 10: "all 11 languages flagged stance"). Where it matters, use WALS-type data: C41 and C42 already do. It remains valid as a functional test: did the round trip carry respect and stance?

---

## Contradictions between reviews

1. **Lexicon size:** A3 4.1 "too small, grow to ~1,000" vs A5 "reasonably lean … right-sized; the size problem is in grammar machinery".
2. **yi and sun:** A4 F7 says replace **yi**, it's additions begetting additions. A5 F10 says the reverse: "the one 'exotic' system with the best evidence of earning its keep" (12 and 3 uses). A7 F15 predicts children may *strengthen* **yi**.
3. **gun + verb:** A4 F6 calls it SAE leakage. A7 F1/F18 treat copula > passive as the natural path natives take, and A7 §7 praises "zero copula tolerated".
4. **The isolating profile:** A4 F8 says it favours adult learners (against N2). A7 §7 says it's "already in the state three generations of natives would push … toward" and lists it among the choices that help acquisition.
5. **SVO:** A3 5.4 rates it medium, "untested shared prior". A4's scorecard says "Pass, justified (no case; Greenberg U41; Gibson et al. 2013)".
6. **Which pairs are fragile:** A3 2.1 and 4.2 rank consonant-only pairs (fa/sa, po/bo) above vowel-only ones ("vowel-only pairs are more robust"). A5 1 rates the vowel-only sets as the high-severity problem. A7 F3 ranks glide-only and voicing pairs as merging first. The design's model sides with A3 on **fa/sa**, with A7 on glides, and against A7 on voicing under noise.
7. **Severity of confidence-in-sixths:** high (A4 F2) vs low (A3 3.2, A7 F13).
8. **The imperative:** A3 3.3 keeps **tin** ("serves B4 directly"); A7 F6 and A4 F20 say bare commands will win.
9. **Size of the senary set:** "~34 words" (A3, A4) vs "29 roots" (A5). The lexicon has 30 rows: 20 unit, 9 senary number words, **senali**. A5's own totals also don't add up ("Medium 5" with four medium findings listed).

## Findings that rest on a misreading

- **A4 F6** "Adjective predication needs the copula". Reference 4.2: "A bare noun followed by a word (**guyi kudu**, **ewo niba**) may be a description or a statement. Context decides, and the clear forms above remove any doubt." Reference 4.5: "With **gun** left out too, a bare state is fine: **bi upe.**"
- **A4 F9** "every act gets a compulsory particle … 7 obligatory illocution particles". Reference 7.1: "A statement has no particle." Reference 4.2: "A command needs **tin**, or **so** for a request." Only directives require one, and questions can do without **min** (4.8: "Question words … need no **min**").
- **A3 2.4** "prescribing … which stance particles exist". Reference 7.2: "Other words used in this position are stance words too."
- **A3 2.1** "the (C)V(n) template allows 140 monosyllables and only 67 are used. That's false." It ignores the design's own constraints. Rationale 4.2: "the space is full (with 13 consonants, 5 vowels, ±n, minus digits, same-slot and -n rules)".
- **A5 7** "sin … three readings". Reference 8.1 defines one meaning, "done", relative to the frame.
- **A5 3** "yo yo = a different speech-act, not 'more warning'; genso genso = scope change, not intensity". Principle 5 reads "Doubling widens or strengthens". Scope is widening, and an emergency is a stronger warning.
- **A4 F3** "a senary calendar … inside the core language". measurement.md: "Apupiwe's own numbers are base 10 … senary is a topic the language can talk about … not a system built into it". Reference 8.3 uses today's calendar.
- **A4 F10** and **A5 4** treat the packet's silence as the design's silence. The rationale and tests contain the evidence; A6 audited 52 cited claims. Neither reviewer could see them, so this is a scoping artefact more than an error.

C4 (added after the reviews) doesn't overturn any finding. It reinforces the "observation, not theory" rule (rationale 5.4) and is consistent with A4 F11's point about **lite pi nosen**.

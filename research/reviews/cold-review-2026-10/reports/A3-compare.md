# A3: Three designs vs the built language

## Severity totals

43 findings: **3 high, 7 medium, 33 low.**

- **High:** 2.1 digits and short grammar words too close (fa/sa, sa/ka/da); 2.3 relative-clause closure and other grammar carried only by pauses; 3.1 the senary measurement system (against L3; it distorts the digits).
- **Medium:** 2.2 no future/irrealis marker; 2.4 pragmatics prescribed instead of left to use; 2.6 vowel-only packing of unstressed grammar words plus a ban on reduction; 4.1 lexicon too small (483 roots); 5.3 the Toki Pona-like phonotactic prior; 5.4 SVO without case is untested; 5.12 loans adapted from English pronunciation (awuwa fails L4).
- **Directions:** delete 1 (3.1, with the digit set rebuilt as a result); repair or trim 14; keep 28.
Inputs: goal.md; A1-design.md, A2-design.md, A8-design-zh.md (read in Chinese); the built language ("apu pi we") in packets/language/.

Method notes:
- All four authors are Claude-family models. Agreement is weighted by the external evidence each gives, not by count.
- Quantitative claims about the built lexicon come from a script over lexicon.tsv (548 entries), grammar.tsv (61 grammar words) and numbers.tsv. "Single-feature pair" means two words of equal length that differ in one consonant by only one of place, manner or voicing.
- The built reference points to measurement.md, vocabulary-method.md and dictionary.md. These are not in the packet, so the senary system and the root-form method are judged only by what language.md, learn.md and the TSVs show.

## 1. Decision table

| Decision | A1 | A2 | A8 | Built |
|---|---|---|---|---|
| Vowels | a e i o u | a e i o u | a e i o u | a e i o u |
| Consonants | 13: p t k b d g f s m n l w y; no h; l/r one phoneme | ~16: p t k b d g m n s f h l r w j; l/r contrast; avoid voicing-only contrasts | 14: A1's set + h; l/r merged; voicing realisation loose; avoid place-only contrasts | 13: identical to A1 |
| Syllable | (C)V(n), no clusters | (C)V(C), coda nasal or s, no clusters | CV(n), onset required | (C)V(n); onsetless only word-initially |
| Stress / tone | Fixed root-initial; no tone | Fixed (e.g. penultimate); no tone | Content-word initial, function words unstressed; no tone | Content-word initial as pitch, grammar words unstressed, digits 0-5 stressed; no tone; declination specified |
| Word-form rules | Length by information content; within class no single confusable feature among top ~2,000; digits, negation and yes/no maximally distinct; sound-symbolism tie-break; C3 last | Zipf; frequent short words differ by more than one weak feature | ~50 monosyllabic function words, ~1,000 disyllabic roots; ≥2 segments apart or non-place difference; antonyms fully distinct; digits ≥2 segments apart | Grammar words 1 syllable, content ≥2; no content word may start with a 0-5 digit syllable. Content roots well spread (4 single-feature pairs in 548); grammar words and digits densely packed (section 2.1) |
| Vocabulary sourcing and size | A priori forms; NSM primes + Leipzig-Jakarta + C1 test; 1,000-1,500 roots | NSM primes as core, the rest by derivation; no number | A priori; NSM + LJ100 + frequent concepts + 6-8 Berlin-Kay colours; CLICS colexification; ~1,000 roots | A priori; 483 roots + 23 loans + ~34 senary/unit words; Swadesh-type core; 6 colours; colexification (apu "word; language", dunan "month; moon") |
| Word order | SVO | SVO | SVO | SVO |
| Modifier order | N-Adj, N-Gen, N-Rel, but Dem Num N | One fixed position (unspecified) | All postnominal: N Adj Num Dem Rel | N Adj Num la Det pi-phrase Rel (= A8) |
| Case | None; optional object marker only for fronting | None | None; optional object marker for fronting | None; no fronting at all; topic by **pi X** + pause |
| Tense / aspect / mood | Optional preverbal mood-tense-aspect; past, future; perfective, progressive, habitual; optional evidentials | Optional stackable particles incl. past, future, perfect, progressive | Optional tense (past/future), mood, aspect; optional evidentials | **No tense markers**: time frame set by time words; aspect sin/le/buntu/manni; modality by verbs; confidence **kon** in sixths; evidentials |
| Polar questions | Final particle | Fixed-position particle | Final particle | **Initial** particle **min**; final **min** is a "right?" tag |
| Content questions | In situ; Q + generic noun | In situ; one root + affixes | In situ; Q + category | In situ; category noun + **yu** |
| Negation | Preverbal; scope by position; negative concord left to use | One particle immediately before verb | Before the negated constituent; no negative concord | **mu** before any phrase; **mu mu** defined as emphasis |
| Pronouns | 1/2/3, no gender, plural by rule, clusivity, one reflexive-logophoric "self"; politeness not grammatical | 1/2/3 × sg/pl + clusivity | 1/2/3 × number, clusivity, no gender or honorifics | to, me, pen/din, wan (human topic), yi (obviative), bu (thing), sun (logophoric), go (generic), nen (self); number-neutral "you" |
| Relative clauses | Invariant particle; gaps for S/O, resumptive pronouns otherwise | One uniform strategy down the hierarchy | Invariant particle; gaps S/O, resumptive for obliques | **man**; gaps for S/O; obliques by **stranded relation word** (kemu man to nume mon); resumptive only for "whose"; closed only by a pause |
| Word-building | Head-first compounds + ~15 suffixes | Agglutinative affixes + compounding | Head-first compounds + ~10 derivational elements | 4 preposed phrasal markers (no, ge, du, pu); bare N+N compounds **banned** except a list; relations via **pi** or **man** |
| Numbers | Decimal; 10/100/1000 roots; SI prefixes above; digits strictest distinctness | Decimal, transparent | Decimal; 10/100/1000 roots; "milion"; digits ≥2 segments apart | Decimal reading, a priori tonen/siwin; digits 0-5 one syllable, 6-9 two; **plus an optional senary measurement system** |
| Writing | Latin, 18 ASCII letters, y for /j/, capitals mark names | Latin, shallow 1:1 | Latin, 19 letters, y for /j/ | Latin, 18 letters (= A1); lowercase; names marked by the word **en**; comma is grammatical |
| Precision vs economy | Economy by default, explicit optional markers; grouping linker for bracketing | Same | Same; circumfix-type scope particles | Same principle; bracketing and clause closure carried by pauses |
| Left undefined | Phonetic detail, reductions, idiom, register, discourse particles, politeness, lexicalisation | Lexicon beyond core, idiom, register, politeness, accent | Style, idiom, discourse particles, politeness, reduplication meaning, address customs | Little: politeness particle, title, stance particles, greetings, reduplication, interjections and clock styles are all specified |
| Drift strategy | No academy; wide margins; nothing irregular; start at typological attractors | No academy; regularity | No academy; margins; pre-allow common sound changes; allow grammaticalisation | No academy stated; harmless variants pre-allowed (= A8); fusion allowed once it changes sound; but "every syllable keeps its full vowel" and "grammar words keep their consonants" |

## 2. All three designs agree and the built language differs

### 2.1 Distinctness of digits and short grammar words: built is wrong in part. Severity high. Repair.
- **Designs:** each sets a stricter distinctness rule for the short, frequent, low-context words. A1 says digits, negation and yes/no must be maximally distinct. A2 says frequent short words must differ by more than one weak feature. A8 says digits must be at least two segments apart, and words in the same slot two segments apart or by a non-place feature.
- **Built:** the content roots honour this well. Only 4 of the 548 entries form single-feature consonant pairs (kudu/gudu "big/liver", duko/tuko "turn/start", gisu/kisu, soto/foto). The grammar words and digits don't. Among the 71 monosyllabic grammar words and digits, 61 pairs differ by one vowel only, and several pairs share a slot:
  - **fa** "none" vs **sa** "2". Both follow a noun and both can stand alone: **to ibe totu fa** "I have no dogs" vs **to ibe totu sa** "I have two dogs". They differ in f/s place only. That is the confusion spelling alphabets exist to prevent on phone lines.
  - Digits **sa ka da** (2 3 4) share the vowel a and differ only in the consonant. Digit strings (phone numbers, codes, years, 24-hour times) have no context to repair them. That is A1's exact argument, and the reason the English digits five and nine, which share a vowel, are the classic radio confusion ("fife", "niner").
  - **po** "0" vs **bo** "unspecified" (voicing only), both after a noun.
- **The built language's own reason:** 0-5 got stressed monosyllables, and learn.md says 6-9 have two syllables "because the language ran out of short sounds". That's false. The (C)V(n) template allows 140 monosyllables and only 67 are used. The real cause is the senary system (3.1).
- **Evidence:** Miller & Nicely (1955) and Lovitt & Allen (2006) disagree on which feature is weakest (section 4.2), but both find that single-feature consonant pairs under noise are the main confusion source. Vowel-only pairs are more robust. So the dense vowel-only packing is a smaller problem (2.6) than the consonant-only digit and slot clashes.
- **Direction:** B2 is a guarantee, so this needs repair, not trading off. Give the ten digits ten monosyllables at least two features apart and avoid same-vowel runs. Free monosyllables exist. Move **fa** to a form far from every digit.

### 2.2 No tense or future marker at all: built has a partial reason. Severity medium. Repair.
- **Designs:** all three include optional tense particles, at least past and future.
- **Built:** no tense words. A time word or the first **sin** sets a frame, and **sin** with no frame reads as past. For the past, this is a good design. It is the Mandarin/Yoruba pattern, it saves repetition in narrative (B8), and **sin** covers most needs.
- **The gap is the future.** There is no general "will". A bare future is said by a time word, context or **buntu** "about to", and **de** is restricted to the speaker's own commitment. "She will come (some time)" needs a periphrasis such as **wo** + anchor. So B3 is met, but awkwardly, for a very frequent meaning.
- **Evidence:** a preverbal future/irrealis particle is close to universal in creoles: Bickerton's TMA core; APiCS, e.g. Louisiana Creole *a/va/ale* future and Palenquero *aké* irrealis. It is also common in "tenseless" languages: Indonesian *akan*, Mandarin *huì/yào*. This is the strongest convergence on any TAM marker after aspect.
- **Direction:** add one optional future/irrealis particle from the unused monosyllables. Keep the frame rule for the past.

### 2.3 Grammar carried by pauses: built is wrong where a guarantee depends on it. Severity high. Repair.
- **Designs:** A1 makes B4 a grammar rule ("anything that changes meaning is carried by a word, never by intonation"), and adds an optional grouping linker for bracketing. A8 puts questions and focus in words and adds frame particles for coordination scope. A2 picks particles over intonation for B4.
- **Built:** a pause, written as a comma, is the only device for several jobs:
  - closing a relative clause ("no word closes a relative clause; a pause closes it, along with every relative clause still open");
  - ending a phrasal derived word before its verb;
  - ending a topic;
  - separating a called name from a subject;
  - the choice tag **, yu** (without the pause it reads "which X").
  At the same time, "in casual writing, pauses that context makes obvious may be dropped". The fallback for precision is restructuring ("use a new sentence").
- **Evidence:** speakers don't reliably produce disambiguating prosody unless they are aware of the ambiguity (Snedeker & Trueswell 2003; Kraljic & Brennan 2005 report mixed prior evidence). Online writing drops commas freely. So the speech channel and the casual-writing channel are both unreliable for exactly these boundaries.
- **The built language's reason** is economy: no closer word costs nothing when unneeded. That serves B8, but B3 and B4 are guarantees.
- **Direction:** keep the pause as the cheap default, and add one optional closing particle for relative clauses and phrasal derived words, as the precise form. It is the same "precision on demand" pattern the built language uses everywhere else.

### 2.4 Politeness, discourse particles and routines specified rather than left to use: built overreaches. Severity medium. Repair (trim).
- **Designs:** all three leave politeness, register and discourse particles to the host culture and to use (A1 §6, A2 §6, A8 §6; goal C2, L2, N4).
- **Built:** under its own principle 6, "every social pressure has its own word", it specifies:
  - **nun** and **nun nun**, and the title **lanno**;
  - the stance words **a**, **buni** and **donon**, and their order;
  - greetings, thanks and apology formulas;
  - pragmatic rules such as "being polite never means hinting" and "in an emergency no **nun** is expected".
- **Source check:** principle 6 traces to no criterion in the goal. It is the builder's own requirement, the category the user's rules call most dangerous.
- **What earns its place:** a single politeness particle is cheap and widely attested (Tagalog *po*, Thai *khráp/khâ*, Korean *-yo*). Keeping politeness separate from the speech act protects B1 for warnings. Keep **nun** and **lanno**.
- **What doesn't:** prescribing how cultures may hint, or which stance particles exist, conflicts with L2 and C2 (carry the cultures' conventions) and with B9/N4 (don't control use).
- **Direction:** delete the pragmatic prescriptions. Mark **a**, **buni** and **donon** as provisional, to be replaced by whatever speakers grow. Add-back trigger: field evidence that softened warnings are actually misread.

### 2.5 Productive noun+noun compounding banned: built has a reason, but pays too much. Severity low. Repair.
- **Designs:** all three grow vocabulary mainly by head-first compounding.
- **Built:** "Noun + noun is used only for gender and for the compounds in compounds.tsv", and other relations need **pi** ("house key" = **tinli pi guyi**).
- **Reason:** with class-free roots, N + word reads as head + modifier, so N+N relations would be ambiguous (B3). But N + content word is already productive (**noso gake** "turtle", **muyi tikun** "summer"), so the ban only adds a **pi** syllable to every noun-noun relation (B8).
- **Evidence:** Mandarin, Thai and Vietnamese use bare N+N compounds massively, with the relation left to context.
- **Direction:** allow bare N+N as a loose "associated with" compound, with **pi** or **man** as the precise form.

### 2.6 Dense vowel-only packing of unstressed grammar words, and a ban on reduction: built is fragile under B9. Severity medium. Repair.
- **Designs:** A8's rule (two segments apart in the same slot) and A2's rule would forbid it. A1's "wide margins" drift argument assumes it away.
- **Built:**
  - Grammar words are unstressed by rule, and 61 of the pairs among them differ by one vowel.
  - Same-slot cases: **wan la isi** "they go" vs **wan le isi** "he is going". With the subject dropped, **mu obu** "(I) don't come" vs **me obu** "you come". Also **sin/sun** before the verb.
  - The language forbids vowel reduction ("every syllable keeps its full vowel"). But reduction of unstressed function-word vowels is among the most regular sound changes there are, so this rule tries to control the change B9 says the language must survive.
- **Counter-evidence:** Japanese case particles (*wa ga no ni de to mo e o*) are packed the same way and survive. Slot position does most of the disambiguation.
- **Direction:** this is not urgent. Re-space the few same-slot vowel-only pairs (la/le, mu/me) when 2.1 is repaired, and delete the ban on reduction. Add-back trigger: none, since the guarantee should come from spacing, not from a pronunciation rule.

### 2.7 Oblique relatives by preposition stranding: built is unusual. Severity low. Repair.
- **Designs:** A1 and A8 use resumptive pronouns for obliques, citing Keenan-Comrie. A2 wants one uniform strategy.
- **Built:**
  - Obliques strand the relation word at the end of the clause (**yetu man to fonsu gan** "the tool I cut with").
  - The stranded word must end its clause or come before a pause, which is one more rule.
  - "Whose" alone uses a resumptive (**pi wan**).
- **Evidence:** preposition stranding is rare (mostly English and Scandinavian, plus a few Niger-Congo languages). Resumptives in low hierarchy positions are the common strategy.
- **The built language's reason:** stranding is just its general rule that a relation word may drop its object, so the extra cost is small.
- **Direction:** make the resumptive (**gan bu**, **mon bu**) the standard precise form, matching **pi wan**. Allow stranding as the casual form.

## 3. Parts of the built language that none of the designs needed

### 3.1 The senary measurement system. Severity high. Propose deletion; rebuild the digits.
- **What it is:**
  - 20 native unit roots: **nane** time, **fomi** mass, **yoke** charge, **sigi** temperature interval, and so on to **masin**.
  - 12 senary number words: **nobi**, **miko**, **niyu**, **yiyo**, **gife**, **yuli**, **kufe**, **bafo**, **genwi**, and others.
  - **senali**, and **boyo** "36-day block".
  - A `₆` notation and a senary calendar in measurement.md, which isn't in the packet.
  - About 34 words, roughly 6% of the lexicon, for a system language.md itself calls optional and says measurement does not use ("Measurements use borrowed international unit names").
- **Against the goal:**
  - L3 is a hard limit: where an international standard exists, follow it. SI and decimal are that standard.
  - B5: no language family measures this way.
  - C1: every word is learning cost with no everyday saving, since ordinary speech is told not to use it.
- **It distorts the rest of the language (path dependence):**
  - digits 0-5 are stressed monosyllables and 6-9 are disyllables (**ufo oma kefi mape**). That puts a syllable cost on 40% of decimal digits, in phone numbers and years read digit by digit;
  - only the six onsets **po fi sa ka da te** are barred from content words;
  - confidence is counted in sixths (3.2);
  - learn.md gives a false rationale ("ran out of short sounds").
- **Direction:** delete the senary roots, notation and calendar, and give 0-9 ten equal, well-separated monosyllables (2.1). Add-back trigger: a real speaker community adopting senary measurement, which L3 makes unlikely ever to justify core status.

### 3.2 Confidence as a number of sixths (kon + digit). Severity low. Repair.
- **No design has this.** A1 and A8 have mood and evidentials.
- **For it:** it is cheap (one particle that reuses the digits), and it gives B3 a precise graded form.
- **Against it:** sixths are a senary artefact. No culture grades belief in sixths. Natural epistemic systems use 3-4 lexical steps (maybe, probably, surely), and the world standard for exact chance is percent or 0-1, which the language already has (**pasentu**).
- **Direction:** keep **kon**, but decouple it from sixths. Use a few step words, or tenths, plus **pasentu** for exact values.

### 3.3 Seven speech-act particles, with "tin" required for commands. Severity low. Keep, and flag fon/yo/de for possible deletion.
- **Designs:** only a question particle.
- **Built:** commands, requests, advice, commitments, warnings and exclamations each have a particle, and a bare verb is a statement.
- **For it:** this serves B4 directly (no reliance on imperative intonation), and imperatives are cross-linguistically marked anyway, so **tin** and **so** earn their place.
- **Against fon, yo and de:** grammaticalised advice, warning and commissive particles are rare, and the verbs "advise", "warn" and "promise" would do (B3).
- **Direction:** propose deleting **fon**, **yo** (keep **yo yo** as an emergency interjection) and **de**. Add-back trigger: communication tests showing warnings or commitments misread without them.

### 3.4 Pronoun extras: obviative yi, the human/thing split, generic go, logophoric sun. Severity low. Keep the words; trim the rule.
- **Designs:** A1 has one combined reflexive-logophoric. None has an obviative or an animacy split.
- **For them:**
  - **wan/bu** follows a very common split (English he/she vs it).
  - **go** removes the generic-"you" ambiguity cheaply.
  - **sun** is attested (West African logophorics) and resolves "she said she…".
- **The cost is in yi:** "a newcomer is **yi** until the speaker makes them the topic" is a discourse-management rule that speakers will not apply consistently (N4). Proximate/obviative systems (Algonquian) are rare.
- **Direction:** keep **yi** as "the other one". Drop the newcomer prescription.

### 3.5 No words for yes and no. Severity low. Keep.
- **Designs:** A1 and A8 both assume yes/no words exist (A1 wants them maximally distinct; A8 lists 是/否 as antonyms to keep apart).
- **Built:** answers echo the verb.
- **Evidence:** echo answers are well attested (Mandarin, Irish, Welsh, Finnish, Latin), and they avoid the yes/no ambiguity after negative questions (B1).
- **Expectation:** speakers will use **ok** or **mm** as "yes" anyway, since interjections pass through. That is fine under B9.

### 3.6 Fixed meanings for doubling, no apposition, a 14-slot template. Severity low. Trim.
- **Doubling:** A8 explicitly leaves the meaning of reduplication undefined. The built language defines a general "widen/strengthen" meaning plus idiomatic cases (**nen nen** "each other", **genso genso** "the whole turn", **yo yo**). The general rule is fine. The idioms belong in usage (N4).
- **"There is no apposition":** this prescription will be ignored by native speakers. Allow apposition after a pause.
- **The 14-slot template:** it describes the order, and costs little.

### 3.7 Clock, calendar, date and pass-through notation rules. Severity low. Keep.
- None of the designs went this far (A1 named ISO 8601, 24-hour time and SI).
- The built rules carry local clock styles, use ISO weekday numbering and pass digits, units and handles through unchanged. That is L2, L3 and C2 applied directly, and it earns its place.

### 3.8 Internal inconsistencies and missing files. Severity low. Repair.
- learn.md lesson 14 puts manner after objects (slots 9 and 10). language.md 4.1 puts manner before objects, and 4.2 confirms it (**nawi yobe pasu**).
- learn.md's "ran out of short sounds" is false (3.1).
- language.md cites `../data/*.tsv`, but the files sit beside it.
- measurement.md, vocabulary-method.md, dictionary.md and examples.md are referenced but absent. The root-form method, so the B2 and C3 rules for roots, can't be audited.
- The UDHR page says "an the language word" (a find-and-replace artefact).

## 4. Where the designs disagree with each other

### 4.1 Vocabulary size. Severity medium. Repair: grow the core.
- **Options:** A1 1,000-1,500 roots by a C1 test. A8 about 1,000. A2 an NSM-prime core with derivation. The built language has 483 roots plus 23 loans.
- **Evidence:**
  - The built UDHR shows the cost of a small lexicon. Paraphrase is long, and it loses or bends meaning: "barbarous acts" becomes **musu bi yomo** "very bad things".
  - "Religion" becomes **lite pi nosen** "the way of God". That is a theistic framing that misfits non-theistic traditions, which is a B5/C2 fairness problem, not just a length problem.
  - Toki Pona's experience (~120-140 words) is the known endpoint: context does all the work, and B3 suffers.
  - C1's own test (paraphrase cost × frequency > learning cost of a root) favours roots for every concept frequent enough to recur in ordinary text.
- **The evidence favours** A1/A8's ~1,000.
- **What would settle it:** measure syllables per meaning and the paraphrase error rate on a sample of everyday text (chat, news, instructions) at 500, 1,000 and 1,500 roots.

### 4.2 Which consonant contrast is fragile: voicing (A2), place (A8) or both (A1). Severity low. Keep the built practice.
- **Evidence:** Miller & Nicely (1955) found voicing and nasality robust and place weakest. The Lovitt & Allen (2006) replication found voicing less robust and place more robust. Both are English-only.
- **The robust answer** is A1's, and the built content lexicon follows it: avoid any single-feature consonant pair among frequent words. The built grammar words and digits don't follow it (2.1).
- **What would settle it:** noise and phone-band confusion tests with listeners from several L1 families, on this inventory.

### 4.3 /h/ and l/r. Severity low. Keep.
- **Options:** A2 keeps h and contrasts l/r. A8 keeps h. A1 and the built language have neither.
- **Evidence:** l/r is a famous learner trap and is non-contrastive in many families. The built lexicon has spare room (4 single-feature pairs), so adding h would buy little. Keep.

### 4.4 Onsetless syllables. Severity low. Keep, watch.
- **Options:** A8 requires an onset for clearer word boundaries. The built language allows a vowel at the start of a word: 59 roots, plus **a o en in un**, some of them very frequent (**ewo**, **osa**, **upe**, **apu**).
- **Expected drift:** glottal-stop insertion at boundaries, which is harmless.
- **What would settle it:** word-segmentation tests in connected speech.

### 4.5 Stress on the first syllable (A1, A8, built) or the penultimate (A2). Severity low. Keep.
The two coincide on two-syllable roots, which are 529 of 548. Initial stress also marks word onsets for recognition (A8's cohort argument).

### 4.6 Demonstrative and numeral before the noun (A1) or after it (A8, built). Severity low. Keep.
- N-Adj-Num-Dem is the frequent mirror order (Greenberg's Universal 20).
- Consistent head-first order is one rule (B7).

### 4.7 Polar question particle: final (A1, A8) or initial (built). Severity low. Keep.
- **Evidence:** WALS 92A counts 314 final, 129 initial and 52 second-position particles out of 884 languages, so final is more common.
- **The built language's reason** is sound: the speech act comes first, so the listener parses the rest accordingly. Initial particles are well attested (e.g. Polish *czy*, Arabic *hal*). The final **min** tag already covers final placement, as a biased question.
- **What would settle it:** a comprehension-latency study. Low stakes.

### 4.8 Scope of negation: strictly preverbal (A2), or before any constituent (A1, A8, built). Severity low. Keep built.
- Constituent negation gives B3 scope precision at no cost.
- On doubling, A1 leaves negative concord to use, A8 forbids it and the built language defines it as emphasis. All three are defensible. A1's position fits B9 best.

### 4.9 Derivation: suffixes (A1), affixes (A2, A8, position unspecified) or preposed phrasal markers (built). Severity low. Keep built.
- A1's 7:1 suffixing figure is driven largely by inflection and by OV languages.
- Head-initial isolating languages build nouns with preposed heads: Thai *nák-*, *khwaam-*, *kaan-*; Vietnamese *người*, *sự*. That is the built language's design, and it is consistent with its head-first order.
- The built language has only 4 markers, against 10-15 in the designs. It covers causatives with **muge** and diminutives with **meli**. Add-back trigger: a role that is paraphrased often in real text.

### 4.10 Opposites by affix (A1, A2) or by separate roots (A8, built). Severity low. Keep built.
- Antonyms occur in the same frames, so a one-syllable prefix would be the only cue between "big" and "small". Mishearing it flips the meaning with no contextual repair (A8's argument).
- **mu** + word stays available as "not X".

### 4.11 Large numbers: SI prefixes (A1), "milion" (A8), a priori tonen/siwin (built). Severity low. Keep built.
- "Million" is not world-shared: compare 百万/万, lakh/crore, Indonesian *juta*. So under L4, borrowing it is doubtful.
- **siwin** = 10⁹ sidesteps the long/short-scale conflict.

### 4.12 Proper names: capitals (A1), original spelling (A8), the word en (built). Severity low. Keep built.
- Capitals don't exist in speech. **en** marks a name in both channels (B4).

### 4.13 Evidentials: yes (A1, A8, built), not mentioned (A2). Severity low. Keep.
- They are optional, cost 3 words, and serve B3. In WALS 77A, 237 of 418 languages mark evidentiality grammatically.

### 4.14 Optional object marker for fronting (A1, A8), or no movement plus a pi-topic (built). Severity low. Keep built.
- The built language gets topicalisation without a new word: a **pi X** topic, with the role left in place.

## 5. Where all four agree, and how much that counts

Rule of thumb: agreement counts as evidence only as far as the external evidence behind it goes. Agreement that merely restates a goal clause (L3, L4) is not evidence. Agreement on a point all three designers listed as their *least* sure is a shared prior, not a finding.

### 5.1 Five vowels a e i o u. Strong. Severity low. Keep.
WALS 2A makes five the modal size, and dispersion theory explains why. The case would be the same without any model agreeing.

### 5.2 No lexical tone, fixed predictable stress. Strong for tone. Severity low. Keep.
- Tone needs diacritics in Latin script (L3, B4).
- It is hard for adult learners (B10).
- 58% of languages lack it (WALS 13A).
- N2 warns against favouring adults, but B4 and L3 alone carry this one.

### 5.3 Small inventory, (C)V(n), no clusters, merged l/r. Medium, and the most suspect agreement. Severity medium. Keep, but test.
- **The prior:** this phonotactic profile is essentially Toki Pona's: five vowels, p t k s m n l w j, (C)V(n). The built language adds voiced stops and f. Its genitive linker **pi**, with nearest-noun attachment, is Toki Pona's **pi**, and **la** and **en** are also Toki Pona words (with other meanings there). That points to a shared training prior, not to independent convergence.
- **The evidence:** the cited support (Coupé et al. 2019: about 39 bits/s across languages, so simple syllables are spoken faster) was measured on natural languages with typical inventories. It has not been tested at 13 consonants. A1 (#1) and A8 (#2) list this as a least-sure decision.
- **Cost so far:** built roots average 2.06 syllables, and the lexicon is uncrowded. So B8 is not yet visibly hurt. The pressure will come with a larger lexicon (4.1).
- **What would settle it:** A1's plan, i.e. model word length and noise confusability at 13 vs about 20 consonants, then run perception-in-noise tests.

### 5.4 SVO, no case, prepositions. Medium. Severity medium. Keep, test.
- **For it:** the evidence is real but indirect. Gibson et al. 2013 give a noisy-channel account. Creoles favour SVO. Bergen 2001 reports native Esperanto children dropping the accusative.
- **Against it:** SOV is more frequent (WALS 81A), and all three designers list this as their least-sure decision. Four-way agreement here is the shared prior.
- **What would settle it:** A8's proposed artificial-language learning studies with children, comparing caseless SVO with SOV plus one object marker, measuring misunderstanding rate and length in noise.

### 5.5 No gender, agreement or articles; optional plural; invariant words. Strong. Severity low. Keep.
WALS 30A and 33A support it, and so do B7 and the native-Esperanto evidence. Nothing here depends on the shared prior.

### 5.6 Postnominal adjectives and relative clauses with an invariant particle. Strong. Severity low. Keep.
WALS 87A and 90A support it, and one headedness rule serves B7.

### 5.7 In-situ question words built regularly from one root. Strong. Severity low. Keep.
WALS 93A supports it. The built forms (**ewo yu**, **mon kemu yu**) avoid A1's worry about a one-sound correlative grid, because the distinguishing part is a full root.

### 5.8 Inclusive/exclusive "we". Weak. Severity low. Keep, but treat as unproven.
- 63 of 200 languages make the distinction (WALS 39A), a minority.
- All the designs justify it with an *asserted* English ambiguity cost, never measured. A2 says so itself.
- This is a conlang-community favourite, so a prior is likely.
- The cost is small (two roots), but the choice is forced on every "we".
- **What would settle it:** count how often English or French "we" needs repair in real conversation.

### 5.9 Decimal, transparent numerals. Strong. Severity low. Keep.
L3 requires it, Miller et al. 1995 support transparent numerals, and WALS 131A shows decimal is most common. The built defect is the digit forms, not the system (2.1, 3.1).

### 5.10 Latin alphabet, one letter per sound, y for /j/, no diacritics. Required by L3, so agreement adds nothing. Severity low. Keep.
The y-for-/j/ argument (A1: shared across unrelated orthographies) is a good B5 point in its own right.

### 5.11 A priori root forms. Medium-low as evidence (it follows from L4 + N3). Severity low. Keep.
- **The untested cost:** adults get no familiar forms (A8 #4).
- **What would settle it:** A8's proposed cross-L1 word-learning experiment.

### 5.12 Loans only where the world shares a form, adapted by one fixed rule. A restatement of L4, but the built execution is flawed. Severity medium. Repair.
- **The flaw:** several built loans are adapted from *English pronunciation*, not from the cross-family shared form:
  - **kilamita** keeps the English reduced vowels (compare kilometr/kilómetro/キロメートル).
  - **pasentu**: much of the world says *procent/Prozent/процент*.
  - **awuwa** "hour" fails L4 outright. There is no world-shared form: heure, hora, Stunde, час, saa, ghanta, 小时, jam.
- **B8 hits on everyday words:** **ilekutulisiti** (7 syllables), **osupitalu**, **bayisikalu**.
- **Against B5 and N3** (one language's form taking the place of the world's).
- **Direction:** source each loan from the majority form across families, and cap length. Replace **awuwa** with a native or derived word (e.g. a time unit + number), since no shared form exists.

### 5.13 Economy by default, precision on demand. Moderate. Severity low. Keep.
- This is a reading of C1 and B3, so agreement is partly a restatement. It is also how isolating languages (Mandarin, Yoruba) work, and it fits Coupé's finding that speakers regulate density.
- The built language departs from it only where it uses pauses instead of an optional word (2.3).

### 5.14 Drift: no academy; regularity protects. Moderate, over-claimed. Severity low. Repair the claim.
- **What holds:** Hudson Kam & Newport 2005 supports children regularising inconsistent input.
- **What doesn't:** all four overreach in implying that a regular system gives drift "nothing to do". Phonetic erosion of unstressed function words and grammaticalisation happen regardless.
- **The tell:** the built language's ban on vowel reduction (2.6). It quietly tries to control exactly that change, against B9.
- A8's approach (pre-allow common changes, keep spacing) is the better reading of B9.

## Sources consulted
- WALS 92A (polar question particle positions), wals.info/chapter/92.
- Miller & Nicely 1955; Lovitt & Allen 2006, "50 years late: repeating Miller-Nicely 1955", Interspeech.
- Snedeker & Trueswell 2003, "Using prosody to avoid ambiguity"; Kraljic & Brennan 2005.
- APiCS (Louisiana Creole, Palenquero TMA), apics-online.info; Winford, creole TMA restructuring.
- Preposition stranding typology (English, Scandinavian, Vata, Gbadi).
- From memory, not re-checked this session: WALS 2A, 13A, 30A, 33A, 39A, 77A, 81A, 87A, 90A, 93A, 131A counts (as cited in the designs); Greenberg's Universal 20; Thai and Vietnamese nominalisers; Japanese particle inventory; Toki Pona's phonology and **pi**.

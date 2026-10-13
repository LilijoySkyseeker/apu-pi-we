# Boundary candidates against Ladder 1 (lexicon-ladder-01, part 2)

Proposals only; no word was changed. Ladder: `docs/vocabulary-method.md` §0, Ladder 1.

## Method

- **Scope.** I went through all 483 non-loan roots in `data/lexicon.tsv` and all 52 compounds. I read every gloss containing ";" or "," and decided whether it joins two senses or only fixes one (§14.2: a comma gloss fixes the sense). I also took the antonym pairs in `data/antonyms.tsv` into account, because a pair can show a sense the gloss hides (see *agi*).
- **Rung 4 data, recomputed.**
  - Source: CLICS⁴ v1.0, downloaded from Zenodo (record 19608447) to `/tmp/clics`.
  - Script: a Python port of `tools/clics_rates.awk` that reproduces the note's figures exactly: MOON/MONTH 69.6, LANGUAGE/WORD 50.2, TREE/WOOD 50.0, FINGER/TOE 15.7.
  - Mapping: I mapped 448 CLICS concepts to roots, using `data/concepts.tsv` plus gloss matching that I checked by hand.
  - Pairs: I computed **every** pair of mapped concepts that CLICS lists (2,767 pairs). This gives two lists: lumps inside one root, and pairs split across two roots that the world lumps.
  - Notation: "*r* = 3.9% (4/19 fam.)" means family-balanced rate, with lumping families out of families with data. † marks a pair involving a concept CLICS copies from broad glosses, so its rate is an upper bound (`research/notes/colexification.md` §1).
- **Panel examples** come from memory (marked M) unless linked. They illustrate a point; they are not a test.
- **Cost** counts occurrences in `texts/`, `examples/` and `spec/` (grep), plus compounds and rules that use the word.

## Candidates, ranked by how strongly the ladder points to a change

### 1. *lite pi nosen* "religion" ("way of god(s)"): rung 2, strong

- **Rung:** 2, second half of C4: don't build a theory into a basic word. The theory here is theism. Calling religion "the way of God" builds the claim that religion is about a god into the only word the language has for it.
  - This isn't "known wrong"; the language shouldn't take a position at all.
  - It also fails the fairness that B5 and C1 are there for. Buddhism, Jainism, Confucianism, Shinto practice and many local religions don't centre a god.
- **Evidence:**
  - CLICS⁴ records **no** language that lumps RELIGION with GOD. RELIGION colexifies only with WORSHIP (2 varieties, 1 family) and single varieties elsewhere.
  - The panel's words come from "law, duty" (Hindi/Bengali *dharm*, Arabic/Turkish/Persian/Swahili/Hausa *dīn*/*din*/*dini*/*addini*), "teaching" (Thai *sàatsanǎa* < *śāsana*; Mandarin/Japanese/Korean/Vietnamese 宗教 "ancestral teaching"), "tradition" (Indonesian *agama*), "worship" (Yoruba *ẹ̀sìn*) and "belief" (Quechua *iñiy*) (M). None says "god's way".
  - The tests found it twice. In `tests/udhr-01/terms.md` (row 25) it is "weak for non-theistic religions"; its add-back trigger is a reader excluding Buddhism. The French re-reading (`tests/udhr-01/relecture-fr.md` G4) says "religions without a god are excluded".
- **Cost of changing:** the phrase occurs 6 times, all in the UDHR translation and example, plus the §5.2.9 example sentence. It isn't in `compounds.tsv`.
- **Options:**
  - (a) A built phrase with no god in it. Either **lite pi dundi** "way of honouring" (worship, cf. Yoruba) or **lite pi gewan** "way of trust/faith" (cf. Quechua *iñiy*, Latin *fides*). Both are 5 syllables, like today's.
  - (b) A new root (tier 2). Religion is frequent in news and law texts, and a phrase that can't help encoding a stance is a real cost (rung 5).
  - (c) Keep it, and add "or conviction" (**lu ge pume feko**) wherever neutrality matters, as the French reviewer did.
  - My lean is (a) with **lite pi dundi**, and (b) if a blind test misreads it.

### 2. *nume* "live, be alive" and *pata* "life": the reverse case (merge), strong

- **Rung:** 4. BE ALIVE/LIFE *r* = **71.4%** (65/83 fam.; 309/515 varieties), well above 50%. Nothing above applies: there is no standard, no wrong belief, and nothing to confuse, since they are one meaning in two roles.
- **Evidence:** §4.2.3 already makes every content word usable in any role ("**sepi** 'apologise / an apology'"), so *nume* used as a noun already means "life". *pata* adds nothing the grammar can't say.
- **Cost:** *pata* has 3 occurrences (UDHR: *pata upe* "a decent life", *pata kunsu* "private life"). These become *nume upe* and *nume kunsu*. Removing it frees a tier-3 form and saves one root to learn (B7).
- **Options:** (a) merge: drop *pata*, and *nume* covers "life". (b) Keep *pata* if "life" should also carry "lifetime, biography"; but that is *muyi pi nume*.

### 3. *kuwi* "keep; protect": rung 3 with rung-4 support, strong

- **Rung:** 3. Both senses are frequent and take the same objects: people, money, things.
  - The difference changes what the listener does. "*kuwi* the children" means keep custody of them, or guard them from harm. "*kuwi* the money" means hold on to it, or secure it.
  - Context often fails, and one compound is ambiguous because of it: **pu kuwi** "warehouse" (`compounds.tsv`) reads equally as "shelter, refuge".
- **Evidence:**
  - KEEP/PROTECT *r* = **3.9%** (4/19 fam.), so rung 4 also says two unrelated roots.
  - Nearby rates: HOLD/KEEP 10.1% (62 fam.), KEEP/GUARD 6.3%, DEFEND/PROTECT 17.6%.
  - Some languages blend keep with guard: Spanish *guardar*, Arabic *ḥafiẓa*, Russian *хранить* (M). They are a minority, and they blend "store" with "guard", not "retain" with "protect".
- **Cost:** 30 occurrences. They include §4.7.4 (*wan gun kuwi* "she is protected"), §13 (*kuwi wan se ben* "protect him against that"), the UDHR text and *pu kuwi*. Splitting needs one new root (tier 3).
- **Options:**
  - (a) *kuwi* = protect (the sense the reference rules use), plus a new root for keep/retain. *warehouse* then uses the new root.
  - (b) *kuwi* = keep, plus a new root for protect. This changes more rule examples.
  - (c) Keep the lump and rename *warehouse* (**pu yaga** "place for putting").
  - My lean is (a).

### 4. *apu* "word; language" (also the language's name): rung 3, medium-strong

- **Rung:** 3. Both senses are frequent, and they meet in exactly one kind of context: talk about language. That context is large for this language's speakers, who live among other languages (P4).
  - "*to yesa apu tan*" means "I'm learning this word" or "this language".
  - In "what's the *apu* for X in *apu pi* Y", the two *apu* differ only by position.
  - Confusing them changes what people do (teach a word, or a language).
- **Evidence:**
  - Rung 4 is a coin flip: *r* = 50.2% (47/71 fam.). The bootstrap 95% interval is 40–61%, with 49% of resamples below 50%. Dropping single-variety families gives 40.7%.
  - Lumping is concentrated in single-variety families. Indo-European lumps 0 of 63 varieties.
  - In the panel, Japanese *kotoba* and Korean *mal* lump. Arabic *luġa*/*kalima*, Hindi *bhāṣā*/*śabd*, Swahili *lugha*/*neno*, Russian *язык*/*слово*, Mandarin 语言/词 and Spanish *lengua*/*palabra* split (M).
  - LANGUAGE/TONGUE is only 9.5% (13/76), so "tongue" is not a better lump partner.
- **Cost:** 94 occurrences. *apu* is the first syllable of the name **apu pi we**/Apupiwe, it heads "any language is *apu pi* X" (§0.2), and it is used in *password* (*apu pi udin*).
- **Options:**
  - (a) Keep the lump (status quo, §14.3).
  - (b) *apu* = language, with a new root for "word" (tier 4). **This keeps the name**, *apu pi X*, and every language reference. Only "word" uses change: *password* and some examples.
  - (c) *apu* = word, with a new root for "language". This renames the language itself.
  - My lean is (b), if the author accepts rung 3 here. Otherwise (a), with a trigger: a blind reader confuses word and language in a language-learning text.

### 5. *mido* "ask" (to inquire / to request): rung 3, medium

- **Rung:** 3. "Ask whether" and "ask to" fill the same slot, and the answer changes what the listener does: reply, or comply.
  - With a **wun** clause the two readings coincide. **to mido wan wun wan isi** is "I asked him whether he's going" or "I asked him to go".
  - Context often fails in reported speech.
- **Evidence:** ASK (INQUIRE)/ASK (REQUEST) *r* = 21.2% (30/74 fam.), just inside the 20–50% band. Rung 4 alone would say two words, one built from the other. Panel (M): Spanish *preguntar*/*pedir*, Russian *спросить*/*попросить*, Mandarin 问/请, Hindi *pūchnā*/*māṅgnā* split; French *demander* lumps.
- **Cost:** 1 occurrence. There is a cheap fix through grammar: the request act **so** exists (§7.1), so "ask to" can be **mido** + **so**-clause or a built form. The gloss and §4/§7 need a line.
- **Options:**
  - (a) Keep *mido* = inquire, and "ask to" = "*mido* … *li* + verb" (purpose). This is built, as the band says.
  - (b) Keep *mido* = inquire, plus a new root for request.
  - (c) Leave it as it is.
  - My lean is (a): zero new roots.

### 6. *agi* "lose, misplace", which is also the opposite of *yiyin* "win": rung 3, medium

- **Rung:** 3, plus the §3.4 trap. The gloss says "misplace", but `antonyms.tsv` pairs *agi* with both **find** and **win**. So it silently lumps losing a game with misplacing a thing, and a text also uses it for losing a state (*agi fanse* "lost his calm", `texts/002`). That is the English word *lose*.
  - Frequent and same context: "*to agi nimo*" means "I lost money", either misplaced it or lost it in a deal or bet.
- **Evidence:** No CLICS pair matches it cleanly; CLICS has MISPLACE and DEFEAT, but DEFEAT is the winner's verb. Panel (M): Mandarin 丢/输, Japanese *nakusu*/*makeru*, Korean *ilta*/*jida*, Hindi *khonā*/*hārnā*, Swahili *kupoteza*/*kushindwa*, Indonesian *hilang*/*kalah*, Russian *потерять*/*проиграть* split; Spanish *perder*, French *perdre* and Turkish *kaybetmek* lump. The lump is mostly Romance plus English.
- **Cost:** 2 occurrences, plus 1 antonym row. "Lose a game" is cheap to build as **mu yiyin** "not win".
- **Options:**
  - (a) Narrow *agi* to misplace and drop the win↔agi antonym pair. "Lose (a contest)" becomes **mu yiyin** or **gun yiyin** "be beaten".
  - (b) Make the lump explicit in the gloss.
  - My lean is (a).

### 7. *dili* "day, daytime or 24 hours": rung 1 and rung 3, medium

- **Rung 1:** the standard day is the 24-hour day. SI accepts the unit "day" = 86 400 s, and ISO 8601 defines the calendar day. The calendar uses *dili* that way: "*dili pi* 1–7", "*dili pi mape*" "the 9th". The lumped daytime sense is outside the standard.
- **Rung 3:** one grammar rule makes the two senses collide. §8.2.3: **nin** + duration = "for a span". So *wan doku nin dili* is "she works during the day" or "she works for a (whole) day". Elsewhere context usually tells.
- **Evidence:** DAY (24 HOURS)/DAY (NOT NIGHT) *r* = 52.9%, but on thin data (16/25 fam.); rung 4 would lump if nothing above applied.
- **Cost:** 20 occurrences, mostly the 24-hour sense, which stays. Daytime needs a phrase: **muyi pi giwe** "time of the sun", or **muyi mu yami** "not night".
- **Options:**
  - (a) *dili* = 24-hour day only, with daytime as a phrase.
  - (b) Keep the lump and add a note to §8.2.3 that *nin dili* means "during the daytime".
  - My lean is (a), because it is cheap and follows the standard.

### 8. *wupi* "need; should": rung 3, medium-low

- **Rung:** 3. Both senses fill the modal slot before a verb, and they differ in strength: "you need to take this" against "you should take this".
  - That difference matters in exactly the contexts §12.2 is for: medicine, safety, instructions.
  - The modal system has *keya* "must", but nothing between "must" and "should" except *wupi* covering both.
- **Evidence:** No CLICS pair exists (CLICS has only NEED (NOUN)). Two things make a fix cheap:
  - The advise speech act **fon** (§7.1) already expresses "should" as advice. So *wupi*'s "should" sense duplicates grammar that exists.
- **Cost:** 9 occurrences (§12.2 and a few texts). No new root.
- **Options:**
  - (a) *wupi* = need (to), with "should" said with **fon** or **upe** "good (to)".
  - (b) Keep the lump.
  - My lean is (a), but it touches §12.2 wording.

### 9. *wabun* "rule, regulation or law": rung 3, medium-low (the author already chose this lump)

- **Rung:** 3. Both senses are frequent and meet in the same contexts ("that's against the *wabun*"). Confusing them changes what people do: a legal penalty against a house or game rule.
- **Evidence:**
  - CLICS⁴ records **no** language that lumps LAW and RULE. The pair is absent from the colexification table, so fewer than 3 families lump it. The denominator isn't recoverable from the table.
  - Panel (M): Arabic *qānūn*/*qāʿida*, Mandarin 法律/规则, Swahili *sheria*/*kanuni*, Spanish *ley*/*regla*, Hindi *kānūn*/*niyam* split.
  - The lump was a deliberate choice (design log 2026-10-10, "Law is lumped with *wabun* 'rule'").
- **Cost:** 68 occurrences, almost all in the UDHR, where the sense is "law". *court* = *pu pi wabun*.
- **Options:**
  - (a) Keep, and say "law" as **wabun pi gigin** "rule of the country" where it matters.
  - (b) Split: *wabun* = law (most uses already), plus a new root or *ge wungu* for rule.
  - Because the author decided this, I flag it rather than recommend.

### 10. *lula* "power, strength or control": rung 3, low

- **Rung:** 3. Physical strength against power or authority over others. *wan ibe lula* means "he is strong" or "he has power". These come up together in politics and conflict. The adjective *konke* "strong" already covers the physical sense.
- **Evidence:** CLICS⁴ has STRENGTH/POWER in **1** variety only. The denominator isn't available.
- **Cost:** 5 occurrences. This also interacts with the loans proposal: electricity → *lula pi mufin* (`loans.md`).
- **Options:**
  - (a) *lula* = power/control, with physical strength = *konke* used as a noun (§4.2.3).
  - (b) Keep it.
  - My lean is (a); it needs no new root.

### 11. *bendo* "leg" / *pifo* "foot": reverse (merge), weak

- **Rung:** 4 alone would lump: LEG/FOOT *r* = 53.1% (100/136 fam.)†, an upper bound. The method's own example even says "LEG→FOOT" (§3).
- **But rung 3 applies first.** Leg and foot are frequent and share contexts (injury, pain, walking, clothing). "He hurt his *bendo*" against his foot changes what a medic does, and context often fails. So the ladder keeps two words.
- **Options:**
  - (a) Keep, and fix the stale example in §3 of the method.
  - (b) Merge if the author reads rung 3 more narrowly.
  - My lean is (a).

### 12. *gala* "tree" / *kima* "wood, the material": reverse (merge), weak

- **Rung:** 4 at exactly *r* = 50.0% (58/85 fam.), the same coin flip as *apu*. Rung 3 is weak: in "cut the *gala*" against "cut the *kima*", context mostly tells.
- **Cost of merging:** *kima* has 3 occurrences, plus *stick* = *kima netu*.
- **Options:**
  - (a) Keep (cheapest; a decision at the threshold is noise).
  - (b) Merge, with the material built (*kima* → *gala* + …).
  - Treat it consistently with *apu*. Both sit on the 50% line; if one is decided by rung 3, decide the other the same way.

### 13. Band 20–50%: two unrelated roots where rung 4 says "built from the other"

Not ≥50%, so this is outside the brief's reverse case, but rung 4's middle band is just as much a ladder output. These pairs are two unrelated roots today; the band says the less basic one should be built transparently from the other:

| Pair | Roots | *r* |
|---|---|---|
| HEAR/LISTEN | *nulu*/*doma* | 45.4% (53/74) |
| LAND/COUNTRY | *fowo*/*gigin* | 42.2% (30/53) |
| PAPER/BOOK | *mabo*/*ingo* | 37.5% (26/56) |
| ARM/HAND | *inyi*/*kiti* | 34.9% (53/105) |
| SEE/LOOK | *nagu*/*miya* | 23.9% (36/84) |
| TAKE/GET | *yidu*/*dunu* | 23.2% (25/68) |
| SUN/DAY | *giwe*/*dili* | 20.0% (68/216), on the line |

- ARM/HAND passes rung 3 (same body contexts, action-relevant in injury), so it keeps two roots.
- For the rest, rung 3 is weak. The ladder points mildly to built forms: listen = "*nulu* on purpose", look = "*nagu* on purpose", book = "*mabo* …".
- The research note says the 20% and 50% cuts are arbitrary and Claude's own addition. I'd put this group to the author as a question about the band rule itself, rather than as seven word changes.

### 14. *dunan* "month; moon": known candidate; the ladder says **keep**

- **Rung 1:** doesn't apply. ISO 8601 fixes what a month is, and *dunan* means exactly that month. Also naming the moon doesn't move the month's boundary. The standard has nothing to say about which other meaning a word may carry.
- **Rung 2:** no wrong belief is involved. Months came from lunations, which is an observation; the Gregorian calendar dropped the link but didn't refute it.
- **Rung 3:** weak. The moon is a sky object, the month a counted span (*dunan sa* "two months", *dunan pi yawu* "October"), and they rarely compete in one slot. The one shared context is lunar calendars (Hijri, Hebrew, Chinese), where the month starts at the new moon, so the confusion is harmless.
- **Rung 4:** *r* = 69.6% (60/75 fam.), robust on every variant.
- **Verdict:** keep. Add-back trigger for splitting: a blind test confuses the two.

## Borderline cases rejected

- **nebe "back, of the body; behind".** BACK/BEHIND *r* = 5.5% (17/187), so rung 4 would split. But "behind" from "back" is a common body-part-to-space path across families, which CLICS undercounts because BEHIND is often an adposition. Rung 3 doesn't apply: context always tells a body part from a relation.
- **doku "work; of a machine, function".** WORK (LABOUR)/(ACTIVITY) is 7.5%, on thin data (21 fam.). The machine sense has its own subject ("the phone doesn't *doku*"), so context always tells. Mandarin 工作 lumps the same way (M).
- **muge "do; make".** DO/MAKE ~90%† lump (note §1).
- **pani "old, aged or worn".** OLD (AGED)/(USED) is 94.1% (209/218). Lump correct.
- **lowu/futa "man, male"/"woman, female".** MALE person/animal is 79.2%, WOMAN/FEMALE (OF PERSON) 55.1%. Lumps correct.
- **fowo "ground, earth or soil".** LAND/SOIL is 53.8%. Lump correct. (Planet Earth isn't covered; that's a gap, not a boundary error.)
- **guyi "house, home".** 53.8%, but on thin data (21 fam.). Lump fine; no confusing context.
- **tiwu "child"** (young/descendant). 76.2%. Lump correct.
- **kanko "smell, sense or give off an odour".** SMELL perceive/stink is 88.1%. Lump correct.
- **nume "live, be alive or dwell".** The dwell sense always takes a place phrase; Spanish *vivir* and French *vivre* lump (M). No confusion.
- **gunmo "thin"** (slim/flat) 95.4%; **duko "turn"** 90.3%; **mibun "hide"** 97.0%; **onti "burn"** 88.8%; **sola "road/path"** 85.2%†; **fuyu "meat/flesh"** 86.6%†. All are lumps the world shares.
- **fugi "end"** (space/time) 27.5%; **penyu "connect, join"** 13.8%, thin; **pensi "wash"** 15.0%, thin. No rung-3 case: context tells.
- **situ "shade, shadow"; ninge "sound, noise"; lunyu "page, sheet"; kemin "document, file"; ginni "add, put in more".** These are related senses that rarely compete in one slot.
- **tinli "key, button".** Fine as one sense (a thing you press). But the English gloss "key" also reads as a door key, which *tinli* isn't (a door key would be *du udin*). That is a §3.4/§14.2 gloss fix ("key (to press), button"), not a boundary change.
- **yunen "oil, the liquid"** (cooking against fuel oil). The setting nearly always tells; no change.
- **gigin "country, nation".** It lumps state with people (nations without states). LAND/COUNTRY sits at 42% against *fowo*. Political texts may need *funti pi ewo* for "a people"; this is a rung-5 phrase question, not a boundary error. Low.
- **woga "fish, the animal"** (whales). §3b lists "whales grouped with fish" as a belief-laden boundary. The gloss doesn't say whether whales count. Under C4, define it by what's observed (gills, lives in water), so whales aren't *woga* because they breathe air. That's a gloss clarification, not a change. ("Fish" is not a clade either, so no science-based boundary exists to follow, per rung 3's last sentence.)
- **giwe "sun" / uwan "star"; noso "animal"** (excluding humans); **sunni "insect"** (folk sense). These are perception boundaries, which §3b says are never outdated. The compounds avoid wrong groupings already: *spider* and *scorpion* are *noso meli*, not *sunni*; *bat* is *no bina mon yami*, not a bird.
- **Compounds.** I checked all 52.
  - Only *pu kuwi* "warehouse" carries a boundary problem; see #3.
  - *landlord* = *no ibe guyi* "one who has the house" lumps homeowner with landlord. That is low-cost, since context (renting) tells.
  - *meditate* = *goyu pume* "sit thinking" names one posture-based practice. It's a phrase, so it's cheap to revise if a test objects.
  - *alien* = *no obu se yaye* "one who comes from the sky" describes what is observed, not a theory.

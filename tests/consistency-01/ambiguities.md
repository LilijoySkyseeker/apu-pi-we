# Translator ambiguity lists, collected 2026-10-10

Raw, from every translation in the tests run on 2026-10-10. Many were resolved later the same day; triage is in consistency-01/triage.md.

## tests/economy-01-context/translation-v2.md
1. tan vs ben for events. "tan = nearer (just said, or here and now), ben = further." Is "just said" measured by time, by speaker, or by how far back the event itself is? The doc's own examples use **ben** for "I told him that" and "that's fine", both about something the other person just said. I used **tan** for a speaker's own just-said description or the present situation (turns 4, 7, 12), and **ben** for what someone else said or a past event (turns 6, 9, 18).
2. wan vs yi for a newly introduced person. **yi** is for someone "newly brought in", but a newly introduced person who becomes the subject of the talk (the neighbour, turn 20) is also "the person being talked about". It's unclear when the new person takes over **wan**.
3. Position of bo. It's listed with the operators, but operators "cover what follows". **kon bo** and **ewo yu** suggest it follows its noun. I wrote **musu bo** "something / anything"; the doc never shows it with a noun.
4. Interjections and discourse markers ("hey", "wait", "okay", "honestly", "I mean", "by the way", "ha"). There's no rule for which of these get a word, an act particle or nothing. "Ha" can't even be spelled. "Okay" got three different treatments by function (dropped, **de** + verb, folded into **ben gun upe**).
5. "should" about a third person. **fon** is advice to the listener only, **keya** is "must", **wupi** is "need to". There's no stated word for a weaker "ought to" about someone else.
6. "Last month" / "last time". The doc gives **wo nelon fi** "next week" but no past example. **ya dunan fi** could mean "a month ago" rather than "in the previous calendar month".
7. Which-questions over clauses. **… lu … yu** is shown only with nouns. With two full clauses (turn 19), it's unclear where **yu** goes and whether a comma is needed before it.
8. muge + one word with the object dropped (**muge inan**, turn 3). The result/manner order rule needs both words to decide between "make clean" and "do cleanly". Here both readings mean the same thing.

## tests/economy-01-context/translation.md
1. **wan and first/second-person subjects.** Rule 6 says **wan** is "the most
2. **Mentioned vs subject.** A person mentioned many times but never a subject
3. **Dropped subjects after a subjectless echo.** Rule 11 allows dropping after
4. **Advice with no subject.** Rule 11 licenses dropping the subject only for
5. **Objects in echo answers.** Rule 4's echo answers have no object
6. **Modifiers inside derived phrases.** In **pu siten minwe pi yi** (line 7),
7. **Clock times with "about".** Where **fu** goes relative to **mon** and a
8. **"Last time".** The anchor + offset rule names calendar units. Using
9. **Name adaptation.** `tools/names.py` (run, not read) prints only a demo list.

## tests/grammar-rebuild/roundtrip/translation.md
1. Fillers and interjections (ねえ, んー, え, あー, interjectory さ): the reference names a place only for stance words (sentence end) and **mm**/**huh?**. Where a new filler goes, at the start or after a linker, is unspecified.
2. A modifier after a compound with a verb in it (**kubo pu nume ganna**): does it modify the whole compound or only **nume**?
3. **gun** after a compound ending in a verb (**kubo pu nume gun …**) could be read as "to be" after another verb (rule 7).
4. Chained **pi** (**dili pi ufo pi nelon tan**): it's unclear whether the second **pi** attaches to **dili** or to **ufo**.
5. Whether **bu** may refer to an event (the move), or only **tan**/**ben** can.
6. Where **bo** "unspecified" goes on a noun: before it, like an operator, or after it, as in **kon bo**. I avoided it and used **in**.
7. A sentence opening with **gi** + clause and the main clause left out (rule 11 vs rule 15).
8. Past progressive (～てた): whether **sin** and **le** can combine is undefined. I used **sin** alone.
9. **fanmu** "gather" has no second gloss, so it could mean collect or assemble.
10. Whether **min** is needed or allowed on **yu** questions. The examples omit it.
11. Whether a doubled content word (そうそう → **feko feko**?) follows principle 5. All the examples are grammar words.
12. **yen** after an object noun (**pasu in pi minfi yen dinyo bu**) could read as a noun list ("noon and …") rather than as joining two clauses.
13. The scope of an afterthought (健太のおごりで): a pause is allowed only in the three listed places, so the afterthought comma was dropped.

## tests/multilang-01/retest/hindi-urdu/translation.md
1. lanno before a non-name. The reference allows **lanno** before a name, or alone in address. चाचा जी has no name, so I used **lanno faba lowu pi wede**. This isn't covered. A respected person without a name (Gupta's daughter, the wife at home) has no respect carrier at all.
2. Bare title in reference. सर is used *about* B ("सर से पूछ लो"), but **lanno** alone is for address only. I used **no wungu**.
3. Order of an address and a linker before the particle (लेकिन सर, और सर). I wrote address, then linker, then scene-setting.
4. Apposition. No rule covers it. "X, NP" at the end of a sentence reads as an address, so I split appositives into separate sentences (रमेश …, पूजा …).
5. fule with an aspect word: **sun fule win neke** or **sun win fule neke**? I put fule first.
6. Fronted count phrase (**gimu sa, …**): the scene-setting rule names time and place, not number of occasions.
7. Emphatic "himself" (ख़ुद "in person"): **nen** is only described as reflexive. I used **genfo**.
8. yi for someone never mentioned (the woman at home), and **wan/yi** when a newly introduced person becomes the topic within one turn (the uncle, the daughter).
9. A lone particle as a whole utterance (**ba.** for अरे) under rule 11.
10. ke with amounts: **ke feli** or **ke kudu** for money; stacking **to ke kudu** "rather more".
11. Vague times of day (दोपहर): there is no word, and the clock-time rule forces a precise time.

## tests/multilang-01/retest/japanese/translation.md
1. lanno with a role noun. Can lanno go before a role noun such as no ibe guyi, as Japanese さん does with 大家? language.md only gives it before a name or alone in address.
2. Stance after a question. Can a stance word follow a min question (min …, donon)? The examples only show it after statements.
3. ba with a stance word. Can ba combine with a stance word at the end (ba …, buni)?
4. Clock times before 10:00. Is 09:00 read mape po po or po mape po po? The examples are only 15:30 and 22:00.
5. Getting attention and hesitating without a name. There is no way to call for attention (ねえ) without a name or kin word, and no hesitation or recognition filler (んー, あー). mm means only "heard".
6. Where a du phrase ends. A modifier after du + verb can be read as part of the verb phrase (du dinyo uyo = "thing for carrying few"?). I used gun to close it.
7. Brand loans as verbs. Can a loaned brand name (layin) work as a verb the way native roots do?
8. Overlapping sentence-end words. じゃん/でしょ (iwun), ね/よね (buni) and 多くない？/っけ (min) were mapped by judgment. The seeded words overlap at the edges.
9. tan or ben. Should "that idea you just said" (Japanese それ) be tan (just said) or ben (the demonstrative example in rule 6)?
10. "Enough". There is no word or stated construction for "enough" / "not enough".

## tests/multilang-01/retest/spanish/translation.md
- **Writing numbers:** the Writing section says numbers are written in digits, but every example in the doc spells them out (**dunan pi yawu**, **mon fi te ka po**). Clock times like `10:00` would also need the banned `:`. Numbers are spelled out here.
- **Day of the month:** "points in time are read digit by digit", but the example **dunan pi yawu** (month 10) uses quantity reading. 14 is written **yawu da** by analogy; digit reading would be **fi da**. Whether 09:00 is **mape po po** or **po mape po po** is also unclear.
- **lanno before a role or common noun** ("Estimados vecinos"): the doc only shows it before a name, or alone.
- **Two speech-act particles** (**a min**, sarcastic question): the doc doesn't say whether they stack, or in which order.
- **Letters as labels** (3.º B): no rule. Here the letter's name is treated as a name. `names.py` returns **biu**/**beu**, which breaks the vowel-glide rule, so the glide was added by hand (**bewu**, from Spanish "be").
- **Prepositional phrase after a relative clause** (3, 15): rule 8 says it attaches to "its clause's main verb", but it isn't clear whether a comma closes the relative clause. Here a comma is taken to close it.
- **Relative clause with a place gap** (22, "where it has stood"): the doc shows only subject gaps.
- **Determiner order** with both plural and demonstrative (**kemu tan la** vs **kemu la tan**): no rule.
- **Distributive "per/each"** (180 € per dwelling): no word or construction.
- Spanish impersonal *se*: leaving out the subject (rule 11) seems right, but after a speech act it could read as "you" (21).

## tests/multilang-01/stage2/arabic/translation.md
- **Vocatives.** Nothing says where an address (يا كريم) goes. Only a linker, scene-setter or if/when clause may precede the speech-act particle, so I put names after the first clause, and يا جماعة as its own sentence (**sonu la.**).
- **Address words.** Respect is "a role word before the name", but there is no guidance for address without a name (أستاذ, فندم, حبيبي, ستي, ابني), or for figurative kin/endearment terms.
- **Rhetorical questions.** Can **a** combine with **min** (a non-literal question)? Unstated; I avoided it.
- **Wishes / blessings.** Is **so** + third-person subject (**so nosen kuwi me**) an optative "may God…"? Only **so pen** "let's" is given.
- **Loans as verbs.** Position rule says any content word can be a verb; unclear if that holds for unlisted loans (**din fowutowu**, **lon sutanpu bu**).
- **Clock time before 10:00.** Is 09:00 **mape po po** or **po mape po po**?
- na after a relation word (**tun na lon**): "before a single word" presumably allows it, but not shown.
- **"Turned out" (mirative).** Whether **o** "seen" is the right source for something discovered by experience.
- nun with routines: whether **nun** goes before a greeting (**nun upe leso**) as "first in a statement".
- **Doubled answers**: Egyptian ماشي ماشي doubles for grudging concession; the doubling principle (widen/strengthen) seems to forbid copying it.

## tests/multilang-01/stage2/english/translation.md
1. **gun** "there is" applies "only at the very start of a sentence". It's unclear whether that still holds after a linker (**yen gun …**) or at the start of a **gi** clause (**gi gun imeyilu**, turn 13).
2. **Impersonal or unknown "they".** No rule covers it. Can **bo** modify a noun (**ewo bo** "someone"), by analogy with **ewo yu**? **go** is generic ("one"), not existential.
3. **Dropped subjects** (rule 11): nothing says how a dropped subject is read when context supplies no referent (a default "I"? an unspecified agent?).
4. **sun** when the reported "speaker" is a document (an email), and whether **sun la** is a valid plural.
5. **Days of the month:** **dili pi** + 1–7 alone is a weekday, so "the first" (of an unnamed month) can't be said without naming the month.
6. **Verb + verb:** the list of verbs that take a verb object ends in "…". Is **mido nunya** "ask to tow"? Does **li** + an action noun mean "for X" or "in order to X"?
7. **de with an explicit non-"I" subject** (**de din yidu …**): allowed? And do speech-act particles work inside quotes the same way?
8. **Commas after a bare linker before a particle** (**un min …**, **yen ba …**). The only example (**gi tan, tin**) has a linker phrase.
9. **Scope of la and pi chains:** **pu pi tale pi pen** ((place of car) of us, or place of (car of us)?), and whether **la** after a derived noun (**no lugo wabun la**) pluralizes the whole noun or just its last word.
10. **Manner modifier vs a wun object:** rule 15 makes a clause-final **fu yu** attach to the inner clause, so placing "how" before a **wun** object (**lugo fu yu wun …**) is forced, but object-then-manner is the stated order.
11. **wame** before a subject noun to mean "X too" (**wame tale kudu …**): only object positions have examples.
12. **Quoting a word without a say-verb** (**"kon bo".**) vs rule 12, which says quotes are framed by a say-verb.
13. **Clock times before 10:00:** read with or without a leading zero (**oma fi te** vs **po oma fi te**)?
14. **Role word before a name** for family names: **yonyo en endalusan** "the Hendersons" and **lowu en endalusan** "Mr Henderson". Only **no tofo en mala** is given.
15. **Confidence on echo answers:** where **kon** goes when a one-word echo answer is itself uncertain.

## tests/multilang-01/stage2/hindi-urdu/translation.md
1. **Third-person honorifics.** **nun** marks politeness toward the listener only. Hindi marks respect for the person *talked about* (बैठी थीं, साहब, जी, आ गए, देखती हैं). There is no rule for this, and no word. Seven or more instances were dropped.
2. **Address without a name.** The reference shows a role word before a name (**no tofo en mala**). Is a role word alone (**no wungu** for "sir") fine as a vocative, and where does it go in the sentence?
3. **Apposition and fronted topics.** "Ramesh, the one who works at the godown, a tallish boy" and "our new intern, you know, Pooja, she said…" have no stated construction. A comma after a relative clause was used; the reference says nothing may follow a relative clause in its phrase, and it is unclear whether a comma ends that phrase.
4. **"Self" as an intensifier.** **nen** is defined as reflexive. Using it after an intransitive verb (**obu nen** "came in person") is inferred, not stated. After a transitive verb it would be read as an object, so "of his own accord" became **se nen**.
5. **Emphatic NOT plus "not yet".** Does **mu mu sin** "emphatically not yet" combine like this?
6. Bare **ke**. The reference gives **ke** + adjective. Whether **ke nimo** "more money" and a bare **ke** "more, extra" are allowed is not stated.
7. **gun "there is" inside a subordinate clause.** That reading is allowed only at the start of a sentence, so "no problem" inside a **wun** clause had to become **ben mu gun batu**.
8. **"Speech-act particle, then nun" after a linker.** **un nun liga…** follows "linker before particle" plus "nun first in a statement", but the combination isn't shown.
9. **Several fronted elements.** A scene-setting phrase, then a linker, then an if-clause, all before **tin** (turn 22). Each is allowed alone; stacking them isn't addressed.
10. **Where the obviative points inside reported speech.** In turn 11 Pooja is **sun** and her uncle is **yi**. Whether **wan** in a report means the report's topic or the conversation's topic is not stated.
11. **Hindi ʋ.** `names.py` maps ʋ to **w**. The written rule only says v → b; ʋ isn't listed.

## tests/multilang-01/stage2/mandarin/translation.md
- Numbers in writing. The Writing section says digits; rules 9 and 11 write clock times and counts as words (fu sa sa po po). Digits are used here. Clock times can't use a colon, so they are written 23 00, which looks like the grouping of a single number. The phone number was regrouped in threes, though phone digits are read as an identifier.
- Anchor + offset with weekday labels and story time. "Last Thursday" and "next Monday" (dili pi 4 ya nelon 1, dili pi 1 wo nelon 1) follow the pattern but aren't exemplified. With no anchor the anchor is "now", so "the next day" in a narrative needed a relative clause (dili man lefan).
- Topic switch for wan. When a new person becomes the subject of several sentences (小何 in 6–7), it's unclear whether he becomes wan or stays yi.
- Purpose li-phrases. They may not come before the speech-act particle, and rule 15 doesn't say whether a final li-phrase attaches to the innermost clause.
- Relation phrases after an agent/place noun with a phrasal base. In no wungu guyi gan ewo in, the phrase could belong to the base or to the main verb. Commas were used to separate.
- la after no + verb + object. In no ibe pu nume la, it's unclear whether la makes the owners or the dwellings plural.
- de with a third-person subject. It's unclear whether an institution naming itself can use de.
- Vocatives. Their position relative to the speech-act particle isn't given, nor whether nun may stand before a bare address (12).
- gun "there is" after a fronted place phrase (21). The rule says "only at the very start".
- gi + noun phrase (gi lafi yen yema). Only gi tan is exemplified.
- Loans and the checker. check.py flags every loan (tadu, powintu, pawuwa sutulipu, ibayiku, …), although the borrowing rule allows them. names.py gives different forms for rhotic and non-rhotic English input (taludu / tadu). Non-rhotic was used, to match awuwa and kilamita.

## tests/multilang-01/stage2/russian/translation.md
1. **Vocatives:** rule 1 lets only a linker, a scene-setting phrase or an if/when clause come before the speech-act particle. Where a name used in address goes ("Серёж, давай…") isn't stated, so I made it a separate fragment.
2. **Inclusive/exclusive "we" with several listeners:** when "we" includes one listener and excludes another (line 22), it isn't said whether **pen** or **din** applies.
3. **Stacking speech-act particles:** **a min** (rhetorical question) and **a tin** (sarcastic order). It isn't said whether **a** combines with another particle.
4. **Clock times before 10:00:** is 07:00 **oma po po** or **po oma po po**? Can a casual "at seven" be just **mon oma**?
5. **Emphasis / discourse particles** (же, ж, -то, ведь, между прочим): the tag **min** is the closest match, but it asks for confirmation instead of asserting shared knowledge. There is no stated way to mark "as you know".
6. **mu + sin:** **mu sin** is "not yet", so a negated past completed event ("hadn't taken") has no clear form.
7. **Relative clauses with a time gap** ("days when I don't work" = **dili la man lon mu doku**): it isn't said what role the head noun plays inside a **man** clause.
8. **Imperfective nuances** (general-factual past, annulled result) have only **sin**, **le** or nothing to map onto.

## tests/multilang-01/stage2/spanish/translation.md
- Vocatives. No rule says where a form of address goes, or how it orders with **nun**, which must come "first in a statement". I put the address first, then **nun** (1, 11).
- Numbers in writing vs. the examples. The Writing section says numbers are written in digits, but the newest examples (rule 11, 2026-10-10) spell out clock times (**sa sa po po**), and no written clock format exists. I used digits for counts and dates, and words for clock times. Also, rule 9 says months are "read digit by digit", but its own example is **dunan pi yawu**, a quantity reading. With digits in writing this didn't arise here, but it would when reading aloud (**dili pi 14**: "fi da" or "yawu da"?).
- Institutions: borrow or describe? The Words section says institutions are borrowed from English; Word building says government "composed fine". I described "Administración", "Junta" and "Comunidad de Propietarios".
- Topic fronting. "Nothing moves", and only time/place phrases may open a sentence. It's unclear whether a topic like "en cuanto a X" / "con la azotea" may open as a scene-setting phrase (I avoided it in 13 and 18).
- Relative clauses with an object or location gap (**mabo man me la yaga**, **fanmu man go yebin**). All the doc's examples are subject gaps.
- a + question. Whether the non-literal particle can combine with a **yu** question to make a rhetorical question, and whether **a** and a final **min** tag can coexist (14).
- "any" (bo). **bo** is "unspecified" as an operator. Using it as "any/anything" after a noun or as an object (2, 9, 12) is my extension.
- Speech-act particle mid-sentence. Only linkers, scene phrases and if/when clauses may precede it, so a Spanish sentence that turns into a question, a rhetorical aside or an intention halfway through has to be split (14, 22).
- la with tan/pi. The relative order of plural **la** and other determiners or **pi** phrases after a multi-word noun (**kemu la pi we**, **no nume gelu la**) isn't specified.
- "before/after" + offset with an explicit anchor (**bu ya dili 4** "four days before it"). Rule 9 shows anchor + offset only with time words (**wuma wo dili fi**). I assumed any noun can be the anchor.

## tests/regression-01/english/translation.md
- **Discourse "ok"** (msgs 1, 10, 22): no word, no linker and no stance word fits an opener or closer meaning "alright then". **mm** means only "heard you". I folded it into **gi tan** or left it out.
- **Bare predicate fragments** (**bi upe.**, **o feko.**): rule 11 forbids leaving out the subject of **gun** but allows leaving out the verb. It's unclear whether **gun** and its subject can both go. I treated it as allowed.
- **fu minfi** "around noon": "about" is defined only for **fu** + a number.
- **Quantity determiner as head** (**kin pi foto** "some of the photos"): the part-of-whole pattern is given only with numbers.
- **Two pi phrases on one noun** (**foto … pi [X1] pi me**): no rule says which noun the second one attaches to.
- **ba min** is defined as an indignant question. Plain surprise ("??") has no listed form.
- **Can a relation word drop its object at the end of a clause?** Rule 8 allows it, but **mon** "there" before **fu**/**yu** would misparse, so I used **kemu ben** or the place name.
- **Writing "!!"/"??"**: allowed but "not needed". It's unclear whether doubling them (chat intensity) means anything. I left them out and used **ba**.

## tests/regression-01/indonesian/translation.md
- **Address vs. a fronted noun phrase.** The rule is that a short noun phrase plus a pause at the start is an address. That blocks openers such as "Satu lagi," ("one more thing"), so I used **gun fe musu fi.** The same reading threatens a time phrase after a comma at the end of a sentence.
- **Day plus clock time in one phrase.** The doc gives month plus day (**dunan pi yawu, dili pi mape**), but not weekday plus hour.
- **Q3 parse.** **dunan ka pi ka** could also parse as "month, three of three" (X **pi** Y = part of a whole).
- **lanno as a pronoun for the listener.** The doc says **lanno** alone can refer to someone and "marks the person, never the listener". It is unclear whether it may stand for *you*, as Indonesian *Ibu* does.
- **Stacking stance words.** *dong ya* wants both **a** and **min**; the doc doesn't say whether two stance words can follow each other.
- **Placing ya "beforehand" before a mon phrase** (11). It is unclear whether **ya mon …** would read as "before at …", so I moved the time phrase to the front.
- **upe + verb as a wish.** **upe doku** could be read as praise for work already done ("good work") instead of a wish.
- **Speech-act particle for a first-person request** (**so to … nagu** "let me see"). Only **so pen** "let's" is documented.
- **Emoji and the sentence boundary.** Where an emoji ends a sentence before another one starts (21), I added a full stop after the emoji.

## tests/roundtrip-01-japanese/translation.md
1. Stacked pi phrases. "Saturday of this week" (**dili pi ufo pi nelon tan**): it's unclear whether the second **pi** attaches to **dili** or to the label **ufo**. There's no documented way to tie a weekday to a particular week.
2. Degree words on relation words. Does **ke ya** "more beforehand" = "earlier" work? Rule 13 shows **ke** only before adjectives, and **ya** alone is an adverb (rule 8). No documented way to say "earlier / later than planned".
3. Existential gun after a linker. Rule 7 says **gun** means "there is" only at the very start of a sentence with no subject. Does **un, gun …** count as the start?
4. Derived nouns with a verb-phrase base, followed by the clause's verb. **kubo pu nume wupi …**: since **pu** can take a whole verb phrase, the verb could be swallowed into the derived noun. I used a comma, but the pause rule lists only three places, and none covers this exactly.
5. Adjectives vs. verbs as predicates. Rule 7 requires **gun** before an adjective, but not every root is clearly an adjective or a verb (**kete** full, **sogi** happy, **feko** true). I used **gun** for the ones glossed as adjectives.
6. Tag min with fon. Is a clause-final tag **min** allowed after a non-statement speech act (**fon …, min**)?
7. Clock reading of times before 10:00. 09:00 as **mape po po** or **po mape po po**? The examples only show times with two-digit hours.
8. Combining aspect words. There's no documented way to say "was doing" in the past (**sin** + **le**), so 嘆いてた lost its progressive.
9. Interjections. Only **mm** and **huh?** exist. ねえ, え, あー, んー and いや had nowhere to go except dropping them or turning them into a linker.

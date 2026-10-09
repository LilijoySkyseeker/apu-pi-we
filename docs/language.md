# The language: current reference

This is the current state. Reasons and history are in [design-log.md](design-log.md); evidence is in [../research/](../research/).

**What it is:** a thought experiment in designing a universal human language for modern Earth from first principles. It's imagined as a *native* language, one that children grow up speaking, so the only fixed constraints are human: mouth, ear, memory, attention.

**Goal:** faithful transmission of thought, at a cost speakers will actually pay. When features conflict, this decides.

## Six principles

Most of the grammar follows from these. The rules after them are the cases the principles don't cover.

1. **The common case costs nothing.** Statements, ordinary belief, unknown source, the main character, and present-or-unspecified time are all unmarked. Only departures from the default cost a word. Frequent meanings get the shortest words.
2. **Heads come first, and position carries role.** The order is subject, verb, object. Anything that modifies a word follows it: adjectives after nouns, verbs after nouns (**ewo niba** "walking person"), one verb after another (**goyu pume** "sit thinking" = meditate), noun after noun (**dinbu lumi** "snake fire" = dragon). Nothing moves, not even question words, so a listener who loses one word can still tell who did what.
3. **Operators cover what follows them.** The speech-act particle at the start covers the sentence. NOT, confidence, source, ONLY, AT LEAST and degree words cover the clause when they start it, or a single word when placed before it.
4. **Heavy goes last.** A noun's own modifiers come before its "of" phrase (**lugo to meli pi kima** "rather little knowledge of sticks"). In a causative, the result comes before the object (**muge bonko me** "make angry you"). Long clauses go to the end of the sentence ("there's a good idea: that one hits…"). Relative clauses have no end marker, so nothing may follow them in their phrase.
5. **Doubling widens or strengthens.** **yo yo** = emergency. **a** = this sentence is not literal; **a a** = the whole turn. **mu mu** = emphatic NOT. **ku ku** = extra deference.
6. **Every social pressure gets its own outlet.** Emphasis has **ba**, **bi** and doubling; politeness has **ku**. People will always need to stress, soften and show respect. If those needs had no channel of their own, they would wear down the precision words instead (see [drift.md](drift.md)). So the confidence numbers are never used for emphasis, and the speech acts and hedges are never used for politeness.

## Sounds

- **Vowels:** a e i o u.
- **Consonants (13):** p b t d k g · m n · f s · l w y. Only three places in the mouth (lips, tongue tip, back of tongue), because place is the cue noise destroys first. /v/ and /z/ were deleted: both are rare worldwide, /v/ is easily confused with /b/ and tends to merge with /w/, and /s/–/z/ tends to merge. Removing /z/ cost almost nothing at a 3,000-root scale.
- **Syllables:** (C)V(n). A vowel-only syllable may appear only at the start of a word. The only syllable-final consonant is n.
- **Stress:** the first syllable of every content word; grammar words are unstressed. Stress marks where each content word begins. The stressed syllable is said **higher in pitch, stepping down after it**, as English says WA-ter or MO-ther, but **not longer**, because listeners hear lengthening as the *end* of a word. Every syllable keeps its full vowel: the rhythm is syllable-timed, like Spanish or Japanese, not stress-timed like English.
- **Harmless variants:** k and g may sound like "ch" and "j" before i and e; a vowel plus n may become a nasal vowel; consonants between vowels may soften. The vocabulary is built so these changes never merge two words.
- **Declination:** across a phrase, each stressed syllable is a little lower than the one before, so a run of words steps down like a staircase instead of bouncing at one height. Pitch resets at the next phrase (after a comma or a full stop). Nearly all languages do this; Finnish and Hungarian (first-syllable stress) and Japanese (downstep) are clear examples.
- **No tones.** Pitch is free for intonation and emotion. A question needs no rising tone, since the question word does that job; rising anyway is fine.
- **Interjections outside the system:** **mm** "heard you", **huh?** "say again".
- **Writing:** see the Writing section below.

## Writing

Agreed with the user, 2026-10-09. The Latin transliteration is the language's script for now: it costs nothing to type on any keyboard or phone, and computing runs on it. A script designed from first principles is deferred. Add one if human tests show reading trouble, or when there's a way to work on visual design together.

- **Letters:** the 18 plain letters a b d e f g i k l m n o p s t u w y, one per sound, with no accents and no letter pairs. Only letters, never digits, inside words.
- **All lowercase, names included.** The name article **en** marks names, so capitals carry nothing. A capital I never appears, which avoids the l/I/1 confusion of sans-serif fonts (found by the user's first reading check).
- **Stress is not written**, because it's predictable: the first syllable of every word of two or more syllables is stressed, and so is each one-syllable digit (**po fi sa ka da te**). All other one-syllable words are unstressed grammar words. (Docs used capitals for stress until 2026-10-09.)
- **Numbers** are written with the digits 0–5, grouped in fours from the point with a space (senary's grouping): `1045 4323`. **.** is the point. Where text mixes bases, mark base 6 with a subscript ₆ (or `_6` in plain text).
- **Punctuation: three marks only** (first-principles review with the user, 2026-10-09). Writing marks exactly what speech marks with the voice; everything else is carried by words.

| Mark | Use |
|---|---|
| `,` | wherever the pause rule calls for a pause; clause attachment depends on it |
| `.` | end of a sentence; which "he" is meant depends on sentence boundaries. (In numbers, `.` is the point; it always has digits on both sides.) |
| `" "` | around quoted speech; the speech-tag rule needs the quote's edges, which speech marks by a change of voice |

  No `?` or `!`. The opening word (**min**, **yo**, **ba**) already says it, and earlier: like Spanish's opening ¿, a reader knows the sentence's shape before saying it. The user's reading test showed end marks steer the voice, but too late. No `-` (compounds are ordinary phrases in speech) and no `:` (in speech it's just a pause). Triggers to bring one back: `?`/`!` if readers or text-to-speech misplace intonation despite the opening word; `-` if established compounds get misread; `:` if a pause can't carry a construction.

- **Spelling follows the standard pronunciation.** The harmless variants (k sounding like "ch" before i, nasal vowels, softened middle consonants) are never written, so spelling stays one letter per sound.

## Words

- Grammar words have one unstressed syllable; content words have two or more, stressed on the first. The one exception is the six digits: one syllable, stressed. No content word begins with a digit's syllable, so a digit followed by a grammar word can never sound like a content word. Every meaning is a separate word that never changes: no endings, no agreement, no case, no gender.
- Content words with similar or opposite meanings are given forms that sound as different as possible, because context can't tell them apart.
- **Built for drift:** no two content words may become the same after the changes a language like this is likely to undergo: later syllables blurring e/i and o/u, middle consonants voicing, a final n melting away. Grammar words that can stand in the same slot start with different consonants, so they stay apart even if their vowels weaken.
- **A word's role comes from its position.** Any content word can be a noun, verb or modifier: **sepi** "apologize / an apology", **miya bonko** "look angrily / an angry look". After a verb, a modifier describes the manner: **oyi fanse** "say calmly".
- **Verb + verb:** if the first verb can take an object (want, try, need, must, can, start, stop, teach…), the second is that object: **walo alun** "try to break". Otherwise the second describes the first: **goyu pume** "sit thinking".
- **muge** is "do", and also the causative "make". The order tells them apart: **muge upe tan** (result, then object) = "make this good, fix it"; **muge tan upe** (object, then manner) = "do this well".
- Compounds are ordinary phrases that stuck; the established ones are listed in [../data/compounds.tsv](../data/compounds.tsv). To list nouns rather than modify one with another, use **yen** "and": **mole yen wede** "mother and father".
- **Gender is a modifier**, stated once when it matters: **ewo wungu futa** "the commander, a woman". After that, **wan** carries her.
- **Emphasis and contrast** have no special device yet. Back-translation test 02 showed parallel sentences carry contrast on their own ("**lon mu yidu bu. en tomasu yidu bu.**" = "*I* didn't take it, *Tomas* did"). Add a focus particle if a test shows contrast being lost.
- **The curse word gefo** fits any content-word slot: a verb (**ba gefo me** "fuck you"), a modifier (**lukan gefo** "fucking head"), or after **yu** (**yu gefo** "what the fuck").
- **Names** take the article **en**, always: **en mala** "Mara". Many languages have such articles (Tagalog *si*, Māori *a*, Catalan *en*). With the article, a name that happens to sound like a word can't be mistaken for it, the way English copes with names like Rose or Baker.
- **Names and loanwords are adapted by rule** (`tools/names.py`):
  - Each foreign sound becomes the nearest native sound: r → l, v → b, z/sh/zh → s, th → f, dh → d, ch → t, j → d, kh → k. h and glottal sounds disappear, ng → n, and length, aspiration and tone are dropped.
  - Two vowels in a row get a glide (y or w).
  - A consonant that can't stand where it is gets an added **u**; consonants are never dropped. Names have at least two syllables.
  - Examples: Lilith → **en lilifu**, Christopher → **en kulisutafalu**, London → **en landan**, Nairobi → **en nayilobi**.
  - In a blind test, a reader recovered 43 of 44 world names from their adapted forms. A fixed added vowel beat copying a nearby vowel, because it marks itself as "not in the original" (`tests/names-01/`).
- **Loanwords** follow the same sound rules without the article, and are listed in the lexicon with field "loan": dollar → **dola**. New concepts are normally built with the word-building markers instead; borrowing is for names of things that have no description, like brands.

## Word building

Four markers turn a verb, or a verb phrase, into a noun that names a role in the action. A marker comes first, like any head. (A blind A/B test decoded these about as well as generic heads like "person teach": 71/76 vs 69/76. They are kept because they are shorter, and because generic heads would erode into exactly such markers anyway; see `tests/wordbuilding-ab-01/`.)

| Marker | Role | Example |
|---|---|---|
| **no** | the one who does it | **no febo** "one who answers" |
| **ge** | the thing it's done to, or what it makes | **ge iko** "what is told" = news, a report |
| **du** | the thing used to do it | **du bubo** "thing for laughing" = a joke |
| **pu** | the place where it's done | **pu niba** "place for walking" = a path |

- **A person it's done to** uses the plain construction **ewo gun** + verb, "person who is …ed": **ewo gun tofo** = student. In the test, **ge** for people was read as a thing ("lesson" for student), and the one-syllable grammar space is full, so there is no separate person marker.
- **The base can be a whole verb phrase:** **no isi se guyi** "one who goes from home" = traveller.
- **With a noun base, state the relation with a relation word:** **musu se yaye** "thing from the sky" = meteorite; **pu pi mabo** "place of paper" = an office. The blind test showed that a bare noun + noun leaves the relation to guesswork, so it's used only for established compounds (`data/compounds.tsv`).
- **No markers are needed for:**
  - action and quality nouns: word position already does it;
  - opposites: **mu**;
  - causatives: **muge**;
  - small and big: **kudu** etc.;
  - gender: a modifier.

  Add a marker only if a test shows one of these failing.
- **Derived words that get frequent may be clipped into new two-syllable roots,** as drift predicts. When that happens, assign the clipped form with the optimizer.

## Conditions, modality, choices and quantities

These are built from existing words; no new grammar words were needed (roadmap B2, 2026-10-08).

- **Conditions use the confidence scale.** Plain **don** "if" is an open condition. Adding **kon** + digit says how likely the speaker thinks it is:
  - **don kon po** "if (and it isn't so)" is counterfactual;
  - **don kon fi** is "if (unlikely)".

  Tense doesn't change; **sin** marks a past event as usual. **don kon po lon sin isi, lon sin nagu wan** = "if I had gone, I would have seen her". There is no separate "would"; the main clause of a condition is understood as its consequence.
- **Modality: three kinds of "can/must", kept apart.**
  - Ability: **lanu** "can, be able to".
  - Obligation: **keya** "must, have to", **wupi** "need to".
  - Permission: **efon** "allow". "May" is **gun efon** "is allowed": **me gun efon nawi** "you may eat".
  - "Might" and "must" in the sense of *probably* are never modal verbs; they are confidence. "She must be home" is **kon te wan gun mon guyi**. English "must" and "may" each mean two different things; here they can't.
- **Comparison:** **ke** + adjective + **se** + standard (**ke kudu se guyi ben** "bigger than that house"). Less = more of the opposite (**ke meli** "smaller"). Most = **se we** "than all". As … as = **fu** "like" (**kudu fu bu** "as big as it").
- **Choices.**
  - **min … lu …** is a yes/no question about the whole "or": "do you want either?"
  - **… lu … yu.** asks *which*: **me momu osa lu nimo yu.** "water or money, which do you want?" Answer by echoing the choice.
  - **lu X lu Y** is "either X or Y, not both", like French *ou… ou*. Plain **lu** allows both.
- **Quantities.**
  - About: **fu** + number (**ewo fu miko** "about 36 people").
  - Range: **se** X **tun** Y "from X to Y".
  - At least: **pa**. At most: **mu ke se** X "not more than X".
  - Part of a whole: X **pi** Y (**fi pi ka** "one of three", a third). Fractions: the point **mimi**.
  - Occasions: **muyi** + number (**muyi sa** "twice").
- **Small words built from roots:**
  - **wame** "also" works like **na** "only": it covers what follows (**lon wame nagu wan** "I also saw her"; **lon nagu wame wan** "I saw her too").
  - Each other = **nen nen** ("self" doubled widens to mutual).
  - Don't = **tin mu** ….
  - Let's = **so pen** … ("request: we").
  - Not yet = **mu sin**; still = **le**.
  - Whether: **min** inside a **wun** clause (**lon mu lugo wun min …** "I don't know whether …").
  - Purpose: **li** + verb "in order to" (**li bika** "to buy").

## Politeness and routines

Evidence: `research/notes/politeness.md`.

- **ku** adds politeness or deference and nothing else. Repeat it for more: **ku ku**, **ku ku ku**. It will wear down: every dedicated politeness word does (English *please*), and polite pronouns cycle every 150–300 years. When plain **ku** stops sounding polite, **ku ku** becomes the ordinary polite form. The renewal stays in its own slot.
- **No polite pronouns and no speech levels.** **me** is "you" to anyone. Respect is **ku** plus how you address someone: a name (**en …**) or a role word before the name, e.g. **no tofo en mala** "Teacher Mara". Address words can be replaced when they wear out; pronouns can't.
- **Politeness never changes what you're doing.**
  - A polite instruction is **tin ku**; a very polite warning is **yo ku ku**.
  - Hints, questions, advice (**fon**) and low confidence numbers are never used to be polite. In accident reports the danger is a junior hinting where they should warn, and hints are judged *less* polite than clear requests anyway.
  - The pattern crews rated most effective: state the problem, name the act, say what *we* need. **yo ku, osa le obu. fon ku, pen wupi isi.** "(Warning, politely) the water is coming. (Advice, politely) we need to go."
- **In an emergency (yo yo), ku isn't expected.** Leaving it out is urgent, not rude.
- **Routines** (none is required; people in many languages rarely thank in everyday requests):
  - greeting: **upe**, optionally with the time of day (**upe leso** "good morning");
  - farewell: **upe isi** "go well";
  - thanks: **lota**;
  - sorry: **sepi**.

## Rules the principles don't cover

1. **Speech acts:** question **min**, request **so**, instruct **tin**, advise **fon** (the decision stays with you), intend **de**, warn **yo**, not literal **a**, exclaim **ba**. **ku** adds politeness or deference and nothing else: it changes no truth, confidence or speech act. It goes right after the speech-act particle, or first in a statement (**so ku …** "please …"). Only a linker to the previous sentence, a scene-setting phrase, or an **if**/**when** clause may come before the particle (**gi tan, tin …** "so, do …"; **don …, de …** "if …, I will …"). A clause-final **min** is a tag: "…, right?"
2. **Confidence is a number of sixths:** **kon** + digit = how many chances in 6 that the statement is true (**kon da** = 4 in 6, about 67%). Seven levels, 0 to 6 (**kon nobi** = 6 in 6, certain), match the about 7 bands ordinary forecasters can use without losing accuracy (Friedman et al. 2018). Extremes take a digit after the point: **kon te mimi ka** = 5.3 in 6 in base 6, i.e. 5½ in 6, about 92%. **kon bo** = "don't know how sure". It is never used for emphasis; that's what **bi** and **ba** are for.
3. **Source is optional:** **o** seen, **fen** told, **san** inferred.
4. **There are no words for yes and no; answers echo the verb.** "Aren't you coming?" → **obu** "coming" / **mu obu** "not coming". Acknowledgment: **mm** = heard, an echo = understood, **de** + verb = will do.
5. **Questions:** question words stay where the answer would go: **me momu wun lon oyi yu.** "you want me to say what?". They are built from parts: **yu** what, **ewo yu** who, **gi yu** why, **fu yu** how. **yu** inside a **wun** clause is an indirect question ("I don't know what I did").
6. **Reference:**
   - **People and animals:** **wan** = the most recent person or animal that was the subject of a clause (if none yet, the most recent one mentioned); **yi** = the one before that, the next most recent *different* one. Anyone further back is named again. Two details: a pronoun never means the subject of its own clause (that's **nen**), so in "the dog saw him", *him* is the most recent subject *before* the dog; and a say-verb that frames a quote ("…," **en benu oyi**) doesn't count, so a quote split by a speech tag keeps its references. The rule is mechanical, so children can compute it and speaker and listener can't disagree.
   - **Things:** **bu** = "it", the most recent thing mentioned.
   - In reported speech or thought, **sun** = the person whose words are reported.
   - **go** = anyone (generic); **me** is only ever the listener.
   - **nen** = self, for any person: **lon yonnu nen** "I held myself back", **feme la … pi nen** "the feelings … of themselves".
7. **"Is" (gun),**
   - **gun** + adjective: **guyi gun kudu** "the house is big" (**guyi kudu** is only "the big house").
   - **gun** + noun: **wan gun tiwu** "she is a child".
   - **gun** + **wun** clause: "is that…".
   - **gun** + place phrase: "is at/in": **wan gun mon guyi** "he is at home".
   - **gun** + verb = the resulting state: **gun tapi** "is closed".
   - After another verb, **gun** = "to be": **momu gun tiwu** "want to be a child".
   - Only at the very start of a sentence, with no subject, does **gun** mean "there is".
8. **Prepositions:**
   - A prepositional phrase attaches to its clause's main verb, never to a modifier.
   - A preposition can take a clause (**wo wan la yidu go** "after they take someone") or a verb that names the act (**se kusa** "from leaving").
   - **ya** alone = "first, beforehand".
   - To give a *noun* a location, use a relative clause: **sola man gun mon bige pi yolan** "the road that is above the river" (a bridge). A bare place phrase after a noun attaches to the verb instead (rule above).
   - **nin** + noun phrase = during (**nin dili nobi fi** "for seven days").
   - A phrase setting time or place may open the sentence (**mon muyi fa, …** "at no time, …"). It sets the scene and changes no roles.
9. **Time:** tense is optional. A narrative sets its time once (**afe …**, or **sin** on its first verb) and then leaves tense unmarked. Aspect: **sin** done, **le** ongoing, **win** about to. Time words name an anchor plus an offset, and the offset always names its unit: **wuma wo dili fi** "tomorrow after one day" = the day after tomorrow. With no anchor, the anchor is now: **wo nelon fi** "after one week" = next week. A time point is an amount elapsed, said as a label: the clock is the fraction of the day (**mon mimi ka da ka** "at .343" = 15:00), the date the days elapsed in the year, always four digits (**dili pi po te ka sa**), the year the years since year 0 (**fawu pi fi ka ka**), a weekday one digit (**dili pi ka**). A duration is a count (**aya ka** "three watches", 12 h). Age is lived time: **lon nume fawu te nobi** "I have lived 30 years". Words and the calendar: [measurement.md](measurement.md#time-and-calendar). Never a "move forward" metaphor. Roots: **eda** now, **mefa** today, **wuma** tomorrow, **afe** yesterday.
10. **Numbers are base 6.** The six digits are one syllable each; there is no second form. Larger numbers are built from place words: 6 **nobi**, 36 **miko**, 216 **niyu**, and groups of four places, 6⁴ = 1296 **yiyo**, 6⁸ **gife**, 6¹² **yuli**, which play the role "thousand" and "million" play in decimal. Why base 6: `docs/number-base.md`.
    - **Quantity reading:** place words in descending order, each preceded by its digit; a digit 1 before a place word is dropped: 7 = **nobi fi** ("six one"), 42 = **miko nobi** (36 + 6), 100 = **sa miko da nobi da** (2·36 + 4·6 + 4).
    - **Digit reading:** digit by digit, in groups of four from the right. Used for identifiers, phone numbers, codes, clock times and dates, and whenever the exact digits matter more than the size. Fixed groups let a listener notice a missing digit.
    - **Fractions:** **mimi** "point" separates the fraction digits: 1/2 = **po mimi ka** (0.3 in base 6), 1/3 = **po mimi sa**. **guti** = minus.
    - Noun + number = count (**dili nobi fi** "seven days"); noun + **pi** + number = label or order (**lite pi po** "step zero"; **aya pi ka** "watch three", noon to 16:00).
11. **Dropped subjects** are allowed only when the subject repeats after **yen** / **un**, or for the addressee of an instruction or request.
12. **Direct quotes** are framed by a say-verb; there's no quote particle. In writing, quotes take quotation marks and a broken-off word ends in a dash.
13. **Degree words** (**ke** more, **bi** very, **to** rather) come before what they modify: **ke kudu** "bigger".
    - **Comparison:** **ke** + adjective + **se** ("from") + the standard: **wan gun ke gole se pen** "he is smarter than us". Most = **ke** … **se we** "more … than all".
    - **How much, how many:** **wifu yu** "number what": **gun nimo wifu yu.** "how much money is there?"
14. **Two objects:** verb + recipient + thing: **tofo me nuta** "teach you fear".

15. **Clause attachment** (tested on contract language, `tests/backtranslation-04-nesting/`):
    - A relative clause (**man …**) attaches to the nearest noun before it.
    - A clause of time, reason or condition (**nin**, **ya**, **wo**, **gi**, **don** …) at the **start** of a sentence belongs to the main clause. At the **end**, it belongs to the innermost clause before it. So **nin leso, lon sin miya ewo man sigo** = "in the morning, I watched the person who came back" (the watching was in the morning), while **lon sin miya ewo man sigo nin leso** = "I watched the person who came back in the morning" (the coming back was in the morning).
    - A pause (a comma in writing) goes wherever a phrase could otherwise run on. That means three places: after a fronted clause; at the end of a subject that contains a clause, before its verb (**no sanwa man … sin sege, keya unfu …**); and between a recipient and a long object.
    - There is no clause-closing word. Add one (two syllables, since the one-syllable space is full) if a blind test shows attachment failing despite these rules.

## Grammar words

| Group | Words |
|---|---|
| Speech acts | question **min** · request **so** · instruct **tin** · advise **fon** · intend **de** · warn **yo** · not literal **a** · exclaim **ba** · polite **ku** |
| Operators | NOT **mu** · which? **yu** · unspecified **bo** · confidence **kon** · seen **o** · told **fen** · inferred **san** · only **na** · at least **pa** |
| Pronouns | I **lon** · you **me** · we incl. you **pen** · we excl. you **din** · he/she **wan** · the other one **yi** · it **bu** · logophoric **sun** · anyone **go** · self **nen** |
| Determiners | plural **la** · this **tan** · that **ben** · all **we** · some **in** · some-not-all **kin** · none **fa** |
| Degree | more **ke** · very **bi** · rather **to** |
| Aspect | done **sin** · ongoing **le** · about to **win** |
| Relations | of **pi** · at **mon** · to **tun** · from **se** · with **gan** · for **li** · before **ya** · after **wo** · like **fu** |
| Linkers | and **yen** · or **lu** · but **un** · if **don** · because **gi** · that (said that) **wun** · who/which **man** · while **nin** |
| Copula | is **gun** |
| Names | name article **en** |

Determiners, like other modifiers, follow the noun: **guyi tan** "this house", **wan la** "they".

## Numbers

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 36 | 216 | 6⁴ | 6⁸ | 6¹² | point | minus |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **po** | **fi** | **sa** | **ka** | **da** | **te** | **nobi** | **miko** | **niyu** | **yiyo** | **gife** | **yuli** | **mimi** | **guti** |

Fractional groups: 6⁻⁴ **kufe**, 6⁻⁸ **bafo**. Any other power: **unun** "power" + exponent. Units and how to say measurements: [measurement.md](measurement.md).

## Vocabulary

[../data/lexicon.tsv](../data/lexicon.tsv) holds 447 roots (including 20 measurement units) plus numbers, each with its semantic field and frequency tier. [../data/compounds.tsv](../data/compounds.tsv) lists established compounds. Add words with `tools/words.py`. All words were rebuilt once on 2026-10-08 under the drift rules; from here on, existing words don't move.

## How much to trust the sound choices

The word forms were chosen by a mishearing model. Its consonant data are real: English listeners in noise (Miller & Nicely 1955). Its vowels, its l/w/y, its final -n and the drift predictions are estimates. Its scores measure the model against itself and have not been checked against real listeners.

## Open questions

- The test texts, the listener data and the concept list are all English-centred. "Universal" is a goal, not yet a result.
- The vocabulary lacks modern-world concepts (machines, medicine, money systems, science).
- Do confirmation and speech-act particles survive native use, or wear away?
- The frequency tiers are judgment, not cross-linguistic data.

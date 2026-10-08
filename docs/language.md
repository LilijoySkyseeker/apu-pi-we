# The language: current reference

This is the current state. Reasons and history are in [design-log.md](design-log.md); evidence is in [../research/](../research/).

**What it is:** a thought experiment in designing a universal human language for modern Earth from first principles. It's imagined as a *native* language, one that children grow up speaking, so the only fixed constraints are human: mouth, ear, memory, attention.

**Goal:** faithful transmission of thought, at a cost speakers will actually pay. When features conflict, this decides.

## Six principles

Most of the grammar follows from these. The rules after them are the cases the principles don't cover.

1. **The common case costs nothing.** Statements, ordinary belief, unknown source, the main character, and present-or-unspecified time are all unmarked. Only departures from the default cost a word. Frequent meanings get the shortest words.
2. **Heads come first, and position carries role.** The order is subject, verb, object. Anything that modifies a word follows it: adjectives after nouns, verbs after nouns (**Ewo NIba** "walking person"), one verb after another (**GOyu PUme** "sit thinking" = meditate), noun after noun (**DINbu LUmi** "snake fire" = dragon). Nothing moves, not even question words, so a listener who loses one word can still tell who did what.
3. **Operators cover what follows them.** The speech-act particle at the start covers the sentence. NOT, confidence, source, ONLY, AT LEAST and degree words cover the clause when they start it, or a single word when placed before it.
4. **Heavy goes last.** A noun's own modifiers come before its "of" phrase (**LUgo to MEli pi KIma** "rather little knowledge of sticks"). In a causative, the result comes before the object (**MUge BONko me** "make angry you"). Long clauses go to the end of the sentence ("there's a good idea: that one hits…"). Relative clauses have no end marker, so nothing may follow them in their phrase.
5. **Doubling widens or strengthens.** **yo yo** = emergency. **a** = this sentence is not literal; **a a** = the whole turn. **mu mu** = emphatic NOT. **ku ku** = extra deference.
6. **Every social pressure gets its own outlet.** Emphasis has **ba**, **bi** and doubling; politeness has **ku**. People will always need to stress, soften and show respect. If those needs had no channel of their own, they would wear down the precision words instead (see [drift.md](drift.md)). So the confidence numbers are never used for emphasis, and the speech acts and hedges are never used for politeness.

## Sounds

- **Vowels:** a e i o u.
- **Consonants (13):** p b t d k g · m n · f s · l w y. Only three places in the mouth (lips, tongue tip, back of tongue), because place is the cue noise destroys first. /v/ and /z/ were deleted: both are rare worldwide, /v/ is easily confused with /b/ and tends to merge with /w/, and /s/–/z/ tends to merge. Removing /z/ cost almost nothing at a 3,000-root scale.
- **Syllables:** (C)V(n). A vowel-only syllable may appear only at the start of a word. The only syllable-final consonant is n.
- **Stress:** the first syllable of every content word; grammar words are unstressed. Stress marks where each content word begins. It is a pitch movement at the start of the syllable, not extra length, because listeners hear lengthening as the *end* of a word. Every syllable keeps its full vowel: the rhythm is syllable-timed, like Spanish or Japanese, not stress-timed like English.
- **Harmless variants:** k and g may sound like "ch" and "j" before i and e; a vowel plus n may become a nasal vowel; consonants between vowels may soften. The vocabulary is built so these changes never merge two words.
- **No tones.** Pitch is free for intonation and emotion.
- **Interjections outside the system:** **mm** "heard you", **huh?** "say again".
- **Writing:** plain lowercase, since stress is predictable. Numbers are written with base-6 digits (0–5), so a written number is never confused with a word. Teaching examples capitalize the stressed syllable: **Ewo**, **Alun**, **LUgo**.

## Words

- Grammar words have one unstressed syllable; content words have two or more, stressed on the first. The one exception is the six digits: one syllable, stressed. No content word begins with a digit's syllable, so a digit followed by a grammar word can never sound like a content word. Every meaning is a separate word that never changes: no endings, no agreement, no case, no gender.
- Content words with similar or opposite meanings are given forms that sound as different as possible, because context can't tell them apart.
- **Built for drift:** no two content words may become the same after the changes a language like this is likely to undergo: later syllables blurring e/i and o/u, middle consonants voicing, a final n melting away. Grammar words that can stand in the same slot start with different consonants, so they stay apart even if their vowels weaken.
- **A word's role comes from its position.** Any content word can be a noun, verb or modifier: **SEpi** "apologize / an apology", **MIya BONko** "look angrily / an angry look". After a verb, a modifier describes the manner: **Oyi FANse** "say calmly".
- **Verb + verb:** if the first verb can take an object (want, try, need, must, can, start, stop, teach…), the second is that object: **WAlo Alun** "try to break". Otherwise the second describes the first: **GOyu PUme** "sit thinking".
- **MUge** is "do", and also the causative "make". The order tells them apart: **MUge Upe tan** (result, then object) = "make this good, fix it"; **MUge tan Upe** (object, then manner) = "do this well".
- Compounds are ordinary phrases that stuck; the established ones are listed in [../data/compounds.tsv](../data/compounds.tsv). To list nouns rather than modify one with another, use **yen** "and": **MOle yen WEde** "mother and father".
- **Gender is a modifier**, stated once when it matters: **Ewo WUNgu FUta** "the commander, a woman". After that, **wan** carries her.
- **Emphasis and contrast** have no special device yet. Back-translation test 02 showed parallel sentences carry contrast on their own ("**lon mu YIdu bu. TOmasa YIdu bu.**" = "*I* didn't take it, *Tomas* did"). Add a focus particle if a test shows contrast being lost.
- **The curse word GEfo** fits any content-word slot: a verb (**ba GEfo me** "fuck you"), a modifier (**LUkan GEfo** "fucking head"), or after **yu** (**yu GEfo** "what the fuck").
- **Loanwords** are adapted the same way as names and listed in the lexicon with field "loan": dollar → **DOla**.
- **Names** are adapted: a foreign sound becomes the native sound listeners most often hear it as (th → f, per Miller & Nicely 1955), and a final consonant gets an echo vowel. Lilith → **LIlifi**.

## Word building

Four markers turn a verb, or a verb phrase, into a noun that names a role in the action. A marker comes first, like any head. (A blind A/B test decoded these about as well as generic heads like "person teach": 71/76 vs 69/76. They are kept because they are shorter, and because generic heads would erode into exactly such markers anyway; see `tests/wordbuilding-ab-01/`.)

| Marker | Role | Example |
|---|---|---|
| **no** | the one who does it | **no FEbo** "one who answers" |
| **ge** | the thing it's done to, or what it makes | **ge Iko** "what is told" = news, a report |
| **du** | the thing used to do it | **du BUbo** "thing for laughing" = a joke |
| **pu** | the place where it's done | **pu NIba** "place for walking" = a path |

- **A person it's done to** uses the plain construction **Ewo gun** + verb, "person who is …ed": **Ewo gun TOfo** = student. In the test, **ge** for people was read as a thing ("lesson" for student), and the one-syllable grammar space is full, so there is no separate person marker.
- **The base can be a whole verb phrase:** **no Isi se GUyi** "one who goes from home" = traveller.
- **With a noun base, state the relation with a relation word:** **MUsu se YAye** "thing from the sky" = meteorite; **pu pi MAbo** "place of paper" = an office. The blind test showed that a bare noun + noun leaves the relation to guesswork, so it's used only for established compounds (`data/compounds.tsv`).
- **No markers are needed for:**
  - action and quality nouns: word position already does it;
  - opposites: **mu**;
  - causatives: **MUge**;
  - small and big: **KUdu** etc.;
  - gender: a modifier.

  Add a marker only if a test shows one of these failing.
- **Derived words that get frequent may be clipped into new two-syllable roots,** as drift predicts. When that happens, assign the clipped form with the optimizer.

## Rules the principles don't cover

1. **Speech acts:** question **min**, request **so**, instruct **tin**, advise **fon** (the decision stays with you), intend **de**, warn **yo**, not literal **a**, exclaim **ba**. **ku** adds politeness or deference and nothing else: it changes no truth, confidence or speech act. It goes right after the speech-act particle, or first in a statement (**so ku …** "please …"). Only a linker to the previous sentence, a scene-setting phrase, or an **if**/**when** clause may come before the particle (**gi tan, tin …** "so, do …"; **don …, de …** "if …, I will …"). A clause-final **min** is a tag: "…, right?"
2. **Confidence is a number of sixths:** **kon** + digit = how many chances in 6 that the statement is true (**kon DA** = 4 in 6, about 67%). Seven levels, 0 to 6 (**kon NObi** = 6 in 6, certain), match the about 7 bands ordinary forecasters can use without losing accuracy (Friedman et al. 2018). Extremes take a digit after the point: **kon TE MImi KA** = 5.3 in 6 in base 6, i.e. 5½ in 6, about 92%. **kon bo** = "don't know how sure". It is never used for emphasis; that's what **bi** and **ba** are for.
3. **Source is optional:** **o** seen, **fen** told, **san** inferred.
4. **There are no words for yes and no; answers echo the verb.** "Aren't you coming?" → **Obu** "coming" / **mu Obu** "not coming". Acknowledgment: **mm** = heard, an echo = understood, **de** + verb = will do.
5. **Questions:** question words stay where the answer would go: **me MOmu wun lon Oyi yu?** "you want me to say what?". They are built from parts: **yu** what, **Ewo yu** who, **gi yu** why, **fu yu** how. **yu** inside a **wun** clause is an indirect question ("I don't know what I did").
6. **Reference:**
   - **People and animals:** **wan** = the most recent person or animal that was the subject of a clause (if none yet, the most recent one mentioned); **yi** = the one before that, the next most recent *different* one. Anyone further back is named again. Two details: a pronoun never means the subject of its own clause (that's **nen**), so in "the dog saw him", *him* is the most recent subject *before* the dog; and a say-verb that frames a quote ("…," **BEne Oyi**) doesn't count, so a quote split by a speech tag keeps its references. The rule is mechanical, so children can compute it and speaker and listener can't disagree.
   - **Things:** **bu** = "it", the most recent thing mentioned.
   - In reported speech or thought, **sun** = the person whose words are reported.
   - **go** = anyone (generic); **me** is only ever the listener.
   - **nen** = self, for any person: **lon YONnu nen** "I held myself back", **FEme la … pi nen** "the feelings … of themselves".
7. **"Is" (gun):**
   - **gun** + adjective: **GUyi gun KUdu** "the house is big" (**GUyi KUdu** is only "the big house").
   - **gun** + noun: **wan gun TIwu** "she is a child".
   - **gun** + **wun** clause: "is that…".
   - **gun** + place phrase: "is at/in": **wan gun mon GUyi** "he is at home".
   - **gun** + verb = the resulting state: **gun TApi** "is closed".
   - After another verb, **gun** = "to be": **MOmu gun TIwu** "want to be a child".
   - Only at the very start of a sentence, with no subject, does **gun** mean "there is".
8. **Prepositions:**
   - A prepositional phrase attaches to its clause's main verb, never to a modifier.
   - A preposition can take a clause (**wo wan la YIdu go** "after they take someone") or a verb that names the act (**se KUsa** "from leaving").
   - **ya** alone = "first, beforehand".
   - **nin** + noun phrase = during (**nin DIli NObi FI** "for seven days").
   - A phrase setting time or place may open the sentence (**mon MUyi fa, …** "at no time, …"). It sets the scene and changes no roles.
9. **Time:** tense is optional. A narrative sets its time once (**afe …**, or **sin** on its first verb) and then leaves tense unmarked. Aspect: **sin** done, **le** ongoing, **win** about to. Time words name an anchor plus an offset, and the offset always names its unit: **WUma wo DIli FI** "tomorrow after one day" = the day after tomorrow. Time of day is the fraction of the day, read digit by digit (**mon MImi KA DA KA** "at .343 of the day" = 15:00); a duration is a count (**Aya KA** "three watches", 12 h). See [measurement.md](measurement.md). Never a "move forward" metaphor. Roots: **eda** now, **mefa** today, **wuma** tomorrow, **afe** yesterday.
10. **Numbers are base 6.** The six digits are one syllable each; there is no second form. Larger numbers are built from place words: 6 **NObi**, 36 **MIko**, 216 **NIyu**, and groups of four places, 6⁴ = 1296 **YIyo**, 6⁸ **GIfe**, 6¹² **YUli**, which play the role "thousand" and "million" play in decimal. Why base 6: `docs/number-base.md`.
    - **Quantity reading:** place words in descending order, each preceded by its digit; a digit 1 before a place word is dropped: 7 = **NObi FI** ("six one"), 42 = **MIko NObi** (36 + 6), 100 = **SA MIko DA NObi DA** (2·36 + 4·6 + 4).
    - **Digit reading:** digit by digit, in groups of four from the right. Used for identifiers, phone numbers, codes, clock times and dates, and whenever the exact digits matter more than the size. Fixed groups let a listener notice a missing digit.
    - **Fractions:** **MImi** "point" separates the fraction digits: 1/2 = **PO MImi KA** (0.3 in base 6), 1/3 = **PO MImi SA**. **GUti** = minus.
    - Noun + number = count (**DIli NObi FI** "seven days"); noun + **pi** + number = label or order (**LIte pi PO** "step zero"; **Aya pi KA** "hour three", three o'clock).
11. **Dropped subjects** are allowed only when the subject repeats after **yen** / **un**, or for the addressee of an instruction or request.
12. **Direct quotes** are framed by a say-verb; there's no quote particle. In writing, quotes take quotation marks and a broken-off word ends in a dash.
13. **Degree words** (**ke** more, **bi** very, **to** rather) come before what they modify: **ke KUdu** "bigger".
    - **Comparison:** **ke** + adjective + **se** ("from") + the standard: **wan gun ke GOle se pen** "he is smarter than us". Most = **ke** … **se we** "more … than all".
    - **How much, how many:** **WIfu yu** "number what": **gun NImo WIfu yu?** "how much money is there?"
14. **Two objects:** verb + recipient + thing: **TOfo me NUta** "teach you fear".

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

Determiners, like other modifiers, follow the noun: **GUyi tan** "this house", **wan la** "they".

## Numbers

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 36 | 216 | 6⁴ | 6⁸ | 6¹² | point | minus |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **po** | **fi** | **sa** | **ka** | **da** | **te** | **NObi** | **MIko** | **NIyu** | **YIyo** | **GIfe** | **YUli** | **MImi** | **GUti** |

Fractional groups: 6⁻⁴ **KUfe**, 6⁻⁸ **BAfo**. Any other power: **Unun** "power" + exponent. Units and how to say measurements: [measurement.md](measurement.md).

## Vocabulary

[../data/lexicon.tsv](../data/lexicon.tsv) holds 315 roots (including 20 measurement units) plus numbers, each with its semantic field and frequency tier. [../data/compounds.tsv](../data/compounds.tsv) lists established compounds. Add words with `tools/words.py`. All words were rebuilt once on 2026-10-08 under the drift rules (old-to-new map in `data/rename-2026-10-08.tsv`); from here on, existing words don't move.

## How much to trust the sound choices

The word forms were chosen by a mishearing model. Its consonant data are real: English listeners in noise (Miller & Nicely 1955). Its vowels, its l/w/y, its final -n and the drift predictions are estimates. Its scores measure the model against itself and have not been checked against real listeners.

## Open questions

- The test texts, the listener data and the concept list are all English-centred. "Universal" is a goal, not yet a result.
- The vocabulary lacks modern-world concepts (machines, medicine, money systems, science).
- Do confirmation and speech-act particles survive native use, or wear away?
- The frequency tiers are judgment, not cross-linguistic data.

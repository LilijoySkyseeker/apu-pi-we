# The language: current reference

This is the current state. Reasons and history are in [design-log.md](design-log.md); evidence is in [../research/](../research/).

**What it is:** a thought experiment in designing a universal human language for modern Earth from first principles. It's imagined as a *native* language, one that children grow up speaking, so the only fixed constraints are human: mouth, ear, memory, attention.

**Goal:** faithful transmission of thought, at a cost speakers will actually pay. When features conflict, this decides.

## Five principles

Most of the grammar follows from these. The rules after them are the cases the principles don't cover.

1. **The common case costs nothing.** Statements, ordinary belief, unknown source, the main character, and present-or-unspecified time are all unmarked. Only departures from the default cost a word. Frequent meanings get the shortest words.
2. **Heads come first, and position carries role.** The order is subject, verb, object. Anything that modifies a word follows it: adjectives after nouns, verbs after nouns (**NIte TAlan YUyu** "intruding alien"), one verb after another (**KApo Ife** "sit thinking" = meditate), noun after noun (**BOzen NOwi** "snake fire" = dragon). Nothing moves, not even question words, so a listener who loses one word can still tell who did what.
3. **Operators cover what follows them.** The speech-act particle at the start covers the sentence. NOT, confidence, source, ONLY, AT LEAST and degree words cover the clause when they start it, or a single word when placed before it.
4. **Heavy goes last.** A noun's own modifiers come before its "of" phrase (**Ozi ban Owu on FEbu** "rather little knowledge of sticks"). In a causative, the result comes before the object (**Avu OPun vun** "make angry you"). Long clauses go to the end of the sentence ("there's a good idea: that one hits…"). Relative clauses have no end marker, so nothing may follow them in their phrase.
5. **Doubling widens or strengthens.** **ze ze** = emergency. **san** = this sentence is not literal; **san san** = the whole turn.

## Sounds

- **Vowels:** a e i o u.
- **Consonants (15):** p b t d k g · m n · f v s z · l w y. Only three places in the mouth (lips, tongue tip, back of tongue), because place is the cue noise destroys first.
- **Syllables:** (C)V(n). A vowel-only syllable may appear only at the start of a word. The only syllable-final consonant is n.
- **Stress:** the first syllable of every content word; grammar words are unstressed. Stress marks where each content word begins.
- **No tones.** Pitch is free for intonation and emotion.
- **Interjections outside the system:** **mm** "heard you", **huh?** "say again".
- **Writing:** plain lowercase, since stress is predictable. Teaching examples capitalize the stressed syllable: **NIte**, **LANpu**, **Ozi**.

## Words

- Grammar words have one syllable; content words have two or more. Every meaning is a separate word that never changes: no endings, no agreement, no case, no gender.
- Content words with similar or opposite meanings are given forms that sound as different as possible, because context can't tell them apart.
- **A word's role comes from its position.** Any content word can be a noun, verb or modifier: **YEba** "apologize / an apology", **VOko OPun** "look angrily / an angry look". After a verb, a modifier describes the manner: **GAka ENmo** "say calmly".
- **Verb + verb:** if the first verb can take an object (want, try, need, must, can, start, stop, teach…), the second is that object: **NOnu LANpu** "try to break". Otherwise the second describes the first: **KApo Ife** "sit thinking".
- **Avu** is "do", and also the causative "make". The order tells them apart: **Avu Itu va** (result, then object) = "make this good, fix it"; **Avu va Itu** (object, then manner) = "do this well".
- Compounds are ordinary phrases that stuck; the established ones are listed in [../data/compounds.tsv](../data/compounds.tsv). To list nouns rather than modify one with another, use **gu** "and": **KOnu gu VUge** "mother and father".
- **Gender is a modifier**, stated once when it matters: **NIte GOni DUli** "the commander, a woman". After that, **lu** carries her.
- **The curse word FEzi** fits any content-word slot: a verb (**dun FEzi vun** "fuck you"), a modifier (**PIbi FEzi** "fucking head"), or after **mi** (**mi FEzi** "what the fuck").
- **Names** are adapted: a foreign sound becomes the native sound listeners most often hear it as (th → f, per Miller & Nicely 1955), and a final consonant gets an echo vowel. Lilith → **LIlifi**.

## Rules the principles don't cover

1. **Speech acts:** question **yun**, request **fu**, instruct **gon**, advise **to** (the decision stays with you), intend **zin**, warn **ze**, not literal **san**, exclaim **dun**. Only a linker to the previous sentence may come before the particle (**win va, gon …** "so, do …"). A clause-final **yun** is a tag: "…, right?"
2. **Confidence is a number:** **mon** + digit = chance in 10 that the statement is true (**mon Ayon** = 7 in 10). A second digit handles extremes (**mon ENge NEnon** = 95%). **mon wan** = "don't know how sure".
3. **Source is optional:** **kin** seen, **sun** told, **ven** inferred.
4. **There are no words for yes and no; answers echo the verb.** "Aren't you coming?" → **Ime** "coming" / **na Ime** "not coming". Acknowledgment: **mm** = heard, an echo = understood, **zin** + verb = will do.
5. **Questions:** question words stay where the answer would go: **vun ZIzi yo e GAka mi?** "you want me to say what?". They are built from parts: **mi** what, **NIte mi** who, **win mi** why, **wo mi** how. **mi** inside a **yo** clause is an indirect question ("I don't know what I did").
6. **Reference:**
   - Once a second third person is in play, plain **lu** = the main character and **tan** = anyone or anything else. Importance decides, not animacy: if the commander is the main character, her reaction is **tan**. This is obligatory.
   - In reported speech or thought, **gan** = the person whose words are reported.
   - **pen** = anyone (generic); **vun** is only ever the listener.
   - **ku** = self, for any person: **e SIdo ku** "I held myself back", **NUvu in … on ku** "the feelings … of themselves".
7. **"Is" (la):**
   - **la** + adjective: **Iwa la ZUvo** "the house is big" (**Iwa ZUvo** is only "the big house").
   - **la** + noun: **lu la TAde** "she is a child".
   - **la** + **yo** clause: "is that…".
   - **la** + verb = the resulting state: **la FEson** "is closed".
   - After another verb, **la** = "to be": **ZIzi la TAde** "want to be a child".
   - Only at the very start of a sentence, with no subject, does **la** mean "there is".
8. **Prepositions:**
   - A prepositional phrase attaches to its clause's main verb, never to a modifier.
   - A preposition can take a clause (**tun lu in WIye pen** "after they take someone") or a verb that names the act (**gen FOta** "from leaving").
   - **fi** alone = "first, beforehand".
   - **zan** + noun phrase = during (**zan ONo AYon** "for seven days").
   - A phrase setting time or place may open the sentence (**yi DOye bon, …** "at no time, …"). It sets the scene and changes no roles.
9. **Time:** tense is optional. A narrative sets its time once (**zafo …**, or **fa** on its first verb) and then leaves tense unmarked. Aspect: **fa** done, **gi** ongoing, **yan** about to. Time words name an anchor plus an offset, never a "move forward" metaphor. Roots: **ibo** now, **zume** today, **ili** tomorrow, **zafo** yesterday.
10. **Numbers** are base 10 and fully regular ("ten one" = 11), with two syllables each. Base 10 matches finger counting and the decimal system the modern world already runs on. Noun + number = count (**ONo AYon** "seven days"); noun + **on** + number = label or order (**PEpa on DONma** "step zero").
11. **Dropped subjects** are allowed only when the subject repeats after **gu** / **fen**, or for the addressee of an instruction or request.
12. **Direct quotes** are framed by a say-verb; there's no quote particle. In writing, quotes take quotation marks and a broken-off word ends in a dash.
13. **Degree words** (**u** more, **we** very, **ban** rather) come before what they modify: **u ZUvo** "bigger".
14. **Two objects:** verb + recipient + thing: **BUfo vun BOsi** "teach you fear".

## Grammar words

| Group | Words |
|---|---|
| Speech acts | question **yun** · request **fu** · instruct **gon** · advise **to** · intend **zin** · warn **ze** · not literal **san** · exclaim **dun** |
| Operators | NOT **na** · which? **mi** · unspecified **wan** · confidence **mon** · seen **kin** · told **sun** · inferred **ven** · only **bin** · at least **wun** |
| Pronouns | I **e** · you **vun** · we incl. you **nin** · we excl. you **so** · he/she/it **lu** · obviative **tan** · logophoric **gan** · anyone **pen** · self **ku** |
| Determiners | plural **in** · this **va** · that **nun** · all **len** · some **vi** · some-not-all **kon** · none **bon** |
| Degree | more **u** · very **we** · rather **ban** |
| Aspect | done **fa** · ongoing **gi** · about to **yan** |
| Relations | of **on** · at **yi** · to **ke** · from **gen** · with **zo** · for **men** · before **fi** · after **tun** · like **wo** |
| Linkers | and **gu** · or **be** · but **fen** · if **ti** · because **win** · that (said that) **yo** · who/which **mu** · while **zan** |
| Copula | is **la** |

Determiners, like other modifiers, follow the noun: **Iwa va** "this house", **lu in** "they".

## Numbers

0 **donma** · 1 **tugun** · 2 **suki** · 3 **wumun** · 4 **tumin** · 5 **nenon** · 6 **livan** · 7 **ayon** · 8 **digun** · 9 **enge** · 10 **newen** · 100 **tonvu** · 1000 **senni**

## Vocabulary

[../data/lexicon.tsv](../data/lexicon.tsv) holds 284 roots plus numbers, each with its semantic field and frequency tier. [../data/compounds.tsv](../data/compounds.tsv) lists established compounds. Add words with `tools/words.py`; existing words never move.

## How much to trust the sound choices

The word forms were chosen by a mishearing model. Its consonant data are real: English listeners in noise (Miller & Nicely 1955). Its vowels, its l/w/y and its final -n are estimates. Its scores measure the model against itself and have not been checked against real listeners.

## Open questions

- The test texts, the listener data and the concept list are all English-centred. "Universal" is a goal, not yet a result.
- The vocabulary lacks modern-world concepts (machines, medicine, money systems, science).
- Do confirmation and speech-act particles survive native use, or wear away?
- The frequency tiers are judgment, not cross-linguistic data.

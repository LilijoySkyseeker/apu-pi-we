# Apupiwe: reference
<!-- Generated from spec/reference.toml by tools/spec.py build. Edit the spec, not this file. -->

<span id="r-0-1"></span>This document states what the language is. The reasons for each part are in [rationale.md](rationale.md), its history is in [design-log.md](design-log.md), and the word lists are in the [data folder](https://github.com/LilijoySkyseeker/apupiwe/tree/main/data).

<span id="r-0-2"></span>The language calls itself **apu pi we** "everyone's language", said [ˈapu pi we], roughly AH-poo pee weh, with only the first syllable stressed. Its name in English and other languages is one word, Apupiwe, said the same way. Any language is named with **apu pi** followed by whose language it is.

<span id="r-0-3"></span>Apupiwe is a designed language for people who speak it natively, within the world's existing cultures. Its own grammar is built for native speakers. Where it meets a culture's conventions, such as clocks, calendars, units, names and customs, it carries them. Where conventions conflict and one must be chosen, it follows the international standard.

<span id="r-0-4"></span>What the language is for, and how its criteria are weighed against each other, is set out in [the goal](goal.md).

---

## 1. Principles

1. <span id="r-1-1"></span>The common case costs nothing. Statements, ordinary belief, an unknown source, the topic, and present or unspecified time are unmarked. Frequent meanings have the shortest words.
2. <span id="r-1-2"></span>Heads come first, and position carries role. The order is subject, verb, object. A content word that describes a noun or a verb follows it. Words never move to show their role.
3. <span id="r-1-3"></span>Operators come before what they cover (section 6).
4. <span id="r-1-4"></span>Heavy goes last. A noun's own modifiers come before its **pi** "of" phrase, and long clauses go to the end. Nothing may follow a relative clause in its phrase.
5. <span id="r-1-5"></span>Doubling widens or strengthens any word except a digit in a number: **mu mu** emphatic "not", **nun nun** extra deference, **yo yo** emergency, **genso genso** "the whole turn is not literal", **nen nen** "each other", **feko feko** "exactly so". Doubled **mu** is always emphasis and never means "not not".
6. <span id="r-1-6"></span>Emphasis, politeness, respect and stance have words of their own: **ba** and **bi** for emphasis, **nun** for politeness, **lanno** for respect, and the stance words of section 7.
7. <span id="r-1-7"></span>A precise way always exists, but it need not always be used. Anything the listener can supply may be left out (section 4.5), and any ambiguity can be removed by saying more.

## 2. Sounds

- <span id="r-2-1"></span>The vowels are a e i o u. In the reference pronunciation, every syllable keeps its full vowel.
- <span id="r-2-2"></span>There are 13 consonants: p b t d k g · m n · f s · l w y. They are made at the lips (p b m w, and f with lip and teeth), with the tongue tip (t d n s l), with the tongue body (y) and with the back of the tongue (k g).
- <span id="r-2-3"></span>A syllable has the shape (C)V(n). A syllable with no consonant before its vowel (**a**, **en**) occurs only at the start of a word. The only consonant that can end a syllable is n.
- <span id="r-2-4"></span>Words fall into three types by sound:
  - grammar words have one unstressed syllable (table in section 13), except the two-syllable operators listed after that table, which are stressed on the first like content words;
  - the digits 0–5 have one stressed syllable;
  - every other word has two or more syllables and is stressed on the first.
- <span id="r-2-5"></span>Words never change form. There are no endings, no agreement, no case and no gender.
- <span id="r-2-6"></span>Stress is a higher pitch on the stressed syllable, stepping down after it. In the reference pronunciation it does not lengthen the syllable, and the rhythm is syllable-timed.
- <span id="r-2-7"></span>Across a phrase, each stressed syllable is a little lower than the one before (declination), and pitch resets after a pause.
- <span id="r-2-8"></span>There are no tones. Pitch carries only intonation and emotion. A question needs no rising tone, because its words make it a question, but rising anyway is fine.
- <span id="r-2-9"></span>Some harmless variants are allowed. Before i and e, k and g may sound like "ch" and "j". A vowel plus n may become a nasal vowel. Consonants between vowels may soften. In the reference pronunciation these variants occur inside content words only, and grammar words keep their consonants.
- <span id="r-2-10"></span>**mm** "heard you", **huh?** "say again", and any other interjection or hesitation sound speakers use are outside the sound system and carry no grammar.
- <span id="r-2-11"></span>Native content words never begin with an open syllable identical to a digit (**po fi sa ka da te**). Loans are exempt.

## 3. Writing

- <span id="r-3-1"></span>The letters are a b d e f g i k l m n o p s t u w y, one per sound, with no accents. Digits never appear inside a word. Spelling follows the standard pronunciation, and neither the harmless variants nor stress are written.
- <span id="r-3-2"></span>Lowercase is the standard. Capitals carry no meaning and are harmless.
- <span id="r-3-3"></span>These marks carry grammar:

  | Mark | Use |
  |---|---|
  | `,` | a pause (section 4.6) |
  | `.` | end of a sentence; between digits, the decimal point |
  | `" "` | around quoted speech |

  `?` and `!` are allowed. In the reference variety the words already show what they would mark, so they carry no grammar of their own. `-` and `:` are not used in the language's own words.
- <span id="r-3-4"></span>Some things pass through as written: chat abbreviations and interjections (ok, lol), digits, unit symbols (`5 km`, `20 °C`, `30%`), the local clock notation (`21:30`, `9:30 pm`), ISO dates (`2026-10-10`), letters used as labels, links, email addresses, @handles, #tags, emoji, code, file names, and personal and brand names (section 11). Unit symbols are read aloud by their borrowed names (9.3) and clock notation in the speaker's clock style (8.3). Other notation is read as the speaker's culture reads it.
- <span id="r-3-5"></span>Ordinary writing uses digits for numbers. This reference spells numbers out only to show how they are said. Digits are grouped in threes from the decimal point with a space (`1 250 000`), and `.` is the decimal point.
- <span id="r-3-6"></span>Words are written apart. A phrase said fast keeps its spaces until a fused form actually changes sound and becomes a new word.

## 4. The sentence

### 4.1 Template

<span id="r-4-1-1"></span>A sentence fills these slots in this order. Only the verb, or a fragment (4.5), is required.

<span id="r-4-1-2"></span>

| # | Slot | Contents | Section |
|---|---|---|---|
| 1 | Calling someone | a person word (a name, a title, or a single role or kin word), then a pause | 10.1 |
| 2 | Opener | a linker to the previous sentence (**gi tan** "so"), then a relation phrase that sets the scene (time, place) or a topic **pi X**, then an **if**/**when** clause, each followed by a pause | 4.3 |
| 3 | Speech act | one particle; **genso** or **ba** may come before it | 7.1 |
| 4 | Politeness | **nun**, after the particle or in its place | 10.2 |
| 5 | Clause operators | confidence **kon** + number, source **wanme**/**inwun**/**wemen** | 6.1 |
| 6 | Subject | a noun phrase (section 5) | |
| 7 | Phrase operators, habit, aspect | e.g. **mu**, **fe**, **manni**, **sin** | 6.2, 8.1 |
| 8 | Verb | one verb, or verb + verb; with no object, a bare word right after the verb says how | 4.2 |
| 9 | Objects | recipient, then thing | 4.2 |
| 10 | Relation phrases | **mon**, **tun**, **se**, **gan**, **li**, **fu** … + noun phrase or clause; **fu** + a word says how | 4.4, 4.2 |
| 11 | Trailing clause | **wun**, **gi**, **don**, **nin** … clause | 4.4 |
| 12 | Stance | a pause, then **min**, **a**, **buni**, **donon** … | 7.2 |
| 13 | Calling someone | a pause, then a person word | 10.1 |

### 4.2 The verb and its objects

- <span id="r-4-2-1"></span>For any content word, what you mean decides the clear form:
  - for a state ("is big", "is closed"), use **gun** + word: **guyi gun kudu** "the house is big". A feeling named by an action word is said with the plain verb: **to nuta** "I'm afraid" (I fear);
  - for an event ("walks", "is walking", "walked"), use the word as the verb, with an aspect word when precision matters: **ewo le niba** "the person is walking", **ewo manni niba** "the person (usually) walks", **ewo sin niba** "the person walked";
  - for a description of a noun ("the person who walks", "the house that is big"), use **man**: **ewo man niba**, **guyi man gun kudu**.
- <span id="r-4-2-2"></span>A bare noun followed by a word (**guyi kudu**, **ewo niba**) may be a description or a statement. Context decides, and the clear forms above remove any doubt.
- <span id="r-4-2-3"></span>Any content word can take any role by its position. As an object, or with a derivation marker, it is a noun (**sepi** "apologise / an apology").
- <span id="r-4-2-4"></span>How something is done is said with **fu** "like", an ordinary relation phrase after the verb and its objects: **nawi pasu fu yobe** "eat food quickly". A bare word right after an object describes the object: **nawi pasu yobe** "eat fast food". With no object, a bare word right after the verb describes the action: **oyi fanse** "say calmly".
- <span id="r-4-2-5"></span>With two objects, the recipient comes first and then the thing: **tofo me nuta** "teach you fear".
- <span id="r-4-2-6"></span>When one verb follows another and the first takes an object (want, try, need, must, can, start, stop, teach, see, like, help…), the second verb is that object: **walo alun** "try to break". Otherwise the second verb describes the first: **goyu pume** "sit thinking". Phrases and clauses after a second verb that is an object belong to it, the nearest verb: **momu isi tun guyi** "want to go home".
- <span id="r-4-2-7"></span>**muge** "do; make" followed by a result and then an object means "make (it) so": **muge upe tan** "fix this". Followed by an object and then a **fu** phrase saying how, it means "do (it) so": **muge tan fu upe** "do this well".
- <span id="r-4-2-8"></span>A command needs **tin**, or **so** for a request. Without a particle, a sentence is a statement.

### 4.3 Openers

- <span id="r-4-3-6"></span>A linker is a word or phrase at the start that ties the sentence to the one before it, such as **gi tan** "so", **un** "but" or **yen** "and also".
- <span id="r-4-3-1"></span>Any relation phrase may open the sentence, followed by a pause. A time or place phrase there sets the scene: **mon minfi, …** "at noon, …". An opening phrase changes no roles.
- <span id="r-4-3-2"></span>A topic is **pi** + a noun phrase at the start, meaning "as for X": **pi tale la, no kuwi guyi, yidu bu la.** "As for the cars, the caretaker takes them." At the start, **pi** has no other reading, and the topic runs to its pause, or to **kiyo** "end of phrase", so it can be a list: **pi upe yen yomo,** "as for good and bad,".
- <span id="r-4-3-3"></span>An if/when clause is **don** "if", **nin** "while/when", **wo** "after", **ya** "before" or **gi** "because", followed by a clause.
- <span id="r-4-3-4"></span>When several of these open a sentence, they come in this order: linker, scene or topic, if/when clause. The speech-act particle follows them.
- <span id="r-4-3-5"></span>Only a person word (4.1) calls someone. A longer noun phrase before a pause is the subject (4.6), and a fronted relation phrase or **pi** phrase is a scene or topic phrase.

### 4.4 Clauses and relation phrases

- <span id="r-4-4-1"></span>A relation phrase (**mon**, **tun**, **se**, **gan**, **li**, **ya**, **wo**, **fu**, **nin**, **gi** "because of", and the two-syllable **anko** "until" and **nuwen** "without") at clause level attaches to the clause's verb. Inside a noun phrase, only **pi** attaches to a noun. To give a noun any other relation, use a relative clause: **sola man gun mon bige pi yolan** "the road that is above the river". In comparisons and quantities (9.3), **se**, **tun** and **fu** belong to their number or adjective. After a time, **wo** and **ya** belong to that time (8.2): **to isi mon wuma wo dili fi** "I go the day after tomorrow". **gi** with a noun phrase gives **gi yu** "why" and **gi tan** "so" (because of this).
- <span id="r-4-4-2"></span>A relation word may drop its object when context supplies it, as in **wo** "after that" and **ya** "beforehand". It then ends its clause or comes before a pause.
- <span id="r-4-4-3"></span>A relation word can take a clause (**wo wan la yidu ewo bo** "after they took someone") or an action noun (**se kusa** "from leaving").
- <span id="r-4-4-4"></span>A relative clause attaches to the nearest noun before it. A time, reason or condition clause at the *start* of a sentence belongs to the main clause. At the *end*, it belongs to the innermost clause before it, unless a pause closes that clause first (**kiyo** doesn't, 5.3): **nin leso, to sin miya ewo man sigo** "in the morning, I watched the person who came back"; **to sin miya ewo man sigo nin leso** "I watched the person who came back in the morning". In the same way, a phrase or clause after verbs joined by **yen**, **lu** or **un** belongs to the last of them, and at the start it covers them all: **wan doku yen nawi mon guyi** "he works, and eats at home"; **mon guyi, wan doku yen nawi** "at home, he works and eats".
- <span id="r-4-4-5"></span>**yen** "and", **lu** "or" and **un** "but" join nouns, verbs, modifiers or clauses. Nouns in a list are joined with **yen**: **mole yen wede** "mother and father". **lu X lu Y** means "either X or Y, not both".
- <span id="r-4-4-7"></span>Verbs joined by **yen**, **lu** or **un** are separate predicates. Operators and aspect words before one of them cover only that verb, and an object after the last verb belongs to it: **wan mu nawi yen wopo** "she doesn't eat, and she sleeps"; **to nagu yen yidu bu** "I see (it) and take it".
- <span id="r-4-4-6"></span>A quote is framed by a say-verb, and in writing it goes in quotation marks. It is its own sentence with its own speech-act particle. Broken-off speech just stops.

### 4.5 Leaving things out

- <span id="r-4-5-1"></span>Anything the listener can supply from context may be left out: the subject, the object, the object of a relation word or the verb. An answer or follow-up can be just the new part: **muyi yu? moti?** "what time? again?"; **nagu me la mon dili dife ufo.** "see you all Saturday".
- <span id="r-4-5-2"></span>**gun** with no subject is "(it) is", like any verb with its subject left out: **gun nimo** "(it's) money". With **gun** left out too, a bare state is fine: **bi upe.** "very good." "There is" is **ibe** "have" with no subject (4.7).
- <span id="r-4-5-3"></span>When leaving something out could be unclear, say it.

### 4.6 Pauses

<span id="r-4-6-1"></span>A pause, written as a comma, goes wherever a phrase could otherwise run on. It belongs in these places:
- <span id="r-4-6-2"></span>after someone called at the start, and before someone called at the end;
- <span id="r-4-6-3"></span>after an opener (linker, scene, topic, if/when clause);
- <span id="r-4-6-4"></span>after a subject that contains a clause or a phrasal derived word, before its verb (**no sanwa man … sin sege, keya unfu …**);
- <span id="r-4-6-5"></span>between a recipient and the thing, where it helps: it is optional, and recommended when the thing is several words long or has a relative clause;
- <span id="r-4-6-6"></span>between clauses joined by **yen**, **lu** or **un** when the first ends in a noun, and the same between joined verbs (4.4.7): **to nawi pasu, yen wopo** "I eat food, and sleep";
- <span id="r-4-6-7"></span>before a stance word, and before the choice tag **yu** (4.8);
- <span id="r-4-6-8"></span>between a larger and a smaller calendar unit (**dunan dife yawu, dili dife mape**);
- <span id="r-4-6-9"></span>after a relative clause, to close it before more material (or **kiyo**, 5.3).

<span id="r-4-6-10"></span>In casual writing, pauses that context makes obvious may be dropped.

### 4.7 "Is": gun

- <span id="r-4-7-1"></span>**gun** goes before a state: **guyi gun kudu** "the house is big". Without it, **guyi kudu** is normally read as "the big house".
- <span id="r-4-7-2"></span>**gun** goes before a noun: **wan gun tiwu** "she is a child".
- <span id="r-4-7-3"></span>**gun** goes before a place phrase: **wan gun mon guyi** "he is at home".
- <span id="r-4-7-4"></span>**gun** before an action word gives the state of whoever undergoes the action: **gun tapi** "is closed", **wan gun kuwi** "she is protected", **to gun nuta** "I am feared". This holds for every action word, feelings included; the one who feels takes the plain verb (**to nuta** "I'm afraid").
- <span id="r-4-7-5"></span>**gun** before a **wun** clause means "is that …".
- <span id="r-4-7-6"></span>**gun** with no subject is always "is" or "to be", with the subject understood: **momu gun tiwu** "want to be a child", **go ibe sogan li gun kuwi** "everyone has the right to be protected", **wan obu yen gun simi** "she came and is sick".
- <span id="r-4-7-7"></span>"There is" is **ibe** "have" with no subject, and **ibe** with no subject always means "there is": **ibe pasu** "there's food", **mu ibe pasu** "there's no food", **un, ibe musu feli** "but there are many things", **don ibe pasu** "if there is food". To say someone has it, name them: **to ibe pasu** "I have food".

### 4.8 Questions and answers

- <span id="r-4-8-1"></span>A yes/no question starts with **min**. A **min** at the end of a clause is a tag, "…, right?".
- <span id="r-4-8-2"></span>Question words stay where the answer goes and need no **min**: **me momu wun to oyi yu.** "you want me to say what?"
- <span id="r-4-8-3"></span>Question words are built from **yu**: **yu** what; **ewo yu** who; **X yu** which X; **mon kemu yu** where; **mon muyi yu** when; **gi yu** why; **fu yu** how; **wifu yu** how many/much; **pi ewo yu** whose. **wifu yu** follows its noun the way a number does: **ewo wifu yu** "how many people".
- <span id="r-4-8-4"></span>To offer a choice, ask **min … lu …** "either?", or ask **… lu …, yu** "which?" with a pause before **yu** so it isn't read as "which X". That second kind is answered by echoing the choice.
- <span id="r-4-8-5"></span>An indirect question starts its **wun** clause with **min**, with or without a question word: **to mu lugo wun min wan obu** "I don't know whether she's coming", **to mu lugo wun min ewo yu obu** "I don't know who is coming". Without **min**, a question word anywhere in the sentence makes the whole sentence a question: **me momu wun to oyi yu** "you want me to say what?"
- <span id="r-4-8-6"></span>Answers echo the verb, since there are no words for yes and no: "Aren't you coming?" → **obu** / **mu obu**. A question with **gun** is answered by echoing what follows **gun**: "Is the house big?" → **kudu** / **mu kudu**. To acknowledge, **mm** says you heard, an echo says you understood, and **de** + verb says "will do".

## 5. The noun phrase

### 5.1 Template

<span id="r-5-1-1"></span>A noun phrase runs in this order: noun, content modifiers, number, **la**, determiner, **pi** phrase, relative clause, as in **guyi kudu sa la tan pi en mara man …**. Titles and **lanno** come before the noun (10.1), and phrase operators come before the whole phrase (6.2).

### 5.2 Parts

- <span id="r-5-2-1"></span>Describing words follow the noun: **guyi kudu** "big house". For a clear description, use **man** (5.3).
- <span id="r-5-2-2"></span>Gender is a modifier, stated once when it matters: **tiwu futa** "daughter", **no wungu futa** "the leader, a woman".
- <span id="r-5-2-3"></span>Noun + noun is used only for gender and for the compounds in `compounds.tsv`. Other relations use **pi** or a relative clause.
- <span id="r-5-2-4"></span>Numbers and times can stand alone as noun phrases: **yawu gun upe** "ten is fine", **wuma gun upe** "tomorrow is fine".
- <span id="r-5-2-5"></span>A noun followed by a number is a count (**dili oma** "seven days"). A noun + **dife** + number is a label (**kemin dife sa** "document 2"), and a label also gives a place in order: **gimu dife ka** "the third time", **ewo dife fi** "the first person". "Last" is **pi fugi**, "of the end": **gimu pi fugi** "the last time". With a number before **pi** "of", the phrase is a part: **fi pi ka** "one of three".
- <span id="r-5-2-6"></span>The plural word **la** is optional. A count or context can show plurality.
- <span id="r-5-2-7"></span>There are no articles. Whether something is known or new is left to context, or shown with **tan**, **ben**, **bo** or a number.
- <span id="r-5-2-8"></span>Determiners (table in section 13) and **mesun** "each" follow the noun: **guyi tan** "this house", **ewo bo** "someone", **musu bo** "something", **pu nume mesun** "each home". A determiner right after a noun or pronoun belongs to it. So to give a recipient a determiner standing alone as the thing, use **tun**: **to iko ben tun wan** "I told that to him" (**to iko wan ben** is "I told that-him"). A determiner may stand alone as a noun phrase: **we** "all", **in** "some", **fa** "none". A part of a whole is a determiner or number + **pi** + noun: **kin pi foto la** "some of the photos".
- <span id="r-5-2-9"></span>**pi** "of" links a noun to a noun: **guyi pi en mara** "Mara's house". Each **pi** attaches to the nearest noun before it, and its phrase is the nearest single noun after it, so a list joined by **yen** or **lu** is outside it: **enpa pi pume yen lite pi nosen** is "freedom of thought, and religion". To cover every item, repeat the head: **enpa pi pume yen enpa pi lite pi nosen** "freedom of thought and freedom of religion".
- <span id="r-5-2-10"></span>"One's own" is **pi nen**: **to ibe guyi pi nen** "I have my own house". Since a **pi** phrase holds a single noun, two owners of one thing take a relative clause: **guyi man en mara yen to ibe** "Mara's and my house".

### 5.3 Relative clauses

<span id="r-5-3-1"></span>A relative clause is **man** + clause, placed after the noun. The noun fills the role missing from the clause:
- <span id="r-5-3-2"></span>subject: **ewo man niba** "the person who walks";
- <span id="r-5-3-3"></span>object: **mabo man me la yaga** "the papers you put";
- <span id="r-5-3-4"></span>place or time, with the relation word at the end of the clause: **kemu man to nume mon** "the place where I live";
- <span id="r-5-3-6"></span>any other relation, the same way: **yetu man to fonsu gan** "the tool I cut with";
- <span id="r-5-3-7"></span>"whose", with **pi** + the pronoun that fits the noun (**pi wan**, **pi bu**, **pi wan la**) inside the clause pointing back to it: **ewo man guyi pi wan gun kudu** "the person whose house is big", **guyi man beya pi bu gun tapi** "the house whose door is closed".

<span id="r-5-3-8"></span>If both the subject and the object are missing, the noun is the subject: **ewo man nagu** "the person who sees". For "the person I see", keep the subject: **ewo man to nagu**.

<span id="r-5-3-5"></span>A relative clause attaches to the nearest noun or pronoun before it, so after a **pi** phrase it describes the **pi** noun. To describe the head instead, put a quality before the **pi** phrase or use a new sentence. A pause, or the word **kiyo** "end of phrase", closes it, along with every relative clause still open: **to sin miya ewo man sigo kiyo nin leso** "I watched the person who came back, in the morning". **kiyo** is optional; use it where a missed pause could mislead. It closes only the phrases that run on: relative clauses, phrasal derived words (5.4) and topics (4.3). A trailing clause (4.4.4) is closed by a pause.

### 5.4 Derived words

<span id="r-5-4-1"></span>Four markers before a verb or verb phrase name a role in the action:

<span id="r-5-4-2"></span>

| Marker | Role | Example |
|---|---|---|
| **no** | the one who does it | **no febo** "one who answers" |
| **ge** | the thing done or made | **ge iko** "what is told" = news |
| **du** | the thing used | **du bubo** "thing for laughing" = a joke |
| **pu** | the place | **pu niba** "place for walking" = a path |

- <span id="r-5-4-3"></span>A **pi** phrase after a derived word belongs to the last noun inside its base, or to the derived word itself if its base has no noun: **du kuwi pi to** "my thing for keeping".
- <span id="r-5-4-4"></span>The base may be a verb phrase: **no isi se guyi** "one who goes from home", a traveller. It runs to the end of its phrase, like a relative clause, and a pause or **kiyo** separates it from a following verb. It also ends before a name (**en** …) or a gender word (**futa**, **lowu**), so **no tofo en mara** is "Teacher Mara" and **no wungu futa** "the leader, a woman".
- <span id="r-5-4-5"></span>A person something is done to is **ewo man gun** + verb: **ewo man gun tofo** "a student".
- <span id="r-5-4-6"></span>A noun base is linked with **pi** or a verb: **pu pi mabo** "an office", **no obu se yaye** "an alien".
- <span id="r-5-4-7"></span>For opposites, **mu** + word means "not X" (**mu upe** "not good"), and a separate opposite root names the other pole (**yomo** "bad").

## 6. Operators

### 6.1 Clause operators

<span id="r-6-1-1"></span>Clause operators start the clause (slot 5) and cover all of it.
- <span id="r-6-1-2"></span>Confidence is **kon** + a number of sixths, the chance in 6 that the statement is true: **kon po** impossible, **kon fi** unlikely, **kon sa** doubtful, **kon ka** even odds, **kon da** likely, **kon te** very likely, **kon ufo** certain; **kon te mimi te** 5.5 in 6; **kon bo** "maybe, possibly", with no particular chance in mind: **kon bo wan obu** "maybe she's coming". An unmarked statement is believed. Exact probabilities use a number and **pasentu**.
- <span id="r-6-1-3"></span>Source is optional: **wanme** seen, **inwun** told, **wemen** inferred.
- <span id="r-6-1-4"></span>"Might" and "must" in the sense of *probably* are a matter of confidence: "She must be home" is **kon te wan gun mon guyi**.

### 6.2 Phrase operators

<span id="r-6-2-1"></span>Phrase operators cover the word or phrase right after them, including a phrase that opens the sentence (**na mon funti, …** "only in the community, …"). Before the verb, they cover the predicate, which is the verb with everything after it in its clause. To negate a single phrase, put **mu** before that phrase: **wan doku mu mon guyi** "she works, but not at home".
- <span id="r-6-2-2"></span>**mu** not (**to mu yidu bu** "I don't/didn't take it"; **mu mu** emphatic);
- <span id="r-6-2-3"></span>**na** only; **fe** also; **wi** even (**wi don** "even if"); **o** focus, "this one, not another" (**o en tomas sin yidu bu** "*Tomas* took it"; before the verb it insists: **to o unfu** "I *did* pay");
- <span id="r-6-2-4"></span>to add a whole statement ("also, …"), start with **yen**; **fe** before the verb means the subject also does it;
- <span id="r-6-2-5"></span>**konsin** at least; **nedin** almost;
- <span id="r-6-2-6"></span>degree words **ke** more, **bi** very, **tason** rather (**ke kudu** "bigger"; **nimo ke uyo** "less money").
- <span id="r-6-2-7"></span>Before the verb, the order is phrase operators, then **manni**, then aspect, then the verb: **to fe manni le doku**. The one exception is **le mu** "still not" (8.1).

## 7. Speech acts and stance

### 7.1 Speech acts (slot 3)

<span id="r-7-1-1"></span>

| Particle | Act |
|---|---|
| **min** | yes/no question |
| **so** | request; with another subject, a wish (**so to nagu** "let me see"; **so nosen kuwi me** "may God keep you") |
| **tin** | instruction (**tin mu** "don't") |
| **fon** | advice; the decision stays with the listener |
| **de** | the speaker (or the group the speaker speaks for) commits: **de din** "we will" |
| **yo** | warning; **yo yo** emergency |
| **ba** | exclamation: surprise or strong feeling |
| **genso** | not literal (irony, joking); **genso genso** the whole turn |

- <span id="r-7-1-2"></span>A statement has no particle. Each sentence has one speech act.
- <span id="r-7-1-3"></span>**genso** or **ba** may modify the act from in front of its particle: **genso min me lugo** "as if you'd know"; **ba min** is a surprised or indignant question.
- <span id="r-7-1-4"></span>Someone else's intention is reported (**inwun**) or stated with time words and **kon**; in the reference variety, **de** is for the speaker's own commitment.

### 7.2 Stance (slot 12)

<span id="r-7-2-1"></span>After a pause at the end, a word can comment on the whole sentence, whatever its speech act:
- <span id="r-7-2-2"></span>**min** "…, right?" (checks);
- <span id="r-7-2-3"></span>**a** "as you know, you see" (shared ground): **wan sin oyi bu, a.**;
- <span id="r-7-2-4"></span>**buni** "okay?" (softens, invites agreement): **so pen isi, buni.**;
- <span id="r-7-2-5"></span>**donon** "it turned out" (against expectation): **wan gun no ibe guyi, donon.**
- <span id="r-7-2-6"></span>A half-remembered "wasn't it?" is low confidence plus the tag: **kon ka wan sin oyi bu, min.**
- <span id="r-7-2-7"></span>If two stance words occur, one pause comes before both, and **min** comes last: **wan sin oyi bu, a min.** "she said it, you know, right?"
- <span id="r-7-2-8"></span>Other words used in this position are stance words too. The choice tag **, yu** "which?" (4.8) has its own slot at the end and is not a stance word.

## 8. Time

### 8.1 Tense and aspect

- <span id="r-8-1-1"></span>Tense is optional. A time word or the first **sin** of a narrative sets the frame, the time that what follows is about, and later verbs in that frame stay unmarked. The future is shown by a time word or by context: **mon wuma, gegi muwo** "it will rain tomorrow".
- <span id="r-8-1-2"></span>Aspect words come right before the verb. **sin** means done. With no frame set it reads as past. Inside a past frame it marks something already done by that time, "had done", and inside a future frame it is "will have". **le** means ongoing, and also "still". **buntu** means about to. **sin** and **le** don't combine, so "was doing" is a past frame + **le**.
- <span id="r-8-1-3"></span>"Not yet" is **le mu** "still not", as in Mandarin *hái méi* and German *noch nicht*: **to le mu nawi** "I haven't eaten yet". Here the aspect word comes before **mu**, which covers only the verb. **mu sin** is "not done, didn't": **to mu sin nawi** "I didn't eat".
- <span id="r-8-1-4"></span>**manni** "usually" marks habit. With a past frame it means "used to".
- <span id="r-8-1-5"></span>Intent is marked with **gan momu** "on purpose" and **mu gan momu** "by accident".

### 8.2 Time words

- <span id="r-8-2-1"></span>The time roots are **eda** now, **mefa** today, **wuma** tomorrow, **afe** yesterday; **dili** day, **nelon** week (7 days), **dunan** month (also "moon"), **fawu** year; **muyi** time (a span or a point); **gimu** occasion (**gimu sa** "twice").
- <span id="r-8-2-2"></span>A time can be an anchor plus an offset, and the offset names its unit: **wuma wo dili fi** "the day after tomorrow". With no anchor, the offset counts from the current frame (8.1), which is now unless a story has set another time: **wo nelon fi** "a week from now, next week", **ya dunan fi** "a month ago". Any time or event can be the anchor.
- <span id="r-8-2-3"></span>A duration is a count: **awuwa ka** "three hours". **nin** + duration means "during, for" a span that frames the clause: **nin dili oma** "for seven days".
- <span id="r-8-2-4"></span>Age is lived time: **to nume fawu ka yawu** "I have lived 30 years".
- <span id="r-8-2-5"></span>Hours, minutes and seconds are borrowed: **awuwa**, **minitu**, **sekandu**.

### 8.3 Clock, calendar, dates

- <span id="r-8-3-1"></span>The clock follows the speaker's culture, and both styles are always understood.
  - The 24-hour style reads four digits one at a time: **mon po mape ka po** "at 09:30", **mon sa fi ka po** "at 21:30".
  - The 12-hour style counts the hour (1–12), then gives the minutes as two digits, then optionally **pi** + a part of the day: **mon mape ka po pi yami** "at 9:30 at night"; **mon yawu po sa** "at 10:02". On the hour, the hour is said alone: **mon yawu sa** "at 12".
  - The parts of the day are **leso** morning, **minfi** noon, **duwun** afternoon, **kegin** evening and **yami** night. Midnight is **yawu sa pi yami**.
  - For *about* a time, put **fu** before it: **mon fu minfi** "around noon".
- <span id="r-8-3-2"></span>A weekday is **dili dife** + 1–7 on its own, with Monday as 1 (ISO 8601): **dili dife ka** "Wednesday". A day of the month is said with its month; without one, say whose day it is: **dili dife ka pi dunan** "the 3rd (of the month)", **dili dife ka pi isi** "the third day of the trip".
- <span id="r-8-3-3"></span>Dates are labels (5.2) and put the larger unit first, with a pause between: **dunan dife yawu, dili dife mape** "October 9". A weekday with a time is said the same way: **dili dife te, mon …**. Years are read digit by digit: **fawu dife sa po sa ufo** "2026".

## 9. Numbers

### 9.1 Digits and place words

<span id="r-9-1-1"></span>

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| **po** | **fi** | **sa** | **ka** | **da** | **te** | **ufo** | **oma** | **kefi** | **mape** |

<span id="r-9-1-2"></span>

| 10 | 100 | 1000 | million | billion | point | minus | × 10 to the |
|---|---|---|---|---|---|---|---|
| **yawu** | **loki** | **munno** | **tonen** | **siwin** | **mimi** | **guti** | **unun** |

### 9.2 Reading numbers

- <span id="r-9-2-1"></span>The place words are **yawu** 10, **loki** 100, **munno** 1000, **tonen** million and **siwin** billion. The last three are also group words. In the quantity reading, place words come in descending order, each preceded by its digit. A 1 before a place word is dropped, and zero places are skipped: 15 **yawu te**, 50 **te yawu**, 42 **da yawu sa**, 105 **loki te**. A group word takes a whole number before it: 250 000 = **sa loki te yawu munno**.
- <span id="r-9-2-2"></span>The digit reading says one digit at a time. It is used whenever the exact digits matter more than the size: for identifiers, phone numbers and codes (in groups of three from the right), and for years and 24-hour clock times (as one four-digit group).
- <span id="r-9-2-3"></span>Labels (noun + **dife** + number) under 100 use the quantity reading (**dili dife yawu da** "day 14"). Larger labels use the digit reading.
- <span id="r-9-2-4"></span>Decimals use **mimi** "point": 1.5 = **fi mimi te**. **guti** means minus. With **unun** "× 10 to the", **ka unun guti ufo** = 3 × 10⁻⁶.

### 9.3 Amounts and comparison

- <span id="r-9-3-1"></span>For "about", put **fu** before the number: **ewo fu ka yawu** "about 30 people".
- <span id="r-9-3-2"></span>A range is **se** X **tun** Y. "At least" is **konsin** X, and "at most" is **mu ke se** X.
- <span id="r-9-3-3"></span>"Enough" is **tonya**.
- <span id="r-9-3-4"></span>A comparison is **ke** + quality + **se** + standard: **ke kudu se guyi ben** "bigger than that house". For "most", compare with everything: **ke kudu se we** "biggest" (bigger than all). For "less", use **ke** with the opposite (**ke meli** "smaller"). For "as … as", use **fu** (**kudu fu bu** "as big as it").
- <span id="r-9-3-5"></span>Measurements use borrowed international unit names, with the unit first like any counted noun: **kilamita te** "5 km".

## 10. People

### 10.1 Calling someone, titles, respect

- <span id="r-10-1-1"></span>You can call someone with a person word (a name, a title, or a single role or kin word) at the start (slot 1, for attention) or at the end (slot 13, to soften): **en mara, tin obu.** / **tin obu, en mara.**
- <span id="r-10-1-2"></span>Titles go before the name with no comma, and work both in address and in reference: **no tofo en mara** "Teacher Mara"; **no tofo en mara sin oyi** "Teacher Mara said".
- <span id="r-10-1-3"></span>**lanno** is the title of respect, and has no gender. It goes before a name, role or kin word (**lanno en olusegun** "Mr/Ms Olusegun", **lanno faba pi wede** "Uncle / Aunt (father's sibling)"). It can stand alone in address (**lanno, so nun …** "Sir/Madam, please …"), and alone in reference when context shows who (**lanno sin oyi** "the honoured one said"). It marks respect for the person named. In the reference variety it is a title, not a word for "you".
- <span id="r-10-1-4"></span>There is no apposition. To describe someone, use a title before the name, a relative clause or a new sentence.

### 10.2 Politeness and routines

- <span id="r-10-2-1"></span>**nun** adds politeness or deference and nothing else. It comes after any opener, right after the speech-act particle (**so nun …** "please …"), or where the particle would be in a statement. **nun nun** adds more.
- <span id="r-10-2-2"></span>There are no polite pronouns and no speech levels. **me** is "you" to anyone. Respect is carried by **lanno**, titles and **nun**.
- <span id="r-10-2-3"></span>Politeness never changes the act. A polite instruction is **tin nun**, and a polite warning is **yo nun**: **yo nun osa le obu. fon nun pen wupi isi.** "(Warning, politely) the water is coming. (Advice, politely) we need to go."
- <span id="r-10-2-4"></span>In an emergency (**yo yo**), no **nun** is expected.
- <span id="r-10-2-5"></span>Routines are fixed formulas. The greetings are **upe** and **upe leso** "good morning", the farewell is **upe isi** "go well", thanks is **lota** and sorry is **sepi**. With politeness, **nun** comes first: **nun upe leso**.

### 10.3 Reference

- <span id="r-10-3-1"></span>**wan** "he/she" is the person or animal being talked about. **yi** is another one who isn't the topic: **wan nagu yi** "she saw him". A newcomer is **yi**, or is named, until the speaker makes them the topic.
- <span id="r-10-3-2"></span>**bu** "it" is the thing being talked about. **ben** alone is a thing that isn't the topic: **me momu bu lu ben, yu.** "this one or that one?"
- <span id="r-10-3-3"></span>**tan** or **ben** alone stands for an event, statement or situation. **tan** is nearer (what I'm saying, here and now), and **ben** further (what you said, an earlier event): **ben gun upe** "that's good"; **gi tan** "so". For a recipient, see 5.2.
- <span id="r-10-3-4"></span>**sun**, in reported speech or thought, is the person whose words are reported.
- <span id="r-10-3-5"></span>**go** is anyone, people in general. In the reference variety, **me** is the listener only; for people in general, use **go**. An unknown doer is **ewo bo**.
- <span id="r-10-3-6"></span>**nen** is self. As an object it is reflexive (**to kuwi nen** "I keep myself"). After a noun or pronoun it means "in person" (**wan nen obu** "he came himself").
- <span id="r-10-3-7"></span>**pen** is we including you, and **din** is we not including you. **wan la** is "they" and **me la** "you all".
- <span id="r-10-3-8"></span>A pronoun never means the subject of its own clause; for that, use **nen**. The listener finds referents from context. If one could be unclear, name it.

## 11. Names, loans, new words

- <span id="r-11-1"></span>Names take **en**: **en mara**. A personal or brand name keeps its owner's spelling in lowercase, even with letters the language lacks: **en denise**, **en xi jinping**, **en nguyen**, **en wi-fi**. Say it as close to its owner's pronunciation as you can. Place names are names too: **en london**, though an established adapted form may be used instead: **en landan**. Names aren't used as verbs. A name runs until the next grammar word or pause, so a name of several words is written with no grammar words inside it, and a content word right after a name needs a grammar word or a pause before it: **en xi jinping sin oyi** "Xi Jinping said".
- <span id="r-11-2"></span>The adapted form (`tools/names.py`) is the spoken fallback for a name and the form of every loan. It is made like this:
  - each foreign sound becomes the nearest native sound: r → l, v → b, ʋ → w, z/sh/zh → s, th → f, dh → d, ch → t, j → d, kh → k; h and glottal sounds disappear; ng → n; length, aspiration and tone are dropped; ə, ʌ, æ → a;
  - two vowels in a row get a glide between them, y after i or e and w otherwise;
  - a consonant that can't stand where it is gets an added **u**;
  - the result has at least two syllables, counting a glide (**tuwu**).
- <span id="r-11-3"></span>Loans take no **en**. They are used only where the world shares a form, and are taken in that international form: **dola** dollar, **minitu**, **kilamita**, **pasentu**, **intalunetu**, **imeyilu**, **kamela**, **foto**. A loan enters the lexicon once it is common, and until then near-collisions are tolerated. Everything else is said with native words, built words or phrases.
- <span id="r-11-4"></span>Computers and interfaces use everyday words: search **ditun**, delete **nuton**, share **peton**, copy **gayen**, add **ginni**, download **dunu**, install **yaga**, turn on/off **benbi**/**tapi**, settings **ge finsa la**, computer **du sunbu** (`compounds.tsv`). **doku** "work" covers a machine working.
- <span id="r-11-5"></span>Letters used as labels (apartment 3B) pass through and are read as the speaker's culture reads them.
- <span id="r-11-6"></span>New words are made by the method in [vocabulary-method.md](vocabulary-method.md).

## 12. Conditions and modality

- <span id="r-12-1"></span>A condition is **don** "if" + clause. **kon** + number after **don** says how likely the condition is: **don kon fi** "if (unlikely)". **don kon po** "if (and it isn't so)" is counterfactual: **don kon po to sin isi, to sin nagu wan** "if I had gone, I would have seen her". The main clause is the consequence, and there is no "would".
- <span id="r-12-2"></span>There are three kinds of modality: ability, with **lenu** "can"; obligation, with **keya** "must" and **wupi** "need to, should"; and permission, with **efon** "allow" (**me gun efon nawi** "you may eat"). There, **gun** + an action word takes a verb as its object, as the plain verb would (4.2.6): "you are allowed to eat". Probability is confidence (6.1).
- <span id="r-12-3"></span>Purpose is **li** + verb, "in order to": **li bika** "to buy".
- <span id="r-12-4"></span>"Let's" is **so pen** …, and "don't" is **tin mu** ….

## 13. Grammar words

<span id="r-13-1"></span>

| Group | Words |
|---|---|
| Speech acts | question **min** · request **so** · instruct **tin** · advise **fon** · intend **de** · warn **yo** · exclaim **ba** |
| Politeness | **nun** |
| Clause operator | confidence **kon** |
| Phrase operators | not **mu** · only **na** · also **fe** · even **wi** · focus **o** |
| Degree | more **ke** · very **bi** |
| Aspect | done **sin** · ongoing **le** |
| Sentence end | tag **min** · "you know" **a** |
| Pronouns | I **to** · you **me** · we incl. **pen** · we excl. **din** · he/she **wan** · the other one **yi** · it **bu** · logophoric **sun** · anyone **go** · self **nen** |
| Determiners | plural **la** · this **tan** · that **ben** · all **we** · some **in** · some-not-all **kin** · none **fa** · unspecified **bo** · which/what **yu** |
| Relations | of **pi** · at **mon** · to **tun** · from/than **se** · with **gan** · for **li** · before **ya** · after **wo** · like/about **fu** · during **nin** · because of **gi** |
| Linkers | and **yen** · or **lu** · but **un** · if **don** · because **gi** · that **wun** · who/which **man** · while **nin** · before **ya** · after **wo** |
| Copula | is **gun** |
| Names | **en** |
| Derivation | doer **no** · thing **ge** · tool **du** · place **pu** |

<span id="r-13-2"></span>These operators have two syllables, stressed on the first: not literal **genso**, seen **wanme**, told **inwun**, inferred **wemen**, at least **konsin**, about to **buntu**, rather **tason**, almost **nedin**, each **mesun**, usually **manni**, "okay?" **buni**, "it turned out" **donon**, title **lanno**, until **anko**, without **nuwen**, end of phrase **kiyo**, number label **dife**. **dife** goes between a noun and a number to make a label or an ordinal (5.2). **anko** and **nuwen** are relation words, used like **ya** and **gan**: **to doku anko kegin** "I work until evening", **wan obu nuwen nimo** "he came without money". "Against" in the sense of protection is **se** "from" (**kuwi wan se ben** "protect him against that"); in the sense of opposing it is the verb **ninsu** "oppose".

## 14. Vocabulary

- <span id="r-14-1"></span>[../data/lexicon.tsv](../data/lexicon.tsv) lists roots and loans, each with a field and a frequency tier (1 rare – 5 most common). [../data/grammar.tsv](../data/grammar.tsv) lists the grammar words, [../data/numbers.tsv](../data/numbers.tsv) the number words and [../data/compounds.tsv](../data/compounds.tsv) the established compounds.
- <span id="r-14-2"></span>A gloss with a second gloss after a comma fixes the sense: **gufu** "hard, not soft". A root means that sense only.
- <span id="r-14-3"></span>One root may cover senses that most language families lump together: **apu** "word; language". Context tells them apart.

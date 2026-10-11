# Apupiwe: reference
<!-- Generated from spec/reference.toml by tools/spec.py build. Edit the spec, not this file. -->

This document states what the language is. The reasons for each part are in [rationale.md](rationale.md), its history is in [design-log.md](design-log.md), and the word lists are in the [data folder](https://github.com/LilijoySkyseeker/apupiwe/tree/main/data).

The language calls itself **apu pi we** "everyone's language", said [ˈapu pi we], roughly AH-poo pee weh, with only the first syllable stressed. Its name in English and other languages is one word, Apupiwe, said the same way. Any language is named with **apu pi** followed by whose language it is.

Apupiwe is a designed language for people who speak it natively, within the world's existing cultures. Its own grammar is built for native speakers. Where it meets a culture's conventions, such as clocks, calendars, units, names and customs, it carries them. Where conventions conflict and one must be chosen, it follows the international standard.

When its goals conflict, they rank in this order:
1. Clarity. A precise, unambiguous way to say anything always exists.
2. Predictability. Nothing is arbitrary to memorise, and rules follow from meaning.
3. Economy. For fluent speakers, it is short and trusts context.
4. Reach. It carries what the world's languages express.

Any adult can learn it. Explicitness for learners is never bought at the cost of fluent use.

---

## 1. Principles

1. The common case costs nothing. Statements, ordinary belief, an unknown source, the topic, and present or unspecified time are unmarked. Frequent meanings have the shortest words.
2. Heads come first, and position carries role. The order is subject, verb, object. A content word that describes a noun or a verb follows it. Words never move to show their role.
3. Operators come before what they cover (section 6).
4. Heavy goes last. A noun's own modifiers come before its **pi** "of" phrase, and long clauses go to the end. Nothing may follow a relative clause in its phrase.
5. Doubling widens or strengthens any word except a digit in a number: **mu mu** emphatic "not", **nun nun** extra deference, **yo yo** emergency, **genso genso** "the whole turn is not literal", **nen nen** "each other", **feko feko** "exactly so".
6. Every social pressure has its own word: **ba** and **bi** for emphasis, **nun** for politeness, **lanno** for respect, and the stance words of section 7.
7. A precise way always exists, but it need not always be used. Anything the listener can supply may be left out (section 4.5), and any ambiguity can be removed by saying more.

## 2. Sounds

- The vowels are a e i o u. Every syllable keeps its full vowel.
- There are 13 consonants: p b t d k g · m n · f s · l w y. They are made at the lips (p b m w, and f with lip and teeth), with the tongue tip (t d n s l), with the tongue body (y) and with the back of the tongue (k g).
- A syllable has the shape (C)V(n). A syllable with no consonant before its vowel (**a**, **en**) occurs only at the start of a word. The only consonant that can end a syllable is n.
- Words fall into three types by sound:
  - grammar words have one unstressed syllable (table in section 13);
  - the digits 0–5 have one stressed syllable;
  - every other word has two or more syllables and is stressed on the first.
- Words never change form. There are no endings, no agreement, no case and no gender.
- Stress is a higher pitch on the stressed syllable, stepping down after it. It does not make the syllable longer. The rhythm is syllable-timed.
- Across a phrase, each stressed syllable is a little lower than the one before (declination), and pitch resets after a pause.
- There are no tones. Pitch carries only intonation and emotion. A question needs no rising tone, because its words make it a question, but rising anyway is fine.
- Some harmless variants are allowed, inside content words only. Before i and e, k and g may sound like "ch" and "j". A vowel plus n may become a nasal vowel. Consonants between vowels may soften. Grammar words keep their consonants.
- **mm** "heard you", **huh?** "say again", and any other interjection or hesitation sound speakers use are outside the sound system and carry no grammar.
- Native content words never begin with a digit's syllable (**po fi sa ka da te**). Loans are exempt.

## 3. Writing

- The letters are a b d e f g i k l m n o p s t u w y, one per sound, with no accents. Digits never appear inside a word. Spelling follows the standard pronunciation, and neither the harmless variants nor stress are written.
- Lowercase is the standard. Capitals carry no meaning and are harmless.
- These marks carry grammar:

  | Mark | Use |
  |---|---|
  | `,` | a pause (section 4.6) |
  | `.` | end of a sentence; between digits, the decimal point |
  | `" "` | around quoted speech |

  `?` and `!` are allowed and add nothing. `-` and `:` are not used in the language's own words.
- Some things pass through as written: chat abbreviations and interjections (ok, lol), digits, unit symbols (`5 km`, `20 °C`, `30%`), the local clock notation (`21:30`, `9:30 pm`), ISO dates (`2026-10-10`), letters used as labels, links, email addresses, @handles, #tags, emoji, code, file names, and personal and brand names (section 11). Unit symbols are read aloud by their borrowed names (9.3) and clock notation in the speaker's clock style (8.3). Other notation is read as the speaker's culture reads it.
- Ordinary writing uses digits for numbers. This reference spells numbers out only to show how they are said. Digits are grouped in threes from the decimal point with a space (`1 250 000`), and `.` is the decimal point. A senary number is marked `₆` (or `_6`).
- Words are written apart. A phrase said fast keeps its spaces until a fused form actually changes sound and becomes a new word.

## 4. The sentence

### 4.1 Template

A sentence fills these slots in this order. Only the verb, or a fragment (4.5), is required.

| # | Slot | Contents | Section |
|---|---|---|---|
| 1 | Calling someone | a name, title, role or kin word, then a pause | 10.1 |
| 2 | Opener | a linker to the previous sentence (**gi tan** "so"), then a scene-setting phrase (time, place) or topic **pi X**, then an **if**/**when** clause, each followed by a pause | 4.3 |
| 3 | Speech act | one particle; **genso** or **ba** may come before it | 7.1 |
| 4 | Politeness | **nun** | 10.2 |
| 5 | Clause operators | confidence **kon** + number, source **wanme**/**inwun**/**wemen** | 6.1 |
| 6 | Subject | a noun phrase (section 5) | |
| 7 | Phrase operators, habit, aspect | e.g. **mu**, **fe**, **manni**, **sin** | 6.2, 8.1 |
| 8 | Verb | one verb, or verb + verb (4.2) | |
| 9 | Manner | a word describing the action | 4.2 |
| 10 | Objects | recipient, then thing | 4.2 |
| 11 | Relation phrases | **mon**, **tun**, **se**, **gan**, **li** … + noun phrase or clause | 4.4 |
| 12 | Trailing clause | **wun**, **gi**, **don**, **nin** … clause | 4.4 |
| 13 | Stance | a pause, then **min**, **a**, **buni**, **donon** … | 7.2 |
| 14 | Calling someone | a pause, then a name, title, role or kin word | 10.1 |

### 4.2 The verb and its objects

- For any content word, what you mean decides the clear form:
  - for a state ("is big", "is afraid"), use **gun** + word: **guyi gun kudu** "the house is big", **to gun nuta** "I'm afraid";
  - for an event ("walks", "is walking", "walked"), use the word as the verb, with an aspect word when precision matters: **ewo le niba** "the person is walking", **ewo manni niba** "the person (usually) walks", **ewo sin niba** "the person walked";
  - for a description of a noun ("the person who walks", "the house that is big"), use **man**: **ewo man niba**, **guyi man gun kudu**.
- A bare noun followed by a word (**guyi kudu**, **ewo niba**) may be a description or a statement. Context decides, and the clear forms above remove any doubt.
- Any content word can take any role by its position. As an object, or with a derivation marker, it is a noun (**sepi** "apologise / an apology").
- A word right after the verb describes the action: **oyi fanse** "say calmly". It comes before the object, as in **nawi yobe pasu** "eat food quickly". After the object, a word describes the object: **nawi pasu yobe** "eat fast food".
- With two objects, the recipient comes first and then the thing: **tofo me nuta** "teach you fear".
- When one verb follows another and the first takes an object (want, try, need, must, can, start, stop, teach, see, like, help…), the second verb is that object: **walo alun** "try to break". Otherwise the second verb describes the first: **goyu pume** "sit thinking".
- **muge** "do; make" followed by a result and then an object means "make (it) so": **muge upe tan** "fix this". Followed by an object and then a manner, it means "do (it) so": **muge tan upe** "do this well".
- A command needs **tin**, or **so** for a request. Without a particle, a sentence is a statement.

### 4.3 Openers

- A time or place phrase may open the sentence to set the scene: **mon minfi, …** "at noon, …". It changes no roles.
- A topic is **pi** + a noun phrase at the start, meaning "as for X": **pi tale la, no kuwi guyi, yidu bu la.** "As for the cars, the caretaker takes them." At the start, **pi** has no other reading, and the topic runs to the pause, so it can be a list: **pi upe yen yomo,** "as for good and bad,".
- An if/when clause is **don** "if", **nin** "while/when", **wo** "after", **ya** "before" or **gi** "because", followed by a clause.
- When several of these open a sentence, they come in this order: linker, scene or topic, if/when clause. The speech-act particle follows them.
- Only person words call someone. A fronted phrase that isn't a person word is a scene or topic phrase.

### 4.4 Clauses and relation phrases

- A relation phrase (**mon**, **tun**, **se**, **gan**, **li**, **ya**, **wo**, **fu**, **nin**) at clause level attaches to the clause's verb. Inside a noun phrase, only **pi** attaches to a noun. To give a noun any other relation, use a relative clause: **sola man gun mon bige pi yolan** "the road that is above the river". In comparisons and quantities (9.3), **se**, **tun** and **fu** belong to their number or adjective. After a time, **wo** and **ya** belong to that time (8.2): **to isi mon wuma wo dili fi** "I go the day after tomorrow".
- A relation word may drop its object when context supplies it, as in **wo** "after that" and **ya** "beforehand". It then ends its clause or comes before a pause.
- A relation word can take a clause (**wo wan la yidu ewo bo** "after they took someone") or an action noun (**se kusa** "from leaving").
- A relative clause attaches to the nearest noun before it. A time, reason or condition clause at the *start* of a sentence belongs to the main clause. At the *end*, it belongs to the innermost clause before it, unless a pause closes that clause first: **nin leso, to sin miya ewo man sigo** "in the morning, I watched the person who came back"; **to sin miya ewo man sigo nin leso** "I watched the person who came back in the morning". In the same way, a phrase or clause after verbs joined by **yen**, **lu** or **un** belongs to the last of them, and at the start it covers them all: **wan doku yen nawi mon guyi** "he works, and eats at home"; **mon guyi, wan doku yen nawi** "at home, he works and eats".
- **yen** "and", **lu** "or" and **un** "but" join nouns, verbs, modifiers or clauses. Nouns in a list are joined with **yen**: **mole yen wede** "mother and father". **lu X lu Y** means "either X or Y, not both".
- A quote is framed by a say-verb, and in writing it goes in quotation marks. It is its own sentence with its own speech-act particle. Broken-off speech just stops.

### 4.5 Leaving things out

- Anything the listener can supply from context may be left out: the subject, the object, the object of a relation word or the verb. An answer or follow-up can be just the new part: **muyi yu? moti?** "what time? again?"; **nagu me la mon dili pi ufo.** "see you all Saturday".
- The exception is a clause that starts with **gun** and has no subject, which means "there is" (4.7). To say "(it) is X", keep the subject: **bu gun nimo** "it's money". With **gun** left out too, a bare state is fine: **bi upe.** "very good."
- When leaving something out could be unclear, say it.

### 4.6 Pauses

A pause, written as a comma, goes wherever a phrase could otherwise run on. It belongs in these places:
- after someone called at the start, and before someone called at the end;
- after an opener (linker, scene, topic, if/when clause);
- after a subject that contains a clause or a phrasal derived word, before its verb (**no sanwa man … sin sege, keya unfu …**);
- between a recipient and a long object;
- between clauses joined by **yen**, **lu** or **un** when the first ends in a noun;
- before a stance word;
- between a larger and a smaller calendar unit (**dunan pi yawu, dili pi mape**);
- after a relative clause, to close it before more material.

In casual writing, pauses that context makes obvious may be dropped.

### 4.7 "Is": gun

- **gun** goes before a state: **guyi gun kudu** "the house is big". Without it, **guyi kudu** is "the big house".
- **gun** goes before a noun: **wan gun tiwu** "she is a child".
- **gun** goes before a place phrase: **wan gun mon guyi** "he is at home".
- **gun** before an action word gives the resulting state: **gun tapi** "is closed".
- **gun** before a **wun** clause means "is that …".
- After another verb, and after **li**, **gun** is "to be": **momu gun tiwu** "want to be a child", **sogan li gun kuwi** "the right to be protected".
- Anywhere else, **gun** at the start of a clause with no subject means "there is": **un, gun musu feli** "but there are many things".

### 4.8 Questions and answers

- A yes/no question starts with **min**. A **min** at the end of a clause is a tag, "…, right?".
- Question words stay where the answer goes and need no **min**: **me momu wun to oyi yu.** "you want me to say what?"
- Question words are built from **yu**: **yu** what; **ewo yu** who; **X yu** which X; **mon kemu yu** where; **mon muyi yu** when; **gi yu** why; **fu yu** how; **wifu yu** how many/much; **pi ewo yu** whose.
- To offer a choice, ask **min … lu …** "either?", or ask **… lu …, yu** "which?" with a pause before **yu** so it isn't read as "which X". That second kind is answered by echoing the choice.
- An indirect question puts **yu** or **min** inside a **wun** clause: **to mu lugo wun min …** "I don't know whether …".
- Answers echo the verb, since there are no words for yes and no: "Aren't you coming?" → **obu** / **mu obu**. A question with **gun** is answered by echoing what follows **gun**: "Is the house big?" → **kudu** / **mu kudu**. To acknowledge, **mm** says you heard, an echo says you understood, and **de** + verb says "will do".

## 5. The noun phrase

### 5.1 Template

A noun phrase runs in this order: noun, content modifiers, number, **la**, determiner, **pi** phrase, relative clause, as in **guyi kudu sa la tan pi en mara man …**. Titles and **lanno** come before the noun (10.1), and phrase operators come before the whole phrase (6.2).

### 5.2 Parts

- Describing words follow the noun: **guyi kudu** "big house". For a clear description, use **man** (5.3).
- Gender is a modifier, stated once when it matters: **tiwu futa** "daughter", **no wungu futa** "the leader, a woman".
- Noun + noun is used only for gender and for the compounds in `compounds.tsv`. Other relations use **pi** or a relative clause.
- Numbers and times can stand alone as noun phrases: **mon yawu gun upe** "10 o'clock is fine".
- A noun followed by a number is a count (**dili oma** "seven days"). Noun + **pi** + number is a label (**kemin pi sa** "document 2"), and a label also gives a place in order: **gimu pi ka** "the third time", **ewo pi fi** "the first person". "Last" is **pi fugi**, "of the end": **gimu pi fugi** "the last time".
- The plural word **la** is optional. A count or context can show plurality.
- There are no articles. Whether something is known or new is left to context, or shown with **tan**, **ben**, **bo** or a number.
- Determiners (table in section 13) and **mesun** "each" follow the noun: **guyi tan** "this house", **ewo bo** "someone", **musu bo** "something", **pu nume mesun** "each home". A determiner right after a noun or pronoun belongs to it. So to give a recipient a determiner standing alone as the thing, use **tun**: **to iko ben tun wan** "I told that to him" (**to iko wan ben** is "I told that-him"). A determiner may stand alone as a noun phrase: **we** "all", **in** "some", **fa** "none". A part of a whole is a determiner or number + **pi** + noun: **kin pi foto la** "some of the photos", **fi pi ka** "one of three".
- **pi** "of" links a noun to a noun: **guyi pi en mara** "Mara's house". Each **pi** attaches to the nearest noun before it, and its phrase is the nearest single noun after it, so a list joined by **yen** or **lu** is outside it: **enpa pi pume yen lite pi nosen** is "freedom of thought, and religion". To cover every item, repeat the head: **enpa pi pume yen enpa pi lite pi nosen** "freedom of thought and freedom of religion".

### 5.3 Relative clauses

A relative clause is **man** + clause, placed after the noun. The noun fills the role missing from the clause:
- subject: **ewo man niba** "the person who walks";
- object: **mabo man me la yaga** "the papers you put";
- place or time, with the relation word at the end of the clause: **kemu man to nume mon** "the place where I live".

A relative clause attaches to the nearest noun or pronoun before it, so after a **pi** phrase it describes the **pi** noun. To describe the head instead, put a quality before the **pi** phrase or use a new sentence. No word closes a relative clause. A pause closes it, along with every relative clause still open.

### 5.4 Derived words

Four markers before a verb or verb phrase name a role in the action:

| Marker | Role | Example |
|---|---|---|
| **no** | the one who does it | **no febo** "one who answers" |
| **ge** | the thing done or made | **ge iko** "what is told" = news |
| **du** | the thing used | **du bubo** "thing for laughing" = a joke |
| **pu** | the place | **pu niba** "place for walking" = a path |

- A **pi** phrase after a derived word belongs to the last noun inside its base, or to the derived word itself if its base has no noun: **du kuwi pi to** "my thing for keeping".
- The base may be a verb phrase: **no isi se guyi** "one who goes from home", a traveller. It runs to the end of its phrase, like a relative clause, and a pause separates it from a following verb.
- A person something is done to is **ewo man gun** + verb: **ewo man gun tofo** "a student".
- A noun base is linked with **pi** or a verb: **pu pi mabo** "an office", **no obu se yaye** "an alien".
- For opposites, **mu** + word means "not X" (**mu upe** "not good"), and a separate opposite root names the other pole (**yomo** "bad").

## 6. Operators

### 6.1 Clause operators

Clause operators start the clause (slot 5) and cover all of it.
- Confidence is **kon** + a number of sixths, the chance in 6 that the statement is true: **kon po** impossible, **kon fi** unlikely, **kon sa** doubtful, **kon ka** even odds, **kon da** likely, **kon te** very likely, **kon ufo** certain; **kon te mimi te** 5.5 in 6; **kon bo** "don't know how sure". An unmarked statement is believed. Exact probabilities use a number and **pasentu**.
- Source is optional: **wanme** seen, **inwun** told, **wemen** inferred.
- "Might" and "must" in the sense of *probably* are a matter of confidence: "She must be home" is **kon te wan gun mon guyi**.

### 6.2 Phrase operators

Phrase operators cover the word or phrase right after them, including a phrase that opens the sentence (**na mon funti, …** "only in the community, …"). Before the verb, they cover the predicate.
- **mu** not (**to mu yidu bu** "I didn't take it"; **mu mu** emphatic);
- **na** only; **fe** also; **wi** even (**wi don** "even if"); **o** focus, "this one, not another" (**o en tomas yidu bu** "*Tomas* took it"; before the verb it insists: **to o unfu** "I *did* pay");
- to add a whole statement ("also, …"), start with **yen**; **fe** before the verb means the subject also does it;
- **konsin** at least; **nedin** almost; **mesun** each;
- degree words **ke** more, **bi** very, **tason** rather (**ke kudu** "bigger"; **nimo ke uyo** "less money").
- Before the verb, the order is phrase operators, then **manni**, then aspect, then the verb: **to fe manni le doku**.

## 7. Speech acts and stance

### 7.1 Speech acts (slot 3)

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

- A statement has no particle. Each sentence has one speech act.
- **genso** or **ba** may modify the act from in front of its particle: **genso min me lugo** "as if you'd know"; **ba min** is a surprised or indignant question.
- Someone else's intention is reported (**inwun**) or stated with time words and **kon**; **de** is only for the speaker's own commitment.

### 7.2 Stance (slot 13)

After a pause at the end, a word can comment on the whole sentence, whatever its speech act:
- **min** "…, right?" (checks);
- **a** "as you know, you see" (shared ground): **wan sin oyi bu, a.**;
- **buni** "okay?" (softens, invites agreement): **so pen isi, buni.**;
- **donon** "it turned out" (against expectation): **wan gun no ibe guyi, donon.**
- A half-remembered "wasn't it?" is low confidence plus the tag: **kon ka wan sin oyi bu, min.**
- If two stance words occur, **min** comes last.
- Other words used in this position are stance words too.

## 8. Time

### 8.1 Tense and aspect

- Tense is optional. A time word or the first **sin** of a narrative sets the time, and later verbs stay unmarked. The future is shown by a time word or by context: **wuma gegi muwo** "it will rain tomorrow".
- Aspect words come right before the verb. **sin** means done: with a past frame it is past, and with a future frame "will have". **le** means ongoing, and also "still". **buntu** means about to. **sin** and **le** don't combine, so "was doing" is a past frame + **le**.
- **mu sin** "not yet". For "didn't do", use a past frame + **mu** + verb.
- **manni** "usually" marks habit. With a past frame it means "used to".
- Intent is marked with **gan momu** "on purpose" and **mu gan momu** "by accident".

### 8.2 Time words

- The time roots are **eda** now, **mefa** today, **wuma** tomorrow, **afe** yesterday; **dili** day, **nelon** week (7 days), **dunan** month (also "moon"), **fawu** year; **muyi** time (a span or a point); **gimu** occasion (**gimu sa** "twice").
- A time can be an anchor plus an offset, and the offset names its unit: **wuma wo dili fi** "the day after tomorrow". With no anchor, the anchor is now: **wo nelon fi** "next week", **ya dunan fi** "a month ago". Any time or event can be the anchor.
- A duration is a count: **awuwa ka** "three hours". **nin** + duration means "during, for" a span that frames the clause: **nin dili oma** "for seven days".
- Age is lived time: **to nume fawu ka yawu** "I have lived 30 years".
- Hours, minutes and seconds are borrowed: **awuwa**, **minitu**, **sekandu**.

### 8.3 Clock, calendar, dates

- The clock follows the speaker's culture, and both styles are always understood.
  - The 24-hour style reads four digits one at a time: **mon po mape ka po** "at 09:30", **mon sa fi ka po** "at 21:30".
  - The 12-hour style counts the hour (1–12), then gives the minutes as two digits, then optionally **pi** + a part of the day: **mon mape ka po pi yami** "at 9:30 at night"; **mon yawu po sa** "at 10:02". On the hour, the hour is said alone: **mon yawu sa** "at 12".
  - The parts of the day are **leso** morning, **minfi** noon, **duwun** afternoon, **kegin** evening and **yami** night. Midnight is **yawu sa pi yami**.
  - For *about* a time, put **fu** before it: **mon fu minfi** "around noon".
- A weekday is **dili pi** + 1–7 on its own, with Monday as 1 (ISO 8601): **dili pi ka** "Wednesday". A day of the month is said with its month.
- Dates put the larger unit first, with a pause between: **dunan pi yawu, dili pi mape** "October 9". A weekday with a time is said the same way: **dili pi te, mon …**. Years are read digit by digit: **fawu pi sa po sa ufo** "2026".
- The senary calendar is described in [measurement.md](measurement.md).

## 9. Numbers

### 9.1 Digits and place words

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| **po** | **fi** | **sa** | **ka** | **da** | **te** | **ufo** | **oma** | **kefi** | **mape** |

| 10 | 100 | 1000 | million | billion | point | minus | × 10 to the |
|---|---|---|---|---|---|---|---|
| **yawu** | **loki** | **munno** | **tonen** | **siwin** | **mimi** | **guti** | **unun** |

### 9.2 Reading numbers

- In the quantity reading, place words come in descending order, each preceded by its digit. A 1 before a place word is dropped, and zero places are skipped: 15 **yawu te**, 50 **te yawu**, 42 **da yawu sa**, 105 **loki te**. A group word takes a whole number before it: 250 000 = **sa loki te yawu munno**.
- The digit reading says one digit at a time. It is used whenever the exact digits matter more than the size: for identifiers, phone numbers and codes (in groups of three from the right), and for years and 24-hour clock times (as one four-digit group).
- Labels (noun + **pi** + number) under 100 use the quantity reading (**dili pi yawu da** "day 14"). Larger labels use the digit reading.
- Decimals use **mimi** "point": 1.5 = **fi mimi te**. **guti** means minus. With **unun** "× 10 to the", **ka unun guti ufo** = 3 × 10⁻⁶.
- A senary number is **senali** + digits: **senali sa po** = 20₆ = 12.

### 9.3 Amounts and comparison

- For "about", put **fu** before the number: **ewo fu ka yawu** "about 30 people".
- A range is **se** X **tun** Y. "At least" is **konsin** X, and "at most" is **mu ke se** X.
- "Enough" is **tonya**.
- A comparison is **ke** + quality + **se** + standard: **ke kudu se guyi ben** "bigger than that house". For "most", compare with everything: **ke kudu se we** "biggest" (bigger than all). For "less", use **ke** with the opposite (**ke meli** "smaller"). For "as … as", use **fu** (**kudu fu bu** "as big as it").
- Measurements use borrowed international unit names, with the unit first like any counted noun: **kilamita te** "5 km". The native unit roots in the lexicon belong to the senary system ([measurement.md](measurement.md)).

## 10. People

### 10.1 Calling someone, titles, respect

- You can call someone by name, title, role or kin word at the start (slot 1, for attention) or at the end (slot 14, to soften): **en mara, tin obu.** / **tin obu, en mara.**
- Titles go before the name with no comma, and work both in address and in reference: **no tofo en mara** "Teacher Mara"; **no tofo en mara sin oyi** "Teacher Mara said".
- **lanno** is the title of respect, and has no gender. It goes before a name, role or kin word (**lanno en olusegun** "Mr/Ms Olusegun", **lanno faba pi wede** "Uncle"). It can stand alone in address (**lanno, so nun …** "Sir/Madam, please …"), and alone in reference when context shows who (**lanno sin oyi** "the boss said"). It marks respect for the person named and never means "you".
- There is no apposition. To describe someone, use a title before the name, a relative clause or a new sentence.

### 10.2 Politeness and routines

- **nun** adds politeness or deference and nothing else. It goes right after the speech-act particle, or first in a statement: **so nun …** "please …". **nun nun** adds more.
- There are no polite pronouns and no speech levels. **me** is "you" to anyone. Respect is carried by **lanno**, titles and **nun**.
- Politeness never changes the act. A polite instruction is **tin nun**, and a polite warning is **yo nun**: **yo nun osa le obu. fon nun pen wupi isi.** "(Warning, politely) the water is coming. (Advice, politely) we need to go."
- In an emergency (**yo yo**), no **nun** is expected.
- Routines are fixed formulas. The greetings are **upe** and **upe leso** "good morning", the farewell is **upe isi** "go well", thanks is **lota** and sorry is **sepi**. With politeness, **nun** comes first: **nun upe leso**.

### 10.3 Reference

- **wan** "he/she" is the person or animal being talked about. **yi** is another one who isn't the topic: **wan nagu yi** "she saw him". A newcomer is **yi**, or is named, until the speaker makes them the topic.
- **bu** "it" is the thing being talked about. **ben** alone is a thing that isn't the topic: **me momu bu lu ben, yu.** "this one or that one?"
- **tan** or **ben** alone stands for an event, statement or situation. **tan** is nearer (what I'm saying, here and now), and **ben** further (what you said, an earlier event): **ben gun upe** "that's good"; **gi tan** "so". For a recipient, see 5.2.
- **sun**, in reported speech or thought, is the person whose words are reported.
- **go** is anyone, people in general. **me** is only ever the listener and is never generic. An unknown doer is **ewo bo**.
- **nen** is self. As an object it is reflexive (**to kuwi nen** "I keep myself"). After a noun or pronoun it means "in person" (**wan nen obu** "he came himself").
- **pen** is we including you, and **din** is we not including you.
- A pronoun never means the subject of its own clause; for that, use **nen**. The listener finds referents from context. If one could be unclear, name it.

## 11. Names, loans, new words

- Names take **en**: **en mara**. A personal or brand name keeps its owner's spelling in lowercase, even with letters the language lacks: **en denise**, **en xi jinping**, **en nguyen**, **en wi-fi**. Say it as close to its owner's pronunciation as you can. Place names are names too: **en london**, though an established adapted form may be used instead: **en landan**. Names aren't used as verbs.
- The adapted form (`tools/names.py`) is the spoken fallback for a name and the form of every loan. It is made like this:
  - each foreign sound becomes the nearest native sound: r → l, v → b, ʋ → w, z/sh/zh → s, th → f, dh → d, ch → t, j → d, kh → k; h and glottal sounds disappear; ng → n; length, aspiration and tone are dropped; ə, ʌ, æ → a;
  - two vowels in a row get a glide between them, y after i or e and w otherwise;
  - a consonant that can't stand where it is gets an added **u**;
  - the result has at least two syllables, counting a glide (**tuwu**).
- Loans take no **en**. They are used only where the world shares a form, and are taken in that international form: **dola** dollar, **minitu**, **kilamita**, **pasentu**, **intalunetu**, **imeyilu**, **kamela**, **foto**. A loan enters the lexicon once it is common, and until then near-collisions are tolerated. Everything else is said with native words, built words or phrases.
- Computers and interfaces use everyday words: search **ditun**, delete **nuton**, share **peton**, copy **gayen**, add **ginni**, download **dunu**, install **yaga**, turn on/off **benbi**/**tapi**, settings **ge finsa la**, computer **du sunbu** (`compounds.tsv`). **doku** "work" covers a machine working.
- Letters used as labels (apartment 3B) pass through and are read as the speaker's culture reads them.
- New words are made by the method in [vocabulary-method.md](vocabulary-method.md).

## 12. Conditions and modality

- A condition is **don** "if" + clause. **kon** + number after **don** says how likely the condition is: **don kon fi** "if (unlikely)". **don kon po** "if (and it isn't so)" is counterfactual: **don kon po to sin isi, to sin nagu wan** "if I had gone, I would have seen her". The main clause is the consequence, and there is no "would".
- There are three kinds of modality: ability, with **lenu** "can"; obligation, with **keya** "must" and **wupi** "need to, should"; and permission, with **efon** "allow" (**me gun efon nawi** "you may eat"). Probability is confidence (6.1).
- Purpose is **li** + verb, "in order to": **li bika** "to buy".
- "Let's" is **so pen** …, and "don't" is **tin mu** ….

## 13. Grammar words

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
| Relations | of **pi** · at **mon** · to **tun** · from/than **se** · with **gan** · for **li** · before **ya** · after **wo** · like/about **fu** · during **nin** |
| Linkers | and **yen** · or **lu** · but **un** · if **don** · because **gi** · that **wun** · who/which **man** · while **nin** · before **ya** · after **wo** |
| Copula | is **gun** |
| Names | **en** |
| Derivation | doer **no** · thing **ge** · tool **du** · place **pu** |

These operators have two syllables, stressed on the first: not literal **genso**, seen **wanme**, told **inwun**, inferred **wemen**, at least **konsin**, about to **buntu**, rather **tason**, almost **nedin**, each **mesun**, usually **manni**, "okay?" **buni**, "it turned out" **donon**, title **lanno**.

## 14. Vocabulary

- [../data/lexicon.tsv](../data/lexicon.tsv) lists roots and loans, each with a field and a frequency tier (1 rare – 5 most common). [../data/grammar.tsv](../data/grammar.tsv) lists the grammar words, [../data/numbers.tsv](../data/numbers.tsv) the number words and [../data/compounds.tsv](../data/compounds.tsv) the established compounds.
- A gloss with a second gloss after a comma fixes the sense: **gufu** "hard, not soft". A root means that sense only.
- One root may cover senses that most language families lump together: **apu** "word; language". Context tells them apart.

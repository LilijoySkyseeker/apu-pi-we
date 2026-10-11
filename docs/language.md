# Apu Pi We: reference

This document states what the language is. Why each part is the way it is: [rationale.md](rationale.md). How it got here: [design-log.md](design-log.md). Word lists: [../data/](../data/).

**Name:** **apu pi we** "everyone's language" (English: Apu Pi We). Any language is named **apu pi** + whose it is.

**What it is:** a designed language for humans who speak it natively, living within the world's existing cultures. Its own grammar is built for native speakers; where it meets a culture's conventions (clocks, calendars, units, names, customs) it carries them. Where conventions conflict and one must be chosen, it follows the international standard.

---

## 1. Principles

1. **The common case costs nothing.** Statements, ordinary belief, unknown source, the topic, and present or unspecified time are unmarked. Frequent meanings have the shortest words.
2. **Heads come first, and position carries role.** Subject, verb, object. Content words that describe a noun follow it; content words that describe a verb follow it. Words never move to show their role.
3. **Operators come before what they cover** (section 6).
4. **Heavy goes last.** A noun's own modifiers come before its **pi** "of" phrase; long clauses go to the end; nothing may follow a relative clause in its phrase.
5. **Doubling widens or strengthens** any word (not digits in a number): **mu mu** emphatic "not", **nun nun** extra deference, **yo yo** emergency, **genso genso** "the whole turn is not literal", **nen nen** "each other", **feko feko** "exactly so".
6. **Every social pressure has its own word:** emphasis **ba**, **bi**; politeness **nun**; respect **lanno**; stance (section 7).
7. **A precise way always exists; it need not always be used.** Anything the listener can supply may be left out (section 4.5), and any ambiguity can be removed by saying more.

## 2. Sounds

- **Vowels:** a e i o u. Every syllable keeps its full vowel.
- **Consonants (13):** p b t d k g · m n · f s · l w y. Places: lips (p b m w, and f with lip and teeth), tongue tip (t d n s l), tongue body (y), back of the tongue (k g).
- **Syllables:** (C)V(n). A vowel-only syllable occurs only at the start of a word. The only syllable-final consonant is n.
- **Word types by sound:**
  - grammar words: one syllable, unstressed (table, section 13);
  - digits 0–5: one syllable, stressed;
  - every other word: two or more syllables, stressed on the first.
- **Words never change form:** no endings, no agreement, no case, no gender.
- **Stress** is higher pitch on the stressed syllable, stepping down after it, not extra length. Rhythm is syllable-timed.
- **Declination:** across a phrase, each stressed syllable is a little lower than the one before; pitch resets after a pause.
- **No tones.** Pitch carries intonation and emotion only. A question needs no rising tone (its words make it a question); rising anyway is fine.
- **Harmless variants,** inside content words only: k and g may sound like "ch" and "j" before i and e; a vowel plus n may become a nasal vowel; consonants between vowels may soften. Grammar words keep their consonants.
- **Outside the sound system:** **mm** "heard you", **huh?** "say again", and any other interjection or hesitation sound speakers use; they carry no grammar.
- **Native content words** never begin with a digit's syllable (**po fi sa ka da te**). Loans are exempt.

## 3. Writing

- **Letters:** a b d e f g i k l m n o p s t u w y, one per sound, no accents; never digits inside a word. Spelling follows the standard pronunciation; the harmless variants are not written. Stress is not written.
- **Lowercase** is the standard. Capitals carry no meaning and are harmless.
- **Marks that carry grammar:**

  | Mark | Use |
  |---|---|
  | `,` | a pause (section 4.6) |
  | `.` | end of a sentence; between digits, the decimal point |
  | `" "` | around quoted speech |

  `?` and `!` are allowed and add nothing; `-` and `:` are not used in the language's own words.
- **Passes through as written:** digits, unit symbols (`5 km`, `20 °C`, `30%`), the local clock notation (`21:30`, `9:30 pm`), ISO dates (`2026-10-10`), letters used as labels, links, email addresses, @handles, #tags, emoji, code, file names, personal and brand names (section 11). Unit symbols are read aloud by their borrowed names (9.3); clock notation in the speaker's clock style (8.3); other notation as the speaker's culture reads it.
- **Numbers in writing:** digits, grouped in threes from the decimal point with a space (`1 250 000`), `.` as the decimal point. A senary number is marked `₆` (or `_6`).
- **Word boundaries:** words are written apart; a phrase said fast keeps its spaces until a fused form actually changes sound and becomes a new word.

## 4. The sentence

### 4.1 Template

A sentence fills these slots in this order. Only the verb (or a fragment, 4.5) is required.

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
| 9 | Objects | recipient, then thing | 4.2 |
| 10 | Manner | a content word describing the verb | 4.2 |
| 11 | Relation phrases | **mon**, **tun**, **se**, **gan**, **li** … + noun phrase or clause | 4.4 |
| 12 | Trailing clause | **wun**, **gi**, **don**, **nin** … clause | 4.4 |
| 13 | Stance | a pause, then **min**, **a**, **buni**, **donon** … | 7.2 |
| 14 | Calling someone | a pause, then a name, title, role or kin word | 10.1 |

### 4.2 The verb and its objects

- **A content word's role comes from its position.** Any content word can be a noun, a verb or a modifier: **sepi** "apologise / an apology".
- **After a subject, the next content word is the verb:** **ewo niba** "the person walks". To describe a noun with a verb, use a relative clause: **ewo man niba** "the person who walks" (5.3).
- **Object or manner:** a content word after the verb is its object if the verb takes one, otherwise its manner: **oyi fanse** "say calmly". To mark manner unambiguously after an object, put it after the object: **nawi pasu yobe**.
- **Two objects:** recipient, then thing: **tofo me nuta** "teach you fear".
- **Verb + verb:** if the first verb takes an object (want, try, need, must, can, start, stop, teach, see, like, help…), the second verb is that object: **walo alun** "try to break". Otherwise the second describes the first: **goyu pume** "sit thinking".
- **muge** "do; make": **muge** + result + object = "make (it) so": **muge upe tan** "fix this"; **muge** + object + manner = "do (it) so": **muge tan upe** "do this well".
- **Command:** a command needs **tin** (or **so** for a request). Without a particle a sentence is a statement.

### 4.3 Openers

- **Scene-setting:** a time or place phrase may open the sentence: **mon minfi, …** "at noon, …". It changes no roles.
- **Topic:** **pi** + a noun phrase at the start = "as for X": **pi tale la, no kuwi guyi yidu bu la.** "As for the cars, the caretaker takes them." At the start, **pi** has no other reading.
- **If/when clause:** **don** "if", **nin** "while/when", **wo** "after", **ya** "before", **gi** "because" + clause.
- **Order** when several open a sentence: linker, scene or topic, if/when clause; then the speech-act particle.
- **Only person words call someone.** A fronted phrase that isn't a person word is a scene or topic phrase.

### 4.4 Clauses and relation phrases

- **A relation phrase** (**mon**, **tun**, **se**, **gan**, **li**, **ya**, **wo**, **fu**, **nin**) at clause level attaches to the clause's verb. Inside a noun phrase, only **pi** attaches to a noun; give a noun any other relation with a relative clause: **sola man gun mon bige pi yolan** "the road that is above the river". In comparisons and quantities (9.3) **se**, **tun** and **fu** belong to their number or adjective.
- **A relation word may drop its object** when context supplies it (**wo** "after that", **ya** "beforehand"). It then ends its clause or comes before a pause.
- **A relation word can take a clause** (**wo wan la yidu ewo bo** "after they took someone") or an action noun (**se kusa** "from leaving").
- **Clause attachment:**
  - a relative clause attaches to the nearest noun before it;
  - a time, reason or condition clause at the **start** of a sentence belongs to the main clause; at the **end**, to the innermost clause before it, unless a pause closes that clause first: **nin leso, to sin miya ewo man sigo** "in the morning, I watched the person who came back"; **to sin miya ewo man sigo nin leso** "I watched the person who came back in the morning".
- **Joining:** **yen** "and", **lu** "or", **un** "but" join nouns, verbs, modifiers or clauses. To list nouns rather than modify one with another, use **yen**: **mole yen wede** "mother and father". **lu X lu Y** = "either X or Y, not both".
- **Quotes:** framed by a say-verb; quotation marks in writing. A quote is its own sentence with its own speech-act particle. Broken-off speech just stops.

### 4.5 Leaving things out

- **Anything the listener can supply from context may be left out:** the subject, the object, the object of a relation word, the verb. An answer or follow-up can be just the new part: **muyi yu, moti.** "what time, again?"; **nagu me la mon dili pi ufo.** "see you all Saturday".
- **Exception:** a clause that starts with **gun** and no subject means "there is" (4.7). To say "(it) is X", keep the subject: **bu gun nimo** "it's money". With **gun** left out too, a bare state is fine: **bi upe.** "very good."
- When leaving something out could be unclear, say it.

### 4.6 Pauses

A pause (a comma in writing) goes wherever a phrase could otherwise run on. Its places:
- after someone called at the start, and before someone called at the end;
- after an opener (linker, scene, topic, if/when clause);
- after a subject that contains a clause or a phrasal derived word, before its verb (**no sanwa man … sin sege, keya unfu …**);
- between a recipient and a long object;
- between clauses joined by **yen**/**un** when the first ends in a noun;
- before a stance word;
- between a larger and a smaller calendar unit (**dunan pi yawu, dili pi mape**);
- after a relative clause, to close it before more material.

In casual writing, pauses that context makes obvious may be dropped.

### 4.7 "Is": gun

- **gun** + state: **guyi gun kudu** "the house is big" (**guyi kudu** is "the big house").
- **gun** + noun: **wan gun tiwu** "she is a child".
- **gun** + place phrase: **wan gun mon guyi** "he is at home".
- **gun** + action word = the resulting state: **gun tapi** "is closed".
- **gun** + **wun** clause: "is that …".
- After another verb, **gun** = "to be": **momu gun tiwu** "want to be a child".
- **gun** at the start of a clause with no subject = "there is": **un, gun musu feli** "but there are many things".

### 4.8 Questions and answers

- **Yes/no question:** **min** at the start. A clause-final **min** is a tag "…, right?".
- **Question words stay where the answer goes**, and need no **min**: **me momu wun to oyi yu.** "you want me to say what?"
- **Question words** are built: **yu** what; **ewo yu** who; **X yu** which X; **mon kemu yu** where; **mon muyi yu** when; **gi yu** why; **fu yu** how; **wifu yu** how many/much; **pi ewo yu** whose.
- **Choices:** **min … lu …** "either?"; **… lu … yu** "which?" (answer by echoing the choice).
- **Indirect question:** **yu** or **min** inside a **wun** clause: **to mu lugo wun min …** "I don't know whether …".
- **Answers echo the verb;** there are no words for yes and no: "Aren't you coming?" → **obu** / **mu obu**. A question with **gun** is answered by echoing what follows **gun**: "Is the house big?" → **kudu** / **mu kudu**. Acknowledgment: **mm** heard; an echo understood; **de** + verb "will do".

## 5. The noun phrase

### 5.1 Template

Noun, content modifiers, number, **la**, determiner, **pi** phrase, relative clause: **guyi kudu sa la tan pi en mara man …**. Titles and **lanno** come before the noun (10.1); phrase operators before the whole phrase (6.2).

### 5.2 Parts

- **Content modifiers** follow the noun: **guyi kudu** "big house".
- **Gender** is a modifier, stated once when it matters: **tiwu futa** "daughter", **no wungu futa** "the leader, a woman".
- **Noun + noun** is used only for gender and for the compounds in `compounds.tsv`. For other relations, use **pi** or a relative clause.
- **Number:** noun + number = a count (**dili oma** "seven days"); noun + **pi** + number = a label (**kemin pi sa** "document 2").
- **Plural la** is optional; a count or context can show plurality.
- **There are no articles.** Known vs new is left to context, or shown with **tan**, **ben**, **bo** or a number.
- **Determiners** (table, section 13), and **mesun** "each", follow the noun: **guyi tan** "this house", **ewo bo** "someone", **musu bo** "something", **pu nume mesun** "each home". A determiner right after a noun or pronoun belongs to it, so to give a recipient a standalone determiner as the thing, use **tun**: **to iko ben tun wan** "I told that to him" (**to iko wan ben** is "I told that-him"). A determiner may stand alone as a noun phrase: **we** "all", **in** "some", **fa** "none". Part of a whole: determiner or number + **pi** + noun: **kin pi foto la** "some of the photos", **fi pi ka** "one of three".
- **pi** "of" links a noun to a noun: **guyi pi en mara** "Mara's house". Each **pi** attaches to the nearest noun before it.

### 5.3 Relative clauses

**man** + clause after the noun. The noun fills the missing role:
- subject: **ewo man niba** "the person who walks";
- object: **mabo man me la yaga** "the papers you put";
- place or time: end the clause with the relation word: **kemu man to nume mon** "the place where I live".

No word closes a relative clause; a pause closes it.

### 5.4 Derived words

Four markers before a verb or verb phrase name a role in the action:

| Marker | Role | Example |
|---|---|---|
| **no** | the one who does it | **no febo** "one who answers" |
| **ge** | the thing done or made | **ge iko** "what is told" = news |
| **du** | the thing used | **du bubo** "thing for laughing" = a joke |
| **pu** | the place | **pu niba** "place for walking" = a path |

- The base may be a verb phrase: **no isi se guyi** "one who goes from home" = traveller. It runs to the end of its phrase, like a relative clause; a pause separates it from a following verb.
- A person something is done to: **ewo man gun** + verb: **ewo man gun tofo** "a student".
- With a noun base, link with **pi** or a verb: **pu pi mabo** "an office", **no obu se yaye** "an alien".
- Opposites: **mu** + word = "not X" (**mu upe** "not good"); a separate opposite root names the other pole (**yomo** "bad").

## 6. Operators

### 6.1 Clause operators

They start the clause (slot 5) and cover all of it.
- **Confidence:** **kon** + a number of sixths = the chance in 6 the statement is true: **kon po** impossible, **kon fi** unlikely, **kon sa** doubtful, **kon ka** even odds, **kon da** likely, **kon te** very likely, **kon ufo** certain; **kon te mimi te** 5.5 in 6; **kon bo** "don't know how sure". An unmarked statement is believed. Exact probabilities use a number and **pasentu**.
- **Source:** **wanme** seen, **inwun** told, **wemen** inferred. Optional.
- "Might" and "must" meaning *probably* are confidence: "She must be home" = **kon te wan gun mon guyi**.

### 6.2 Phrase operators

They cover the word or phrase right after them; before the verb they cover the predicate.
- **mu** not (**to mu yidu bu** "I didn't take it"; **mu mu** emphatic);
- **na** only; **fe** also; **wi** even (**wi don** "even if"); **o** focus, "this one, not another" (**o en tomas yidu bu** "*Tomas* took it"; before the verb it insists: **to o unfu** "I *did* pay");
- **konsin** at least; **nedin** almost; **mesun** each;
- degree words **ke** more, **bi** very, **tason** rather (**ke kudu** "bigger"; **nimo ke uyo** "less money").
- **Order before the verb:** phrase operators, then **manni**, then aspect, then the verb: **to fe manni le doku**.

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
- **genso** or **ba** may modify it from in front of its particle: **genso min me lugo** "as if you'd know"; **ba min** a surprised or indignant question.
- Someone else's intention is reported (**inwun**) or stated with time words and **kon**; **de** is only for the speaker's own commitment.

### 7.2 Stance (slot 13)

After a pause at the end, a word comments on the whole sentence, whatever its speech act:
- **min** "…, right?" (checks);
- **a** "as you know, you see" (shared ground): **wan sin oyi bu, a.**;
- **buni** "okay?" (softens, invites agreement): **so pen isi, buni.**;
- **donon** "it turned out" (against expectation): **wan gun no ibe guyi, donon.**
- A half-remembered "wasn't it?" is low confidence plus the tag: **kon ka wan sin oyi bu, min.**
- If two stance words occur, **min** comes last.
- Other words used in this position are stance words too.

## 8. Time

### 8.1 Tense and aspect

- **Tense is optional.** A time word or a narrative's first **sin** sets the time; later verbs stay unmarked. The future is shown by a time word or context: **wuma gegi muwo** "it will rain tomorrow".
- **Aspect** (right before the verb): **sin** done (with a past frame: past; with a future frame: "will have"); **le** ongoing, also "still"; **buntu** about to. **sin** and **le** don't combine: "was doing" = a past frame + **le**.
- **mu sin** "not yet". "Didn't do" = a past frame + **mu** + verb.
- **Habit:** **manni** "usually"; with a past frame, "used to".
- **Intent:** **gan momu** "on purpose", **mu gan momu** "by accident".

### 8.2 Time words

- **Roots:** **eda** now, **mefa** today, **wuma** tomorrow, **afe** yesterday; **dili** day, **nelon** week (7 days), **dunan** month (also "moon"), **fawu** year; **muyi** time (a span or a point); **gimu** occasion (**gimu sa** "twice").
- **Anchor + offset:** the offset names its unit: **wuma wo dili fi** "the day after tomorrow". With no anchor, the anchor is now: **wo nelon fi** "next week", **ya dunan fi** "a month ago". Any time or event can be the anchor.
- **Duration** is a count: **awuwa ka** "three hours". **nin** + duration = "during, for" a span that frames the clause: **nin dili oma** "for seven days".
- **Age** is lived time: **to nume fawu ka yawu** "I have lived 30 years".
- **Hours, minutes, seconds** are borrowed: **awuwa**, **minitu**, **sekandu**.

### 8.3 Clock, calendar, dates

- **The clock follows the speaker's culture;** both styles are always understood.
  - **24-hour:** four digits read one at a time: **mon po mape ka po** "at 09:30", **mon sa fi ka po** "at 21:30".
  - **12-hour:** the hour counted (1–12), then the minutes as two digits, then optionally **pi** + part of the day: **mon mape ka po pi yami** "at 9:30 at night"; **mon yawu po sa** "at 10:02"; on the hour, the hour alone: **mon yawu sa** "at 12".
  - **Parts of the day:** **leso** morning, **minfi** noon, **duwun** afternoon, **kegin** evening, **yami** night; midnight = **yawu sa pi yami**.
  - **About** a time: **fu** before it: **mon fu minfi** "around noon".
- **Weekdays:** **dili pi** + 1–7 on its own, Monday = 1 (ISO 8601): **dili pi ka** "Wednesday". A day of the month is said with its month.
- **Dates:** larger unit first, a pause between: **dunan pi yawu, dili pi mape** "October 9"; a weekday with a time: **dili pi te, mon …**. Years are read digit by digit: **fawu pi sa po sa ufo** "2026".
- **Senary calendar:** [measurement.md](measurement.md).

## 9. Numbers

### 9.1 Digits and place words

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| **po** | **fi** | **sa** | **ka** | **da** | **te** | **ufo** | **oma** | **kefi** | **mape** |

| 10 | 100 | 1000 | million | billion | point | minus | × 10 to the |
|---|---|---|---|---|---|---|---|
| **yawu** | **loki** | **munno** | **tonen** | **siwin** | **mimi** | **guti** | **unun** |

### 9.2 Reading numbers

- **Quantity reading:** place words in descending order, each preceded by its digit; a 1 before a place word is dropped; zero places are skipped: 15 **yawu te**, 50 **te yawu**, 42 **da yawu sa**, 105 **loki te**. A group word takes a whole number before it: 250 000 = **sa loki te yawu munno**.
- **Digit reading:** one digit at a time, whenever the exact digits matter more than the size: identifiers, phone numbers and codes (in groups of three from the right), years and 24-hour clock times (as one four-digit group).
- **Labels** (noun + **pi** + number) under 100 use the quantity reading (**dili pi yawu da** "day 14"); larger labels use digit reading.
- **Decimals:** **mimi** "point": 1.5 = **fi mimi te**. **guti** minus; **unun** "× 10 to the": **ka unun guti ufo** = 3 × 10⁻⁶.
- **Senary numbers:** **senali** + digits: **senali sa po** = 20₆ = 12.

### 9.3 Amounts and comparison

- **About:** **fu** + number: **ewo fu ka yawu** "about 30 people".
- **Range:** **se** X **tun** Y. **At least** **konsin** X; **at most** **mu ke se** X.
- **Enough:** **tonya**.
- **Comparison:** **ke** + quality + **se** + standard: **ke kudu se guyi ben** "bigger than that house". Most: **ke** + quality + **se we** "more … than all". Less: **ke** + the opposite (**ke meli** "smaller"). As … as: **fu** (**kudu fu bu** "as big as it").
- **Measurements:** borrowed international unit names, unit first like any counted noun: **kilamita te** "5 km". The native unit roots in the lexicon belong to the senary system ([measurement.md](measurement.md)).

## 10. People

### 10.1 Calling someone, titles, respect

- **Calling someone** by name, title, role or kin word: at the start (slot 1, attention) or the end (slot 14, softening): **en mara, tin obu.** / **tin obu, en mara.**
- **Titles** go before the name, with no comma, and work in address and reference: **no tofo en mara** "Teacher Mara"; **no tofo en mara sin oyi** "Teacher Mara said".
- **lanno** is the title of respect, without gender: before a name, role or kin word (**lanno en olusegun** "Mr/Ms Olusegun", **lanno faba pi wede** "Uncle"); alone in address (**lanno, so nun …** "Sir/Madam, please …"); alone in reference when context shows who (**lanno sin oyi** "the boss said"). It marks respect for the person named; it never means "you".
- **There is no apposition:** describe someone with a title before the name, a relative clause, or a new sentence.

### 10.2 Politeness and routines

- **nun** adds politeness or deference and nothing else. It goes right after the speech-act particle, or first in a statement: **so nun …** "please …"; **nun nun** more.
- **No polite pronouns and no speech levels:** **me** is "you" to anyone. Respect is carried by **lanno**, titles and **nun**.
- **Politeness never changes the act:** a polite instruction is **tin nun**; a polite warning is **yo nun**: **yo nun osa le obu. fon nun pen wupi isi.** "(Warning, politely) the water is coming. (Advice, politely) we need to go."
- **In an emergency (yo yo)** no **nun** is expected.
- **Routines** are fixed formulas: greeting **upe**, **upe leso** "good morning"; farewell **upe isi** "go well"; thanks **lota**; sorry **sepi**; with politeness, **nun** first: **nun upe leso**.

### 10.3 Reference

- **wan** "he/she": the person or animal being talked about. **yi** another one who isn't the topic: **wan nagu yi** "she saw him". A newcomer is **yi** or named until the speaker makes them the topic.
- **bu** "it": the thing being talked about. **ben** alone: a thing that isn't the topic: **min me momu bu lu ben yu.** "this one or that one?"
- **tan** / **ben** alone for an event, statement or situation: **tan** nearer (what I'm saying, here and now), **ben** further (what you said, an earlier event): **ben gun upe** "that's good"; **gi tan** "so". (For a recipient, see 5.2.)
- **sun** in reported speech or thought: the person whose words are reported.
- **go** anyone, people in general; **me** is only ever the listener, never generic. An unknown doer is **ewo bo**.
- **nen** self: as object, reflexive (**to kuwi nen** "I keep myself"); after a noun or pronoun, "in person" (**wan nen obu** "he came himself").
- **pen** we including you, **din** we not including you.
- A pronoun never means the subject of its own clause (that's **nen**). The listener finds referents from context; if it could be unclear, name them.

## 11. Names, loans, new words

- **Names** take **en**: **en mara**. A personal or brand name keeps its owner's spelling, lowercase, even with letters the language lacks: **en denise**, **en xi jinping**, **en nguyen**, **en wi-fi**. Say it as close to its owner's pronunciation as you can. Place names are names: **en london**; an established adapted form may be used instead: **en landan**. Names aren't used as verbs.
- **Adapted form** (`tools/names.py`): the spoken fallback for a name, and the form of every loan:
  - each foreign sound becomes the nearest native sound: r → l, v → b, ʋ → w, z/sh/zh → s, th → f, dh → d, ch → t, j → d, kh → k; h and glottal sounds disappear; ng → n; length, aspiration and tone are dropped; ə, ʌ, æ → a;
  - two vowels in a row get a glide: y after i or e, w otherwise;
  - a consonant that can't stand where it is gets an added **u**;
  - the result has at least two syllables (glide included: **tuwu**).
- **Loans** (no **en**) only where the world shares a form, taken in that international form; a loan enters the lexicon once it is common, and until then near-collisions are tolerated: **dola** dollar, **minitu**, **kilamita**, **pasentu**, **intalunetu**, **imeyilu**, **kamela**, **foto**. Everything else is said with native words, built words or phrases.
- **Computers and interfaces** use everyday words: search **ditun**, delete **nuton**, share **peton**, copy **gayen**, add **ginni**, download **dunu**, install **yaga**, turn on/off **benbi**/**tapi**, settings **ge finsa la**, computer **du sunbu** (`compounds.tsv`). **doku** "work" covers a machine working.
- **Letters as labels** (flat 3B) pass through and are read as the speaker's culture reads them.
- **New words** are made by the method in [vocabulary-method.md](vocabulary-method.md).

## 12. Conditions and modality

- **Conditions:** **don** "if" + clause. **kon** + number after **don** says how likely the condition is: **don kon fi** "if (unlikely)"; **don kon po** "if (and it isn't so)" is counterfactual: **don kon po to sin isi, to sin nagu wan** "if I had gone, I would have seen her". The main clause is the consequence; there is no "would".
- **Modality, three kinds:** ability **lenu** "can"; obligation **keya** "must", **wupi** "need to, should" (for anyone); permission **efon** "allow" (**me gun efon nawi** "you may eat"). Probability is confidence (6.1).
- **Purpose:** **li** + verb "in order to": **li bika** "to buy".
- **Let's:** **so pen** …; **don't:** **tin mu** ….

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

**Two-syllable operators** (stressed on the first syllable): not literal **genso**, seen **wanme**, told **inwun**, inferred **wemen**, at least **konsin**, about to **buntu**, rather **tason**, almost **nedin**, each **mesun**, usually **manni**, "okay?" **buni**, "it turned out" **donon**, title **lanno**.

## 14. Vocabulary

- [../data/lexicon.tsv](../data/lexicon.tsv): roots and loans, each with a field and a frequency tier (1 rare – 5 most common). [../data/grammar.tsv](../data/grammar.tsv): grammar words. [../data/numbers.tsv](../data/numbers.tsv): number words. [../data/compounds.tsv](../data/compounds.tsv): established compounds.
- A gloss with a second gloss after a comma fixes the sense: **gufu** "hard, not soft". A root means that sense only.
- One root may cover senses most language families lump: **apu** "word; language"; context tells them apart.

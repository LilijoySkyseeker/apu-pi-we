# Learning Apu Pi We: a guide for English speakers

Written 2026-10-09 for someone who speaks only English. The full rules are in [language.md](language.md); this guide gives you the order to learn them in, the parts English makes hard, and how to practise.

## Before you start

- **The language is small and unfinished.** About 450 root words, 64 little grammar words, six digits. Your vocabulary hits its ceiling quickly, and that's normal here: when there's no word, you **describe** the thing. Describing is the core skill, not a fallback (lesson 11).
- **Nothing changes shape.** No verb endings, no plurals you must add, no "a/the", no gender, no irregular anything. Almost all the difficulty is in sounds, word order and numbers.
- **There is no one else to talk to yet, except me.** Start any Claude session with "let's practise Apu Pi We at my level" and I'll talk with you, correct you, and explain. That's your conversation partner.
- **When you hit a gap, tell me.** Real use is how the language grows. A gap you find is data, not failure.

## How to study

A plan that fits 15–20 minutes a day:

1. **Week 1:** lessons 1–4, and the 50 most common words (tiers 5 and 4 in the lexicon).
2. **Week 2:** lessons 5–8, and the grammar-word table (the traps first).
3. **Week 3:** lessons 9–10 (numbers and time). Count things in base 6 every day.
4. **Week 4 on:** lessons 11–12, the next 132 words (tier 3), and short conversations with me.

Three habits matter more than the schedule:

- **Say everything aloud.** Reading silently trains your eyes, not your mouth.
- **Use spaced repetition for words.** [../data/lexicon.tsv](../data/lexicon.tsv) imports straight into Anki: map the `gloss` column to the front and `form` to the back, and start with tier 5 and 4. Do the same with [../data/grammar.tsv](../data/grammar.tsv).
- **Make your own sentences early,** even wrong ones. Bring them to me.

## Lesson 1: Sounds

The sounds are easy for an English speaker. The hard part is what English does *to* sounds without you noticing.

| Letter | Say it like | Watch out |
|---|---|---|
| **a** | *father* | |
| **e** | *bet* | never "ay" as in *day* |
| **i** | *machine* | never "eye" |
| **o** | *go*, but cut short | no "oo" glide at the end (Spanish *no*) |
| **u** | *rule* | never "yoo" |
| **p t k b d** | as in English | |
| **g** | *get* | always hard, never *gem* |
| **s** | *see* | always s, never z |
| **m n l f** | as in English | |
| **w y** | *we*, *yes* | always consonants |

- **Every letter is said, every time.** **ewo** "person" is *e-wo*, three sounds, two syllables. **apu** is *a-pu*.
- **The only consonant that ends a syllable is n:** **lon** "I", **kegin** "evening".
- **The one-letter-per-sound rule has no exceptions.** If you can read it, you can say it.

**The big English habit to break: don't swallow unstressed vowels.** English turns most unstressed vowels into "uh" (*banana* = buh-NA-nuh). Here every vowel keeps its full sound: **apu** is "AH-poo", not "AH-puh"; **dili** "day" is "DEE-lee", not "DIL-ee". Think Spanish or Japanese: even, clear syllables.

**Stress:**
- **Words of two or more syllables are stressed on the first syllable**, always: **TO-tu** "dog", **GU-yi** "house". Stress is *higher pitch*, not extra length or loudness.
- **One-syllable words are grammar words, said low and quick** (**lon**, **me**, **pi**, **mu**…). The six digits are the exception: they're stressed.
- **Across a phrase, the stressed syllables step down like a staircase** and reset after a comma or full stop. English already does this; just don't fight it.
- **Questions don't need a rising voice.** The first word already says it's a question. Rising anyway is fine.

**Practice:** read these aloud, slowly then normally: **ewo, osa, guyi, totu, pasu, upe, momu, nagu, lugo, oyi**. Check that each vowel sounds the same in every position.

## Lesson 2: First sentences

The order is **who + does + what**, like English:

- **lon nagu totu.** "I see a dog." / "I see the dog."
- **me momu osa.** "You want water."
- **wan nawi pasu.** "She eats food." (or "he": **wan** is both)

There is no "a" or "the", and the verb never changes: **lon nagu**, **wan nagu**, **pen nagu** ("we see"). Plural is usually left out; add **la** only if it matters (**totu la** "dogs"), or just give the number (**totu sa** "two dogs").

## Lesson 3: Describing words come after

This is the first real switch for English speakers: **anything that describes a word comes after it.**

- **guyi kudu** "big house" (house big)
- **totu tan** "this dog" (dog this)
- **ewo niba** "a walking person"

To *say* something is big, use **gun** "is":

- **guyi gun kudu.** "The house is big."
- **guyi kudu** alone is just "the big house", not a sentence. This is the most common early mistake.

Degree words are the one thing that goes *before*: **bi kudu** "very big", **ke kudu** "bigger".

## Lesson 4: No, questions and answers

- **NOT** is **mu**, before what it denies: **lon mu lugo.** "I don't know."
- **Yes/no questions start with min:** **min me momu osa.** "Do you want water?"
- **There are no words for yes and no. You answer by repeating the verb:** **momu** "(I) want (it)", **mu momu** "(I) don't want (it)". This feels strange for a week and then very natural.
- **Question words stay where the answer goes.** English moves *what* to the front; this language doesn't:
  - **me momu yu.** "What do you want?" (you want what)
  - **ewo yu obu.** "Who is coming?" (person-what comes)
  - **me kusa gi yu.** "Why are you leaving?" (you leave because-what)
  - **me muge bu fu yu.** "How did you do it?" (you do it like-what)

## Lesson 5: Pronouns

| | |
|---|---|
| **lon** | I, me |
| **me** | you (anyone, any number) |
| **pen** | we, including you |
| **din** | we, not including you |
| **wan** | he or she (the most recent person who did something) |
| **yi** | the other one (the person before that) |
| **bu** | it (the most recent thing) |
| **wan la** | they |
| **nen** | self: **lon miya nen** "I look at myself" |
| **go** | anyone, people in general |

**Watch me: it means "you", not "me".** Expect to trip on this for a while.

**pen / din:** English "we" hides whether the listener is included. Here you have to choose: **pen isi** "let's go, you and I" vs **din isi** "we're going (without you)".

**wan and yi** follow a simple, mechanical rule: **wan** is the most recent person who was the subject of a clause, **yi** the one before. So in a story with two people, **wan** and **yi** keep them apart without names. Name someone again when there are three or more.

## Lesson 6: Little words that look like English

Many grammar words are spelled like English words and mean something else. Learn these as a set:

| Looks like | Means | Example |
|---|---|---|
| **me** | you | **me obu** "you come" |
| **no** | the one who… | **no tofo** "one who teaches", a teacher |
| **go** | anyone | |
| **we** | all | **ewo we** "all people", everyone |
| **in** | some | **pasu in** "some food" |
| **to** | rather | **to kudu** "rather big" |
| **a** | not literal (joking, irony) | **a lon bi sogi.** "I'm *so* happy." (sarcastic) |
| **so** | please / request | **so neke lon osa.** "Please give me water." |
| **man** | who, which | **ewo man obu** "the person who comes" |
| **sin** | done (finished) | **lon sin nawi.** "I've eaten." |
| **don** | if | |
| **fen** | (I was) told | **fen wan kusa.** "She left, I'm told." |

## Lesson 7: Of, at, to, from, with

The relation words come before their noun, as in English:

- **pi** of: **guyi pi lon** "my house" (house of me); **guyi pi en mala** "Mara's house"
- **mon** at, in: **wan gun mon guyi.** "She's at home."
- **tun** to: **lon isi tun guyi.** "I'm going home."
- **se** from: **wan obu se guyi.** "He comes from home."
- **gan** with: **lon isi gan me.** "I'm going with you."
- **li** for: **li me** "for you"
- **ya** before, **wo** after

Giving something to someone: **verb + who gets it + what**: **neke lon osa** "give me water".

Names always take **en**: **en mala** "Mara". Names are adapted to the sounds: Lilith becomes **en lilifu**. Ask me to adapt yours.

## Lesson 8: Being polite, and everyday phrases

- **upe** hello ("good"), **upe leso** good morning, **upe isi** goodbye ("go well")
- **lota** thanks, **sepi** sorry
- **ku** makes anything polite: **so ku neke lon osa.** "Could you please give me water?" Add more for more: **ku ku**.
- **mm** "I heard you", **huh?** "say again"

The first word of a sentence can say what kind of sentence it is. You'll mostly use these:

| | |
|---|---|
| **min** | question |
| **so** | request |
| **tin** | instruction ("do this") |
| **fon** | advice ("I'd suggest…; your call") |
| **de** | "I'll…" (I intend) |
| **yo** | warning; **yo yo** = emergency |
| **ba** | exclamation |

Being polite never means hinting. English softens a warning into "might want to check the stove"; here you say **yo ku** (warning, politely) and then the problem.

## Lesson 9: Numbers in base 6

This is the hardest part for anyone raised on base 10, because you have to stop translating.

**The digits:** **po** 0, **fi** 1, **sa** 2, **ka** 3, **da** 4, **te** 5.

**Place words:** **nobi** 6, **miko** 36 (6×6), **niyu** 216. Build numbers digit + place word, biggest first. A 1 before a place word is dropped:

| Number | Said | Meaning |
|---|---|---|
| 6 | **nobi** | six |
| 7 | **nobi fi** | six and one |
| 12 | **sa nobi** | two sixes |
| 13 | **sa nobi fi** | two sixes and one |
| 35 | **te nobi te** | five sixes and five |
| 36 | **miko** | |
| 42 | **miko nobi** | 36 + 6 |

**Count on two hands.** Your right hand shows 0–5 ones, your left hand 0–5 sixes. Two hands count to 35 (**te nobi te**). Do it with real things every day (steps, cups, people on a bus) and **say the number in the language, never in English first**. The goal is to stop thinking "13" at all and think **sa nobi fi**.

- **Counting things:** the thing, then the number: **totu sa** "two dogs", **dili nobi fi** "seven days".
- **Phone numbers and codes** are read digit by digit, in groups of four.
- **Half** is **po mimi ka** (0.3 in base 6: **mimi** is the point). A third is **po mimi sa**.

## Lesson 10: Time

- **Tense is optional.** Say when once, then stop marking it: **afe, lon nawi pasu.** "Yesterday, I ate food."
- **eda** now, **mefa** today, **wuma** tomorrow, **afe** yesterday.
- **sin** done (**lon sin nawi** "I've eaten"), **le** in progress (**lon le nawi** "I'm eating"), **win** about to (**lon win kusa** "I'm about to leave").
- **Offsets from now:** **wo nelon fi** "after one week" = next week; **ya boyo fi** "before one block" = a block ago. A **nelon** is a six-day week; a **boyo** is 36 days, the language's "month".
- **Clock time is the fraction of the day,** read digit by digit after **mimi**: **mon mimi ka** "at .3" = noon, **mon mimi da** = 16:00. An **aya** "watch" is 4 hours.
- **Age is time lived:** **lon nume fawu …** "I have lived … years".

## Lesson 11: Making words you don't have

This is the skill that makes a small vocabulary enough. Four markers turn an action into a noun:

| | | |
|---|---|---|
| **no** + verb | the one who does it | **no tofo** teacher, **no wungu** leader |
| **ge** + verb | the thing done or made | **ge iko** news ("what's told") |
| **du** + verb | the thing used for it | **du nawi** something to eat with |
| **pu** + verb | the place for it | **pu wopo** bedroom ("place for sleeping") |

- **A person it's done to:** **ewo gun tofo** student ("person who is taught").
- **Linking two nouns:** use **pi**: **pu pi mabo** an office ("place of paper").
- **Anything else: describe it.** Don't know "spider"? **noso meli pi bendo feli** "small animal of many legs". That isn't a workaround; it's how the language works.

## Lesson 12: Longer sentences

- **yen** and, **lu** or, **un** but
- **don** if, **gi** because, **nin** while
- **wun** that (**lon pume wun …** "I think that …")
- **man** who/which (**ewo man obu** "the person who comes")
- **Put a comma where you'd pause:** after a clause that opens the sentence (**don me obu, lon sogi.** "If you come, I'll be happy."), and after a long subject.
- **Whether a clause goes first or last changes what it attaches to.** At the start, it belongs to the main sentence. At the end, it belongs to the nearest clause. Full rule: [language.md](language.md), rule 15.

## Two things English doesn't have

You can skip these at first. Learn them once the basics are easy.

- **How sure you are, as a number of sixths:** **kon da wan obu** "4 in 6 she's coming" (likely). **kon nobi** is certain, **kon po** impossible. It's optional; plain statements mean you believe them.
- **How you know:** **o** "I saw it", **fen** "I was told", **san** "I worked it out". Also optional.

## Where to go next

- The three translated texts, [../texts/](../texts/), have word-by-word glosses.
- The full reference: [language.md](language.md).
- Measurements, dates and the calendar: [measurement.md](measurement.md).
- And conversation: start a session and say **upe**.

# Learning Apu Pi We: a guide for English speakers

Written 2026-10-09 for someone who speaks only English. The full rules are in [language.md](language.md); this guide gives you the order to learn them in, the parts English makes hard, and how to practise.

## Before you start

- **The language is small and unfinished.** About 480 root words and two dozen borrowed international words, 61 one-syllable grammar words plus 13 two-syllable ones, and the number words. Your vocabulary hits its ceiling quickly, and that's normal here: when there's no word, you **describe** the thing. Describing is the core skill, not a fallback (lesson 11).
- **Nothing changes shape.** No verb endings, no plurals you must add, no "a/the", no gender, no irregular anything. Almost all the difficulty is in sounds, word order and numbers.
- **There is no one else to talk to yet, except me.** Start any Claude session with "let's practise Apu Pi We at my level" and I'll talk with you, correct you, and explain. That's your conversation partner.
- **When you hit a gap, tell me.** Real use is how the language grows. A gap you find is data, not failure.

## How to study

A plan that fits 15–20 minutes a day:

1. **Week 1:** lessons 1–4, and the 61 most common words (tiers 5 and 4 in the lexicon).
2. **Week 2:** lessons 5–8, and the grammar-word table (the traps first).
3. **Week 3:** lessons 9–10 (numbers and time). Count things aloud every day.
4. **Week 4 on:** lessons 11–14, the next 181 words (tier 3), and short conversations with me.

Three habits matter more than the schedule:

- **Say everything aloud.** Reading silently trains your eyes, not your mouth.
- **Use spaced repetition for words.** [../data/lexicon.tsv](../data/lexicon.tsv) imports straight into Anki: map the `gloss` column to the front and `form` and `kind` to the back, and start with tier 5 and 4. The kind (thing, action or quality) matters; lesson 3 shows why. Do the same with [../data/grammar.tsv](../data/grammar.tsv).
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
| **g** | *get* | hard *g* is the standard; some speakers say a soft "j" before i and e, which is harmless |
| **s** | *see* | always s, never z |
| **m n l f** | as in English | |
| **w y** | *we*, *yes* | always consonants |

- **Every letter is said, every time.** **ewo** "person" is *e-wo*, three sounds, two syllables. **apu** is *a-pu*.
- **The only consonant that ends a syllable is n:** **to** "I", **kegin** "evening".
- **One letter, one sound.** If you can read it, you can say it.
- **Some softening is harmless.** Speakers may say k and g like "ch" and "j" before i and e, say a vowel plus n through the nose, or soften a consonant between vowels. These variants are never written and never change meaning. Grammar words always keep their consonants.

**The big English habit to break: don't swallow unstressed vowels.** English turns most unstressed vowels into "uh" (*banana* = buh-NA-nuh). Here every vowel keeps its full sound: **apu** is "AH-poo", not "AH-puh"; **dili** "day" is "DEE-lee", not "DIL-ee". Think Spanish or Japanese: even, clear syllables.

**Stress:**
- **Words of two or more syllables are stressed on the first syllable**, always: **totu** "dog" is *TO-tu*, **guyi** "house" is *GU-yi*. Stress is *higher pitch*, not extra length or loudness.
- **One-syllable words are grammar words, said low and quick** (**to**, **me**, **pi**, **mu**…). The digits 0–5 are the exception: they're stressed.
- **Across a phrase, the stressed syllables step down like a staircase** and reset after a comma or full stop. English already does this; just don't fight it.
- **Questions don't need a rising voice.** **min** or a question word already marks them (lesson 4). Rising anyway is fine.

**Writing:**
- Write in lowercase; capitals mean nothing (and do no harm).
- A comma marks a pause and a full stop ends a sentence. **?** and **!** are allowed but add nothing, so questions often end in a full stop, as in this guide.
- Numbers are written in digits, grouped in threes with a space (`1 250 000`), with `.` for the decimal point.
- Times, dates, unit symbols (`5 km`), links, handles and names stay as they are written.

**Practice:** read these aloud, slowly then normally: **ewo, osa, guyi, totu, pasu, upe, momu, nagu, lugo, oyi**. Check that each vowel sounds the same in every position.

## Lesson 2: First sentences

The order is **who + does + what**, like English:

- **to nagu totu.** "I see a dog." / "I see the dog."
- **me momu osa.** "You want water."
- **wan nawi pasu.** "She eats food." (or "he": **wan** is both)

There is no "a" or "the", and the verb never changes: **to nagu**, **wan nagu**, **pen nagu** ("we see"). Plural is usually left out; add **la** only if it matters (**totu la** "dogs"), or just give the number (**totu sa** "two dogs").

**Two verbs in a row.** If the first verb takes an object (want, try, need, can, start, stop, like, help…), the second verb is that object:
- **to momu isi.** "I want to go."
- **walo alun** "try to break"

Otherwise the second verb describes the first: **goyu pume** "sit thinking".

**muge** "do, make" has two patterns:
- **muge** + result + thing = make it so: **muge upe tan** "fix this" (make good this)
- **muge** + thing + how = do it so: **muge tan upe** "do this well"

**A comma marks a pause:** after anything that opens the sentence (**afe, to nawi pasu.** "Yesterday, I ate food."), and around a name you're calling. Lesson 12 has the full list.

## Lesson 3: Describing words come after

This is the first real switch for English speakers: **a content word that describes another comes after it.**

- **guyi kudu** "big house" (house big)
- **totu tan** "this dog" (dog this)
- **ewo meli** "a small person"

To *say* something is big, use **gun** "is":

- **guyi gun kudu.** "The house is big."
- **guyi kudu** is "the big house", never "the house is big". This is the most common early mistake.

**Every word has a usual kind: a thing, an action or a quality.** The `kind` column of the lexicon tells you which. It shows the *clear* way to read a word that comes right after a noun. In casual talk people blur it and context sorts it out, so getting it "wrong" is never a mistake, just less clear:

| Right after a noun | What it does | Example |
|---|---|---|
| a quality | describes the noun | **ewo meli** "a small person" |
| an action | is the verb: you've made a sentence | **ewo niba** "the person walks" |
| a thing | only gender, or a set compound | **tiwu futa** "daughter" (child woman) |

So to be clear, "a walking person" is not **ewo niba**. Not sure of a word's kind? **man** always makes a description clear. Describe a noun with an action through **man** "who" (lesson 12): **ewo man niba** "the person who walks". Position can still give a word another job: an action word used as an object is a noun (**sepi** "apologise" or "an apology"), and a quality after a verb says how (below).

**gun does more than qualities:**
- **gun** + noun: **wan gun tiwu.** "She is a child."
- **gun** + place: **wan gun mon guyi.** "He's at home." (**mon** "at", lesson 7)
- **gun** + action word = the state that results: **gun tapi** "is closed"
- after another verb, **gun** is "to be": **momu gun tiwu** "want to be a child"
- with no subject, **gun** is "there is": **gun musu feli.** "There are many things."

**Right after the verb,** a quality word says *how*: **oyi fanse** "say calmly". It comes before the object: **nawi yobe pasu** "eat food quickly". (After the object, a quality describes the object: **nawi pasu yobe** "eat fast food".)

**Order after a noun:** describing words, then a number, then **la**, then this/that, then a **pi** phrase (lesson 7), then a **man** clause (lesson 12): **guyi kudu sa la tan** "these two big houses". Gender is just a describing word, used only when it matters: **tiwu futa** "daughter", **tiwu lowu** "son".

**Small operator words come before what they cover:** degree words (**bi kudu** "very big", **ke kudu** "bigger", **tason kudu** "rather big"; "bigger than" is in lesson 9), **mu** "not" and a few others (lesson 4).

## Lesson 4: Not, questions, answers and commands

**Not, also, only, even:**
- **NOT** is **mu**, before what it denies: **to mu lugo.** "I don't know." Doubled, **mu mu** is "definitely not".
- **fe** also, **na** only, **wi** even, each before what it covers: **to fe obu.** "I'm coming too." **na to** "only me". **wi tiwu la obu.** "Even the children came." **wi don** "even if".
- **Focus:** where English stresses a word for contrast, put **o** before it: **o en tomas yidu bu.** "*Tomas* took it." Before the verb it insists: **to o unfu.** "I *did* pay."

**Questions and answers:**
- **Yes/no questions start with min:** **min me momu osa.** "Do you want water?"
- **There are no words for yes and no. You answer by repeating the verb:** **momu** "(I) want (it)", **mu momu** "(I) don't want (it)". This feels strange for a week and then very natural.
- **A question with gun is answered with what follows gun:** **min guyi gun kudu.** "Is the house big?" → **kudu** / **mu kudu**.
- **Saying you got it:** **mm** "heard you"; echoing the answer back means "understood"; **de** + verb means "will do": **de obu** "I'll come".
- **Question words stay where the answer goes.** English moves *what* to the front; this language doesn't:
  - **me momu yu.** "What do you want?" (you want what)
  - **ewo yu obu.** "Who is coming?" (person-what comes)
  - **me kusa gi yu.** "Why are you leaving?" (you leave because-what; **gi** is "because")
  - **me muge bu fu yu.** "How did you do it?" (you do it like-what; **fu** is "like")
- **More question words:** **mon kemu yu** where (at what place), **mon muyi yu** when (at what time), **totu yu** which dog, **wifu yu** how many / how much, **pi ewo yu** whose. **me nume mon kemu yu.** "Where do you live?"
- **Choices:** **min me momu osa lu pasu.** "Do you want water or food (either one)?" **me momu osa lu pasu yu.** "Which do you want, water or food?" Answer by echoing your choice: **osa**.
- **Inside a sentence:** **to mu lugo wun min wan obu.** "I don't know whether she's coming." **to mu lugo wun ewo yu obu.** "I don't know who is coming."

**What kind of sentence it is.** A particle near the start, after any name you're calling or any opener such as **afe,**, says what kind of sentence it is. Without one, a sentence is a plain statement.

| | |
|---|---|
| **min** | question |
| **so** | request ("would you…?"); with "we", "let's": **so pen isi** "let's go"; with someone else, a wish |
| **tin** | instruction ("do this") |
| **fon** | advice ("I'd suggest…; your call") |
| **de** | "I'll…" (I intend), or "we will" for your group: **de din** |
| **yo** | warning; **yo yo** = emergency |
| **ba** | exclamation |
| **genso** | not literal (joking, irony) |

- **A command needs tin:** **tin obu.** "Come." On its own, **obu.** is a statement, "(someone) comes". "Don't" is **tin mu**: **tin mu kusa.** "Don't leave."
- **To ask rather than tell, use so:** **so neke to osa.** "Give me water?" "Please" is **so nun** (lesson 8).
- **genso and ba can go in front of another particle:** **ba min** is a surprised or indignant question; **genso min me lugo.** "As if you'd know." **genso to gun bi sogi.** "I'm *so* happy." (sarcastic)
- **de is only for your own plans** (or your group's). Someone else's plan is said with a time word or **kon** "how sure" (lesson 13).

## Lesson 5: Pronouns

| | |
|---|---|
| **to** | I, me |
| **me** | you (anyone, any number) |
| **pen** | we, including you |
| **din** | we, not including you |
| **wan** | he or she (the person being talked about) |
| **yi** | the other one (someone who isn't the person being talked about) |
| **bu** | it (the thing being talked about) |
| **ben** | that one (a different thing); also "that" for something said or done: **ben gun upe** "that's good" |
| **tan** | this, for something just said or here now: **gi tan** "so" |
| **wan la** | they |
| **nen** | self: **to miya nen** "I look at myself" |
| **sun** | he or she in reported speech: the person whose words are reported |
| **go** | anyone, people in general |

**Watch me: it means "you", not "me".** Expect to trip on this for a while. And **me** is only ever the person you're talking to: English "you" meaning people in general ("you never know") is **go**.

**pen / din:** English "we" hides whether the listener is included. Here you have to choose: **so pen isi** "let's go (you and I)" vs **din isi** "we're going (without you)".

**wan** and **yi** work like English "he" and "she", but split by focus instead of gender: **wan** is the person the conversation is about, **yi** is someone else. So in a story with two people, **wan** and **yi** keep them apart without names: **wan nagu yi** "she saw him". Someone new stays **yi**, or is named, until you make them the topic. Name someone again whenever it could be unclear.

**A pronoun never means the subject of its own clause.** For that, use **nen**: **to miya nen** "I look at myself", never **to miya to**. After a noun or pronoun, **nen** means "in person": **wan nen obu.** "He came himself."

**sun** is for reporting what someone said or thought: **wan oyi wun sun kusa.** "She said that she (herself) was leaving."

**Someone unknown** is **ewo bo** "someone": **ewo bo yidu bu.** "Someone took it."

**Leave out what's obvious.** If the listener already knows who or what, you can drop it, like casual English but more so: **wuma, nagu me.** "See you tomorrow." (**wuma** "tomorrow"), or just **osa.** "Water." as the answer to **me momu yu.** Say it in full when leaving it out could confuse.

**One trap:** a clause that starts with **gun** and has no subject means "there is" (lesson 3). To say "it's money", keep the subject: **bu gun nimo.** With **gun** dropped too, a bare state is fine: **bi upe.** "Very good."

## Lesson 6: Little words that look like English

Many grammar words are spelled like English words and mean something else. Learn these as a set:

| Looks like | Means | Example |
|---|---|---|
| **to** | I (not "to"; "to" is **tun**) | **to obu** "I come" |
| **me** | you | **me obu** "you come" |
| **a** | "you know", at the end of a sentence (not "a") | **wan sin oyi bu, a.** "She said it, you know." |
| **o** | focus: this one, not another | **o to** "*me*" |
| **no** | the one who… | **no tofo** "one who teaches", a teacher |
| **go** | anyone | |
| **we** | all | **ewo we** "all people", everyone |
| **wi** | even (not "we") | **wi to** "even me" |
| **in** | some | **pasu in** "some food" |
| **kin** | some but not all | **kin pi foto la** "some of the photos" |
| **bo** | some (unspecified) | **ewo bo** "someone" |
| **tan** | this | **totu tan** "this dog" |
| **ben** | that | **guyi ben** "that house" |
| **pen** | we, including you | **so pen isi.** "Let's go." |
| **sun** | he/she, in reported speech | lesson 5 |
| **gun** | is | **guyi gun kudu.** "The house is big." |
| **tin** | do it (a command) | **tin obu.** "Come." |
| **nun** | politely | **so nun …** "please …" |
| **yen** | and | **mole yen wede** "mother and father" |
| **so** | a request | **so neke to osa.** "Give me water?" |
| **man** | who, which | **ewo man obu** "the person who comes" |
| **sin** | done (finished) | **to sin nawi.** "I've eaten." |
| **don** | if | |

**Saying "a" and "the".** There are no articles. Usually context is enough; when it matters, use **tan** "this", **ben** "that", **bo** "some (unspecified)" or a number: **ewo bo** "someone", **musu bo** "something". These words go after the noun. Some can stand alone as a noun: **we** "all, everyone", **in** "some", **fa** "none". For part of a whole, use the word or a number + **pi** + noun: **kin pi foto la** "some of the photos", **fi pi ka** "one of three".

## Lesson 7: Of, at, to, from, with

The relation words come before their noun, as in English:

- **pi** of: **guyi pi to** "my house" (house of me); **guyi pi en mara** "Mara's house"
- **mon** at, in: **wan gun mon guyi.** "She's at home."
- **tun** to: **to isi tun guyi.** "I'm going home."
- **se** from: **wan obu se guyi.** "He comes from home."
- **gan** with: **to isi gan me.** "I'm going with you."
- **li** for: **li me** "for you"
- **fu** like, about; **nin** during
- **ya** before, **wo** after. On their own they mean "beforehand" and "after that".

**Only pi joins a noun to a noun.** English builds "house key" or "the road above the river" directly; here you don't. Use **pi**: **tinli pi guyi** "house key" (key of house). For any other relation, use a **man** clause (lesson 12): **sola man gun mon bige pi yolan** "the road above the river". Two nouns side by side are only for gender (**tiwu futa**) and the set compounds in [../data/compounds.tsv](../data/compounds.tsv).

Giving something to someone: **verb + who gets it + what**: **neke to osa** "give me water". One catch: **tan** or **ben** right after a noun or pronoun belongs to it, so **to iko wan ben** is "I told that-him". To give "that" as the thing, use **tun**: **to iko ben tun wan.** "I told that to him."

Names always take **en** and keep their owner's spelling: **en mara**, **en lilith**. Say a name as close to its owner's pronunciation as you can. If you can't, use the adapted form, the nearest native sounds (Lilith → *lilifu*). Ask me to work out yours.

## Lesson 8: Being polite, and everyday phrases

- **upe** hello ("good"), **upe leso** good morning, **upe isi** goodbye ("go well")
- **lota** thanks, **sepi** sorry
- **nun** makes anything polite. It goes right after the particle (**so nun**, **tin nun**, **yo nun**), or first in a plain statement or greeting (**nun upe leso**): **so nun neke to osa.** "Could you please give me water?" Add more for more: **nun nun**.
- **No polite "you".** **me** is "you" to anyone, boss or child. Respect comes from **lanno**, titles and **nun**. In an emergency (**yo yo**) nobody expects **nun**.
- **Calling someone:** put the name or title first, with a comma, to get their attention, or last to soften: **en mara, tin obu.** / **tin obu, en mara.** "Mara, come."
- **Titles** go before the name, with no comma, and work when talking about someone too: **no tofo en mara** "Teacher Mara"; **no tofo en mara sin oyi** "Teacher Mara said".
- **lanno** is the polite title for anyone, like Mr/Ms or sir/madam: **lanno en olusegun**, or just **lanno, …** when you address someone. It also goes before a role or kin word: **lanno faba pi wede** "Uncle (father's sibling)", with respect. When it's clear who you mean, it works alone when talking about someone: **lanno sin oyi** "the boss said". **lanno** shows respect for the person named; it never means "you".
- **No "Mara, my teacher,".** To describe someone, put a title before the name (**no tofo en mara**), use a **man** clause, or say it in a new sentence.
- **Tone words at the end:** after a comma at the end of a sentence, **a** is "you know", **buni** is "okay?" (friendly, not a real question), **donon** is "it turned out", and **min** checks, "…, right?": **so pen isi, buni.** "Let's go, okay?" If two come together, **min** goes last. "Wasn't it?" when you half remember: **kon ka wan sin oyi bu, min.** "She said it, didn't she?" (**kon ka** "maybe", lesson 13)
- **mm** "I heard you", **huh?** "say again"

Being polite never means hinting. English softens a warning into "might want to check the stove"; here you say **yo nun** (warning, politely) and then the problem: **yo nun osa le obu. fon nun pen wupi isi.** "(Warning, politely) the water is coming. (Advice, politely) we need to go."

## Lesson 9: Numbers

Numbers are base 10, like English, but completely regular.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| **po** | **fi** | **sa** | **ka** | **da** | **te** | **ufo** | **oma** | **kefi** | **mape** |

Yes, 6 is **ufo**. Enjoy it. 6–9 have two syllables because the language ran out of short sounds.

**Place words:** **yawu** 10, **loki** 100, **munno** 1000, **tonen** million, **siwin** billion. Say the digit, then the place word, biggest first. A 1 before a place word is dropped, and places with a zero are skipped:

| Number | Said | Literally |
|---|---|---|
| 10 | **yawu** | ten |
| 12 | **yawu sa** | ten two |
| 15 | **yawu te** | ten five |
| 20 | **sa yawu** | two ten |
| 50 | **te yawu** | five ten |
| 99 | **mape yawu mape** | nine ten nine |
| 100 | **loki** | hundred |
| 105 | **loki te** | hundred five |
| 365 | **ka loki ufo yawu te** | three hundred six ten five |
| 2026 | **sa munno sa yawu ufo** | two thousand two ten six |
| 250 000 | **sa loki te yawu munno** | two hundred five ten thousand |

There are no teens, no "-ty", no irregular numbers at all. English makes you learn *eleven*, *twelve*, *fifteen* and *fifty* separately; here they fall out of the rule. **munno**, **tonen** and **siwin** take a whole number in front, as in the last row.

- **Counting things:** the thing, then the number: **totu sa** "two dogs", **dili oma** "seven days".
- **Labels:** the thing, then **pi**, then the number: **dili pi yawu da** "day 14", **dunan pi yawu** "month 10" (October). From 100 up, a label is read digit by digit.
- **Phone numbers, codes and years** are read digit by digit: **sa po sa ufo** for 2026 as a year. Phone numbers and codes go in groups of three from the right.
- **Decimals:** **mimi** is the point: **fi mimi te** 1.5. **guti** is minus.
- **Half** is **timon**; as a number, 0.5 is **po mimi te**. A third is **fi pi ka** "one of three".
- **Senary:** if you ever need a base-6 number, say **senali** first and read its digits.

**Amounts and comparing:**
- **"Than" is se:** **ke kudu se guyi ben** "bigger than that house". Most: **ke kudu se we** "biggest" (bigger than all). Less: **ke** + the opposite: **ke meli** "smaller". As … as: **fu**: **kudu fu bu** "as big as it".
- **About** a number: **fu** before it: **ewo fu ka yawu** "about 30 people".
- **From … to …:** **se te tun yawu** "from 5 to 10". At least: **konsin ka** "at least 3". At most: **mu ke se ka** "not more than 3". Enough: **pasu tonya** "enough food".
- **Units** are the international names, said first like any counted thing: **kilamita te** "5 km".

## Lesson 10: Time

- **Tense is optional.** Say when once, then stop marking it: **afe, to nawi pasu.** "Yesterday, I ate food." The future works the same way: **wuma, to obu.** "Tomorrow, I'll come."
- **eda** now, **mefa** today, **wuma** tomorrow, **afe** yesterday.
- **sin** done (**to sin nawi** "I've eaten"), **le** in progress, also "still" (**to le nawi** "I'm eating"), **buntu** about to (**to buntu kusa** "I'm about to leave").
- **mu sin** is "not yet": **to mu sin nawi.** "I haven't eaten yet."
- **sin and le don't combine.** "I was eating" is a past time word + **le**: **afe, to le nawi.**
- **Habits and intent:** **manni** before a verb is "usually" (**to manni isi** "I usually go"); with a past time word, "used to". **gan momu** is "on purpose", **mu gan momu** "by accident".
- **Before the verb, the order is:** small operator words, then **manni**, then **sin**/**le**/**buntu**, then the verb: **to fe manni le doku** "I'm also usually working".
- **Offsets from now:** **wo nelon fi** "after one week" = next week; **ya dunan fi** "before one month" = a month ago. Any time can be the starting point: **wuma wo dili fi** "the day after tomorrow".
- **dili** day, **nelon** week, **dunan** month (also "moon"), **fawu** year. Hours, minutes and seconds are borrowed: **awuwa**, **minitu**, **sekandu**.
- **Lengths of time are counts:** **awuwa ka** "three hours". **nin** + a length = "for": **nin dili oma** "for seven days". **gimu** is an occasion: **gimu sa** "twice".
- **Clock time works the way your culture does,** and both styles are always understood.
  - 12-hour: count the hour, then the minutes as two digits, then the part of the day if needed: **mon mape ka po pi yami** "at 9:30 at night", **mon yawu po sa** "at 10:02". On the hour, just the hour: **mon yawu sa** "at 12". Midnight is **yawu sa pi yami**.
  - Parts of the day: **leso** morning, **minfi** noon, **duwun** afternoon, **kegin** evening, **yami** night.
  - 24-hour: four digits, one at a time: **mon sa fi ka po** "at 21:30".
  - "Around" a time: **fu** before it: **mon fu minfi** "around noon".
  - Write the time the way your culture writes it.
- **Dates:** bigger unit first, with a comma between: the month by number, then the day: **dunan pi yawu, dili pi mape** "October 9". A year is read digit by digit: **fawu pi sa po sa ufo** "2026". On its own, **dili pi** + 1–7 is a weekday, Monday = 1: **dili pi ka** "Wednesday".
- **Age is time lived:** **to nume fawu ka yawu** "I have lived 30 years" = I'm 30.

## Lesson 11: Making words you don't have

This is the skill that makes a small vocabulary enough. Four markers turn an action into a noun:

| | | |
|---|---|---|
| **no** + verb | the one who does it | **no tofo** teacher, **no wungu** leader |
| **ge** + verb | the thing done or made | **ge iko** news ("what's told") |
| **du** + verb | the thing used for it | **du nawi** something to eat with |
| **pu** + verb | the place for it | **pu wopo** bedroom ("place for sleeping") |

- **The base can be a whole verb phrase:** **no isi se guyi** "traveller" ("one who goes from home"). It runs to the end of its phrase, so put a comma before a verb that follows it.
- **A person it's done to:** **ewo man gun tofo** student ("person who is taught").
- **Linking to a noun:** use **pi** or a verb: **pu pi mabo** an office ("place of paper"), **no obu se yaye** an alien ("one who comes from the sky").
- **Opposites:** **mu** + word is "not X" (**mu upe** "not good"); many words also have an opposite word (**yomo** "bad").
- **Ready-made compounds** are listed in [../data/compounds.tsv](../data/compounds.tsv), such as **du sunbu** "computer" ("thing for counting").
- **Borrowed words:** things the whole world names the same way are borrowed in their international form, without **en**: **foto** photo, **imeyilu** email, **intalunetu** internet, **dola** dollar, **kilamita** kilometre.
- **Computer words** are everyday words: search **ditun**, delete **nuton**, share **peton**, copy **gayen**, add **ginni**, download **dunu**, install **yaga**, turn on/off **benbi**/**tapi**.
- **Anything else: describe it.** Don't know "spider"? **noso meli pi bendo feli** "small animal of many legs". That isn't a workaround; it's how the language works.

## Lesson 12: Longer sentences

**Joining words:**
- **yen** and, **lu** or, **un** but. They join nouns, verbs, describing words or whole clauses.
- **To list nouns, use yen:** **mole yen wede** "mother and father". Two nouns side by side don't make a list.
- **lu** X **lu** Y = "either X or Y, not both": **lu osa lu pasu**.
- **don** if, **gi** because, **nin** while, **wo** after, **ya** before: each can start a clause.
- **wun** that (**to pume wun …** "I think that …")

**man clauses ("who", "which", "where"):**
- **man** + clause after a noun describes it. The noun fills the missing part: **ewo man obu** "the person who comes" (the noun does it); **mabo man me la yaga** "the papers you put" (it's done to the noun).
- **For a place or time, end the clause with the relation word:** **kemu man to nume mon** "the place where I live" (place that I live at).
- **No word closes a man clause; a comma does,** and nothing else in the phrase can come after it.

**Opening a sentence:**
- **A time or place phrase can open the sentence:** **mon minfi, …** "at noon, …".
- **To set a topic, start with pi:** **pi tale la, to mu lugo.** "As for the cars, I don't know."
- **An if/when clause can open it too:** **don me obu, to gun sogi.** "If you come, I'll be happy."
- **When several open a sentence:** a linker (**gi tan,** "so"), then time, place or topic, then the if/when clause, each followed by a comma; then the particle (lesson 4).
- **Only a person word at the very start is someone being called** (lesson 8). Anything else there is a time, place or topic.

**Put a comma where you'd pause:**
- after someone called at the start, and before someone called at the end;
- after anything that opens the sentence;
- after a subject that contains a clause or a derived phrase, before its verb: **ewo man obu, gun no tofo.** "The person who's coming is a teacher.";
- between who gets something and a long thing given;
- between clauses joined by **yen** or **un** when the first ends in a noun;
- before a tone word at the end (lesson 8);
- between month and day (**dunan pi yawu, dili pi mape**);
- after a **man** clause, to close it before more words.

In casual writing you can drop commas that are obvious.

**Whether a clause goes first or last changes what it attaches to.** At the start, it belongs to the main sentence: **nin leso, to sin miya ewo man sigo** "in the morning, I watched the person who came back". At the end, it belongs to the innermost clause before it: **to sin miya ewo man sigo nin leso** "I watched the person who came back in the morning". Full rule: [language.md](language.md), section 4.4.

**Quotes** follow a say-verb, and are full sentences with their own particle: **wan oyi "tin obu."** "She said, 'Come.'"

## Lesson 13: Can, must, maybe

**Can, must, should, may:**
- **lenu** can: **to lenu lonfe.** "I can swim."
- **keya** must, **wupi** need to, should: **pen wupi isi.** "We need to go."
- **efon** allow: **me gun efon nawi** "you may eat" (you are allowed to eat).
- **li** + verb = "in order to": **li bika** "to buy".

**How sure you are, in sixths.** **kon** + a number says the chance in 6 that the statement is true. It goes before the subject:

| | |
|---|---|
| **kon po** | impossible |
| **kon fi** | unlikely |
| **kon sa** | doubtful |
| **kon ka** | even odds, maybe |
| **kon da** | likely, probably |
| **kon te** | very likely |
| **kon ufo** | certain |
| **kon bo** | "I'm not sure how sure" |

**kon da wan obu** "4 in 6 she's coming" (she's probably coming). Half steps work: **kon te mimi te** (5.5 in 6). A plain statement means you believe it, so **kon** is optional. For an exact chance, use a number and **pasentu** "percent".

English "might", "probably" and "must be" (when it means *probably*) are all **kon**: "She must be home" = **kon te wan gun mon guyi**. "Must" meaning *have to* is **keya**.

**"If" and "if only":** **kon** after **don** says how likely the condition is: **don kon fi** "if (unlikely)". **don kon po** is "if (but it isn't so)": **don kon po to sin isi, to sin nagu wan.** "If I had gone, I would have seen her." There is no "would": the second clause is simply the result.

**How you know (optional extra):** **wanme** "I saw it", **inwun** "I was told", **wemen** "I worked it out". They go where **kon** goes: **inwun wan kusa.** "She left, I'm told." You can skip these until the rest feels easy.

## Lesson 14: Putting it together

A full sentence has a fixed order. You'll rarely use every part; only the verb is required.

1. someone you're calling, then a comma
2. openers: linker, time/place or **pi** topic, if/when clause, each with a comma
3. the particle (**min**, **so**, **tin** …), with **genso** or **ba** in front if needed
4. **nun**
5. **kon** and how you know
6. the subject
7. small operator words, **manni**, then **sin**/**le**/**buntu**
8. the verb (or verb + verb)
9. who gets it, then what
10. how (a describing word)
11. relation phrases (**mon**, **tun**, **se**, **gan**, **li** …)
12. a clause at the end (**gi**, **don**, **wun** …)
13. a comma, then a tone word (**a**, **buni**, **donon**, **min**)
14. a comma, then someone you're calling

For example: **en mara, afe, kon da wan fe sin obu tun pu pi mabo, a.** "Mara, yesterday she probably came to the office too, you know." That's calling, opener, **kon**, subject, **fe**, **sin**, verb, relation phrase and tone word, in order.

## Where to go next

- The three translated texts, [../texts/](../texts/), have word-by-word glosses. They were written with earlier versions of the language, so some words in them are out of date; check anything odd against the lexicon.
- The full reference: [language.md](language.md).
- Senary measurements and the senary calendar: [measurement.md](measurement.md).
- And conversation: start a session and say **upe**.

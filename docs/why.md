# Why is it like this?

Short answers to the questions people ask first. The full reasoning behind every decision is in the [design notes](rationale.md), and the [changelog](design-log.md) records when and why each one was made.

## Who made it?

Apupiwe is designed by its author together with Claude, an AI assistant, starting in October 2026. Claude does most of the research, drafting and testing. The author decides the questions that shape the language, and many of the rules below are the author's calls. Both are recorded, decision by decision, in the [design notes](rationale.md#11-what-the-project-is).

## Why is 6 "ufo", with two syllables, when 0 to 5 have one?

The language started out counting in sixes. A test of read-aloud ID numbers showed that six one-syllable digits can be made far harder to mishear than ten: 0.26% of digits came out wrong, against 2.3%. Then the author ruled that the world counts in tens and will keep doing so, so the language does too. The digits 0 to 5 kept their carefully chosen one-syllable forms. There was no room left for four more one-syllable words that stay just as distinct, so 6 to 9 have two (**ufo oma kefi mape**). Two syllables also survive a burst of noise better, the same reason radio operators say "niner" for nine. [More on numbers](rationale.md#7-numbers-time-measurement).

## Why does the describing word come after the noun?

Because the head of a phrase comes first, and word order alone shows who does what to whom, so a listener who misses a word still has the structure. Noun-then-adjective is also the more common order among the world's languages, as in **guyi kudu** "big house" (house big). [More on the grammar](rationale.md#4-grammar).

## Why is there no tense?

Many languages, among them Mandarin, Indonesian, Thai and Yoruba, mark time with words like "yesterday" and leave the verb alone. You say when something happened once, and the rest of the story follows. When it matters whether something is finished or still going on, the small words **sin** and **le** say so.

## Why one word for "he" and "she"?

Most of the world's languages don't mark gender in their pronouns, and those that do, like English, often have to guess or work around it. **wan** means "he" or "she". When gender matters, it can be said with **futa** "female" or **lowu** "male".

## Why are there two words for "we"?

**pen** is "we, including you" and **din** is "we, not including you". Many languages around the world make this distinction, and it is among the most stable features languages have. English "we" leaves the listener guessing whether they are included.

## Why do you say how sure you are in sixths?

Words like "probably" and "likely" mean very different things to different people. A number doesn't. **kon** plus a number from 0 to 6 gives seven steps, about as many as forecasters can reliably use, and every step but certainty is a one-syllable digit. It also suits a language whose digits once counted in sixes. [The confidence scale](language.md#61-clause-operators).

## Why does one word mean both "moon" and "month"?

Where the world's languages draw the lines between meanings decided where this one does. When more than half of the language families use one word for two meanings, it gets one word too. Moon and month share a word in about 70% of families, so here they are both **dunan**. [How word boundaries are drawn](rationale.md#54-where-boundaries-go-lump-or-split).

## Why only five vowels, and why does only n end a syllable?

The vowels a, e, i, o and u are the most common vowel system in the world, and they are spread as far apart as five vowels can be, which makes them hard to confuse. Syllables are a consonant and a vowel, with an optional **n** at the end, a shape almost anyone can say and that survives noise. Allowing only one ending consonant keeps words short without clusters like *str*. [More on the sounds](rationale.md#2-sounds).

## Why no capital letters and no question marks?

Writing marks only what the voice marks in speech. Names already have **en** in front of them, so capitals would carry nothing, and on a phone l, I and 1 are easy to confuse. A question starts with **min** or contains a question word, so the reader knows it's a question from the first word; a "?" at the end arrives too late to help. [More on writing](rationale.md#6-writing-researchnotes-human-test-01).

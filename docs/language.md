# The language: current reference

This is the current state. Reasons and history are in [design-log.md](design-log.md); evidence is in [../research/](../research/).

**Goal:** faithful transmission of thought, at a cost speakers will actually pay. It's a hypothetical *native* language with two surfaces, speech and sign, sharing one grammar.

## Sounds

- **Vowels:** a e i o u.
- **Consonants (15):** p b t d k g · m n · f v s z · l w y. Three places of articulation only (lips, tongue tip, back of tongue), because place is the cue noise destroys first.
- **Syllables:** (C)V(n). A vowel-only syllable may appear only at the start of a word. The only syllable-final consonant is n.
- **Stress:** the first syllable of every content word. Grammar words are unstressed.
- **No tones.** Pitch is free for intonation and emotion.
- **Syllable partition:** 58 syllables belong to grammar words, the rest to content words. A content word never contains a grammar syllable, so a grammar syllable heard is always a grammar word.
- Interjections outside the system: **mm** "heard you", **huh?** "say again".
- **Writing:** plain lowercase. Stress is fully predictable (first syllable of every content word; grammar words never), so normal writing needs no mark. Teaching examples capitalize the whole stressed syllable: **NIte**, **LANpu**, and for a vowel-first word just the vowel, **Ozi**.

## Signs

- **Location** carries most contrasts: face/head, chin/neck, chest, space in front, the other hand.
- **Handshapes:** flat, fist, index, spread, C-curve, O. Fine distinctions only near the face.
- **Movement:** straight, arc, circle, repeated, contact.
- **The face** carries speech act and confidence in parallel with the hands.
- Signed words are their own forms, often iconic; they share meanings and grammar with speech, not sounds. Mirror-image antonyms (come/go) are allowed only for large path reversals.

## Grammar

1. **Word shape tells category.** Grammar words have one syllable; content words two or more. Every meaning is a separate unchanging word: no endings, no agreement, no case.
2. **Order:** [speech act] subject verb object. Modifiers follow what they modify. A noun's own modifiers come before its "of" phrase (**Ozi ban Owu on FEbu** "rather little knowledge of sticks").
3. **Operators cover what follows them.** NOT, confidence, source, ONLY, AT.LEAST: at the start of a clause they cover the clause; before a word, that word.
4. **Speech act first.** Statements are unmarked. Others open with a particle. **ze ze** = emergency. A standalone **san.** marks the speaker's whole turn as not literal.
5. **Confidence is a number:** **mon** + digit = chance in 10 that the statement is true (**mon Ayon** = 7 in 10). Second digit for extremes (**mon ENge NEnon** = 95%). **mon wan** = "don't know how sure". Unmarked = ordinary belief. Sign: digit held on the non-dominant hand during the clause.
6. **Source is optional:** **kin** seen, **sun** told, **ven** inferred.
7. **Answers echo the verb**, there are no words for yes and no: "Aren't you coming?" → **Ime** "coming" / **na Ime** "not coming". Acknowledgment: **mm** = heard, an echo = understood, **zin** + verb = will do.
8. **Reference:**
   - Once a second third person is active, plain **lu** = the main character and **tan** (obviative) = anyone else. This is obligatory.
   - In reported speech or thought, **gan** = the person whose words are reported.
   - For crowded scenes, **ku** / **sin** = "this-side one" / "that-side one", with a point. In sign these are loci in space.
   - **pen** = anyone (generic); **vun** is only ever the listener.
   - No grammatical gender.
9. **"Is":** adjectives need **la** as a predicate (**Iwa la ZUvo** "the house is big"; **Iwa ZUvo** is only "the big house"). Without a subject, **la** = "there is".
10. **Verbs can modify nouns** directly: **NIte TAlan YUyu** "intruding alien".
11. **A prepositional phrase attaches to its clause's main verb**, never to a modifier.
12. **Time:** tense optional. Aspect particles **fa** done, **gi** ongoing, **yan** about to. Time words name an anchor plus an offset; no "move forward" metaphors. Roots: **zume** today, **ili** tomorrow, **zafo** yesterday.
13. **Compounds** are ordinary head-first phrases that stuck: **BOzen NOwi** "snake fire" = dragon.
14. **Numbers** are base 10, fully regular ("ten one" = 11), each two syllables.

## Grammar words

| Group | Words |
|---|---|
| Speech acts | question **yun** · request **fu** · instruct **gon** · advise **to** · intend **zin** · warn **ze** · not-literal **san** · exclaim **dun** |
| Operators | NOT **na** · which? **mi** · unspecified **wan** · confidence **mon** · seen **kin** · told **sun** · inferred **ven** · only **bin** · at least **wun** |
| Pronouns | I **e** · you **vun** · we incl. **nin** · we excl. **so** · he/she/it **lu** · obviative **tan** · logophoric **gan** · this-side **ku** · that-side **sin** · anyone **pen** |
| Determiners | plural **in** · this **va** · that **nun** · all **len** · some **vi** · some-not-all **kon** · none **bon** |
| Degree | more **u** · very **we** · rather **ban** |
| Aspect | done **fa** · ongoing **gi** · about to **yan** |
| Relations | of **on** · at **yi** · to **ke** · from **gen** · with **zo** · for **men** · before **fi** · after **tun** · like **wo** |
| Linkers | and **gu** · or **be** · but **fen** · if **ti** · because **win** · that (said that) **yo** · who/which **mu** · while **zan** |
| Copula | is **la** |

## Numbers

0 **donma** · 1 **tugun** · 2 **suki** · 3 **wumun** · 4 **tumin** · 5 **nenon** · 6 **livan** · 7 **ayon** · 8 **digun** · 9 **enge** · 10 **newen** · 100 **tonvu** · 1000 **senni**

## Vocabulary

[../data/lexicon.tsv](../data/lexicon.tsv): 266 roots plus numbers, with semantic field and frequency tier. Add words with `tools/words.py`; existing words never move.

## Open questions

- Only 4 free grammar syllables remain. Next grammar words need a plan (reshuffle content words, or two-syllable grammar words).
- Do confirmation and speech-act particles survive native use, or erode?
- The concept list and frequency tiers are judgment, not cross-linguistic frequency data.
- Sign vocabulary exists only as principles and a few examples.

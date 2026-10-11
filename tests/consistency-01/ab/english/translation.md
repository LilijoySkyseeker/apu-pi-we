# consistency-01 / ab / english: translation

Three lines per message: English, Apu Pi We, word-by-word gloss. Glosses in capitals are grammar words (names from `data/grammar.tsv`); `CONF 3` = **kon ka** "3 in 6".

```
A: ok so are we still doing the lake saturday or what
A: gi tan, min pen le isi tun nenwa mon dili pi ufo lu mu.
   BECAUSE THIS, Q WE.incl ONGOING go TO lake AT day OF 6 OR NOT
```
- "ok so" is one discourse opener here: the linker **gi tan**. "or what" is **lu mu** "or not", with the verb left out (4.5).

```
B: yes!! i've been looking forward to it all week
B: ba isi!! to le sefu sogi bu nin nelon minwe.
   EXCLAIM go!! I ONGOING wait happy IT DURING week whole
```
- "yes" is an echo of the verb (4.8); **ba** carries the "!!". "look forward to" = "wait happily for".

```
C: im in but not before 10 lol
C: to obu un mu ya 10. bubo.
   I come BUT NOT BEFORE 10. laugh
```
- "lol" is the fragment sentence **bubo** "(I) laugh".

```
A: 10 works. who's driving
A: 10 gun upe. ewo yu wungu tale.
   10 BE good. person WH guide car
```
- "drive" = **wungu tale** "guide the car".

```
B: i can but my car only fits 4 and jake might come
B: to lenu un tale pi to lenu dinyo na ewo 4, yen kon ka en jake obu.
   I can BUT car OF I can carry ONLY person 4, AND CONF 3 NAME jake come
```
- "fits 4" = "can carry only 4 people".

```
C: wait jake's coming?? since when
C: tin sefu. ba min en jake obu?? se muyi yu.
   INSTRUCT wait. EXCLAIM Q NAME jake come?? FROM time WH
```

```
B: he texted me last night, he said maybe
B: wan sin sege to ge tusi mon yami pi afe. wan oyi wun kon ka sun obu.
   HE/SHE DONE send I RESULT write AT night OF yesterday. HE/SHE say THAT.comp CONF 3 LOGOPHOR come
```
- "text" = send a **ge tusi** "written thing". "he said maybe" is spelled out as "he said that he might come".

```
A: lol jake's maybe means no
A: bubo. nin en jake oyi "kon ka", wan yofu wun sun mu obu.
   laugh. WHILE NAME jake say "CONF 3", HE/SHE mean THAT.comp LOGOPHOR NOT come
```
- There is no word for "no" (4.8), so "means no" = "means he isn't coming".

```
C: facts
C: feko feko.
   true true
```

```
B: ok so i'll drive. pick you guys up at 10:15?
B: gi tan, de to wungu tale. min to yidu me la mon 10:15?
   BECAUSE THIS, INTEND I guide car. Q I take YOU PL AT 10:15?
```

```
A: perfect
A: bi upe.
   VERY good
```

```
C: can you get me first, i'm on the way
C: so yidu to ya ewo eni la. to gun mon sola man me isi mon.
   REQUEST take I BEFORE person other PL. I BE AT road WHO.rel YOU go AT
```
- "first" = "before the other people". "on the way" = "on the road you take".

```
B: yeah sure
B: de yidu.
   INTEND take
```
- **de** + verb "will do" (4.8).

```
A: should we bring food or just get something there
A: pen wupi dinyo pasu lu na dunu musu bo mon kemu ben, yu.
   WE.incl need carry food OR ONLY get thing UNSPEC AT place THAT, WH
```
- A "which?" choice (**… lu … yu**). The comma keeps **yu** from reading as "which place".

```
C: let's stop at the taco place on 5th
C: so pen bamo mon pu pi tako mon sola pi 5.
   REQUEST WE.incl stop AT PLACE OF taco AT road OF 5
```
- **tako** is a new loan of the international "taco", adapted by 11. "5th" is a label, "road 5".

```
B: omg yes
B: ba bamo.
   EXCLAIM stop
```
- "omg" is **ba**; "yes" echoes **bamo**.

```
A: hold on my phone keeps saying my storage is full and it won't load the map
A: tin sefu. liga pi to le oyi wun du kuwi pi to gun kete, yen bu mu dunu mabo pi sola la.
   INSTRUCT wait. phone OF I ONGOING say THAT.comp TOOL keep OF I BE full, AND IT NOT get paper OF road PL
```
- "storage" = **du kuwi** "thing for keeping". I avoided **pu kuwi** because it is the "warehouse" compound. "load" = **dunu**, as in "download" (11). "map" = **mabo pi sola la** "paper of roads".

```
C: just delete some of your 4000 cat pics
C: tin na nuton kin pi foto 4000 pi me pi [X1].
   INSTRUCT ONLY remove PART OF photo 4000 OF YOU OF [X1]
```
- "just" = **na**. The second **pi** is meant to attach to **foto**, not **me** (see ambiguity 5).

```
A: never
A: mu mu nuton.
   NOT NOT remove
```
- An emphatic negative echo of the verb.

```
B: i'll send the address to the group, don't worry about it
B: de to sege apu pi kemu tun funti. tin mu nuta fu ben.
   INTEND I send word OF place TO group. INSTRUCT NOT fear LIKE THAT
```
- "address" = **apu pi kemu** "words of the place". "worry" = **nuta** "fear".

```
C: also sarah said she might meet us there around noon
C: yen, en sarah sin oyi wun kon ka sun fanmu gan pen mon kemu ben mon fu minfi.
   AND, NAME sarah DONE say THAT.comp CONF 3 LOGOPHOR gather WITH WE.incl AT place THAT AT LIKE noon
```
- The sentence-level "also" is the linker **yen**. **fe** would cover only the next phrase ("Sarah too").

```
A: nice. ok see you guys saturday
A: upe. gi tan, nagu me la mon dili pi ufo.
   good. BECAUSE THIS, see YOU PL AT day OF 6
```

## Placeholders

- [X1] = cat. There is no root, and the word isn't one shared internationally, so it can't be borrowed.

`check.py` flags only **tako** (a new loan, see ambiguity 8), the placeholder, speaker labels and English text.

## Rules I found ambiguous or had to guess about

1. **Chat interjections** ("ok", "lol", "omg"): section 2 lets any interjection pass with no grammar, but section 3 doesn't list such acronyms as text that passes through. I rendered them as **gi tan**, **bubo** and **ba**.
2. **"lol" position:** 7.2 says "other words used in this position are stance words too", which might license a final ", bubo". I used a separate fragment sentence instead.
3. **Choice questions:** 4.8 gives **… lu … yu** with no **min**, but the 10.3 example **min me momu bu lu ben yu** has both. A clause-final **yu** after a noun also collides with determiner **yu** "which X". I added a pause to separate them.
4. **"or what" / "or not":** it's unclear whether a bare **mu** with the predicate left out (**lu mu**) is allowed.
5. **What attaches where:** 4.4 says a relative clause attaches to "the nearest noun before it", and 5.2 says each **pi** attaches to the nearest noun. But the 5.1 template orders the head's pi phrase before its relative clause. I also had to guess whether a pronoun (**pi me**) counts as a "noun" for nearest-noun attachment.
6. **pi after a derived word** (**du kuwi pi to**): it's unclear whether **pi** modifies the derived noun or goes inside the verb base, which "runs to the end of its phrase".
7. **Derived word vs compound:** it's unclear whether a regular derivation may still be used in another sense when `compounds.tsv` fixes it (**pu kuwi** = warehouse, **du wuye** = screen).
8. **New loans:** 11 says a loan enters the lexicon "once it is common", so it's unclear whether an unlisted loan (**tako**) may be used. The adaptation table works from sounds, so I had to map the spelling "c" to **k** myself.
9. **Street names / ordinals:** there's no ordinal rule. It's unclear whether "5th" is a name (**en 5th**) or a label (**sola pi 5**).
10. **Digits vs number words in running text:** section 3 says digits pass through, but the examples spell numbers out. I used digits where the English did.
11. **A clock time as subject** ("10 works" → **10 gun upe**): it's not stated whether a bare time is a noun phrase.
12. **"might" → which kon number** (**ka** vs **sa**). It's also unclear whose confidence a **kon** inside a reported **wun** clause states.
13. **Iterative "keeps saying":** only **le** "ongoing, also still" is available. There is no repetition aspect.
14. **"never":** there's no word for it. I used emphatic **mu mu** + echo instead of **mon muyi fa** "at no time".
15. **"just"** (simply) vs **na** (only): there's no separate softener.
16. **Quoting a word** ("jake's maybe"): quotes are defined only for speech framed by a say-verb, so I rephrased with **oyi "kon ka"**.
17. **Sentence-level "also":** **fe** covers only the next phrase. Using **yen** as a sentence linker is my guess from the linker slot.
18. **Request with the subject left out:** 7.1 says **so** with "another subject" is a wish. It's unclear whether **so me …** stays a request, so I left the subject out.
19. **Discourse "wait / hold on":** it needs **tin** because a bare verb is a statement. Whether a casual imperative interjection gets this exemption isn't stated.
20. **Two relation phrases in slot 11** (place + time, **mon … mon …**): their order isn't specified.
21. **"there":** there's no place pro-form, so I used **kemu ben**.
22. **Pause after a wun clause** before a joining **yen**: the pause list doesn't cover this. I added one to show that **yen** joins the main clauses.
23. **sefu "wait" with a direct object** ("wait for it"): it's not stated whether **sefu** takes the awaited thing as a plain object.

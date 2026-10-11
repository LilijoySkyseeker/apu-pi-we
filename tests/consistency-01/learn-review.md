# learn.md against language.md

Checked 2026-10-10. Reference: `docs/language.md` (authoritative). Guide: `docs/learn.md`. Words were checked in `data/lexicon.tsv`, `data/grammar.tsv` and `data/compounds.tsv`. Line numbers are learn.md lines.

Counts: contradicts reference 14 · bad examples 6 · missing for beginners 30 · confusing order 8.

---

## 1. Contradicts the reference

**1.1 · L7 · word counts.** "About 450 root words, 64 little grammar words." The data has 540 lexicon entries (23 of them loans) and 61 grammar words in `grammar.tsv`; the reference also lists 13 two-syllable operators (sec. 13).
Fix: "About 540 root words and loans, about 60 one-syllable grammar words plus a dozen two-syllable ones, ten digits."

**1.2 · L16, L19 · tier sizes.** Tiers 5 and 4 hold 61 words, not 50; tier 3 holds 181, not 132.
Fix: "the 61 most common words (tiers 5 and 4)"; "the next 181 words (tier 3)".

**1.3 · L33 · wrong letter.** The letter column says **genso**; the row is the vowel *a* (as in *father*).
Fix: `| **a** | *father* | |`

**1.4 · L36 · wrong letter.** The letter column says **wanme**; the row is the vowel *o*.
Fix: `| **o** | *go*, but cut short | no "oo" glide at the end (Spanish *no*) |`

**1.5 · L39, L46 · "always hard, never *gem*"; "no exceptions".** Reference sec. 2 allows harmless variants in content words: k and g may sound like "ch" and "j" before i and e, a vowel plus n may become a nasal vowel, and consonants between vowels may soften. Grammar words keep their consonants.
Fix (L39 "Watch out"): "hard *g* is the standard; others may say a soft 'j' before i and e, which is harmless". Add after L46: "Speakers may soften some sounds (k/g before i/e, a vowel plus n said through the nose). These variants are never written and never change meaning. Grammar words always keep their consonants."

**1.6 · L54, L166 · "the first word says what kind of sentence it is".** By sec. 4.1, calling someone (slot 1) and openers (slot 2) come before the speech-act particle (slot 3), and **genso**/**ba** can come before another particle. Question-word questions have no **min** (sec. 4.8), so their first word isn't a question marker at all.
Fix L54: "**Questions don't need a rising voice.** **min** or a question word already marks them. Rising anyway is fine."
Fix L166: "A particle near the start, after any name you're calling or any opener such as **afe,**, says what kind of sentence it is."

**1.7 · L79 · "guyi kudu alone is … not a sentence".** By sec. 4.1/4.5, a fragment can stand as a sentence (**bi upe.** "very good."). The real point is that it doesn't mean "the house is big".
Fix: "**guyi kudu** is 'the big house', never 'the house is big'. This is the most common early mistake."

**1.8 · L81 · "Degree words are the one thing that goes before".** Every operator comes before what it covers (sec. 1.3, 6.2): **mu**, **na**, **fe**, **wi**, **o**, **konsin**, **nedin**. So do titles and **lanno** (sec. 5.1), the markers **no/ge/du/pu** (5.4) and relation words. The guide itself puts **mu** (L85) and relation words (L140) before.
Fix: "Describing *content* words come after. Small operator words come *before* what they cover: degree (**bi kudu** 'very big', **ke kudu** 'bigger'), **mu** 'not' (lesson 4) and a few others you'll meet later."

**1.9 · L132 · so = "please".** By sec. 7.1, **so** marks a request; "please" is **so nun** (sec. 10.2, and the guide's own L158). Minor.
Fix: `| **so** | request ("would you…") | **so neke to osa.** "Give me water?" (asking); "please" is **so nun** |`

**1.10 · L152 · names get adapted.** "Names are adapted to the sounds: Lilith becomes **en lilifu**." Sec. 11: a personal name keeps its owner's spelling, lowercase, even with letters the language lacks. The adapted form is only the spoken fallback (and the form of loans).
Fix: "Names always take **en** and keep their owner's spelling: **en mara**, **en lilith**. Say a name as close to its owner's pronunciation as you can. If you can't, use the adapted form, the nearest native sounds (Lilith → *lilifu*). Ask me to work out yours."

**1.11 · L208 · "Half is po mimi te".** The lexicon has a root for half, **timon** (size, tier 2; also used in the compound **doku pi timon** "part-time work"). **po mimi te** is the number 0.5.
Fix: "**Half** is **timon**; as a number, 0.5 is **po mimi te** (**mimi** is the point)."

**1.12 · L233 · "ewo gun tofo" student.** Sec. 5.4 gives **ewo man gun** + verb: **ewo man gun tofo**. Without **man**, **ewo gun tofo** is a sentence: "the person is taught".
Fix: "**A person it's done to:** **ewo man gun tofo** student ('person who is taught')."

**1.13 · L244 · "rule 15", "nearest clause".** language.md has no rule 15; clause attachment is sec. 4.4. The reference says the *innermost* clause before it.
Fix: "At the end, it belongs to the innermost clause before it: **to sin miya ewo man sigo nin leso** 'I watched the person who came back in the morning'. Full rule: [language.md](language.md), section 4.4."

**1.14 · L257 · measurement.md for "dates and the calendar".** Ordinary dates are in language.md sec. 8.3; measurement.md has the senary units and the senary calendar (sec. 8.3, 9.3). Minor.
Fix: "Senary measurements and the senary calendar: [measurement.md](measurement.md)."

## 2. Examples that break the rules or misuse words

**2.1 · L74 · ewo niba "a walking person".** Sec. 4.2: "after a subject, the next content word is the verb: **ewo niba** 'the person walks'. To describe a noun with a verb, use a relative clause: **ewo man niba**."
Fix: replace with "**ewo meli** 'a small person'". Then add: "Careful with action words: **ewo niba** is a sentence, 'the person walks'. 'A walking person' is **ewo man niba** (lesson 12)."

**2.2 · L113 · pen isi "let's go".** Without a particle a sentence is a statement (sec. 4.2, 7.1). "Let's" is **so pen** (sec. 12), and sec. 7.2 has **so pen isi, buni.**
Fix: "**so pen isi** 'let's go (you and I)' vs **din isi** 'we're going (without you)'."

**2.3 · L131, L243 · states without gun.** **genso to bi sogi** and **don me obu, to sogi** use a bare state word as the predicate. Lesson 3 (L76–79) and sec. 4.7 say a state takes **gun**.
Fix: **genso to gun bi sogi.** / **don me obu, to gun sogi.**
Note: the reference itself is ambiguous here. Sec. 4.2 makes the content word after a subject the verb (**ewo niba**), but 4.7/5.2 make **guyi kudu** a noun phrase, and the reference never says how a listener tells the two apart. The fix follows 4.7 and the guide's own lesson 3 until the reference settles it.

**2.4 · L142, L152, L160 (twice) · en mala.** In the lexicon **mala** means "heart", and the name rule (sec. 11) keeps the owner's spelling. The reference writes **en mara** throughout.
Fix: **guyi pi en mara**, **en mara** "Mara", **en mara, tin obu.**, **no tofo en mara**.

**2.5 · L161 · en tomasu.** That is the adapted form. The reference writes **o en tomas yidu bu** (sec. 6.2), which is the owner's spelling.
Fix: **o en tomas yidu bu** "*Tomas* took it".

**2.6 · L218 · mon mape ka yawu pi yami "at 9:30 at night".** Sec. 8.3 says 12-hour minutes are read as two digits: **mon mape ka po pi yami**. **ka yawu** is the quantity "thirty".
Fix: **mon mape ka po pi yami** "at 9:30 at night".

## 3. Missing things a beginner needs

**3.1 · Sentence template (sec. 4.1).** The template doesn't appear anywhere in the guide. Lesson: end of lesson 12, or a short lesson 13 "Putting it together". Text: the slot order in plain words: calling · opener (linker, time/place or **pi X** topic, if/when clause), comma · speech-act particle · **nun** · **kon**/source · subject · operators, **manni**, aspect · verb · recipient, thing · manner · relation phrases · trailing clause · comma, stance word · comma, calling. Add the rule for what goes before the verb (sec. 6.2): operators, then **manni**, then aspect, then the verb: **to fe manni le doku**.

**3.2 · Verb + verb and muge (sec. 4.2).** "I want to go" is everyday, and the guide never shows how to build it. Lesson 2. Text: "If the first verb takes an object (want, try, need, can, start, stop, like, help…), the second verb is that object: **to momu isi** 'I want to go', **walo alun** 'try to break'. Otherwise the second describes the first: **goyu pume** 'sit thinking'. **muge** + result + object = make it so (**muge upe tan** 'fix this'); **muge** + object + manner = do it so (**muge tan upe** 'do this well')."

**3.3 · Commands need tin (sec. 4.2).** An English speaker will say **obu!** for "come!", but by the reference that is a statement. Lesson 8, or lesson 4 if the particle table moves there (4.6). Text: "A command needs **tin** (or **so** to ask): **tin obu.** 'Come.' **obu.** on its own is a statement, '(someone) comes'. 'Don't' is **tin mu**."

**3.4 · Object or manner after the verb (sec. 4.2).** Lesson 3. Text: "After the verb, a content word is its object if the verb takes one, otherwise it describes how: **oyi fanse** 'say calmly'. After an object, it always describes how: **nawi pasu yobe**."

**3.5 · The other uses of gun (sec. 4.7).** Lesson 3 has only gun + state. Text: "**gun** + noun: **wan gun tiwu** 'she is a child'; + place: **wan gun mon guyi**; + action word = the result: **gun tapi** 'is closed'; after another verb, 'to be': **momu gun tiwu**; with no subject, 'there is': **gun musu feli** 'there are many things'."

**3.6 · Noun-phrase order and gender (sec. 5.1, 5.2).** Lesson 3. Text: "Order after the noun: describing words, number, **la**, this/that, **pi** phrase, **man** clause: **guyi kudu sa la tan** 'these two big houses'. Gender is just a describing word, used when it matters: **tiwu futa** 'daughter'."

**3.7 · Only pi links a noun to a noun (sec. 4.4, 5.2).** English speakers will build "house key" or "the road above the river" directly. Lesson 7. Text: "Inside a noun phrase only **pi** attaches to a noun. For any other relation, use a **man** clause: **sola man gun mon bige pi yolan** 'the road above the river'. Don't put two nouns side by side; that is only for gender and the set compounds in `compounds.tsv`."

**3.8 · The rest of the question words and answer forms (sec. 4.8).** "Where" and "when" are missing, and they are basic. Lesson 4. Text: "**mon kemu yu** where, **mon muyi yu** when, **X yu** which X, **wifu yu** how many/much, **pi ewo yu** whose. Choices: **min … lu …** 'either?', **… lu … yu** 'which?'. Tag: **…, min** '…, right?'. Indirect: **to mu lugo wun min …** 'I don't know whether …'. A **gun** question is answered **gun** / **mu gun**. Echoing the answer means 'understood'; **de** + verb means 'will do'."

**3.9 · Also fe, only na, even wi don (sec. 6.2).** **fe** is on the task list and the guide never teaches it; **na** is missing too. Lesson 4, next to **mu**. Text: "**fe** also, **na** only, **wi** even, each before what it covers: **to fe obu** 'I'm coming too', **na to** 'only me', **wi don** 'even if'. Doubling strengthens: **mu mu** 'definitely not'."

**3.10 · Tag min as a stance word (sec. 7.2).** L163 gives **a**/**buni**/**donon** but not **min** at the end, and not the order rule. Lesson 8. Text: "**…, min** checks: '…, right?'. If two end words come together, **min** goes last. 'Wasn't it?' when you half remember: **kon ka wan sin oyi bu, min.**"

**3.11 · Determiners bo, fa, kin; how to say "a/the" (sec. 5.2).** Lesson 6 has **we** and **in** but not **bo** "some(one/thing)", which is essential (**ewo bo** someone, **musu bo** something). Text: "**bo** unspecified: **ewo bo** 'someone', **musu bo** 'something'; **fa** none; **kin** some-not-all (**kin pi foto la** 'some of the photos'). When 'the' or 'a' matters, use **tan**, **ben**, **bo** or a number."

**3.12 · The real lookalike traps (sec. 13).** Lesson 6's table leaves out the worst ones. Lesson 6. Add rows: **to** = I (not "to"; "to" is **tun**); **a** = "you know" at the end (not "a"); **o** = focus; **gun** = is; **pen** = we incl.; **tin** = do it (command); **sun** = he/she in reported speech; **wi** = even (not "we"; "all" is **we**); **yen** = and; **tan** = this; **ben** = that; **kin** = some-not-all; **nun** = politely; **bo** = some(one).

**3.13 · Pronoun rules (sec. 10.3).** Lesson 5. Text: "A pronoun never means the subject of its own clause; for that use **nen**: **to miya nen**, never **to miya to**. **nen** after a noun or pronoun = 'in person': **wan nen obu** 'he came himself'. An unknown doer is **ewo bo**. **sun** is the speaker being quoted: **wan oyi wun sun kusa** 'she said she (herself) was leaving'."

**3.14 · The exception to leaving things out (sec. 4.5).** L117 teaches dropping words but not the one trap. Lesson 5. Text: "One exception: a clause starting with **gun** and no subject means 'there is'. To say 'it's money', keep the subject: **bu gun nimo**. With **gun** dropped too, a bare state is fine: **bi upe.** 'very good.'"

**3.15 · Calling someone and lanno, in full (sec. 10.1).** Lesson 8. L160 is missing these parts. Calling someone first gets their attention; calling them last softens. **lanno** alone works in reference when context shows who (**lanno sin oyi** "the boss said"). **lanno** marks respect and never means "you". There is no apposition ("Mara, my teacher"): use a title before the name, a **man** clause or a new sentence.

**3.16 · Where nun goes; no polite "you" (sec. 10.2).** Lesson 8. Text: "**nun** goes right after the particle (**so nun**, **tin nun**, **yo nun**), or first in a plain statement (**nun upe leso**). **me** is 'you' to anyone, boss or child; respect comes from **lanno**, titles and **nun**. In an emergency (**yo yo**) nobody expects **nun**."

**3.17 · Clock details (sec. 8.3).** Lesson 10. Text: "Both styles are always understood. In 12-hour time the minutes are two digits (**mon yawu po sa** 'at 10:02'); on the hour, just the hour (**mon yawu sa** 'at 12'). Midnight is **yawu sa pi yami**. 'Around' is **fu**: **mon fu minfi** 'around noon'."

**3.18 · Aspect and time details (sec. 8.1, 8.2).** Lesson 10. Text: "**mu sin** 'not yet'. **le** also means 'still'. **sin** and **le** don't combine; 'was doing' = a past time word + **le**. **manni** with a past time = 'used to'. Any time can be the anchor: **wuma wo dili fi** 'the day after tomorrow'. Lengths of time are counts: **awuwa ka** 'three hours'; **nin dili oma** 'for seven days'. **gimu sa** 'twice'."

**3.19 · Numbers: zero places, groups, labels (sec. 9.2, 5.2).** Lesson 9. Lesson 10 depends on labels (**dunan pi yawu**, **dili pi ka**) and L117 uses one, but the guide never teaches them. Text: "Zero places are skipped: 105 = **loki te**. A group word takes a whole number: 250 000 = **sa loki te yawu munno**. Noun + number counts (**dili oma** 'seven days'); noun + **pi** + number is a label (**dili pi yawu da** 'day 14'; above 99, read the label digit by digit). Phone numbers go in groups of three from the right."

**3.20 · Amounts and comparison (sec. 9.3).** Lesson 3 teaches **ke kudu** "bigger" but never "than". Lesson 9, or lesson 3 for the comparison. Text: "'Than' is **se**: **ke kudu se guyi ben** 'bigger than that house'; most = **ke … se we**; as … as = **fu** (**kudu fu bu**). About: **fu ka yawu** 'about 30'. From X to Y: **se X tun Y**. At least **konsin X**; enough **tonya**. Units come first like any counted noun: **kilamita te** '5 km'."

**3.21 · Confidence scale and "might/must" (sec. 6.1).** "Two things English doesn't have" (L250) leaves out part of the scale. Text: "**kon fi** unlikely, **kon sa** doubtful, **kon bo** 'not sure how sure'; half steps: **kon te mimi te** (5.5 in 6). English 'might', 'probably' and 'must be' (meaning *probably*) are all **kon**: 'She must be home' = **kon te wan gun mon guyi**. For an exact chance, use a number and **pasentu**."

**3.22 · Can, must, should, may; purpose; "if I had" (sec. 12).** These are everyday words, and the guide teaches none of them. Lesson 12. Text: "**lenu** can, **keya** must, **wupi** need to / should, **efon** allow (**me gun efon nawi** 'you may eat'). **li** + verb = 'in order to': **li bika** 'to buy'. **don kon po** = 'if (but it isn't so)': **don kon po to sin isi, to sin nagu wan** 'if I had gone, I'd have seen her'."

**3.23 · Relative clauses beyond the subject (sec. 5.3).** Lesson 12 (L242) shows only **ewo man obu**. Text: "The noun can be the object: **mabo man me la yaga** 'the papers you put'. For a place or time, end the clause with the relation word: **kemu man to nume mon** 'the place where I live'. No word closes the clause; a pause does, and nothing else in the phrase can follow it."

**3.24 · All the pause places (sec. 4.6).** L243 lists two. Lesson 12. Add: after someone called at the start and before someone called at the end; before a stance word; between a recipient and a long object; between **yen**/**un** clauses when the first ends in a noun; between calendar units (**dunan pi yawu, dili pi mape**); after a relative clause to close it. Replace "after a long subject" with the reference's wording: "after a subject that contains a clause or a phrasal derived word".

**3.25 · Openers: time/place phrase, and their order (sec. 4.3).** Lesson 12 (move **pi X** here from L162). Text: "A time or place phrase can open the sentence: **mon minfi, …** 'at noon, …'. When several open a sentence: linker (**gi tan,** 'so'), then time/place or topic, then the if/when clause, each followed by a comma; then the particle. Only a person word at the very start is someone being called."

**3.26 · Joining and quotes (sec. 4.4).** Lesson 12. Text: "To list nouns, use **yen** (**mole yen wede** 'mother and father'); two nouns side by side don't make a list. **lu X lu Y** = 'either X or Y, not both'. A quote follows a say-verb and is a full sentence with its own particle."

**3.27 · Writing (sec. 3).** The guide's questions end in "." (L86) and it never says why. Lesson 1. Text: "Write in lowercase; capitals mean nothing. A comma marks a pause and a full stop ends a sentence. **?** and **!** are allowed but add nothing, so questions often end in a full stop. Numbers are digits grouped in threes with a space (`1 250 000`), with `.` for the decimal point. Times, dates, unit symbols, handles and names stay as they are written."

**3.28 · More about making words (sec. 5.4).** Lesson 11. Text: "The base can be a whole verb phrase: **no isi se guyi** 'traveller'. It runs to the end of its phrase, so put a comma before a following verb. A noun base links with **pi** or a verb: **no obu se yaye** 'alien'. Opposites: **mu** + word (**mu upe** 'not good'), or the opposite root (**yomo** 'bad'). Ready-made compounds are in `compounds.tsv`."

**3.29 · Loans and computer words (sec. 11).** These are useful from day one ("email", "photo", "minute"). Lesson 11. Text: "Words the whole world shares are borrowed in their international form, without **en**: **foto**, **imeyilu**, **intalunetu**, **dola**, **kilamita**. Everything else is built: search **ditun**, delete **nuton**, share **peton**, copy **gayen**, computer **du sunbu**."

**3.30 · Speech-act details (sec. 7.1).** Lesson 8 table, L166–176. Add: **genso** and **ba** can come before another particle (**ba min** a surprised question; **genso min me lugo** "as if you'd know"). **de** covers the speaker or their group (**de din** "we will") and is never used for someone else's plan. Add a **genso** row so the table is complete.

## 4. Order that would confuse a beginner

**4.1 · L91–92 · gi yu, fu yu in lesson 4.** **gi** "because" first appears in lesson 12 and **fu** is never taught. Either gloss them in place ("**gi** = because, **fu** = like") or teach the relation words (lesson 7) before question words.

**4.2 · L117 · clock time and weekday in lesson 5.** **mon dili pi ufo** and **mon fi mape po po** use the weekday label and the 24-hour digit reading from lessons 9–10. "At seven" is also only right as 19:00. Use examples built from earlier lessons, for example **nagu me wuma** "see you tomorrow" and **mon guyi** "at home" as an answer. Or keep them, gloss "at 19:00" and add "(you'll learn times in lesson 10)".

**4.3 · L119–136 · lesson 6 table mixes a trap drill with new grammar.** Under "looks like English" it introduces **genso**, **so**, **sin**, **don**, **inwun**, **man** and **tason** ahead of their lessons, and **tason**, **genso** and **inwun** don't look like English words at all. Keep only true lookalikes (and add the ones in 3.12). Move **genso**/**so** to the particle table, **inwun** to the evidence section, and **sin** to lesson 10.

**4.4 · L159 · names rule comes after the opposite rule.** Lesson 7 (L152) teaches adapting names, and lesson 8 then says names keep their own spelling. Move L159 into lesson 7, replacing the adaptation sentence (see 1.10).

**4.5 · L161–162 · grammar parked in the politeness lesson.** **o**, **wi**, **manni**, **gan momu** and topic **pi X** have nothing to do with politeness. The heading "Stress in a word" also clashes with lesson 1, where stress means pitch on the first syllable. Move **o**/**wi** (with **fe**, **na**) to lesson 4 next to **mu**, under "Focus: **o**". Move **manni** and **gan momu** to lesson 10 and **pi X** to lesson 12.

**4.6 · L160, L166 · particles used before they are introduced.** Lesson 4 teaches **min** alone, lesson 6 adds **so**, and L160 uses **tin** before the particle table at L166. Move the particle table (and the rule that a command needs **tin**, 3.3) into lesson 4 right after **min**, so every particle is met once and early.

**4.7 · L213, L219 · commas used before the pause rules.** **afe, to nawi pasu** and **dunan pi yawu, dili pi mape** show commas whose rule only comes in lesson 12 (L243). Add one line to lesson 2: "A comma marks a pause: after anything that opens the sentence, and around a name you're calling. Lesson 12 has the full list."

**4.8 · L136, L246–251 · evidence and confidence are taught early and then called skippable.** **inwun** is taught in lesson 6, but L248 says to skip "how you know" at first. Meanwhile **kon** is the only way to say "maybe", "probably" or "must be" (sec. 6.1), and those are everyday words. Move **kon** (with 3.21) to right after lesson 8 as an ordinary lesson. Keep **wanme**/**inwun**/**wemen** as the optional extra and take **inwun** out of lesson 6.

# Consistency 01: rule inventory, old reference vs rewrite

Compared `/tmp/language-old.md` (old) with `docs/language.md` (new), with `docs/vocabulary-method.md` §5, `docs/drift.md` (Watch list) and `docs/rationale.md` as the places content was moved to. I went through the old doc statement by statement and skipped reasoning, evidence, history, dates and test references, as well as the nine deliberate changes in the brief. Data files (`data/*.tsv`) were not read, so a word that is only in the data counts as lost from the docs.

**Counts: LOST 13 · CHANGED (not deliberate) 11 · NEW CONTRADICTIONS 7**

---

## 1. LOST (in the old reference, now in none of the five docs)

1. **Question intonation.** Old, Sounds: "A question needs no rising tone, since the question word does that job; rising anyway is fine." New §2 only says "Pitch carries intonation and emotion only."
2. **No digits inside words.** Old, Writing: "Only letters, never digits, inside words." New §3 lists the letters and then lets digits pass through, but never says digits can't appear inside a word.
3. **Direction of digit grouping.** Old: digits are "grouped in threes **from the point** with a space". New §3 says only "grouped in threes with a space", so it no longer says how the digits after the point are grouped.
4. **Add-back triggers for punctuation.** Old: "Triggers to bring one back: `?`/`!` if readers or text-to-speech misplace intonation despite the opening word; `-` if established compounds get misread; `:` if a pause can't carry a construction." rationale.md §6 still says "Triggers to bring each back are in language.md", but they're no longer there or anywhere else.
5. **How loans enter the lexicon.** Old: "A loan goes into the lexicon (field 'loan') once it's common, and is checked against native words then; until that, an occasional near-collision is tolerated, as in every language."
6. **Conditions graded by confidence.** Old: "Adding **kon** + digit says how likely the speaker thinks it is … **don kon fi** is 'if (unlikely)'." New §12 keeps only **don kon po** (counterfactual). Neither the general mechanism nor **don kon fi** appears anywhere.
7. **`me` is never generic.** Old: "**go** = anyone (generic); **me** is only ever the listener." New §10.3 keeps **go** but drops the rule that **me** can't mean generic "you". (§10.2 "me is 'you' to anyone" is about politeness, not generic use.)
8. **A determiner right after a noun belongs to it.** Old: "A determiner right after a noun or pronoun still belongs to it, so after a recipient, use **tun** … (**to iko wan ben** would be 'I told that-him')." New §10.3 keeps only the instruction, and its wording is now garbled: "After a recipient, use **tun**", although the example puts **tun** *before* the recipient. The general attachment rule is gone.
9. **Weekday vs day of the month.** Old: "A day of the month is said with its month …; **dili pi** + 1–7 **alone** is a weekday." New §8.3 gives weekdays as **dili pi** + 1–7 and labels like **dili pi yawu da** "day 14" (§9.2), but no longer says that a bare **dili pi ka** is Wednesday and not "day 3".
10. **When to read digit by digit.** Old: digit reading is also used "whenever the exact digits matter more than the size." New §9.2 has only a closed list (identifiers, phone numbers, codes, years, 24-hour times).
11. **Broken-off speech.** Old: "a broken-off word just stops (there is no dash)." New §3 bans `-` only "in the language's own words" and says nothing about broken-off speech.
12. **apu disambiguated by a count.** Old: "A count keeps them apart: **apu fi** 'one word'." New §14 keeps only "**apu** 'word; language'".
13. **Words and examples that appear only in the old reference** (they may survive in `data/*.tsv`, which I didn't read):
    - account **ge sunbu**, spam **imeyilu bekin**, the loan **kontakutu**;
    - dragon **dinbu pi lumi**, meteorite **no dosi se yaye**;
    - learn **yesa** vs teach **tofo** kept as two roots;
    - the adapted-name examples (**lilifu**, **kulisutafalu**, **nayilobi**, **malukasu**).

**Not counted: add-back triggers that went missing too** (they're process, not language):
- script: "Add one if human tests show reading trouble, or when there's a way to work on visual design together" (rationale §6 says only "deferred");
- word building: "Add a marker only if a test shows one of these failing."

**Not counted: weakly carried.** "Every meaning is a separate word that never changes: no endings, no agreement, no case, no gender" is now only in the drift.md list ("no inflection") and the heading of rationale §4.2. The reference itself never says words don't inflect.

---

## 2. CHANGED, and not one of the deliberate changes

1. **ewo niba.** Old principle 2: a verb after a noun modifies it, **ewo niba** = "walking person". New §4.2: "After a subject, the next content word is the verb: **ewo niba** 'the person walks'"; describing a noun with a verb now needs **man**. This may be what the brief means by "'adjective'-like predication". If so, it's deliberate, but see contradiction 1.
2. **Person something is done to.** Old: **ewo gun** + verb (**ewo gun tofo** student). New §5.4: **ewo man gun** + verb (**ewo man gun tofo**). rationale §5.1 still says **ewo gun**.
3. **Places of articulation.** Old: "Only three places in the mouth (lips, tongue tip, back of tongue)". New §2 lists four, adding "tongue body (y)". rationale §2 still says three.
4. **tan vs ben for events.** Old: **tan** = "something nearer (just said, or here and now)". New §10.3: **tan** = "what I'm saying", **ben** = "what you said". Something the listener just said moves from **tan** to **ben**.
5. **More pause places.** Old said "That means three places" (fronted clause, subject containing a clause, recipient + long object). New §4.6 adds, beyond the deliberate phrasal-derived-word case:
   - between clauses joined by **yen**/**un** when the first ends in a noun;
   - after a relative clause, "to close it before more material" (also §5.3: "a pause closes it").
6. **Commas can be dropped.** Old: `,` goes "wherever the pause rule calls for a pause; clause attachment depends on it". New §4.6: "In casual writing, pauses that context makes obvious may be dropped." rationale §10 records this as decided ("Commas droppable in chat").
7. **Unknown doer.** Old example: **wo wan la yidu go** "after they take someone" uses **go** for "someone". New §4.4/§10.3: **wo wan la yidu ewo bo**, and "an unknown doer is **ewo bo**". This fixes an old inconsistency, but it is a change.
8. **Grouping when reading years and 24-hour times.** Old: digit reading "in groups of three from the right", which covered clock times and years. New §9.2: years and 24-hour times are read "as one four-digit group".
9. **muyi.** Old: "**muyi** is time as duration". New §8.2: "**muyi** time (a span or a point)". The old doc already used it as a point (**muyi yu** "what time"), so the new wording matches that usage, but the definition changed.
10. **wupi.** Old: "**wupi** 'need to'". New §12: "**wupi** 'need to, should' (for anyone)". The added "should" overlaps with advice, which is **fon**'s job.
11. **How passed-through symbols are read aloud.** Old: unit symbols and clock notation "are read aloud by their borrowed names". New §3: "read aloud as the speaker's culture reads them, or by their borrowed names". The deliberate pass-through change named only interjections and letter labels, not units.

---

## 3. NEW CONTRADICTIONS inside the new doc

1. **Noun + content word: verb or modifier?** §4.2 says "After a subject, the next content word is the verb: **ewo niba** 'the person walks'". But principle 2 ("Content words that describe a noun follow it"), §5.2 (**guyi kudu** "big house") and §4.7 ("**guyi kudu** is 'the big house'") say it's a modifier. §4.2 also says "Any content word can be a noun, a verb or a modifier", so nothing tells a listener which reading applies. **ewo niba** and **guyi kudu** have the same structure and get opposite readings.
2. **mesun comes after its noun.** §6.2 lists **mesun** as a phrase operator ("cover the word or phrase right after them") but places it "after its noun: **pu nume mesun**". That conflicts with principle 3 ("Operators come before what they cover") and §5.1 ("phrase operators before the whole phrase").
3. **Answering gun.** §4.8: "A question with **gun** is answered **gun** / **mu gun**." But §4.5 and §4.7 say a clause that starts with **gun** and has no subject means "there is". By those rules the answer **gun** reads as "there is".
4. **Pause after a relative clause vs end-clause attachment.** §5.3 and §4.6 say a pause closes a relative clause. §4.4 says a time, reason or condition clause at the end belongs "to the innermost clause before it", with no exception for a pause. In **to sin miya ewo man sigo, nin leso**, the rules disagree on whether **nin leso** attaches to the watching or to the coming back. Principle 4 ("nothing may follow a relative clause in its phrase") sits uneasily with "close it before more material".
5. **One particle per sentence?** §7.1 says "One particle covers one sentence" directly after saying "**genso** or **ba** may come before another particle" (**genso min me lugo**).
6. **Doubling "any word" vs repeated digits.** Principle 5: "Doubling widens or strengthens **any** word". Digit reading routinely repeats a digit (22:00 = **sa sa po po**, 1 100 = **fi fi po po**), where a doubled digit is just two digits.
7. **Wrong cross-reference.** §4.4: "In comparisons (9.3) and quantities (9.2) **se**, **tun** and **fu** belong to their number or adjective". The quantities (about, range, at least/most) are in §9.3; §9.2 is "Reading numbers".

---

## Not counted: stale pointers in the moved-to docs

- rationale §4.1 is headed "Six principles (language.md)". The new doc has seven, and principle 7 has no rationale row.
- rationale §11.4 places the watch list in "language.md, Open questions". It is now in drift.md.
- rationale §5.2 cites "How a new word is made (language.md)". It is now in vocabulary-method §5.
- rationale §4.5, §5.1 and §4.6 refer to "rule 8", "rule 11" and "rule 15". The new doc has no numbered rules.
- vocabulary-method §2 step 5 says "Loans only for names and brands", and §3.1 says "Numerals: unchanged (base 6)". Both conflict with language.md §11 and §9.
- drift.md item 6 mentions "a soft v between vowels", but /v/ is deleted.

## Coverage map (old → where it is now)

| Old | Now |
|---|---|
| Name, what it is, goal | new header; goal and north star in rationale §1.1 |
| Principles 1, 2, 4, 5, 6 | new §1 (2 changed: item C1); 6's prediction in drift Watch list |
| Principle 3 (operator scope) | deliberate change; new §6 |
| Sounds | new §2 (except L1, C3) |
| Writing | new §3 (except L2–L4, L11); script and lowercase reasons in rationale §6 |
| Words: types, digits, roles, verb+verb, muge, compounds, gender, focus | new §2, §4.2, §5.2, §6.2 |
| Built for drift, similar and opposite forms | rationale §3.1, §3.3 |
| Names and adapted form | new §11 (examples: L13) |
| Technical loans | new §11; "borrowing replaces describing, not native roots" in rationale §5.5 (except L5) |
| Word building | new §5.4 (C2; trigger not counted); clipping in vocabulary-method §5.4 and drift item 9 |
| How a new word is made | vocabulary-method §5 |
| Computers and text | new §11 (except L13) |
| Conditions, modality, choices, quantities, small words | new §4.4, §4.8, §6.2, §8.1, §9.3, §12 (except L6) |
| Politeness and routines | new §10.2; prediction in drift item 2; "routines optional" in rationale §4.7 |
| Direct address, titles, lanno | new §4.3, §10.1 |
| Stance | new §7.2; watch item in drift.md |
| Rules 1–5 (speech acts, confidence, source, answers, questions) | new §4.1, §4.8, §6.1, §7.1 |
| Rule 6, reference | new §10.3 (except L7, L8, C4, C7) |
| Rule 7, gun | new §4.5, §4.7 |
| Rule 8, prepositions and topic | new §4.3, §4.4, §8.2 |
| Rule 9, time and clock | new §8 (except L9, C9); reasons in rationale §7 and §10 |
| Rule 10, numbers | new §9 (except L10, C8) |
| Rules 11–15 | new §4.2, §4.4, §4.5, §4.6, §6.2, §9.3 (except L11, C5, C6); clause-closing trigger in rationale §4.6 |
| Grammar-word tables, two-syllable operators, slot swapping | new §13; vocabulary-method §5.7 |
| Numbers table, measurements | new §9.1, §9.3 |
| Vocabulary | new §14 (except L12); freeze in rationale §1.2 |
| Trust in sound choices | rationale §3.2, §11 |
| Open questions and watch list | drift.md Watch list; rationale §11 |

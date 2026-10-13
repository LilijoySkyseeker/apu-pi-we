# Questions for the author (from building the core grammar, phase 2)

Each one is a place where the reference is unclear, or an example needs a rule the reference doesn't state.
The grammar works around each as noted; nothing here was decided for you.

## 1. ibe with no subject: always "there is"? (4.7.7, 4.5.1)

4.7.7 says "there is" is **ibe** with no subject, and 4.5.1 lets any subject drop. So **ibe pasu** could be
"there's food" or "(they) have food". The UDHR uses the second: **ewo we … , yen ibe bawe kige** "(they) have
equal dignity".
- Options: (a) **ibe** with no subject is always "there is", as 4.7.6 says of **gun**; "(they) have" says
  its subject. (b) Both readings; context decides; 4.7.7 says "can be".
- Recommendation: (a). It mirrors **gun** and keeps a precise form (B3).
- Grammar now: one tree, "no subject + ibe"; it doesn't choose.

## 2. Is manner just fu "like" + a word? (4.2.4, 4.4.1, template slots 10-11)

Manner is **fu** + word (slot 10), and **fu** "like" is also a relation word (slot 11). Since any word can be
a thing, **fu yobe** is also "like speed". So there are two analyses of one meaning, and the slot order
can't be enforced: **nawi pasu mon guyi fu yobe** parses, with **fu yobe** as a relation phrase.
- Options: (a) manner is the relation word **fu** + a word: one rule, and slot 10 merges into slot 11.
  (b) keep slot 10 and say **fu** + quality after a relation phrase is wrong.
- Recommendation: (a). It's one rule fewer, and nothing seems to need the separate slot.
- Grammar now: both exist; they give the same structure, so the checker counts them as one reading.

## 3. Verb + verb: what do later phrases attach to? (4.2.6, 4.4.4)

In **momu isi mon guyi**, does **mon guyi** go with **isi** ("want [to go home]") or with **momu**?
- Options: (a) innermost, the second verb, like 4.4.4's rule for clauses. (b) the first verb.
- Recommendation: (a). It's consistent with 4.4.4 and with how speakers of most languages hear it.
- Grammar now: (b). The object verb takes only its own objects; manner and relation phrases go to the
  first verb. One reading either way, so this is easy to switch.

## 4. "whose" for things and plurals (5.3.7)

5.3.7 says **pi wan** inside the clause points back to the noun. **wan** is a person or animal (10.3.1).
What about a thing (**guyi man beya pi bu gun tapi** "the house whose door is closed") or a plural
(**pi wan la**)?
- Options: (a) **pi** + whichever pronoun fits the noun (**wan**, **bu**, **wan la**). (b) always **pi wan**.
- Recommendation: (a).
- Grammar now: only **pi wan**.

## 5. Names of more than one word (11.1)

**en xi jinping**: where does a name end? A name keeps its owner's spelling, so the next word may be a
name word or Apupiwe (**en tomas yidu bu**).
- Options: (a) a name of more than one word is followed by a pause or **kiyo**, like an open phrase.
  (b) each word takes **en**. (c) the words are joined in writing (**en xi-jinping**).
- Recommendation: (a). It reuses the closing rule speakers already know.
- Grammar now: a name is one word after **en**.

## 6. Examples made only of grammar words: utterances or citations? (6.1.2, 6.2.3, 7.1.1, 8.1.3, 12.1)

**tin mu** "don't", **de din** "we will", **mu sin** "not yet", **wi don** "even if", **kon bo**, **don kon fi**.
Some read as answers with the verb left out (4.5.1): "Will you come?" → **de din**. The grammar can't take
"the verb may be left out" in general: every sentence would gain readings.
- Options: (a) they are citations of word combinations, not utterances. (b) a narrow answer rule: a whole
  utterance may be operators, aspect or a particle with their subject and no verb (**mu sin.**,
  **de din.**, **tin mu.**).
- Recommendation: (b) for the answer-like ones (**tin mu**, **de din**, **mu sin**); (a) for **wi don**,
  **kon bo**, **don kon fi**, which only show what a word does.
- Grammar now: the checker treats all six as citations, checked against the word lists.

## 7. The pause between joined verbs (4.6.6, 4.4.7)

4.6.6 puts a pause between clauses joined by **yen**, **lu** or **un** when the first ends in a noun. Does
this hold for verbs joined without a second subject (4.4.7)? Without the pause, **to nawi pasu yen wopo**
reads **pasu yen wopo** as a list (or **pasu** as a manner word: "eat foodly and sleep"); with it,
**to nawi pasu, yen wopo** has one reading.
- Options: (a) yes, joined verbs too. (b) clauses only.
- Recommendation: (a), and say so in 4.6.6.
- Grammar now: (a).

## 8. Which pauses are optional? (4.6.5, 4.4.4, 5.3.5)

The grammar is strict: a pause goes only where something open must be closed, and in the fixed places 4.6
lists (after openers and calls, before stance, in dates, between joined clauses after a noun).
- 4.6.5 "between a recipient and a long object": "long" isn't defined. The grammar requires the pause
  when the recipient is open (has a relative clause) and allows none otherwise.
- **kiyo** closes relative clauses, phrasal derived words and topics (5.3.5, its gloss). Can it close a
  trailing clause, as a pause does (4.4.4)? The grammar says no.
- Options: (a) the pause in 4.6.5 is optional whenever the object is more than one word; **kiyo** closes
  anything a pause closes. (b) define "long" (say, contains a clause); keep **kiyo** as it is.
- Recommendation: (a): "kiyo is a spoken pause" is the simpler rule to learn.

## 9. gi + noun phrase (4.8.3, 4.3.6, 4.4.1, 13.1)

**gi yu** "why" and **gi tan** "so" use **gi** with a noun phrase, but **gi** is listed only as a linker
taking a clause, not among the relation words (4.4.1, 13.1).
- Options: (a) **gi** is also a relation word, "because of", in the 4.4.1 list. Then a sentence-initial
  **gi tan ,** is both the linker and an opening relation phrase: two analyses of one meaning, unless the
  linker entry goes. (b) **gi** + noun phrase only in the fixed **gi yu** and **gi tan**.
- Recommendation: (a), and drop **gi tan** as a separate linker: it is just "because of this".
- Grammar now: **gi** + noun phrase is a relation phrase at the end of a clause but can't open a sentence,
  so a sentence-initial **gi tan ,** is only the linker.

## 10. gun + action word + verb (12.2, 4.7.4, 4.2.6)

**me gun efon nawi** "you may eat" needs the undergoer's state (**gun efon** "be allowed", 4.7.4) to take a
verb as its object (4.2.6). Each rule is stated, but not the combination.
- Options: (a) state it: **gun** + an action word that takes an object can take a verb as that object.
  (b) another analysis of the example.
- Recommendation: (a).
- Grammar now: (a) (the function `GunVV`).

## 11. Two stance words (7.2.7)

"If two stance words occur, **min** comes last": one pause before both, or one before each?
- Grammar now: one before each (**…, a, min**). No example uses it.

## 12. dunan: time word or nature word? (8.2.1; data)

8.2.1 lists **dunan** "month" among the time roots; `lexicon.tsv` puts it in the field "nature" (moon). The
grammar needs time words for 4.4.1 (wo/ya after a time) and for dates (8.3.3).
- Options: (a) move **dunan** to field "time". (b) keep it; the grammar lists it as a time word itself.
- Grammar now: (b), in `tools/gf_lexicon.py` (TIME_EXTRA).

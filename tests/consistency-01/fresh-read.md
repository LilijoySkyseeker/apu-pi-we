# Fresh read of docs/language.md (consistency-01)

Sources read: `docs/language.md` (cited as L + line number) and `data/grammar.tsv`, `data/lexicon.tsv`, `data/compounds.tsv`, `data/numbers.tsv`. Nothing else in the repo was read.

## 1. Contradictions

1. **Names keep their owner's spelling, but the examples use adapted forms.** L67: "A personal name keeps its owner's spelling … **en denise**". Yet L65 has **o en tomasu** "*Tomas*", L66/L172/L173 have **en mala** "Mara", and L173 has **no wungu en danisu** "the manager, Denise". That's the same person spelled **en denise** in L67 and **en danisu** in L173. **mala** is also "heart" in lexicon.tsv (line 24). Under L67 these should be **en tomas**, **en mara** and **en denise**.
2. **Borrowing policy vs the computer vocabulary and the lexicon.** L74: devices are "borrowed in their international form … Borrowing replaces *describing*". L113: "Interfaces mostly reuse everyday words … rather than borrowing English computer terms", so computer = **du sunbu** (a description). The lexicon also has native roots for modern international things (car **tale**, phone **liga**, bus **ensu**, watch **aya**, card **mise**), while train **tuleyin**, bicycle **bayisikalu** and camera **kamela** are loans. No rule says which applies when.
3. **Whether words may still change.** L274: "All words were rebuilt once on 2026-10-08 … from here on, existing words don't move." L276: "existing words and rules may change when the design benefits." On the same topic, L106 says "Forms are never hand-picked", but L276 hand-swapped "I" to **to** and moved "rather" to **tason**, and L256 says a future need "takes a slot by swapping with the rarest holder".
4. **Where a relation phrase attaches.** Rule 8 (L213): "A prepositional phrase attaches to its clause's main verb, never to a modifier", and L216: "A bare place phrase after a noun attaches to the verb instead." These examples contradict it:
   - **pi** stays with a noun (L89).
   - **fu** + number attaches to a noun: **ewo fu ka yawu** "about 30 people" (L135).
   - **fu** attaches to an adjective: **kudu fu bu** (L129).
   - **se** X **tun** Y ranges (L136), and **se** in comparisons inside a noun phrase (L129).
   - Relation phrases sit inside **no/ge/du/pu** bases: **no isi se guyi** (L88), **no obu se yaye**, **no dosi se yaye** (L89), **no bina mon yami** (compounds.tsv). Once such a noun is an object (**to nagu no isi se guyi**), rule 8 sends **se guyi** to **nagu**.
5. **The scope rule for operators vs its own examples.** Principle 3 (L17): operators "cover the clause when they start it, or a single word when placed before it". But **o en tomasu yidu bu** (L65) and **wi tiwu la obu** "even the children came" (L142) put the operator at the start of the clause and mean only the subject. Principle 3 also puts HABITUAL at the clause start, while L220 says **manni** goes "before the verb" (**to manni isi**).
6. **"Anything that modifies a word follows it" (L16)** vs words that come before what they modify:
   - degree words: "**ke** … **bi** … **tason** … come before what they modify" (L229);
   - all the operators (L17);
   - **lanno** before a person word (L174–175);
   - titles before names (L173);
   - **o** (L65).

   In the same principle, "Nothing moves" vs time and place phrases that "may open the sentence" (L218), and time clauses that attach differently at the start and at the end (L236).
7. **Noun + noun.** Principle 2 (L16) gives noun after noun as a general modifying pattern (**tiwu futa**). L89 says bare noun + noun "is used only for gender … and for compounds listed in `data/compounds.tsv`".
8. **Stress and syllable count of grammar words.** L27: "grammar words are unstressed". L57: "Grammar words have one unstressed syllable … The one exception is the digits 0–5". L256 adds two-syllable operators that "work like grammar words" (**genso**, **wanme**, **buni** …), and L40 says "the first syllable of every word of two or more syllables is stressed". Are these operators stressed grammar words, or content words?
9. **The drift rule for grammar words is broken by the inventory.** L59: "Grammar words that can stand in the same slot start with different consonants." Same-slot pairs that share a consonant:
   - **wan** / **wun**, both right after a verb: **to lugo wan** "I know him" vs **to lugo wun …** "I know that …";
   - **man** / **mon**, both right after a noun: **ewo man …** vs **ewo mon …**;
   - **ben** / **bu**, side by side in the same slot in L199's own example: **bu lu ben**;
   - **tan** / **tun** / **to**, after a verb or noun: **iko ben tun wan** (L200);
   - **ya** / **yen** and **wo** / **wun**, all introducing clauses (L236, L227);
   - **un**, **o**, **en**, **a** and **in** start with a vowel, so no consonant keeps them apart.
10. **"Harmless variants never merge two words" (L28) vs voicing pairs among grammar words.** L28 lets "consonants between vowels … soften", and L59 predicts "middle consonants voicing". In connected speech that merges **pi**/**bi** (**guyi pi upe** "house of good" vs **guyi bi upe** "very good house"), **ke**/**ge** (both before a content word), **pu**/**bu** and **tin**/**din**. The doc never says that softening stops at word boundaries.
11. **Content words that start with a digit syllable.** L57: "No content word begins with one of those digit syllables." Lexicon: **polisu** (po-) and **kamela** (ka-). **kamela** even equals **ka me la** "three, you, plural". L59 predicts "a final n melting away", and L256 rejected **san** as "one final -n away from the digit **sa**". By that same reasoning, many content words begin with a digit syllable plus -n:
    - **sanwa**, **sanku**, **sandu**, **sanne**, **sanfi**;
    - **kanko**, **kanwi**, **kanga**;
    - **tenbe**, **tenmi**, **tengi**;
    - **danki**, **dandi**;
    - **finlu**, **finbi**, **finsa**.
12. **What tan and ben mean when they stand alone.**
    - L199: **ben** alone = "a thing that *isn't* the topic".
    - L200 and L258: **tan**/**ben** alone are "for an event, statement or situation". L258 mentions only that use.
    - L62 uses **tan** alone for a thing: **muge upe tan** "make this good, fix it".
    - L258 says only **tan** and **ben** stand alone, but **we** stands alone in **apu pi we** (L5) and **se we** "than all" (L129, L230).
13. **The pause rule lists three places; the doc uses many more.** L237: "That means three places". Commas also appear:
    - for address (L172) and stance (L181);
    - after topic phrases (L219) and scene-setting phrases (L218);
    - after linkers: **gi tan,** (L191), **un,** (L211);
    - after a speech-act particle: **yo nun, osa le obu** and **fon nun, pen wupi isi** (L160);
    - between month and day: **dunan pi yawu, dili pi mape** (L220);
    - after a fragment: **kon ka wo,** (L227).

    L172 also claims "a short noun phrase plus a pause at the start is someone being addressed". A fronted bare time word (**afe, …**, cf. L220 "**afe** …") is exactly that and isn't an address.
14. **End punctuation.** L50: "`?` and `!` are not needed … the opening word (**min**, **yo**, **ba**) already says it, and earlier." Wh-questions have no opening word (rule 5, L195: **me momu wun to oyi yu.**), and the tag **min** comes at the end (L181).
15. **nun is not a speech act, but it's filed as one.** L191: **nun** "changes no truth, confidence or speech act". The Grammar words table (L244) lists "polite **nun**" under Speech acts, and grammar.tsv gives POLITE class `act`. grammar.tsv also gives **a** (YOUKNOW) class `act`, while the doc treats it as a sentence-end stance word (L183, L246).
16. **What wan covers.** grammar.tsv gives **wan** as `HE/SHE/IT`. The doc (L197, L198, L247) says **wan** = he/she (people and animals) and **bu** = it.
17. **"Most".** L129: "Most = **se we** 'than all'". L230: "Most = **ke** … **se we**".
18. **"No new grammar words were needed" (L117)** vs the same section introducing **fe** and **wi** (L141–142). Both are one-syllable grammar words in grammar.tsv (`op`), listed under "Small words built from roots" although they aren't built from roots. **konsin** (L137) is also a new operator (L256).
19. **What muyi means.** lexicon.tsv: "time, duration". L139: "**muyi** is time as duration". But:
    - **mon muyi fa** "at no time" (L218) uses it as a point in time;
    - **muyi yu, moti.** "what time, again?" (L227) uses it as clock time;
    - compounds.tsv uses it for seasons and times of day: summer **muyi tikun**, winter, rainy.season, local.time.
20. **"Imposes no culture's conventions."** The goal (L9) says the language "carries any culture's conventions and imposes none", and the clock "follows the speaker's culture" (L220). Weekday numbering imposes ISO Monday = 1 (L220), and written numbers impose space grouping in threes and `.` as the point (L41). Indian grouping and comma-decimal cultures differ.
21. **Digit reading.** L223 says digit reading goes "in groups of three from the right" and applies to "clock times and years". L220 says 24-hour times are "four digits read one at a time" (**fi te ka po**), and reads the year as **sa po sa ufo**.
22. **Do place names take en?** L66: names take **en**, "always". L72: "London → **en landan**". L67 gives the established form **landan** without **en**, and L74 says loans take no article. Is an established adapted place name a name or a loan?
23. **Unit words.** L270: "Measurements use borrowed unit words", and L41: units are "read aloud by their borrowed names". lexicon.tsv has 20 native unit roots (`unit.length` **ago**, `unit.time` **nane**, `unit.mass` **fomi** …, several at tier 4). L274 counts them as "measurement units" without saying they're senary-only.
24. **Harmless variants are stated two ways.** L28: "k and g may sound like 'ch' and 'j' before i and e". L53: "k sounding like 'ch' before i".
25. **Places of articulation.** L25: "Only three places in the mouth (lips, tongue tip, back of tongue)". But **y** is palatal (front of the tongue body) and **f** is labiodental.
26. **The writing system vs examples.** L38: 18 letters, and L50: no `-`. Yet L31 has the interjection **huh?** (h isn't a letter), and L113 has brands "Wi-Fi" (capitals, hyphen). Pass-through may be meant, but it's never said for brands or interjections.
27. **Lexicon size and number data.** L274: "about 505 entries … plus numbers". lexicon.tsv has 539 rows, 518 of them non-number.
    - Digits 0–5 are only in numbers.tsv. Digits 6–9, the place words and the senary words are in both files.
    - **senali** is in the doc's numbers table (L268) and in lexicon.tsv, but not in numbers.tsv.

## 2. Gaps

1. **Noun + verb: phrase or clause?** Principle 2 (L16): **ewo niba** = "walking person". But subject + verb is also how a clause is built (**wan nagu yi**). Nothing says how a listener tells "the walking person" from "the person walks". The same problem hits **ewo gun tofo** = student (L87).
2. **Verb + content word: object or manner?** "Any content word can be a noun, verb or modifier" (L60), and "After a verb, a modifier describes the manner" (**oyi fanse**, L60). Then **nawi yobe** could be "eat fast" or "eat a fast thing". The only object-plus-manner order given is for **muge** (L62), and even **muge upe tan** can parse as **muge** + **upe tan** "this good thing". There's no general rule for V + object + manner.
3. **Order inside the noun phrase.** Nothing states the order of:
   - adjectives, verb modifiers and gender;
   - numbers (L225: noun + number);
   - determiners and **la**;
   - the **pi** phrase (L18 only says modifiers come before it) and relative clauses.

   Is **la** required for plurals, and is it used with numbers (**ewo fu ka yawu** has none)? Is there any definite or indefinite marking? The doc never says there are no articles.
4. **How relative clauses handle non-subject roles.** Every example relativizes the subject (**ewo man sigo**, **sola man gun …**). Nothing covers "the house that I saw" or "the person I gave it to": a gap, a resumptive **bu**/**wan**, or something else?
5. **Order of words before the verb.** Nothing gives the relative order of **mu**, **sin**, **le**, **buntu**, **manni**, **fe**, **wi**, **na**, **o**, modal verbs (**lenu**, **keya**), and **kon** or source words when they don't start the clause. Only **mu sin** "not yet" (L147) and **don kon po to sin isi** (L123) are shown. Can you say **sin mu**? What does it mean?
6. **Spatial relations (in, on, under, behind, into).** They're never stated. They're only implied by one example, **mon bige pi yolan** (L216): space nouns (**bese**, **deba**, **sinye**, **nebe**) + **pi**. Direction (to / into / onto with **tun**) isn't covered.
7. **Question words are incomplete.**
   - Rule 5 lists what, who, why, how.
   - "how many" (**wifu yu**) is only in L231, and "what time" (**muyi yu**) only in L227.
   - "which" is only in the table (L245), with no example of **X yu**.
   - "where", "when" and "whose" are missing.
   - L191 mentions "an **if**/**when** clause", but no word for "when" exists. **nin** is "while" and **wo** is "after".
8. **Tense, aspect and the future.**
   - Is **sin** past or completed? L123 calls it "a past event", L220 calls it "done".
   - What does **sin** mean with a future time word?
   - How do you say plain future ("it will rain tomorrow")? **buntu** is only "about to, soon", and **de** is only the speaker's intention.
   - **le** is both "ongoing" and "still" (L147), with no note on how the two relate.
9. **Duration.** "A duration is a count" (**awuwa ka**, L220; **nume fawu ka yawu**). But **nin dili oma** "for seven days" (L217) uses **nin**. When is **nin** needed?
10. **12-hour clock: where the hour ends.** L220: in 12-hour style "the hour and minutes are counted". So **yawu sa** is 12:00 or 10:02, and **sa yawu** is 2:10 or the quantity 20. Minutes under 10, "o'clock" and "quarter past" aren't covered.
11. **Large numbers.** The quantity rule (L222) doesn't cover a multi-digit multiplier of a group word (250 000 = ?), nor how groups chain (1 250 000). Zero inside numbers isn't covered. Digit reading "in groups of three" (L223) doesn't say how groups are marked in speech.
12. **Confidence scale.**
    - **kon sa** (2 in 6) is never named in L192. The list jumps from **fi** to **ka**, though the text says seven values.
    - The confidence of an unmarked statement ("ordinary belief", L15) isn't given as a number.
    - **bi** is "very" (table) and also "emphasis" (L192, L20). What does **bi** mean at the start of a clause, where principle 3 lets degree words stand?
13. **Words that are defined but never used.**
    - **in** "some", **kin** "some-not-all", **fa** "none" and **we** "all" (L248) have no usage rules and almost no examples.
    - **nedin** "almost" and **mesun** "each" (L256) have no placement and no example.
    - **sun** (L201) has no example and no position.
    - "at least" **konsin** (L137) has no position relative to the number.
    - "at most" **mu ke se X** isn't placed relative to the noun.
14. **Coordination.** L63 gives **yen** for nouns, and L227 has clauses after **yen**/**un**. Can **yen** join verbs (the compound frog **noso meli man lonfe yen niba** does) and adjectives? Can **lu** join clauses? What is shared when clauses are joined?
15. **Imperatives and bare verb-initial sentences.** Is **tin** obligatory for a command? With free subject dropping (rule 11), is **nagu me la mon dili pi ufo** (L227) a statement or a command?
16. **Two-syllable operators vs sequences of grammar words.** These are identical in sound to sequences of grammar words, and only stress separates them (L27, L40). Nothing covers this juncture:
    - **wanme** = **wan me**;
    - **inwun** = **in wun**;
    - **konsin** = **kon sin**;
    - **mesun** = **me sun**;
    - **buni** = **bu ni…**.
17. **How name adaptation maps vowels and glides.** L69 maps consonants only. Nothing covers schwa, ɪ, æ, ʌ or diphthongs, though the examples show ə/ʌ → a (**landan**, **kulisutafalu**). L70 never says when the glide is **y** and when it's **w**.
18. **Brands.** L74 says they are names, so do they take **en**? Are they written with their capitals and hyphens (L113 "Wi-Fi")?
19. **Reading notation aloud.**
    - Writing gives `5 km`, but speech reverses the order (**kilamita te**, L270). The reordering is only implied.
    - `°C` has no borrowed word in the lexicon (only **diguli** "degree").
    - How to read ISO dates (`2026-10-10`) and `%` aloud isn't stated.
20. **Answering yes/no questions.** "Answers echo the verb" (L194), but which answer applies when the verb is **gun**? A bare **gun** at the start means "there is" (L211). What if the question's verb was left out (rule 11)?
21. **Order of several elements at the edges of a sentence.** Before the particle, the order of address, linker, topic phrase and if-clause (L191) isn't given. At the end, the order of address and stance words (L172, L181), and whether several stance words can stack, isn't given.
22. **Doubling.** Does it apply outside the listed words (L19, L144)? What does **kudu kudu** or **upe upe** mean?
23. **Opposites.** L92: "opposites: **mu**", but the lexicon has paired antonym roots (**upe**/**yomo**, **kudu**/**meli**). When is **mu upe** right and when is **yomo**? Do they differ in meaning?
24. **Comparing amounts of a noun.** "more money" and "fewer people" aren't covered. "Less = more of the opposite" (L129) only works for adjectives.
25. **"Well", "anyway", "so" as openers.** L181 says they "use the linker position at the start", but only **gi tan** "so" is given.
26. **The coexistence principle is never defined.** It's referenced as "coexistence principle" (L67) and "coexistence tie-breaker" (L74). The goal statement (L9) may be it, but that's not said.
27. **The verb + verb list is open-ended.** L61: "want, try, need, must, can, start, stop, teach…". Which other verbs take a verb as object? **nagu**? **tana**? **yema**?
28. **Ambiguous English glosses in the data.** L274 says ambiguous glosses carry a second gloss, but these don't:
    - lexicon.tsv: "blow", "tie", "flat", "field", "rule", "change", "smell", "root", "shade";
    - compounds.tsv: "park" (green space or to park a car), "bat";
    - compounds.tsv "keyboard" **tinli la** = "the keys", which is the plain plural of **tinli**.
29. **Two frequency scales.** grammar.tsv `freq` (0.5–10) and lexicon.tsv `tier` (1–5) are never defined or related. So "Frequent meanings get the shortest words" (L15) and "Two-syllable operators … are rarer" (L256) can't be checked. **buni** is tier 4, while **yo** has freq 0.5.
30. **Senary-calendar compounds the doc never mentions.** compounds.tsv `the.count`, `body.time`, `local.time`, `leap.year` and lexicon **boyo** (36-day block) are unexplained apart from the L220 pointer to measurement.md.
31. **Where apposition goes.** Title + name is covered (L173). "Mara the teacher" (name first) isn't.
32. **Parts of the day.** No boundaries are given. Is 21:30 **yami** or **kegin** (L220: **mape ka yawu pi yami**)?

## 3. Stale or wrong examples

1. **min me momu bu lu ben yu.** "do you want it or that one?" (L199) uses both **min** and **yu**. By L131–132, **min … lu …** is a yes/no "either?" question and **… lu … yu.** asks which. The combination isn't defined.
2. **ewo gun tofo** = student (L87). By rule 7 (L205, L209: **gun** + verb = resulting state; **guyi gun kudu** is a clause) this is the sentence "the person is taught". As a noun phrase it would need **ewo man gun tofo**.
3. **en mala** "Mara" (L66, L172, L173 ×2), **o en tomasu** (L65) and **no wungu en danisu** (L173) use adapted forms against L67's owner's-spelling rule. **mala** is also the lexicon word "heart".
4. **lite pi po** "step zero" (L225): **lite** is "way, method" in lexicon.tsv. No word for "step" exists.
5. **lugo tason meli pi kima** "rather little knowledge of sticks" (L18): **kima** is "wood, the material". Stick is **kima netu** in compounds.tsv. **meli** is "small" (size), not "little" (amount; cf. **uyo** "few").
6. **upe isi** "go well" (L164): under head-first order (L16) a modifier follows its head, so "go well" is **isi upe**. As written it reads "good + going". **upe leso** "good morning" (L163) has the same problem unless greetings are an exception, which isn't stated.
7. **mon muyi fa** "at no time" (L218) and **muyi yu, moti.** "what time, again?" (L227) use **muyi** as a point in time. Data and L139 say duration only.
8. **muge upe tan** / **muge tan upe** (L62) use **tan** alone for a thing ("this"). Rule 6 (L200, L258) gives standalone **tan** only for events, statements and situations.
9. **yo nun, osa le obu. fon nun, pen wupi isi.** (L160): no rule puts a pause after particle + **nun**. Rule 1 (L191) shows **so nun …** with no comma, and the comma makes **yo nun** look like a fronted element.
10. **pi bayisikalu la, no kuwi guyi buntu yidu bu la.** "the caretaker will remove them" (L219):
    - **buntu** is "about to, soon" (lexicon), not "will";
    - **yidu** is "take", while the lexicon has **nuton** "remove, erase".
11. **tiwu lowu** "son" (compounds.tsv line 8): lexicon **lowu** is "man, adult male", so the compound reads "child adult-male". The gender modifier (L64) needs a plain "male" sense.
12. **apu fi** "one word" (L274) is offered as the way "a count keeps them apart". But **apu fi** is equally "one language". A count doesn't separate the two senses.
13. **wo wan la yidu go** "after they take someone" (L214): **go** is "anyone (generic)" (L202), not "someone".
14. **nin dili oma** "for seven days" (L217) marks duration with **nin**. L220 says "A duration is a count" (**awuwa ka**), with no **nin**.
15. **no wungu en danisu** "the manager, Denise" (L173): **wungu** is "lead, guide", and compounds.tsv glosses **no wungu** as "commander" (also L64). The English gloss also has a comma, while the rule says "with no comma".
16. **dunan pi yawu, dili pi mape** (L220) puts a comma inside a date. That isn't one of the pause places in L237.
17. **Name examples handle en inconsistently.**
    - L68 gives **malukasu** without **en**, while L72 gives **en lilifu** etc.
    - L67 gives **landan** without **en**, while L72 gives **en landan**.
18. **tuwu, not tuu** (L70) has no source word, so the learner can't see what was adapted.
19. **"there's a good idea: that one hits…"** (L18) is English-only, with no Apu Pi We form. It also uses `:`, which L50 removes from the writing system.
20. **fon [chips].** "maybe chips?" (L227) is a placeholder, not a usable sentence.
21. **2026 = sa munno sa yawu ufo** (L222) uses a year as the quantity-reading example. L223/L225 say years are read digit by digit (**sa po sa ufo**, L220). It's correct as a quantity but invites the wrong reading.
22. **to yonnu nen** "I held myself back" (L203): **yonnu** is "hold". "Back" isn't expressed.
23. **free.of.charge go mu unfu** "anyone not pay" (compounds.tsv) is a complete clause (subject + **mu** + verb). Listed as a compound modifier, it would read as a clause after a noun.

## 4. Not spec

These are reasoning, evidence, history, dates, test references, rejected alternatives or process notes, not statements of the current design.

1. L5: "chosen 2026-10-09".
2. L20 (principle 6): "People will always need to stress … would wear down the precision words instead (see drift.md) … Whether speakers actually keep them apart is a prediction, on the watch list, not a rule."
3. L25: "because place is the cue noise destroys first. /v/ and /z/ were deleted: both are rare worldwide … Removing /z/ cost almost nothing at a 3,000-root scale."
4. L27: "because listeners hear lengthening as the *end* of a word" (rationale).
5. L29: "Nearly all languages do this; Finnish and Hungarian … and Japanese (downstep) are clear examples."
6. L36: the whole paragraph: "Agreed with the user, 2026-10-09 … it costs nothing to type … A script designed from first principles is deferred. Add one if human tests show reading trouble…"
7. L39: "(found by the user's first reading check)".
8. L40: "(Docs used capitals for stress until 2026-10-09.)"
9. L42: "(first-principles review with the user, 2026-10-09)" and "(2026-10-10, for text and computer use)".
10. L50: "like Spanish's opening ¿ … The user's reading test showed end marks steer the voice, but too late … Triggers to bring one back: …"
11. L52: "it gets checked with the word tools" (process).
12. L65: "Added 2026-10-10 after multilanguage test 01 (10 of 11 languages flagged focus; the round trips lost Spanish contrastive *yo* …), the trigger this bullet used to set."
13. L66: "Many languages have such articles (Tagalog *si*, Māori *a*, Catalan *en*) … the way English copes with names like Rose or Baker."
14. L67: "(2026-10-10, coexistence principle)" and "This is how English, Spanish, Indonesian and most Latin-script languages coexist with foreign names."
15. L68: "`tools/names.py`, given the name in broad IPA: `python3 names.py maɹkəs`" (tool usage).
16. L73: the whole bullet: "In a blind test, a reader recovered 43 of 44 world names … (`tests/names-01/`)."
17. L74: "(user's ruling, 2026-10-09; reworded 2026-10-10 under the coexistence tie-breaker)" and "A loan goes into the lexicon (field "loan") once it's common, and is checked against native words then; until that, an occasional near-collision is tolerated" (process).
18. L78: "(A blind A/B test decoded these about as well as … 71/76 vs 69/76. They are kept because … see `tests/wordbuilding-ab-01/`.)"
19. L87: "In the test, **ge** for people was read as a thing … and the one-syllable grammar space is full, so there is no separate person marker."
20. L89: "The blind test showed that a bare noun + noun leaves the relation to guesswork".
21. L97: "Add a marker only if a test shows one of these failing."
22. L98: "as drift predicts. When that happens, assign the clipped form with the optimizer."
23. L100–109 ("How a new word is made") is coining method, not language description. In particular:
    - L102 (Wilkins 1668, Solresol rationale);
    - L104 "(government, prescription and orbit composed fine in the vocabulary tests)";
    - L105 "lumped in only 9.2% of families" and the vocabulary-method.md reference;
    - L106 (`tools/words.py add-content`, `--antonym`);
    - L107;
    - L109 (`tools/offensive.py`, Wiktionary, 34 languages).
24. L113: "Added 2026-10-10 (`tests/computer-vocab-01/`)", the "as Mandarin, Spanish, Russian and Arabic do" framing, and every cross-language parenthetical (Mandarin 开/关, 计算机, Arabic حاسوب, Spanish *cuenta*, "as in Mandarin and German").
25. compounds.tsv `literal` column: evidence parentheticals on computer, account and spam ("as Mandarin 计算机, Arabic حاسوب" etc.).
26. L117: "no new grammar words were needed (roadmap B2, 2026-10-08)".
27. L128: "English 'must' and 'may' each mean two different things; here they can't."
28. L139: "(**muyi** is time as duration; until 2026-10-10 it also counted occasions, an English leak: French *fois*/*temps* …)"
29. L143: "Blame and excuses need this everywhere; the phrase may clip if it gets frequent."
30. L153: "Evidence: `research/notes/politeness.md`."
31. L155: "It will wear down, as every dedicated politeness word does (drift.md)."
32. L156: "Address words can be replaced when they wear out; pronouns can't."
33. L159: "In accident reports the danger is a junior hinting … Speakers will still use questions and hedges to be polite …; that's on the watch list."
34. L160: "The pattern crews rated most effective".
35. L162: "(… people in many languages rarely thank in everyday requests)".
36. L170: the whole paragraph: "Added 2026-10-10 after multilanguage test 01: five of seven translators …"
37. L174: "like Hindi *-ji* or Japanese *-san*" and "It gives respect its own word, so speakers don't turn 'old' or 'leader' into titles (English *sir* … Latin *senior*) …"
38. L175: "(added 2026-10-10 after the retest; all three translators asked)", "(Hindi *chacha-ji*)" and "as Hindi uses *sir* about a superior".
39. L179: the whole paragraph: "Added 2026-10-10 after multilanguage test 01: all 11 languages flagged stance words …"
40. L181: "The tag '…, min' … was the first word in this position."
41. L185: "(Japanese っけ)".
42. L187: "They're seeded only so that **min**, **kon** and **ba** don't get pressed … Watch list: if a test shows that happening anyway, seed the job …"
43. L192: "Seven values match the about 7 bands forecasters can use … (Friedman et al. 2018)", "(History: sixths until 2026-10-09, tenths … then back to sixths …)" and "Most speakers will use a few favourite values; that's expected."
44. L197: "This is how obviation works where it is native: in Algonquian languages such as Cree …" and "(Until 2026-10-10 the rule was mechanical … `tests/economy-01-context/`.)"
45. L198: "(Until 2026-10-10 **bu** was the most recent thing mentioned … `tests/economy-01-context/`.)"
46. L199: "German divides the work the same way: *es* … *das* …"
47. L200: "Added after `tests/economy-01-context/`, where every 'that happened' … needed a noun."
48. L219: "This keeps the thing acted on in focus … (only 162 of 373 languages have one, WALS 107)" and "Added 2026-10-10 after multilanguage test 01."
49. L220:
    - "Added 2026-10-10: five of eleven languages flagged habitual aspect.";
    - "(the same word as 'moon', as in most language families)";
    - "(2026-10-10)" after the clock rule;
    - "Cultures number weekdays differently (Portuguese, Arabic, Hebrew and Vietnamese …), so the language follows the standard".
50. L221: "(user's ruling, 2026-10-09: base 10 is what the world uses; base 6 was the language's own system until then, see `docs/number-base.md`)" and "because the one-syllable space is full of grammar words (like English 'seven')".
51. L222: "so 15 and 50 can't be confused the way English *fifteen* and *fifty* are" (rationale).
52. L227: "Mandarin, Japanese and Korean … drop subjects and objects the same way." and "(Until 2026-10-10 a subject could drop only after **yen**/**un** … `tests/economy-01-context/`.)"
53. L234: "(tested on contract language, `tests/backtranslation-04-nesting/`)".
54. L238: "Add one (two syllables …) if a blind test shows attachment failing despite these rules."
55. L256:
    - "(grammar rebuild, 2026-10-10, `grammar-rebuild-spec.md`)";
    - "the two freed by the rebuild, **san** and **pa**, turned out to be unusable (both match the offensive filter …)";
    - "A future frequent need takes a slot by swapping with the rarest holder" (process).
56. L274:
    - "Add words with `tools/words.py`";
    - "as the Language Construction Kit advises";
    - "(CLICS4, lumped in 47 of 71 families, 50.2% family-balanced; 'tongue' = 'language' is only 9.5%)";
    - "All words were rebuilt once on 2026-10-08 under the drift rules; from here on, existing words don't move."
57. L276: the whole paragraph (freeze history, Ido/Esperanto, the user's learning status, "Changes still go through the tools and the design log", the **lon** → **to** history). The two open flaws it names belong with open questions, not in the spec.
58. L278–280: the whole "How much to trust the sound choices" section (Miller & Nicely 1955, model caveats).
59. L282–293: the whole "Open questions" section, including the watch list. L288 also carries "(2026-10-10)".
60. Scattered rationale clauses throughout the spec are reasoning, not rules, for example:
    - L16 "so a listener who loses one word can still tell who did what";
    - L57 "so a digit followed by a grammar word can never sound like a content word";
    - L58 "because context can't tell them apart";
    - L172 "A subject is only followed by a pause when it contains a clause, so …".

    Decide whether one-clause rationales stay or go.

## 5. Order and structure

1. **The core syntax comes after the topical sections.** "Rules the principles don't cover" (L189–238) holds speech acts, reference, copula, prepositions, time, numbers and clause attachment. It sits after Politeness, Address, Stance and Computers, which already depend on it by forward reference ("rule 8" at L89, "rule 11" at L215, "rule 6" at L258, "rule 7" at L227).
2. **No single sentence template.** The slots of a clause are scattered:
   - address (L172);
   - linker, topic and if-clause before the particle (L191, L218–219);
   - particle and **nun** (L191);
   - operators (L17);
   - subject, aspect and verb (L16, L220);
   - objects (L232, L200);
   - manner (L60);
   - relation phrases (L213);
   - trailing clauses (L236);
   - stance (L181) and end address (L172).

   One ordered template would answer most of the gaps in section 2.
3. **Noun-phrase rules are scattered** over:
   - principle 2 (L16) and principle 4 (L18);
   - gender (L64) and determiners (L258, after the table);
   - standalone **tan**/**ben** (L199–200);
   - noun + number (L225);
   - relative clauses (L216, L235);
   - "about" quantities (L135).
4. **Operators are scattered** over:
   - principle 3 (L17);
   - focus **o** (in the Words section, L65);
   - **fe**/**wi** (under "Small words built from roots", L141–142);
   - **konsin** (Quantities, L137);
   - **manni** (inside rule 9, L220);
   - source (rule 3) and confidence (rule 2);
   - the table (L245) and the two-syllable list (L256).
5. **Rule 9 (L220) is one 300-word paragraph** mixing:
   - tense and aspect, habitual;
   - anchor + offset time words;
   - the calendar, both clock styles and parts of the day;
   - written notation, dates, weekdays, durations and age;
   - the time roots, tacked on at the end.

   Aspect also appears at L123, L147 and L256, and **muyi**/**gimu** at L139.
6. **Numbers are in four places:**
   - Writing (L41);
   - Quantities (L134–139);
   - rule 10 (L221–226);
   - the Numbers tables (L260–270).

   "Part of a whole" **fi pi ka** is duplicated (L138, L224), and so is "fractions" with **mimi** (L138, L224). L224's "Fractions" heading actually covers decimals.
7. **Comparison is stated twice, inconsistently** (L129 and L230, see contradiction 17).
8. **nun is described four times:** principle 5/6 (L19–20), Politeness (L155), rule 1 (L191) and the table (L244).
9. **Stress is stated three times** (L27, L40, L57). Harmless variants are stated twice (L28, L53), with different coverage.
10. **Names and loans are spread out:** Words (L66–74), "How a new word is made" (L108) and Writing (L39). The **apu** word/language note appears at L105 and L274. Clipping appears at L98 and L107.
11. **Questions are scattered:**
    - intonation (L30) and `?` (L50);
    - rule 5 (L195);
    - choices (L131–133);
    - "whether" (L148);
    - tags (L181, L191);
    - "how much" (L231);
    - "what time" (L227).
12. **Pause and comma rules are scattered:**
    - the Writing table (L46) points to "the pause rule" in rule 15 (L237);
    - the other pause uses are at L172, L181 and L218–219.
13. **Writing comes too early.** The Writing section (L34–53) sits before Words and grammar but relies on concepts introduced later: the name article **en**, the pause rule, **min**/**yo**/**ba**, and compounds. The Sounds bullet "Writing: see the Writing section below" (L32) points at the very next section and can go.
14. **"Conditions, modality, choices and quantities" (L115–149) is a grab bag.** Its "Small words built from roots" subsection mixes grammar words (**fe**, **wi**) with phrases ("on purpose", "let's", "don't", "whether", purpose **li**).
15. **The Grammar words table (L242–254) is incomplete or misfiled:**
    - the derivational markers **no**/**ge**/**du**/**pu** (in grammar.tsv) are missing;
    - **nin** is listed only as a linker, though it's a preposition at L217;
    - **ya**/**wo** are listed only as relations, though they're clause linkers at L236;
    - **tason** is missing from Degree, though rule 13 lists it;
    - **nun** is filed under Speech acts.
16. **Data files are split differently from the doc.**
    - Two-syllable operators (**genso**, **wanme**, **buni**, **buntu**, **manni** …) live in lexicon.tsv under fields "abstract"/"time", not in grammar.tsv.
    - Number words are duplicated across numbers.tsv and lexicon.tsv (21 forms), with digits 0–5 only in numbers.tsv.
17. **The two lanno bullets (L174, L175) should be one.** L175 extends L174's "before a name, or alone when speaking to someone".
18. **The stance section says "Three seed words" (L182) but has four bullets,** and the third is explicitly not a word.
19. **"How a new word is made" (L100–109)** is a procedure for the designer, sitting inside the language description. The "Computers and text" section (L111–113) is a vocabulary list with evidence. It belongs with Vocabulary/compounds and overlaps the loan policy at L74.
20. **The doubling cases are scattered.** Principle 5 (L19) lists them, but **nen nen** "each other" (L144) and **nun nun nun** (L155) are elsewhere.
21. **Rule 1 (L191) packs six rules into one paragraph:**
    - the particle list;
    - **nun** placement;
    - what may precede the particle;
    - the end tag;
    - **genso**/**ba** stacking;
    - the semantics of **de**.
22. **Formatting slips.**
    - Rule 7's heading reads `**"Is" (gun),**` (L204), with a stray trailing comma.
    - A blank line splits rule 14 from rule 15 (L233).
    - L50's paragraph is indented two spaces after the table.
23. **The Vocabulary section (L274–276) mixes things.** It combines a data description, lexical-semantics evidence, history and the freeze policy. Only the first sentence and the gloss convention are spec.
24. **The "Six principles" contain rules the later sections don't restate** (causative order in principle 4, the ban on anything following a relative clause in principle 4). The rules section heading says it covers "the cases the principles don't cover", so the reader has to merge the two lists.

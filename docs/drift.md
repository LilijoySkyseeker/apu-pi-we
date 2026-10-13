# Planning for drift

A native language changes. The author asked (2026-10-08) to weigh this heavily: predict where the language will drift and design for it now. Evidence is in `research/notes/stress-and-sound-change.md`, `grammaticalization-and-drift.md` and `designed-languages-going-native.md`.

## The main finding

Most of the machinery for faithful transmission sits in the one-syllable grammar words: speech acts, NOT, confidence, source and reference. That is the layer that changes fastest. Prepositions and conjunctions are replaced fastest, though pronouns are among the slowest (Pagel et al. 2007), frequent words lose sounds fastest (Bybee 2002), and grammar changes on average about five times faster than basic vocabulary (Greenhill et al. 2017; some grammar, e.g. clusivity, is very stable). *(Corrected 2026-10-12 after the fact-check, C29: was "function words are replaced fastest". The one consonant rule still covers all one-syllable words; only its stated reason for pronoun-like words is weaker.)* The two-syllable content words are the slow, stable core.

So drift-proofing is mostly about the grammar words.

**Status:** every pre-emption below was adopted on 2026-10-08, and the word lists were rebuilt to enforce them (`tools/build.py`).

## Predicted drift, most likely and most harmful first

| # | Drift | Evidence | Pre-emption |
|---|---|---|---|
| 1 | **Top confidence values become emphasis.** "certain" (**kon ufo**; originally "ga LUbu") comes to mean "really". | *literally*, *surely*, *no doubt* all bleached this way | Give emphasis its own outlet (**ba**, **bi**, doubling) and teach it as *the* way to emphasise. Keep **kon** optional, so saying it carries information. Two digits keep a precise top end after "10" bleaches. |
| 2 | **Politeness takes over hedges, questions and "advise".** | Hedges read as tact (Bonnefon & Villejoubert 2006); politeness inflation and T/V pronoun shifts | A dedicated politeness particle with no truth meaning, so the wear lands on it and not on **kon** or the speech acts. It will wear down too (English *please*; polite pronouns inflate and get replaced, irregularly; *usted* and *Sie* have held 300–400 years). *(Corrected 2026-10-12 after the fact-check, C32: cut "cycle every 150–300 years", which had no source.)* Likely renewal: doubling it, **nun nun** becoming the ordinary polite form. |
| 3 | **Unstressed grammar words reduce and merge.** Vowels blur; words fuse onto neighbours. | Esperanto native speakers reduced grammar-word vowels, but only ~5% of the time, in 8 children (Bergen 2001; *corrected 2026-10-12 after the fact-check, C17*); frequent words reduce first (Bybee 2002); the morphological cycle | Grammar words that can occupy the same slot must differ by consonant, not only by vowel. Fusion is then harmless: it just turns particles into regular affixes. |
| 4 | **The obligatory wan/yi (obviation) rule gets simplified.** "Importance" can't be predicted by a learner, so children replace it. | Learners regularize what they can't predict (Hudson Kam & Newport 2005); natives drop redundant required marking | Adopted 2026-10-08: a mechanical most-recent-subject rule. **Superseded 2026-10-10:** **wan**/**yi** follow the topic, loosely like Algonquian obviation (partly topic-driven, partly obligatory grammar; *corrected 2026-10-12 after the fact-check, C25: was "as Algonquian obviation does natively"*). Hudson Kam & Newport is about random input, and topic-based reference isn't random; children everywhere learn it (design log). |
| 5 | **Later syllables of content words erode.** Initial stress was followed by loss of later vowels in Germanic, Old Irish, Latvian and Estonian. Finnish and Czech kept theirs, perhaps thanks to vowel-length contrasts, which this language lacks; but Estonian and Latvian had length and still eroded, so that is a hypothesis, not a guarantee *(corrected 2026-10-12 after the fact-check, C7)*. | stress-and-sound-change notes | Score words against their likely *future* pronunciations: no pair may differ only in a later vowel, or only in the voicing of a middle consonant. 7 current pairs fail this. |
| 6 | **Predictable sound changes:** k/g → ch/j before i/e; vowel + n → nasal vowel; middle consonants voice; w → v (24 cases vs 9 the other way in a rough count); z devoices. | Index Diachronica counts; Gurevich 2004 (92% of 230 lenitions merged nothing; covers the middle consonants only, since palatalisation and nasal vowels aren't lenitions: those rest on our collision check, *scope added 2026-10-12 after the fact-check, C8*) | Declare harmless variants in advance ("ch" before i, nasal vowels, soft middle consonants). Protect only the contrasts that keep words apart. |
| 7 | **New grammar grows from content words:** "say" → quotative or hearsay, "go" → future, **sin** done → past, **tan** this → "the". | Grammaticalization pathways (Heine & Kuteva) | Mostly let it happen; none of it harms fidelity. The language already has hearsay (**inwun**), about-to (**buntu**) and done (**sin**), so there's less pressure to invent them. |
| 8 | **Negation wears down and gets reinforced** (Jespersen's cycle). | Common in Romance and Germanic | Sanction **mu mu** as the reinforcement in advance, so renewal stays inside the system. |
| 9 | **Frequent compounds get shortened** (**no wungu** → **wungu** in context, or first syllables). | Zipf's law of abbreviation; omnibus → *bus*, Mandarin 北京大学 → 北大 | Welcome it, and don't pre-empt it: speakers shorten from the words they already say, so a designed replacement form wouldn't be adopted. Frequent concepts get roots in the seed instead (author, 2026-10-13). |
| 10 | **Numbers get clipped** in running speech. | Users clip frequent long words | Pre-empted twice: first by making short forms the first syllable of long forms, then (base 6) by making every digit one syllable with no long form at all. |

## What can't be pre-empted

- **Dialects.** One language for all of Earth splits regionally, as Latin did. Schools can stop changes people notice (Iceland's 1940s–60s campaign ended the *flámæli* vowel shift among children), but not syntax (Iceland's "New Impersonal" spreads anyway). *(2026-10-12, C47: "merger" loosened to "vowel shift".)*
- **Sounds drift toward the founders' first languages** (Hebrew's "Founder Principle"). For a world language, the founders are everyone, so sounds many of them lack are at risk (our inference; Israeli Hebrew kept /v/ and /z/ because its founders had them). The least common two of the candidates, **v** (27% of languages) and **z** (30%, PHOIBLE), were deleted on 2026-10-08: uncommon, not rare. *(Corrected 2026-10-12 after the fact-check, C3, C5: was "rare sounds are at risk", "the rarest two".)*
- **Usage overrides the designer's word list.** Toki Pona's community dictionary (*ku*, 2021) took in words by poll, including some the author had dropped or listed as synonyms. *(2026-10-12, C48: was "reinstated words the author had dropped".)*

## What's already drift-resistant

Creoles mostly (not uniformly) have what this design already has: SVO order, little inflection, preverbal aspect particles, optional tense, analytic possession ("grandfather of me"); some have tone or morphology (Saramaccan), and part of the creole profile comes from substrate languages (Blasi, Michaelis & Haspelmath 2017). Native Esperanto speakers lost some redundant marking, mostly by transfer from their other native language (Bergen 2001).

Inclusive/exclusive "we" is among the most stable distinctions (Greenhill et al. 2017).

*(Corrected 2026-10-12 after the fact-check, C14, C15. Cut as wrong: "Native Esperanto, Modern Hebrew and the creoles all moved toward [SVO, no inflection, no tone, particles for aspect, optional tense, analytic possession]": Modern Hebrew is SVO but heavily inflected with obligatory tense, and native Esperanto speakers were no more SVO than L2 speakers. Cut: "Fixed word order is among the most stable features (Dediu & Cysouw 2013)": the paper found word-order type (which order) stable, not fixed vs free order.)*

## Watch list

Moved here from the reference (2026-10-10). These are predictions, not rules; act only if use or a test shows them.

- **kon** collapsing to a few favourite values, or being used for emphasis.
- Questions, hedges and low **kon** used for politeness, blurring what they carry.
- **min**, **kon** or **ba** pressed into stance jobs despite the stance words.
- **wan**, **yi** and **bu** follow the topic. Bring back a mechanical rule if a blind test shows listeners losing track where one would have helped.
- The aspect words **le** and **buntu** going unused.
- Whether confirmation and speech-act particles survive native use or wear away.
- Grammar words that share a first consonant across different positions (**wan**/**wun**, **man**/**mon**, **to**/**tun**/**tan**) and voicing pairs (**pi**/**bi**, **ke**/**ge**) merging in fast speech. Position separates them now; act if a listening test shows confusion.

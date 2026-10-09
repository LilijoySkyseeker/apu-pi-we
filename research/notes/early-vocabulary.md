# Early vocabulary across languages as an ordering signal

Written 2026-10-08 for step 1 of `docs/vocabulary-plan.md`. Labels: **[sourced]** means I read it in the cited source. **[inferred]** is my reasoning. **UNVERIFIED** means I found it only in a secondary source or recalled it.

**Bottom line.** Children's *very first* words are strikingly similar across languages. They cover caregivers, social routines (hi, bye, no, thank you), body parts, animal sounds, and a few foods and actions. That similarity fades over the next few hundred words. The data come from parent checklists adapted from a US English template, and about 82% of the children learn Indo-European languages. The data can rank **concept categories** reliably, but individual items only roughly. Their main value for this project is surfacing social-routine and interjection concepts that basic-vocabulary lists such as Swadesh leave out.

## 1. Wordbank

- **Size today.** The live data page reports 104,106 children, 120,878 administrations, 50 languages or dialects and 108 instruments **[sourced, page stats JSON]**. The 2021 book used about 82,000 administrations in 29 languages **[sourced]**. English accounts for 40,179 children (39%).
- **Lineages.** **[inferred]** By my count the languages fall into about 10 spoken families plus 2 sign languages. Most are Indo-European, plus Uralic, Turkic, Sino-Tibetan, Koreanic, Japonic, Afro-Asiatic, Austronesian (Malay), Bantu (Kiswahili, Kigiriama, Tsonga, Ronga) and Mayan (Tseltal). Non-Indo-European languages make up about 18% of children.
- **Unilemmas.** A unilemma is a "rough cross-linguistic conceptual mapping" written as an English gloss (DOG = dog/perro/chien) **[sourced, policy]**.
  - The policy is deliberately **lumper**: it merges distinctions such as clock/watch → *reloj*. It splits only when the cultural roles differ (*pan* vs *tortilla*).
  - Pronouns are glossed as 1SG, 2PL and so on.
  - 46 of 56 instruments had mappings in 2021 **[sourced]**. Most current instruments have 85–100% coverage **[sourced, page JSON]**.
- **Consistency (book ch. 8).** The analysis covers 15 languages and 335 concepts that appear on at least 8 forms **[sourced]**.
  - In production, 12 of the 36 distinct top-10 words were in the top 10 of *every* language.
  - The earliest words were "important family members (*mommy, daddy, grandma*), social routines (*hi, bye, peekaboo*), and sounds (*yum yum, vroom, woof woof*)".
  - The cross-linguistic correlation of age of acquisition **declines** as vocabulary grows.
  - Languages that are closely related agree more than unrelated ones. The authors warn that because CDI items are not a random sample, the correlations "may overestimate" the similarity.
- **Categories (ch. 12)** **[sourced]**:
  - Over-represented everywhere: Sounds, Games & Routines and Body Parts (body parts are highest; Mandarin and Cantonese are lowest).
  - Uniformly under-represented: **Places and Time**.
  - Variable: People, Food, Animals, Vehicles and Clothing. Northern European children skew towards vehicles, clothing and animals. Children in rural Kenya skew towards outside things and places.
  - Animal and body-part words vary least across languages; colour, logic and time words vary most.
  - "No" is very early and "not" comes later. Kiswahili children produce by far the fewest colour words.
- **Predictors (ch. 10 / Braginsky et al. 2019).** For content words the strongest predictors are concreteness and frequency in child-directed speech. "Babiness" (association with babies) matters most early on. These patterns hold across languages more often than chance **[sourced]**.
- **Access.** **[sourced]**
  - A browser tool exports a per-instrument "by word" CSV with item, category, `uni_lemma`, age and proportion of children producing.
  - Full tables are on Redivis, either via R `wordbankr` (needs a free Redivis account) or the Redivis API.
  - Licence: CC-BY, with some datasets CC-BY-NC.
  - Size: a few hundred to about 700 items × about 15 ages per instrument, so small (**[inferred]**). Whether the browser export needs an account is **UNVERIFIED**.
  - I found no Wordbank or CDI list in Concepticon or NoRaRe. NoRaRe holds only adult-rated age-of-acquisition norms. Searched by dataset name, 2026-10-08.

## 2. First-words studies, nouns and verbs

- **Tardif et al. 2008.** 265 English-, 336 Mandarin- and 369 Cantonese-learning infants (8–16 months) with 1–10 words.
  - **[sourced]** The abstract reports "striking commonalities", along with differences in how common nouns, people terms and verbs were.
  - Mommy, daddy, hello, bye, uh-oh and woof-woof made the top 20 in all three languages, and Chinese children were likelier to have a verb among their first 10 words. **UNVERIFIED**: this comes only from a secondary source (Kelty-Stephen, *Psychology Today* 2020).
- **Bornstein et al. 2004.** 269 twenty-month-olds in 7 communities. Nouns made up a larger share of vocabulary in every language **[sourced]**.
- **Gentner (1982) and Gentner & Boroditsky (2001).** Objects are "natural partitions" that a child can pick out easily. Verbs are relational and differ more between languages **[sourced, via Wordbank ch. 11]**.
- **Tardif 1996, "Nouns are not always learned before verbs"** (Mandarin). Wordbank confirms **predicate-favouring production in Mandarin and Cantonese**, but not in Korean **[sourced]**.
  - Even so, two Beijing samples tested on the same items disagreed. The authors warn that bias estimates are fragile.
- **Tseltal (Mayan).**
  - Daylong recordings of 29 children show "weak to no evidence for a noun bias" (Casillas et al. 2024) **[sourced]**.
  - Tseltal has very specific verbs, for example *we'* "eat (tortilla-like food)".
  - The Tseltal CDI (84 children) still reproduces the over-represented categories (Sounds, Routines, Body parts) and the under-represented ones (Places, Time) **[sourced]**.
- **Systematic review (Zhang, Kim & Casillas 2026).** 68 papers covering 28 languages and 10,262 children **[sourced]**.
  - The noun bias is "broadly present but not truly universal". 27% of datapoints show a verb bias.
  - Checklists inflate the noun bias: 1.5% of checklist datapoints are ≤0.5 nouns, against 43% of observational ones.
  - **[inferred]** CDI-based rankings will push actions later than children actually learn them.
- **Social words.** Hi/bye, no, yes, thank you and uh-oh are among the earliest words in nearly all 15 Wordbank languages (Table 8.1) **[sourced]**. "More" is not in any language's top 10 there. I did not verify a universality claim for "more" (**UNVERIFIED**).

## 3. Limitations for this project

1. **Circularity.** Every form adapts the US English item list. A concept missing from the template can't show up as early. **[sourced]** Words are "adaptations and not translations". **[inferred]** Absence from a form must count as missing data, not as "late".
2. **WEIRD skew.** About 82% of children are Indo-European (39% English). The non-industrial samples are small: Tseltal 77 children (subsistence village, Chiapas), Kiswahili 141 and Kigiriama 230 (coastal Kenya, low-literacy interview format; Alcock et al. 2015), Tsonga/Changana 374 and Ronga 242 (rural and urban Mozambique; Vogt et al. 2015). The book itself notes that "African, South American, and South/South-East Asian languages are notably under-/un-represented".
3. **Toys and manufactured goods.** Vehicles, toys, colour words and items like *banana*, *cereal* and *cracker* reflect material culture. **[sourced]** Kiswahili children produce few colour words, perhaps because they have few contrastively coloured toys.
4. **The early tier is a baby register, not adult need.** Onomatopoeia, *peekaboo* and *vroom* rank high because they are "babyish". Babiness predicts early learning and then fades.
5. **Unilemmas are English glosses with a lumper policy.** They are fine for *ordering*, but must not set concept *boundaries*: the plan's strong-rigor rule takes boundaries from cross-linguistic data. One hint for the boundary work: *hand* and *foot* are learned before *arm* and *leg* **[sourced]**.
6. **Fixes.** Rank **categories** rather than items, since they are stable across Tseltal, Kenya and Europe. Weight by family, not by child. Use only concepts that appear on forms from several families.

## 4. A concept-level ranking

**[inferred from §1–2]** Tiers by robustness across families:

- **Tier 1 (earliest everywhere):** mother, father, grandparent; greeting/farewell, thanks, yes/no, *uh-oh* (mishap); eat/food, water, milk; core body parts (hand, foot, eye, nose, mouth); a few animals (dog, cat).
- **Tier 2:** further kin; body parts; basic actions (give, go, sleep, sit, fall); negation; *this*; bodily states (hungry, hurt).
- **Late everywhere:** time words, places, quantifiers and logical words (other than *no/none*), colour.

**Combining with lineage counts.** **[inferred]** The two signals measure different things. Lineage coverage asks "does every society name it?" Acquisition asks "is it in the infant's world?". They agree on body parts, kin, water and eat. They disagree in two useful ways:

- Acquisition adds **routines and interjections**. Lexicostatistic lists such as Swadesh leave these out because they are unstable or sound-symbolic.
- Lineage counts add **adult concepts** that children learn late: time, places and number.

## Recommendation: how to use acquisition data in ordering

1. **Use it as a secondary signal**, behind lineage coverage. Its job is to admit concepts that basic-vocabulary lists miss (social routines, interjections, negation, bodily states) and to break ties at the top of the seed.
2. **Use the category tiers above, not item ranks.** No script for now. Add-back trigger: if lineage data leaves many ties in the first ~200 concepts, write the one extraction script the plan allows. It would download "by word" CSVs for one instrument per family (about 10), compute age of acquisition per `uni_lemma`, and average **per family**. Concepts missing from a form count as missing data. Mapping to Concepticon would be done by hand for about 300 concepts.
3. **Don't let the noun-heavy CDI demote actions.** Put basic actions in tier 1–2. The Mandarin, Cantonese and Tseltal evidence and the 2026 review show checklists understate verbs.
4. **Don't take boundaries from unilemmas.** Take them from lexical typology (CLICS, Majid on body parts).
5. **Proposed deletion:** leave onomatopoeia and baby-register words (woof, vroom, peekaboo) out of the root seed; a sound-symbolism rule can cover them later. Add-back trigger: blind tests of child-directed or conversational text lose points to missing interjections.

## Sources

- Frank, Braginsky, Yurovsky & Marchman 2021, *Variability and Consistency in Early Language Learning* (MIT Press; free online): [book](https://langcog.github.io/wordbank-book/), [ch. 3](https://langcog.github.io/wordbank-book/methods-and-data.html), [ch. 8](https://langcog.github.io/wordbank-book/items-consistency.html), [ch. 10](https://langcog.github.io/wordbank-book/items-prediction.html), [ch. 11](https://langcog.github.io/wordbank-book/categories-syntactic.html), [ch. 12](https://langcog.github.io/wordbank-book/categories-semantic.html)
- Wordbank [data page](https://langcog.github.io/wordbank-datapage/) and [data access](https://langcog.github.io/wordbank-datapage/data.html); [wordbankr](https://github.com/langcog/wordbankr); [Redivis dataset](https://stanford.redivis.com/datasets/627v-9ewzpdvz0); [uni-lemma policy](https://github.com/langcog/update_unilemmas/blob/main/unilemma_policy.md)
- Braginsky et al. 2019, *Open Mind* 3: [doi](https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00026/5378/Consistency-and-Variability-in-Children-s-Word)
- Tardif et al. 2008, *Dev Psych* 44(4):929–938: [doi:10.1037/0012-1649.44.4.929](https://doi.org/10.1037/0012-1649.44.4.929); secondary: [Kelty-Stephen 2020](https://www.psychologytoday.com/us/blog/the-building-blocks-of-language/202008/which-words-will-my-child-learn-first)
- Tardif 1996, *Dev Psych* 32(3):492–504: [doi:10.1037/0012-1649.32.3.492](https://doi.org/10.1037/0012-1649.32.3.492)
- Bornstein et al. 2004, *Child Dev* 75(4):1115–1139: [doi:10.1111/j.1467-8624.2004.00729.x](https://doi.org/10.1111/j.1467-8624.2004.00729.x)
- Gentner & Boroditsky 2001: [doi:10.1017/cbo9780511620669.010](https://doi.org/10.1017/cbo9780511620669.010)
- Casillas et al. 2024, *First Language* 44(6): [doi:10.1177/01427237231216571](https://doi.org/10.1177/01427237231216571)
- Casillas et al. 2025, Tseltal checklist, *Language Development Research* 5(3):245–275: [doi:10.34842/ldr2025-862](http://doi.org/10.34842/ldr2025-862)
- Zhang, Kim & Casillas 2026, *Cognitive Science* 50(7) e70241: [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13347766/)
- Alcock et al. 2015, *J Child Lang* 42(4):763–785: [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5496672/)
- Vogt et al. 2015, *Child Dev Research*: [doi](https://onlinelibrary.wiley.com/doi/10.1155/2015/189195)
- NoRaRe datasets: [concepticon/norare-data](https://github.com/concepticon/norare-data)

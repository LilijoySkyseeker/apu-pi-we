# Ambiguity and structural complexity: what actually causes misunderstanding across languages

Scope note: these notes separate (a) **lab processing difficulty**, meaning slower reading, ERP effects or a measurable interpretation preference, from (b) **real-world miscommunication**, meaning a listener ends up with the wrong meaning and doesn't repair it. Most of the literature measures (a), and evidence for (b) is thin. Claims marked **[UNVERIFIED]** come from search-engine summaries or my background knowledge, not from a primary source I read.

Research caveat: several primary PDFs (Wasow 2015, Piantadosi et al. 2012 preprint, Futrell et al. 2015 PNAS, the Cognitive Science "Wednesday's meeting" meta-analysis) returned 403/405 errors or unreadable binary. Their findings come from abstracts and search snippets, not full text. One fetch of a PDF mirror of Dingemanse et al. returned numbers that conflict with the published PLoS ONE article (it claimed "English and Swedish", "once every 4.8 turns", "46% hearing problems"). That output looks like summarizer hallucination and is **not used** below.

## Baseline: how often does conversation actually break down?

### Takeaway
Across 12 unrelated languages, listeners flag a communication problem about once every 1.4 minutes, and the repair system is structurally the same everywhere. Miscommunication is routine and cheaply repaired in live talk. Unrepaired errors are the real danger, and they concentrate where repair is impossible: writing, one-shot radio messages, high time pressure.

### Cited Findings
- Dingemanse et al. 2015 studied "12 languages of 8 language families spoken on 5 continents" and found "a repair initiation about once every 1.4 minutes across all languages"; "95% of repair initiations happen within 4.13 minutes of the last one." — [Dingemanse et al. 2015, PLoS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0136100)
- "Unrelated languages share the same three functionally distinct types of repair initiator": open requests ("huh?"), restricted requests ("who?", "where?"), and restricted offers (repeating or paraphrasing for confirmation). — [PLoS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0136100); [MPG press release](https://www.mpg.de/9405856/universal-repair-mechanisms-language)
- Max Planck press release: people resolve misunderstandings "once every 90 seconds" on average, and listeners prefer the strategy that "minimizes the effort required by the speaker." — [MPG](https://www.mpg.de/9405856/universal-repair-mechanisms-language)
- The study's conclusion supports a "pragmatic universals" view: "key systems of language use may be largely similar across cultural groups." — [PLoS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0136100)

### Inferences
- Because repair is universal and frequent, a language that runs over a live, interactive channel doesn't need to remove all ambiguity. It needs to make the ambiguities that do occur cheap to detect and query. A designed language could build in efficient clarification forms, such as a "which referent?" query.
- The case for eliminating ambiguity is strongest in **non-interactive channels**: text, recorded instructions, radio under time pressure. There the repair loop is missing.

### Gaps
- I found no breakdown, from the primary source, of what share of repairs are caused by hearing versus lexical, referential or syntactic trouble. I could not verify such figures, and the one set I saw appears fabricated (see the caveat above).

## Lexical ambiguity: how common, and does it cause real misunderstanding?

### Takeaway
Lexical ambiguity is pervasive by design: short, frequent, easy words carry the most meanings. Context almost always resolves it, so it is mostly harmless in practice. Speakers don't reliably avoid it, and when they do, they avoid it only when they can notice it non-linguistically.

### Cited Findings
- Piantadosi, Tily & Gibson 2012 (*Cognition* 122:280–291) give an information-theoretic argument that "all efficient communication systems will be ambiguous, assuming that context is informative about meaning." Ambiguity lets efficient (short, easy) units be reused. They tested this in English, German and Dutch. — [PhilPapers record](https://philpapers.org/rec/PIATCF); [MIT open-access preprint](https://dspace.mit.edu/bitstream/handle/1721.1/102465/Piantadosi,%20Tily%20&%20Gibson%20Cognition%202012%20preprint.pdf?sequence=1); [ScienceDaily summary](https://www.sciencedaily.com/releases/2012/01/120119133755.htm)
- **[UNVERIFIED in full text]** The specific results: shorter words, more frequent words and phonotactically easier words have more meanings and homophones. This is the paper's widely cited result, but I could not open the PDF to get the effect sizes.
- Ferreira, Slevc & Rogers 2005 (*Cognition*): in a referential communication task, "speakers were less likely to modify referring expressions to avoid linguistic ambiguities" (a flying-mammal bat among baseball bats) "than they were to avoid nonlinguistic ambiguities" (two bats of different sizes). — [PubMed](https://pubmed.ncbi.nlm.nih.gov/15996561/); [ResearchGate](https://www.researchgate.net/publication/7746881_How_do_speakers_avoid_ambiguous_linguistic_expressions)
- Wasow, "Ambiguity Avoidance is Overrated" (2015): when potential ambiguity was present, speakers used a disambiguating modifier only about 60% of the time and the ambiguous bare noun about 40% of the time. — [Wasow PDF](https://web.stanford.edu/~wasow/Ambiguity.pdf) (snippet via [ResearchGate](https://www.researchgate.net/publication/319593818_Ambiguity_Avoidance_is_Overrated); the full PDF was unreadable to me)
- Real-world lexical failures do happen, but in specific settings: aviation radio. Cushing's *Fatal Words* covers ambiguities "when aviation jargon and colloquial English are mixed, when a word is used that has different meanings, and when different words are used that sound alike." The "to/two" homophone ("descend to two seven zero zero") is a known hazard. Controllers work around it by saying "tah" or stressing "to". — [U Chicago Press](https://press.uchicago.edu/ucp/books/book/chicago/F/bo3633901.html); [McMillan, "Say again?"](https://www.pacdeff.com/pdfs/Communication%20Issues.pdf)
- Tenerife 1977 (583 deaths): the KLM pilot's "We are now at takeoff" was meant as "taking off." The tower took it as "at the takeoff point, waiting." — [U Chicago Press, Cushing](https://press.uchicago.edu/ucp/books/book/chicago/F/bo3633901.html); [Tajima 2004, World Englishes](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.0883-2919.2004.00368.x)

### Inferences
- Harmless lexical ambiguity: homonyms whose senses can't both fit the context (bank/bank). Dangerous lexical ambiguity: senses that fit the **same** context and lead to **different actions** ("at takeoff", "to/two" before a number). Numerals and the words around them are high-risk.
- Speakers are poor at noticing their own linguistic ambiguity, because the intended meaning is obvious to them. So "speakers will disambiguate when needed" is a weak safeguard. A designed language should rule out ambiguity structurally where it matters, especially between function words and numerals, rather than trust speakers to avoid it.
- Removing all homophony has a cost under Piantadosi et al.'s argument: longer or harder words. The efficient target is no ambiguity within the same context, not zero ambiguity.

### Gaps
- I found no corpus-level estimate of how often lexical ambiguity causes unrepaired misunderstanding in everyday talk. The real-world data are aviation and medical incident reports, which are case studies, not rates.
- I didn't retrieve Arnold et al. on prosodic disambiguation or the optional-"that" studies (Ferreira & Dell 2000; Jaeger) in primary form. **[UNVERIFIED]** My understanding is that both found little production-side ambiguity avoidance.

## Referential ambiguity: pronouns and reference-tracking systems

### Takeaway
Listeners use gender and other agreement cues on pronouns within a fraction of a second, so these cues do disambiguate in processing. Switch-reference and obviation exist as dedicated reference-tracking grammar in many languages. I found **no** comparative evidence that any of these systems measurably reduces real-world reference errors. Reference trouble is a known trigger for repair ("who?" is one of the universal restricted repair types).

### Cited Findings
- Arnold, Eisenband, Brown-Schmidt & Trueswell 2000 (*Cognition* 76:B13–B26): eye-tracking shows English listeners use pronoun gender rapidly to pick the referent. Gender cues interact with order of mention, so when gender doesn't distinguish the candidates, listeners fall back on first-mention or subject preference. — [Arnold et al. 2001 child study PDF, citing 2000](https://cpb-us-w2.wpmucdn.com/web.sas.upenn.edu/dist/4/81/files/2019/07/Arnold_Novick_Brown-Schmidt_Eisenband_Trueswell_2001-tgem5q-pdf.pdf); search summary
- Järvikivi, van Gompel, Hyönä & Bertram 2005 (*Psychological Science*), "Ambiguous Pronoun Resolution": Finnish, where pronouns have no gender. Both subjecthood and first mention affect which antecedent readers choose for an ambiguous pronoun. — [DOI](https://doi.org/10.1111/j.0956-7976.2005.01525.x) (title and topic verified; details **[UNVERIFIED]**)
- Switch-reference: verb morphology marks whether the subject (pivot) of the linked clause is the same as or different from that of the current clause. Its "primary function is to indicate whether two linked clauses have coreferential pivots." — [Wiley, Camacho: Switch Reference and Obviation](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118358733.wbsyncom014); [PMC, Mbyá switch-reference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12919634/)
- Obviation, as in Algonquian languages, ranks third-person arguments: the proximate marks the topic in focus and the obviative marks the others. Obviation works within a clause, while switch-reference always works across clauses. — [Wiley, Camacho](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118358733.wbsyncom014)
- Switch-reference markers are not purely referential. In some languages they also mark changes in time, place or actuality ("non-canonical switch-reference"). A multivariate study of Mbyá Guaraní narratives analyses canonical and non-canonical uses. — [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12919634/); [PubMed](https://pubmed.ncbi.nlm.nih.gov/39582735/)

### Inferences
- Reference tracking is the most likely place for a carefully designed system to pay off: sign languages' spatial loci, obviation, switch-reference, and noun-class agreement all give each referent its own "handle." But the empirical case that they reduce errors is **theoretical, not demonstrated**. And the fact that switch-reference markers drift into non-referential uses suggests natural systems don't hold them to strict reference tracking.
- A natural design target is an explicit referent-index or proximate/obviative device for third persons. It is optional when context suffices and available when two or more same-class referents compete. That matches what gender does in English: it disambiguates when it can and falls back on salience when it can't.

### Gaps
- I found no cross-linguistic study comparing pronoun-misresolution rates between languages with and without switch-reference or obviation, or with rich versus poor gender systems.
- I didn't retrieve sign-language spatial-loci studies in this pass.
- I didn't retrieve studies on null-subject (pro-drop) languages such as Italian, Spanish or Chinese and their effect on reference errors. A Catalan eye-tracking study exists ([Springer](https://link.springer.com/article/10.1007/s10936-025-10189-7)), but I didn't read it.

## Structural ambiguity, garden paths, center embedding and dependency length

### Takeaway
Here the evidence is strongest that structure, not just ambiguity, imposes real limits. Multiple center-embedding essentially never occurs in speech and stops at depth 3 even in writing. Languages measurably minimize dependency length. Attachment ambiguity and garden paths are robust in the lab, but I found no evidence that they cause frequent real-world errors.

### Cited Findings
- Karlsson 2007 (*Journal of Linguistics* 43(2):365–392), a corpus study: "in spoken language, multiple center-embedding is practically absent"; "the maximal degree of multiple center-embedding of clauses is exactly 3 in written language". Typical center-embeddings are relative clauses on the subject NP. — [U Helsinki research portal](https://researchportal.helsinki.fi/en/publications/constraints-on-multiple-center-embedding-of-clauses); [ResearchGate](https://www.researchgate.net/publication/231982450_Constraints_on_multiple_center-embedding_of_clauses)
- Futrell, Mahowald & Gibson 2015 (*PNAS* 112(33):10336–10341): in parsed corpora of 37 languages, "overall dependency lengths for all languages are shorter than conservative random baselines". The authors call this "the first large-scale, quantitative, cross-linguistic evidence for a universal syntactic property." — [ADS abstract](https://ui.adsabs.harvard.edu/abs/2015PNAS..11210336F/abstract); [Semantic Scholar](https://www.semanticscholar.org/paper/Large-scale-evidence-of-dependency-length-in-37-Futrell-Mahowald/cdb9d583f4d241bc31fc7e25d503f706b6712652)
- A later reappraisal questions how universal dependency length minimization (DLM) really is. — [PMC9692064, "A Reappraisal of Dependency Length Minimization as a Linguistic Universal"](https://pmc.ncbi.nlm.nih.gov/articles/PMC9692064/) (title only; I didn't read the content)
- **[UNVERIFIED]** Background: Futrell et al. report weaker minimization in head-final languages (Japanese, Korean, Turkish) and German than in head-initial languages. Gibson's Dependency Locality Theory (1998/2000) links processing cost to dependency length.

### Inferences
- These are hard **capacity** limits, not ambiguity problems. Even a perfectly unambiguous sentence fails if it needs deep center-embedding or long dependencies. A designed language should make right-branching and short dependencies the default, and offer flattening devices (serial clauses, resumptive markers) so that nesting is never needed.
- Garden paths are mostly a lab and writing phenomenon. In speech, prosody and context usually prevent them. The risk remains in **text without prosody**: headlines, instructions, legal language.

### Gaps
- I found no corpus or incident evidence that attachment ambiguity ("I saw the man with the telescope") causes real miscommunication at any measurable rate. **[UNVERIFIED]** Legal disputes over modifier scope, such as the Oxford-comma overtime case *O'Connor v. Oakhurst Dairy* (2017), are anecdotal evidence that it matters in unrepairable text.

## Quantifier scope and negation (including answers to negative questions)

### Takeaway
Scope ambiguity is resolved by a strong surface-order preference. Inverse readings are available to adults, but children often miss them. Negation is slower to process in isolation, but the cost largely disappears when context licenses it. The clearest real communicative hazard in this area is **answering negative questions**: languages split between polarity-based and truth-based yes/no systems, and English bare "yes" to a negative question is genuinely indeterminate.

### Cited Findings
- Scope: when a scope ambiguity arises, people prefer the surface-order (overt) reading over the inverse reading. Kurtzman & MacDonald 1993 established this with continuation-sentence methods. — [Szendrői, Quantifier scope judgments (UCL)](https://www.ucl.ac.uk/~uczaksz/papers/Quantifier_Scope.pdf); [ResearchGate](https://www.researchgate.net/publication/14928991_Resolution_of_quantifier_scope_ambiguities)
- "Every horse didn't jump over the fence": children accepted the not-all (inverse) reading about 7.5% of the time and adults 100%, per a search summary of Musolino et al. Children improve markedly when an overt contrast is given. Musolino & Lidz 2002 found about 34% for children versus 93% for adults in another condition. — [Lidz & Musolino 2002 PDF](https://semantics.uchicago.edu/kennedy/classes/s09/experimentalsemantics/lidz-musolino02.pdf) (**[UNVERIFIED]**: exact figures from a search summary, not read from the PDF)
- Negation cost: in sentence-picture verification, negative sentences take significantly longer than affirmatives (Clark & Chase 1972; Carpenter & Just 1975). — [Tian & Breheny, UCL](https://discovery.ucl.ac.uk/1571834/1/negation%20tian%20&%20breheny%20pre-pub%20draft.pdf); [Nordmeyer & Frank](https://langcog.stanford.edu/papers/NF-cogsci2014.pdf)
- Nieuwland & Kuperberg 2008: when context licenses the negation ("With proper equipment, scuba diving is not dangerous"), true negatives show no extra N400 cost. Context "softens or even eliminates" the negation cost. — [ResearchGate](https://www.researchgate.net/publication/23718838_When_the_Truth_Is_Not_Too_Hard_to_Handle_An_Event-Related_Potential_Study_on_the_Pragmatics_of_Negation)
- Double negation versus logic: there is recent work on whether "two negatives make a positive" in processing. — [Language, Cognition and Neuroscience 2023](https://www.tandfonline.com/doi/full/10.1080/23273798.2023.2190134) (title only; I didn't read it)
- Answer systems: in **polarity-based** systems (English, Swedish), "no" agrees with a negative question ("Are you not tired?" → "Nej" = I'm not tired). In **truth-based** systems (Japanese), "yes" (hai/un) agrees with the negative proposition (= I'm not tired). — [Holmberg, The syntax of yes and no (2015)](https://recos-dtal.mmll.cam.ac.uk/system/files/documents/Holmberg2015Thesyntaxofyesandno.pdf); [ACL Y17-1001](https://aclanthology.org/Y17-1001.pdf)
- Kramer & Rawlins ran a large online experiment. Bare "yes" in answer to a negative question with *not* either confirms the negation or is judged indeterminate, so English "yes" is unreliable here. — [summary in ACL Y17-1001](https://aclanthology.org/Y17-1001.pdf); [LSA proceedings](https://journals.linguisticsociety.org/proceedings/index.php/PLSA/article/download/4518/4141)

### Inferences
- Negative questions and their answers are a **real** cross-linguistic hazard. Within one language, bare "yes" is indeterminate, and across a polarity-based/truth-based language pair, the same word means opposite things. A designed language should avoid bare polarity particles after negative questions. Options: echo answers (repeat the verb, as Finnish and Chinese do), or separate particles for "agree" and "proposition is true", like French *si* or German *doch* for contradicting a negative.
- Negation's processing cost doesn't argue against negation. It argues against negation without context. Double negation and negative concord are mostly a learner and cross-dialect issue, since natives resolve them by convention. **[UNVERIFIED]**: I found no study showing real-world errors caused by negative concord among native speakers.
- For scope, the default is surface order. A designed language that makes scope follow linear order, with an explicit marker for the rare inverse reading, would match the preference listeners already have.

### Gaps
- I found no corpus or incident rate for scope-related misunderstanding outside the lab.
- I didn't find the WALS chapter on answers to polar questions, or counts of how many languages use each system.

## Time reference: tense, aspect, tenseless languages and relative time words

### Takeaway
I found no evidence that lacking obligatory tense (Mandarin, Cantonese) causes misunderstanding. Listeners infer time from adverbials, aspect and context, and even L2 learners do this accurately. The documented time-reference hazard is lexical and metaphorical: "move the meeting forward" splits English speakers roughly in half. "Next Friday" has the same reputation, but I couldn't verify it from a primary source.

### Cited Findings
- Mandarin has no tense morphemes. Its speakers get time reference from temporal adverbials (yesterday, last week), viewpoint-aspect markers (*le* perfective/completion, *zài* progressive) and connectives (*zhīqián* before, *zhīhòu* after). — [Brain Sciences 2022 ERP study](https://doi.org/10.3390/brainsci12040474); [Springer, Temporal Reference in Mandarin Chinese](https://link.springer.com/article/10.1023/A:1023665301095)
- Mandarin speakers are sensitive online (ERP) to temporal agreement violations even without overt tense. — [ResearchGate, ERP study](https://www.researchgate.net/publication/221839442_Processing_temporal_agreement_in_a_tenseless_language_An_ERP_study_of_Mandarin_Chinese)
- L2 Mandarin learners follow the "deictic pattern" (bounded events read as past, unbounded as present). Their temporal interpretations were "highly accurate even at intermediate levels of proficiency." — [ERIC EJ1070158, Modern Language Journal 2015](https://eric.ed.gov/?id=EJ1070158)
- Cantonese is described as "genuinely tenseless." — [ResearchGate](https://www.researchgate.net/publication/366681794_Genuinely_tenseless_encoding_time_in_Cantonese)
- "Next Wednesday's meeting has been moved forward two days": answers split between Monday and Friday. One comparison group answered at chance, 54% Monday and 46% Friday. A meta-analysis was published in *Cognitive Science* (2018), "Wednesday's Meeting Really Is on Friday." — [Wiley, Cogn Sci](https://onlinelibrary.wiley.com/doi/full/10.1111/cogs.12559); [ResearchGate](https://www.researchgate.net/publication/320376226_Wednesday's_Meeting_Really_Is_on_Friday_A_Meta-Analysis_and_Evaluation_of_Ambiguous_Spatiotemporal_Language)
- The question is ambiguous in Swiss German but not in Standard German (Stocker & Hartmann 2019, *Swiss J Psych*). Mandarin speakers have also been tested. — [Hogrefe](https://econtent.hogrefe.com/doi/10.1024/1421-0185/a000220); [ScienceDirect, Lingua 2020](https://www.sciencedirect.com/science/article/abs/pii/S0024384120300139)

### Inferences
- Obligatory tense is not needed for faithful time transmission. Optional time adverbials plus aspect seem to work. **The real failures are in relative and metaphorical time expressions**, where the anchor (now, or a reference event) or the direction (forward/back) is ambiguous. A designed language should give **deictic anchor plus signed offset** an explicit, unambiguous form ("the Friday in the 7-day window after today" versus "the Friday of next calendar week") and avoid space-motion metaphors for moving events.
- It is a consistent pattern that the ambiguity changes between closely related varieties (Standard versus Swiss German). These ambiguities come from lexical conventions, not cognition, so design can fix them.

### Gaps
- I found no primary study measuring misinterpretation of "next Friday" or "this Friday". The claim is widely reported informally. **[UNVERIFIED]**
- I couldn't access the meta-analysis's pooled percentages.
- I found no study testing whether Mandarin speakers misunderstand time reference in real communication more than English speakers. The absence of such a study is itself informative: the question appears in L2 and ERP work, not as a documented failure.

## Numbers: transparency of number-word systems and errors in number communication

### Takeaway
Transparent base-10 number words (Chinese) measurably speed children's counting acquisition beyond the teens. Opaque systems (English teens; French 70–99 **[UNVERIFIED here]**) cost learning time. In adult real-world communication, the main documented number errors come from homophony and mishearing (to/two in aviation), not from opacity.

### Cited Findings
- Miller, Smith, Zhu & Zhang 1995 (*Psychological Science* 6:56–60), "Preschool origins of cross-national differences in mathematical competence: the role of number-naming systems": Chinese children show more counting competence than US children by age 5. The difference is traced to the regular Chinese names for 11–20 (ten-one, ten-two...) versus irregular English teens. — [search summary; cited in Springer review](https://link.springer.com/article/10.1007/s007870070004); [Ng & Rao 2010 review, Rev Ed Research](https://journals.sagepub.com/doi/abs/10.3102/0034654310364764)
- Aviation: the homophones "to/two" and "for/four" before altitudes and headings are a recognized error source, with procedural workarounds. — [McMillan, "Say again?"](https://www.pacdeff.com/pdfs/Communication%20Issues.pdf); [Cushing, Fatal Words](https://press.uchicago.edu/ucp/books/book/chicago/F/bo3633901.html)

### Inferences
- Number words should be strictly compositional (base and digit order) and **phonologically distinct from every function word**. Aviation's "niner" and "tree" respellings are evidence that natural numerals fail on noisy channels.
- **[UNVERIFIED]** Background: Miller et al. found that the US–China gap appears only after about 10. Below 10, both groups are similar, which supports the transparency explanation over a general-ability one.

### Gaps
- I didn't retrieve the Miller et al. 1995 primary text or effect sizes, the French and Danish vigesimal data, or studies on digit-order inversion (German/Dutch "one-and-twenty") causing transcription errors in adults. **[UNVERIFIED]** I recall such studies exist, for example on transcoding errors in German-speaking children.

## Obligatory categories and their communicative consequences (Jakobson/Boas)

### Takeaway
Boas and Jakobson's principle says languages differ in what they **must** express, not in what they **can** express. Obligatory categories therefore force information into the message, whether or not the speaker meant it or it is accurate. I found no empirical study showing that lacking an obligatory category causes misunderstanding. The evidence above, on tense and on gender as a pronoun cue, points to context and optional devices covering the gap.

### Cited Findings
- Jakobson (1959, "On Linguistic Aspects of Translation"): "Languages differ essentially in what they must convey and not in what they may convey." Example: to translate "I hired a worker," a Russian speaker needs information English leaves out: whether the action was completed (aspect) and whether the worker was male or female (gender). "Each verb of a given language imperatively raises a set of specific yes-or-no questions." — [Cultural Reader: Jakobson full text](https://culturalstudiesnow.blogspot.com/2011/10/roman-jakobson-on-linguistic-aspects-of.html); [Deutscher interview, Paris Review](https://www.theparisreview.org/blog/2010/11/09/guy-deutscher-on-%E2%80%98through-the-language-glass%E2%80%99/)
- Boas: the grammar of each language "determines those aspects of each experience that must be expressed." — [Paris Review / Deutscher](https://www.theparisreview.org/blog/2010/11/09/guy-deutscher-on-%E2%80%98through-the-language-glass%E2%80%99/)

### Inferences
- For faithful transmission, an obligatory category has two edges. It guarantees that a dimension is always present, as evidentiality or tense would. But it also forces speakers to commit to values they may not know or intend, adding false precision. That is a fidelity loss too. Design implication: make high-value dimensions available and cheap to mark, with an explicit "unspecified" value instead of a forced choice. Candidates are reference index, time anchor, polarity agreement and number.
- Given the doghouse warning: this whole note suggests natural languages already handle most ambiguity through context and repair. The measurable failures cluster in a short list: numerals and homophones on noisy channels, answers to negative questions, relative and metaphorical time expressions, reference with competing same-class referents, and deep embedding or long dependencies. A designed language that fixes those few points captures most of the evidence-backed gain.

### Gaps
- I didn't consult the WALS chapters, for example on evidentiality, gender systems or tense. I found no study quantifying the communicative consequences of having or lacking a given obligatory category.
- Evidentiality, a candidate obligatory category directly relevant to transmitting thought faithfully, was out of my search budget.

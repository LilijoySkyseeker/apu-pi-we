# Globasa in depth: what Apupiwe should adopt, adapt or not

Task: `research/notes/globasa-prompt.md`. Roadmap item "Globasa in depth" (author, 2026-10-13). Working note: terse.

## Progress

- [x] Sources fetched: Globasa-Team GitHub repos cloned to `~/work/cache/globasa/` (main-pages-grav = globasa.net pages; xwexi-pages-grav = course + full grammar; globasa-docs; globasa-api; cdn-files). Dictionary export `https://cdn.globasa.net/api2/word-list.csv` (9,516 rows, 2026-10-13). Prior notes read: `research/notes/auxlangs-parts/4-modern-auxlangs.md` (Globasa section), `research/reports/Conlang design principles compared.md`.
- [x] Site pages read: design principles, methodology, word proposal, history, stability, changes (phases 1–6), Q&A, licence.
- [x] Grammar (xwexi, all 14 pages) read and summarised (§3).
- [x] Dictionary data analysed (§4.3): sources per root, core vs whole, length, minimal pairs, antonym distance; same measures on Apupiwe's lexicon. Scripts `~/work/cache/globasa/an3.py`–`an9.py` (outside the repo; rerun with `direnv exec <repo> python3 anN.py` from that folder).
- [x] Tooling and governance (§5).
- [x] Outside discussion (§5.4).
- [x] Sections 1–6 written.
- [ ] Idea table (§7) and the floorboard question (§8).
- [ ] Summary lists (§9); roadmap entry.

Labels: **[site]** Globasa's own pages; **[data]** my count from Globasa's dictionary export; **[sec]** secondary source; **[unverified]** not checked against a primary source; **[me]** my inference.

---

## 1. Aim and principles, against Apupiwe's goal

- **Founding image** [site, [home](https://www.globasa.net/eng/)]: 1,000 randomly chosen people from around the world settle an empty island; "What would the village language look like within three generations?" Launched 2019 by Hector Ortega, "a linguist, translator and expert in adult language acquisition and teaching", "created with the average world citizen in mind to be as easy as possible to learn and to use without sacrificing clarity or expressiveness."
- **Three principles** [site, [Design Principles](https://www.globasa.net/eng/max/diseno-principi)]: internationality; "optimal simplicity with the goal of maximum learnability *and* ease of use for *both* speaker *and* listener"; "optimal balance between opposing linguistic parameters". Design "reminiscent of the world's creole languages".
- **Three explicit asymmetries** [site, same page]: easy for the speaker is not always easy for the listener; easy in writing is not always easy in speech; easy for a linguist is not always easy for an ordinary person. Hence "middle ground" everywhere: 5 vowels + 20 consonants, limited clusters, mostly analytic with "just enough" affixes, head-last for simple phrases and word formation, head-first for complex phrases.
- **Internationality is weighted by size and influence** [site]: "rely primarily, although not exclusively, on the largest and most influential languages and language families". Rationale: smaller languages have borrowed from these, so they "are bound to have at least a small number of words in common".

**How this differs from Apupiwe.**
| | Globasa | Apupiwe | Note |
|---|---|---|---|
| Who it's for | adult learners, "the average world citizen" | native speakers (P3, C2); adults only through the gate (B10) | The island image is a *nativisation* scenario (third generation = natives), but every Globasa design argument is about learners [me]. Apupiwe takes the image's own logic further. |
| Fairness unit | the largest, most influential languages and families | lineages, not head counts (N3; method §1) | Globasa's choice directly conflicts with N3. |
| What is borrowed | roots (form + meaning) from a 16–17-language panel | functions and boundaries from lineage data (B5); forms only when world-shared (L4) | The floorboard question, §8. |
| Simplicity | "middle ground", balance | costs minimised together: lifetime effort (B8) + learning effort (B7); guarantees hold first (C1) | Same instinct; Apupiwe's is more explicit about who pays. |
| Listener ease | named principle | B2 (hard to mishear) as a guarantee; confusion model | Both treat the listener as a first-class constraint; rare among auxlangs [me]. |

---

## 2. Sounds and spelling

Sources: [Alphabet and Pronunciation](https://xwexi.globasa.net/eng/gramati/abece-ji-lafuzu) [site], [Design Principles](https://www.globasa.net/eng/max/diseno-principi) [site], [History](https://www.globasa.net/eng/max/histori-de-globasa) [site].

- **Inventory:** 5 vowels a e i o u; 20 consonants b c(tʃʰ) d f g h(x) j(dʒ) k(kʰ) l m n p(pʰ) r(ɾ) s t(tʰ) v w x(ʃ) y z. Latin alphabet minus q; one letter, one phoneme. Chosen from "phonemes familiar to at least 50% of the population", within Roman-alphabet limits (History).
- **Voiceless stops ideally aspirated** "so as to better distinguish them from their voiced counterparts". [site]
- **Declared free variants per phoneme** (a table): r may be [ɾ r ɹ ɹ̠ ɻ ʁ]; h [x χ ħ h]; x [ʃ ʂ ɕ]; c [tʃʰ ʈʂʰ tɕʰ tʃ]; j [dʒ ʒ dʑ ɟʝ]; k may be [q]; w and v may both be [ʋ]; w/y may be pronounced as unstressed u/i. "everybody should make an effort to not deviate too much from the set of allophones listed here." [site]
- **Unwritten epenthesis allowed:** a glottal stop between any two vowels; a central vowel (ə) between any two consonants or word-finally ("magneto" → [magəˈneto]). [site]
- **Syllable (ordinary words):** (C)(C)V(C); onsets single C or C+l/r/w/y; any single coda inside a word, but word-finally only f l m n r s w x y (since Sept 2019); no stop+stop clusters (Italian model: *ativo*, *otima*).
- **Three phonotactic tiers** [site]: ordinary words; proper nouns (any coda, two-consonant codas, *Madrid*, *Budapest*); **culture-specific words** (proper-noun rules inside the word, ordinary rules word-finally: *teriyaki*, *koktel*, *vodka*, *jazu*).
- **Stress:** last vowel if the word ends in a consonant, else penultimate; one stress per word, no secondary stress; monosyllabic content words stressed, monosyllabic particles unstressed. Spelling y/w vs i/u encodes stress placement (*Maryo* vs *Maria*).
- **Capitals:** "no set rules"; at the writer's discretion.
- **Stated trade-off** [site]: fewer consonants would mean "a greater number of similar-sounding words … Or, to avoid this, average word length would need to be increased" and less fidelity to sources. Apupiwe measured the same trade-off and went the other way (13 consonants, `build.py scale`; rationale §2), because its forms don't need source fidelity.

**Against Apupiwe.** Apupiwe has 13 consonants, (C)V(n), initial stress, lowercase standard. The parts of Globasa's sound design that exist for source fidelity (h /x/, c, j, x, z, v, r, clusters, codas) have no source in Apupiwe's goal, since its roots aren't borrowed. Two parts do transfer: the **declared accent-tolerance table** (which realisations count as the same sound) and the **culture-specific word tier**. Both are in §7.

Independent agreement worth recording: Globasa's hard bans are minimal pairs with v/w, s/z, or m/n word-finally ([Methodology](https://www.globasa.net/eng/max/metode-fe-lexiseleti)) [site]. Apupiwe deleted /v/ and /z/ and treats final -n as the first thing to drift (rationale §2, §3.3). Two designers reached the same three weak spots by different routes.

---

## 3. Grammar

Sources: the complete grammar on Xwexi, `xwexi-pages-grav/04.gramati/*` ([Content words](https://xwexi.globasa.net/eng/gramati/inharelexi), [Function words](https://xwexi.globasa.net/eng/gramati/gramatilexi), [Pronouns](https://xwexi.globasa.net/eng/gramati/pornamelexi), [Correlatives](https://xwexi.globasa.net/eng/gramati/tabellexi), [Numbers](https://xwexi.globasa.net/eng/gramati/numer-ji-mesi), [Verb forms](https://xwexi.globasa.net/eng/gramati/falelexili-morfo), [Phrase structure](https://xwexi.globasa.net/eng/gramati/jumlemonli-estrutur), [Sentence structure](https://xwexi.globasa.net/eng/gramati/jumleli-estrutur), [Word formation](https://xwexi.globasa.net/eng/gramati/lexikostrui), [Truncated morphemes](https://xwexi.globasa.net/eng/gramati/ofkatado-morfomon)) [site]. A full PDF grammar dated 2026-08 is in the repo (`ENG_KompletoGramati_mesi8_nyan2026.pdf`; not read beyond the pages, which it compiles [unverified]).

### 3.1 Word order and word classes
- SVO; S-O-V and O-S-V allowed in poetry with the object marker **el**. Prepositions. Relatively strict order inside phrases.
- **Noun phrase is head-last:** determiner → possessive → quantifier → adj-modifying adverb → adjective → noun: *hin misu care daymo lama kitabu* "these four very old books of mine". Complex adjective phrases and relative clauses follow the noun. Apupiwe is head-first throughout (noun, modifiers, number, **la**, determiner, **pi**, relative clause).
- **Two content-word classes** (noun/verb words; adjective/adverb words) plus three auxiliaries. Ortega rejected classless words because Pandunia "lacked the necessary morphology and syntax to disambiguate simple sentences" ([History](https://www.globasa.net/eng/max/histori-de-globasa)). Apupiwe is classless and disambiguates by meaning-based clear forms (**gun** state, aspect word event, **man** description; rationale §10, "Clear forms by meaning").
- Consequence in Globasa: **a noun phrase must end in a noun or pronoun** (*banete ergo* "some (people) work" vs *ban ergo* "some work"), because nouns and verbs share forms. Apupiwe lets a determiner stand alone (5.2.8) and relies on position.

### 3.2 Particles, tense and aspect
- Tense particles **nun** present, **le** past, **xa** future; stack two for aspect (*le nun* was doing, *nun le* have done, *le xa* was going to, *xa le* will have); **dupul** continuative ("have been doing for"); **ja-** immediate (*jale* just did, *jaxa* about to); **du-** habitual/durative and gerund; **ger** conditional; **am** imperative/jussive (and polite request with **kam**); **na** infinitive; **be-** passive with the agent as a bare object (*Piu le beoko mi* "the bird was seen by me").
- **Omission rule** (revised Phase 4): the bare verb is general present; narration may use the bare verb; once a tense is set by the first verb of a predicate it carries. This converged on Apupiwe's frame rule (8.1.1), from the opposite starting point (Globasa started with obligatory particles).
- **Negation** **no** immediately before what it negates; focus adverbs (**sol** only, **pia** also, **hata** even) precede what they cover. Same scope rule as Apupiwe's phrase operators (6.2).
- **Contrastive emphasis** **he** before any word (*He mi le …* "*I* …"). Same function and position as Apupiwe's **o**.

### 3.3 Questions, answers, clauses
- Yes/no: initial **kam**; tag *…, kam no?*. Wh-words in situ (*Yusu name sen keto?* "your name is what?"). "Colon questions" for choices: *Yu suki keto: kafe or cay?* Apupiwe has the same three (**min** initial, **yu** in situ, **… lu …, yu**). Converged.
- **Yes/no words exist** (**si**, **no**). Apupiwe has none: echo answers (4.8.6), because "yes" to a negative question means opposite things across languages.
- **Relative clauses:** marker **hu**, normal SVO kept (Phase 4 replaced relative pronouns to "preserve SVO"), and an **obligatory resumptive pronoun da** for every role, including subject: *femixu hu da lubi mi* "the woman who (she) loves me"; *katatul hu mi kata roti yon da* "the knife which I cut bread with it". Place/time/manner take an obligatory resumptive correlative (Phase 5: *Xaher hu mi le yam sen Tokyo* was a garden path, "the city which I ate", so *denloka* "there" is now required) ([reddit, archived](https://web.archive.org/web/2024/https://www.reddit.com/r/Globasa/comments/zq9xwx/grammar_adjustment_resumptive_correlative_adverb/)). Apupiwe: gap strategy, relation word stranded at the clause end for obliques (**kemu man to nume mon**), resumptive only for "whose" (**pi wan**). Apupiwe already marks the oblique, so it doesn't have Globasa's garden path.
- **Content clauses** on nouns use **feki** ("the news *that* he won"), distinct from relative **hu**. Apupiwe uses **wun** for content clauses and **man** for relatives; same split.
- **Subordinate clauses** keep tense marking (except conditional *if*). Complementiser **ki**; indirect questions **ku**.

### 3.4 Pronouns, nouns, people
- **mi, yu, te** (animate, gender-neutral), **to** (inanimate); plurals by a vowel prefix **imi, uyu, ete, oto**; **ren** impersonal "one"; **se** reflexive; **da** resumptive. Possessive suffix **-su**. Animate/inanimate split = Apupiwe's **wan**/**bu**. No inclusive/exclusive "we" (Apupiwe has **pen**/**din**), no logophor, no topic-based obviation.
- Nouns: no number, no articles; **plu** for plurality, **un** for singularity, **hin/den** for definiteness when needed. Same as Apupiwe (optional **la**, no articles).
- Gender-neutral nouns with **fem**/**man** modifiers (*femnini* girl); gender-neutral **atre** "parent" and **mapa** "mom/dad" beside **matre/patre**, **mama/papa**. Apupiwe: gender as a modifier stated once (5.2.2); "parents" is the compound **mole yen wede**; "parent" is on the coverage list (`roots-1500.txt` line 963).
- **Endearment particle ci** after a noun or name: *mama ci* "mommy", *nini ci* "kiddo", *Jon ci* "Johnny". Apupiwe has nothing for affection/diminutive.
- **Honorifics** **gao** (high) and **kef** (chief) before titles. Apupiwe: **lanno**.
- **Apposition allowed** (*Hotel Kaliforni*, *misu doste Mark*, *lexi kursi* "the word *chair*"). Apupiwe has none (10.1.4).
- Optional particle **di** marks a proper or culture-specific word that is homonymous with an ordinary word. Apupiwe's **en** marks every name, which is stronger.

### 3.5 Modifiers
- Adjective/adverb words share form; before a noun = adjective, elsewhere adverb; adverbs may go before the verb, after the objects, or sentence-initially *with an obligatory pause* ("Without the pause, the adjective/adverb could be mistakenly interpreted as modifying the subject").
- **-mo marks a modifier of a modifier** (Phase 1 fix: *dayo bala uma* meant both "big strong horse" and "very strong horse"; now *perfeto blue oko* "perfect blue eyes" vs *perfetomo blue oko* "perfectly blue eyes"; *syahemo roso* "dark red") ([Changes](https://www.globasa.net/eng/max/alogi-ji-lilalogi)) [site]. **Apupiwe's reference has no rule for a content word modifying another modifier** ("dark red shirt", "naturally black hair"): stacked modifiers after a noun are unspecified [me, checked `spec/reference.toml` and lessons]. A gap Globasa found in use.

### 3.6 Correlatives, comparison, numbers, time
- **Correlative grid** of ke- (which), hin- (this), den- (that), ban- (some), moy- (every), nil- (no), alo- (other), sama- (same) × -te/-to (person/thing), watu (time), loka (place), seba (reason), maner (manner), numer, kwanti, -pul (kind), -mo (degree), -su (whose). So "never" = **nilwatu**, "always" = **moywatu**, "elsewhere" = **aloloka**, "for the same reason" = **samaseba**. Apupiwe builds these from noun + determiner (**mon kemu yu** "where") and has a queued gap: no single word for "never" or "often" (`roadmap.md`).
- Comparison: **max/min … kom**, superlative **maxim/minim** (+ obligatory pronoun), equative **denmo … kom**, **folki … max, … max** "the more …, the more …". Apupiwe: **ke … se**, **ke … se we**, **fu**; no "the more…the more" construction in the reference [me].
- **Numbers:** nil un dua tiga care lima sisa sabe oco nue; 10 **des**, 100 **cen**; teens and tens regular (*des un*, *duades*); and **the SI prefixes are the number words**: 10³ **kilo**, 10⁶ **mega**, 10⁹ **giga**, 10¹² **tera**, larger by stacking (*kilo tera* 10¹⁵); fractions **deci centi mili mikro nano piko** (Phase 4, [reddit](https://www.reddit.com/r/Globasa/comments/mb3ych/deci_centi_mili_mikro_nano_etc_peta_eksa_zeta_yota/), not fetched). Units: *metro, kilometro, gramo, litro*. Ordinals **-yum**, multipliers **-ple**, collectives **-yen/-xey**, fractions **of-** (*tiga oflima* 3/5). Apupiwe: **munno** 1000, **tonen** million, **siwin** billion, beside borrowed **kilo-**, **senti-**, **mili-** in units, so 1000 has two forms.
- **Months by number** (*mesi un* …). Same as Apupiwe.
- **Weekdays by planet** (*Soladin, Lunadin, Marihidin, Bududin, Muxtaridin, Zuhuradin, Xanidin*). A 2020 community vote went **11–9 for numbered days**; Ortega overrode it because numbering conflicts across cultures (Monday-first vs Sunday-first; Swahili counts from Saturday; *duadin* would collide with *dua dina* "two days") and the planetary order is the same in every language that uses it (Europe, India, Japan, Korea) ([reddit, archived](https://web.archive.org/web/2023/https://www.reddit.com/r/Globasa/comments/kidnv2/astronomical_method_selected/)). Apupiwe numbers weekdays by ISO 8601 (Monday = 1).

### 3.7 Word formation
- **Grammatical affixes:** **-li** (of, relating to), **-mo**, **-ya** (abstract noun), **-gi** (causative/transitive), **-cu** (become/intransitive), **-ne** (active participle), **-do** (resultative), **be-** (passive), **du-** (habitual/gerund), **-su** (possessive).
- **Derivational prefixes:** aw- (away), dis-, fin- (end), fron- (forward), ja- (adjacent), nen- (un-), pos- (opposite), pre- (arrive-), ri- (again), ru- (back), xor- (start), awto-, eko-.
- **"Quasi-affixes":** ordinary words used as compound heads: **-dom** place/building, **-tul** tool, **-yen** person, **-xey** thing, **-tora** machine, **-kamer** room, **-maso** meat, **-lari** collection, **-tim** team, **-kef** chief, **-logi** study, **-medis** branch of medicine, **-sa** language/animal cry, **day-/lil-** augmentative/diminutive, **-sim** -like, **-kal** -less, **-pul** -ful, **-ible/-abil**, **-fil** prone to, **-laye** worthy, **mal-** mis-, **semi-**. Compounds are head-last and written as one word (optional hyphens since Phase 5).
- **Truncated morphemes:** many function words are clipped from content words, "similar in form to certain content words as a way to facilitate the process of learning them": **cel** to ← *cele* goal, **tas** to (recipient) ← *taslum* receive, **kom** than ← *kompara*, **kos** because ← *kosa*, **yon** with (using) ← *yongu* use; suffixes **-gi** ← *gibe* give, **-cu** ← *cudu* obtain. Cites Deutscher's *The Unfolding of Language* (grammaticalisation).
- **Verb valency:** each verb is classed transitive, intransitive, copula, auxiliary, "echo-object" (*somno* sleep, *haha* laugh: the optional object repeats the verb), or ambitransitive in four subclasses (feeling, state, non-agentive, motion), each with its own reading when the object is missing. This area changed in Phases 3, 4 and 6 (six posts in Phase 6 alone) [site]: the most-revised part of the grammar. Apupiwe: any content word, any role; **gun** + action = state of the undergoer (4.7.4); no transitivity classes.

---

## 4. Vocabulary method

### 4.1 Procedure as written
Source: [Methodology for Lexical Development](https://www.globasa.net/eng/max/metode-fe-lexiseleti), [Word Proposal Process](https://www.globasa.net/eng/max/proceso-fe-lexijeni), [Q&A](https://www.globasa.net/eng/max/swal-ji-jawabu) [site].
1. **Preliminary step:** can an existing root, an affix or a compound say it? Only then propose a root.
2. **Source:** check 17 languages (English, French, German, Russian, Spanish, Mandarin, Japanese, Korean, Vietnamese, Hindi, Telugu, Arabic, Swahili, Persian, Turkish, Indonesian, Filipino) on Wiktionary, Wikipedia, print dictionaries. **Pick the form shared by the most families**, the five European languages counting as **one** family. Ties: East Asian (2+), then Arabic + support, Hindi + support, European + support, Persian + Turkish. No agreement: try other parts of speech or synonyms; then a last-resort priority list.
   - **Changed 2025-02-01** ([reddit, archived](https://web.archive.org/web/2025/https://www.reddit.com/r/Globasa/comments/1ifb8sc/word_selection_algorithm_adjustment/)): Filipino dropped ("The main purpose of Filipino was to support vastly international European words (primarily English loan words)"); the last-resort list is re-ordered by **inverting the etymological statistics** so the least-represented languages (Telugu, Vietnamese) go first; Mandarin had been low "due to its high prevalence of minimal pairs" and comes back for two-character words only. The static methodology page still lists Filipino [site, checked 2026-10-13]. A 2025 word post groups sources as European (one family), Austronesian (one family) and "others (each its own family)" ([lexiseleti: battery](https://web.archive.org/web/2025/https://www.reddit.com/r/Globasa/comments/1ilkdht/lexiseleti_battery/)).
3. **Semantics:** decide the root's part of speech by usefulness (frequency), or by what derives best: **termo** "heat" is the root, not *garme* "warm", so *termometer*, *termodo* derive cleanly. Rules for which profession words are roots and which derive (*medis* → *medisyen*; *bishop* a root).
4. **Form** — "the caveats … always trump the source selection":
   - never word-final minimal pairs v/w, s/z, m/n; never ± a consonant or vowel at a word edge unless checked against affixed words; avoid l/r, b/p, f/p, c/j, c/x, h/r pairs; avoid *any* minimal pair when there's a choice;
   - prefer 2–3 syllables, "Globasa favors three-syllable words over two-syllable words"; avoid words that look affixed;
   - **a blend may differ from some natural language by one phoneme** (two if close);
   - **avoid roots beginning le-, xa-, nun-, ger-, be-, du-** (the verb particles), added Phase 4;
   - **choose the least-used phonemes** when options are equal (e over a; m over n; l over r; d over t …): load-balancing the inventory;
   - add a final vowel "found in at least one of the major languages" (Spanish -o/-a, Swahili -i/-u, Japanese -u; Arabic nouns/verbs -u), with exceptions (8+ sources ending in a consonant keep it: *tufan*);
   - European words "favor spelling" (*rum*, not *ram*); English words favour pronunciation where Globasa can render it; Mandarin blended with Japanese/Korean/Vietnamese (-ang → o).
5. **Proposal:** anyone posts on r/Globasa ("lexiseleti: X" posts: a table of the 16 languages grouped by family, then candidate forms with family counts, e.g. "bateri, batri, baterey (9 famil), pila (4 famil), denci (3–4 famil)"); discussion; check the admin tools for homonyms and minimal pairs; add to the dictionary with the etymology in a fixed format.
6. **Blending is deliberate** (Q&A): resemble at least one source closely ("usually … only one phoneme"), spread "the burden of learning", mimic creolisation, and gain "greater selective power" to avoid minimal pairs.

### 4.2 Stated outcome
- Launch (2019-07-26): core grammar and 1,000 roots ([History](https://www.globasa.net/eng/max/histori-de-globasa)).
- Now: "over 9,000 total dictionary entries" [site, home]; "over 3,000 root words" [site, learn page]. Claim: the 500 most common roots and affixes give "basic fluency" and cover "over 90% of the words in typical Globasa texts" [site; no method given].
- Etymology stats ([Menalari](https://menalari.globasa.net/eng/estatisti-fe-lexiasel), 2026-10-13, % of roots listing the language, multi-counted): English 60.63, Spanish 56.96, French 55.62, Turkish 53.74, German 52.97, Persian 51.37, Indonesian 50.8, Russian 49.2, Japanese 46.46, Hindi 42.21, Korean 39.94, Arabic 39.3, Swahili 30.49, Vietnamese 22.7, Telugu 22.64, Mandarin 22.29. My count from the export reproduces English (1,905 of 3,131 roots with source languages = 60.8%) [data].

### 4.3 What the dictionary data shows [data]
Export `word-list.csv`, 9,516 rows: 4,811 derived, 3,220 roots, 913 proper words, 450 phrases, 91 affixes. The "500 most common" list is 469 roots + 31 affixes (tag in the export). Blocs below are mine, by origin cluster: EUR (all European), EA (Sinosphere: zh ja ko vi), ARA (Arabic, Hebrew), PER, TUR, IND (Indo-Aryan), DRA (Dravidian), MP (Austronesian), SW (Swahili).

| Measure | All 3,220 roots | 469 core roots ("500 most common") |
|---|---|---|
| First-listed source bloc (proxy for the main source) | EUR 61.5%, EA 13.2%, ARA 11.8%, IND 6.6%, MP 2.4%, rest <1% each | EUR 49.0%, EA 17.7%, ARA 17.3%, IND 7.0%, rest ≤1.5% |
| Source languages listed per root (median) | 7 | 5 |
| Roots attested in only one bloc | 477 (15%) | 112 (24%) |
| Roots in ≥10 of the 17 panel languages and ≥4 blocs (roughly Apupiwe's L4 panel bar) | 1,002 (31%) | **29 (6.2%)** |
| Mean syllables | 2.42 | 2.01 (83 one-syllable, 302 two, 81 three) |

The 29 core roots that clear an L4-like bar are internationalisms: *bus, hotel, kafe, cay, karta, komputer, kultura, maxina, mobil, sistema, filme, grupo, programa, tema, eskol, numer, turi, danse, termo, kilo, teli*, plus *haha*, *wao*. The 1,002 wide roots in the full lexicon are mostly science, chemistry, animals, products (*adrenalin, algoritma, aluminyum, ameba, antena, aorta …*).

Everyday core words come from one or two blocs, and often by a long path: **oko** "eye" is justified by Russian/Spanish/French/English *oculist*; **sui** "water" by Mandarin 水, Japanese 水 (listed as *mizu*, the native reading) and Turkish *su*; **kitabu** "book" by the Arabic sphere (Arabic, Persian, Turkish, Hindi, Swahili, Indonesian); **tiga** "three" by Hindi *tīn* + Indonesian *tiga*; **lima** "five" by Indonesian/Filipino; **ixu** "adult" by Hebrew alone; **pawbu** "run" by Mandarin alone; **side** "sit" counts Hindi, Japanese and Korean loans of English *seat* (*सीट*, *シート*, *시트*) [data, `LexiliAsel` column]. The exception proves the rule: the nursery word **mama** lists 12 languages from every bloc. So for the words a child learns first, a worldlang root is recognisable to one or two regions of the world and opaque to the rest.

**Minimal pairs** (edit distance 1: one letter substituted, added or dropped):
| | words with ≥1 minimal-pair neighbour | pairs |
|---|---|---|
| Globasa core roots, ≥2 syllables (386) | 27.2% | 94 |
| Globasa all roots (3,215) | 36.2% | 1,879 |
| Apupiwe lexicon (517) | 30.0% | 93 |

Raw minimal-pair density is about the same. Globasa enforces its "never" rule (0 word-final v/w, s/z, m/n pairs) but keeps 30 pairs from its "avoid" list (*bala/pala* strong/speak, *basa/pasa* language/pass, *fori/pori*, *hisi/risi*, *mol/mor*, *pel/per* …). Apupiwe's distinctness doesn't show in raw counts; it shows in **where the near neighbours fall**:

| Opposites (antonym lists) | edit distance 1 | 2 | 3 | ≥4 |
|---|---|---|---|---|
| Globasa root antonyms (97 pairs) | 3 (*matre/patre*, *mare/pare*, *makro/mikro*) | 20 (*bon/bur* good/bad, *max/min* more/less, *hin/den* this/that, *le/xa* past/future, *har/wal* with/without, *ex/in* out/in, *no/si*, *mama/papa*, *kal/pul* -less/-ful) | 20 | 54 |
| Apupiwe antonyms (112 pairs) | 0 | 2 | 22 | 88 |

Derived opposites in Globasa differ by one morpheme by design: *jaledin/jaxadin* yesterday/tomorrow, *nerleli/nerxali* recently/soon, *exkludi/inkludi*, *maxori/minori*. In noise, one lost syllable flips the meaning. This is exactly the failure Apupiwe's ×30 antonym weight exists to prevent (rationale §3.1, §3.5). It is the clearest measured difference between the two designs.

### 4.4 How regions are balanced
- By counting families, with Europe as one family and tie-breaks favouring East Asia, then Arabic, Hindi.
- By feedback: the etymology statistics are published, and in 2025 the last-resort list was re-ordered against them (least-represented first) (§4.1).
- Result: Europe still supplies the main source of 61.5% of roots (49% of the core), and Mandarin, the largest first language, is last in the stats (22%). Counting families rewards *diffusion*: a European word that spread by colonial, scientific or commercial borrowing scores high everywhere (*ceke* "cheque" is listed for Arabic, Hindi, Indonesian, Japanese …). Pandunia shows the same pattern, with English in 76% of etymologies (`auxlangs-parts/4-modern-auxlangs.md`).

### 4.5 Imitative words
All onomatopoeic words come from "cross-linguistic onomatopoeia" (History), tagged *kwasilexi* in the dictionary (23 roots + uses) [data]. Several are *names* built from the sound, not just sound words: **myaw** cat, **bwaw** dog, **mumu** cattle, **meme** sheep, **kwake** duck, **piu** bird, **beze** bee, **huhu** owl, **kroa** frog, **kraw** crow, **kuku** chicken; and bodily actions: **haha** laugh, **wawa** cry, **kof** cough, **acum** sneeze, **hwam** yawn, **hor** snore, **gepu** burp, **hiku** hiccup, **mwa** kiss, **glu** drink, **yam** eat (Turkish *yemek* + "yum yum, nyam nyam" in many languages), **tutum** heart, **bum** explode, **toka** knock. Many of these concepts are on Apupiwe's coverage list right now: duck (line 1), sheep (3), frog (29), baby (40), cat (42), bee (56), wolf (101), kiss (110), owl (132), knock (230) in `tests/coverage-01/part2b/roots-1500.txt`.

---

## 5. Tooling, process, governance, community

### 5.1 Tooling [site, repos]
- **Dictionary source:** a shared Google Sheet ("word list"), imported periodically by a PHP script into the Menalari dictionary app ([globasa-docs](https://github.com/Globasa-Team/globasa-docs), `user_world_list_editor.md`). Columns: word, category (root/derived/affix/phrase/proper), word class, translations (eng, epo, spa, deu, fra, rus, zho, hin, ara), tags (semantic field, list membership), **etymology in a parseable format** (natlang list with forms; derived: morphemes with `+`; `kwasilexi -` prefix for onomatopoeia; `a priori` flag), synonyms, antonyms, "compare" notes.
- **API:** CSV/JSON/YAML exports at `cdn.globasa.net/api2/` ([api2-standard.md](https://github.com/Globasa-Team/globasa-docs/blob/HEAD/api2-standard.md)); search-term indexes per language; example-sentence corpus repo (`data-example-sentences`, updated 2026-10-11).
- **Admin tools** ([menalari.globasa.net/eng/tul](https://menalari.globasa.net/eng/tul)): Translation aide (looks up each word of a text), IPA converter "for text-to-speech applications", **Find Homonyms** ("identical word pairs that would be generated with the introduction of candidate root word", i.e. across affixed forms), **Find Minimal Pairs**.
- **Learning:** Xwexi course (20 lessons), complete grammar (also PDF, EN/EO/ES), "500 most common roots" list in five parts, Doxo reader (the whole site has audio, per a 2024–25 r/Globasa post [sec, archived sidebar]), Globasawiki (300 articles, same source), recorded audio for sounds and phrases.
- **Licence:** everything public domain (CC0-style waiver) ([License](https://www.globasa.net/eng/max/izindoku)). Apupiwe is CC0 too (`LICENSE`).

### 5.2 Governance and change
- Ortega designed alone until publication; after 2019, changes came with "the help and collaboration of the auxlang community" [site].
- **Changes are batched in dated phases**, each listed with old → new forms and a rationale ([Changes and Adjustments](https://www.globasa.net/eng/max/alogi-ji-lilalogi)). Phase 5 (January 2022) set up "a language development committee": "Grammar and word-form adjustments that are deemed absolutely necessary will be voted on and made by the committee. Other than that, we may see some semantic adjustments." ([Stability](https://www.globasa.net/eng/max/andinya-de-globasa)).
- Votes are advisory in practice: the weekday vote (11–9 numeric) was overridden by the designer's argument (§3.6).
- Stability is self-assessed ("started off around 90% stable and is now about 99% stable") and demonstrated with a text in 2019 Globasa beside current Globasa ([reddit](https://www.reddit.com/r/Globasa/comments/qskclh/globasas_stability_comparison_of_original_globasa/), archived copy read).

### 5.3 Community and activity
- Discord: 493 members, 62 online (invite API, 2026-10-13) [data]. Subreddit: counts blocked to automated access. Word-selection posts ("lexiseleti: …") appeared every few days in early 2025 (archived sidebar: puppet, file, tissue, swing, sabotage, porridge, spear, yacht …) [sec].
- Lexicon growth: 1,000 roots (2019) → 3,220 (2026), about 300 roots a year.
- Speakers: no census. FrathWiki reportedly says "approximately 15 speakers" as of 2025 (search-result snippet; the page returned 403) [unverified]. No ISO 639-3 code, no Wikipedia edition (`auxlangs-parts/4-modern-auxlangs.md`).

### 5.4 Outside discussion
- vecderg, [Auxlangs](https://www.vecderg.com/articles/auxlangs): calls Globasa "the conlang closest to being the perfect auxlang"; the cost of worldlangs is that "comprehensibility is greatly reduced without study" (*te suki roso pingo*); the 10% / 50% / 100% memorisation figures for eurolang / worldlang / a priori are the author's guesses, not data. [sec]
- vecderg, [Auxlangs 2](https://www.vecderg.com/articles/auxlangs2): "English speakers should be able understand over 50% of Globasa's vocabulary and Chinese speakers over 20%" [sec, no method]. My data (§4.3) is consistent with a lopsided figure like that: English is listed for 61% of roots; Mandarin for 22%.
- [Dan Reviews Conlangs](http://throneofsalt.blogspot.com/2023/01/dan-reviews-conlangs.html) (2023): "Globasa is probably my favorite in the genre … helpful website … public domain". [sec]
- Kupsala (Pandunia's author), [Worldlangs](https://www.kupsala.net/risto/worldlangs/): lists Globasa as active; no assessment. [sec]
- No blind recognisability or comprehension study of Globasa or any worldlang was found (also `research/research_notes/Conlang design principles compared/modern-auxlangs.md`).

---

## 6. History

[site: [History](https://www.globasa.net/eng/max/histori-de-globasa), [Changes](https://www.globasa.net/eng/max/alogi-ji-lilalogi), [Stability](https://www.globasa.net/eng/max/andinya-de-globasa)]
- ~2000: Ortega, a linguistics graduate student, concludes from creoles that a world language "with a truly international lexicon and a simpler phonology and grammar than those of Esperanto" is possible. Ideas fixed early: selection methodology; phonemes familiar to ≥50% of people; no codas (later only word-final limits); no articles, no plural, gender-neutral nouns, particles not suffixes; cross-linguistic onomatopoeia; "easily distinguishable function words and avoiding minimal pairs".
- ~2009 meets Neo Patwa; July 2017 meets Pandunia, argues its phonology back to a simpler inventory, judges it unable "to disambiguate simple sentences", leaves within weeks.
- 2017–2019: year 1 on function words and affixes ("the most difficult part"); year 2 on core grammar and 1,000 roots. Names *Geokreol*, *Gayabas*, then *Globasa*. Published 2019-07-26 (Esperanto's *Unua Libro* date), aiming at ≥95% stable, "certainly not under 90%".
- **Phase 1 (2019)**, the big one (~175 old → new lines, my count in `auxlangs-parts/4`): fixes for ambiguities found in use (**-li/-mo** modifier-of-modifier; obligatory infinitive **na**; **hay** for "there is"); Sept 2019 phonology change (word-final consonants limited to nine; coda consonants allowed inside words) causing dozens of respellings, some twice (*lexi → leksiko → leksi → lexi*, *seleci → seleksi → seleti*); final vowels added to ~90 roots; roots swapped for "greater Mandarin representation" (*komerci → xangyo*, *vidwe → gwafu*, *voto → tupyo*) and then made more Japanese-like (*xangyo → xogyo*); numbers re-formed (*doy → dua*, *tin → tiga*, *car → care*, *lim → lima* …); school became a root (*xwexidom → eskol*); street lost its root (*kuca → dolo*).
- **Phase 2 (Dec 2019)**: indirect-object **tas**, **nen-**, continuative **dupul**, correlatives fused into one word, "maybe/probably" forms changed twice in a year (*abilli → bilpul → bilbil → bilpul*).
- **Phase 3 (Jul 2020)**: transitivity of verbs revised; weekdays to planets; **-xi**; **di** archaic.
- **Phase 4 (Jan 2021)**: relative pronouns replaced by **hu** to keep SVO; metric prefixes as numerals; ambitransitive verbs; verbs may not begin le-, xa-, nun-, ger-, du-; copula *is → sen*; ~36 form changes.
- **Phase 5 (Jan 2022)**: committee; one set of question words; obligatory resumptive correlative; splits of over-broad roots (*xuji* finger → *dari* digit + *xuji*; *sampo* walk → *anda* walk + *sampo* stroll; *tofa* hair → *belo* hair/fur + *tofa* head hair; *guje* → *kasiru* break + *guje* fracture).
- **Phase 6 (Jul 2023)**: **hu** only for relatives; four new systems for ambitransitive verbs; ~29 form changes.
- Pattern: grammar changes were almost all **ambiguity fixes discovered in use**; form changes were for recognisability, phonotactics, or regional balance. Splits of lumped meanings came only after use showed the lump cost meaning (Phase 5), which matches Apupiwe's ladder 1, rung 3 (split when lumping costs meaning in modern use).


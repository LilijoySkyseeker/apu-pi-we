# Globasa in depth: what Apupiwe should adopt, adapt or not

Task: `research/notes/globasa-prompt.md`. Roadmap item "Globasa in depth" (author, 2026-10-13). Working note: terse.

## Progress

- [x] Sources fetched: Globasa-Team GitHub repos cloned to `~/work/cache/globasa/` (main-pages-grav = globasa.net pages; xwexi-pages-grav = course + full grammar; globasa-docs; globasa-api; cdn-files). Dictionary export `https://cdn.globasa.net/api2/word-list.csv` (9,516 rows, 2026-10-13). Prior notes read: `research/notes/auxlangs-parts/4-modern-auxlangs.md` (Globasa section), `research/reports/Conlang design principles compared.md`.
- [x] Site pages read: design principles, methodology, word proposal, history, stability, changes (phases 1–6), Q&A, licence.
- [x] Grammar (xwexi, all 14 pages) read and summarised (§3).
- [x] Dictionary data analysed (§4.3): sources per root, core vs whole, length, minimal pairs, antonym distance; same measures on Apupiwe's lexicon. Script: `research/notes/globasa-data.py` (rerun: download the export, then `direnv exec <repo> python3 research/notes/globasa-data.py word-list.csv`).
- [x] Tooling and governance (§5).
- [x] Outside discussion (§5.4). Reddit blocks automated access; posts were read from archive.org copies.
- [x] Sections 1–6 written.
- [x] Idea table (§7, 64 rows) and the floorboard question (§8).
- [x] Summary lists (§9); roadmap entry added under "Queued for the author".
- Done 2026-10-13. Not done: the 2026-08 PDF grammar wasn't read beyond the web pages it compiles; Globasa speaker numbers remain unknown.

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
| Apupiwe antonyms (113 pairs) | 0 | 2 | 22 | 89 |

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

---

## 7. Idea by idea

Verdicts: **adopt** (take as is), **adapt** (take the idea, change the form), **test** (plausible; a cheap blind test decides), **no** (don't adopt), **same** (Apupiwe already does it; convergence noted as evidence). Goal ids from `docs/goal.md`.

### 7.1 Aim and process

| # | Globasa idea | Apupiwe now | Verdict | Reason |
|---|---|---|---|---|
| 1 | Island thought experiment: the village language of 1,000 random world settlers after three generations | Native speakers who grow up with it (P3) | same | Both are nativisation scenarios. Globasa's arguments then serve learners; Apupiwe's serve the third generation (C2). Useful as a check question: "would the island's grandchildren keep this?" |
| 2 | Speaker *and* listener ease; speech vs writing; linguist vs ordinary person, all named | B1, B2, B4 as guarantees | same | Convergent. Apupiwe's version is stricter (guarantees, not balance). |
| 3 | "Optimal balance / middle ground" between extremes | Costs minimised together (C1) | no | "Middle ground" has no stated cost function; Apupiwe's C1 does. |
| 4 | Sources weighted toward "the largest and most influential languages" | Lineages, not head counts (N3) | no | Direct conflict with N3. |
| 5 | Changes batched into dated phases with old → new tables, a stability estimate and a then-vs-now text | Design log; review-repair batch committed locally, published at the end | adapt | When the freeze returns (rationale §1.2), keep publishing batches and add an old → new form table per batch: one relearning step per release for the author and anyone learning (B10). Process, so only when learners exist (step 5). |
| 6 | A committee votes on grammar and form changes; the designer can override (weekday vote) | The author decides; agents recommend | no | Nobody to vote yet. B9 says the language doesn't try to control its evolution; a committee is control. |
| 7 | Anyone may propose a root in public; a template post lists sources by family and candidate forms with family counts | Agents propose, the author decides; panel tables in `tests/lexicon-ladder-01/` | same | Apupiwe's loan panel table is the same artefact. Public proposals need a community (trigger: one exists). |
| 8 | Etymology statistics published, and the tie-break order re-tuned against them (2025: least-represented languages first) | Panel pass rule (12/20, 4/7 regions) for loans; nothing measures balance afterwards | adapt | A one-off audit, not a dashboard: by region, whose lumps (ladder 1, rungs 3–4) and whose loans won, and which regions the coverage concept list leans on. Serves N3 and C1's "fair to every culture". Repeat only if the audit finds a lean. |
| 9 | Everything public domain | CC0 (`LICENSE`) | same | — |

### 7.2 Sounds and writing

| # | Globasa idea | Apupiwe now | Verdict | Reason |
|---|---|---|---|---|
| 10 | 20 consonants incl. /x/, tʃ, dʒ, ʃ, z, v, ɾ; clusters; 9 final consonants | 13 consonants, (C)V(n) | no | Those sounds serve source fidelity, which Apupiwe doesn't need. Fewer consonants keep place contrasts robust (B2; rationale §2); clusters cost children and many adults (B10). |
| 11 | Hard bans on minimal pairs v/w, s/z, m/n word-finally | /v/, /z/ deleted; final -n treated as the first to drift | same | Independent confirmation of the same three weak spots. |
| 12 | **Declared free variants per sound** (r as [ɾ r ɹ ʁ], h as [x χ ħ h], x as [ʃ ʂ ɕ] …); aspiration optional; w/y as vowels | Three harmless variants (2.9) | adapt | Speakers live among other languages (P4) and bring their accents; children copy them (B9). Declare, per sound, which realisations count as the same (l as [ɫ ɾ]; p t k with or without aspiration; f as [ɸ]; w as [ʋ]; s as [ʃ]?), each checked so no variant merges two sounds or two words. Cheap: the inventory is small. |
| 13 | Unwritten epenthesis: glottal stop between vowels, schwa between consonants | No clusters; hiatus only across words | adapt | Declare a glottal stop at vowel–vowel word junctions harmless (**to isi**, **pi en**), so a speaker who inserts one is still in the language (P4). Check it against juncture rules (`juncture.py`). |
| 14 | Three phonotactic tiers: ordinary words, proper names, **culture-specific words** (teriyaki, vodka, jazu) | Names keep the owner's spelling; loans fully adapted by `names.py` | adapt | The coverage tail is named dishes, diseases, objects (`coverage-01/RESULTS.md`): exactly culture-specific words. Option: treat them like names (own spelling, said as close as possible) but without **en**, or adapt them by looser rules. Fits the author's prediction that speakers will borrow freely (design log 2026-10-13) and the queued check of how the grammar handles such words. |
| 15 | Stress by word ending; y/w spelling to steer stress | Fixed initial stress | no | Apupiwe's rule needs no spelling device and marks word starts (rationale §2). |
| 16 | Capitals: no rules | Lowercase standard; capitals harmless | same | — |
| 17 | European internationalisms adapted from **spelling** (*rum*, not *ram*); English from pronunciation where possible | Loans from the panel's median pronunciation | adapt (small) | Where panel pronunciations scatter but the written form is shared, prefer the written form: P4 includes writing online, and B4 wants writing and speech to agree. Tie-breaker only. |

### 7.3 Grammar

| # | Globasa idea | Apupiwe now | Verdict | Reason |
|---|---|---|---|---|
| 18 | Two content-word classes (noun/verb, adj/adv); classless rejected as ambiguous | Classless; clear forms chosen by meaning | no | Apupiwe tested and removed word kinds as arbitrary (rationale §10). Globasa's class system needs extra rules (NPs must end in a noun; obligatory **na**; four ambitransitive classes) and was its most-revised area. Watch item: the ambiguities Globasa met are the ones to test (rows 19–21). |
| 19 | **-mo** marks a modifier of a modifier ("perfectly black hair" vs "perfect black hair", "dark red"), a Phase-1 fix for an ambiguity found in use | No rule: stacked content modifiers after a noun are unspecified | test, then adapt | A real gap (B3: a precise way must exist). Colours alone need it (grey = white + dark, method §3). Write a short blind test (dark red shirt, light blue car, naturally black hair, very tall old man) and pick the cheapest fix: a stated reading ("a second modifier describes the first"), a **fu** phrase, or a marker. |
| 20 | Obligatory infinitive **na**: *Mi suki oko* was "I like the eye" or "I like to see" | Second verb after a verb that takes an object is that object (4.2.6); any word can be a verb | test (low) | Globasa's case came from one root meaning eye and see. Apupiwe keeps such meanings apart (CLICS rates), so the risk is smaller; include two or three verb-or-noun objects in the test of row 19. |
| 21 | Ambitransitive verbs sorted into four classes (feeling, state, non-agentive, motion), each with its own reading without an object; the most-revised part of the grammar | Any word, any role; **gun** + action = undergoer's state; anything context supplies may be left out (4.5) | test | With object omission allowed, **beya tapi** "the door closes" and **wan tapi** "she closes (it)" have the same shape. Context usually decides; Globasa's six Phase-6 posts say it doesn't always. A blind test of verbs with no object (break, open, stop, move, boil, sink, interest, tire) decides whether a rule is needed (B1, B3). |
| 22 | Tense particles optional after the first; narration in the bare form | Tense optional; a frame carries (8.1) | same | Converged from opposite starting points. Evidence for Apupiwe's rule. |
| 23 | Aspect stacking: *le xa* "was going to", *xa le* "will have", *dupul* "have been doing for", *jale* "just did" | **sin**, **le**, **buntu**, **sin le**; frames | test (low) | Check that "was about to", "had just" and "have been doing for 10 years" are sayable without ambiguity; Apupiwe has the parts (**buntu** in a past frame; **sin le** + **nin**). |
| 24 | Passive **be-** with the agent as a bare object | Topic opener **pi X,**; **gun** + action word | no | WALS 107 (rationale §10): the function is covered without a passive. |
| 25 | Relative clauses: marker **hu**, normal word order, **obligatory resumptive pronoun da**, obligatory resumptive adverb for place/time (Phase 5 garden-path fix) | **man** + clause, normal order, gap; obliques keep the relation word at the clause end; resumptive only for "whose" | same (mostly) | Apupiwe's stranded relation word already marks the oblique role, so Globasa's garden path (*the city which I ate*) can't arise. Option kept in reserve: a resumptive **bu**/**wan** after the stranded relation word (**mon bu**) if a test shows clause-final relation words get lost. Typology of resumptives vs stranding not checked [unverified]. |
| 26 | Content clause **feki** distinct from relative **hu** | **wun** vs **man** | same | — |
| 27 | Yes/no **kam** initial; wh in situ; "colon questions" (*keto: kafe or cay?*) | **min**; **yu** in situ; **… lu …, yu** | same | Independent convergence on all three. |
| 28 | Words for yes and no (**si**, **no**) | Echo answers | no | Answers to negative questions flip across languages; echo answers avoid it (B1). |
| 29 | Contrastive **he** before any word | **o** focus | same | — |
| 30 | **Endearment particle ci** (*mama ci* mommy, *Jon ci* Johnny) | Nothing | adapt | Diminutive/affectionate forms are widespread and central to speech to children (Jurafsky 1996, "Universal tendencies in the semantics of the diminutive", *Language* 72(3): 533–578, over 60 languages, [ERIC](https://eric.ed.gov/?id=EJ537707); the link to child-directed speech is his central "child" sense; how much diminutives help children learn is not checked [unverified]). A function the world converges on gets a home (rationale §1.2 "convergent function, free form"); P3 makes child-directed speech core use. A two-syllable word after a noun or name, like **lanno** before it. |
| 31 | Honorifics **gao**, **kef** before titles | **lanno** | same | — |
| 32 | Apposition (*Hotel Kaliforni*, *misu doste Mark*, *lexi kursi*) | None (10.1.4) | no | Apupiwe's titles and **en** cover the same ground; the queued name gaps (names containing grammar words) are a different problem. |
| 33 | **di** marks a culture word or name homonymous with an ordinary word | **en** marks every name | no | Apupiwe's rule is stronger and simpler (B7). |
| 34 | te/to animacy; gender-neutral pronouns; plurals by vowel prefix (*mi/imi*, *te/ete*) | **wan**/**bu**; **la** | no | The vowel-prefix plurals are minimal pairs (B2). |
| 35 | Gender-neutral **atre** parent and **mapa** mom/dad beside mother/father | Mother, father; "parents" a compound; "parent" on the coverage list | same | Already queued in the coverage batch (line 963). |
| 36 | **Correlative grid** (which/this/that/some/every/no/other/same × person/thing/time/place/reason/manner/number/amount/kind/degree/owner) | Noun + determiner (**muyi**, **kemu**, **ewo**, **musu** + **yu**, **tan**, **we**, **fa** …) | adapt | Use the grid as a completeness check: every cell regular (B7), frequent cells short (B8). It answers the queued "no single word for never or often" (`roadmap.md`): see which cells are frequent enough for their own root (ladder 1, rung 5). |
| 37 | "The more …, the more …" (**folki** … **max**, … **max**) | Not in the reference | test (low) | Check sayability with **ke** + clauses; add to the grammar-gap list if it fails. |
| 38 | **SI prefixes as the number words** (kilo 10³, mega 10⁶, giga 10⁹, tera 10¹²; deci … piko) | **munno**, **tonen**, **siwin**; **kilo**, **senti**, **mili** only in units | adapt (author) | The cold review kept **tonen**/**siwin** (low severity, A3 §4.11: "million" isn't world-shared; **siwin** sidesteps the long/short-scale clash). New point: the SI prefixes are an international standard form (ladder 2, rung 1; L3), avoid the scale clash just as well, and **kilo** is already in the lexicon, so 1,000 now has two forms (**munno**, **kilo-**), a B7 cost. Lengths are equal (two syllables). Decision for the author. |
| 39 | Ordinals **-yum**, multipliers **-ple**, fractions **of-** | **mena** labels; **fi pi ka** parts | same | Same functions, analytic forms. |
| 40 | Weekdays by planet (designer overrode an 11–9 vote for numbers) | ISO 8601 numbers | no | The planetary week rests on astrology (C4: agreement on a wrong belief doesn't count) and needs five planet roots; ISO 8601 is the standard (L3). Globasa's evidence that numbering clashes (Monday is "second day" in Portuguese, Arabic, Hebrew, Greek, Vietnamese) is a known cost Apupiwe already accepted (rationale §10). |
| 41 | Abbreviations pronounced by meaning (*fmk* = *fe moy kaso*) | Chat abbreviations pass through | no | Speakers will invent these (N4, B9). |

### 7.4 Word formation

| # | Globasa idea | Apupiwe now | Verdict | Reason |
|---|---|---|---|---|
| 42 | Rich affix set (causative **-gi**, become **-cu**, start **xor-**, end **fin-**, again **ri-**, back **ru-**, opposite **pos-**, un- **nen-**, mis- **mal-**, -less **-kal**, -ful **-pul**, -like **-sim**, -able **-ible**, big/small **day-/lil-**) | Four derivation markers; phrases; roots for become (**lewe**), start (**tuko**), end (**fugi**), again (**moti**), return (**sigo**), change (**kubo**) | adapt (as a checklist) | Don't fuse (author, 2026-10-13: no fusing). Use the list as a checklist of the most-used derivational meanings and make sure each has one short, regular Apupiwe phrase (B7): "make X" (**muge** + result), "become X" (**lewe**), "start to", "un-", "mis-", "-less" (**nuwen**), "-like" (**fu**). |
| 43 | Quasi-affixes: frequent nouns as compound heads (-dom place, -tul tool, -yen person, -xey thing, -tora machine, -kamer room, -maso meat, -lari set) | **no**, **ge**, **du**, **pu**; **pi** phrases | same | Apupiwe's four markers are the same top four; others go through **pi**. |
| 44 | **Truncated morphemes**: function words clipped from content words (*cel* ← *cele*, *tas* ← *taslum*, *kom* ← *kompara*), as a memory aid | Grammar words are one-syllable, maximally distinct from everything | no | A memory aid for adults (N2). It makes grammar words near-homophones of content words (*cel/cele*: B2). Grammaticalisation will produce such links anyway (B9, `drift.md`). |
| 45 | Head-last compounds written as one word | Compounds separate, no fusing | no | Decided 2026-10-13: fusing makes writing disagree with speech or needs a compound-stress rule. |
| 46 | Body-part nouns double as sense verbs (*oko* eye/see, *ore* ear/hear) | Separate roots | no | Lump/split by lineage rates (method §3); eye/see is not a majority lump. |
| 47 | Echo-object verbs (*somno somno* "sleep a sleep") | Doubling = emphasis | no | Clashes with Apupiwe's doubling rule (1.5). |
| 48 | Choose which member of a word family is the root by what derives best (*termo* heat, not *garme* warm) | Ladder 1, rung 4: the less basic built from the other | same | — |
| 49 | Rules for which profession words are roots and which derive | **no** + verb; roots for frequent concepts | same | — |

### 7.5 Vocabulary method

| # | Globasa idea | Apupiwe now | Verdict | Reason |
|---|---|---|---|---|
| 50 | Roots drawn from 16–17 world languages, most families wins | A priori roots; loans only where the world shares a form (L4) | **no** | The floorboard question, §8. |
| 51 | Preliminary step: can an existing root, affix or compound say it? | Ladder 2, rung 3; but frequent concepts get roots | same | Globasa moved the same way: school went from compound to root (*xwexidom → eskol*); street lost its root. Evidence for the 2026-10-13 rule "frequent concepts get roots". |
| 52 | Splits of lumped roots only after use showed a cost (Phase 5: finger/digit, walk/stroll, hair/head hair) | Ladder 1, rung 3 | same | Confirms rung 3's logic: split on evidence of cost in modern use. |
| 53 | **Imitative words from cross-linguistic onomatopoeia**, including animal names (*myaw* cat, *mumu* cow, *kwake* duck, *meme* sheep, *piu* bird) and bodily actions (*haha*, *wawa*, *acum*, *mwa*, *glu*); nursery *mama*/*papa* | Onomatopoeia and baby words left out of the seed (method §1.4, with an add-back trigger); cat, duck, sheep, frog, bee, owl, wolf, kiss, baby, knock queued as new roots | **adopt** (via L4) | These are the forms the world *does* share, and they are children's first words (Wordbank), so they serve natives directly (P3, C2). Run the L4 panel test on the imitative subset of `roots-1500.txt` before Part 4 places forms; where a form passes, it is a loan by L4, with B2 checked like any loan. Links to the queued sound-symbolism item. |
| 54 | A blend must stay within one phoneme of some natural form | Panel-median pronunciation | adapt (small) | Add a check: a loan's adapted form should be recognisably one panel form, not only a median no language uses. |
| 55 | **No root may begin with a verb particle's syllable** (le-, xa-, nun-, ger-, be-, du-) (Phase 4) | Juncture rules for digits and -n; `--after/--before` only for fixed frames | **adopt** | The same haplology argument Apupiwe uses for fixed frames (method §5.3) applies to the most frequent frame of all: operator + verb. Today 11 verbs start with a pre-verbal grammar syllable: **muge** do (after **mu**), **muwo** happen, **nagu** see, **nawi** eat and **nanyo** blow (after **na** "only"), **lewe** become, **lefan** follow, **lenu** can (after **le**), **feme** feel, **febo** answer, **fesun** hunt (after **fe**) [data, `lexicon.tsv` vs `grammar.tsv`]. Apply to the ~1,000 new roots (Part 4 placement); list the existing 11 for the author, changed only if a test shows trouble. |
| 56 | Prefer the least-used phonemes when options tie (load balancing) | The optimiser minimises confusion with existing words | same | Same effect by a better route. |
| 57 | Homonym check across derived forms; minimal-pair finder | `words.py` (model-weighted, meaning-weighted), `juncture.py`, `offensive.py` | same | Apupiwe's tools are stronger. Globasa's homonym check across affixed forms has a parallel in phrasal derived words (**no** + verb phrase), already caught by juncture. |
| 58 | Root form 2–3 syllables, three preferred | Length by frequency | no | B8: frequent words short. |
| 59 | Opposites and paired meanings built by minimal contrast (*bon/bur*, *max/min*, *le/xa*, *jaledin/jaxadin*, *matre/patre*, *hin/den*) | Opposites pushed apart (×30 antonym weight) | **no** | B2. One lost sound flips the meaning; context can't catch it because both readings fit (rationale §3.1). Measured: 23 of 97 Globasa root antonym pairs within edit distance 2, against 2 of 113 in Apupiwe (§4.3). |

### 7.6 Tooling and learning

| # | Globasa idea | Apupiwe now | Verdict | Reason |
|---|---|---|---|---|
| 60 | Machine-readable dictionary with an API and structured etymology | TSV data, generated reference | same | Apupiwe's data is already machine-readable; the loan evidence lives in `tests/lexicon-ladder-01/loans.md`, not in the lexicon. Optional: a `source` column for loans (trigger: someone asks where a loan came from). |
| 61 | Glosses in 9 languages | English glosses (second gloss where ambiguous) | adapt (later) | English glosses caused real leaks (fly/fly, light; rationale §5.4). Glosses in a few panel languages would expose more of them and serve sharing. Trigger: a non-English reader, or the lexicon review pass. |
| 62 | "500 most common roots" learning list with a coverage claim (>90% of words in typical texts) | Frequency tiers 1–5 (judgement) | **adopt** | Measure it: the coverage-01 translations give running-text counts per root. "The first N roots cover X% of running words" gives the author (a real learner) a learning order and replaces judged tiers with data where they disagree (B7, B10). One script. |
| 63 | Recorded audio for every sound and phrase; IPA converter for TTS | Listening test blocked by TTS (rationale §9.4) | no (not new) | Apupiwe's rerun plan (human reader, or cloud TTS with IPA) already covers this. |
| 64 | Course, reader, wiki, multi-language site | Lessons, declaration page | no | Sharing infrastructure; build when people come (doghouse check). |

---

## 8. The floorboard question: should Apupiwe's roots come from world languages?

### 8.1 The question
Globasa takes each root's form from the world's major languages (most families wins). Apupiwe invents each root's form with an optimiser that minimises predicted mishearing (`tools/words.py`), and borrows only where the world already shares a form (L4: panel of 20 languages, a cognate everyday word in ≥12 across ≥4 of 7 regions). Should the default flip?

### 8.2 Goal item by goal item

| Item | Favours world-sourced roots? | Why |
|---|---|---|
| **B5** built from what many languages share | weakly, on a literal reading | B5 is "the method": convergence as evidence of what works, fair to every culture (C1). Applied to *forms*, convergence barely exists in the core (8.3). A worldlang root shared by one or two regions is "built from one or two", not "from many". Apupiwe applies B5 to functions and boundaries (ladder 1), where convergence is real. |
| **L4** borrow only when the world shares the form | no; L4 is the answer already | L4 says yes exactly where the world shares the form, and no elsewhere. Globasa's method borrows everywhere, so it would break L4 for most roots. Changing this means the author changing L4. |
| **B2** hard to mishear | against | Natural forms can't be placed in sound space; opposites and same-slot alternatives come out close (Globasa: 23 of 97 root antonym pairs within edit distance 2; Apupiwe 2 of 113, §4.3). Raw minimal-pair density is similar (27% vs 30% of words have a one-letter neighbour), so the B2 advantage is specifically about *which* words are neighbours. Caveat: Apupiwe's confusion model is unvalidated (rationale §11). |
| **C2** natives first; **N2** not favouring adult learners | against | A child learns *kitabu* or **kemin** equally well: the form's history means nothing to a first-language learner [me; arbitrariness of the sign]. Recognition pays only for people who already know a source language. |
| **P4** speakers live among other languages | partly for | Native Apupiwe speakers will be bilingual in a local language. Cognates help bilingual word access (cognate facilitation: faster picture naming for cognates in Spanish–Catalan bilinguals, larger in the non-dominant language; Costa, Caramazza & Sebastián-Gallés 2000, *JEP: LMC* 26(5): 1283–1296, [ref](https://www.scirp.org/reference/referencespapers?referenceid=1749429); the effect is milliseconds of retrieval time, and false friends cut the other way). But the help goes to bilinguals whose other language supplied the root: a Spanish–Apupiwe child would get it for most roots, a Yoruba–Apupiwe child for almost none. |
| **N3** don't weight cultures by size | against | Globasa's result: Europe supplies the main source of 61.5% of roots (49% of the core); English is listed for 61%, Mandarin for 22% (§4.3–4.4). Counting families still rewards words that spread by colonial and scientific borrowing. |
| **B8** brief | neutral | Globasa's core roots average 2.01 syllables, Apupiwe's 2.05 (§4.3). Globasa's full lexicon averages 2.42; Apupiwe's planned 1,500 roots are almost all two syllables. A worldlang's forms carry codas and clusters; Apupiwe's don't. Roughly a tie at the core, Apupiwe ahead in the long run. |
| **B10** any adult can learn it; the author learns it | for | The author knows only English; about 60% of Globasa roots list English. That is the honest case for world sourcing, and it is an adult-learner case (weighted down by C2, N2), and an English-speaker case (N3). |
| **B9** survives change | neutral | No evidence either way. |
| **B1** meaning gets through | depends | For first-contact adults, recognisable roots carry some meaning without study (no study measures how much, §5.4). For natives in noise, B2 decides. |

### 8.3 What the data says
- **The world doesn't share forms for core concepts.** Of Globasa's 469 most common roots, only 29 (6.2%) are listed for ≥10 of its 17 languages across ≥4 regional blocs, and those are internationalisms (*bus, hotel, kafe, cay, komputer, sistema, grupo, programa, filme*) [data, §4.3]. Apupiwe's own panel came out the same way: 9 of 22 loans passed, all currencies, units, *internet*, *camera*, *battery*, *email* (`tests/lexicon-ladder-01/loans.md`). A worldlang core therefore isn't "the shared form"; it's a choice of one region's form per word.
- **Where shared forms do exist, L4 already takes them.** In Globasa's full lexicon 31% of roots clear the L4-like bar, mostly science, technology, products, animals and foods. That is the coverage study's long tail.
- **The coverage study** (`tests/coverage-01/RESULTS.md`): exact meaning rises 84.4% → 90.2% from 517 to 1,500 roots and stops; what's left at 2,000 is "named dishes …, diseases …, specific tools and objects … Most are names, loans-to-be or rare concepts". So the remaining loss sits in exactly the area where world-shared forms are common. The ladder already sends every new concept through rung 2 (world-shared loan) before rung 4 (new root) (vocabulary-method §0); Globasa's figures suggest how many will pass: few of the first-word concepts, more of the modern frequent ones, many in the tail [me, estimate from §4.3].
- **The one core area where forms *are* shared is imitative and nursery words** (*mama* listed for 12 languages in every bloc; *myaw*, *mumu*, *kwake*, *haha*, *wawa*), and those are children's first words. Apupiwe's seed left them out (method §1.4). This is the strongest thing to take from Globasa's vocabulary (row 53).

### 8.4 What a priori costs (honestly)
- The author, and anyone sharing the language, gets no familiar forms. Every root is memorised. This is the cost the cold review called "untested" (A3 §5.11) and proposed a cross-L1 word-learning experiment to measure.
- The name says "everyone's language", and an a priori lexicon reads as no one's. Neutrality didn't win Kotava speakers (`research/reports/Conlang design principles compared.md`); recognisability didn't win Globasa many either (~490 Discord members, "approximately 15 speakers" [unverified], §5.3). Neither approach has shown it attracts people; for a thought experiment built for natives (P1, P3) that settles little.
- Globasa found its ambiguities by being used (Phase 1). Apupiwe's forms have only been checked by a model and AI readers. That is a gap in testing, not in the choice of forms.

### 8.5 Options
- **A. Keep today's rule:** a priori roots; loans by L4.
- **B. Worldlang core:** take each root's form from the panel (most regions wins), adapted to Apupiwe's sounds. Requires changing L4 (author) and accepting B2 losses in opposites; re-forms ~500 roots during the coverage batch.
- **C. A, plus four extensions taken from Globasa** (recommended). Parts, with sources:
  1. a priori roots, optimiser-placed (today; author's L4, B2);
  2. L4 checked for every concept in the coverage batch before any root is placed (today; vocabulary-method §0, rung 2);
  3. **imitative and nursery forms** go through the L4 panel like any loan (source: Globasa row 53 + Wordbank first words; **added by me**);
  4. **a culture-specific word tier** for the long tail: own spelling or looser adaptation (source: Globasa row 14 + coverage tail; **added by me**; links to the author's "speakers will borrow freely" item);
  5. optional, and the weakest: a **recognisability tie-breaker**: among optimiser forms within a small margin of the best score, prefer one that echoes a form shared by several *regions*, like the queued sound-symbolism tie-breaker and C3 (**added by me**; risk: it quietly re-imports big-language forms, N3; I'd leave it out unless the sound-symbolism study recommends a tie-breaker mechanism anyway).

**Recommendation: C, parts 1–4.** The core stays a priori because for natives the form's origin buys nothing and its placement buys distinctness every day (C2, B2), and because the world mostly doesn't share core forms (L4, N3). Globasa's real lesson is not "borrow the core" but "the world *does* share forms in two places a priori design ignores: sound words and the cultural long tail".

### 8.6 What would change the answer (add-back triggers for option B)
- A cross-L1 word-learning or listening experiment (A3 §5.11) shows world-sourced forms are learnt markedly faster by adults *of many regions* (not just Europe) **and** listening tests show opposites placed by the optimiser are not misheard less than worldlang opposites. Both, because natives weigh B2 and adults weigh learning.
- The author decides that P1's "real language its author learns and shares" outweighs C2 for the vocabulary (an author's call, not evidence).

---

## 9. Summary

### 9.1 Was the earlier comparison too shallow?
Yes, for grammar, data and tooling. `auxlangs-parts/4-modern-auxlangs.md` and the conlang report covered Globasa's aim, vocabulary algorithm, source stats, history and community, but not its grammar, its form rules (particle-syllable ban, culture-specific tier, accent table), its imitative vocabulary, or any measurement of its lexicon. The data (§4.3) is new: it shows where world sourcing helps (the tail, sound words) and where it doesn't (the core, opposites).

### 9.2 Where Globasa is plainly better today
- It has been **used**, and its grammar was repaired from use: modifier-of-modifier (-mo), infinitive marking, relative-clause garden paths, transitivity. Apupiwe has only blind AI tests.
- **Documentation for learners**: complete grammar (also PDF, three languages), course, reader with audio, dictionary in 9 languages with an API.
- **Release discipline**: batched phases with old → new lists; a published stability estimate.
- **Imitative vocabulary** and **declared accent tolerance**: two things Apupiwe hasn't designed.
- **Explicit form rules that Apupiwe lacks**: no root starting with a pre-verbal particle's syllable; a separate tier for culture-specific words.

### 9.3 The ten most important ideas to adopt or adapt
1. **Imitative and nursery forms** (*myaw*, *mumu*, *kwake*, *haha*, *mama*): panel-test the imitative subset of the coverage list before Part 4 places forms; take passing forms as loans (L4, C2, P3). (row 53)
2. **No new root starts with the syllable of a grammar word that regularly precedes it** (operators before verbs: **mu**, **le**, **sin**, **na**, **fe** …); apply in the Part 4 batch; 11 existing verbs listed for the author (method §5.3, B2). (row 55)
3. **Modifier of a modifier** ("dark red", "perfectly black hair") has no rule in Apupiwe: blind-test, then state a reading or add a marker (B3). (row 19)
4. **A verb with no object**: test whether "the door closes" vs "she closes (it)" stays clear under omission (B1, B3); Globasa's most-revised area. (row 21)
5. **Correlative grid as a completeness check**: regular forms for every determiner × time/place/person/thing/way/reason cell, short forms for frequent ones; settles the queued never/often gap (B7, B8). (row 36)
6. **Culture-specific word tier** for dishes, instruments, customs: own spelling or looser adaptation, no **en** (P4, B6, coverage tail). (row 14)
7. **Declared accent tolerance**: per sound, which realisations count as the same, each checked not to merge words; glottal stop at vowel junctions harmless (P4, B9, B2). (rows 12–13)
8. **An endearment/diminutive word** after nouns and names (*mama ci*): a function the world converges on, central to speech to children (P3, rationale "convergent function, free form"). (row 30)
9. **Measure the learning core**: "the first N roots cover X% of running words" from the coverage-01 translations, giving the author a data-based learning order (B7, B10). (row 62)
10. **A one-off regional-balance audit** of which regions' boundaries and loans won in the ladders and the coverage list, as Globasa re-tunes against its etymology stats (N3). (row 8)

Also worth the author's time, lower: SI prefixes as the number words (**kilo** is already in the lexicon, so 1,000 has two forms; row 38); old → new tables per release when the freeze returns (row 5); multi-language glosses (row 61).

### 9.4 The three most important not to adopt
1. **Root forms drawn from world languages for the core vocabulary**: the world shares few core forms (6% of Globasa's core clears an L4-like bar), the result leans European (N3), and natives gain nothing from a form's origin while losing distinctness (C2, B2). (row 50, §8)
2. **Opposites and paired meanings by minimal contrast** (*bon/bur*, *max/min*, *le/xa*, *jaledin/jaxadin*, *matre/patre*): one lost sound flips the meaning, and context can't catch it (B2). (row 59)
3. **Function words clipped from content words** (*cel* ← *cele*, *tas* ← *taslum*) as a memory aid: it helps adult learners only (N2) and creates near-homophones between grammar and content words (B2). (row 44)

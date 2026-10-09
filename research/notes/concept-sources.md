# Concept sources and data for the seed vocabulary

Research notes, 2026-10-08, for vocabulary-plan step 1. Labels: **[S]** read in a source this session; **[C]** computed this session from the downloaded data; **[I]** my inference; **UNVERIFIED** means recalled or seen only in a snippet. Numbers in brackets point to the source list.

## 1. Concepticon

**What it is.** Concepticon is a reference catalogue of "concept sets" (comparative concepts with an English gloss, a definition, a semantic field and an ontological category). Published concept lists are linked to these sets, so that "hand" in one questionnaire and "the hand" in another become the same ID [1, 2]. The latest release is v3.4.0 (Feb 2025; CLDF v3.4.2 has 4,034 concept sets and 466 lists) [2, 3]. The GitHub master (Aug 2026) has 4,164 rows, 66 of them retired, and **481 linked lists** [C].

**Lists it links** (file IDs) [C]:
- Swadesh lists: 1950-215, 1952-200, 1955-100, 1971-100 and others.
- Comrie-1977-207.
- Leipzig–Jakarta: Tadmor-2009-100.
- ASJP 40: Holman-2008-40.
- WOLD 1,460: Haspelmath-2009-1460.
- IDS 1,310: Key-2016-1310.
- NSM primes: Goddard-2001-42, Goddard-2002-59, Goddard-2011-63.
- Calude-2011-200, which has log frequencies of the 200 items in 17 languages.
- Dellert-2018-1016: basicness and stability over NorthEuraLex.
- Age-of-acquisition lists: Łuniewska-2016-299 and Łuniewska-2019-299, covering 25 and then 32 languages.
- CLICS lists: Rzymski-2020-1647 and List-2014-1280.

About 216 lists are tagged "basic". Many are Swadesh derivatives [C].

**Does it count how often a concept appears across lists?** No released table has such a column. The concept-set table in the web app has a "Representation" column, but UNVERIFIED that it is this count [4]. It takes about 10 lines to compute. Across the 481 lists, EYE appears in 358, EAR and NOSE in 343 each, and DOG in 338. 570 concept sets appear in at least 50 lists, and 255 in at least 100 [C]. **But this measures what linguists chose to ask, and most lists copy Swadesh. It is not evidence about languages.** [I]

**Useful for the boundary question.** Concepticon has 169 "X OR Y" sets (ARM OR HAND, BLUE OR GREEN, MOON OR MONTH, TREE OR WOOD) and a broader/narrower relation table (`conceptrelations.tsv`). These already record many non-English ways of dividing meanings [C].

**Format and size.** These are plain TSV files on GitHub, with releases archived on Zenodo [3]:
- `concepticon.tsv`: 486 KB.
- `conceptlists.tsv`: 270 KB.
- `conceptlists/`: 17 MB for all lists [C].

## 2. Measures of how widely a concept is named across languages

- **CLICS4** (Tjuka, Forkel, Rzymski, List 2025) [5]: 3,432 varieties, 247 families and 1,730 concepts. It was rebuilt to give a "more balanced sample covering more language families". Its `concepts.csv` already has a **Family_Count** for each concept [S, C].
  - Counts at selected ranks [C]: BLOOD is first with 246 of 247 families; rank 100 has 228, rank 250 has 174, rank 300 has 128, rank 500 has 79 and rank 800 has 63.
  - Concepts by threshold [C]: 306 concepts reach at least half the families; 498 reach at least 80.
- **Lexibank 2** [6]: 5,501 varieties, 3,205 concepts and 1.74 M forms [C]. It shows the same curve [C].
- **The coverage curve has a cliff, and it comes from how the data was collected.** [C, I]
  - Up to about rank 250–300, almost every dataset asked about the concept, so coverage tracks being named everywhere.
  - Past that point, coverage tracks *which questionnaires* reached which regions. At ranks 500–800 the lists mix FISHHOOK, KETTLE, TABLE, SOLDIER, SILVER and FISH TRAP with LICK, SMILE and SPIN.
  - A missing form usually means "not asked", not "no word". **No dataset measures how many languages lexicalize a concept past roughly the Swadesh-200 core.** [I]
- **WOLD** (41 languages, 1,460 meanings) [7, 8] scores each meaning for:
  - representation: share of the 41 languages with a counterpart;
  - simplicity/analyzability: share of monomorphemic words;
  - age;
  - borrowing.

  These scores are in `Haspelmath-2009-1460.tsv` [C]. **Simplicity bears directly on the "root vs compound" decision** [I].
- **Calude & Pagel 2011** [9]: corpus frequencies of the Swadesh 200 meanings in 17 languages from 6 families. They correlate at a mean r = 0.73, and the first component explains 70% of the variance [S]. This supports cross-linguistic frequency as a real, shared signal, but it covers only 200 meanings.
- **NoRaRe** [10] (norare-data v1.1: 126 datasets, 863 variables): frequency, AoA and other norms linked to Concepticon IDs [C]. **Its 39 languages are mostly European**, with Chinese, Turkish, Hebrew, Arabic, Persian, Malay, Swahili, Xhosa, Basque, Māori and Tok Pisin as the exceptions [C]. That makes it unsuitable as a lineage-weighted signal.
- **Łuniewska et al. 2016** [11]: AoA ratings for 299 words in 25 languages from 5 families, mostly Indo-European. The ordering is consistent across languages [S]. Use it as a tie-breaker, not as a primary signal.
- **Dellert & Buch 2018** [12]: "basicness" measured as information content over NorthEuraLex (Northern Eurasia only) [S]. Areal, so skip it.

## 3. Lineage weighting

- **Glottolog 5.3** (CLDF `languages.csv`, 2.5 MB) [13] gives each language its top-level family and one of 6 **macroareas** (Hammarström & Donohue 2014) [14].
  - Excluding the bookkeeping, sign, pidgin, mixed and artificial pseudo-families leaves about 7,674 languages in about 421 top-level lineages: 238 families and 183 isolates [C].
  - The lineages are very uneven by area [C]: Papunesia 126, South America 110, North America 75, Africa 53, Eurasia 38, Australia 33.
- **Dryer 1989** [15]: count *genera* rather than languages, and require a result to replicate in each large area independently [S]. WALS has 626 genera across 3,573 languages [C]. That a genus is about 2,500 years deep (Germanic- or Romance-level) is UNVERIFIED. **WALS 100 sample:** 67 families, 94 genera. **WALS 200 sample:** 103 families, 179 genera [C].
- **Practical count [I]:** treat a (family, macroarea) pair as one lineage. For each area, take the share of that area's sampled lineages that have a form, then average the six shares.
  - **Counting families raw would let New Guinea and the Americas dominate**, so concepts like NETBAG and SAGO would rise.
  - Area-averaging fixes that, but in the tail it lets Eurasia's IDS-style questionnaires lift KING, SOAP and AUTUMN [C, run on Lexibank]. **Either way the tail stays an artefact.**
  - Africa's low count partly reflects huge stocks such as Atlantic-Congo (1,408 languages) [C, I].

## 4. Which list to seed from

- **Swadesh lists** were built for glottochronology: stable, "culture-free" items. Swadesh's 1955 cut to 100 items explicitly "weeded out" items [16, secondary]. These lists leave out everyday needs (buy, work, cook, sick) by design [I].
- **Leipzig–Jakarta** ranks WOLD meanings for **resistance to borrowing**, with representation, age and simplicity as further factors [7, 8, S]. That answers a different question from ours ("what everyone needs to say").
- **IDS (and through it WOLD and much of CLICS)** takes its concept outline from **Buck's 1949 dictionary of Indo-European synonyms** (23 chapters; 1,310 entries adapted from about 1,200) [17, S]. **So outside the core, the inventory of concepts that were even asked about is Indo-European-framed.** [I]
- **NSM primes:** 65 in the current list [18], derived from cross-linguistic semantic analysis. Goddard 2001 reviewed about 100 candidate universals [19]. He found I, THIS, ONE and MOTHER strong, and EAT and GIVE doubtful. Critics:
  - Bohnemeyer 2003: Yucatec has no exponents of BEFORE or AFTER [20].
  - Riemer 2006: the reductive-paraphrase method itself [21].

  The primes are **the one list that covers function/logic concepts** (WANT, KNOW, BECAUSE, IF, CAN, MAYBE, LIKE), which content-word wordlists miss. Use them as a checklist, not as an authority on frequency.
- **Best seed:** the **CLICS4 concept set ranked by lineage coverage**. It is family-balanced by design, has counts precomputed, and is the same dataset the colexification step will need anyway. Add the NSM primes as a function-word checklist.

## Recommendation: data sources and procedure

**Download** (about 50 MB, no pipeline):
1. CLICS4 `cldf/concepts.csv.zip` (10.5 MB), `forms.csv.zip` (37 MB) and `languages.csv` (0.4 MB) [5].
2. Concepticon `concepticon.tsv` and `conceptrelations.tsv`.
3. From Concepticon `conceptlists/`: `Goddard-2011-63`, `Haspelmath-2009-1460` (WOLD scores) and `Luniewska-2019-299` (AoA).

**One script** (about 50 lines, stdlib only). Output is one TSV per Concepticon ID with these columns:
- (a) **area-balanced lineage coverage**: the mean over 6 macroareas of the share of that area's families that have a form;
- (b) the raw Family_Count;
- (c) the number of macroareas present;
- (d) an area-skew flag (max area share − min area share);
- (e) WOLD simplicity and representation;
- (f) mean AoA where available;
- (g) an NSM-prime flag;
- (h) related "X OR Y" sets from `conceptrelations`, for the boundary step.

**Procedure:**
1. **Core (about 250–300 concepts):** rank by (a). This is the only range where the data measures shared naming rather than shared questionnaires.
2. **Add the NSM primes** not already present, and those already covered by grammar markers.
3. **Rank 300 onward:** the CLICS4 pool, restricted to concepts present in all 6 macroareas and not area-skewed. Order by (a), with AoA and WOLD representation as tie-breakers. Treat the order as weak, and record the evidence line for each item.
4. Boundaries (lump or split) come from CLICS colexifications in the separate step.

**Proposed deletions** (each with what would bring it back):
- **Concepticon list-counts as an ordering signal.** They are circular. Add back if CLICS4 lacks a concept that tests need.
- **NoRaRe frequency norms and Dellert's measure.** They are not lineage-balanced. Add back if CLICS4 ties can't be broken.
- **Lexibank.** CLICS4 is its balanced subset with counts already computed. Add back if a needed concept is missing from CLICS4's 1,730.
- **The 500–800 seed target itself, proposed for the user to decide.** Shrink it to the **about 300 data-backed concepts plus the primes**, then go words-on-demand. Past rank 300 the "shared experience" criterion can't be measured, so ranks 300–800 would rest on questionnaire coverage. Add back the larger seed if the first blind tests lose more than 1 point to missing everyday words.

## Sources
1. List, Cysouw, Forkel 2016, LREC: https://aclanthology.org/L16-1379/
2. Concepticon: https://concepticon.clld.org ; data: https://github.com/concepticon/concepticon-data (v3.4.0, DOI 10.5281/zenodo.14923393)
3. https://github.com/concepticon/concepticon-cldf
4. https://concepticon.clld.org/parameters
5. CLICS4: https://arxiv.org/html/2503.11377 ; https://github.com/clics/clics4
6. Lexibank: https://lexibank.clld.org ; https://github.com/lexibank/lexibank-analysed ; https://zenodo.org/records/15590072
7. Tadmor, Haspelmath, Taylor 2010, Diachronica 27(2): https://www.researchgate.net/publication/216842412_Borrowability_and_the_Notion_of_Basic_Vocabulary
8. WOLD: https://wold.clld.org ; https://concepticon.clld.org/contributions/Tadmor-2009-100
9. Calude & Pagel 2011, Phil Trans R Soc B 366: https://pubmed.ncbi.nlm.nih.gov/21357232/
10. Tjuka, Forkel, List 2022, Behav Res Methods 54: https://link.springer.com/article/10.3758/s13428-021-01650-1 ; https://github.com/concepticon/norare-cldf
11. Łuniewska et al. 2016, Behav Res Methods 48: https://doi.org/10.3758/s13428-015-0636-6
12. Dellert & Buch 2018, Language Dynamics and Change 8(2) (search result only)
13. Glottolog: https://github.com/glottolog/glottolog-cldf (v5.3)
14. Macroareas: https://glottolog.org/glossary
15. Dryer 1989, Studies in Language 13: https://www.acsu.buffalo.edu/~dryer/foundation.htm
16. https://en.wikipedia.org/wiki/Swadesh_list
17. https://www.eva.mpg.de/linguistics/past-research-resources/language-history/intercontinental-dictionary-series-ids/
18. https://en.wikipedia.org/wiki/Natural_semantic_metalanguage
19. Goddard 2001, Linguistic Typology 5: https://doi.org/10.1515/lity.5.1.1
20. Bohnemeyer 2003, Theoretical Linguistics 29(3): https://www.degruyterbrill.com/document/doi/10.1515/thli.29.3.211/html
21. Riemer 2006, Linguistics and Philosophy: https://link.springer.com/article/10.1007/s10988-006-0001-4

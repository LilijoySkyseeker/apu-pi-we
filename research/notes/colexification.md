# Colexification: where concept boundaries go

Research notes, 2026-10-08. Labels: **[S]** sourced (read in this session), **[D]** computed by me from CLICS4 data this session, **[I]** my inference, **UNVERIFIED** = recalled or seen only second-hand. Bracketed numbers point to the source list at the end.

## 1. CLICS: what it is and what it can tell us

**CLICS⁴ is out** (v1.0, 2026; Tjuka, Forkel, Rzymski, List) [1][2]. The paper [2] reports 3,432 varieties (2,152 Glottocodes, **247 families**), 1,730 concepts, 1,445,845 word forms in phonetic transcription, and 3,986 colexifications. A colexification is only counted if it occurs in at least 3 families. CLICS³ [3] had 3,156 varieties, 200 families and 2,906 concepts. The release on GitHub lists 3,447 varieties [1]. [S]

**Format.** CLICS⁴ is a CLDF dataset (CSV tables plus JSON metadata), and the colexifications are now a structure dataset. `colexifications.csv` (4 MB zipped, 20 MB unzipped) gives each pair with Form, Variety, Language and **Family counts and weights**. `values.csv` (35 MB zipped, 255 MB unzipped) marks each language present or absent for each pair, counting only languages where both concepts are attested. A GML graph is also provided. [S/D] **Lineage weighting needs no pipeline.** One 15-line gawk script over `values.csv` + `languages.csv` gives a **family-balanced rate**: the mean, across families with data, of the share of each family's languages that colexify the pair. Quirk: `values.csv` holds a duplicate 0-row next to each 1-row, so take the maximum per language. [D]

**Trap: the top of the CLICS⁴ ranking is mostly an elicitation artefact.** To capture lumps like Vietnamese *tay* 'arm/hand', CLICS⁴ copies any word glossed with a broad concept (ARM OR HAND, UNCLE, BROTHER, WE, HE OR SHE, THINK, BREAK, PATH OR ROAD, …; 85 sets) onto every narrower concept it covers [2]. Of 1,445,845 forms, 107,921 are such copies [2]. A word list that only asked for "uncle" therefore records a lump even when the language splits uncles. [S] Cross-check against WALS: HE/SHE comes out lumped in **98%** (family-balanced) in CLICS⁴, but only **68%** of WALS languages (257/378) lack gender in third-person pronouns [4]. WE inclusive/exclusive: **70%** vs WALS **65%** (130/200) [5]. ARM/HAND agrees well: **35%** family-balanced (43.5% of varieties) vs WALS 37% (228/617) [6]. [D/S] **Rule: when a pair involves one of these copied concepts, treat the CLICS rate as an upper bound and cross-check it against WALS, Kinbank or the World Color Survey (WCS).** [I]

**Rates for the pairs at issue** (family-balanced %, families with data; † = pair involves a copied concept) [D]:

| Lumped by most lineages | | Split by most lineages | |
|---|---|---|---|
| DO/MAKE† | 90 (81) | ARM/HAND† | 35 (105) |
| FLESH/MEAT† | 87 (111) | BLUE/GREEN | 29 (177) |
| PATH/ROAD† | 85 (129) | SEE/LOOK; WEATHER/TIME | 24 (84); 24 (44) |
| PATERNAL/MATERNAL UNCLE† | 76 (80) | LEND/BORROW | 24 (51) |
| MOON/MONTH | 70 (75) | SUN/DAY; HEAR/UNDERSTAND | 20 (216); 20 (74) |
| LEG/FOOT† | 53 (136) | FINGER/TOE; SKIN/BARK | 16 (168); 16 (209) |
| TREE/WOOD (borderline) | 50 (85) | EAT/DRINK; BUY/SELL | 7 (240); 6 (82) |
| HEAR/LISTEN (borderline) | 45 (74) | SEE/KNOW; SMELL/HEAR | 3 (231); 1 (210) |

LEFT/RIGHT is colexified in **one** language in the whole database. [D]

**Recomputed 2026-10-12 after the fact-check (C36: "family-balanced rates could not be recomputed"; FINGER/TOE anomaly).** CLICS4 v1.0 from Zenodo (record 19608447), `clics_rates.awk` unchanged. CLICS4 pair names: LANGUAGE/WORD, SEE/KNOW (SOMETHING), SUN/DAY (NOT NIGHT). [D]

| Pair | Varieties lumping / with both concepts | Families lumping / with data | Family-balanced | Family bootstrap 95% | Families with ≥2 varieties only | Area-balanced |
|---|---|---|---|---|---|---|
| LANGUAGE/WORD (**apu**) | 116/446 | 47/71 | **50.2%** | 40–61% | 40.7% (36 fams) | 49.7% |
| MOON/MONTH (**dunan**) | 430/688 | 60/75 | **69.6%** | 61–78% | 70.8% | 77.9% |
| FINGER/TOE | 153/1026 | 39/168 | **15.7%** | 11–21% | 14.3% | 17.5% |
| EAT/DRINK | 108/2848 | 33/240 | **7.2%** | 4–10% | 4.7% | 7.6% |
| SEE/KNOW | 49/2524 | 19/231 | **2.9%** | 1–5% | 2.3% | 2.2% |

(Bootstrap: 5,000 resamples of families. Area-balanced: mean over macro-areas of the family-balanced rate. Same run reproduces the §1 table: WOOD/TREE 50.0, LEG/FOOT 53.1, ARM/HAND 34.9, BLUE/GREEN 28.8, SUN/DAY 20.0, SKIN/BARK 16.4.) None of these pairs involves a copied broad concept (`etc/split-concepts.tsv`).
- **Every claimed rate reproduces exactly.** The fact-check worked from the raw link counts, which can't give these rates (see the oddity below).
- **Thresholds:** MOON/MONTH stays well above 50% on every variant. FINGER/TOE, EAT/DRINK and SEE/KNOW stay below 20% (FINGER/TOE's upper bootstrap bound touches 21%). **LANGUAGE/WORD is a coin flip:** 49% of bootstrap resamples fall below 50%; dropping one-variety families gives 40.7%; area balancing gives 49.7%. Its point estimate is over the line, its evidence isn't. Families: Indo-European 0/63 varieties, Sino-Tibetan 16/50, Nakh-Daghestanian 7/66, Uralic 14/39; 35 of the 71 families have one variety, and 21 of those lump, each counting as 100%.
- **The raw-count oddity is explained by denominators.** CLICS's link counts (FINGER/TOE 155 forms, LANGUAGE/WORD 117) count only lumping languages. The rate divides by languages that have *both* concepts: LANGUAGE is elicited far less often, so LANGUAGE/WORD has data in 446 varieties and 71 families against FINGER/TOE's 1,026 and 168. 116 of 446 (26%) is a much larger share than 153 of 1,026 (15%), and family balancing raises it further because many of LANGUAGE/WORD's families are single lumping varieties.
- **Consequence for decisions:** **dunan** (moon = month) stands. **apu** = word + language is not settled by the rule: under the 20–50% band "language" would be built from **apu**, and the name **apu pi we** would only get longer. One root is a defensible reading; it's the author's call.

**Disagreement between sources: BLUE/GREEN.** In the WCS sample (WALS 134A, 120 languages), **71%** of languages lump green with blue in some way [7]; CLICS⁴ gives 29%. The WCS sample favours small, tropical communities, and word lists probably skip colour terms often. For colour, use the formal model, not CLICS (§4). [S/I]

## 2. Why languages colexify

- **Xu, Duong, Malt, Jiang & Srinivasan 2020** [8], ~250 languages: pairs colexified more often are more strongly associated by (English) speakers. They call this "cognitive economy": lumps follow easy mental links. [S]
- **Brochhagen & Boleda 2022** [9], >1,200 languages and 1,400 meanings from CLICS³: colexification rises with relatedness and then falls for meanings that are *too* related (Goldilocks). The mechanism is **confusability in context**. Pairs of opposites are more similar in distribution than part–whole or kind–of pairs, yet they colexify less. Their example: *left/right* are highly related, but saying "go left" makes "right" the live alternative. Caveats from the preprint [9]: the fall might only be a **plateau**, and "informativeness may exert less force than we expected". Lend/borrow still lumps in 40+ languages. [S]
- **Karjus, Blythe, Kirby, Wang & Smith 2021** [10]: in artificial-language games (10 meanings, 7 signals), paired players lumped similar meanings (e.g. drizzle/rain) by default. They **split those pairs when the pair often appeared together as the two options** (11 times vs 3). What drives the split is how often two meanings compete, not similarity itself. [S]
- **Brochhagen, Boleda, Gualdoni & Xu 2023** [11]: the same few kinds of semantic link explain children's overextensions and meaning extensions across 1,400+ languages. Lumps on these links are therefore easy to learn. [S]
- **Jackson et al. 2019** [12], 2,474 languages, 24 emotion concepts: emotion networks vary by family, and the variation follows geographic proximity. **Every family separates emotions mainly by valence (pleasant vs unpleasant) and arousal.** Few languages lump sadness with anger [13]. Some families group grief with fear and anxiety, others with regret [13]. Other family-specific examples I recall (surprise with fear in Austronesian, and so on) are UNVERIFIED. In CLICS⁴, emotion pairs are thin, about 50 families with data each: GRIEF/ANXIETY 6%, HATE/ANGER 1%. [S/D]

## 3. What this means for a designed language

Natural languages lump **when context will reliably separate the meanings** and split **when the two meanings are live alternatives in the same slot** [9][10]. That fits the stated goal, faithful transmission at a cost speakers will pay. A lump costs fidelity only where context fails, and context fails exactly for contrastive alternatives. **So the Goldilocks finding is usable, but as an override, not the main rule.** The effect is a modest tendency, and the operational measure (WordNet opposites) only covers contrasts. [I]

The designed language changes the trade-off in one respect: regular word formation makes a split cheap. A narrower sense can be a transparent derivative (FOOT = leg + end) instead of a second arbitrary root. So there are three outcomes, not two: **one root**, **root + regular derivative**, or **two roots**. [I]

## 4. Domains to handle explicitly

- **Body.** ARM/HAND 35%, split; FINGER/TOE 16%, split. LEG/FOOT 53%† is borderline once inflation is allowed for. WALS links hand/arm lumping to the tropics and to the absence of tailored clothing [6]. [S/D]
- **Kinship.** Use the formal model: Kemp & Regier 2012 [14] show that kin systems in 566 languages sit near the simplicity–informativeness frontier. Data: Kinbank, 1,229 languages [15]. Sibling and uncle rates in CLICS are inflated by the copied concepts. [S]
- **Colour.** Zaslavsky et al. 2018 [16] (information bottleneck; one trade-off parameter explains much of the variation). Do not use CLICS (§1). [S]
- **Cutting/breaking.** In 28 languages, the main dimension is **how predictable the point of separation is** (slice with a knife … smash a plate). Languages differ in the number of categories but within "a strongly constrained semantic space" [17]. Draw the boundary on that dimension. [S]
- **Putting/taking.** Kopecka & Narasimhan (eds.) 2012 [18], 18 languages, test the goal-over-source asymmetry. That languages draw finer distinctions for putting than for taking is UNVERIFIED (only the volume description was read). TAKE/GET 23%. [S/D]
- **Perception.** Majid et al. 2018 [19], 20 languages: "no single hierarchy of the senses imposes itself upon language"; smell is mostly poorly coded. SEE/KNOW is rare (3%); HEAR/UNDERSTAND is more common (20%). Evans & Wilkins 2000 [20] challenge "vision → intellect" as a universal using Australian data. That Australian languages build cognition verbs from 'hear' is my reading of the title and abstract only, UNVERIFIED. **So don't derive KNOW from SEE** (an Indo-European habit). [S/D]
- **Time/weather.** MOON/MONTH 70%, lump. SUN/DAY 20%, WEATHER/TIME 24%, split. [D]
- **Eat/drink.** 7% (240 families), split. [D]

## Recommendation: a lump/split rule for the decision procedure

For a candidate pair A/B, in order:

1. **Formal model first.** Colour, kinship, number and the spatial terms that have a published model: use the model's near-optimal system and stop. (Source: vocabulary plan.)
2. **Contrast override → two roots.** Split if A and B are frequent **alternatives in the same slot**, so that taking one for the other changes what the hearer does (left/right, buy/sell, lend/borrow, give/take). This is the author's "action-relevant misunderstanding" test, made concrete with [9][10]. Record the slot in the concept table.
3. **Otherwise follow lineages.** Use the CLICS⁴ family-balanced rate *r*; for pairs marked † or under ~30 families with data, cross-check against WALS, Kinbank or the WCS.
   - *r* ≥ 50% → **one root.** The narrow sense, when needed, is a regular derivative (MOON→MONTH, LEG→FOOT).
   - 20% ≤ *r* < 50% → **root + derivative**: two words, but the less basic one built transparently from the other (HAND→ARM, SEE→LOOK).
   - *r* < 20% → **independent roots** (EAT/DRINK, SEE/KNOW, SKIN/BARK).
4. **No single-lineage metaphors.** Never build one sense from another along a link only one lineage uses (KNOW from SEE).
5. **Evidence line**: *r*, families with data, source, any override. This is the doghouse guard in the plan.

Parts and sources: steps 1, 3 and 5 come from the plan (author + Claude). Step 2 is the author's policy, with its test taken from [9][10]. **The 50/20 thresholds, the † cross-check and step 4 are Claude's additions.** The thresholds are arbitrary cut points: add back finer bands only if blind tests show losses at a band edge.

## Sources

1. CLICS⁴ dataset, https://github.com/clics/clics4 ; https://clics.clld.org/ ; DOI https://doi.org/10.5281/zenodo.16900179
2. Tjuka et al. 2025, "Advancing the Database of Cross-Linguistic Colexifications with New Workflows and Data", IWCS, https://aclanthology.org/2025.iwcs-main.1.pdf
3. Rzymski et al. 2020, CLICS³, *Scientific Data* 7:13, https://doi.org/10.1038/s41597-019-0341-x (paywall redirect; figures via [2])
4. WALS 44A, https://wals.info/feature/44A
5. WALS 39A, https://wals.info/feature/39A
6. Brown, WALS ch. 129, https://wals.info/chapter/129
7. Kay & Maffi, WALS ch. 134, https://wals.info/chapter/134
8. Xu et al. 2020, *Cognition* 201:104280, https://doi.org/10.1016/j.cognition.2020.104280
9. Brochhagen & Boleda 2022, *Cognition* 226:105179, https://doi.org/10.1016/j.cognition.2022.105179 ; preprint read: https://osf.io/preprints/psyarxiv/efs4p/
10. Karjus et al. 2021, *Cognitive Science*, https://arxiv.org/abs/2103.11024
11. Brochhagen et al. 2023, *Science* 381:431, https://doi.org/10.1126/science.ade7981
12. Jackson et al. 2019, *Science* 366:1517, https://pubmed.ncbi.nlm.nih.gov/31857485/
13. ScienceDaily summary, https://www.sciencedaily.com/releases/2019/12/191219142735.htm
14. Kemp & Regier 2012, *Science* 336:1049, https://www.science.org/doi/10.1126/science.1218811
15. Passmore et al. 2023, Kinbank, *PLOS ONE*, https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0283218
16. Zaslavsky et al. 2018, *PNAS* 115:7937, https://doi.org/10.1073/pnas.1800521115
17. Majid et al. 2007, *Cognitive Linguistics* 18:133, https://pure.mpg.de/rest/items/item_57738_2/component/file_57739/content
18. Kopecka & Narasimhan (eds.) 2012, https://books.google.com/books/about/Events_of_Putting_and_Taking.html?id=3mlRD8SVLc8C
19. Majid et al. 2018, *PNAS* 115:11369, https://eprints.whiterose.ac.uk/id/eprint/141074/1/LoP_final.pdf
20. Evans & Wilkins 2000, *Language* 76:546, https://eric.ed.gov/?id=EJ613066

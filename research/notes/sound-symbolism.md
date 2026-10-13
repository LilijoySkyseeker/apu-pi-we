# Sound symbolism as a tie-breaker

Scope: does the evidence for systematic sound–meaning links support using sound symbolism as a second tie-breaker in `tools/words.py`, alongside C3 (avoid forms that sound like an offensive word, only between forms that cost about the same)? Prompted by `docs/roadmap.md` (2026-10-13).

Legend: **[primary]** read in the paper or a direct quote from it. **[secondary]** from an abstract, review, press release or a search/fetch summary of the paper, not the paper's full text. **[UNVERIFIED]** from memory, not checked this session.

## Progress

Single pass, complete. Literature review (Blasi et al. 2016; bouba/kiki; magnitude symbolism; early-vocabulary iconicity; ideophones), mapped onto Apupiwe's sound inventory, checked the risk against B2, and counted how many of the ~1,000 queued new roots (`tests/coverage-01/part2b/roots-1500.txt`, 983 concepts) actually fall in a domain with evidence. Recommendation: don't adopt. Nothing left open.

## 1. The evidence

### 1.1 Word-level associations across thousands of languages (Blasi, Wichmann, Hammarström, Stadler & Christiansen 2016, PNAS 113:10818)

Compared basic-vocabulary word lists (ASJP data, 100 concepts, "more than 6,000 languages and dialects" per Leiden University's release) and found that for a chunk of that list, a sound is preferred or avoided far more than chance, controlling for language family (so it isn't just shared inheritance). Reported associations include: "small" with the high-front vowel /i/; "breast" with nasals (/m/); "nose" with /n/; "tongue" with lateral /l/; "round" and "red" with /r/; "knee", "bone" and "horn" with /k/; "full" with /b/ or /p/; "leaf" with /b/, /p/ or /l/; "sand" with /s/. [secondary, press release + search summaries — I could not get PNAS's own page or PDF past a paywall/403 this session] — [PNAS record](https://pnas.org/content/113/39/10818.full), [Leiden release](https://www.universiteitleiden.nl/en/news/2016/09/evidence-for-pervasive-sound-symbolism-across-thousands-of-languages)

**Effect size:** small. Mark Liberman's direct analysis on Language Log, working from the paper's own numbers, put the biases at roughly "1.5–2.5 times" baseline frequency for the concepts involved — real and statistically solid at that sample size, but "extremely small" as a communicative effect, and nowhere near enough to let an unfamiliar listener guess a word's meaning from its sound. Liberman is also explicit that this isn't new: sound symbolism has been on linguistics syllabi since the 1960s, and the paper's own "reexamination of arbitrariness" framing, not the finding itself, is what the press overstated. [primary, direct fetch of the post] — [Language Log](https://languagelog.ldc.upenn.edu/nll/?p=28328)

### 1.2 Bouba/kiki (shape)

Köhler's 1929 observation, popularised by Ramachandran & Hubbard (2001): a rounded blob is "bouba", a spiky star is "kiki". Ćwiek et al. 2022 tested it properly cross-culturally: 917 participants, 25 languages, 9 language families, 10 writing systems. They found strong, consistent matching overall (round shape → the word with sonorants/round vowels), and — importantly — the effect was not stronger for participants whose script itself has rounder/spikier letterforms, so it isn't just reading the shape of the letters. [secondary, multiple consistent search summaries of the published paper] — [paper record](https://royalsocietypublishing.org/doi/10.1098/rstb.2020.0390), [coverage](https://www.technologynetworks.com/neuroscience/news/boubakiki-effect-tested-across-25-languages-in-new-study-356021). Earlier work (Bremner et al. 2013) found the same pattern in the Himba, a pre-literate group, which rules out familiarity with the Latin alphabet as the cause. [UNVERIFIED, from memory, not re-checked this session]

**Effect size:** this is the most robust single finding in the field — forced-choice match rates are typically in the 80–95% range in lab tasks, and it replicates in young children and across very different writing systems and an oral-only culture. It is a shape/sound association, though, not a meaning/sound association: it says nothing about which object a word should refer to, only how a word "shaped" by its sounds will be read.

### 1.3 Magnitude/size symbolism (the "frequency code")

Sapir 1929: asked people which nonsense word, *mil* or *mal*, named the bigger table; they reliably picked *mal*. Ohala's frequency code explanation: smaller larynxes/vocal tracts (and smaller animals generally) produce higher-frequency sound, so high front vowels ([i e]) and voiceless/short sounds get read as "small", low back vowels ([a o u]) and voiced/longer sounds as "large". [secondary, consistent across sources] — [Ohala's paper](http://www.linguistics.berkeley.edu/~ohala/papers/SEOUL4-symbolism.pdf)

Shinohara & Kawahara (2016) tested this with nonce words and five vowels ([i e a o u]) in four languages from different families — Chinese, English, Japanese, Korean — and found back vowels judged reliably "larger" than front vowels in all four. [secondary] — [paper](https://escholarship.org/uc/item/3ns6v23c)

**The catch, found this session:** English's own most basic pair for this very meaning runs backward. "Big" has the high vowel /ɪ/ (predicted "small"), "small" has a lower/back-ish vowel (predicted "large") — the opposite of the rule, in the two words that matter most. [secondary, search summary citing a critique] This doesn't break the cross-linguistic statistical pattern, but it is a clean demonstration that the tendency is weak enough for a single language, including possibly this one, to land on the "wrong" side for any given word.

### 1.4 Iconicity in early child vocabulary

Perry, Perlman & Lupyan (2015, PLoS ONE) had native speakers rate ~600 English and Spanish child-vocabulary words (MacArthur-Bates CDI) for iconicity. Onomatopoeia and interjections rated most iconic (M = 3.15, 2.70 on their scale), then adjectives (1.31) and verbs (1.15), then nouns (0.51) and function words (0.36) — and words rated more iconic were reliably learned earlier (b = .006, 95% CI [.003, .008]). [primary, direct fetch of the paper] — [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0137147)

Spanish verbs, though, rated much lower on iconicity than English verbs (0.74 vs 1.15) — attributed to Spanish being a verb-framed language (manner is expressed differently) versus English's satellite-framing. So even this effect is typologically contingent, not a fixed property of "verbs". Imai & Kita's "sound symbolism bootstrapping hypothesis" [UNVERIFIED, from memory] proposes iconicity helps children bootstrap early word learning before enough vocabulary exists to learn arbitrarily, which would predict the effect concentrates in the first words learned and fades — consistent with "add an iconic word only where a child needs the foothold", not with iconicity as a general design principle for an adult-learnable language (Apupiwe's P3/B10 both apply: it needs native-child-learnable **and** adult-learnable words).

### 1.5 Ideophones

Vivid sensory words (Japanese *kira-kira* "shiny/sparkly", Korean *mallang-mallang* "soft"), common in African and East/Southeast Asian languages, much rarer as a distinct word class in European ones. Dingemanse, Blasi, Lupyan, Christiansen & Monaghan (2015, Trends in Cognitive Sciences) argue iconicity is more pervasive in vocabulary than the "arbitrary sign" assumption allows, citing ideophones and signed languages as the clearest cases. [secondary] — [paper record](https://www.mpi.nl/publications/item2176289/arbitrariness-iconicity-and-systematicity-language). Dingemanse's later cross-linguistic ideophone work finds some recurring articulatory patterns (e.g. voiceless fricatives for depicting quiet/whispering sounds), strongest for sound-imitating ideophones, weaker and more language-specific for the more abstract domains (texture, shape, movement). [secondary] — [overview](https://pure.mpg.de/pubman/item/item_3012530_8/component/file_3343577/Akita_Dingemanse_2019_Ideophones_OREL.pdf)

**Relevance to Apupiwe:** ideophones are a separate word class with their own grammar (often reduplicated, outside normal syntax), which Apupiwe doesn't have and isn't proposing to add; the evidence here is suggestive for a possible future ideophone layer, not for how to pick an ordinary root's two syllables.

## 2. Mapped onto Apupiwe's sounds (vowels a e i o u; consonants p t k b d g f s m n l w y)

Only two of the above are robust enough, and general enough (not single-word facts), to state as a reusable rule:

| Association | Apupiwe sounds | Evidence | Robustness |
|---|---|---|---|
| small ~ front vowels/voiceless stops; large ~ back vowels/voiced stops | **i, e** + **p, t, k** = small; **o, u, a** + **b, d, g** = large | Sapir 1929; Ohala; Shinohara & Kawahara 2016 (4 unrelated families) | Moderate — replicates, but English's own big/small breaks it |
| round ~ sonorants/round vowels; spiky ~ voiceless stops/front vowels | **m, n, l, w** + **o, u** = round; **p, t, k** + **i, e** = spiky | Bouba/kiki, Ćwiek et al. 2022 (25 languages, 9 families, incl. a pre-literate group) | Strong, for shape judgement of invented words |

Everything else in §1 is either a single-concept fact (nose~n, tongue~l, round/red~r — and Apupiwe has no **r** at all, so that one specific, strongest-looking association can't even be used), typologically contingent (verb iconicity), or applies to a word class Apupiwe doesn't have (ideophones).

## 3. Risks

- **Conflicts with B2 (hard to mishear).** `words.py`'s cost function already penalises a candidate for sounding close to existing words (the `S` confusability matrix) and rewards shortness (`EFFORT`). Steering every "small" word toward the same narrow zone (front vowels, voiceless stops) and every "big"/"round" word toward another narrow zone is pulling in the opposite direction from spreading words apart — it would raise confusability precisely within the semantic clusters where a mishearing is most costly (a listener who mishears "tiny" for "narrow" is already primed by context to expect a small-sounding word).
- **The strongest cross-linguistic evidence is about shape judgement of made-up words in a lab, not about communicating in a real language.** Bouba/kiki and the frequency code are forced-choice tasks with two options. A spoken language carries meaning mostly through frequency, context, morphology and plain memorised arbitrary form — B1's real levers — and the one clean within-language counterexample found this session (English big/small) shows the tendency is weak enough to not even hold for the single most basic pair.
- **Partly English/Indo-European-centred, but not uniformly.** Blasi et al. and Ćwiek et al. are both explicitly cross-family and controlled for relatedness — the opposite of English-centred. But the early-vocabulary iconicity numbers (Perry et al.) are English/Spanish only and already show a typological split between them, and most of the adjacent sound-symbolism literature (Winter 2021 on English size symbolism, most ideophone depth studies) is a single-language case study. Treat the general shape/size claims as solid, the specific-word and specific-category claims as fragile.
- **Tiny effect size where it is most solid.** Liberman's reading of Blasi et al.'s own numbers (§1.1) is a 1.5–2.5× shift in a sound's baseline rate for the handful of concepts involved — real, but small next to the scale of decisions `words.py` already makes on confusability and length.

## 4. A concrete proposal (if adopted)

Mirror C3's shape ("only between forms that cost about the same"), restricted to the two associations in §2:

1. In `add_content`, after computing `best_c`, collect every candidate `(a, b)` whose cost is within a small epsilon of `best_c` (e.g. within the cost of swapping one vowel at the current tier's frequency — `EFFORT * f`, the same unit the length penalty already uses).
2. Only for glosses tagged with a magnitude sense (small/big/tiny/huge/thin/wide…) or a shape sense (round/pointy/square…) — a short, explicit list, not an automatic classifier — rank the near-tied set by whether its vowel/consonant choice matches the predicted direction in §2, and take the best match.
3. Everything else (no tag, or no candidates within epsilon) is unaffected — same as C3, never overrides a cheaper or clearer form.

This is a small, bounded addition: a fixed epsilon, a short hand-maintained tag list, and a score over two phonetic dimensions already computed by `Inventory`.

## 5. How much of the ~1,000-root batch it would touch

The classic domains (big, small, round, flat, sharp, smooth, rough, nose, smell) are **already placed** in the existing 517-root lexicon (`data/lexicon.tsv`), and `words.py`'s own rule is that existing words never move. So the tie-breaker could only act on the next ~1,000 roots queued in `docs/roadmap.md` (`tests/coverage-01/part2b/roots-1500.txt`, 983 concepts).

I checked that list directly: it is overwhelmingly concrete everyday nouns (duck, bicycle, kitchen, grandmother), kinship and professions, and modern institutional/abstract vocabulary (ministry, population, election, software, vaccine) — not size or shape adjectives. A full read found only a handful of candidates in scope at all: **giant**, **square**, **point**, and perhaps **tiny**/**huge** if those get added as separate roots rather than built from existing **big**/**small**. That's on the order of 3–6 words out of 983, under 1%, and even for those, the tie-break only fires when near-tied candidates exist at all.

## 6. Recommendation

**Don't adopt.** The two associations strong enough to state as a rule (size, shape) would touch under 1% of the queued roots, since the domains with real evidence are already locked in as existing words. Where it would apply, it pulls against B2 (spreading words apart) for a benefit (§1.1–1.3) that is itself small and partly undercut by English's own big/small pair running backward. Add back if a later listening/learnability test shows the magnitude or shape words specifically (not the vocabulary generally) are harder to learn or guess than other new roots — a narrow, testable trigger, not a general principle to design by now.

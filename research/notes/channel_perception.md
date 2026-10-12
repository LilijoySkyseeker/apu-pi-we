# Where the physical channel fails: mishearing speech and misperceiving sign

Scope: perceptual confusability in spoken and signed languages, and how natural languages build in redundancy against noise. The aim is to let a designer of a spoken and signed language choose sounds and handshapes that resist confusion.

Verification legend. **[primary]** means I read the number in the primary paper's text. **[abstract/secondary]** means it comes from an abstract, a review, or a search snippet of the paper, and I did not read the full text. **[UNVERIFIED]** means it is from memory or an uncited aggregator; treat it as a lead, not a fact.

---

## 1. Which consonant and vowel distinctions survive noise best and worst?

### Takeaway
Across 70 years of confusion studies, voicing and nasality (and, more broadly, manner) survive noise far better than place of articulation. In Miller & Nicely's data the gap was about 18 dB. Vowels are much more robust than consonants: in babble, vowel identification barely changes between 0 and 16 dB SNR, while consonant identification drops by 36 percentage points. Place contrasts that rest on weak high-frequency cues (f/θ, v/ð, and d/g after a vowel) are the first to go.

### Cited Findings
**Miller & Nicely 1955 (JASA 27:338–352) [primary, read from the PDF]**
- Design: 16 English consonants /p t k f θ s ʃ b d g v ð z ʒ m n/, each before /a/ (father). Five female talkers served as the listening crew (one talked, four listened). White noise was mixed in at S/N −18, −12, −6, 0, +6 and +12 dB with a 200–6500 Hz band, and there were 11 further low-pass and high-pass filter conditions. The 16 consonants "make up almost three quarters of the consonants we utter in normal speech and about 40 percent of all phonemes." — [Miller & Nicely 1955 PDF](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)
- Overall correct, computed from Table XX (4000 trials per condition; chance is 250, or 6.25%): −18 dB 7.8%; −12 dB 27.0%; −6 dB 46.5%; 0 dB 71.6%; +6 dB 83.4%; +12 dB 90.9%. — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)
- Per-feature correct at −12 dB (Table XX, out of 4000): voicing 3586 (89.7%; chance 50.8%), nasality 3742 (93.6%; chance 78%), place 1842 (46%; chance 35%). — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)
- Information transmitted (Table XXI, bits per stimulus, with the feature maximum in brackets). At 0 dB: voicing 0.944 [0.989] ≈ 95%; nasality 0.495 [0.544] ≈ 91%; affrication (frication) 0.620 [1.0] = 62%; duration 0.483 [0.811] ≈ 60%; place 0.578 [1.546] ≈ 37%. At −12 dB: voicing ≈ 52%, nasality ≈ 49%, place ≈ 4%. — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)
- Authors' summary: "Voicing and nasality are discriminable at signal-to-noise ratios as poor as −12 db whereas the place of articulation is hard to distinguish at ratios less than 6 db, a difference of some 18 db in efficiency." Affrication and duration fall between them: "somewhat superior to place but far inferior to voicing and nasality." — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)
- Low-pass filtering to 200–300 Hz (S/N +12) keeps about 63% of voicing information and 68% of nasality information, but only about 1.6% of place information (0.025 of 1.546 bits). Low-pass versus high-pass crossover frequencies differ by feature: nasality 450 Hz, voicing 500 Hz, affrication 750 Hz, place 1900 Hz, duration 2200 Hz. Place information sits in the high frequencies, and voicing and nasality sit in the low ones. — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)
- Noise and low-pass filtering produce consistent, structured confusions, while high-pass filtering scatters errors "quite randomly." The five features behaved like nearly independent channels: the per-feature transmissions summed to 4.890 bits against a 4-bit composite maximum, which is evidence of redundancy across features. — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)
- Mechanism given for the place weakness: /b/ (front) separates easily from /d g/, but /d/ versus /g/ "probably cannot be differentiated until their aperiodic, noisy components become sufficiently audible." For voiceless /p t k/, the F2 transition falls inside the aspiration and is "much harder to hear." — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)
- Methodological caveat: S/N was set on the VU-meter peak, which falls in the vowel, so "the consonants, which are consistently weaker than the vowel, were actually presented at much less favorable signal-to-noise ratios." — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)

**Replications and follow-ups**
- Phatak & Allen 2007 (JASA 121:2312–2326) ran 64 CV tokens (16 consonants × 4 vowels, 18 talkers) in speech-weighted noise at −22, −20, −16, −10 and −2 dB and in quiet. Low-energy obstruents, especially stops, were the most susceptible to masking, and vowels were more robust than consonants. [abstract/secondary] — [PubMed 17471744](https://pubmed.ncbi.nlm.nih.gov/17471744/); [Nature review summary](https://www.nature.com/articles/s44384-025-00032-7)
- Phatak, Lovitt & Allen 2008, "Consonant confusions in white noise" (JASA 124:1220), and Lovitt & Allen 2006, "50 years late: Repeating Miller-Nicely 1955" (Interspeech), are direct replications. I could not retrieve the full texts (403 errors), so their per-consonant figures are a gap. — [JASA abstract](https://pubs.aip.org/asa/jasa/article-abstract/124/2/1220/841322/Consonant-confusions-in-white-noise); [Lovitt & Allen 2006](https://www.isca-archive.org/interspeech_2006/lovitt06_interspeech.pdf)
- Cutler, Weber, Smits & Cooper 2004 (JASA 116:3668–3678) tested 16 American English and 16 Dutch listeners on all American English CV and VC syllables (645 syllables, one female talker) in 6-talker babble at 0, 8 and 16 dB SNR. [primary]
  - Grand means: vowels 71.1% correct and consonants 62.5%. Natives scored 73.6% and Dutch listeners 60%. By SNR: 75% at 16 dB, 69.3% at 8 dB, 56.1% at 0 dB.
  - Going from 0 to 8 dB improved vowels by only 2 points, but consonants by 24 points (natives) and 23 points (non-natives). Going from 8 to 16 dB improved vowels by 0–1 points and consonants by 12 points.
  - For native listeners, manner was transmitted most accurately and place least accurately, with voicing equal to manner. Dutch listeners transmitted voicing worst, especially word-finally, because Dutch has final devoicing. Vowel backness was transmitted better than vowel height.
  - Non-native identification ran at about 80% of native at every SNR; noise did not interact with language background.
  - Syllable-final segments were identified better than initial ones in these isolated syllables.
  - Source: [Cutler et al. 2004 PDF](https://pure.mpg.de/rest/items/item_60592/component/file_60593/content)
- Cutler et al. 2004 interpret non-natives' extra difficulty in noise as cumulative inefficiency at higher levels plus weaker use of contextual redundancy, not as worse phoneme perception. They cite Van Wijngaarden et al. 2002, in which letter-guessing entropy predicted non-native speech recognition in noise. — [Cutler et al. 2004](https://pure.mpg.de/rest/items/item_60592/component/file_60593/content)

### Inferences
- Robustness ranking for a designer, from most to least robust: vowel quality (especially backness), then nasality ≈ voicing ≈ manner (stop/fricative/nasal/approximant), then affrication/duration, then consonant place. Two consonants that differ only in place (especially coronal versus dorsal, or labiodental versus dental fricatives) form a fragile minimal contrast. Two consonants that differ in place and in manner or voicing at once are much safer.
- The near-independence of feature channels means that adding a second differing feature to a contrast multiplies robustness. Pairs that differ on several features at once (for example /m/ versus /s/) are much harder to confuse than single-feature pairs.
- Place cues live above about 1.9 kHz. Telephone bands (300–3400 Hz) keep some of them, but heavy low-pass conditions such as distance, walls or muffled speech destroy them first. Voicing and nasality survive in the band below 500 Hz.
- Non-native listeners carry their L1 gaps into the channel (Dutch final voicing). A language meant for speakers of many L1s should not rest key contrasts on features that common L1s lack, such as final voicing or /r/–/l/.

### Gaps
- Per-consonant SNR90 values and confusion groups from Phatak & Allen 2007/2008 and Lovitt & Allen 2006 were not retrievable.
- From memory, and [UNVERIFIED]: in Phatak & Allen's data /f v θ ð b/ cluster as the weakest, and /s ʃ z ʒ m n/ are among the strongest in speech-weighted noise.
- I found no single cross-linguistic Miller–Nicely replication covering non-Indo-European languages (tone languages, languages with ejectives or clicks). Cutler et al. 2004 is the only cross-language study here, and it covers only English stimuli heard by Dutch listeners.
- I did not verify vowel-confusion matrices (for example, which vowel pairs merge first in noise) beyond Cutler's "backness > height" finding.

---

## 2. Typological universals of sound inventories, and what they say about perceptual optimality

### Takeaway
Languages favor five-vowel systems built on the corners of the vowel space (/i a u/ plus /e o/). Dispersion theory reproduces 3- to 6-vowel systems well but over-predicts high central vowels in systems of 7 or more. A handful of consonants (/m k j n p t/) are near-universal. Quantal theory and dispersion both suggest that the point vowels are cheap to produce sloppily and hard to confuse.

### Cited Findings
- WALS ch. 2 (Maddieson), 564 languages: 5 vowel qualities is the modal inventory (188 languages, just over one third), followed by 6 (100 languages, 17.8%). Small (2–4) inventories: 93; average (5–6): 287; large (7–14): 184. [abstract/secondary via search] — [WALS ch. 2](https://wals.info/chapter/2); [WALS feature 2A](https://wals.info/feature/2A)
- PHOIBLE "ph" source, 913 languages (10,286 vowel phonemes, 553 types):
  - Vowel frequencies: /i/ 94.2%, /u/ 91.2%, /a/ 89.5%, /o/ 83.2%, /e/ 82.9%. The next most frequent are /ɛ/ and /ɔ/.
  - Monophthongs make up 92.4% of vowels, diphthongs 7.4% and triphthongs under 1%.
  - The most common secondary vowel features are length (2,346 occurrences) and nasalization (1,101).
  - Source: [Phonetics Speech Sci. 16(3)](https://www.eksss.org/archive/view_article?pid=pss-16-3-1)
- PHOIBLE consonants: /m/ occurs in 96% of languages, /k/ in 90% and /j/ in 90%, and /m k n j/ all exceed 90%. Plosives are the most frequent manner class, then fricatives, then nasals. [abstract/secondary; from search snippet of the article] — [Phonetics Speech Sci. 17(3)](https://www.eksss.org/archive/view_article?pid=pss-17-3-23)
- Liljencrants & Lindblom 1972 (Language 48) maximized pairwise distance in a mel-scaled F1×F2 space. They predicted 3- to 6-vowel systems essentially correctly. For systems of 7 or more they made errors, mainly too many high central vowels, "though generally not more than one per system." For seven-vowel systems the model yields two high vowels between /i/ and /u/, a pattern rare or unattested. — [Stanford Ling 205 handout (Scarborough 2005)](https://web.stanford.edu/class/linguist205/index_files/Handout%208%20-%20QT%20&%20Adaptive%20Dispersion.pdf); [Vaux & Samuels, Explaining vowel systems](https://www.repository.cam.ac.uk/bitstreams/33d7b246-292f-4af0-8712-cec157754c3f/download)
- Lindblom's later Adaptive Dispersion replaced "maximal" with "sufficient" perceptual contrast. Its acknowledged weaknesses: it does not explain inventory size, cross-language variation within a given size, or articulatory cost. — [Stanford handout](https://web.stanford.edu/class/linguist205/index_files/Handout%208%20-%20QT%20&%20Adaptive%20Dispersion.pdf)
- Stevens' Quantal Theory (1972, 1989): the articulatory-to-acoustic mapping is non-linear and has plateaus where articulation can vary without much acoustic change. [a] sits at the F1–F2 convergence, [i] at the F2–F3 convergence (palatal constriction), and [u] at a broad F2 minimum. These "quantal vowels" are predicted to be preferred, and they are. Other quantal continua are glottal state (voiceless, modal, glottal stop) and degree of constriction (vowel, glide, fricative, stop). Criticisms: the theory predicts more cross-language acoustic uniformity than is observed, and languages do not consistently exploit the tolerance for sloppiness. — [Stanford handout](https://web.stanford.edu/class/linguist205/index_files/Handout%208%20-%20QT%20&%20Adaptive%20Dispersion.pdf)

### Inferences
- A designed language that wants robustness and learnability across L1s should use the /i e a o u/ five-vowel system. It is the typological mode, every vowel in it is above 80% frequency in PHOIBLE, and its members are both quantal and dispersed. Adding central or front-rounded vowels buys inventory at the cost of the fragile height and roundness dimensions.
- The near-universal consonants (/m n k j p t/) match the robust features in section 1: nasals stand out, and voiceless stops have strong bursts. Cross-L1 familiarity and perceptual robustness point the same way.
- Dispersion theory works for small systems, which supports keeping a designed inventory small enough (≤6 vowels) that maximal-dispersion predictions hold.

### Gaps
- I did not verify exact PHOIBLE consonant percentages from the PHOIBLE site itself (snippet only), or the full L&L 1972 tables.
- I did not find quantitative tests showing that common inventories are measurably less confusable in noise than rare ones. The link is inferred from theory, not measured.

---

## 3. Functional load: which contrasts carry the lexicon, and do low-load contrasts get lost?

### Takeaway
Yes. In a cross-linguistic corpus of attested mergers, phoneme pairs that distinguish more minimal pairs were significantly less likely to have merged. Lexical properties of those minimal pairs (same syntactic category, frequency) sharpen the prediction.

### Cited Findings
- Wedel, Kaplan & Jackson 2013, "High functional load inhibits phonological contrast loss: A corpus study," Cognition 128(2):179–186. The database covers attested mergers in English, Dutch, French, German, Korean, Slovak, Spanish and Hong Kong Cantonese. The number of minimal pairs a contrast distinguishes predicts that it will not merge. [abstract/secondary] — [Sean Trott research review](https://seantrott.github.io/sound-change/); [search summary of abstract]
- Wedel, Jackson & Kaplan 2013, Language and Speech 56(3): minimal pairs in which both words share a syntactic category, and minimal pairs of particular frequency relationships, predict contrast loss better than raw minimal-pair counts. [abstract/secondary] — [Language and Speech DOI](https://doi.org/10.1177/0023830913489096)
- Related applications include the Korean /e/~/ɛ/ merger and Toronto heritage Cantonese vowel merger, both analyzed in functional-load terms. — [Springer, J East Asian Ling](https://link.springer.com/article/10.1007/s10831-018-9171-7); [Cambridge chapter](https://www.cambridge.org/core/books/abs/phonetics-and-phonology-of-heritage-languages/functional-load-and-vowel-merger-in-toronto-heritage-cantonese/564DF34AA6DC6295D5A94767EC80C5F4)

### Inferences
- For a designed language, functional load is a design variable. Contrasts that are perceptually fragile (section 1: place-only, height-only) should carry little lexical load. In particular, avoid minimal pairs that are the same part of speech and differ only in a fragile feature. Contrasts that carry heavy load should be the robust ones (manner, voicing, nasality, vowel backness).
- Natural languages show the evolutionary version of this. Fragile contrasts that carry little lexical work erode. A designed language can apply the pruning up front.

### Gaps
- I did not get the effect sizes, number of mergers, or the counterintuitive phoneme-frequency result in Wedel et al. 2013 from the full text.
- From memory, and [UNVERIFIED]: I believe phoneme frequency, controlling for minimal pairs, did not protect against merger, or even predicted merger.
- I did not find a published ranking of English (or cross-linguistic) contrasts by functional load. Older work (Hockett 1967; Surendran & Niyogi) exists but was not retrieved.

---

## 4. How much redundancy does language carry, and does it smooth information over time?

### Takeaway
Printed English is roughly 50% redundant over 8-letter windows and roughly 75% redundant once long-range context is counted. Spoken languages trade syllable rate against information per syllable and converge on about 39 bits/s (17 languages). Speakers spread information evenly, lengthening and stressing unpredictable material and reducing predictable material, which matches the channel-capacity logic of Uniform Information Density.

### Cited Findings
- Shannon 1951 ("Prediction and Entropy of Printed English," BSTJ) [primary]:
  - Statistics up to 8 letters give about 2.3 bits/letter, or roughly 50% redundancy.
  - Long-range effects up to 100 letters reduce entropy "to something of the order of one bit per letter, with a corresponding redundancy of roughly 75%," and redundancy "may be still higher" with paragraph-level structure.
  - The experimental bounds at about 100 letters are 0.6 to 1.3 bits/letter.
  - N-gram values: F0 = log2 26 = 4.7; F1 = 4.14; F2 = 3.56; F3 = 3.3. Word-based estimate: 11.82 bits/word ÷ 4.5 letters = 2.62 bits/letter.
  - Source: [Shannon 1951 PDF](https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf)
- Coupé, Oh, Dediu & Pellegrino 2019 (Science Advances 5:eaaw2594) [primary]:
  - 17 languages from 9 families, read by 170 native adult speakers (85 female).
  - Information rate: mean 39.15 bits/s, SD 5.10.
  - Speech rate: mean 6.63 syllables/s, SD 1.15, with individual speakers ranging from 4.3 to 9.1.
  - Information density per syllable, measured as word-internal syllable-bigram conditional entropy, ranges from 4.8 bits (Basque) to 8.0 bits (Vietnamese).
  - Density and rate trade off.
  - Source: [Coupé et al. 2019, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970/)
- Pellegrino, Coupé & Marsico 2011 (Language 87(3)) [primary]: 7 languages (English, French, German, Italian, Japanese, Mandarin, Spanish) with Vietnamese as reference, 59 speakers and 585 recordings of 20 parallel texts.

  | Language | Info density (ref = 1) | Syllables/s | Info rate (ref = 1) |
  |---|---|---|---|
  | English | 0.91 | 6.19 | 1.08 |
  | French | 0.74 | 7.18 | 0.99 |
  | German | 0.79 | 5.97 | 0.90 |
  | Italian | 0.72 | 6.99 | 0.96 |
  | Japanese | 0.49 | 7.84 | 0.74 |
  | Mandarin | 0.94 | 5.18 | 0.94 |
  | Spanish | 0.63 | 7.82 | 0.98 |
  | Vietnamese | 1 | 5.22 | 1 |

  The negative density–rate correlation is real, but rate is "not necessarily" constant: Japanese comes out at 0.74. — [Pellegrino et al. 2011 PDF](https://gwern.net/doc/cs/algorithm/information/2011-pellegrino.pdf)
- Aylett & Turk 2004 (Language and Speech 47(1):31–56), Smooth Signal Redundancy hypothesis: regressions on a large spontaneous-speech corpus show an inverse relation between language redundancy (predictability) and syllable duration, and a strong relation between prosodic prominence and duration. Prosodic prominence is the mechanism that keeps the overall recognition likelihood smooth. [abstract/secondary] — [Edinburgh Research Explorer](https://www.research.ed.ac.uk/en/publications/the-smooth-signal-redundancy-hypothesis-a-functional-explanation-)
- Levy & Jaeger 2007 (NIPS 19) and Jaeger 2010 (Cognitive Psychology 61:23–62), Uniform Information Density: in Switchboard, speakers more often include the optional complementizer "that" when the complement clause onset is high-information. Speakers insert redundant material at information spikes. [abstract/secondary] — [Levy & Jaeger 2007 PDF](https://www.mit.edu/~rplevy/papers/levy-jaeger-2007.pdf)
- Recent critiques question UID's generality for syntactic choices. — [PubMed 38476664](https://pubmed.ncbi.nlm.nih.gov/38476664)
- Miller & Nicely on why redundancy matters for the channel: for "isolated words, numerals, station call letters ... a miss is as good as a mile; there is no redundancy in the message to enable the listener to correct an error," whereas in connected discourse listeners "can detect perceptual errors on the basis of context." — [Miller & Nicely 1955](https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf)

### Inferences
- The roughly 39 bits/s convergence suggests a shared human processing bottleneck. A designed language should not expect to beat it by making syllables denser. Denser syllables (more contrasts per slot) must be spoken slower or will be misheard.
- Natural redundancy is uneven. It is high in running text (about 75%) but near zero for isolated tokens (names, numbers, codes). Those are exactly where natural languages fail and where radio procedure adds artificial redundancy (section 6). A designed language should build redundancy into low-context items, for example with check-syllables or longer number words.
- UID and smooth-signal results suggest a design rule: unpredictable content should get more phonetic material (length, stress, more distinctive segments), and predictable function material can be short.

### Gaps
- Shannon's estimates are for printed English letters, not phonemes. I found no comparable phoneme-level redundancy estimate across languages beyond Coupé's syllable-bigram measure, which ignores cross-word context and is therefore an upper bound on entropy.
- Sign language information rate: I found an arXiv paper on ASL entropy ([arXiv 0912.1768](https://arxiv.org/pdf/0912.1768)) but did not read it.

---

## 5. Slips of the ear and mondegreens: what natural mishearing looks like

### Takeaway
Natural mishearings mostly hit consonants, not vowels. They involve a word or short phrase, often re-segment word boundaries, and usually keep the stress pattern (stressed syllables swap with stressed syllables). Listeners experience the wrong percept as vividly as a correct one.

### Cited Findings
- Bond 1999, *Slips of the Ear: Errors in the Perception of Casual Conversation* (Academic Press), is a corpus of almost 1000 naturally occurring misperceptions classified by linguistic level (phonetic, morphological, lexical). Most affect a word or short phrase, and "listeners report hearing, as clearly and distinctly as any correctly perceived stretch of speech, something that does not correspond to the speaker's utterance." [abstract/secondary] — [Google Books](https://books.google.com/books/about/Slips_of_the_Ear.html?id=ZRd0QgAACAAJ); [Bond, Handbook of Speech Perception chapter](https://onlinelibrary.wiley.com/doi/10.1002/9780470757024.ch12)
- Two patterns, from search summaries of Bond's chapter [abstract/secondary]:
  - "Consonants are much more likely than vowels to be affected in slips of the ear, in both simple and more complex misperceptions."
  - Across word boundaries, "stressed syllables are exchanged with other stressed syllables rather than weak syllables."
  - Source: [Wiley Handbook chapter](https://onlinelibrary.wiley.com/doi/abs/10.1002/9781119184096.ch10)
- Vitevitch 2002 (Language and Speech 45(4)): naturalistic and experimental analyses show word frequency and phonological neighborhood density effects in slips of the ear. [abstract only] — [DOI](https://doi.org/10.1177/00238309020450040501)
- Marxer, Barker, Cooke et al. 2016 (JASA), "A corpus of noise-induced word misperceptions for English": 212 participants and over 300,000 token presentations yielded 3,207 consistent misperceptions. [abstract/secondary via search snippet] — [PubMed 27908057](https://pubmed.ncbi.nlm.nih.gov/27908057)

### Inferences
- Natural mishearing mirrors lab confusion data: consonants fail and vowels and stress survive. The stress and vowel skeleton is the most reliable part of the signal. A designed language could make its word-level distinctions lean heavily on vowel identity and stress position, and treat consonant place as secondary.
- Word-boundary re-segmentation (the classic mondegreen) suggests that clear word-boundary markers, such as fixed stress position or obligatory word-initial or word-final segments, would cut a whole class of errors.
- Frequency and neighborhood effects mean that words with many near-neighbors are at risk. A designed lexicon can deliberately keep phonological neighborhoods sparse.

### Gaps
- I could not access Bond's actual percentages (for example, the share of vowel versus consonant errors, or boundary errors) or the error taxonomy counts.
- From memory, and [UNVERIFIED]: Bond reports that stressed vowels are rarely misperceived, and that most errors involve one or two segments or a boundary shift.
- I did not retrieve the error-type breakdown of the Marxer/Cooke corpus.

---

## 6. Numbers and letters over radio: spelling alphabets, "niner," fifteen/fifty

### Takeaway
Radio procedure fixes a gap in natural language: isolated, context-free tokens have no redundancy. It does this by swapping letters for long, multi-syllabic, cross-lingually tested code words; by respelling digits for distinctness; and by sending numbers digit by digit. The 1956 ICAO/NATO alphabet came out of hundreds of thousands of comprehension tests across 31 nationalities.

### Cited Findings
- WWII: Harvard's Psycho-Acoustic Laboratory tested candidate words "using military interphones in the intense noise encountered in modern warfare." It found many military-list words had low intelligibility, mostly fixable by picking words from commercial codes. [secondary: Wikipedia, citing primary memos] — [Wikipedia: NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)
- ICAO criteria (Jean-Paul Vinay, Université de Montréal, 1948–49):
  1. Live words in English, French and Spanish.
  2. Easily pronounced and recognized by airmen of all languages.
  3. Good radio transmission characteristics.
  4. Similar spelling across the three languages, with the right initial letter.
  5. No objectionable meanings.

  Between 1952 and 1956, testing among speakers from 31 nations was run mainly by the UK and US governments, with the USAF Operational Applications Laboratory working through Ohio State University. [secondary] — [Wikipedia](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet); [Jean-Paul Vinay](https://en.wikipedia.org/wiki/Jean-Paul_Vinay)
- The 1951 version produced confusions "among words like Delta and Extra, and between Nectar and Victor." The 1956 revision replaced the words for C, M, N, U and X (Coca→Charlie, Metro→Mike, Nectar→November, Extra→X-ray). [secondary] — [Wikipedia](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)
- Two findings from the testing:
  - "Higher noise levels do not create confusion, but do intensify those confusions already inherent between the words in question."
  - Context changes rank order: "Football has a higher chance of being understood than Foxtrot in isolation, but Foxtrot is more often understood when combined with other words."
  - Changing one word "involves reconsideration of the whole alphabet," because a fix for one confusion can create another (1955 NATO memo).
  - [secondary] — [Wikipedia](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)
- Digit respellings and rationales:
  - "Tree" so it is not said "sri."
  - "Fower" for length, to separate it from "for."
  - "Fife," because /v/ "is easily confused with fire."
  - "Niner," with an extra syllable to keep it distinct from German "nein."
  - [secondary] — [Wikipedia](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)
- UK CAA CAP 413 Radiotelephony Manual (June 2020) [primary]: "All numbers, except [whole hundreds/thousands] shall be transmitted by pronouncing each digit separately," including callsigns, altimeter settings, flight levels, headings, wind and frequencies. The prescribed forms are WUN, TOO, TREE, FOWER, FIFE, SIX, SEVEN, AIT, NINER, TOUSAND and HUN DRED. — [CAP 413 PDF](https://skybrary.aero/sites/default/files/bookshelf/5761.pdf)
- Other explanations of "niner" exist. Some sources say it prevents confusion with "five" over a noisy radio; Wikipedia cites the German "nein." [secondary; the two claims are not mutually exclusive] — [ICAO radiotelephony search summary](https://icao4u.com/aviation-pronunciation-guide-numbers-letters/); [Wikipedia](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet)

### Inferences
- Five design principles fall out of the alphabet's history:
  1. Every token in a closed set should be multi-syllabic, so several features differ at once. (This is from the *letter* alphabet. ICAO's own digits are mostly one syllable; fower, seven and niner have two for distinctness, not for surviving a lost syllable. Don't cite it as an ICAO rule for digits; added 2026-10-12 after the fact-check, C44.)
  2. The tokens should differ in stressed-vowel and syllable-count patterns, not just in consonant place.
  3. They should be tested on the whole set at once, because confusions are pairwise.
  4. They should be tested with speakers of many L1s.
  5. They should be tested both in isolation and in context.
- "Fifteen/fifty" is a typical natural-language failure (documented for learners of English, in ESL work and a BSRLM study; not in aviation or phone research; added 2026-10-12 after the fact-check, C45). The two words differ mainly in the final syllable (/tiːn/ versus /ti/) and in stress position, which noise and accent erode. Digit-by-digit transmission gets around this by turning a weak suffix contrast into two independent, maximally distinct digit words.
- Noise intensifies existing confusions rather than creating new ones. So a confusion matrix measured at moderate noise is a valid design tool, and confusable pairs can be found before deployment.

### Gaps
- I could not find the primary Ohio State or USAF test reports with intelligibility scores per word, or published confusion data for the digits.
- I found no peer-reviewed source documenting fifteen/fifty confusion rates in air-traffic control incident data. The claim that digit-by-digit transmission prevents it is inferred from the procedure, not from measured results.
- The NATO history here rests on Wikipedia, which cites archival memos I did not read.

---

## 7. Sign languages: which parameters (handshape, location, movement) are most error-prone?

### Takeaway
Location is the most robust sign parameter: it is identified first in gating, discriminated most easily by learners, and least often slipped. Handshape and movement are the fragile ones. Handshape is the most error-prone in production slips, and movement is the hardest contrast for learners and the parameter most often misperceived in BSL nonsense-sign tasks. Because signers fixate the lower face, handshape detail on the torso is seen in low-acuity peripheral vision. ASL seems to compensate by placing rare handshapes near the face.

### Cited Findings
- Lane, Boyes-Braem & Bellugi 1976 (Cognitive Psychology 8:263–289): subjects identified ASL handshapes obscured by visual noise, and the confusion frequencies yielded similarity scores. Pairs sharing more features in their binary distinctive-feature model were confused more. Deaf signers (native and non-native) and hearing non-signers made "the same types of visual confusions," so handshape confusability is largely a property of the visual system, not of linguistic experience. [abstract/secondary] — [Semantic Scholar](https://www.semanticscholar.org/paper/Preliminaries-to-a-distinctive-feature-analysis-of-Lane-Boyes-Braem/2412293d346d5d59398440f15c718ca19badcc28); [Baker et al., PMC2730958](https://pmc.ncbi.nlm.nih.gov/articles/PMC2730958/)
- Baker, Idsardi, Golinkoff & Petitto 2005, "The perception of handshapes in ASL" (Perception & Psychophysics), compared 15 prelingually deaf native ASL signers with 15 hearing non-signers on continua between [5]–[flat-O], [B-bar]–[A-bar] and [5]–[S]:
  - Both groups put the identification boundaries in the same places.
  - Only deaf signers showed categorical-perception discrimination peaks, on the first two continua.
  - [5]–[S] showed an intermediate category ([hooked-5]).
  - Place of articulation (location) showed no categorical-perception effects.
  - [primary-ish: PMC full text, summarized] — [PMC2730958](https://pmc.ncbi.nlm.nih.gov/articles/PMC2730958/)
- Emmorey & Corina 1990 (Perceptual and Motor Skills 71:1227), gating study: location is identified first, then handshape, then movement, and identifying the movement completes recognition. Signs were isolated at about 240 ms on average and recognized with confidence at about 310 ms. [secondary via citing papers] — [DOI](https://doi.org/10.2466/pms.1990.71.3f.1227); [Frontiers 2021 citing summary](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.655168/xml)
- Bochner et al. 2011 (Language Learning 61(4)) tested 127 hearing ASL learners (beginning and intermediate) and 10 Deaf native signers on sentence-embedded minimal pairs in five categories. Movement contrasts were the most difficult, location contrasts the easiest, and handshape, orientation and complex morphology fell in between. L2 learners found movement and handshape harder than orientation and location. [abstract/secondary] — [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9922.2011.00671.x); [ResearchGate](https://www.researchgate.net/publication/263066368_When_Is_a_Difference_Really_Different_Learners'_Discrimination_of_Linguistic_Contrasts_in_American_Sign_Language)
- Orfanidou, Adam, McQueen & Morgan 2009 (Memory & Cognition 37:302–315): when deaf BSL signers misperceived nonsense signs as real signs, "the most salient parameter, movement, is the most likely to be misperceived." [abstract/secondary] — [Springer](https://link.springer.com/article/10.3758/mc.37.3.302)
- Orfanidou et al. 2010 (Journal of Memory and Language 62:272–283), a related BSL segmentation study: false alarms (nonsense signs reported as real) occurred on 678 trials, 20%. Every BSL sign must have a handshape, location and movement. [primary] — [MPI PDF](https://pure.mpg.de/rest/items/item_143949_12/component/file_385001/content)
- Newkirk, Klima, Pedersen & Bellugi 1980, "Linguistic evidence from slips of the hand" (in Fromkin, ed., *Errors in Linguistic Performance*, pp. 165–197): handshape is the parameter most prone to slips of the hand in ASL production. [secondary] — [search summary citing Newkirk et al.](https://www.researchgate.net/publication/369112456_Development_of_sign_phonology_in_Kata_Kolok)
- Gaze and acuity: perceivers look almost exclusively at the lower face, so signs articulated away from the face are perceived in peripheral vision. In a peripheral handshape-identification task, deaf signers were more accurate than hearing non-signers, near periphery was better than far periphery, and real signs were identified better than non-signs (a "sign superiority effect"). — [PMC7887614](https://pmc.ncbi.nlm.nih.gov/articles/PMC7887614/)
- Caselli, Emmorey & Cohen-Goldberg 2022, "Perceptual optimization of language: Evidence from ASL" (Cognition): frequent signs tend to be articulated farther from the face than infrequent ones, and frequent signs with rare handshapes sit closer to the face than frequent signs with common handshapes. Lexical predictability buys tolerance for low-acuity placement. [abstract/secondary; full text 403] — [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0010027722000282); [phys.org](https://phys.org/news/2022-03-american-language-people-easier.html)
- Yin, Regier & Klein 2024 (arXiv 2406.04024) used ASL-LEX: 2,723 signs and about 45 handshapes, with frequency ratings from 25 Deaf signers.
  - In native signs, handshape frequency correlates negatively with finger-independence effort (r = −0.46, p = 0.04). Borrowed or fingerspelled signs show no such correlation (r = −0.06).
  - English letter confusability shows only a weak relation to handshape distance (r = −0.19).
  - Handshape distance was operationalized as the mean angular difference between corresponding joints.
  - [preprint] — [arXiv](https://arxiv.org/html/2406.04024v1)

### Inferences
- Robustness ranking for a signed surface, from most to least robust: location (large-scale, seen even peripherally, identified first), then orientation, then handshape (fine finger detail, peripheral, most slips), with movement fragile for perception by non-natives and for nonsense-sign mapping.
- There is a modality twist. Movement is the most salient parameter, the sign equivalent of the vowel or syllable nucleus, yet the BSL and learner data show it is the most misperceived. It may carry many fine distinctions (manner, repetition, size). Coarse movement categories (straight, arc, circle, none) are probably safe, while fine movement distinctions are not.
- This is the visual analogue of Miller & Nicely's "place is fragile, manner is robust": coarse, large-scale contrasts (location regions, major movement type) survive degradation, and fine contrasts (finger configuration, subtle movement manner) fail first. Lane et al.'s finding that confusions are the same for signers and non-signers means a handshape confusion matrix is a property of human vision and can be reused across user populations.
- Design rules that follow:
  1. Carry high-load lexical contrasts on location and gross movement.
  2. Use a small, maximally distinct handshape set (fully open, fist, single extended finger, and so on).
  3. Place any fine handshape contrasts near the face, where foveal vision falls, as ASL does with rare handshapes.
  4. Make the signed number system rely on location and movement as well as finger count.

### Gaps
- I found no study of sign perception with measured accuracy as a function of viewing distance, video resolution or frame rate. Point-light and low-bandwidth studies exist ("Perceiving minimal distinctions in ASL under normal and point-light display conditions," [Springer](https://link.springer.com/article/10.3758/BF03206238); fingerspelling via point-light, [PMC9380947](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9380947/)), but I did not retrieve their numbers.
- I could not get the Lane et al. 1976 handshape count, subject numbers, or the full confusion matrix. Stungis 1981 (Perception & Psychophysics, "Identification and discrimination of handshape in ASL") was likewise not read: [Springer](https://link.springer.com/article/10.3758/BF03207293).
- I could not get the per-parameter error percentages from Newkirk et al. 1980 or from Orfanidou et al. 2009.
- Non-manual channels (facial grammar, mouthing) and their robustness were not covered.
- I found no sign equivalent of a Miller–Nicely feature-transmission study with systematic visual noise across all parameters at once.

# Confusion data for the mishearing model (v2)

## Progress

- 2026-10-13: **done** (§1–7). Model v2 proposed in §5, parameters in `confusion-data/model-v2-params.tsv`, robustness method §6, open uncertainties §7. `tools/confusion.py` not changed: implementing v2 is the next step, after the author decides (§5 parts marked "added by me" and the aspiration question in §7.1).
- Data files in `confusion-data/`: source matrices (`cooke2008-*`, `cutler2004-*`, `yu-do2024-mandarin-*`, each with a `# source:` line), projections onto Apupiwe's consonants (`proj-*.tsv`, by `project.py`; run `python3 project.py 0.2`), typology gaps (`phoible_gaps.py`, needs PHOIBLE's `data/phoible.csv`).
- Not reached: Wang & Bilger 1973 and Phatak & Allen 2007 matrices (paywall/403); no open five-vowel noise matrix; no rates for glide-hiatus or -n resegmentation. If resumed: try Felty et al. 2013 supplementary data (coda -n deletion rates in words), Gibson et al. 2026 full text (Spanish five vowels), Moreno-Torres 2017 matrices (Spanish /ʝ l m n/).
- Prior work reused, not redone: `channel_perception.md` §1.
- 2026-10-15: **done** §8, the face-to-face (audiovisual) listener: sources `vonseth2025-*`, `braida1998-japanese-*`, projections `proj-av-*.tsv` by `project_av.py`, variant `src-av` in `tools/confusion2.py`. Short-word rerun with it not done.
- 2026-10-15: **done** §9, the listener without high frequencies (low-pass): sources `mn55-lowpass-{1200,2500,5000}.tsv`, `mn55-noise-{0dB,6dB}.tsv` (Miller & Nicely 1955 Tables X–XII, IV, V), check `trevino2013-HI-avg.tsv`, projections `proj-lp-*.tsv` by `project_lowpass.py`, variant `src-lp` in `tools/confusion2.py`. Short-word rerun with it not done.

## 1. Consonant confusions in noise (multi-L1)

### 1.1 Cooke & Scharenborg 2008, Interspeech Consonant Challenge [primary, read from PDF]
- 24 British English consonants in VCV (vowels /i: u: æ/, both stress positions), 8 test talkers; 23 native British listeners reported (27 tested). Noise test sets: competing talker −6 dB, 8-talker babble −2 dB, SSN −6 dB, factory 0 dB, modulated SSN −6 dB, 3-talker babble −3 dB. Native scores (Table 2): clean 93.8%, noise sets 79.5, 76.5, 72.2, 66.7, 79.2, 71.4%.
- Fig. 3 prints full 24×24 percent matrices for clean and for the average over noise conditions: `confusion-data/cooke2008-native-{clean,noise}.tsv`. Row p sums to 104 in the printed figure (rounding or a print error; renormalize).
- Noise-averaged, for our approximants (percent, row = sent): l→l 84, r 3, w 2, b 2, v 2, n 2; w→w 78, r 7, b 3, v 3, y 2, l 2; y(j)→y 80, g 4, l 3, ng 3. So in English ears at ≈ −6 to 0 dB, l/w/j are about as robust as the nasals (m 73, n 68) and better than the stops p 69, b 64; their errors go mostly to other sonorants (w→r, l→r/n) and to b/v (for w) and g (for j).
- Authors: "As a group, the sibilants were typically well identified while /f, v, th, dh, b, ng/ presented most difficulties"; "/b/ and /v/ are often confused"; "/v/ is the most reported sound in noise (1.56 times its actual rate of occurrence)".
- Voicing, place and manner are "equally-well transmitted" averaged over most noise sets; voicing is "particularly adversely affected by stationary noise".

### 1.2 Cooke, García Lecumberri, Scharenborg & van Dommelen 2010, Speech Communication 52:954–967 [primary, read from PDF]
- Same British VCV corpus; 178 listeners of 8 L1s (English 23, Czech 18, Dutch 15, German 18, Italian 18, Norwegian 21, Romanian 26, Spanish 39); maskers SSN, speech-modulated noise, competing speaker. PDF text gives the SNR as "6 dB" (likely −6 dB with a lost minus sign; unverified).
- Key result: "A significant degree of similarity in the response to many of these factors was evident across all eight language groups, suggesting that acoustic and auditory considerations play a large rôle in determining intelligibility. Language-specific influences were observed in the rankings of individual consonants".
- Kendall's W across the 8 groups (Table 3): consonant ranking 0.74 (SSN), 0.67 (CS), 0.67 (SMN), mean 0.69 — the least L1-independent factor; phonetic feature 1.00/0.64/0.96.
- "Voice is the least well-transmitted feature for all language groups and maskers." Sibilants and /t/ well recognised by most groups; "weak fricatives /θ,ð,f,v/ and /p/ were particularly problematic for most listeners." L1 effects: /z/ poor for Spanish (no voiced fricative phonemes), "German listeners have particular problems with /w/".
- Native per-consonant scores range "from around 36% to 94%". Per-L1 per-consonant scores are only in a scatter figure (Fig. 5), not extractable reliably.
- Vowel context: /æ/ as the second vowel gives the best consonant scores; /i:_i:/ and /u:_u:/ the lowest (all groups).

### 1.3 Cutler, Cooke, García Lecumberri & Pasveer 2007, Interspeech, "L2 consonant identification in noise: cross-language comparisons" [primary, read from PDF]
- 23 American English consonants (Shannon et al. VCV /a_a/), 10 talkers; 53 Spanish, 24 Dutch, 12 British listeners; quiet, competing talker 0 dB, SSN 0 dB.
- Spanish listeners scored 91% of L1 in quiet, 87% with a competing talker, 83% in SSN; Dutch 82%, 82%, 76%. "performance on the laterals and nasals in quiet is, for both L2 groups, hardly worse than L1 performance, while performance on the fricatives is, again for both groups, clearly worse".
- Cites García Lecumberri & Cooke 2006: Spanish L2 = 92% of L1 without masker, 78–90% at 0 dB with maskers; Cutler et al. 2004: Dutch L2 ≈ 80% of L1 at 16 to 0 dB.

### 1.4 Lovitt & Allen 2006, "50 years late: repeating Miller–Nicely 1955", Interspeech [primary, read from PDF]
- Same 16 consonants + /a/, 18 talkers from the LDC Articulation Index corpus, 26 untrained-ish native US listeners, recorded tokens, a "noise only" button. Relative information transmitted (Table 2):

  | feature | MN55 −6 dB | MN05 −6 dB | MN55 0 dB | MN05 0 dB |
  |---|---|---|---|---|
  | voicing | .806 | .372 | .955 | .528 |
  | nasality | .730 | .750 | .910 | .906 |
  | place | .161 | .328 | .373 | .643 |
- "In the repeat experiment the voicing feature is less robust whereas the place feature is more robust." Voicing errors dominate s/z, f/v, θ/ð and the /b/ group (b, v, f, θ, ð) at high SNRs. Authors suspect MN55's crew (highly trained, listening to each other live, forced to guess) inflated voicing.
- **Consequence for the model:** `confusion.py` uses MN55, whose voicing transmission is the high outlier. Cooke 2008 (§1.1) and Cooke 2010 ("Voice is the least well-transmitted feature for all language groups") agree with MN05. MN55 understates voicing confusions and overstates place confusions.

### 1.5 Cutler, Weber, Smits & Cooper 2004, JASA 116:3668–3678 [primary, read from PDF; tables extracted]
- 16 American and 16 Dutch listeners; all American English CV and VC syllables, one female talker, 6-talker babble at 0, 8, 16 dB. Tables I–VIII print full 0 dB matrices (percent; "Where rows do not sum to 100%, the remainder was missing data"; "No response ('miss') was registered on in total 0.64%"). Extracted to `cutler2004-{native,dutch}-{initial,final}-{consonants,vowels}.tsv` by PDF word positions; Table I checked against a rendered page image; Table VIII re-parsed from layout text after the position parse dropped two columns (row sums now 99.8–100.2).
- Initial (CV, after silence) consonants at 0 dB are very poorly identified by both groups (natives: p 15.4%, t 19.6, k 25.8, b 19.6, d 14.6, g 29.6; m 63.8, n 77.9, l 54.2, j 65.8, w 73.3). The voiceless stops go mostly to **/h/**: p→h 39.2%, t→h 27.9, k→h 27.9, f→h 14.2 (natives); Dutch similar. With no /h/ in Apupiwe, that is a "heard no consonant" outcome, but only word-initially after a pause: in VCV (Cooke 2008) p→h is 3%, t→h 0, k→h 2.
- Native and Dutch per-phoneme accuracy correlate r = 0.83 / 0.87 / 0.91 at 16 / 8 / 0 dB: "the phonemes which were most difficult for non-native listeners were also difficult for native listeners".
- Dutch listeners: "Dutch phonotactics prohibit voicing contrasts in final position, and the Dutch listeners made many more voicing errors on final consonants such as /b, d, g/ than native listeners did."
- Vowels: "Vowel backness was transmitted better than vowel height" (both groups; height better than tenseness).

### 1.6 Yu & Do 2024, Mandarin onsets, Data in Brief 52:109868 [primary data, downloaded from OSF]
- 47 native Mandarin listeners (online), all 23 Mandarin onsets incl. /l w j/, rimes a/an/ang, white noise; quiet, +12 dB, +6 dB. Matrices: `yu-do2024-mandarin-{quiet,snr12,snr6}.tsv` (counts, 360 per row).
- Overall onset accuracy (computed): quiet 93.0%, +12 dB 82.1%, +6 dB 75.8%. At +6 dB, for the onsets that map to ours: pinyin b(/p/) 53%, p(/pʰ/) 38, d 52, t 56, g 79, k 54, f 76, s 92, m 76, n 80, l 75, y(/j/) 81, w 84.
- The non-European data point for /l w j/: at +6 dB l→n 10%, l→r 11%; n→m 10%, n→l 6%; m→n 19%; w→g 12%, w→d 2.5%; y(/j/)→/tɕ/ 7%, →r 5%. Aspiration (Mandarin's laryngeal contrast) is almost never confused (b↔p 4 and 0 of 360), but white noise turns unaspirated /p/ into /f/ (106/360 = 29%).
- Note: white noise masks high frequencies most; speech-shaped noise and babble (Cooke, Cutler) are more realistic. The f↔b effect is likely masker-specific.

### 1.7 Other native-language studies (abstracts or partial text only)
- Spanish (Moreno-Torres et al. 2017, JASA 141:3079; 16 Spanish consonants × 5 vowels, 8-talker babble −6/−2/+2 dB) [abstract via PubMed E-utilities]: resistance groups "(1) high resistance: /ʧ, s, ʝ/; (2) mid resistance: /r, l, m, n/; and (3) low resistance: /t, θ, x, ɡ, b, d, k, f, p/. Confusions involved mostly place of articulation and voicing errors"; confusion groups "/f, θ, x/", "the six stops", and "/m, n, l/". Full matrices paywalled (403).
- Malayalam listeners (Kalaiah et al. 2020, Noise & Health; 16 consonants incl. /l r/, VCV /a/, SSN +8/0/−8 dB) [PMC, text only, numbers in figures]: "transfer of information was highest for consonant feature manner of articulation and lowest for voicing, across listening conditions".
- French, natural noise at −8.8 to −18.4 dB, monosyllabic words (Meyer, Dentel & Meunier 2013, PLoS ONE 8:e79279) [primary, via WebFetch summary of the article page]: vowels 91.5% correct; "Among the 8.5% of errors, a great majority was due to an absence of a response (deletions) (85%) and much fewer were due to confusions with other vowels (15%)"; consonants 70.3%; most frequent consonant confusions "[f] was taken for a [p], [p] was taken for a [b], [k] was taken for a [g]".
- Not found/accessible: Wang & Bilger 1973 matrices (paywalled, no open copy found); Phatak & Allen 2007 (403 from both hosts); any African, Arabic, Hindi or Japanese native-language matrix with open data (Malay 22-consonant study exists on ResearchGate, not read).

### 1.8 What the sources say about Apupiwe's pairs (computed by `confusion-data/project.py`)
Method: restrict each matrix to our 13 consonants (other responses dropped, rows renormalized; /h/ responses = "heard no consonant"); then scale every row's error mass by one factor so the mean error is 20% (pattern compared at an equal noise level). Cells: symmetric pair confusion (P[a,b]+P[b,a])/2 in percent. Derived projected matrices: `confusion-data/proj-*.tsv`.

```
group (E=20%)            cooke-noise   cutler-nat   cutler-dutch  mand+12dB     mand+6dB    mand-quiet     mn55-6dB
raw mean error                   15.5           52.4           57.0           17.0           23.5            5.0           40.2
voicing p-b t-d k-g              6.77           1.28           2.26           0.36           0.34           0.93           0.09
place vl stops                   4.23           3.88           5.42          13.78          16.15          15.15          13.14
place vd stops                   4.11           1.66           2.25           6.31           7.47           6.87           8.11
f-p                              3.12           7.82           7.12           0.18           0.27           0.49           3.88
f-b                              1.69           3.72           5.02          24.67          15.85           3.24           1.45
f-s                              2.29           2.66           4.54           2.68           3.57           0.93           4.80
m-n                             10.57           3.70           4.21          12.03          12.76          15.03          10.37
m-b                              3.68           3.78           3.22           0.18           0.24           0.00           1.15
n-d                              2.80           5.29           3.02           0.18           0.25           0.00           0.57
l-n                              6.94           1.96           1.63          12.45           7.44          12.27              -
l-d                              1.39           2.17           3.12           0.18           0.27           0.00              -
l-w                              2.81           0.77           1.51           0.00           0.00           1.89              -
l-j                              2.77           0.83           0.50           0.57           0.41           0.96              -
w-j                              2.83           1.30           0.15           0.00           0.28           0.95              -
w-b                              3.77           1.90           2.05           0.18           0.00           0.46              -
w-g                              1.41           0.45           0.33           2.51           5.25           1.86              -
j-g                              3.48           4.96           4.99           0.00           0.28           0.00              -
j-d                              1.40           3.03           1.89           0.18           0.42           0.00              -
C -> no onset (mean)             1.20           5.28           2.88           0.00           0.00           0.00           0.00
```
(columns: Cooke 2008 noise avg; Cutler native CV 0 dB; Cutler Dutch CV 0 dB; Mandarin +12, +6, quiet; MN55 −6 dB. Mandarin quiet and Cooke clean have too few errors for level-matching to mean much; Cooke clean omitted.)

Readings:
- **Voicing** is the widest disagreement: 0.09% (MN55) to 6.8% (Cooke 2008), a 75× spread at the same overall error. MN55 is the low outlier (§1.4). Mandarin aspiration is also robust (0.3%), so a listener who hears Apupiwe voicing as aspiration might do well; the European data (Cooke, Cutler, Lovitt & Allen, Cooke 2010 "Voice is the least well-transmitted feature for all language groups") put it at 1–7%.
- **Place among voiceless stops**: 4–16%; voiced stops 2–8%.
- **m-n**: 4–13% in every source: the most stable large confusion.
- **l-n** 2–12%; **l-d** 0.2–3%.
- **Approximants** (the old guesses): l-w 0–2.8%, l-j 0.4–2.8%, w-j 0–2.8%, w-b 0–3.8%, w-g 0.3–5.3%, j-g 0–5%, j-d 0.2–3%. They are not each other's main competitors; l's main competitor is n, w's is b/g (by masker), j's is g/d.
- **f-b** 1.5–25% (white noise only at the top), **f-p** 0.2–7.8%.

## 2. Vowels

### Findings
- **No open five-vowel noise matrix found.** Best candidate: Gibson et al. 2026, "Acoustic-phonetic masking in Spanish vowel recognition by native English- and Spanish-speaking subjects", JASA 159(1):105–116 (Spanish /a e i o u/ in [dV], SSN and 1–16-talker babble at 0, −6, −12 dB; Spanish and English listeners). Abstract read (PubMed E-utilities); full text 403. A search-engine summary says both groups had "consistent difficulty ... discriminating the back rounded vowels /o/ and /u/" — **unverified** (not in the abstract).
- Cutler et al. 2004 (§1.5) vowel matrices, projected onto i←/i/ (beat), e←/eɪ/ (wait), a←/ɑ/ (hot), o←/oʊ/ (boat), u←/u/ (boot), other responses dropped (computed):

  | 0 dB babble | mean 5-vowel error | share of error: i-e | o-u | a-o | e-a | i-u | e-o | rest |
  |---|---|---|---|---|---|---|---|---|
  | native, Table III (V in VC) | 7.6% | 20% | 28% | 21% | 7% | 20% | 1% | 3% |
  | native, Table IV (V in CV) | 3.0% | 4 | 9 | 23 | 21 | 38 | 0 | 4 |
  | Dutch, Table VII (VC) | 22.2% | 33 | 27 | 14 | 0 | 17 | 1 | 8 |
  | Dutch, Table VIII (CV) | 13.8% | 10 | 12 | 33 | 0 | 40 | 0 | 5 |
  Same listeners' consonants (CV, 0 dB, projected): 52% (native), 57% (Dutch). Vowel/consonant error ratio: 0.06–0.15 native, 0.24–0.39 Dutch.
  The large i-u share is mostly English /u/ fronting (u→i 4–28%), a talker property; in a five-vowel language with talkers from many L1s some fronting of u is still expected (English, Japanese [ɯ]).
- Cutler 2004: "Vowel backness was transmitted better than vowel height"; going from 0 to 8 dB improved vowels by 2 points but consonants by 23–24.
- Meyer et al. 2013 (French words, natural noise −8.8 to −18.4 dB): of 8.5% vowel errors, 85% were missing responses and 15% confusions → ≈1.3% vowel substitutions; "no particular confusion occurred between vowels".
- Bond 1999, via Felty et al. 2013: in ~900 natural slips of the ear, "Approximately 1/3 of the errors involved misperception of a single consonantal segment ... Simple vowel misperceptions accounted for approximately 5%" → vowel:consonant ≈ 0.15.
- Jin & Liu 2014 (Front. Neurosci.; 12 English vowels, SSN and babble −15…0 dB; 12 English, 12 Chinese, 12 Korean listeners) [PMC, summary]: quiet 88% / 63% / 58%; native advantage 3–22 points in noise; back vowels identified worst. No five-vowel projection possible from what was retrievable.
- Typology (PHOIBLE, §4): 15.9% of languages lack a front mid vowel and 18.2% a back mid vowel (computed; e-i and o-u risk for their speakers). WALS 2A (channel_perception.md): 5 vowels is the modal system.

### Reading
Vowel errors are an order of magnitude below consonant errors for native listeners and 3–4× below for L2 listeners at the same SNR. Errors go to height neighbours (i-e, o-u), a-o, and i-u (u-fronting); e-o and diagonal pairs (i-a, i-o, e-u, a-u) are near zero. The v1 guess (neighbours 0.04, i-u and e-o 0.01, others 0.003) has the right ranking except that it treats e-a like i-e (data: e-a smaller), e-o like i-u (data: e-o ≈ 0, i-u large), and puts mean vowel error at ≈7.6% against MN55's 40% consonant error (ratio 0.19, inside the data's 0.06–0.39).

## 3. Onset vs no onset; final -n

Apupiwe facts that decide which data apply (spec/reference.toml §Syllables): "A syllable with no consonant before its vowel (a, en) occurs only at the start of a word. The only consonant that can end a syllable is n." So onset presence is only uncertain **word-initially**, and every case is a junction with what precedes.

### Findings
- **After a pause, voiceless stops lose their consonant.** Cutler 2004 initial CV at 0 dB babble: p→h 39.2%, t→h 27.9, k→h 27.9, f→h 14.2, b→h 15.0 (natives); Dutch p→h 20.9 (projected), similar. Apupiwe has no /h/, so this is "heard no consonant". Level-matched to 20% mean error (computed): p 17%, t 12.5%, k 11.7%, b 8.2%, f 6.9%, g 4.6%, others ≤2.4% (natives); Dutch about half. In VCV (Cooke 2008) the same rates are 1–4%: the vowel before the consonant protects it.
- **Hiatus across a word boundary is usually marked.** Davidson & Erker 2014 (Language; American English; read from PDF): vowel+vowel across a word boundary ("see otters") had glottalization 28% + glottal stop 17% ("nearly half"); word-internal VV and V+glide+V had ≤5%; non-glottalized VV and VGV still differed "on all measures, including duration, intensity, and formants". Dilley, Shattuck-Hufnagel & Ostendorf 1996 (J. Phonetics) [abstract via search]: glottalization of word-initial vowels 13–44% across speakers, more at phrase onsets and pitch accents.
- **Glide vs hiatus after i is confusable.** Clear & Hogoboom 2021 (Proc. LSA) [abstract]: listeners "sometimes perceived a glide that was truly absent"; Hogoboom 2020 (via search summary, **unverified**): [i.a] and [i.ja] are confusable even for speakers of languages that contrast them (Mandarin, Korean). No rates retrieved.
- **Nasal codas in noise.** Gwizdzinski et al. 2023 (Front. Commun. 8:1307547; read): words with oral (/d/) vs nasal (/n/) codas, 0 dB white noise, TTS voices: coda errors 5–6% for oral-coda words, 12–20% for nasal-coda words. Cutler 2004 final /n/ at 0 dB: heard as some nasal 82.5% (native), 65.8% (Dutch), mostly m/ŋ otherwise (forced choice, no "none" option). Mandarin onsets were 4–6 points less accurate before -an than before -a (computed from Yu & Do raw data).
- **Production-side loss of -n.** Caribbean Spanish (search summaries, **unverified**): Dominican final /n/ realized as vowel nasalization only in ~50% of cases, velar 47%, full elision 1%; other corpora 28.7% elision-with-nasalization. A listener whose L1 lacks nasal vowels may hear a nasalized vowel as plain V.
- **Syllable structure typology.** WALS 12A: simple (C)V only 61/486 languages (12.6%); moderately complex 274; complex 151.
- **Word-level insertions/deletions.** Felty et al. 2013 (JASA 134(1):572–585, doi:10.1121/1.4809540; 1428 words, 6-talker babble 0/+5/+10 dB, 192 listeners; read): of single-segment errors, substitutions 60.9%, deletions 17.1%, additions 21.9% (another passage: 59.4 / 18.6 / 21.9). 74% of all errors keep the target's syllable count; 16.4% are one syllable shorter, 5.8% one longer.

### Reading (inference)
- C→∅ is a word-initial, post-pause event concentrated on voiceless stops and f; v1's weights (w, j 5%; l, v, f 3%; others 0.5%) point at the wrong consonants. Glides lose to ∅ mainly in vowel+vowel junctions, by context: ∅↔j after i/e, ∅↔w after u/o.
- Two junctions the independent-syllable model cannot see: (1) word-final -n + vowel-initial word ("pan a" vs "pa na"), a resegmentation that in syllable-timed speech without a glottal onset is close to a merger; (2) -n + n-/m-initial syllable ("pan na" vs "pa na"), a geminate/singleton contrast that most L1s lack.
- -n loss is more likely than -n insertion (nasal codas are the error-prone side in Gwizdzinski et al.; production weakens them to vowel nasalization).

## 4. Common L2 mergers and their sources

### Direct L2 evidence (read)
- Inventory gaps predict specific L2 errors: Spanish listeners (no voiced fricatives) identify /z/ poorly; "German listeners have particular problems with /w/" (Cooke et al. 2010); Dutch listeners (final devoicing) make "many more voicing errors on final consonants" (Cutler 2004). Laterals and nasals were "hardly worse" for Spanish and Dutch L2 listeners than for natives in quiet (Cutler et al. 2007).
- The L2 penalty on top of the shared acoustic pattern: L2 consonant scores 76–92% of L1 scores (§1.3); consonant ranking agreement across 8 L1s W = 0.67–0.74 (§1.2).

### Typology: who lacks each Apupiwe contrast (computed by `confusion-data/phoible_gaps.py` from PHOIBLE 2.0, data/phoible.csv, downloaded 2026-10-13)
By language (one inventory per Glottocode, 2176 languages; marginal phonemes ignored):

| gap | % of languages | merger risk for Apupiwe |
|---|---|---|
| no voicing contrast in stops | 33.0 | p-b t-d k-g |
| no voiceless labial fricative (f/ɸ) | 53.7 | f-p (f→p or f→pʰ/h) |
| no /p/ | 9.1 | p-b (Arabic type), p-f |
| no /g/ (any) | 43.7 | g-k |
| no /s/ | 28.4 | s-t, s-ʃ (no ʃ in Apupiwe) |
| no lateral approximant | 16.5 | l-n, l-d (l realized ɾ/r) |
| no liquid at all | 4.4 | l-n, l-j |
| no /w/ | 15.7 | w-b (via v/ʋ) |
| no /j/ | 10.2 | j-dʒ→d |
| no front / back mid vowel | 15.9 / 18.2 | e-i / o-u |

Cross-check: WALS 4A no voicing contrast 182/567 (32%) plus fricatives-only 38 → no plosive voicing 38.8%; WALS 8A no laterals 95 + no /l/ 37 of 567; WALS 18A no fricatives 48/567. They agree with the PHOIBLE shares within a few points.

Weighted by L1 speakers of the 35 largest languages (Ethnologue 2026 L1 figures via Wikipedia "List of languages by total number of speakers"; Western Punjabi and Javanese skipped, no L1 figure; Levantine Arabic not in PHOIBLE; each language scored by the share of its PHOIBLE inventories showing the gap):

| gap | % of these L1 speakers | main contributors |
|---|---|---|
| no voicing contrast in stops | 32 | Mandarin, Cantonese, Wu, Korean (all inventories); Spanish 40% and Tamil 33% of inventories (analysis artefact for Spanish: β ð ɣ allophones) |
| no f | 16–17 | Korean, Japanese, Bengali, Indonesian, Tamil, Bhojpuri, Hausa |
| no /p/ | 5 | Arabic varieties, Hausa, Yoruba, Amharic, Vietnamese |
| no lateral | 4 | Japanese, (Korean single liquid) |
| no /w/ | 30 (≈15 without allophone artefacts) | German, Russian, Turkish, Hindi-Urdu (ʋ), Persian; Spanish/Portuguese count only because [w] is analysed as /u/ |
| no front mid vowel | 25 (artefact) | Mandarin's /e/ is analysed as an allophone of /ə/; real 3-vowel L1s (Arabic varieties partly, Quechua, Greenlandic) are a few percent |

Caveat: inventories are phonemic analyses; allophones the speaker hears every day (Spanish [w], Mandarin [e]) inflate the gaps. The robust large ones: **voicing ≈ 25–32%** of L1 speakers (mostly aspiration languages: Mandarin, Cantonese, Korean), **f ≈ 15%**, **w ≈ 10–15%**.
- Inference: an aspiration-language listener hears unaspirated [p] (Spanish, French, Russian talkers) as their unaspirated category, i.e. as Apupiwe b. Mandarin listeners almost never confuse aspiration (§1.6: 0.3% at matched level). So the voicing merger risk for a third of listeners depends on whether talkers aspirate p t k — a production norm, not a perception constant.

## 5. Proposed model v2

Structure (each part with its source; parts I added are marked):
1. **Consonant substitution matrix** = a level-matched pattern from published data, not one study. Best: equal mean of four sources that cover all 13 consonants (Cooke 2008 noise, Cutler native CV, Cutler Dutch CV, Mandarin +6 dB) at mean error E_C. Source: §1.8.
2. **Voicing multiplier** on p-b t-d k-g. Source: the 75× spread between sources (§1.4, §1.8).
3. **Onset presence by junction** (replaces the flat "weak consonant" table): after a pause, vowel-final word, or n-final word. Source: §3; spec rule that onsetless syllables are word-initial only.
4. **Coda -n loss/addition**, asymmetric, plus two junction cases (n + vowel-initial word; n + nasal onset). Source: §3. The junction cases are *added by me*: they need the model to see word pairs across a boundary.
5. **Vowel matrix** = V_ratio × E_C spread over pair shares. Source: §2.
6. **L2 listener groups**: each group is a variant that raises one contrast to a near-merger. Source: §4. *Added by me*; its add-back test is in §6.
7. Syllables stay independent apart from parts 3–4. Dropped: v1's i-u = e-o symmetry and the w/j/l/v/f "weak onset" list (both contradicted by data).

Parameter table (full list with sampling rules: `confusion-data/model-v2-params.tsv`). Rates at E_C = 0.20; pair rates symmetric.

| parameter | v1 | v2 best | range | status |
|---|---|---|---|---|
| consonant pattern | MN55 −6 dB only | mix of 4 sources | each source alone; MN55 | data |
| voicing p-b t-d k-g | ≈0.1% (MN55) | 2.7% | 0.1–7% | data (widest spread) |
| place p-t-k | MN55 | 7.4% | 3.9–16% | data |
| m-n | MN55 | 7.8% | 3.7–13% | data |
| l-n | 1.5% at 40% error | 4.5% | 1.6–12.5% | data |
| l-w, l-j, w-j | 6% at 40% error | 1.1–1.3% | 0–2.8% | data |
| w-b, w-g, j-g, j-d | 0.5–1.5% at 40% error | 1.7–3.4% | 0–5% | data |
| C→none, after pause | w,j 5%; l,v,f 3%; others 0.5% | p 12%, t/k 8.5%, b/f/g 5.5%, others 0.7% | low = VCV rates 1–4% | scaled data |
| C→none, after vowel | (same) | 1.5% | 0.5–4% | data |
| j↔none after i/e; w↔none after u/o | none→C = C→none/3 | 10% each way | 3–30% | **guess** |
| "Vn V" ↔ "V nV" across words | not modelled | 25% | 10–50% | **inference** |
| "Vn nV" ↔ "V nV" | not modelled | 30% | 10–50% | **inference** |
| -n loss | 8% (both ways) | 8% | 3–15% | scaled data |
| -n addition | 8% | 2.5% | 1–6% | scaled data |
| vowel error / consonant error | 0.19 | 0.15 | 0.05–0.40 | data |
| vowel error shares | neighbours equal; i-u = e-o | i-e .22, o-u .24, a-o .23, e-a .10, i-u .15, e-o .01, rest .05 | per-share min–max of 4 Cutler projections | data (i-u inference) |
| L2 groups (share π / their confusion m) | none | voicing .30/.10; no-f .15/.25; no-p .05/.25; no-w .12/.15; no-l .04/.15; no mid V .04/.25; CV-only L1 .08/coda loss .30 | π: §4 ranges; m: 0.02–0.5 | π data, m **guess** |

What stays a guess: every glide-hiatus rate, the two -n junction rates, the within-group L2 confusion levels m, the no-onset-after-pause rate for non-stops, and how voicing behaves for aspiration-language listeners (it hinges on whether talkers aspirate p t k, which the spec does not fix).

## 6. Robustness method

Goal: pick word forms that are hard to confuse under every plausible model, not just under the best guess.

1. **Variants.** Draw N = 32 parameter vectors by Latin-hypercube sampling over the ranges in `model-v2-params.tsv` (log-uniform where a range spans >3×; vowel shares as a Dirichlet centred on the best values). Add fixed corner variants: each consonant source alone; voicing at 0.1× and 3×; each L2 group switched on at π = 1 with its high m (the "worst listener" for that contrast); the v1 model (continuity check). ≈ 45 variants.
2. **Per-variant cost.** For each variant precompute the syllable-pair table (14 onsets × 5 vowels × 2 codas = 140 syllables → 140² table) plus the junction terms, and compute the existing weighted pair cost (frequency × stakes × confusion) for a candidate assignment. Divide by that variant's random-assignment median so noisy variants don't dominate: ĉ_v.
3. **Objective.** Minimize CVaR₀.₂₅ = mean of the worst quarter of ĉ_v (pure max is too brittle with guessed ranges). The annealer keeps one running total per variant; a move updates all N totals (cost N×), then recomputes the CVaR. Same moves as now.
4. **Report** for the winning assignment: ĉ_v for every variant, the variant where it is worst, and the pairs that enter the top-10 confusions under any variant ("regret pairs"). Prefer the assignment that is never worst over one that is best on average.
5. **What to measure next.** Rank parameters by how much the chosen forms change when that parameter alone moves across its range (one-at-a-time re-optimization from the winner). The top one or two are what a listening test should measure first. Likely candidates: voicing (spread 75×) and the -n junctions.
6. **Hold-out check.** Optimize on half the variants, score on the other half. If the winner's rank collapses on the held-out half, the ranges are too wide to design against and the listening test comes before the placement.

Add-back triggers for parts left out: syllable-count errors (Felty: 16.4% of word errors drop a syllable, 5.8% add one) once grammar words of different lengths are compared; vowel-context effects on consonants (Cooke 2010: consonants clearest before /a/, worst in /i_i/, /u_u/; magnitude only in a figure) if the robust winner puts fragile consonants mostly before i/u.

## 7. Biggest remaining uncertainties

1. **Voicing**: 0.1–7% at the same noise level across sources, plus a third of the world's L1 speakers (aspiration languages) whose voicing perception depends on whether talkers aspirate p t k. This single contrast carries many grammar-word distinctions.
2. **Word junctions**: glide vs hiatus (pi a / pi ya, pu a / pu wa), -n + vowel resegmentation (pan a / pa na), and -n + nasal (pan na / pa na). No rates found; the independent-syllable model scores them as distinct when they may be near-mergers.
3. **L2 within-group confusion levels (m)**: which listeners lack a contrast is well sourced (PHOIBLE, WALS), but how much they confuse it when listening to a designed language with mixed-accent talkers is not.

## 8. Face-to-face (audiovisual) listener (2026-10-15)

Decided by the author 2026-10-15 (design log, "A listener who sees the speaker joins the mishearing model"; idea from `unknown-unknowns.md` #7): add one audiovisual listener variant to `confusion2.variants()`, built from a published AV consonant matrix. Choices made while doing it are marked **added**, each with its reason.

### 8.1 Sources
Wanted: AV consonant matrices in noise with the audio-only (AO) condition of the same study. Found two usable ones; neither is masked by plain noise.

- **von Seth, Aller & Davis 2025**, JASA 157:1554–1576, doi:10.1121/10.0034846 (preprint PsyArXiv kj59f, read); trial data OSF https://osf.io/j56y4/ (`data/scored_data/consonants_scored{,_2}.xlsx`, downloaded). 20 English consonants (b tʃ d f g h dʒ k l m n p r ʃ t θ v w j z; **no /s/**) + /ə/, one female talker, closed set of 20, 126 native British English listeners online (113 also did session 2). Sound degraded by **noise vocoding**, not by added noise: "high clarity" = 16 channels, "low clarity" = 1 channel (broadband envelope only). Five conditions incl. AO and AV at both clarities. The paper prints no matrix (only feature transmission); counted here from the trials, 239 per consonant per condition. Overall correct: AO-high 51.7%, AV-high 79.0%, AO-low 22.4%, AV-low 55.4%, visual-only 37.8%. Files `vonseth2025-{AO,AV}-{high,low}.tsv` (counts).
- **Braida, Sekiyama & Dix 1998**, AVSP'98, ISCA archive (open PDF, tables read from the rendered page). 8 consonants b d g p t k m n + /a/, 2 Japanese and 2 American English talkers, 28 Japanese listeners, 16 presentations each per mode; sound **lowpass-filtered plus noise** (cutoff and SNR not given). Tables 2 (A, 48.4% correct) and 4 (AV, 83.3%) print full percent matrices, cells under 1% blank. Files `braida1998-japanese-{A,AV}.tsv`.
- Not usable or not reached: Binnie, Montgomery & Jackson 1974 (JSHR 17:619, doi:10.1044/jshr.1704.619), Grant & Walden 1996 (JASA 100:2415, doi:10.1121/1.417950) and Grant, Walden & Seitz 1998 (JASA, doi:10.1121/1.422788) are closed (OpenAlex: no open copy; ASHA 403). Walden et al. 1977 is a visual-only training study (from its title; not checked further). Lalonde & Werner 2019 (PLoS ONE, open data) tested in quiet only (AO 93% correct: too few errors). Lindborg & Andersen 2021 (PLoS ONE) has only b and g.

### 8.2 Projection
`confusion-data/project_av.py` applies `project.py`'s functions unchanged (restrict to our 13; other responses dropped and rows renormalized; /h/ = heard no consonant; `level_match` for comparisons) and writes `proj-av-*.tsv`. `project.py` itself is not changed (**added**: a separate script, so the existing projections can't move; it writes nothing else).
- Missing consonants. von Seth: **s** (no row, and no listener could answer s). Braida: **f s l w j**. `project.py` does not fill gaps: a missing consonant has no row and gets no responses. In `confusion2` the AV pattern needs all 13 rows, so `_fill_from_mix` (**added**) uses the `mn55+mix` rule for any missing set: the s row comes from mix4, and in every other row the share mix4 gives to s is put back at s and the rest scaled down. s is the most robust consonant in every audio source, so the fill matters little.
- Mapping: y = /j/; dʒ, tʃ, ʃ, θ, v, z, r responses dropped (no Apupiwe category).
- **added**: all released trials pooled (126 listeners in session 1, 113 in session 2), including listeners the paper left out of some analyses. Reason: pooled confusions, not individual differences, are what the model needs. The files label both sessions "Session_2", so the session is taken from the file.

### 8.3 Audio-only vs audiovisual, same study
Symmetric pair confusion in percent, level-matched to E = 20% (`python3 project_av.py`). Raw mean error over our consonants: vs-AO-high 36.5, vs-AV-high 17.5, vs-AO-low 77.9, vs-AV-low 40.9, Braida A 50.9, Braida AV 12.4.

```
group                    vs-AO-high   vs-AV-high    vs-AO-low    vs-AV-low   braida98-A  braida98-AV
voicing p-b t-d k-g            3.47         7.77         2.40         8.69         0.13         1.08
place vl stops                 7.74         5.84         2.49         0.86        11.44        11.17
place vd stops                 3.32         4.37         0.63         0.71         9.78        13.34
f-p                            0.48         0.00         0.67         0.13            -            -
f-b                            2.78         0.29         0.84         0.00            -            -
m-n                            7.64         0.96         4.51         0.58        15.18         0.00
m-b                            0.00         2.16         1.18         5.55         0.00         0.00
n-d                            0.24         0.75         0.31         2.62         0.00         0.80
l-n                           10.20        22.03         1.88         5.48            -            -
l-d                            0.00         1.00         0.66         5.15            -            -
l-w                            2.06         0.00         2.04         0.00            -            -
l-j                            1.54         0.24         2.48         8.37            -            -
w-j                            1.35         0.72         0.80         0.11            -            -
w-b                            0.00         0.24         1.98         0.00            -            -
w-g                            0.48         0.00         1.47         0.24            -            -
j-g                            0.36         0.24         1.24         2.79            -            -
j-d                            0.25         0.75         0.87         0.60            -            -
```

Largest changes, von Seth high clarity (the source the variant uses), level-matched (raw in brackets):

| pair | place | AO → AV, level-matched | raw |
|---|---|---|---|
| n-l | same (alveolar) | 10.2 → 22.0 | 18.6 → 19.3 |
| m-n | differs | 7.6 → 1.0 | 14.0 → 0.8 |
| p-b | same (voicing) | 2.8 → 9.3 | 5.1 → 8.2 |
| n-j | differs | 4.4 → 10.2 | 8.0 → 9.0 |
| t-d | same (voicing) | 6.3 → 11.7 | 11.5 → 10.3 |
| d-g | differs (alveolar/velar) | 7.9 → 11.9 | 14.4 → 10.4 |
| p-k, t-f, b-f | differs | 4.4, 3.0, 2.8 → under 0.8 | 8.0, 5.4, 5.1 → under 0.7 |
| b-m | same (nasality) | 0.0 → 2.2 | 0.0 → 1.9 |

Checking the expectation ("place confusions fall sharply, voicing and nasality stay"):
- **Place falls sharply when one consonant is labial or labiodental** (lips visible): m-n, p-t, p-k, b-d, b-f, t-f go to about 0 in all three comparisons. **It doesn't when both are inside the mouth**: t-k and d-g stay large (Braida AV: d-g 24%, t-k 21% raw; von Seth AV: t-k 14.5%, d-g 10.4% raw), and as a share of the errors they grow. The face shows lips, not alveolar against velar.
- **Voicing stays.** Raw p-b, t-d, k-g barely move (or rise at low clarity), so their share of the remaining errors grows 2 to 4 times. Braida's sound kept voicing (A 0.1%), so the face has nothing to add there.
- **Nasality vs oral at one place (b/m, d/n) stays small but rises**: b-m 0 → 2.2, n-d 0.2 → 0.8 level-matched (von Seth high), 1.2 → 5.6 and 0.3 → 2.6 at low clarity. In these sources sound carries nasality well, so these pairs are smaller than voicing even face to face.
- **Same-place sonorants rise**: n-l (and n-j, l-j, d-l at low clarity). n-l and n-j are already large in this study's audio-only data (n heard as l 31% in AO-high): probably talker- or vocoder-specific, since the four noise sources in §1.8 put l-n at 2–12%. The AV pattern inherits them. Treat the variant's n-l weight as an upper end.

### 8.4 The variant
`tools/confusion2.py`: pattern `"av"` = `proj-av-vonseth25-AV-high.tsv` with s filled from mix4. Variant `src-av` = best parameters with `C_pattern="av"`, level-matched to E_C through `_source` like the other single-source corners. It is placed after `src-mn55+mix`. `variants(av=False)` returns the previous 48 variants unchanged (same draws, names and order; the self-check asserts this, and it was checked against the old file cell by cell). `"av"` is not one of C_pattern's LHS categories, so no other variant moves. Best parameters and objective are unchanged.
- **added**: AV-high, not AV-low or Braida. Reasons: its raw error (17.5%) is closest to E_C = 20%, so level matching barely rescales it; 16-channel sound keeps some place information, as moderate noise does; English listeners, and 12 of 13 consonants measured. AV-low (1 channel, close to no spectrum) and Braida (8 consonants) are kept as cross-checks above.
- **added**: one source, not a mix of AV sources like mix4. Reason: Braida covers only 8 consonants and its sound kept voicing, unlike the noise sources. Add-back trigger: an open AV matrix in real noise covering l w j.
- Effect, best parameters, no listener groups, internal syllable (self-check line): p-b 9.3%, t-d 11.6%, k-g 2.3%, p-t 0.2%, m-n 1.0%, l-n 22.0%, m-b 2.2%, n-d 0.7%. Under best: p-b 3.6, t-d 1.4, p-t 10.2, m-n 7.8, l-n 4.5.
- `tests/confusion-v2/check.py` with the variant (results file not rewritten): it passes; 50 pairs are in some variant's short-word top 10 (was 48). src-av alone brings **ya~na** and **yo~no** (the n-j effect) into a top 10, and adds **de~te** and **tin~din** to the variants that put them there (voicing). Content words: src-av puts gulo~yulo, tikun~ditun, nanyo~lanno, lodi~loki and kuwun~duwun in a top 20. (Separately, `results.txt` is already out of date before this change: the worst-voicing column differs, e.g. tin~din 18.0 vs 22.5 now. Not caused here.)
- Flag (one line, design rule 1): the source's degradation is vocoding, and its n-l and n-j confusions look like artefacts of this study. Another option for the author: carry only the AO → AV *change* of the same study onto mix4, rather than using the AV pattern directly. Not done; the decision named the AV pattern.
- Drop test (design log): if the short-word rerun with the variant changes no form, drop it. The rerun is not done here.

## 9. Listener without high frequencies (low-pass) (2026-10-15)

Decided by the author 2026-10-15 (design log, "A listener without high frequencies joins the mishearing model"; idea from `unknown-unknowns.md` #8): add one low-pass listener variant to `confusion2.variants()` from Miller & Nicely 1955's filtered conditions, checked against a hearing-impaired matrix if one is usable. Built the same way as §8. Choices made while doing it are marked **added**, each with its reason.

### 9.1 Sources
- **Miller & Nicely 1955**, JASA 27:338–352 (scan, open PDF at jontallen.ece.illinois.edu; read from the rendered page images, pdftotext only as a cross-check). Low-pass series: Tables VII–XII, band 200 Hz up to 300, 400, 600, 1200, 2500 and 5000 Hz, all at S/N +12 dB (white noise; filter skirts 24 dB/octave, cutoff at −3 dB). High-pass series: Tables XII–XVII, 200/1000/2000/2500/3000/4500 up to 5000 Hz. There is no band-pass condition like the telephone's 300–3400 Hz.
- Transcribed (counts, all 16×16): Table XI (200–2500) `mn55-lowpass-2500.tsv`, Table X (200–1200) `mn55-lowpass-1200.tsv`, Table XII (200–5000) `mn55-lowpass-5000.tsv`; and for comparison the unfiltered tables at the nearest overall error, Table IV (0 dB) `mn55-noise-0dB.tsv` and Table V (+6 dB) `mn55-noise-6dB.tsv` (**added**: matched by Table XX's overall correct, 2862 vs 2913 for 2500 Hz, 3336 vs 3332 for 5000 Hz).
- Checks on the transcription: every table sums to 4000, every row to a multiple of 4 (four listeners per token), and the diagonal and the five per-feature correct counts match Table XX exactly, except one: Table X's duration total comes to 3515 against 3526 printed. Re-reading the cells found no misread that would explain it without breaking another total; it looks like an inconsistency in the paper (11 of 4000 responses; it touches only θ/s or ð/z columns).
- **Cut-offs (added).** Telephone (upper limit ~3.4 kHz) falls between 2500 and 5000 Hz; age-related loss (energy lost above ~2 kHz, sloping) is closest to 2500 Hz. The variant uses **2500 Hz** (Table XI): it is the conservative bracket for the telephone and the closest table to the typical presbycusis edge; its raw error over our consonants (17.2%) is the closest to E_C = 20%, so level matching barely rescales it (the same reason as AV-high in §8). 5000 Hz is too close to unfiltered to show the effect (f-s 0.65% level-matched; raw error 6.9%, so level matching triples its few errors), and 1200 Hz stands for severe loss; both are kept as cross-checks. High-pass tables model a different listener (low-frequency loss) and were not used. For the telephone the effect lies between the 5000 and 2500 Hz columns below, nearer which is unknown.
- **Hearing-impaired check.** Bilger & Wang 1976 (JSHR 19:718), Wang, Reed & Bilger 1978 (JSHR 21:5, "A comparison of the effects of filtering and sensorineural hearing loss on patterns of consonant confusions", the most direct check) and Dubno & Dirks 1982 (JSHR 25:141) are closed (ASHA 403; OpenAlex: no open copy). Used instead (**added**): **Trevino & Allen 2013**, JASA 134:607–617, doi:10.1121/1.4807474 (open in PMC3732204), Table III: 17 ears of 9 hearing-impaired American English listeners, mostly slight-to-moderate high-frequency sloping loss, 14 consonants (no θ ð), one female and one male token each, averaged over speech-weighted noise at 0, +6, +12 dB and quiet; percent, cells under 2% not printed. `trevino2013-HI-avg.tsv` (parsed from the HTML table); the two tokens of a consonant are averaged (f has only the female token). As the task asked, it is a check, not a variant.

### 9.2 Projection
`confusion-data/project_lowpass.py` applies `project.py`'s functions unchanged and writes `proj-lp-*.tsv` (**added**: a separate script, as in §8, so the existing projections can't move).
- Mapping: θ ð ʃ ʒ v z responses dropped and rows renormalized (no Apupiwe category). M&N has no /h/, so no "heard no consonant" column.
- Missing consonants: **l w j** (M&N tested none of them; Trevino & Allen neither). `project.py` does not fill them: they have no row and get no responses. In `confusion2` the `"lp"` pattern goes through `_fill_from_mix`, which for l w j gives exactly the `mn55+mix` rule the author accepted on 2026-10-13: the l w j rows come from mix4, and in every other row the share mix4 gives to l w j is put back and the rest scaled down. So the variant says nothing new about l, w, j.
- Caveat on θ: in the 2500 Hz table θ is the main sink for s (s→θ 78 of 272) and f (31 of 236). Dropping θ spreads those responses over the other answers in proportion; where a listener without a θ category would really put them is not measured. Trevino & Allen's set has no θ, and there f→s is 17% (female token).

### 9.3 Unfiltered vs low-pass, same study
Symmetric pair confusion in percent, level-matched to E = 20% (`python3 project_lowpass.py`). Raw mean error over our 10 consonants: lp1200 28.4, lp2500 17.2, lp5000 6.9, n0dB 19.7, n6dB 10.2, Trevino HI 11.5.

```
group                        lp1200       lp2500       lp5000         n0dB         n6dB trevino13-HI
voicing p-b t-d k-g            0.05         0.00         0.00         0.00         0.00         1.84
place vl stops                15.99        17.48        10.48        19.55        18.28         7.14
place vd stops                 8.09         7.45        11.21         9.04        11.19         8.33
f-p                            3.51         2.81         4.83         2.19         4.36         0.89
f-b                            4.17         3.75        10.47         1.68         1.81         4.13
f-s                           11.90        10.57         0.65         2.35         0.42        18.44
m-n                            2.02         4.49         7.10         3.11         2.02        17.44
```

Largest changes, 0 dB unfiltered → 2500 Hz low-pass (both about 18–20% raw error), level-matched (raw in brackets):

| pair | n0dB → lp2500 | raw |
|---|---|---|
| p-k | 31.8 → 9.2 | 31.2 → 8.0 |
| p-t | 12.9 → 26.4 | 12.7 → 22.7 |
| f-s | 2.3 → 10.6 | 2.3 → 9.1 |
| d-g | 26.3 → 20.8 | 25.9 → 17.9 |
| t-k | 14.0 → 16.9 | 13.8 → 14.5 |
| b-f | 1.7 → 3.8 | 1.6 → 3.2 |
| m-n | 3.1 → 4.5 | 3.1 → 3.9 |
| p-f | 2.2 → 2.8 | 2.2 → 2.4 |
| s-t | 0.6 → 1.0 | — |

Checking the expectation ("f/s, f/p, s/t-type pairs rise"):
- **f-s rises 4.5×** (2.3 → 10.6), and 1200 Hz gives the same (11.9). It is one-way: s is heard as f (17% of s after projection), f is rarely heard as s (1%). Without the hiss above 2.5 kHz an s sounds like a weak fricative. 5000 Hz keeps it (0.65): the s cue sits between 2.5 and 5 kHz, which is also where the telephone cuts.
- **f-p rises only a little** (2.2 → 2.8); **s-t stays small** (0.6 → 1.0). The expectation holds for f-s, barely for f-p, and not for s-t in this data.
- **Place among stops reshuffles rather than grows**: t loses its high-frequency burst and goes to p and k (t→p 74, t→k 47 of 212), so p-t and t-k rise while p-k, the largest noise confusion in M&N, falls. d-g stays very large either way. The whole voiceless-stop place group is about the same (19.6 vs 17.5).
- **Voicing and nasality stay intact** (0–0.05%), as M&N say for low-pass. M&N's voicing is the low outlier anyway (§1.4), so the variant carries no voicing information either way.
- **Hearing-impaired check (Trevino & Allen).** Its top two pairs are f-s (18.4) and m-n (17.4); low-pass gives f-s the expected rise, m-n only slightly (3.1 → 4.5). Spearman over 45 pairs: HI vs lp2500 0.61, HI vs n0dB 0.54, so low-pass is a bit closer to the hearing-impaired pattern than noise is. Stop place is lower in the HI data (7.1) and voicing higher (1.8), which fits Trevino & Allen's quiet and mild-noise conditions and modern recorded tokens rather than hearing loss. Treat it as support for f-s, and as a hint that real hearing-impaired listeners also confuse m-n more than the filter predicts (not built in).

### 9.4 The variant
`tools/confusion2.py`: pattern `"lp"` = `proj-lp-mn55-lp2500.tsv`, l w j filled from mix4 (`_fill_from_mix`). Variant `src-lp` = best parameters with `C_pattern="lp"`, level-matched to E_C through `_source` like the other single-source corners, placed after `src-av`. `variants(lp=False)` returns the previous 49 variants unchanged, and `variants(av=False, lp=False)` the original 48 (the self-check asserts both). `"lp"` is not one of C_pattern's LHS categories, so no other variant moves. Best parameters and objective are unchanged.
- **added**: one table (2500 Hz), not a mix of cut-offs. Add-back trigger: a decision to model telephone speech on its own; then interpolate 2500 and 5000 or find a 300–3400 Hz matrix.
- **added**: only the consonant pattern changes. Onset loss, -n and vowels stay at best values; low-pass mostly spares vowels' first two formants up to 2.5 kHz, but no data was gathered on that.
- Effect, best parameters, no listener groups, internal syllable (self-check line), with best (mix4) and src-mn55+mix for comparison:

  | pair | best | mn55+mix | src-lp |
  |---|---|---|---|
  | f-s | 3.3 | 4.8 | 10.6 |
  | p-t | 10.2 | 12.8 | 26.2 |
  | t-k | 6.6 | 13.0 | 16.8 |
  | d-g | 6.0 | 19.0 | 19.6 |
  | p-k | 5.5 | 13.3 | 9.1 |
  | f-p | 4.6 | 3.8 | 2.8 |
  | f-b | 6.6 | 1.4 | 3.6 |
  | m-n | 7.8 | 9.8 | 4.3 |
  | p-b | 3.6 | 0.3 | 0.0 |

- `python3 tools/confusion2.py`: passes (50 variants, all matrices stochastic). `tests/confusion-v2/check.py`: runs to completion with the variant (results file not rewritten). Short words: src-lp brings no new pair into any variant's top 10 (still 50 pairs). Its own top 10: **to~po** 24.4% (best 9.4%), **de~ge** 18.5, **ke~te** 15.8, **tin~kin** 14.6, **fa~sa** 10.0 (best 3.1%, rank 22 → 5), **se~fe** 9.9 (rank 23 → 6), pi~fi 5.7, fu~pu 5.7, la~na 4.7, min~nin 3.7. So it is the only variant that makes **fa~sa** and **se~fe** dangerous: 10.0% and 9.9% against at most 4.7% in any other variant (lhs-09); `check.py`'s "max 10.0" for fa~sa and se~fe is now src-lp. ke~te and tin~kin reach about the same maxima as src-av (15.8 vs 15.5, 14.6 vs 14.3); to~po stays below lhs-10's 29.1%. Content words: src-lp puts apu~batu, kige~tiwe, wase~afe, afe~tase and unfu~kunsu in a top 20. (`check.py` prints "14 corners" as fixed text; with src-av and src-lp there are 16.)
- Flag (one line, design rule 1): the variant inherits M&N's quirks (trained crew, white noise, no voicing errors, p-k/d-g heavy), so its stop-place numbers say as much about MN55 as about low-pass. The same option as in §8 is open to the author: carry only the n0dB → lp2500 *change* of the same study onto mix4 (which would keep the f-s and t-burst effects without M&N's baseline). Not done; the decision named M&N's filtered conditions.
- Drop test (design log): if the short-word rerun with the variant changes no form, drop it. The rerun is not done here.

## Sources (read in this study unless marked)
- Cooke & Scharenborg 2008, The Interspeech 2008 Consonant Challenge. https://www.isca-archive.org/interspeech_2008/cooke08_interspeech.pdf
- Cooke, García Lecumberri, Scharenborg & van Dommelen 2010, Speech Communication 52:954–967. https://pure.mpg.de/rest/items/item_1169655_1/component/file_1169654/content
- Cutler, Cooke, García Lecumberri & Pasveer 2007, Interspeech, L2 consonant identification in noise. https://pure.mpg.de/rest/items/item_58738_2/component/file_58739/content
- Cutler, Weber, Smits & Cooper 2004, JASA 116:3668–3678. https://pure.mpg.de/rest/items/item_60592_4/component/file_60593/content
- Lovitt & Allen 2006, 50 years late: repeating Miller–Nicely 1955, Interspeech. https://www.isca-archive.org/interspeech_2006/lovitt06_interspeech.pdf
- Yu & Do 2024, Data in Brief 52:109868; data https://osf.io/rbt8x
- Moreno-Torres et al. 2017, JASA 141:3079 (abstract, PubMed 28599525)
- Kalaiah et al. 2020, Noise & Health (PMC7158896; text summary)
- Meyer, Dentel & Meunier 2013, PLoS ONE 8:e79279 (article page summary)
- Gibson et al. 2026, JASA 159:105–116 (abstract, PubMed 41481345)
- Jin & Liu 2014, Front. Neurosci. (PMC4212258; summary)
- Felty, Buchwald, Gruenenfelder & Pisoni 2013, JASA 134:572–585 (PMC3724775)
- Davidson & Erker 2014, Hiatus resolution in American English, Language (author PDF, NYU)
- Clear & Hogoboom 2021, Proc. LSA 6 (abstract); Hogoboom 2020 (search summary only)
- Dilley, Shattuck-Hufnagel & Ostendorf 1996, J. Phonetics (search summary only)
- Gwizdzinski, Barreda, Carignan & Zellou 2023, Front. Commun. 8:1307547 (UCL PDF)
- WALS chapters 4, 8, 12, 18 (wals.info); PHOIBLE 2.0 data (github.com/phoible/dev, data/phoible.csv)
- Ethnologue 2026 L1 figures via Wikipedia, List of languages by total number of speakers (accessed 2026-10-13)
- Not accessible: Wang & Bilger 1973 (paywall), Phatak & Allen 2007 (403), Moreno-Torres 2017 and Gibson 2026 full texts (403), Felty 2013 supplementary data (AIP).
- von Seth, Aller & Davis 2025, JASA 157:1554–1576, doi:10.1121/10.0034846; preprint https://osf.io/preprints/psyarxiv/kj59f; data https://osf.io/j56y4/ (§8)
- Braida, Sekiyama & Dix 1998, AVSP'98. https://www.isca-archive.org/avsp_1998/braida98_avsp.pdf (§8)
- Lalonde & Werner 2019, PLoS ONE 14:e0213588 (article page summary; quiet only) and Lindborg & Andersen 2021, PLoS ONE 16:e0246986 (article page summary; b/g only) (§8)
- Not accessible: Binnie, Montgomery & Jackson 1974; Grant & Walden 1996; Grant, Walden & Seitz 1998 (closed, §8)
- Miller & Nicely 1955, JASA 27:338–352, doi:10.1121/1.1907526, Tables IV, V, X, XI, XII and XX. https://jontallen.ece.illinois.edu/uploads/537.F18/Papers/MillerNicely55.pdf (§9)
- Trevino & Allen 2013, JASA 134:607–617, doi:10.1121/1.4807474, Table III. https://pmc.ncbi.nlm.nih.gov/articles/PMC3732204/ (§9)
- Not accessible: Bilger & Wang 1976 (JSHR 19:718, doi:10.1044/jshr.1904.718); Wang, Reed & Bilger 1978 (JSHR 21:5, doi:10.1044/jshr.2101.05); Dubno & Dirks 1982 (JSHR 25:141) (closed, ASHA 403, §9)

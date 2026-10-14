# Confusion data for the mishearing model (v2)

## Progress

- 2026-10-13: started. Plan: (1) consonant matrices, multi-L1; (2) vowels; (3) onset/none, final nasal; (4) L2 mergers + typology; (5) model v2 parameters; (6) robustness method.
- Prior work to reuse, not redo: `channel_perception.md` §1 (Miller & Nicely, Cutler et al. 2004 grand means, Phatak & Allen gaps).
- 2026-10-13: §1 consonants: Cooke & Scharenborg 2008 matrix extracted (TSV), Cutler et al. 2007 (Spanish/Dutch L2), Cooke et al. 2010 (8 L1s) read. Next: Wang & Bilger, Phatak/Lovitt, non-European listeners.

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

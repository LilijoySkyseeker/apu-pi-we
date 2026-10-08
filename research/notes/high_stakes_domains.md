# High-stakes communication domains: natural experiments in miscommunication and the controlled languages built to fix them

Scope note: aviation, maritime, medicine, technical documentation (STE) and military radio. Primary sources were read in full text where marked "(read)": FAA CAMI reports AM-96/26, AM-06/21, AM-06/25; the 1959 ICAO spelling-alphabet rationale (DTIC AD227630); ICAO Doc 9835; the IMO SMCP text (NAV 46/WP.3 annex, the draft adopted as Res. A.918(22)); the EUROCONTROL Air-Ground Communication Safety Study; and Joint Commission Sentinel Event Alert 58. Everything else came from abstracts or secondary summaries and is flagged as such.

## 1. Aviation: what the incident and tape data show about pilot–controller miscommunication

### Takeaway
In routine operations, measured readback errors are rare (<1% of clearances in Cardosi's en-route tapes; about 6% of TRACON readbacks in 2004). They rise steeply with message complexity, and they cluster on **numbers** (headings, frequencies, altitudes) and **addressing** (similar call signs). Incident databases are much more skewed: information transfer appears in more than 70% of early ASRS reports, and similar call signs are the top factor in European communication occurrences. The famous accidents (Tenerife, Avianca 52, the "to/two" crash) are failures of speech-act marking, urgency marking and number homophony, which phraseology alone did not prevent.

### Cited Findings
**Base rates from voice-tape field studies (normal operations)**
- Cardosi (1993, DOT/FAA/RD-93/11) analysed 47–48 h of tapes from 8 en-route centres: 5,032 controller transmissions and 3,576 clearances. She found 27 communication errors, i.e. readback errors in less than 1% of clearances. Of the clearances, 3% were not acknowledged and a further 2.7% needed repetition. — [Prinzo 1996, AM-96/26, lit. review (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/AM96-26.pdf); [Cardosi 1993 report](https://rosap.ntl.bts.gov/view/dot/8659/dot_8659_DS1.pdf) (primary not opened)
- Across Cardosi's series (en route, TRACON, tower; about 50 h of tapes each), the readback-error rate was "consistently less than 1%". Repeat requests were similarly low except en route (1.4%). Local (tower) controllers saw one readback error per 2.5 h; TRACONs saw about one per half-hour. "The vast majority of these errors were caught and corrected." Less than 0.5% of all exchanges ended in an uncorrected readback/hearback error. — [Schroeder 2006, FAA AM-06/21 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200621.pdf)
- Full readbacks were given in about 70% of en-route responses but in under 30% of tower Local Control responses. — [Schroeder 2006 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200621.pdf)
- **Complexity effect.** En route, the readback-error rate doubled when complexity went from 3 to 4 elements. Transmissions with ≥5 elements were 4% of controller transmissions but produced 26% of errors. TRACONs showed the same pattern. — [Schroeder 2006, summarising Cardosi & DiFiore 2004 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200621.pdf)
- Prinzo, Hendrix & Hendrix (2006) studied 50 h of tapes from 5 of the busiest US TRACONs (Oct 2003–Feb 2004), with 14,673 controller-to-pilot transmissions and 11,159 paired readbacks analysed:
  - 93.8% of readbacks were correct. Of the 6.2% faulty ones, 654 had 1 error and 34 had ≥2.
  - Below complexity 10, the error rate stayed at 2.28% (62/2,718) to 6.14% (41/668).
  - At complexity 11–13 it rose from 10.84% to 19.16%. Above 16 it "approached 38%".
  - With a liberal scoring criterion the overall rate was 1.3%.

  — [Prinzo et al. 2006, AM-06/25 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200625.pdf)
- Same study, trend since Cardosi et al. 1996:
  - Full readbacks rose from 60% to more than 82%.
  - Full readback with a complete call sign rose from 37% to 61%.
  - Pilot/controller call-sign mismatch fell from 0.8% to 0.3%.
  - "Aircraft headings and radio frequency changes still are the most frequently occurring readback errors."

  — [AM-06/25 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200625.pdf)
- Number errors observed in the same study:
  - **Number rounding/truncation**, e.g. call sign "Ownship67H" became "Ownship60H" and heading 140 became "ONE FOUR".
  - **Cross-topic leakage of format**: "THREE POINT FIVE" for 3,500 ft, borrowing the frequency "point".
  - Non-native readbacks such as "TWO ZERO HUNDRED" for 200 kt.

  — [AM-06/25 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200625.pdf)
- Prinzo (1996) studied 3 TRACONs: 4,500 transmissions and 12,200 communication elements. Using a broad definition of "communication error" that includes deviations from prescribed form, not only misunderstandings:
  - 40% of 2,500 controller elements and 59% of 5,900 pilot elements had at least one error.
  - More than 50% of errors fell in the *instruction* speech-act category.
  - Controllers omitted key words (frequency, airspeed). Pilots gave partial readbacks and grouped digits.
  - The study notes the irony that omitting and grouping numbers to save airtime "may create the problems that pilots and controllers are trying to prevent".

  — [AM-96/26 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/AM96-26.pdf)
- Pilot/controller communication was a factor in incidents in 1993–94:
  - 27% of operational errors (205/747 in 1993)
  - 40% of pilot deviations (573/1,423)
  - 15% of near mid-air collisions (38/255)

  The 1994 figures were similar (26% / 41% / 14%). — [AM-96/26, Table 1 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/AM96-26.pdf)
- Communication errors in operational-error (OE) investigations:
  - Rodgers & Nye (1993): 36% of en-route OEs involved communication errors.
  - Cardosi & Yost (2001), tower: 41% of OEs involved communication errors and 19% pilot–controller miscommunication.
  - Listed causal factors: too much information per message, frequency congestion, workload, speech rate, poor English of international pilots, similar-sounding call signs.

  — [Schroeder 2006 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200621.pdf)

**Incident-database analyses**
- Billings & Cheaney (1981, NASA TP-1875) reviewed about 28,000 ASRS reports from the first five years. More than 70% involved information-transfer problems, mostly voice communication. The problem types were incomplete/inaccurate content, ambiguous phraseology, absent communication, messages misperceived through phonetic similarity, and untimely transmission. — [Flight Safety Foundation, "Failure to Communicate" (secondary)](https://flightsafety.org/asw-article/failure-to-communicate/) (primary NASA TP-1875 not retrieved)
- Grayson & Billings (1981) listed factors in ASRS miscommunications: pilot expectations, similar call signs, transposed numbers, garbled phraseology, and inaccurate or incomplete messages. Monan (1980, 1983) studied similar call signs and readback/hearback. — [Schroeder 2006 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200621.pdf)
- Cardosi, Falzarano & Han (1998, DOT/FAA/AR-98/17) analysed 386 ASRS reports. The most common contributing factors were similar call signs, pilot expectation and high controller workload. — [Schroeder 2006 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200621.pdf); [Cardosi et al. 1998](https://apps.dtic.mil/sti/tr/pdf/ADA356655.pdf) (primary returned 403; the breakdown percentages were not verified)
- An ASRS altitude-deviation analysis of 191 reports (1991) found the 10,000/11,000 ft confusion was "by far the most common altitude combination", in 38% of altitude busts. — [FSF (secondary)](https://flightsafety.org/asw-article/failure-to-communicate/)
- An IATA 2011 survey of 2,070 airline pilots:
  - Non-standard or ambiguous phraseology was ranked the #1 concern.
  - Number homophones ("two/to", "four/for") were ranked #2.
  - 44% said they met non-standard phraseology at least once per flight.

  — [FSF (secondary)](https://flightsafety.org/asw-article/failure-to-communicate/)
- **EUROCONTROL Air-Ground Communication Safety Study** covered 535 reported European occurrences, Mar 2004–Apr 2005 (62% pilot-reported).
  - Problem types:
    - loss of communication 26%
    - readback/hearback error 10% (52)
    - equipment 8%
    - hearback error alone 1%
    - no pilot readback 1%
    - other 36%
  - Top contributing factor was **similar call sign, in 175 occurrences (33%)**. Next came frequency change 12%, airborne radio malfunction 8%, interference 8%, and inaccurate/incomplete content 5%.
  - Within the 52 readback/hearback occurrences, a similar call sign was a factor in 37% and pilot expectation in 17%. An incorrect readback appeared in 15, and **11 of those 15 went undetected by the controller**.
  - Consequences: none in 36%, prolonged loss of communication 23%, altitude deviation 7%, loss of separation 7%, "wrong aircraft accepted clearance" 6%, "instruction issued to wrong aircraft" 4%.

  — [EUROCONTROL AGC Safety Study (read)](https://skybrary.aero/sites/default/files/bookshelf/162.pdf)
- Non-compliance with phraseology is the norm. Mell (1992) found that 70% of en-route speech acts with a prescribed phraseology, by native and non-native speakers, did not comply with the standard. — [ICAO Doc 9835 §1.2.3 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)

**Landmark accidents**
- ICAO Doc 9835 gives two canonical examples.
  - "Descend two four zero zero feet": the "two/to" homophony led the pilot to hear 400 ft instead of 2,400 ft, "The aircraft crashed into high ground". This is widely identified as Flying Tiger 66 (1989), but Doc 9835 does not name the flight.
  - "We are at take-off" (Tenerife 1977): the controller understood the aircraft to be waiting, but it was rolling.

  ICAO "published changes to phraseologies and procedures" after the 1977 accident. — [ICAO Doc 9835 §3.3.6–3.3.7 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)
- After Tenerife, the word "takeoff" is reserved for the actual takeoff clearance, and "departure" is used elsewhere (e.g. "ready for departure"). — [Wikipedia, Tenerife airport disaster (secondary)](https://en.wikipedia.org/wiki/Tenerife_airport_disaster)
- **Avianca 52 (1990)**: the NTSB probable cause included the crew's "failure to communicate an emergency fuel situation to air traffic control". The first officer, a non-native English speaker, asked for "priority" and said they were "running out of fuel" but never used "emergency". The NTSB also cited a lack of "standardized understandable terminology for pilots and controllers for minimum and emergency fuel states". — [Wikipedia, Avianca Flight 052, quoting NTSB AAR-91/04 (secondary)](https://en.wikipedia.org/wiki/Avianca_Flight_052); [FAA Lessons Learned, AVA052](https://www.faa.gov/lessons_learned/transport_airplane/accidents/AVA052)
- Language proficiency:
  - "Over 800 people lost their lives in three major accidents" (a ground collision, a fuel exhaustion, a CFIT) in which insufficient English proficiency contributed.
  - Concern was "heightened" after a 1996 mid-air collision that killed 349.
  - In the CFIT case, the controller admitted the crew's position reports were incongruent but he "lacked plain English proficiency to clarify his doubts".

  — [ICAO Doc 9835 §1.2.1, §1.2.4 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf). The widely quoted "more than 1,100 deaths 1976–2000" sums these: about 800 + 349. — [ERAU / search summary of ICAO material (secondary)](https://worldwide.erau.edu/colleges/aviation/department-of-aviation-english/icao-language-proficiency-requirements)
- Phraseology cannot cover everything:
  - "No set of standardized phraseologies can fully describe all possible circumstances and responses."
  - In one analysed gear-malfunction dialogue, "fully 60 per cent of the dialogue required plain language".
  - Mixing two languages in one airspace degrades the situational awareness of crews who cannot overhear ("party-line" loss).

  — [ICAO Doc 9835 §1.2.3, §1.2.5, §3.3.19 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)

### Inferences
- Failure types ranked roughly by frequency × severity in the data:
  1. **Addressing/reference errors.** Similar call signs, and a clearance accepted by the wrong aircraft, are the #1 factor in the European data and top-3 in ASRS.
  2. **Numeric errors.** Headings and frequencies are the most common readback errors; homophones (two/to, four/for), rounding and grouping, and leakage of format between topics follow.
  3. **Expectation bias.** The listener hears what they expected; it is the second factor after call signs for readback/hearback.
  4. **Message overload.** The error rate is roughly flat up to a threshold, then rises nonlinearly. This is consistent with working-memory limits.
  5. **Speech-act and urgency mis-marking.** This is rare but catastrophic: Tenerife (a statement of action heard as a position report) and Avianca (urgency under-marked).
- Readback is a powerful but leaky loop. Readback errors happen in about 1–6% of clearances, but controllers miss a large share of them: 11 of 15 in the EUROCONTROL data. Cardosi's often-quoted hearback-miss rates (about 11% en route vs 37–40% tower) appear only in secondary search summaries here, and were not verified. The receiver's echo works only if the sender actually listens to it. That is a "closed loop" requirement on attention, not just on syntax.
- The base-rate finding matters for design. A language that is >99% reliable per exchange still produces accidents at scale, so the residual errors must be *detectable* (redundancy, readback), not just rare.
- Speakers economise: they drop words, group digits, truncate and omit call signs. This degrades the code. Any designed language must expect its redundancy to be eroded in use, so redundancy should be cheap to say and costly to omit.

### Gaps
- I could not open the Cardosi 1993 and Cardosi et al. 1998 primaries (DTIC 403; ROSAP returned an HTML stub). The often-quoted hearback-failure rates (11% en route; 37% Local and 40% Ground at towers) appeared only in a search-engine summary and are **not verified**.
- Billings & Cheaney (1981) is known only through a secondary source. The NTRS record I fetched (19810013507) turned out to be Grayson's DABS data-link report, not TP-1875.
- I found no controlled before/after study that isolates the effect of a specific phraseology change on error rates (e.g. "departure" vs "takeoff"). The evidence is accident-driven rule changes plus rising compliance (Prinzo 2006 readback trend), not trials.

## 2. Design features of ICAO phraseology, the spelling alphabet and number pronunciation: why chosen, and evidence

### Takeaway
The ICAO/NATO alphabet (final 1956) is the best-documented engineered vocabulary. Words were chosen by **articulation score** (how often a word is heard correctly) **and confusion-matrix minimisation** (how often it is heard when another word was said). They were tested in noise with speakers and listeners of several NATO nationalities and judged *in the context of the whole set*. The revised set beat its predecessor with p<0.001. The special digit pronunciations ("tree", "fife", "niner") are standard, but the reasons commonly given for them are poorly documented in primary sources.

### Cited Findings
- The problem being solved: letters cluster into confusable sets, e.g. A/H/J/K; B/C/D/E/G/P/T/V/Z; F/S/X; I/R/Y; L/M/N; Q/U/W. The problem is "especially acute in noise, or when communicators are not in face-to-face contact, or when the speaker and the listener come from different regional or language backgrounds". — [ICAO Word-Spelling Alphabet rationale, 1959, DTIC AD227630 (read; OCR)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- The earlier ITU alphabet (Amsterdam, Baltimore, Canada…, 1927/1932) failed in operation because its words "were unusual in everyday language" and "lacked desirable phonetic qualities". — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- WWII testing by the Harvard Psycho-Acoustic Laboratory covered 250 words, including 130 that had been the most intelligible of 2,000 tested. It found many military-list words had low intelligibility but that most deficiencies were fixable by substitution. — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- Testing method (Ohio State, Moser and colleagues):
  - Speakers represented six NATO nations, and five signal-to-noise conditions were used.
  - Listeners had about 12 h of training and heard random 3-letter code groups.
  - Noise was used because it "do[es] not create confusion, but do[es] intensify those confusions already inherent between the words", which exposes weak words cheaply.
  - Both foreign and American listeners did significantly better with the ICAO list from −5 to −16 dB S/N, significant at the 0.1% level.

  — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- Two criteria, stated explicitly. A word must have a high **articulation score** and a low **confusability score**. FOOTBALL had a slightly higher articulation score than FOXTROT but was rejected because listeners heard it when HOTEL and VICTOR were spoken. — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- System-level effects:
  - Replacing COCA, METRO and EXTRA with CHARLIE, MIKE and X-RAY gave a highly significant improvement.
  - A further three-word change (FOOTBALL, UNIFORM, ZEBRA) introduced more confusions than it removed, "in unexpected parts of the matrix".
  - Hence substitutions must be tested "in the context of the entire alphabet".

  — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- NECTAR was confused with VICTOR "both experimentally and operationally" (UK team under G. E. Bell). NOVEMBER beat NUGGET in joint US-UK tests and was adopted. The final list was recommended in 1956. — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- Cross-language criteria:
  - Avoid polysyllables whose syllable count or stress differs across language groups.
  - Avoid false friends (ACTUAL/ACTUEL).
  - Prefer words with Latin roots common to English and Romance languages.
  - Keep final vowels, since final consonants are weak or dropped in French and Spanish.
  - Aim for "minimum linguistic coloring" across speaker groups.

  — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- Polysyllables are deliberate redundancy. Losing one or two syllables of PROPAGANDA still identifies P, whereas a noise burst can wipe out a monosyllable and force a repeat. The four worst words in the old US-UK list (QUEEN, KING, GEORGE, JIG) were monosyllables. A mix of 1-, 2- and 3-syllable words increases variety and reduces confusability. — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- Interaction with digits:
  - "Most errors are intra-set, i.e., digits with digits and letters with letters."
  - NAN was replaced by NICKEL in 1944 "because of confusion with NINE and NINER". This is evidence that "niner" was already in use by WWII.
  - A 1950 count of 121,296 words from 100+ CAA towers found digits dominate traffic (ONE 4,955; TWO 4,249; ZERO 4,219…) versus ROGER 1,045 and ABLE 319. So digits, not letters, carry most of the load.

  — [same (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
- SMCP (and ICAO) digit pronunciations: ZEERO, WUN, TOO, TREE, FOWER, FIFE, SIX, SEVEN, AIT, NINER, TOUSAND. Numbers are spoken digit by digit ("one-five-zero" for 150). — [IMO SMCP §2.2, §10 (read)](https://aflopez.webs.ull.es/nautica/IMO_Standard_Marine_Communication_Phrases.pdf)
- The usual explanations are **unverified, secondary/folk sources**:
  - "niner": avoids confusion with "five" and with German *nein*
  - "fife": avoids "fire"
  - "tree": accommodates languages without /θ/
  - "fower": distinguishes it from "for"

  — [Wikipedia, NATO phonetic alphabet](https://en.wikipedia.org/wiki/NATO_phonetic_alphabet); [AOPA, "Tree, Foh-Wer, Fife"](https://www.aopa.org/news-and-media/all-news/2022/october/flight-training-magazine/ol-aviation-lingo)
- Phraseology design goals: phraseology provides "clear, concise, unambiguous language to communicate messages of a routine nature". Plain language is used "only when standardized phraseology cannot serve an intended transmission", and must itself be clear, concise and unambiguous. — [ICAO Doc 9835 §1.2.3, glossary (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)
- Partly as a result of these accidents, ICAO strengthened its language proficiency requirements (Assembly Resolution A32-16; Level 4 operational minimum). — [ICAO Doc 9835 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)

### Inferences
- The alphabet process is a reusable method for designing any high-stakes lexicon:
  1. Measure per-item recognition.
  2. Measure the full confusion matrix.
  3. Stress-test in noise to surface latent confusions.
  4. Test with the actual multilingual user population.
  5. Re-test every substitution against the whole set, because local fixes create distant confusions.
- Design features with direct evidence:
  - Distinct syllable counts and stress patterns.
  - Vowel-final words for Romance speakers.
  - Avoiding false friends.
  - Reserving words so a token signals exactly one role ("takeoff" only in a clearance).
  - Recoding the most dangerous homophones ("niner"; the "two/to" risk motivating explicit units and digit-wise numbers).
- Digits carry most of the safety-critical payload and most confusions are within the digit set. A designed language should invest more in number encoding (distinct forms, explicit units and type markers like "heading/flight level/knots") than in letters.

### Gaps
- No primary ICAO or ITU document was found that gives the original rationale or test data for "tree/fower/fife/niner". The 1959 report addresses letters, not digit pronunciations, beyond showing "niner" predates 1944.
- I did not retrieve the effect-size tables from the 1959 report; the OCR is too degraded. Only the significance statements are recoverable.
- ICAO Doc 4444 (PANS-ATM) phraseology chapter: not retrieved. Specific rules, e.g. "all numbers in a frequency transmitted digit by digit except whole hundreds/thousands", are from general knowledge and are not cited.

## 3. Maritime: IMO SMCP / Seaspeak and explicit speech-act markers

### Takeaway
SMCP (IMO Res. A.918(22), 2001; mandatory under STCW for officer training) is the most explicit engineered fix for **speech-act ambiguity**. It uses eight optional message markers, fully worded yes/no answers, one phrase per event, and no synonyms or contractions. The design rationale is clearly documented. **Outcome evidence is essentially absent**: I found no study measuring whether markers reduce errors. The quantitative claims about maritime miscommunication come from secondary sources and are weak.

### Cited Findings
- SMCP was "drafted on purpose in a simplified version of Maritime English to reduce grammatical, lexical and idiomatic varieties to a tolerable minimum". It uses "block language" that omits function words (the, a/an, is/are) under time pressure. Its explicit features are:
  - avoiding synonyms
  - avoiding contracted forms
  - fully worded answers to yes/no questions
  - one phrase for one event
  - phrases built as "identical invariable plus variable"

  — [IMO SMCP, General §4 (read)](https://aflopez.webs.ull.es/nautica/IMO_Standard_Marine_Communication_Phrases.pdf)
- The eight **message markers** are INSTRUCTION, ADVICE, WARNING, INFORMATION, QUESTION, ANSWER, REQUEST and INTENTION. They are optional ("at the discretion of the shore personnel or the ship's officer"), spoken before the message, and "may be used to increase the probability of the purpose of the message being properly understood". The definitions encode **authority and obligation**, not just mood:
  - INSTRUCTION implies a sender with "full authority" and a "legally binding" message, to be followed unless there are safety reasons, which must be reported back.
  - ADVICE: "the decision whether to follow … still stays with the recipient."
  - WARNING: danger, needing immediate attention.
  - QUESTION "removes any doubt on whether a question is being asked or statement being made".
  - ANSWER "should not contain another question".
  - REQUEST "must not be used involving navigation".
  - INTENTION is restricted to the sender's own navigational actions.

  — [IMO SMCP, AI/6 "Application of Message Markers" (read)](https://aflopez.webs.ull.es/nautica/IMO_Standard_Marine_Communication_Phrases.pdf)
- The IMO VTS Guidelines recommend that any message to a vessel make clear "whether the message contains information, advice, warning, or instruction". — [IMO SMCP AI/6 (read)](https://aflopez.webs.ull.es/nautica/IMO_Standard_Marine_Communication_Phrases.pdf)
- **Response forms echo the content.** To an instruction or advice, reply "I will / I will not …" followed by the instruction in full. Example: "ADVICE. Do not overtake the vessel North of you." → "I will not overtake the vessel North of me." Other forms: "Yes/No" plus the full phrase; "Stand by" plus a time interval; "No information". — [IMO SMCP §4 (read)](https://aflopez.webs.ull.es/nautica/IMO_Standard_Marine_Communication_Phrases.pdf)
- Repair and emphasis prowords:
  - "Mistake … Correction …", e.g. "My present speed is 14 knots – mistake. Correction, my present speed is 12, one-two, knots".
  - "Repeat" to safeguard critical parts, e.g. "My draft is 12.6 repeat one-two decimal 6 metres"; "Do not overtake – repeat – do not overtake".
  - "Say again".
  - Digit-by-digit numbers with dual encoding.

  — [IMO SMCP §7, §9, §10 (read)](https://aflopez.webs.ull.es/nautica/IMO_Standard_Marine_Communication_Phrases.pdf)
- Unverified claims from Trenkner (principal SMCP author), in the Nautical Institute's *Alert!* No. 14 (2007), which does not cite the underlying studies:
  - "One third of accidents happen primarily due to insufficient command of Maritime English."
  - In VTS areas "communicatively relevant factors contribute up to 40% of collisions involving the human element", mostly radio failures "even in routine conversations".
  - More than 86% of SOLAS vessels have multilingual crews.
  - SMCP familiarity was limited mainly to officers trained after 2001.

  — [Alert! Bulletin 14 (read)](https://www.nautinst.org/static/24046a9f-7411-47b5-a3c8261e08692552/Communication.pdf)

### Inferences
- Message markers are a direct, lexicalised solution to the Tenerife-type failure, where the *illocutionary force* of an utterance (statement vs action vs request) is misread. They also encode **who holds decision authority** (INSTRUCTION vs ADVICE). This is a dimension natural languages usually leave to politeness and context, and that dimension caused the Avianca under-marking.
- The "reply with full content" rule ("I will not overtake…") turns every acknowledgment into a readback. It is the maritime equivalent of aviation's readback and of I-PASS's "synthesis by receiver".
- Marker use is optional. This probably limits impact, but there is no data either way.

### Gaps
- **No empirical evaluation of message markers or SMCP effectiveness was found**: no trial, no before/after incident study, no compliance audit with numbers. This is the largest evidence gap in this note.
- No primary source located for the "one third of accidents" and "40% of VTS collisions" figures.
- Seaspeak (1980s precursor; Weeks et al.) was not researched in depth. Its relation to SMCP is known only from general sources.

## 4. Medicine: handoff errors, SBAR, I-PASS, closed-loop communication, "Do Not Use" abbreviations

### Takeaway
Communication failure is the most consistently reported contributor to serious harm in US healthcare: about 30% of malpractice cases, and the leading root cause of sentinel events 1995–2006. The strongest evidence that an engineered communication protocol reduces harm is I-PASS: a 23% relative reduction in medical errors and a 30% reduction in preventable adverse events across 9 hospitals and 10,740 admissions, though in a non-randomised pre/post design. SBAR evidence is moderate and heterogeneous. Closed-loop orders measurably speed task completion. Banning ambiguous abbreviations targets a real but modest share of errors.

### Cited Findings
- **CRICO Strategies 2015** analysed 23,658 malpractice cases (2009–2013):
  - Communication failures contributed to 7,149 cases (30%), linked to 1,744 deaths and $1.7 billion in costs.
  - They were involved in 37% of high-severity injury cases.
  - Settings: 48% ambulatory, 44% inpatient, 8% ED.

  — [Harvard RMF/CRICO news release](https://www.rmf.harvard.edu/News-and-Blog/In-the-News-Home/In-the-News/2016/February/Communication-failures-linked-to-1744-deaths-in-five-years); also cited in [Joint Commission SEA 58 (read)](https://digitalassets.jointcommission.org/api/public/content/a05e74ef89484e2084b6511189b73a99?v=279f39cc)
- Joint Commission Sentinel Event Alert 58 (2017):
  - A typical teaching hospital may have more than 4,000 hand-offs per day.
  - An ACGME study found 69% of clinical learning environments had no standardised hand-off process and only 20% had some standardisation.
  - Contributing factors: insufficient or misleading information, lack of a safety culture, poor timing between sender and receiver, interruptions, and lack of standardised procedures.
  - Recommendations include I-PASS and other mnemonics, face-to-face hand-offs, and time for questions.

  — [JC SEA 58 (read)](https://digitalassets.jointcommission.org/api/public/content/a05e74ef89484e2084b6511189b73a99?v=279f39cc)
- "Breakdown in communication was the leading root cause of sentinel events reported to the Joint Commission … between 1995 and 2006." — [WHO Patient Safety Solution 3 (search summary)](https://cdn.who.int/media/docs/default-source/patient-safety/patient-safety-solutions/ps-solution3-communication-during-patient-handovers.pdf)
- The often-repeated "communication failures in 50–80% of sentinel events" and "handoffs implicated in 80% of serious errors" circulate in secondary sources with inconsistent attribution. — [PSQH](https://www.psqh.com/analysis/patient-handoffs-gap-mistakes-made/) (treat as **unverified**)
- **I-PASS (Starmer et al., NEJM 2014)**:
  - Design: a prospective, multicentre pre/post intervention study in 9 pediatric residency programs and 10,740 admissions.
  - Medical errors fell 23%, from 24.5 to 18.8 per 100 admissions. Preventable adverse events fell 30%.
  - Written and verbal handoff quality improved.
  - There was no increase in handoff time and no decrease in residents' time with patients.

  — [Starmer et al. 2014, NEJM](https://www.nejm.org/doi/full/10.1056/NEJMsa1405556) (abstract via search summary; full text returned 403). Preventable adverse events went from 4.7 to 3.3 per 100 admissions according to my memory of the abstract; **this figure is not verified**.
- The I-PASS mnemonic is **I**llness severity, **P**atient summary, **A**ction list, **S**ituation awareness and contingency planning, **S**ynthesis by receiver. The last item is a built-in readback. — [JC SEA 58 (read)](https://digitalassets.jointcommission.org/api/public/content/a05e74ef89484e2084b6511189b73a99?v=279f39cc)
- **SBAR systematic review (Müller et al., BMJ Open 2018)**:
  - Across the included studies, 26 different patient outcomes were measured.
  - 8 improved significantly, 11 were described as improved without statistical tests, 6 did not change, and 1 showed a descriptive worsening.
  - The authors judged the evidence "moderate", strongest for telephone communication, with a lack of high-quality studies.

  — [Müller et al. 2018](https://www.researchgate.net/publication/327181945_Impact_of_the_communication_and_patient_hand-off_tool_SBAR_on_patient_safety_a_systematic_review)
- **Closed-loop communication (El-Shafy et al., J Surg Educ 2018)**:
  - The study reviewed 89 pediatric trauma activation videos with 387 verbal orders.
  - 32.6% of orders were directed to a named person, 96.1% were audible, and only 26.1% were closed-loop.
  - Closed-loop orders were completed 3.6× sooner (p<0.0001).
  - The mean time to complete an order was 3.85 min.

  — [El-Shafy et al.](https://www.sciencedirect.com/science/article/abs/pii/S1931720417300387)
- **"Do Not Use" list**:
  - Joint Commission issued a sentinel event alert on abbreviations in 2001, made a National Patient Safety Goal in 2002, and created the list in 2004.
  - The 2004 consultation drew 5,227 responses and 15,485 comments, with more than 80% supportive.
  - Of 643,151 MEDMARX medication errors (2004–2006), 29,974 (4.7%) involved abbreviations. The leading culprits were "QD" (43.1% of those), "U" for units (13.1%), "cc" (12.6%) and "MSO4/MS" (9.7%).

  — [AMN Healthcare summary of Joint Commission/MEDMARX data (secondary)](https://www.amnhealthcare.com/amn-insights/news/abbreviations-may-save-minutes-prohibiting-abbreviations-may-save-lives/); primary analysis is Brunetti et al. 2007, [Jt Comm J Qual Patient Saf](https://www.jointcommissionjournal.com/article/S1553-7250(07)33062-6/abstract) (abstract not opened)

### Inferences
- Medicine's dominant failure is **omission and incompleteness at a transfer of responsibility**, not mishearing. I-PASS fixes it with a *fixed information schema* (slots that must be filled, in a fixed order), plus a mandatory receiver synthesis. This is a different lever from aviation's lexical fixes: structure of content rather than form of words.
- "Illness severity" first is a stance/urgency marker leading the message. It is analogous to SMCP markers and MAYDAY/PAN-PAN, and to the Avianca lesson that urgency must be marked explicitly at the start.
- Closed-loop data show that loops are usually *not* closed in practice (26%), even in trained teams. A designed language should make the loop the default grammatical form, not an optional practice.
- The "Do Not Use" list is a negative lexicon: banning tokens with high confusion risk ("U" read as 0 or 4; "QD" vs "QID"). It is the written analogue of reserving "takeoff".

### Gaps
- No randomised controlled trial of I-PASS was found; the evidence is pre/post. Effects in other settings (adult, nursing) were not reviewed.
- No study was found that measures error reduction attributable to the "Do Not Use" list itself (before/after list adoption).
- The primary Joint Commission root-cause tabulations (yearly percentages) were not retrieved.

## 5. Simplified Technical English (ASD-STE100): evidence of improved comprehension

### Takeaway
STE restricts vocabulary to about 900 approved words, each with one meaning and one part of speech, and limits sentence length. Controlled experiments with aircraft maintenance technicians show it improves comprehension of *difficult* texts, with the biggest gains for non-native readers, and no gain on easy texts. The evidence base is small and dates from the 1990s.

### Cited Findings
- ASD-STE100 Issue 9 (2025) has about 53 writing rules in 9 sections and a dictionary of about 900 approved words. Each word has one approved meaning and one part of speech (e.g. "fall" = move down by gravity, not "decrease"). Sentences are at most about 20 words for procedures and 25 for descriptions. — [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) (rule counts via search summary; spec not opened)
- **Shubert, Spyridakis, Holmback & Coney (1995)**, *J. Tech. Writing & Communication*, tested SE vs non-SE aircraft maintenance procedures:
  - SE significantly improved comprehension of the more complex documents and made content easier to locate.
  - Reading/completion time did not differ.
  - Non-native speakers appeared to benefit more, though cell sizes were too unequal to test this statistically.

  — [Shubert et al. 1995](https://doi.org/10.2190/WG69-D74B-4DLL-2WBK) (abstract via search summary)
- **Chervak, Drury & Ouellette (1996)**, HFES Proceedings, tested 175 practising aircraft maintenance technicians on 16 workcards (easy/difficult × SE/non-SE × two layouts), between-subjects. SE significantly reduced comprehension errors on difficult workcards and for non-native speakers, with no difference on easy cards. — [Chervak et al. 1996](https://journals.sagepub.com/doi/abs/10.1177/154193129604000502) (abstract via search summary)

### Inferences
- Controlled language helps where the text is hard and the reader's English is weak. Simplification has little to add when the content is already simple. This suggests design effort should target high-complexity, high-consequence messages, matching aviation's nonlinear complexity curve.
- "One word, one meaning, one part of speech" is the written counterpart of the spelling-alphabet confusability criterion. Both remove polysemy as a failure source.

### Gaps
- No large or recent controlled studies of STE were found. There is no field data linking STE adoption to maintenance error rates.
- Effect sizes for Shubert 1995 and Chervak 1996 were not retrieved; only the abstracts were seen.

## 6. Military and emergency radio procedure words (prowords)

### Takeaway
Prowords such as OVER, OUT, ROGER, WILCO and SAY AGAIN are a closed set of **turn-taking and acknowledgment-level markers**, each with a single defined meaning. They separate "received" (ROGER) from "understood and will comply" (WILCO), and "reply expected" (OVER) from "conversation ended" (OUT). Their rationale is documented in the procedure manuals (ACP 125), but I found **no empirical effectiveness studies**.

### Cited Findings
- ACP 125 meanings:
  - ROGER = "I have received your last transmission satisfactorily".
  - WILCO = "I have received your message, understand it, and will comply". Saying "Roger, wilco" is redundant because WILCO includes ROGER.
  - OVER = "my transmission is ended and I expect a response".
  - OUT = "this is the end of my transmission to you and no answer is required or expected". So "over and out" is self-contradictory.

  — [Wikipedia, Procedure word (secondary, summarising ACP 125)](https://en.wikipedia.org/wiki/Procedure_word); [ACP 125(G) text](https://orwg.cap.gov/media/cms/ACP125GRadioTelephoneProceduresNOV2_EFFE1A51BA783.pdf) (not opened)
- Maritime counterparts are standardised in SMCP: urgency tiers MAYDAY (distress), PAN-PAN (urgency) and SÉCURITÉ (safety), and repair prowords "Say again", "Mistake…Correction" and "Repeat". — [IMO SMCP §5, §7, §9 (read)](https://aflopez.webs.ull.es/nautica/IMO_Standard_Marine_Communication_Phrases.pdf)

### Inferences
- Prowords grammaticalise conversation management: turn boundaries, acknowledgment *depth* (heard vs understood vs will act), and repair. On voice radio these are invisible by default because there is no overlap, gaze or backchannel.
- The three-tier urgency scale (MAYDAY/PAN-PAN/SÉCURITÉ, and aviation's MAYDAY/PAN-PAN plus "minimum fuel"/"emergency fuel") is the fix for Avianca-type under-marking. Urgency becomes a discrete, closed-class token rather than a matter of tone or politeness.

### Gaps
- No empirical study was found on proword error rates or on whether the ROGER/WILCO distinction reduces misunderstanding.
- Emergency-services radio (e.g. APCO's move from "10-codes" to plain language after 9/11 interoperability problems) was not researched; the NIMS/DHS plain-language guidance would be the source.

## 7. Synthesis: recurring failure types across domains and which fixes demonstrably worked

### Takeaway
Five failure types recur across all domains: **(1) reference/addressing**, **(2) numbers**, **(3) speech-act/force ambiguity**, **(4) urgency/stance under-marking**, **(5) unconfirmed or omitted content**. Two amplifiers sit on top: message overload and listener expectation. The fixes with *measured* benefit are few: closed-loop confirmation (I-PASS, closed-loop orders), structured content schemas (I-PASS), shorter/less complex messages (correlational FAA data), controlled vocabulary for hard texts (STE), and empirically tested distinctive vocabularies (the ICAO alphabet). Speech-act markers and urgency tiers are well-motivated by accidents but **unmeasured**.

### Cited Findings
- **Reference/addressing.**
  - Similar call sign was the top factor: 33% of 535 EUROCONTROL occurrences and 37% of its readback/hearback errors. [EUROCONTROL (read)](https://skybrary.aero/sites/default/files/bookshelf/162.pdf)
  - Similar call signs were also top in 386 ASRS reports. [Schroeder 2006 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200621.pdf)
  - Directed (named-recipient) orders were only 32.6% in trauma bays. [El-Shafy](https://www.sciencedirect.com/science/article/abs/pii/S1931720417300387)
- **Numbers.**
  - Headings and frequencies are the most frequent readback errors. [AM-06/25 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200625.pdf)
  - "Two/to" led to a crash into high ground. [Doc 9835 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)
  - The 10,000/11,000 ft confusion was in 38% of 191 altitude busts. [FSF](https://flightsafety.org/asw-article/failure-to-communicate/)
  - Digits are the most frequent words on the frequency. [ICAO 1959 (read)](https://www.governmentattic.org/4docs/ICAO-WordSpellingAlphabet_1959.pdf)
  - "U" and "QD" errors appear in MEDMARX. [AMN/MEDMARX](https://www.amnhealthcare.com/amn-insights/news/abbreviations-may-save-minutes-prohibiting-abbreviations-may-save-lives/)
- **Speech-act ambiguity.**
  - "We are at take-off". [Doc 9835 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)
  - SMCP QUESTION marker "removes any doubt on whether a question is being asked or statement being made". [SMCP (read)](https://aflopez.webs.ull.es/nautica/IMO_Standard_Marine_Communication_Phrases.pdf)
- **Urgency/stance.**
  - Avianca's "priority" vs "emergency". [Wikipedia/NTSB](https://en.wikipedia.org/wiki/Avianca_Flight_052)
  - I-PASS leads with "Illness severity". [JC SEA 58 (read)](https://digitalassets.jointcommission.org/api/public/content/a05e74ef89484e2084b6511189b73a99?v=279f39cc)
- **Confirmation/omission.**
  - 11 of 15 incorrect readbacks went undetected. [EUROCONTROL (read)](https://skybrary.aero/sites/default/files/bookshelf/162.pdf)
  - Only 26% of trauma orders were closed-loop. [El-Shafy](https://www.sciencedirect.com/science/article/abs/pii/S1931720417300387)
  - Incomplete or misleading information is the leading handoff factor. [JC SEA 58 (read)](https://digitalassets.jointcommission.org/api/public/content/a05e74ef89484e2084b6511189b73a99?v=279f39cc)
- **Overload.** The readback-error rate approaches 38% above complexity 16, versus 2–6% below 10. [AM-06/25 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/200625.pdf)
- **Compliance erosion.**
  - 70% of prescribed speech acts were non-compliant. [Doc 9835/Mell 1992 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)
  - 44% of pilots meet non-standard phraseology every flight. [FSF/IATA](https://flightsafety.org/asw-article/failure-to-communicate/)
  - Speakers omit and group numbers to save airtime. [AM-96/26 (read)](https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/AM96-26.pdf)
- **Limits of closed vocabularies.** 60% of one emergency dialogue required plain language. [Doc 9835 (read)](https://www.skybrary.aero/bookshelf/books/2497.pdf)

**Evidence strength of each fix**

| Fix | Evidence |
|---|---|
| Closed loop / receiver synthesis | Measured, though bundled: I-PASS (−23% errors) and closed-loop orders (3.6× faster). Readback catches most errors in aviation tape studies, but only if the sender listens. |
| Structured content schema | Measured (I-PASS). Moderate evidence for SBAR (Müller 2018). |
| Limit message complexity | Strong correlational field data (FAA 1993–2006); no intervention trial. |
| Controlled vocabulary, one word one meaning | Measured comprehension gains on hard texts (Shubert 1995; Chervak 1996). |
| Empirically chosen low-confusion lexicon | Measured in lab, significant at p<0.001 (ICAO 1959). |
| Reserved words, speech-act markers, urgency tiers, banned abbreviations | Accident-motivated rule changes; **no outcome measurement found**. |

### Inferences
Each point below is a candidate requirement for a language designed for faithful transmission of thought. Each is inferred from the above, not tested directly:
1. **Make the addressee and the referent explicit and distinctive.** Use identifiers chosen for low mutual confusability, not just uniqueness. This is the top real-world failure.
2. **Give numbers their own, maximally distinct encoding,** with mandatory type/unit tags (heading vs altitude vs speed) and digit-wise transmission. Prevent format leaking between number types ("three point five").
3. **Mark illocutionary force and authority overtly,** e.g. QUESTION/INSTRUCTION/ADVICE/INTENTION, as a leading, closed-class token. Accidents show the cost of leaving force to context. Effectiveness is unmeasured, so this is a hypothesis to test.
4. **Mark urgency and stance on a small discrete scale at the start of the message.** Do not leave them to prosody, politeness or paraphrase.
5. **Build confirmation into the grammar.** The receiver's reply restates content ("I will not overtake…") and distinguishes received / understood / will comply. The sender must check the echo; the data show hearback is where loops leak.
6. **Cap message complexity per turn.** Error rates are flat up to a threshold, then rise sharply.
7. **Choose vocabulary by measuring confusion matrices in noise with diverse speakers,** and re-test substitutions system-wide.
8. **Plan for erosion.** Speakers drop redundancy to save effort, and non-compliance runs at 44–70%. Either keep required forms short or make omissions detectable.
9. **Keep an escape hatch.** Closed codes fail in novel situations (60% plain language in one emergency), so the language needs a principled "plain" mode that still obeys the force, urgency, number and confirmation rules.

### Gaps
- There is no cross-domain dataset with consistent coding. The percentages come from incompatible taxonomies (EUROCONTROL occurrence factors, FAA readback errors, CRICO malpractice coding) and cannot be compared directly.
- Two candidate fixes have no outcome evaluation in any domain: speech-act markers and urgency tiers. They are the most interesting for the designed-language goal and also the least evidenced.
- Data link and text alternatives to voice (CPDLC; DABS in 1981) were out of scope. They would show which failures disappear once the acoustic channel is removed (homophones) and which persist (reference, expectation, omission).

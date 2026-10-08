# Numeric confidence marking (CONF 0–10): devil's-advocate evidence

Compiled 2026-10-08. Status tags: **[S]** sourced (read in the cited text or abstract), **[2nd]** read only in a secondary source, **[I]** my inference, **UNVERIFIED** couldn't check.

## 1. Speakers prefer words, listeners prefer numbers

- The "communication mode preference paradox": on average, senders prefer verbal probabilities and receivers prefer numeric ones (Brun & Teigen 1988; Erev & Cohen 1990; Wallsten et al. 1993) [S, as summarised in Mandel et al., JDM 2021 and Dhami & Mandel, TiCS 2022].
- **Wallsten, Budescu, Zwick & Kemp 1993**: 45% said they usually prefer to *give* uncertainty in words; 70% said they would rather *receive* numbers [2nd, from Juanchich & Sirota 2020; primary paywalled]. Note that 45% is not a majority, so "most senders prefer words" overstates this study. Senders' stated reasons: words are easier and "more natural" to produce [2nd].
- **Erev & Cohen 1990**: 3 of 4 basketball experts used words for 25 of 26 predictions. 21 lay "experts" produced 67% verbal phrases. Their blame-avoidance hypothesis got little support: experts didn't switch to words more when listeners had money riding on the prediction [2nd, Juanchich & Sirota].
- **Brun & Teigen 1988**: 50 of 66 Norwegian GPs (76%) would tell a patient about a vaccine's chances in words [2nd]. Patients were split 35% words, 32% numbers (Mazur & Hickam 1991) [2nd].
- The preference depends on the kind of uncertainty. Epistemic (lack of knowledge) and dispositional uncertainty go into words; distributional uncertainty (frequencies) goes into numbers; the gap shrinks when vagueness is held constant [S, Juanchich & Sirota abstract]. When stakes are high, both sides lean numeric [S, Dhami & Mandel].
- In real use, family physicians gave a numeric risk in only 11% of 70 consultations, and 99.9% of probabilistic National Weather Service tweets were verbal [2nd].

## 2. Single-event probability and the reference class

- **Gigerenzer et al. 2005** surveyed pedestrians in five cities about "30% chance of rain tomorrow". Only in New York did a majority give the meteorological reading ("in 3 of 10 days like this, it rains"). European respondents preferred "rain 30% of the time" or "in 30% of the area". Cities had different exposure to probability forecasts. The authors' fix: *state the reference class* [S].
- **Gigerenzer & Hoffrage 1995**: Bayesian answers rose from 16% (probability format) to 46% (natural-frequency format), and 50% with the short menu [S].
- **What this means for "7 in 10"** [I]: the confusion in the rain study was about *what event* the number covers (area, time, days like today), not about percent versus "x in 10". "7 in 10" on a single event still needs an implied reference class. The natural-frequency advantage comes from nested counts during reasoning, and wording a single-event estimate as a fraction doesn't supply that. Your grammar has one real advantage: the proposition the particle scopes over *is* the event. The precision burden moves onto the proposition ("storm reaches *this town* *tomorrow*").

## 3. How many levels people can actually use

- **Friedman et al. 2018** (888,328 Good Judgment Project forecasts) rounded forecasts into coarser bins and measured the accuracy lost [S]:
  - Untrained individuals lost almost nothing at **7 equal bins**: mean Brier penalty 0.5%, median 0.2% (not significant). They lost 5.9% at 3 bins and 15% at 2 bins.
  - Superforecasters lost 40% at 7 bins and 236% at 3 bins. The average superforecaster could reliably use **11.3 bins** (SD 5.6).
  - Across questions, the mean usable precision was 6.1 bins (SD 4.4), and more than 7 bins were usable for 42% of questions.
  - Precision gains were predicted by an hour of training, teamwork and practice. Numeracy and education didn't predict them.
  - Left unconstrained, forecasters mostly answered in steps of 5 points.
  - Caveat: the sample was not ordinary people (83% male, highly educated volunteers).
- **Fischhoff & Bruine de Bruin 1999**: open-ended probability questions produce an excess of "50" answers, used as "fifty-fifty", meaning "no idea". The spike vanishes when the response scale has explicit options [S].
- Words are far fuzzier: "possible" spans 63 points for some physicians [S, Dhami & Mandel].

## 4. Calibration and whether practice fixes it

- Overconfidence comes in three kinds: overestimation, overplacement and overprecision. Overprecision is the most persistent. On hard tasks people overestimate themselves; on easy tasks they underestimate [S, Moore & Healy 2008].
- **Weather forecasters** (Murphy & Winkler 1977, Chicago office, 1972–76): 17,514 rain forecasts on the allowed values 0, 2, 5, 10, 20 … 90, 100%. Calibration was "excellent": on days forecast at 30%, it rained 28.5% of the time (449 of 1,574). There was a slight tendency to overforecast [S]. US forecasters have issued probability-of-precipitation forecasts since 1965 [S].
- **GJP training**: a module under one hour improved Brier scores 6–11% over controls (Chang et al. 2016) [S, search abstract]. Forecasters were about 3% overconfident; training plus teams cut that to 1% (Moore et al. 2016) [S].
- **Canadian intelligence analysts** (Mandel & Barnes 2014): 1,514 forecasts on the scale 0, 1, 2.5, 4, 5, 6, 7.5, 9, 10 *out of 10*. Discrimination was very good (AUC 0.94), and the analysts were slightly *under*confident [S].
- **Will a culture that habitually states numbers become calibrated?** The evidence points to feedback, not habit:
  - LessWrong, a community that talks in probabilities (2014 survey, 1,503 respondents): people 50% sure of one answer were right 13% of the time, and people 100% sure were right 44% of the time. Calibration didn't correlate with prior calibration training, and veterans did no better than newcomers [S, Scott Alexander's survey write-up; informal data].
  - Weather forecasters and GJP forecasters, who get scored outcomes, are calibrated [I].
  - So habit alone is not enough. Calibration should emerge where claims resolve quickly and visibly (weather, "will he come"), but not for rare or long-horizon claims [I].

## 5. Numeracy and development

- **Lipkus et al. 2001** (463 highly educated adults aged 40+): 16–20% failed "Which is the larger risk: 1%, 5% or 10%?" [S].
- **Peters et al. 2006**: less numerate people are more swayed by framing and by irrelevant affect, and this isn't explained by intelligence [S]. Precise numbers don't measurably hurt even very low-numeracy receivers [S, Dhami & Mandel].
- **Infants**: 12-month-olds form Bayesian-like expectations (Téglás et al. 2011) [S]. Infants under 12 months are sensitive to *proportions*, not just counts (Denison & Xu 2014) [S].
- **Children**:
  - Before about age 5, children's verbal judgments show no grasp of probability, and in choice tasks only 5-year-olds chose optimally (Girotto et al. 2016) [S].
  - Children's numeric readings of everyday uncertainty words converge on adults' from about **age 9** (Meder et al. 2022, ages 4–14) [S].
  - Rated age of acquisition: "maybe" 4.5 years, "likely" 6.3, "percent" 8.2, "percentage" 10.3 [2nd, Kuperman norms via Juanchich & Sirota].
- **Unschooled adults**: Kaqchikel and K'iche' Maya adults without schooling matched Western controls on tasks involving proportions and priors (Fontanari et al. 2014) [S]. Probabilistic intuition doesn't need school maths; a 0–10 integer scale avoids percentages and fractions altogether [I].

## 6. Social costs

- **Directionality**: verbal terms point toward occurrence ("a small chance") or non-occurrence ("unlikely") whatever the probability (Teigen & Brun 1995) [S]. Listeners infer what the speaker expected from the direction. They draw no such inference from point numbers, which are read as positively directional [S, Dhami & Mandel].
- **Politeness**: "possible" is read as *more* probable the more severe the condition, because listeners take it as tact rather than uncertainty (Bonnefon & Villejoubert 2006) [S]. Speakers say "small probability" for a 50% loss when sparing a friend's face [S, Dhami & Mandel]. "There's a 25% chance I'll have to let you go" sounds unnatural [2nd].
- **Credibility after a miss**: an "unlikely" forecast that turns out wrong costs *more* credibility than "20%" [S, Dhami & Mandel].
- **Strategic vagueness**: Tetlock says pundits use "vague verbiage" ("there could be…") to be "often wrong, but never in error" [S, Edge talk]. At the Bay of Pigs, the Joint Chiefs privately meant about 30% but wrote "a fair chance", which Kennedy read as favourable [S, Friedman et al. 2018].
- **Probability versus confidence**: the US intelligence standard ICD 203 has seven likelihood bands (1–5% … 95–99%). It bars putting a confidence level and a likelihood in the same sentence [S, repo transcription of ICD 203; the official PDF wouldn't download]. Even experts conflate the two, and over half of non-experts gave incoherent numbers for "likely" and "unlikely" (Irwin & Mandel 2023) [S].

## 7. Communities that use numbers

Each case is covered above:
- **Weather services** and **Canadian intelligence analysts** use numbers and are calibrated.
- **Forecasting tournaments** use numbers, which makes scoring and training possible.
- **Rationalists** talk in probabilities without systematic scoring and are miscalibrated.
- **Medicine** stays verbal.
- **Poker players**: **UNVERIFIED**, not researched.

## Implications for the design

**Does it work?** Mostly yes [I]:
- Receivers want numbers.
- Untrained people can use about 7 levels with no loss, and skilled people about 11, so 0–10 is the right ceiling.
- Real organisations have used out-of-10 scales with good calibration.
- Unschooled adults and young children have the underlying intuition.

The main obstacles are social and pragmatic, not cognitive.

**What to change** [I]. Per your working rules, here are the parts with their sources:

1. **Particle + 0–10** (your design). Keep it. Expect speakers to cluster on 0, 5 and 10 plus a few favourite values. That's fine, because untrained users lose almost nothing at 7 levels.
2. **"Don't know how sure" marker** (your design). Keep it. It's exactly the fix Fischhoff & Bruine de Bruin found: give "no idea" its own slot so it doesn't pollute 5.
3. **What 0 and 10 mean** (my addition, prompted by NWS's 2%/5% steps and the IAS and ICD bands). If 10 means certainty, the scale has no slot for "near-certain". Two options: reserve 0 and 10 for logical certainty and add a near-end particle, or define 1 and 9 as "1 or 2 in 20". Add-back trigger: speakers coin their own "almost-10" idiom.
4. **Unmarked default = plain assertion**, roughly "I'd act on it" (refines your "ordinary belief"). Marking will carry implicature: "CONF 9 the sun rose" signals doubt. Write that down rather than fight it.
5. **Directionality comes from polarity, not new particles** (my addition). "CONF 3 storm comes" and "CONF 7 storm doesn't-come" carry the same probability with different focus. That restores the pragmatic channel words have and numbers lack. Expect politeness to migrate into this choice.
6. **Event versus evidence** (my addition, from ICD 203 and Irwin & Mandel). Decide whether CONF means "chance it's true" or "how solid my grounds are". Make it the first, and let the don't-know marker cover the second. Add-back trigger for a separate evidence-strength marker: speakers routinely tack on "but I'm guessing" phrases.
7. **"7 in 10" gloss**: harmless, but it doesn't solve the reference-class problem. The proposition has to name the event precisely.

Deletion candidate: no separate verbal hedge system should be designed in. It will grow on its own (politeness, face-saving).

**Remaining risks** [I]:
- **Calibration**: a culture full of numbers won't be calibrated without feedback, as the LessWrong data shows. It will be calibrated in fast-resolving everyday domains and overconfident on hard or rare questions (the hard–easy effect).
- **Accountability**: numbers make people checkable. Expect social pressure to retreat into unmarked statements, which become the new "vague verbiage". Watch what the unmarked form comes to imply.
- **Children**: they'll use the particle years before using it accurately. Expect their mappings to converge on adults' around age 9, as with verbal terms.

## Sources

- Dhami & Mandel 2022, "Communicating uncertainty using words and numbers", *TiCS* 26(6). https://doi.org/10.1016/j.tics.2022.03.002 (read via repository PDF: https://repository.mdx.ac.uk/download/4b3cfb68b0304e53c4f693e5f763d20b16f65cc3230d821be96137fb3395851c/936229/CellPress%20logo)
- Juanchich & Sirota 2020, "Do people really prefer verbal probabilities?", *Psychological Research*. https://repository.essex.ac.uk/24764/
- Mandel et al. 2021, "Facilitating sender-receiver agreement…", *JDM*. https://sjdm.org/~baron/journal/20/200930/jdm200930.html
- Wallsten et al. 1993, *Bull. Psychonomic Soc.* 31:135 (paywalled). https://doi.org/10.3758/BF03334162
- Erev & Cohen 1990, *OBHDP* 45:1 (not read). https://doi.org/10.1016/0749-5978(90)90002-q
- Gigerenzer et al. 2005, *Risk Analysis* 25:623. https://doi.org/10.1111/j.1539-6924.2005.00608.x
- Gigerenzer & Hoffrage 1995, *Psych. Review*. https://pure.mpg.de/rest/items/item_2543495_7/component/file_2562163/content
- Friedman et al. 2018, *ISQ* 62(2). https://sites.dartmouth.edu/friedman/files/2017/06/Value-of-Precision-June-17.pdf
- Fischhoff & Bruine de Bruin 1999, *JBDM* 12:149. https://doi.org/10.1002/(SICI)1099-0771(199906)12:2<149::AID-BDM314>3.0.CO;2-J
- Moore & Healy 2008. https://pubmed.ncbi.nlm.nih.gov/18426301/
- Murphy & Winkler 1977, *National Weather Digest*. http://nwafiles.nwas.org/digest/papers/1977/Vol02No2/1977v002no02-MurphyWinkler.pdf
- Mellers et al. 2014. https://pubmed.ncbi.nlm.nih.gov/24659192/
- Moore et al. 2016, *Mgmt Sci*. https://escholarship.org/uc/item/1700r340
- Chang et al. 2016, *JDM*. https://www.sas.upenn.edu/~baron/journal/16/16511/jdm16511.html
- Mandel & Barnes 2014, *PNAS*. https://pmc.ncbi.nlm.nih.gov/articles/PMC4121776/
- LessWrong 2014 survey results. https://www.greaterwrong.com/posts/YAkpzvjC768Jm2TYb/2014-survey-results
- Lipkus et al. 2001. https://pubmed.ncbi.nlm.nih.gov/11206945/
- Peters et al. 2006. https://pubmed.ncbi.nlm.nih.gov/16683928/
- Téglás et al. 2011, *Science*. https://doi.org/10.1126/science.1196404
- Denison & Xu 2014. https://pubmed.ncbi.nlm.nih.gov/24384147/
- Girotto et al. 2016. https://pubmed.ncbi.nlm.nih.gov/27015350/
- Fontanari et al. 2014. https://pubmed.ncbi.nlm.nih.gov/25368160/
- Meder et al. 2022. https://pubmed.ncbi.nlm.nih.gov/34291870/
- Bonnefon & Villejoubert 2006. https://pubmed.ncbi.nlm.nih.gov/16984289/
- Teigen & Brun 1995, *Acta Psychologica* 88:233 (abstract via search only).
- Irwin & Mandel 2023, *Risk Analysis*. https://doi.org/10.1111/risa.14009
- ICD 203 likelihood table (transcription). https://github.com/wesinator/ICD203-intel-analysis
- Tetlock, Edge master class. https://www.edge.org/conversation/philip_tetlock-a-short-course-in-superforecasting

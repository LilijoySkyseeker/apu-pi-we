# Human and cognitive evidence for choosing a number base

Written 2026-10-08. Labels: **[sourced]** means I read it in the cited source. **[inferred]** is my reasoning across sources. **UNVERIFIED** means recalled or found only in secondary or advocacy text. Derived numbers come from a small awk script (formulas are given inline).

**Bottom line.** No study has compared bases for human use head-to-head. The best recent review says so directly, and lists "whether base-10 is easier to learn than base-3" as future work (Göbel, Inglis & Bahnmueller 2025). The well-known language effects, such as the Chinese counting advantage, all compare **base-10 against base-10**. They measure **regularity**, not base size. The base-specific evidence is indirect. Smaller bases need fewer facts to memorise. Larger bases pack more information into each spoken item.

## 1. Number-word transparency and learning

- **Miller, Smith, Zhu & Zhang 1995** (*Psych Sci* 6:56). 99 Chinese and 98 US children aged 3–5. **[sourced]** No difference in counting up to 10: 94% of US and 92% of Chinese children reached 10. The gap opened in the teens: 74% of Chinese children counted to 20, against 48% of US children. From 20 to 99 there was no significant difference, and both groups made "scalloped" errors at decade boundaries. After 100 the Chinese children dropped off *more*, which the authors tie to the irregular *ling* in Chinese 101–109. Object counting of small sets and simple problem solving showed no difference. The same base produced different outcomes depending on where the irregularities sat.
- **Ho & Fuson 1998** (*J Educ Psych* 90:536). **[sourced, abstract via search]** At 5, about half the Chinese children with average or higher ability understood teen numbers as ten plus ones. English-speaking 5-year-olds in the UK and US showed no such understanding.
- **Fuson & Kwon 1992**. **[sourced, abstract via search]** Korean first-graders, *before* being taught sums over 10, solved 95% of problems that make 10, 85% of single-digit sums from 10 to 18, and 75% of matching subtractions. The authors credit the named-ten words ("ten-two") together with finger methods structured around ten.
- **Base held constant, culture held constant:** these studies show transparency helps, but only narrowly.
  - Mark & Dowker 2015 compared Hong Kong children in Chinese-medium schools, Hong Kong children in English-medium schools, and UK children. Chinese-medium pupils were better at counting backward, but there was "no statistical difference in counting forward, place value understanding, and a measure of arithmetic" **[sourced]**.
  - In Wales, Dowker et al. 2008 found Welsh-medium pupils better at reading and comparing two-digit numbers, with no difference in overall arithmetic **[sourced, via Dowker & Roberts 2015]**.
  - Vietnamese preschoolers beat Belgian francophone ones "only in counting" (Lê & Noël 2020) **[sourced]**.
- **Inversion** (German "five-and-twenty") is a separate, well-replicated cost. Up to 50% of German-speaking children's transcoding errors are inversion errors **[sourced, Göbel et al.]**. Norway changed its number words in 1951 after the telegraph agency saw fewer errors with words that follow digit order **[sourced, Göbel et al.]**.
- **What drives the advantage?** Göbel et al. 2025: the natural-language evidence "does not allow us to disentangle whether the explicit presence of the base … or the systematic use of generative transparent rules" is responsible **[sourced]**. Either way it is a property of the **naming scheme** and says nothing about the base's size. An intervention that taught English and Spanish pre-K children explicit "one-ten one" names gave achievement gains years later (Magargee & Beauford 2016) **[sourced, ERIC abstract via search; one study]**.
- **A small-base point.** Holt & Barner 2025 taught preschoolers number systems anchored at 2 and at 3. Children picked up additive composition ("two-and-one") early, sometimes before they could count large sets **[sourced]**. **[inferred]** In a smaller base the rule-built words start earlier (at 7 in base 6, at 13 in base 12), so children meet the composition rule sooner and get more examples of it.

## 2. Arithmetic facts

- **How many facts.** Nontrivial multiplication facts, using operands 2…b−1 and counting commutative pairs once (squares included), number (b−2)(b−1)/2: **base 6: 10, base 8: 21, base 10: 36, base 12: 55, base 16: 105**. Addition facts using operands 1…b−1 number b(b−1)/2: **15 / 28 / 45 / 66 / 120**. Base 12 has 5.5× base 6's multiplication load and 1.5× base 10's.
- **Does a smaller set mean faster learning?** The best experimental evidence is Logan & Klapp 1991, on alphabet arithmetic (letters used as a novel counting system). **[sourced]**
  - Over 12 sessions with 40 facts, the reaction-time slope per counting step fell from 486 ms to 45 ms: counting was replaced by retrieval.
  - Rote memorising 6 facts gave the same automaticity in one session.
  - Their Experiment 3 found that "learning rate [depends] on the number of presentations of individual items, not on the number of items to be learned."
  - **[inferred]** So for a fixed amount of practice, total learning time scales roughly with table size: base 6 needs about 0.28× the drill of base 10, and base 12 about 1.5×.
- **Problem-size effect.** Problems with larger operands are slower and more error-prone. Structural size indices explain about 20–40% of latency variance. Ties and ×5 problems are exceptions, and 40–80% of adult errors are operand-related, e.g. 6×8 answered as "42" (LeFevre et al. 1996, citing Campbell & Graham 1985) **[sourced]**. Adults retrieve about 80% of products and fall back on rules or derived facts for the rest **[sourced]**. **[inferred]** Base 12 adds a band of larger, harder problems (7–11 × 7–11). Pattern-rich columns (×2, 3, 4, 6, and ×11) could be handled by rules, the way ×5 and ×9 are in base 10. That is plausible but untested.
- **Interference.** De Visscher & Noël 2014 found that how much a problem's digits overlap with earlier-learned problems predicts its difficulty, in children and adults **[sourced]**. **[inferred]** This partly offsets base 6's advantage: with only 6 symbols, the 10 facts overlap heavily. There are far fewer of them, though, and no study measures the net effect.
- **Fewer symbols, longer procedures.** Göbel et al. cite Schlimm & Neth's analysis of Roman numerals: fewer symbols lower the long-term-memory load, but arithmetic algorithms need more steps **[sourced; theoretical, untested on people]**. Base 6 has the same trade-off: about 28% more digit positions means more column operations and carries per calculation **[inferred]**.
- **Training in non-decimal bases.** Göbel et al. list everything they found **[sourced]**:
  - Weiers et al.: 204 adults learned a novel base-3 place-value notation and compared numbers with 81% accuracy on trained numerals and 76% on untrained ones.
  - Krajcsi & Szabó: over 95% accuracy with explicit rules.
  - Herman et al.: about 15% of 700 computer-science students misread positional weights in other bases, and about 25% believed numbers written in a larger base are bigger. Interference from decimal is the likely cause.

  None of these tested fluent arithmetic, and none compared bases with each other.
- Aitken (1962) said he calculated "more than one-and-a-half times as fast" in duodecimal. That is the self-report of one expert mental calculator: an anecdote, not evidence **[sourced as a quotation via Wikipedia; original *Listener* article not read]**.

## 3. Working memory for spoken numbers

- **Span tracks speaking time.** In Schweickert & Boruff 1986, span equalled about what can be said in 1.5 s, with an estimated mean trace of **1.88 s** **[sourced]**. In Baddeley et al. 1975, lists of five one-syllable words were recalled correctly over 90% of the time, against about 50% for five-syllable words **[sourced via Mattys et al.]**. Caplan et al. 1992 found the effect follows syllable and phoneme count, not articulatory duration as such **[sourced]**. **For design purposes, count syllables.**
- **Cross-language evidence.**
  - Welsh digits take longer to say than English ones, and Welsh digit span is shorter (Ellis & Hennelly 1980) **[sourced, abstract via search]**. That they also found more errors in mental arithmetic in Welsh is **UNVERIFIED**.
  - Chinese adults hold 9–10 digits, against 7 for American students. Mandarin digits take about 320 ms each, English about 420 ms. Chinese 4- to 6-year-olds already show the advantage in forward span but not backward span (Chen & Stevenson 1988, summarising Stigler, Lee & Stevenson 1986 and Hoosain) **[sourced]**.
  - Mattys, Baddeley & Trenkic 2018 found digit span of 8.84 in Mandarin against 6.94 in English, with articulation of 6.44 against 4.47 syllables/s. But articulation rate left 73–89% of span variance unexplained, so storage differences also contribute **[sourced]**.
  - Chen & Stevenson report that the advantage vanishes for words; Mattys et al. found it for words too. The sources conflict.
- **Items, not bits.** Miller 1956, summarising Hayes: span is about 9 for binary digits and about 5 for monosyllabic words, "far less" variation than constant information would require. "Immediate memory is limited by the number of items." In Smith's recoding, span was 9 binary digits but 7 octal digits, i.e. 9 bits against 21 bits **[sourced]**. Cowan 2001 puts the core capacity at about 3–5 chunks **[sourced, abstract via search]**.
- **Quantified for this language** [inferred, all from length = log(10)/log(b)]:
  - A base-6 number has 1.285× as many digits as the same number in decimal. A base-12 number has 0.927×.
  - A million takes 8 digits in base 6, 7 in base 10 and 6 in base 12. A billion takes 12, 10 and 9.
  - A 7-item span holds about 5.4 decimal digits' worth of value in base 6 (6⁷ ≈ 280,000), 7.0 in base 10, and 7.5 in base 12.
  - Syllables per decimal digit's worth of value:

    | base and digit words | syllables |
    |---|---|
    | base 6, short words | 1.29 |
    | base 12, short words | 0.93 |
    | base 12, long words | 1.85 |
    | base 6, long words | 2.57 |

  - Base 6's 28.5% length penalty is about the size of the English-to-Mandarin duration gap (420/320 ms = 1.31×), which goes with about 2 digits of span. So base 6 with one-syllable digits costs roughly what English costs relative to Chinese.
  - Base 12 with *two-syllable* digits is worse than base 6 with one-syllable digits. **Digit-word length matters more than the base.**

## 4. Subitizing and estimation

- Subitizing covers about 3–4 items. Revkin et al. 2008 found precision for 1–4 far above what Weber's law predicts, which points to a dedicated mechanism **[sourced]**. Children map "one" to "four" onto small-set representations *before* learning the counting principles. Numerals above four map onto approximate magnitudes only about six months after (Le Corre & Carey 2007) **[sourced]**.
- The approximate number system is imprecise and sharpens until late childhood (Halberda & Feigenson 2008) **[sourced]**. The Mundurukú compare large approximate quantities well but fail exact arithmetic above 4–5 (Pica et al. 2004) **[sourced]**.
- **Interaction with base:** I found no empirical work. **[inferred]** Exact digit values are symbols, so a base of 6, 10 or 12 doesn't touch the subitizing limit. A digit drawn as dots could be subitized whole only in bases ≤5. Mental-abacus users store each column as one unit with internal structure (Frank & Barner 2012) **[sourced]**. The soroban's 1+4 bead split keeps each group within the subitizing range, but the bead layout is **UNVERIFIED** here, from memory. A base-12 column would need a sub-base such as 2×6 or 3×4.

## 5. Fingers and the body

- **Distribution of bases.** WALS chapter 131 (196 languages): 125 decimal, 22 hybrid vigesimal–decimal, 20 pure vigesimal, 20 restricted, 5 "other base", 4 body-part systems **[sourced]**. Base 6 is attested in Kómnzo, which has power words for 6¹ through 6⁶ and is used for counting yams, and in Ndom **[Wikipedia; primary grammar is Döhler 2016, not read]**. Base 12 is attested in some languages of Nigeria's Middle Belt and in Chepang **[Wikipedia, not traced]**.
- **Thumb on phalanges counting to 12.** The method is used in parts of Asia. Ifrah's claim that duodecimal *originated* there is "speculative" **[Wikipedia's wording; Ifrah not read]**.
- **Two-hand senary counting to 35** (one hand for units, the other for sixes). It appears only in advocacy sources and Wikipedia's Senary article. **UNVERIFIED as any culture's traditional practice.**
- **Bender & Beller 2012** (*Cognition*): finger counting varies culturally far more than research assumes, and its properties (base, sub-base, extent) have "representational effects" on learning and memory load **[sourced]**.
- **Children.**
  - Finger use goes with *higher* accuracy in kindergarten and first grade. By second grade, better performers use fingers less (Jordan et al. 1992, 2008, via Soylu, Lester & Newman 2018) **[sourced]**.
  - Finger gnosis predicts later number skills (Noël 2005). Eight weeks of finger-differentiation training improved quantification (Gracia-Bafalluy & Noël 2008, n=47) **[sourced]**. Two published comments followed; that they were critical (Fischer 2010) is **UNVERIFIED**.
  - **[inferred]** The scaffold that helps is one finger per unit, raised. Base-10 counting gets this on two hands, and the full set of fingers equals one unit of the next place. Two-hand base-6 counting also raises one finger per unit, but uses each hand as one place value. That shows place value directly, but stops at 35. Phalanx counting points to positions rather than raising fingers, so it is ordinal and harder to read at a glance. No study compares these for children.

## 6. Direct comparisons

None found. Göbel et al. 2025 is the most recent review, part of a 2025 *Phil Trans B* theme issue on bases. It covers no head-to-head human study and calls for artificial-numeral experiments. Advocacy arguments for base 6 (fewer facts, fingers) and base 12 (divisibility, Aitken) are hypotheses. Divisibility is a mathematical property, not cognitive evidence, and is outside this note.

## Implications for choosing a base

1. **Regularity outweighs base, strongly.** Every replicated naming effect (teens, inversion, irregular hundreds) comes from irregularity within base 10. Any base needs fully transparent words in digit order, with no special teens. This is the largest lever, and this language already pulls it. **Strength: strong.**
2. **Smaller tables favour the smaller base, moderately.** Learning time depends on presentations per fact (Logan & Klapp), so base 6's 10 facts against base 10's 36 and base 12's 55 should mean less drill and fewer retrieval errors. The base-specific claim is still an extrapolation, partly offset by symbol-overlap interference and longer procedures. **Favours 6 over 10 over 12. Strength: moderate, indirect.**
3. **Memory and speech favour the larger base, moderately.** Span is limited by items and syllables, not bits. Base 6 needs 28.5% more digits, about the English-versus-Chinese gap. Base 12 saves about 7% over decimal. **Favours 12 ≥ 10 > 6, but only with one-syllable digits.** With two-syllable digits, any base loses badly.
4. **Early composition favours a small base, weakly.** Children learn combining rules earlier when small anchors make them visible (Holt & Barner). **Strength: weak; one recent study.**
5. **Subitizing and number sense are close to neutral.** No evidence links them to base choice among 6, 10 and 12. **Strength: negligible.**
6. **Fingers favour 10, weakly.** One finger per unit across both hands is what the evidence supports and what most of the world's languages reflect. Base 6 and base 12 body schemes exist but are untested with children. **Strength: weak.**
7. **The trade-off is between learning and using.** Base 6 is cheaper to learn, which children pay for once. Base 12 is cheaper to hold and say, which everyone pays for in every utterance. A base-6 language that keeps one-syllable digits roughly cancels its length cost. **[inferred]**

On cognitive grounds alone, the evidence can't decide between 6, 10 and 12. The differences are modest and pull in opposite directions. Non-cognitive factors (divisibility, measurement, the junctures in `senary-review.md`) may well decide it.

## Sources

- Göbel, Inglis & Bahnmueller 2025, "The cognitive processing of numerical bases: a review", *Phil Trans R Soc B* 380:20240221. https://pmc.ncbi.nlm.nih.gov/articles/PMC12536281/ (read in full via Europe PMC)
- Holt & Barner 2025, *Phil Trans B* 380:20240535. https://pubmed.ncbi.nlm.nih.gov/41111295/
- Miller, Smith, Zhu & Zhang 1995, *Psych Sci* 6:56–60. https://siegler.tc.columbia.edu/wp-content/uploads/2019/12/4027Reading-Miller-etal-1995.pdf
- Ho & Fuson 1998. https://karenfusonmath.net/wp-content/uploads/2023/06/43-Teen-Numbers-Chinese-English-Speakers-JEdPsych-1998.pdf (abstract via search only)
- Fuson & Kwon 1992. https://www.semanticscholar.org/paper/Korean-Children's-Single-Digit-Addition-and-Numbers-Fuson-Kwon/3634b2b61f171e985b5529be2b39e2fd63e6fcf0 (search snippet)
- Mark & Dowker 2015, *Front Psychol* 6:203. https://pubmed.ncbi.nlm.nih.gov/25767456/
- Dowker & Roberts 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4493320/
- Lê & Noël 2020, *PLoS One*. https://pubmed.ncbi.nlm.nih.gov/33284824/
- Magargee & Beauford 2016. https://eric.ed.gov/?id=EJ1099346
- Logan & Klapp 1991, *JEP:LMC* 17:179. http://www.psy.vanderbilt.edu/faculty/logan/1991LoganJEPLMC.pdf
- LeFevre et al. 1996, *JEP:General* 125:284. https://siegler.tc.columbia.edu/wp-content/uploads/2019/12/4027Reading-LeFevre-etal1996.pdf
- De Visscher & Noël 2014. https://pubmed.ncbi.nlm.nih.gov/25347536/
- Campbell & Xue 2001. https://pubmed.ncbi.nlm.nih.gov/11409105/
- Schweickert & Boruff 1986. https://pubmed.ncbi.nlm.nih.gov/2942626/
- Caplan, Rochon & Waters 1992. https://pubmed.ncbi.nlm.nih.gov/1410554/
- Mattys, Baddeley & Trenkic 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC5880866/
- Chen & Stevenson 1988, *JECP* 46:150. https://escholarship.org/content/qt6fq5v9j3/qt6fq5v9j3_noSplash_222c38eb426b848bc6a22223c7e1fe29.pdf
- Ellis & Hennelly 1980. https://www.semanticscholar.org/paper/A-bilingual-word%E2%80%90length-effect:-Implications-for-of-Ellis-Hennelly/2aaee2b19c8c539d67e4b512fb76629745a8ee2c (page blocked; abstract via search)
- Stigler, Lee & Stevenson 1986, *Cognition* 23:1. https://www.sciencedirect.com/science/article/abs/pii/001002778690051X (blocked; results via Chen & Stevenson)
- Miller 1956. http://psychclassics.yorku.ca/Miller/
- Cowan 2001. https://philpapers.org/rec/COWTMN
- Revkin et al. 2008. https://pubmed.ncbi.nlm.nih.gov/18578852/
- Le Corre & Carey 2007. https://pubmed.ncbi.nlm.nih.gov/17208214/
- Halberda & Feigenson 2008. https://pubmed.ncbi.nlm.nih.gov/18793076/
- Pica et al. 2004. https://pubmed.ncbi.nlm.nih.gov/15486303/
- Frank & Barner 2012. https://pubmed.ncbi.nlm.nih.gov/21767040/
- Bender & Beller 2012. https://pubmed.ncbi.nlm.nih.gov/22695379/
- Soylu, Lester & Newman 2018, *J Numer Cogn* 4:107. https://jnc.psychopen.eu/index.php/jnc/article/view/5787
- Gracia-Bafalluy & Noël 2008. https://pubmed.ncbi.nlm.nih.gov/18387567/
- WALS ch. 131 (Comrie). https://wals.info/chapter/131
- Wikipedia, Duodecimal: https://en.wikipedia.org/wiki/Duodecimal; Kómnzo: https://en.wikipedia.org/wiki/K%C3%B3mnzo_language (secondary)

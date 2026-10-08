# Number base: the mathematics and practice of 6, 8, 10, 12 and 16

Written 2026-10-08. The premise is that legacy convention is void, so "the world already uses decimal" counts for nothing. Every number below without a citation was computed by `/tmp/basenotes/bases.py` (sympy; not committed). **[inferred]** marks my reasoning; **recalled** marks memory I did not verify this session (treat as UNVERIFIED).

## 1. Length

Digits per decimal digit = ln 10 / ln b: **6: 1.285, 8: 1.107, 10: 1.000, 12: 0.927, 16: 0.830**. Bits per digit = log₂ b: 2.58, 3.00, 3.32, 3.58, 4.00. Base 6 is 1.39× longer than base 12.

| quantity | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|
| price in cents, 499 | 4 | 3 | 3 | 3 | 3 |
| 1,299.00 in cents | 7 | 6 | 6 | 5 | 5 |
| 10-digit ID space (10¹⁰) | 13 | 12 | 10 | 10 | 9 |
| world population 8.1×10⁹ | 13 | 11 | 10 | 10 | 9 |
| sig. digits for 1% precision | 4 | 3 | 3 | 3 | 3 |
| sig. digits for 0.01% | 6 | 6 | 5 | 5 | 5 |

Scientific exponents stay at 2 digits in every base (Avogadro: 6³⁰, 10²³, 12²²).

**Spoken cost.** Read digit by digit, syllables scale with digit count: at 1–2 syllables per digit, a 10¹⁰ ID costs 13–26 syllables in base 6 and 10–20 in base 10. Read as a quantity (one syllable per nonzero digit plus one per place word, with "one" dropped before a place word), the mean over uniform 1..10⁶ is 10.9 / 10.2 / 9.4 / 9.1 / 8.2 syllables for 6/8/10/12/16. That makes base 6 only 16% longer than decimal when read as a quantity, against 30% when read digit by digit.

**Memory is what length really costs.** Span is limited in *items*, not bits. Miller reports Hayes: "With binary items the span is about nine and, although it drops to about five with monosyllabic English words, the difference is far less than the hypothesis of constant information would require" ([Miller 1956](https://psychclassics.yorku.ca/Miller/)). Span also tracks articulation time: Welsh digits take 385 ms against English 321 ms, and span is 5.77 against 6.55 ([Ellis & Hennelly 1980](https://sites.lsa.umich.edu/nickellis-new/wp-content/uploads/sites/1284/2021/07/Ellis_et_al-1980-British_Journal_of_Psychology.pdf)). So 7 items hold 18.1 bits in base 6, 23.3 in base 10 and 25.1 in base 12. Base 6 would need a span of 9.0 digits to match decimal. Smaller digit sets may raise span somewhat (binary 9), but probably not that far **[inferred]**.

## 2. Fractions

A fraction 1/q terminates iff every prime factor of q divides b. Its period is the multiplicative order of b mod q′.

| 1/q | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|
| 1/2 | .3 | .4 | .5 | .6 | .8 |
| 1/3 | **.2** | .(25) | .(3) | **.4** | .(5) |
| 1/4 | .13 | .2 | .25 | .3 | .4 |
| 1/5 | .(1) | .(1463) | **.2** | .(2497) | .(3) |
| 1/6 | .1 | .1(25) | .1(6) | .2 | .2(A) |
| 1/7 | .(05) | .(1) | .(142857) | .(186A35) | .(249) |
| 1/8 | .043 | .1 | .125 | .16 | .2 |
| 1/9 | .04 | .(07) | .(1) | .14 | .(1C7) |
| 1/10 | .0(3) | .0(6314) | .1 | .1(2497) | .1(9) |
| 1/12 | .03 | .0(52) | .08(3) | .1 | .1(5) |

Periods of 1/p: in base 6, p = 5, 7, 11, 13 give 1, 2, 10, 12. In base 10: 0, 6, 2, 6. In base 12: 4, 6, 1, 2.

- **Terminating unit fractions for q = 2..12:** 6 → 7, 12 → 7, 10 → 5, 8 → 3, 16 → 3. Bases 6 and 12 terminate exactly the same set, since both are 2ᵃ3ᵇ. Base 12 just needs fewer digits.
- **Everyday reduced fractions** (all p/q with q ∈ {2,3,4,5,6,8,10,12}, 23 in total): 6, 10 and 12 each terminate **15/23**; 8 and 16 terminate 7/23. Which base wins depends on how often thirds come up compared with fifths and tenths. Today's frequencies are partly an artefact of decimal (percent, tenths), so they can't settle it **[inferred]**.
- **"Percent" (per b²):** per-36 has a 2.78% step and is exact for 1/2, 1/3, 1/4, 1/6, 1/9, 1/12, 1/18. Per-144 has a 0.69% step and adds 1/8, 1/16, 1/24. Per-100 is exact for 1/2, 1/4, 1/5, 1/10, 1/20, 1/25. Per-36 is too coarse for the job percent does now, so base 6 would need per-216 **[inferred]**.
- Base 6's 1/5 = .1111… is still non-terminating: splitting money five ways still rounds. A short period helps recognition, not exact arithmetic.

## 3. Arithmetic

- **Table sizes** (unordered facts, operands 1..b−1 for addition, 2..b−1 for multiplication): addition 15 / 28 / 45 / 66 / 120; multiplication **10 / 21 / 36 / 55 / 105**. These match seximal.net's "ten" for base 6 and "nif" (36) for decimal ([seximal.net/math](https://www.seximal.net/math)).
- **"Hard" facts** (my definition: neither operand is 0, 1, 2, b/2 or b−1, all of which have patterns): base 6 has 1 (4×4 = 24₆), base 8 has 6, base 10 has 15, base 12 has 28, base 16 has 66. I also recall the problem-size effect: larger operands are retrieved more slowly and with more errors. If so, base 12's extra facts are its hardest ones (**recalled, not checked this session**).
- **Carries:** the long-run carry rate is ½ in every base. Holte's two-number transition matrix is (1/2b)·[[b+1, b−1], [b−1, b+1]] ([Holte 1997](https://sites.math.washington.edu/~billey/classes/561.fall.2019/past.articles/holte.pdf)), and my simulation agrees (0.50 in each base). So carries per *quantity* scale with length: 0.645 / 0.553 / 0.499 / 0.463 / 0.415 per decimal-digit equivalent. Long multiplication needs (digit ratio)² single-digit products: base 6 needs **1.65×** decimal's, base 12 0.86×. Base 6 has fewer facts but more steps.
- **Divisibility tests.** A divisor of bᵏ is tested on the last k digits, a divisor of b−1 by digit sum, a divisor of b+1 by alternating sum.

| d | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|
| 3 | last digit | alt. sum | digit sum | last digit | digit sum |
| 4 | last 2 | last | last 2 | last | last |
| 5 | **digit sum** | alt. pairs | last | alt. pairs | digit sum |
| 7 | **alt. sum** | digit sum | alt. triples | alt. triples | triple sum |
| 9 | last 2 | alt. sum | digit sum | last 2 | triple sum |
| 11 | none | none | alt. sum | digit sum | none |
| 13 | none | alt. pairs | alt. triples | alt. sum | triple sum |

Base 6 has easy tests for every d ≤ 10, the best coverage of the five. Base 12 has none practical for 5 or 7 ("alt. pairs" for 5 is mod 145).
- **Primes > 3 end in 1 or 5 in base 6.** True: they are ±1 mod 6 ([Wikipedia: Senary](https://en.wikipedia.org/wiki/Senary)), and I checked it to 10,000. But the last digit screens out 2/3 of integers in base 6 and in base 12 (where primes end in 1, 5, 7, B), and 3/5 in base 10. Base 6's version is tidier, not stronger.
- **Radix economy** E = b·⌊log_b N + 1⌋ ~ (b/ln b)·ln N ([Wikipedia: Optimal radix choice](https://en.wikipedia.org/wiki/Optimal_radix_choice)). Values: 2: 2.885, 3: 2.731, **6: 3.349, 8: 3.847, 10: 4.343, 12: 4.829, 16: 5.771**. The model prices each digit position at b states, which fits ring-counter hardware. Humans pay the inventory (b symbols, ~b² facts) once and the length on every use, so the real trade-off has the same shape with unknown weights. Taken literally, the metric would make humans count in base 3. The same article notes Dudley's *Mathematical Cranks* on "a greatly exaggerated sense of how important the choice of radix is".

## 4. Measurement, time, binary

- 12 and 60 recur because they are highly composite. 12 has 6 divisors. 60 has 12 and is "the smallest number that is divisible by every number from 1 to 6", from Sumerian/Babylonian usage of the 3rd millennium BC, which survives in minutes, seconds and the 360° circle ([Wikipedia: Sexagesimal](https://en.wikipedia.org/wiki/Sexagesimal)). The 12 night hours trace to Egyptian star observations (decans) ([Wikipedia: Hour](https://en.wikipedia.org/wiki/Hour)). Ifrah traces 12 to counting finger bones with the thumb, which reaches 60 with the other hand ([Wikipedia: Duodecimal](https://en.wikipedia.org/wiki/Duodecimal)). Decimal time was mandatory in France only from 22 Sep 1794 to 7 Apr 1795 ([Wikipedia: Decimal time](https://en.wikipedia.org/wiki/Decimal_time)). That is evidence that people resisted breaking 12/60, but under a legacy premise.
- **Unit subdivision.** Base-power subdivision gives 36 parts (9 divisors) in base 6, 144 parts (15) in base 12, 100 parts (9) in base 10, 256 parts (9) in base 16. Fractions of a turn: 1/6 turn (60°) is .1 in base 6 and .2 in base 12, but .1666… in base 10. 1/8 turn (45°) is .043, .16, .125 and .2 in bases 6, 12, 10, 16.
- **Binary.** 2¹⁰ is 2000₈, 400₁₆, 714₁₂ and 4424₆. Only 8 and 16 map bits to digits (3 and 4 bits each). Bases 6, 10 and 12 all need real conversion, so 6 and 12 are no worse than decimal is today. Fractions of 1 that are exact in both a human base and binary floating point are only the halvings 1/2, 1/4, 1/8, … in every base. Base 12's .4 (1/3) misbehaves in binary floats just as decimal 0.1 does today ([Python docs](https://docs.python.org/3/tutorial/floatingpoint.html)). Today's fixes (integer minor units, radix-matched floats) carry over **[inferred]**. But 8 and 16 give up thirds (1/3 repeats) and fifths, and need 8 or 16 distinct digit words.
- **Fingers.** A base-6 digit is exactly one hand (0–5), and two hands count 0–35 ([seximal.net](https://www.seximal.net/finger-counting); [Senary](https://en.wikipedia.org/wiki/Senary)). Base 10 needs both hands per digit. Base 12 uses thumb-on-phalanges.

## 5. Rounding and estimation

Rounding values with log-uniform (Benford) mantissas:

| | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|
| 1 sig. digit, mean rel. error | 11.1% | 10.1% | 9.4% | 8.9% | 8.2% |
| 2 sig. digits, mean rel. error | **1.93%** | 1.31% | 0.97% | 0.77% | 0.53% |
| one-digit "round values" per factor 10 | 6.4 | 7.8 | 9.0 | 10.2 | 12.5 |
| P(leading digit = 1) | 38.7% | 33.3% | 30.1% | 27.9% | 25.0% |

One-digit estimates differ little, because the "1.x" band dominates every base. Two-digit precision in base 6 is **2× coarser** than decimal, so a base-6 speaker needs about one more digit for "good enough". Even bases all round half at the single digit b/2. Bases 6 and 12 can round to thirds natively.

## 6. The advocacy, checked

**Dozenal (DSA, founded 1944; DSGB, 1959).**
- *Holds:* 12 has 6 divisors against 4. 1/2, 1/3, 1/4 and 1/6 are one digit ("⅓ = 0.4z", [dozenal.org](https://dozenal.org/)), 1/8 and 1/9 two. Last-digit tests work for 2, 3, 4 and 6, digit sum for 11 and alternating sum for 13. 12 has proportionally fewer totatives than 10 (4/12 against 4/10).
- *Overstated:* DSGB says "Decimals handicap the teaching of arithmetic" ([dozenalsociety.org.uk](http://www.dozenalsociety.org.uk/)). The DSA says dozenal "can make everyday arithmetic easier to learn" ([dozenal.org](https://dozenal.org/)), and its FAQ says fewer totatives mean fewer "difficult" product lines ([De Vlieger FAQ](https://dozenal.org/article-devlieger-dozenal-faq.pdf)). The table is 53% larger (55 against 36 facts; the DSA's own count is 78 against 55). One web search found no controlled study of children learning arithmetic in another base (**searched, not found**). Fewer totatives also ties base 6 (2/6). The FAQ "presume[s] a number base will need to be between about 7 or 8 through about 16". Its only argument for that range is a binary speed-limit sign, so base 6 is excluded by assumption.
- *Left out:* 1/5 = .(2497) and 1/10 are bad, with no practical 5- or 7-test. The length gain over decimal is only 7%. Notably, the FAQ's author calls decimal "the second- or third-best number base for general human computation".

**Seximal (jan Misali; [seximal.net](https://www.seximal.net/)).** The video "a better way to count" was confirmed via YouTube oEmbed, but its transcript was behind a bot wall. Claims checked here come from his site.
- *Holds:* the 10-fact table, 1/5 = .(1), 1/7 = .(05), 2/3-tests on the last digit, primes ending in 1 or 5, and finger counting to 35. All are verified above.
- *Overstated:* "on average, [dozenal is] worse than seximal AND decimal" at fractions ([seximal.net/factors](https://www.seximal.net/factors)). This holds on written digit count over 1/2..1/10 (total digits 15 / 18 / 23 for 6 / 10 / 12). The cut-off at 10 makes 1/5, 1/7 and 1/10 three of nine cases, and repeating .(1) is scored as cheap. On *terminating* count, 6 and 12 tie (6/9, and 7/11 up to 1/12). "Objectively the best" is an assertion, not an argument.
- *Left out:* numbers 29% longer than decimal and 39% longer than dozenal. About 22% fewer bits per memory span (10¹⁰ IDs need 13 digits). Long multiplication takes 1.65× the digit products, and there are more carries per quantity. Two-digit precision is 2× coarser and the per-36 "percent" too coarse. 1/11 and 1/13 have periods 10 and 12.

## Comparison

| | 6 | 8 | 10 | 12 | 16 |
|---|---|---|---|---|---|
| length vs decimal | 1.285 | 1.107 | 1 | 0.927 | 0.830 |
| bits per 7-digit span | 18.1 | 21.0 | 23.3 | 25.1 | 28.0 |
| mult. facts / "hard" | 10 / 1 | 21 / 6 | 36 / 15 | 55 / 28 | 105 / 66 |
| terminating 1/q, q = 2..12 | 7 | 3 | 5 | 7 | 3 |
| one-digit 1/2, 1/3, 1/4, 1/5 | ½ ⅓ | ½ ¼ | ½ ⅕ | ½ ⅓ ¼ | ½ ¼ |
| easy tests among 2,3,4,5,7,9 | all 6 | 5 (5 only by alt. pairs) | 5 (no 7) | 4 (no 5, 7) | 4 (7, 9 only by triple sums) |
| 2-sig-digit error | 1.93% | 1.31% | 0.97% | 0.77% | 0.53% |
| long-mult work vs decimal | 1.65× | 1.23× | 1× | 0.86× | 0.69× |
| bits map to digits | no | yes | no | no | yes |
| digit words to keep distinct | 6 | 8 | 10 | 12 | 16 |

"Easy" means a last-k-digits test, a digit sum or an alternating sum.

## Implications for choosing a base

1. **The real trade-off is per-use length against learning cost**, with fractions as a tiebreak among 6, 10 and 12. Base 12 is cheapest per use (shortest numbers, finest 2-digit precision, best per-b² "percent", one-digit thirds and quarters). Base 6 is cheapest to learn (10 facts, every test up to 10, short 5/7 periods) and pays about 29% in length on every use, forever. Decimal sits between the two and wins only on fifths.
2. **8 and 16 lose on the human side.** Without thirds they do worse on everyday fractions (7/23 against 15/23), and base 16 has a 105-fact table and 16 digit words. Their only win is bit-mapping, and computers convert anyway.
3. **For this language's goal (faithful transmission), the deciding unknown is per-digit error rate against digit count** **[inferred]**. A string fails if any digit is misheard, so base 6 wins on transmission only if its digit words are misheard less than 1/1.285 = **78%** as often as decimal's. Six digit words can be spread further apart in sound space than 10 or 12 can. The repo's `tools/confusion.py` could compute the best achievable confusion for 6-, 10- and 12-word digit sets directly. That is the one experiment that would turn this from taste into evidence.
4. **Finger fit favours 6** for the signed surface: one hand is one digit. `docs/design-log.md` currently grounds base 10 in finger counting plus "the decimal system modern Earth already uses". This premise voids the second source, which leaves only finger counting, and base 6 fits fingers at least as well.
5. Unit design is downstream: either base makes 2ⁿ·3ᵐ subdivisions native, so the 12/60 heritage of time and angle fits both 6 and 12 better than 10.

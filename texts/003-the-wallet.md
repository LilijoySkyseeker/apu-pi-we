# Stress test 003: the wallet

An original passage Claude wrote (2026-10-08) to test:
- the rebuilt words
- emphasis and contrast
- every kind of number: a count, a clock time, an ordinal, a phone number and a day offset
- politeness
- a negative question
- logophoric "he"
- three-person reference
- confidence on a single word
- comparison and a loanword, as probes of undesigned grammar

Blind back-translation results are in `tests/backtranslation-02/`. The translation below is the corrected version, after the fixes that test led to. Names: Mara → **en mala** (no r), Tomas → **en tomasu**, Ben → **en benu**, each with the name article **en** (added after names test 01).

## Source

> "Did you take my wallet?" Mara asked.
> "I didn't take it. Tomas did."
> "Tomas was at school all day."
> "He came home at three and said he needed money for the bus."
> "How much was in it?"
> "Forty-two dollars and my bus card, I think. I'm not completely sure about the card."
> "Didn't you lock your door?"
> "No. I forgot."
> "Could you please call him? His number is 0412 785 309."
> Ben called. Tomas answered on the second ring.
> Tomas told Ben that he would return the money the day after tomorrow.
> "He didn't take the money," Ben said. "He took the card."
> "If he loses that card, I'm telling Dad."
> "Dad already knows. Tomas called him first."
> Mara laughed. "Of course he did. He's smarter than both of us."

## Translation

```
"min me  yidu yufa nimo  pi lon." en mala sin  mido.
Q    you take bag  money of me    Mara DONE ask

"lon mu  yidu bu. en tomasu yidu bu."
I    not take it  Tomas  take it

"en tomasu gun mon guyi  yesa  nin    dili minwe."
Tomas   is  at  house learn during day  whole

"wan obu  tun guyi  mon mimi  ka da ka, yen oyi wun  sun wupi nimo  li  ensu."
he   come to  house at  point 3  4  3,  and say that he  need money for bus
                                                     (time of day as a fraction of the day: .343 = 15:00)
                                                     (sun: "he" = Tomas, whose words are reported)

"gun     nimo  wifu   yu   mon bu."
there-is money number what at  it

"lon pume,  dola   miko nobi, yen kon  te mise ensu pi lon."
I    think: dollar 36   6     and CONF 5  card bus  of me
                                                     (42 = 36 + 6; confidence covers only the card: 5 in 6)

"min mu  me  udin beya pi me." "mu udin. lon yakin."
Q    not you lock door of you  not lock  I   forget

"so     ku     yebin wan. wifu   liga  pi wan gun, po, fi po da te, da ka sa ka, fi po ka ka."
REQUEST POLITE call  him  number phone of him is:  0,  1  0  4  5,  4  3  3  2,  1  0  3  3
                                                     (the English number 0412 785 309 written in base 6, read digit by digit in groups of four)

en benu yebin. en tomasu febo   mon yebin pi sa.
Ben  call   Tomas  answer at  call  of 2

en tomasu iko  en benu wun  sun sigo   nimo  mon wuma     wo    dili fi.
Tomas  tell Ben  that he  return money at  tomorrow after day  1

"wan mu  yidu nimo," en benu oyi. "wan yidu mise."
he   not take money  Ben  say  he   take card
                                                     (the speech tag doesn't count, so both "wan" stay Tomas)

"don wan agi  mise ben,  de     lon iko  wede."
if   he  lose card that, INTEND I   tell father

"wede  sin  lugo. en tomasu yebin wan ya."
father DONE know  Tomas  call  him first
                                                     (him: not Tomas, his own clause's subject, so the subject before: Dad)

en mala bubo. "ba     yi    sin  muge. yi    gun ke   gole  se   pen."
Mara laugh EXCLAIM other DONE do    other is  more smart from us
                                                     (yi = the subject before Mara: Tomas)
```

## Measurements

- **Numbers:** converted to base 6 on 2026-10-08 (see `docs/number-base.md`). The measurements below are from the base-10 version.
- **Length:** 228 syllables against about 176 in the English (the phone number counted as spoken digits), so 30% more. That's higher than texts 001 (16%) and 002 (23%). Two things drive it:
  - The phone number: 10 long digits = 20 syllables, against 11 in English. Long forms are the price of context-free numbers.
  - Possessives **pi lon** / **pi me** / **pi wan**, five times.

  At simple-syllable speaking rates the speaking time is still about equal.

## Findings

| # | Finding | Fix | Status |
|---|---|---|---|
| 1 | **Contrast survived without any device.** The judge confirmed both "*I* didn't, *Tomas* did" and "not the money, the card" read as contrasts. | None needed. Add-back trigger: a test where contrast is lost. | observation |
| 2 | "**wuma wo PUmu**" (base-10 forms of the time) read as "tomorrow after one o'clock" | Offsets always name their unit (**wo dili fi** "after one day"); clock times are day fractions (**mimi ka da ka**) | adopted |
| 3 | "it" (the wallet) and "he" (Tomas) both used **yi**; with three people, **yi** didn't say which one | **bu** = "it" for things. **yi** = the next most recent different subject. Anyone further back is named. | adopted |
| 4 | Do speech tags ("…," Ben said) reset pronoun tracking? | No: a say-verb framing a quote doesn't count | adopted |
| 5 | An if-clause before the speech-act particle wasn't allowed | If/when clauses may come first, like scene-setting phrases | adopted |
| 6 | Comparison (**ke … se**), "how much" (**wifu yu**) and the loanword **dola** were undocumented, yet the reader guessed all three | Documented as written | adopted |
| 7 | Short numbers look like grammar words in writing (**o** = 6 or "seen") | Normal writing uses digits | adopted |
| 8 | bus → "car", card → "papers": compounds for modern objects failed (4 of 6 lost content points) | Roots added: bus **ensu**, card **mise**, car **tale**, phone **liga**, hour **aya**. Modern vocabulary (roadmap B1) is now the biggest source of loss. | adopted / B1 |
| 9 | Phone number came back with two digits swapped | It was the translator's (Claude's) error: 0142 written for 0412. Digit strings are easy to get wrong by hand; a checker (C3) would catch it. | translator error |
| 10 | "Of course he did" flattened to an exclamation | Idiom; no fix | observation |

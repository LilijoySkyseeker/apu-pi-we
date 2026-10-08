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

Blind back-translation results are in `tests/backtranslation-02/`. The translation below is the corrected version, after the fixes that test led to. Names: Mara → **MAla** (no r), Tomas → **TOmasa**, Ben → **BEne**.

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
"min me  YIdu YUfa NImo  pi lon?" MAla sin  MIdo.
Q    you take bag  money of me    Mara DONE ask

"lon mu  YIdu bu. TOmasa YIdu bu."
I    not take it  Tomas  take it

"TOmasa gun mon GUyi  YEsa  nin    DIli MINwe."
Tomas   is  at  house learn during day  whole

"wan Obu  tun GUyi  mon Aya  pi KA, yen Oyi wun  sun WUpi NImo  li  ENsu."
he   come to  house at  hour of 3   and say that he  need money for bus
                                                     (sun: "he" = Tomas, whose words are reported)

"gun     NImo  WIfu   yu   mon bu?"
there-is money number what at  it

"lon PUme:  DOla   MIko NObi, yen kon  TE MIse ENsu pi lon."
I    think: dollar 36   6     and CONF 5  card bus  of me
                                                     (42 = 36 + 6; confidence covers only the card: 5 in 6)

"min mu  me  Udin BEya pi me?" "mu Udin. lon YAkin."
Q    not you lock door of you  not lock  I   forget

"so     ku     YEbin wan. WIfu   LIga  pi wan gun: PO, FI PO DA TE, DA KA SA KA, FI PO KA KA."
REQUEST POLITE call  him  number phone of him is:  0,  1  0  4  5,  4  3  3  2,  1  0  3  3
                                                     (the English number 0412 785 309 written in base 6, read digit by digit in groups of four)

BEne YEbin. TOmasa FEbo   mon YEbin pi SA.
Ben  call   Tomas  answer at  call  of 2

TOmasa Iko  BEne wun  sun SIgo   NImo  mon WUma     wo    DIli FI.
Tomas  tell Ben  that he  return money at  tomorrow after day  1

"wan mu  YIdu NImo," BEne Oyi. "wan YIdu MIse."
he   not take money  Ben  say  he   take card
                                                     (the speech tag doesn't count, so both "wan" stay Tomas)

"don wan Agi  MIse ben,  de     lon Iko  WEde."
if   he  lose card that, INTEND I   tell father

"WEde  sin  LUgo. TOmasa YEbin wan ya."
father DONE know  Tomas  call  him first
                                                     (him: not Tomas, his own clause's subject, so the subject before: Dad)

MAla BUbo. "ba     yi    sin  MUge. yi    gun ke   GOle  se   pen."
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
| 2 | "**WUma wo PUmu**" read as "tomorrow after one o'clock" | Offsets always name their unit (**wo DIli PU** "after one day"); clock times are labels (**Aya pi KOse**) | adopted |
| 3 | "it" (the wallet) and "he" (Tomas) both used **yi**; with three people, **yi** didn't say which one | **bu** = "it" for things. **yi** = the next most recent different subject. Anyone further back is named. | adopted |
| 4 | Do speech tags ("…," Ben said) reset pronoun tracking? | No: a say-verb framing a quote doesn't count | adopted |
| 5 | An if-clause before the speech-act particle wasn't allowed | If/when clauses may come first, like scene-setting phrases | adopted |
| 6 | Comparison (**ke … se**), "how much" (**WIfu yu**) and the loanword **DOla** were undocumented, yet the reader guessed all three | Documented as written | adopted |
| 7 | Short numbers look like grammar words in writing (**o** = 6 or "seen") | Normal writing uses digits | adopted |
| 8 | bus → "car", card → "papers": compounds for modern objects failed (4 of 6 lost content points) | Roots added: bus **ensu**, card **mise**, car **tale**, phone **liga**, hour **aya**. Modern vocabulary (roadmap B1) is now the biggest source of loss. | adopted / B1 |
| 9 | Phone number came back with two digits swapped | It was the translator's (Claude's) error: 0142 written for 0412. Digit strings are easy to get wrong by hand; a checker (C3) would catch it. | translator error |
| 10 | "Of course he did" flattened to an exclamation | Idiom; no fix | observation |

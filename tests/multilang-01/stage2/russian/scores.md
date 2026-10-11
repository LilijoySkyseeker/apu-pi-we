# Russian → Apu Pi We → Russian: judge scores

Scale: 2 = same meaning, 1 = gist right but a real part lost/changed, 0 = wrong or missing.
Causes: L = Apu Pi We has no way to say it; T = translator had a way but didn't use it / erred; B = back-translator misread a correct translation; E = root chosen from an English gloss brought the wrong range of meaning.

## 1. Line scores

| # | Speaker | Source (short) | Score | What is lost | Cause |
|---|---|---|---|---|---|
| 1 | A | ты в субботу на даче будешь? | 2 | — (дача reduced to "house far from city" in Apu, but back-translator recovered «на даче, за городом») | — |
| 2 | B | Ну, если Серёга довезёт. Я ж без машины теперь. | 2 | — (see other losses: «ну», «теперь», tag «да?») | — |
| 3 | C | Довезу, куда я денусь. Только выезжаем рано, в семь. | 2 | — («рано» survives only as a bracketed Russian word) | — |
| 4 | B | В семь? Ты серьёзно? Суббота же. | 2 | — | — |
| 5 | C | …в пробке на Новой Риге три часа стоять? Я — нет. | 2 | — | — |
| 6 | A | Да ладно, в субботу утром нормально всё… | 2 | — | — |
| 7 | C | Ага, «нормально». …Шашлык в итоге в темноте жарили. | 2 | — (sarcasm and the 9→13:00→dark chain all kept) | — |
| 8 | A | …Лёха попросил за пивом заехать, пробки тут ни при чём. | 2 | — | — |
| 9 | C | При чём, ещё как при чём. Я по навигатору смотрел… | 2 | — (evidential **o** over-rendered as «своими глазами видел», harmless) | — |
| 10 | B | Слушайте, давайте я тогда на электричке, а вы как хотите. | 2 | — (soft «давайте я тогда» → firmer «Короче, я поеду») | — |
| 11 | C | Ну вот, начинается. Мы ж договаривались вместе. | 2 | — | — |
| 12 | B | Договаривались, но не в семь утра. …выспаться надо. | 2 | — | — |
| 13 | A | Вот, человек дело говорит. Серёж, ну давай в восемь хотя бы, компромисс. | 2 | — | — |
| 14 | C | В восемь — это уже не то. Ладно, смотрите: …не ноете… | 2 | — (back-translator was unsure, but chose the right reading) | — |
| 15 | A | Да кто ноет-то? Ты сам больше всех ноешь, когда стоим. | 2 | — (present «ноет» → future «ныть будет», same function) | — |
| 16 | C | Я не ною, я за рулём. …а я пять часов в этой каше. | 2 | — (metaphor «каша» lost, see below) | — |
| 17 | B | Ну не пять, не преувеличивай. | 2 | — | — |
| 18 | C | Четыре с половиной в прошлый раз. Я засекал, между прочим. | 2 | — («между прочим» lost, see below) | — |
| 19 | A | Ты ещё таблицу заведи, честное слово. | 2 | — (sarcasm and escalating «ещё» kept; «честное слово» lost) | — |
| 20 | C | Смешно вам. Давайте тогда кто-нибудь другой поведёт, раз всё так просто. | 2 | — (unmarked irony survived) | — |
| 21 | B | Я бы повёл, если б у меня права не забрали. | 2 | — | — |
| 22 | A | Ну всё, всё, в восемь — и Серёге кофе с заправки за наш счёт. Договорились? | 2 | — (who pays = A+B, correctly recovered as «мы с ним») | — |

**Total: 44 / 44.** No line scored 1 or 0, so no L/T/B/E causes at line level.

Caveat: several lines reached 2 only because the back-translator, a fluent Russian speaker, restored colloquial material that Apu Pi We did not encode (да ладно, уже, Серёж→«Серёг», ладно as grudging concession, смешно вам, дача). The score measures the round trip, not what the Apu text carries on its own.

## 2. Predicted gaps (gaps.md)

| # | Gap | Occurred here? | Preserved in back.md? |
|---|---|---|---|
| 1 | Stance / common-ground particles | Yes, heavily: ж (2), же (2), ну (5), вот (2), -то, also «между прочим», «честное слово», «да ладно» | **Partly.** ж/же, вот, -то, ну вот, да ладно recovered from context or from the tag **min**/**ba**; «ну» (line 2), «между прочим», «честное слово» lost. Tag **min** for ж produced confirmation-seeking «да?»/«так?» (lines 2, 11) |
| 2 | ты/вы and address gradient | Yes: ты to one person vs plural вы to the group; Серёга (3rd person) vs affectionate vocative Серёж. No T/V politeness asymmetry (all friends) | **Yes.** Plural via **me la** kept; Серёж not encodable (one name form) but back-translator produced the vocative «Серёг» on his own |
| 3 | Information structure by word order | Yes: «Я — нет», «В восемь — это уже не то», «Шашлык … жарили», «Четыре с половиной в прошлый раз», «человек дело говорит» | **Yes.** Contrast kept through parallel sentences and the back-translator's reordering («Я вот не хочу», «В тот раз — четыре с половиной») |
| 4 | Diminutive / pejorative morphology | Marginally: only familiar name forms (Серёга, Лёха, Серёж). No diminutive nouns | **Yes, by transliteration:** the familiar forms are frozen inside the loan names; Apu itself carries no familiarity. Back-translator added diminutives that were not in the source («табличку», «посерединке») |
| 5 | Grammatical gender | Yes: смотрел, засекал (C, masc.), повёл (B, masc.), сам (A to C) | **Yes, by default.** Not encoded; back-translator defaulted to masculine, which happened to match |
| 6 | Aspect nuances | Yes: «договаривались» (annulled-result imperfective), general-factual «смотрел», «засекал», negated «не забрали» | **Partly.** Annulled-result nuance lost (→ «договорились», carried only by же); others fine; translator avoided **mu sin** with counterfactual **don kon po** and it worked |
| 7 | Non-volitional / experiencer framing | Yes: «мне выспаться надо», «смешно вам», impersonal «права забрали» | **Yes.** Recast in Apu («I need», «you laugh», generic **go**), restored by back-translator |
| 8 | Scalar / concessive words | Yes: хоть раз, хотя бы, ещё как, ещё (escalating), уже, ладно (concessive). Not даже | **Yes.** **pa**, **ba bi** carried; «ещё» (→ **wame** "also") and «уже» (dropped) restored by back-translator from context |

Occurred: 8 / 8 (gap 4 only marginally, as name forms). Preserved: 6 fully, 2 partly (gaps 1 and 6), 0 lost outright.

## 3. Losses inside lines scored 2

- L1: дача as a cultural concept reduced to "house far from the city" (L); recovered.
- L2: hesitant «Ну,» lost (L); «теперь» (state has changed) → «сейчас» (L); «ж» → tag «да?», turning a reminder into a mild request for confirmation (L).
- L3: «рано» has no word and stays as bracketed Russian (L).
- L6: dismissive «Да ладно» reduced to **un** "but" (L); restored by back-translator.
- L7: quotation marks around A's «нормально» can't be kept (L); restored.
- L9: evidential **o** over-rendered «своими глазами видел» (B, minor addition).
- L10: «давайте я тогда» (soft proposal, "in that case") → «Короче, я поеду» (firmer, causal link weakened) (T/B, minor); электричка → generic train (L), restored.
- L11: annulled-result imperfective «договаривались» lost (L); tag «так?» artifact from **min**.
- L12: «утра» emphasis dropped (T: **leso** "morning" was available).
- L13: affectionate vocative Серёж vs Серёга (L), restored by guess; «компромисс» (mutual concession) → «посерединке» (just "in the middle") (L).
- L14: grudging «ладно» → neutral **lon tayu** (L); back-translator's «Ладно, согласен» restored most of it.
- L16: «в этой каше» metaphor lost → «в этой пробке» (L).
- L18: pointed «между прочим» lost (L).
- L19: exasperated «честное слово» lost (L); back-translator added «в экселе» and diminutive «табличку» (B, harmless).
- L22: soothing repeated «Ну всё, всё» → «Всё, хватит», sharper (T: translator chose not to repeat); «за наш счёт» as a treat → plain «покупаем» (L, minor).

## 4. Summary

The round trip kept the full meaning of all 22 lines (44/44): who does what, the 7-vs-9 argument, the sarcasm, the concession to 8 and who buys Seryoga's coffee all survived. The real losses are tone and particles («ну», «между прочим», «честное слово», «каша», grudging «ладно»), and much of what did survive was restored by a fluent Russian back-translator rather than encoded in Apu Pi We.

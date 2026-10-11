# Hindi–Urdu → Apu Pi We → Hindi–Urdu: judge scores

Cause codes: **L** = Apu Pi We has no way to say it; **T** = a way existed but the translator didn't use it or erred; **B** = back-translator misread a correct translation; **E** = a root chosen via its English gloss gave the wrong meaning field.

## Per-turn scores

| Turn | Score | What was lost | Cause |
|---|---|---|---|
| 1 A | 2 | — | |
| 2 B | 2 | — (hearsay सुना है kept via **fen**) | |
| 3 A | 1 | Verma "काफ़ी परेशान" (quite upset) became "थोड़ी घबराई" (a little nervous): the translator used **to** "rather", the same word used for -सा / थोड़ा elsewhere in the text, although **bi** "very" was available and used in the same turn | T |
| 4 B | 1 | "वर्मा जी" became bare "वर्मा": B's respect for his colleague is gone, so the boss sounds curt about her | L |
| 5 A | 2 | — (साहब dropped, but back-translator supplied जी; see other losses) | |
| 6 B | 2 | — | |
| 7 A | 2 | — | |
| 8 B | 2 | — | |
| 9 A | 2 | — | |
| 10 B | 2 | — | |
| 11 A | 2 | — | |
| 12 B | 2 | — | |
| 13 A | 2 | — | |
| 14 B | 2 | — | |
| 15 A | 2 | — | |
| 16 B | 2 | — | |
| 17 A | 2 | — | |
| 18 B | 2 | — | |
| 19 A | 2 | — | |
| 20 B | 2 | — | |
| 21 A | 1 | (a) Gupta's angry "आप लोगों" (cold formal distance) became "तुम लोगों" (rude familiarity): Apu has one **me**, and **nun** would have made him sound polite, so it was left bare and read as तुम. (b) "आज दोपहर तक" (by this afternoon) became "बारह बजे से पहले" (before 12:00), a stricter deadline; there is no word for midday. Also "ग़लत था" → "ग़लत है" (minor). "भरोसा" survived only because the translator left it as untranslated Hindi in brackets (see note). | L, L |
| 22 B | 1 | (a) "वो मुझे ढूँढ लेंगी" (she, a respected woman at home, likely his wife) became "घर वाले" (the family): **yi** carries neither gender nor respect. (b) "पैसे-वैसे मत काटना" (don't dock his pay) became "पैसे या कुछ और मत लेना" (don't take money or anything from him); the back-translator read the Apu correctly and flagged that it probably means a fine, but the Apu says "take from him", not "cut his pay" | L, T |

**Total: 40 / 44** (18 turns at 2, 4 turns at 1, 0 at 0).

Loss count by cause (6 losses in 4 turns): **L = 4** (turn 4, 21a, 21b, 22a), **T = 2** (turn 3, 22b), **B = 0**, **E = 0**.

Borderline E, not counted: turn 3 परेशान → **feme nuta** "feel fear" (worry → fear via English) came back as घबराई; in context this is close enough.

**Method note:** in turn 21 the translator wrote "[भरोसा करना]" in Hindi inside the Apu text, and the back-translator copied it. A reader with only Apu would have lost "trust" here, and turn 21 would have lost a third item.

## Predicted gaps (gaps.md)

| # | Gap | In this text? | Survived in back-translation? |
|---|---|---|---|
| 1 | Graded 2nd person tū/tum/āp | Yes: A uses आप to B, B uses तुम to A, Gupta uses आप लोग in anger (no तू) | **Partly.** The A/B asymmetry survived (**nun** on A's turns; the back-translator inferred junior/boss). Gupta's cold आप लोग was lost and came back as तुम लोग (turn 21). |
| 2 | Gender in agreement | Yes: Verma, Pooja, the wife, the daughter, बच्ची, "वो … लेंगी", plus A and B (both male) | **Partly.** It survived where **futa** was stated once or context was clear (Verma, Pooja, wife, daughter; बच्ची guessed from context). It was lost for the woman at home (turn 22). A's and B's gender is never encoded; the back-translator defaulted to male, which happens to be right. |
| 3 | Topic/focus to / hī / scalar bhī | Yes, very often: गड़बड़ तो, आती ही नहीं, रात को ही, निकला ही नहीं, दो बार तो, ही नहीं आया, बताया भी नहीं, वही, ख़ुद ही, ही ग़लत, गाड़ी तो | **Mostly.** **mu mu**, **ya**, **nen** and quotes let the back-translator restore almost every तो/ही. Scalar भी नहीं (turn 9, "didn't even tell") came back as ही नहीं, and contrastive "गाड़ी तो" became a plain "but". |
| 4 | Compound (vector) verbs | Yes: हो गई, ले गया, मना कर दिया, आ गए, दे देंगे, पूछ लो, हाँ कर दी, कह दिया, कर देते हैं, ले लिया, घुस गया, कर देना, ढूँढ लेंगी | **Yes,** but because the back-translator wrote natural Hindi, not because Apu carried them. The one with real meaning, "अपने से हाँ कर दी" (decided on your own), came back as "अकेले ही हाँ कर दी". |
| 5 | Habitual aspect | Yes: आती ही नहीं, बैठता है, चश्मा लगाती है, हिसाब-किताब देखती हैं | **Yes,** inferred from context (**eda** "now" helped for the daughter). The back-translator flagged that the daughter line could mean "was counting the money right then". |
| 6 | Respect for third persons | Yes, about 10 times: Verma मैडम/जी, गुप्ता साहब ×3, the uncle (आ गए, हैं, उन्होंने, चाचा जी), the daughter (देखती हैं, उन्होंने), "वो … लेंगी" | **Partly.** Apu carried none of it. The back-translator put back honorific forms for मैडम, the uncle and the daughter (उन्होंने). Lost or downgraded: वर्मा जी → वर्मा, साहब → जी, चाचा जी → उन्होंने, the daughter's देखती हैं → देखती है, and the woman at home → घर वाले. |
| 7 | Volitionality (accidental vs deliberate; dative experiencer) | Marginal: मुझे लगा, समझ में आता है, फ़ोन बंद आ रहा था, मेरा फ़ोन न लगे | **Yes.** Nothing depended on it. "न लगे" came back as "बात न हो पाए", which is still non-volitional. |
| 8 | Vocabulary strata / humble-exalted words | Yes: mixed Hinglish office speech (सर, मैडम, ऑफ़िस, इंटर्न, साइलेंट) with Perso-Arabic (माफ़ी, नुक़सान, दिक़्क़त, फ़ैसला, बुज़ुर्ग, शाबाश) and Sanskritic धन्यवाद | **Partly.** The register stayed colloquial, but the word choices were reshuffled: गड़बड़/दिक़्क़त → प्रॉब्लम, धन्यवाद → शुक्रिया, ऑफ़िस → दफ़्तर. The humble माफ़ी चाहता हूँ survived. |

**8 of 8 gaps appeared** (no. 7 only marginally). **3 survived** (4, 5, 7), **5 partly survived** (1, 2, 3, 6, 8), and **none was lost entirely.** Most of the survival is the back-translator putting Hindi defaults back from context, not Apu carrying the distinction.

## Other losses, including in turns scored 2

- **Third-person titles flattened:** गुप्ता साहब (an important client) → गुप्ता जी (turns 5, 17, 20); चाचा जी (affectionate kin title) → उन्होंने (turn 19). The honorifics for the uncle (turns 13, 18) and Verma (turn 3) came back only because the back-translator guessed them.
- **Address warmth:** Ramesh's भैया to A → भाई (turn 7); the warmth and respect became plain "sibling".
- **Tone particles:** B's resigned "चलो" (okay, let it go) is gone (turn 10). "हाँ" → "हम्म" (turn 16).
- **बेचारा** became an explicit statement, "मुझे उसके लिए बुरा लगा" (turn 9), so A now voices his pity outright.
- **Apology overstated:** the doubled **nun** came back as "बहुत-बहुत माफ़ी" (turn 17), so A sounds more abject than "माफ़ी चाहता हूँ" (T).
- **नुक़सान (financial loss) → प्रॉब्लम** (turn 17): more general (Apu **agi** is only "misplace").
- **Aspect:** "ट्रक वाला ही नहीं आया" (didn't come) → "आ ही नहीं रहा" (isn't coming) (turn 7), because Apu left it unmarked.
- **Certainty:** "परेशान लग रही थीं" (seemed upset) → "साफ़ दिख रहा था" (it was clearly visible) (turn 3): the seen-evidential **o** made an impression sound like an observation.
- **चाचा vs ताऊ:** "father's younger brother" isn't encoded; the back-translator's guess happened to be right.
- **"अपने से"** (on your own authority) → "अकेले ही" (alone) (turn 16): a slight shift.
- **"अभी"** (just now) is only partly kept in turn 21.
- **Speaker gender:** never encoded; male was a default guess.

## Summary

The dialogue came back almost whole at 40/44. Every event, who did what for whom, the hearsay vs. seen distinction, and the boss/junior relationship survived. What was lost was almost entirely the social layer: respect for people being talked about, Gupta's cold आप लोग, and the gender of the woman at home. These are language gaps (L), plus two translator slips (T).

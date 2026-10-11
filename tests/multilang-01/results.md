# Multilanguage test 01: results (stages 2 and 3)

Stage 1 (desk inventories): `stage1-synthesis.md`. Stage 2: seven round trips
(`stage2/<language>/`), every agent prompted in the target language: writer →
translator → back-translator (never saw the source) → judge.

## Scores

| Language | Registers | Meaning | Losses L / T / B / E (lines scored 1) | Predicted gaps: occurred → kept fully / partly / lost |
|---|---|---|---|---|
| Vietnamese | casual ↔ hierarchical | 42/44 | 0 / 1 / 1 / 0 | 7 → 4 / 3 / 0 |
| Hindi–Urdu | hierarchical ↔ narrative | 40/44 | 4 / 2 / 0 / 0 | 8 → 3 / 5 / 0 |
| Arabic (Egyptian) | casual ↔ hierarchical | 44/46 | 2 / 0 / 0 / 0 | 8 → 3 / 5 / 0 |
| Russian | casual ↔ persuasive | 44/44 | 0 / 0 / 0 / 0 | 8 → 6 / 2 / 0 |
| Mandarin | narrative ↔ written | 42/44 | 1 / 2 / 0 / 0 | 5 → 3 / 1 / 1 |
| English | persuasive ↔ narrative | 46/46 | 0 / 0 / 0 / 0 | 6 → 2 / 3 / 1 |
| Spanish | written ↔ persuasive | 39/44 | 5 / 1 / 1 / 0 | 5 → 2 / 3 / 0 |
| **All** | | **297/310 (96%)** | **12 / 6 / 2 / 0** | **47 → 23 / 22 / 2** |

(Japanese round trip, earlier: 42/44.)

## What the round trips show

1. **Content survives across every language and register: 96%.** No line
   scored 0. Of the 20 line-level losses, 12 are the language (L), 6 the
   translator (T), 2 the back-translator (B). **No English-gloss leak (E)**
   anywhere; the fix holds.
2. **The stage 1 gaps are real but mostly sub-line.** Of 47 predicted gaps
   that occurred, only 2 were lost outright; 22 survived partly. They show up
   as losses *inside* lines that still scored 2: particles, address, tone,
   register.
3. **Round trips overstate survival of exactly these gaps.** Four judges
   (Russian, Hindi–Urdu, Vietnamese, Mandarin) independently warned that the
   back-translator rebuilt register, particles and respect *from context and
   world knowledge*, not from anything in the Apu Pi We. Hindi–Urdu: "Apu
   carried none of its roughly 10 instances" of third-person respect, yet the
   back-translation restored some. So for stance and relationship, stage 1's
   desk inventory is the better gauge; for content, stage 2 is.

## The language's real (L) losses, by theme

| Theme | Where it bit | Example |
|---|---|---|
| **Respect for a third person** | Hindi–Urdu (×10, none carried), Vietnamese, Arabic | "वर्मा जी" came back as bare "Verma"; a respected wife became "the family" |
| **Standing relationship / graded "you"** | Vietnamese, Hindi–Urdu, Spanish, Arabic | cold formal "आप लोग" came back as rude "तुम लोग"; bác (older than parents) became chú (younger); "Muy señores míos" became "Estimados" |
| **Stance and discourse particles** | Russian, Vietnamese, Arabic, English | ну, между прочим, nè, hả, طب, "actually" lost |
| **Focus and contrast** | Spanish, English | contrastive "yo", emphatic "sí tenemos" |
| **Register** (official vs colloquial) | English, Spanish, Hindi–Urdu | legal stiffness and slangy exasperation both came back neutral |
| **Passive with an agent** | Spanish | "serán retirados por el conserje" |
| **"It turned out"** | Arabic | a confirmed discovery became "he seems nice" (**o** read as "appears") |
| **Missing words** | all | trust, pessimistic, midday, early, late, oil, basin, gate, law, storey, formally, right (entitlement), pay-docking, even |

## Side findings

- **lon "I" = Vietnamese vulgarity, in practice:** the Vietnamese speaker says
  **lon** to the elderly landlord twice. That's a known accepted flaw, now
  observed in the setting where it hurts most.
- **Kin terms:** "father's sibling" has no older/younger, though the
  vocabulary method planned cheap older/younger modifiers. The translator
  didn't use them (T), and the docs don't show how.
- **names.py:** *Tư* → **tuu** breaks the documented glide rule (**tuwu**);
  Hindi ʋ → w though the doc only lists v → b; Denise and Janice come out the
  same; rhotic vs non-rhotic input gives different loans.
- **Rules translators found unclear, repeatedly:** whether **gun** "there is"
  works after a linker or a fronted phrase (10 mentions); clock times and
  digits vs words (5+); where a vocative goes (5 of 7 translators); whether
  **a** can combine with **min** for a rhetorical question (4); **de** with a
  third-person subject (2).
- **Test design flaw:** words left in [brackets] in the source language leak
  the source to the back-translator (Arabic, Hindi–Urdu). Next time,
  brackets should hold a neutral placeholder.

## Overall answer to "what have we missed?"

The content layer (who did what, when, how sure, from what source) is robust
across 12 languages and five registers. What was missed is the
**interpersonal layer**: standing relationships (graded "you", kin address),
respect for people talked about, stance particles, focus, and register. In
every language that marks them, they're lost or only rebuilt by a listener's
inference. Two of these (relationship pronouns, gender) were designed out on
purpose; the data now says nearly every language marks them.

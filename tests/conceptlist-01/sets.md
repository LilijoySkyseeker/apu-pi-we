# The sets pass (proposals only)

Source: design log 2026-10-16, "The three meals get roots, and sets are handled as sets". Some collections should be decided by hand as a set, so that each is complete, logical and on one level (all roots, or all built the same way), rather than concept by concept as frequency ranks them. One proposed decision per set. Nothing here changes `concepts.tsv`: these are proposals for the author.

**How coverage is read.** "Root" means on the list (`concepts.tsv`); a form in bold is today's form. "Phrase" and "built" mean a phrase or built word (`excluded.tsv`, `data/compounds.tsv`, the reference). "Missing" means it is on no list and has no stated form.

**Evidence.**
- **Ranks** are the corrected ranks in coverage-02 `candidates.tsv`. The walk stopped at rank 1342.
- **"n/24 families"** is deeplayer-01's count of WOLD families that have their own root for the meaning.
- **Lump rates** come from CLICS4, rung 4, using deeplayer-02's method and its narrower copy rule. `sets_rates.py` → `sets-rates.tsv`.

**One general point first.** The phrase line (at most 3 syllables, or the world's compound) works concept by concept. The kin and colour rules already override it for whole sets: son is **tiwu lowu** (4 syllables), brown **bilun buda**. The proposals below rely on the same reading: **a set built on one stated pattern counts as the world's compound for its members.** If the author doesn't accept that reading, the seasons and colours proposals change (see each one).

## Summary

| Set | Complete and on one level today? | Proposed decision |
|---|---|---|
| Meals | Yes: three roots | No change. Record that supper = dinner, "a meal" = **pasu** "food", snack = long tail |
| Times of day | Nearly: dawn is a root and dusk is missing | One root for dusk (parity with dawn); midnight stays built ("middle of night", the world's compound) |
| Days of the week | Yes: numbered (8.3.2) | No change (decided 2026-10-16); weekend = "week end", the world's compound |
| Months | Yes: numbered (8.3.3) | No change (decided 2026-10-16) |
| Seasons | No: four temperate phrases, two of them with no fixed form; rainy season built; dry season missing | Build all six one way, **[season] + its mark**: hot, cold, flower, harvest, rain, dry season |
| Directions, left/right | Yes: 4 cardinal + 6 relative roots | No change. In-between directions by juxtaposition (**soto anyu** "north-east") |
| Kin | Yes, by the kinship rule (method §3.1) | No new roots. State the age modifiers (**pani** / **loyen**) for older/younger sibling (CLICS: 45% lump) |
| Body parts | Yes: own-root parts are roots, sub-parts built "X of Y" | No change |
| Colours | No: six roots; brown and pink built, orange via the fruit, purple and grey missing | All five non-basic colours built one way, as mixtures of the six roots |
| Weather | Nearly: warm is a root, cool is missing | A root for cool (parity with warm); hail and drought stay out (no evidence) |
| Emotions | No: surprise exists only as a stance word; pity and envy pending | Three roots: surprise (split from **donon**), "pity, compassion" (covers mercy), "envy, jealousy" (one root) |
| Senses | Yes | No change. Spicy = **tikun** "hot", as in the decided chili phrase |
| Numbers-adjacent | Roots yes; fractions have no stated form | No new roots. Fractions (a third, a quarter) go to the author as a number-grammar question (section 9) |
| Opposites | Mostly: both poles of the basic pairs are roots, other negatives are built "not X" | Confirm "not X" as the default second pole; no new roots |

## 1. Meals

| Member | Coverage |
|---|---|
| breakfast | root (LAD) |
| lunch | root (ADD1, 2026-10-16) |
| dinner | root (ADD1, 2026-10-16) |
| supper | WOLD 5-45: covered by dinner (changed in round 2 from the phrase **pasu pi kegin**) |
| meal | missing as its own concept. **pasu** "food" covers it, as in many languages (sw *chakula*, hi *khānā*, zh 饭) |
| snack | rank 1899, long tail. Built "small food" (zh 小吃, id *makanan ringan*) |

- **Complete:** yes. All three main meals are roots, on one level.
- **Proposal:** no change. Record supper and "meal" as above.

## 2. Times of day

| Member | Coverage |
|---|---|
| morning, noon, afternoon, evening, night | roots: **leso minfi duwun kegin yami** |
| daytime | root (ADD1; split from **dili**) |
| today, yesterday, tomorrow | roots: **mefa afe wuma** |
| dawn | root (LAD, rank 1077; WOLD 14-43, 7/24) |
| dusk, sunset | missing (sunset rank 2171) |
| midnight | missing (rank 1937) |
| tonight | missing |
| last night | excluded as a construction (drops, 2026-10-16) |

- **Where the set disagrees:** dawn is a root and dusk has nothing. Both are the same kind of thing: a transition at one end of the day.
- **Options:**
  - (a) a root for dusk, for parity with dawn;
  - (b) both built, "morning start" and "evening start" (**leso tuko**, **kegin tuko**, 4 syllables), which takes dawn's root away;
  - (c) leave it as it is.
- **Proposal: (a).** Dawn already passed the frequency route. Dusk is the same concept at the other end of the day, and in rural life both mark the working day.
- **Midnight** stays built as "middle of night", the world's compound (zh 半夜, es *medianoche*, de *Mitternacht*, hi *ādhī rāt*).
- **Tonight** is **yami mefa** "tonight (this night)", built like the other "this X" phrases.

## 3. Days of the week

- **Members:** Monday … Sunday. A weekday is **dili mena** + 1–7, with Monday as 1 (ISO 8601; reference 8.3.2). week is the root **nelon**. weekend is missing (rank 2271).
- **Complete:** yes. The numbering is a closed system, and the names are their own system (drops, 2026-10-16).
- **Proposal:** no change. Weekend is "week end" **nelon fugi**, the world's compound (en, de *Wochenende*, zh 周末, ja 週末).

## 4. Months

- **Members:** January … December. A month is **dunan mena** + 1–12 (8.3.3). Month and year are the roots **dunan** and **fawu**. calendar is now the loan **kalendalu** (deeplayer-02).
- **Complete:** yes.
- **Proposal:** no change.

## 5. Seasons

| Member | Coverage | Evidence |
|---|---|---|
| season | root (LAD, rank 285) | WOLD 14-78, 6/24 |
| summer | **muyi tikun** "hot time" (compounds.tsv, 4 syllables) | rank 872; WOLD 11/24; SUMMER/HOT lump 1.4% |
| winter | **muyi weki** "cold time" (compounds.tsv, 4 syllables) | rank 814; WOLD 13/24; WINTER/COLD lump 2.0% |
| spring (season) | **muyi pi meyen** "time of flowers" (ladder, 5 syllables) | WOLD 10/24 |
| autumn | **muyi pi [harvest]** (WOLD P, 5 syllables) | WOLD 11/24 |
| rainy season | **muyi pi gegi** (compounds.tsv) | CLICS RAINY SEASON, only 10 families |
| dry season | missing | CLICS DRY SEASON, only 10 families |

- **Where the set disagrees:**
  - Two patterns are mixed: "time + quality" and "time of + noun".
  - **muyi** "time" makes "hot time" ambiguous with a hot spell.
  - The tropical pair is half there: rainy season has a form and dry season has none.
  - The four temperate names cover a climate many speakers don't have, which the 2026-10-16 "everyone's modern life" correction warns against.
- **The world:** the seasons have their own roots in roughly half the WOLD families, and CLICS shows nobody calls summer just "hot". Many tropical and Southeast Asian languages build them as "season + mark": id/ms *musim panas* "hot season", *musim hujan* "rain season", *musim kemarau* "dry season"; th *rúedu rón* "hot season".
- **Options:**
  - (a) build all six one way, **[season] + its mark**:
    - summer: **[season] tikun**;
    - winter: **[season] weki**;
    - spring: **[season] pi meyen**;
    - autumn: **[season] pi [harvest]**;
    - rainy season: **[season] pi gegi**;
    - dry season: **[season] kilan**;
  - (b) roots for the temperate four, and the rainy and dry seasons built;
  - (c) six roots.
- **Proposal: (a).**
  - One pattern covers every climate.
  - "Hot season" is literally right in both hemispheres; "summer" names different months in each.
  - It uses the season root the list already has.
- **Cost:** summer and winter (ranks 814 and 872) fall inside the frequency route, so the phrase line alone would give them roots. (a) depends on the set reading above. Add-back trigger: a test where speakers reach for a short word for summer or winter.

## 6. Directions, left and right

- **Members:**
  - **Cardinal:** north **soto**, south **monna**, east **anyu**, west **munke**.
  - **Relative:** left **funbe**, right **nata**, front **sinye**, back **nebe**, above **bige**, below **deba**; inside and outside, near and far are also roots.
  - **Movement:** rise (root, LAD), descend (root, round 2), forward **tun sinye**, backward **tun nebe** (compounds.tsv). direction is a root (LAD).
- **Complete:** yes, and on one level.
- **Proposal:** no change.
  - In-between directions are said by juxtaposition (**soto anyu** "north-east"), as most languages do.
  - Rise and descend are now both roots, recorded as an added antonym pair.

## 7. Kin

| Member | Coverage |
|---|---|
| mother, father, parent, child, sibling, spouse | roots (**mole wede tiwu faba ofin**); parent is new (2026-10-16) |
| family, relative, ancestor, baby, orphan, partner | roots (**yonyo**; the rest new) |
| son, daughter, brother, sister, husband, wife, boy, girl | built: + **lowu** / **futa** (gender is a modifier, B7) |
| grandparents, grandchild, uncle, aunt, cousin, nephew, niece, in-laws | composed with **pi** (method §3.1) |
| descendants | phrase **tiwu la** "children" (WOLD) |
| widow(er) | out (WOLD edge with an alternative; phrase **ewo pi ofin fafin**) |
| older and younger sibling | "cheap optional modifiers" (method §3.1); no modifier named |

- **Complete:** yes, by the decided rule.
- **The one gap:** the older/younger modifiers that §3.1 promises are never named. CLICS lumps OLDER and YOUNGER BROTHER (of a man) at 45.0% (range 39–51), so about half the world's families split them by root, and for many speakers (zh, ja, ko, id, hi, sw) the distinction is obligatory.
- **Proposal:** no new roots.
  - State that **pani** "old" and **loyen** "young" are the modifiers: **faba pani** "older sibling", **faba loyen** "younger sibling".
  - Grandparent is now **[parent] pi [parent]**.
  - Mother and father stay roots by the 2026-10-16 decision, though the other gendered kin are built.
  - Add-back trigger: speakers of the age-marking languages find **pani** "old, worn" wrong for people.

## 8. Body parts

- **Members:** 41 roots with forms (head to armpit), plus the new roots:
  - **ladder:** cheek, chin, forehead, muscle, womb, joint;
  - **WOLD:** ankle, wrist, elbow, heel, hip, waist, thigh, rib, jaw, gums, eyebrow, kidney, spleen, tendon, blood vessel, beard, snot, scar, pus.
- **How the boundaries were set:**
  - **By lump rate:** chest is merged into **egu** "breast", stomach into **suyon** "belly", and claw into **tolin** (round 2).
  - **Built "X of Y", as the world builds them:** skull, spine, eyelid, eyelash, nostril, palm, thumb ("big finger").
  - **Long tail:** earlobe, nape, molar, collarbone, shoulder blade, calf, temple.
- **Complete:** yes, and on one level. Parts with their own root in many families are roots, and sub-parts are built.
- **One visible asymmetry:** eyebrow is a root and eyelash is built. That follows the evidence (eyebrow WOLD core; eyelash weaker, per Codex's list and the 2026-10-16 decision).
- **Proposal:** no change.

## 9. Colours

| Member | Coverage |
|---|---|
| black, white, red, yellow, green, blue | roots **tago pinda wiwi bilun gisu deta** (decided 2026-10-08: six basic roots, the others compounds) |
| colour | root (LAD) |
| brown | built **bilun buda** "dark yellow" (rank 1696) |
| pink | built **wiwi pinda** "red white" (rank 1443) |
| orange | covered by the fruit root "orange" (the colour sense rank 1148 is pooled with the fruit) |
| purple | missing (rank 2067) |
| grey | missing (rank 1807); the method's example is "white + dark" |
| gold, silver | roots as metals (LAD) |

- **Where the set disagrees:** five non-basic colours are made three ways (a shade, a mixture, an object), and two of them have no form at all.
- **The world:** grey isn't lumped with black or white (CLICS 0.0% and 1.0%), so it is a colour of its own wherever a language names it. Orange is named after the fruit in most languages that have it (es *naranja*, ar *burtuqālī*, hi *nārangī*).
- **Options:**
  - (a) all five as mixtures of the six roots:
    - brown **bilun buda**;
    - pink **wiwi pinda**;
    - grey **pinda buda** (or **tago pinda**);
    - purple **wiwi deta**;
    - orange **wiwi bilun**;
  - (b) each the way the world most often does it: orange and purple from objects, grey from ash (**sulen**), brown and pink as now;
  - (c) roots for brown and grey (Berlin and Kay's next terms).
- **Proposal: (a).**
  - It is one pattern, learnable as a set, and keeps the 2026-10-08 six-root decision.
  - All five rank past the walk's stop, so the frequency route gives none of them a root anyway.
  - Orange the fruit stays a root.
  - Add-back trigger (the decided one): a test shows colour meaning lost.

## 10. Weather

| Member | Coverage |
|---|---|
| rain, snow, wind, storm, cloud, fog, thunder, lightning, ice, sun | roots with forms |
| dew, rainbow, freeze | roots (WOLD) |
| weather, climate, flood | roots (LAD) |
| hot, cold, wet, dry | roots with forms |
| warm | root (BAL; split from **tikun**; CLICS WARM/HOT 16.7%) |
| cool | missing (no usable rank: "cool" pools the slang sense) |
| temperature | loan candidate (pending the panel) |
| hail | missing (rank 2217; CLICS only 3 families) |
| drought | missing (no rank; not in WOLD) |

- **Where the set disagrees:** temperature has four steps, hot, warm, cool, cold. Three are roots and cool has nothing. The phrase **tason weki** "rather cold" (3 syllables) meets the line, but then warm would have to be **tason tikun** to match.
- **Options:**
  - (a) a root for cool;
  - (b) cool is **tason weki**, and warm stays a root;
  - (c) no change.
- **Proposal: (a), on parity.** The evidence is thin: no rank, and no CLICS COOL concept. The warm/hot split rate shows languages keep the middle steps apart.
- **Hail and drought stay out.** Hail is **nokun gegi** "ice rain" (as id *hujan es*, sw *mvua ya mawe* "stone rain"). Drought is a phrase from **kilan** "dry".
- Add-back trigger for drought: a rural-life test (the deep-layer route) shows it missing.

## 11. Emotions

| Member | Coverage | Evidence |
|---|---|---|
| happy, sad, angry, fear, love, disgust, hope, calm, panic, disappointed, miss | roots with forms | |
| hate | root (BAL) | |
| shame, proud, worry, regret, satisfied, tense/nervous | roots (LAD) | |
| surprise, astonished | **donon** "it turned out, surprisingly" (a sentence-end stance operator) | rank 640; WOLD 16-15, 14/24 |
| pity, mercy | pending: sets pass | rank 1431; WOLD 16-35, 9/24; PITY/GRIEF 1.1% |
| envy, jealousy | pending: sets pass | rank 1506; WOLD 16-44 (one meaning), 12/24 |
| guilty | out (WOLD 21-35, 3/24; **ibe [fault]**) | |
| grief | covered by **bayi** "sad" (WOLD) | |
| lonely, bored, curious, grateful, excited, joy | missing or long tail | bored 2255, curious 2240 |

- **Where the set disagrees:**
  - Of the six basic emotions most often listed (Ekman), five are roots. Surprise exists only as **donon**, a stance word, which can't say "I was surprised" or "a surprise".
  - Pity and envy were left to this pass.
- **Options:**
  - (a) three roots:
    - surprise: "surprise, be surprised", separate from **donon**, which stays the stance word;
    - "pity, compassion": mercy, the act of sparing, is built from it or from **forgive**;
    - "envy, jealousy": one root, as WOLD treats it as one meaning;
  - (b) surprise only: pity and envy past the walk's stop, out;
  - (c) no change.
- **Proposal: (a).**
  - **Surprise:** rank 640, 14/24 families.
  - **Envy:** 12/24 families. Pity is at 9/24. Both are at the strength of the edge items with no short alternative, which were admitted on 2026-10-16. Their phrases ("feel sad for", "want what another has") run 5 syllables or more.
  - **Envy and jealousy as one root:** CLICS has no JEALOUS concept, so rung 4 can't measure the pair. WOLD lumps them, and the decided sets principle prefers one level. Add-back trigger: a test where rivalry in love and envy of goods get confused.
- **Lonely, bored and the rest stay built** ("sad alone", "tired of"): all past the stop, and none in WOLD.

## 12. Senses

- **Members:**
  - **Senses as verbs:** see **nagu**, hear **nulu**, smell **kanko**, taste **tenmi**, touch **sanne**, feel **feme**.
  - **Active pairs:** look **miya**, listen **doma**.
  - **Sense nouns:** sound **ninge**; voice and "sense" are roots (LAD).
  - **Lacking a sense:** blind, deaf, mute (all roots, a set by the 2026-10-16 decision).
  - **Tastes:** sweet **sinta**, sour **tufun**, salty **lage**, bitter **finlu**; spicy is **tikun** "hot".
- **Complete:** yes.
- **Proposal:** no change.
  - Spicy stays **tikun**, as the decided chili phrase **[pepper] tikun** already uses it.
  - Add-back trigger: a test where "hot food" is read as temperature.

## 13. Numbers-adjacent words

- **Members:**
  - **Roots:** number **wifu**, count **sunbu**, half **timon**; percent, pair, sum/total, average, rate, measure and unit (new).
  - **Signs:** **guti** minus, **mimi** point, **unun** power.
  - **Ordinals:** **mena** + number (first = **mena ni**), and last is a root.
  - **Times:** **gimu** occasion (**gimu sa** "twice").
  - **Each:** **mesun**.
  - **Grammar words:** ALL, SOME, NONE, MORE, ONLY.
  - **Missing:** quarter, a third, any fraction.
- **Complete:** yes as words. What's missing is grammar: the reference gives no form for a fraction other than **timon** "half".
- **Proposal:** no new roots. Fractions (a third, three quarters) go to the author as a section 9 grammar question. One candidate is ordinal + part, but that is a grammar decision, outside this list.

## 14. Opposites

- **Today:**
  - The basic pairs in `data/antonyms.tsv` have a root at each pole (good/bad, strong/weak, ugly/beautiful …).
  - The list adds pairs where both poles passed separately: accept/refuse, love/hate, increase/decrease, lend/borrow, appear/disappear, win/lose, here/there, always/never, bless/curse, heaven/hell, keep/lose, and rise/descend (round 2).
  - Other second poles are built with negation: impossible, unpleasant, stupid (**mu gole**), forbid (**mu efon**), disagree, disobey, fake.
- **Where the set disagrees:** nowhere in principle. The few cases that look odd (ugly a root, stupid built) follow the evidence: ugly is in the seed's basic pairs, and stupid **mu gole** is 3 syllables, on the phrase line.
- **Proposal:**
  - Confirm "not X" as the default second pole: a pole gets its own root only when it passes a route on its own.
  - No new roots.
  - Keep every root–root pair in the antonym weighting, as now.

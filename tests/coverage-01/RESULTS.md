# Coverage measurement (coverage-01): results so far (2026-10-13)

20 everyday texts (talk, chat, news, how-to; 12 original languages), translated into Apupiwe at four vocabulary sizes, back-translated by cold readers (one per size), scored per meaning unit (799 units) by two AI scorers. Extra roots were placeholders taken from the modern-frequency concept list (Part 1) in rank order.

| Roots | Syllables | Exact | Vaguer | Wrong | Missing |
|---|---|---|---|---|---|
| today, 517 | 5,190 (100%) | 89.6% | 72 | 7 | 4 |
| 1,000 | 4,939 (95%) | 89.9% | 73 | 5 | 3 |
| 1,500 | 4,929 (95%) | 90.9% | 69 | 1 | 3 |
| 2,000 | 4,749 (92%) | 92.4% | 52 | 5 | 4 |

Per unit: 652 exact at every size; 46 gained with size (parties, poll, elections, warn, heartburn, ice cream, caviar, thermal paste…); 24 lost with size, almost all translator style (base wrote borscht, shashlik, vodka as names; larger sizes described them); 49 mixed (noise); 28 lost at every size.

## What it shows

1. **The effect is small:** +2.8 points of exact meaning and −8% length for +1,483 roots, judged by AI readers. No knee between 517 and 2,000.
2. **Translator noise is as big as the effect** (49 mixed units vs 46 gains): each size had its own translator agent.
3. **The ranking misses home life.** The 28 units lost at every size are mostly concrete household and food words that text corpora rank low: lemon 8,103, salad 6,961, pepper 7,478, refrigerator 4,797, torch 6,363, colleague 4,157, cooperative 4,115 (cash was merged into money). Written text (news, Wikipedia) under-represents the kitchen and the home; speech doesn't.
4. **AI readers are lenient** (resolved "black bean drink" as coffee, "milk fat" as butter); the author's sheet checks how lenient.

## Possible next steps

- Add a speech source to Part 1: OpenSubtitles 2018 frequency lists exist for 12 of the 20 panel languages (zh, ko, vi, th, id, bn, fa, ar, tr, ru, es, fr); plus the deep layer's child vocabulary (Wordbank) for home objects.
- Rerun Part 2 with one translator per text doing all four sizes in turn, so only vocabulary differs.

## Rerun (2026-10-13): speech frequencies, children's first words, one translator per text

Root lists: the 235 first-word concepts (Wordbank, ≥15 of 30 languages) with no root today come first, then the speech-and-text frequency order. Each translator made all four sizes of its texts by swapping phrases for newly available roots and changing nothing else. 748 meaning units per size.

| Roots | Syllables | Exact | Vaguer | Wrong | Missing |
|---|---|---|---|---|---|
| today, 517 | 5,039 (100%) | 84.4% | 106 | 7 | 4 |
| 1,000 | 4,841 (96%) | 88.1% | 82 | 4 | 3 |
| 1,500 | 4,802 (95%) | 90.2% | 67 | 2 | 4 |
| 2,000 | 4,734 (94%) | 89.7% | 72 | 2 | 3 |

**What it shows.**
1. **A clear curve this time:** +3.7 points from today to 1,000 roots, +2.1 to 1,500, then flat (−0.5, within scorer noise). The knee is at about 1,500.
2. **What's left at 2,000 is the long tail:** named dishes (caviar, borscht, shashlik, akkawi), diseases (dengue, heatstroke), specific tools and objects (parasol, bamboo blinds, curds, graphite, screws). Most are names, loans-to-be or rare concepts; more roots from the frequency list don't reach them.
3. **Length** falls 6% by 2,000; brevity is not where the gain is.
4. **For a person the gap is larger.** The phrase test (`guess/RESULTS.md`) found AI readers resolve about a third of the phrases a person misses, and today's vocabulary leans on such phrases far more than 1,500 roots does. So a person reading today's version would lose more than 15.6%; the curve's shape (steep to 1,000, flattening by 1,500) should hold, the size of the first step is understated.

## Part 4 measurement: should today's roots move? (2026-10-13)

`part4/placement.py`, 1,483 two-syllable roots (today's 500 + 983 new; operators held fixed), scored with the word tool's own confusion objective. New concepts' fields and tiers are approximated.

| Strategy | Score | Frequency-weighted nearest-neighbour confusion | Today's roots moved |
|---|---|---|---|
| A: add new roots one at a time (today's tool) | 61.7 | 0.0062 | 0 |
| B: place the new roots together | 59.4 (−4%) | 0.0055 (−12%) | 0 |
| C: place everything together | 56.4 (−9%) | 0.0044 (−29%) | 278 of 500 |

**apu** stays. Moves are spread across tiers (5 of 15 at tier 5, 33 of 46 at tier 1) and many are small (**kiti** → **kidi**, **wede** → **wedi**). The gain is real under the model, but the model is the one the review called unvalidated (B2; no listening test yet), so a full re-placement fits to an untested model.

## Non-European checklists (Part 5, stage 6)

`part3/wordbank-nonwestern.tsv`, 192 rows. Wordbank word items on the non-European checklists (Kiswahili, Kigiriama, Mandarin Beijing and Taiwanese, Cantonese, Korean, Japanese, Persian, Turkish, Hebrew) whose concept is on at most 5 of the 21 European languages' checklists, matched by uni_lemma and gloss. Items whose gloss is more specific than their uni_lemma (chapati under bread, ugali under porridge, msikiti under church) were added by hand. Persian and Chinese items with no gloss were translated. Function words were left out. The Arabic file in the cache is a 404 page, so Arabic is missing; so are American and Australian English (Irish English stands for English). Each row is tagged EVERYDAY (common across many non-Western households), regional (one large region), local (one culture, or a name or brand) or general (common in Europe too; the European checklists just leave it out).

**What it shows.**
1. **Most gaps are general, not Western.** About 70 rows (body parts, verbs, town objects) are concepts every culture has. The European checklists simply don't list them. They belong on the frequency ladder, not on this list.
2. **61 rows are EVERYDAY.** About half are already covered by a root, a planned root or a composed phrase. Examples: market, village, porridge, carpet for mat, yard for courtyard, bus for minibus, cart, sibling plus age, kinship with the side always stated, the honorific root, welcome.
3. **Everyday concepts Apupiwe has no word for:** chili pepper, spicy, noodles (pasta is only a borrowing or phrase), coconut, mango, ginger, lemon/lime, shrimp, eggplant (one checklist), chopsticks, basin, tray, kettle/teapot, cockroach, lizard/gecko, camel, bracelet/bangle, earring, machete, kite, squat, greet, hang (laundry). Flour, herder and cooking stick have none either, but they compose easily.
4. **Roots that cover an everyday concept only if their definition is widened:** spade for hoe, balcony for veranda/baraza, cloth for the wrapper cloth (kanga, sarong; also the usual baby sling), carpet for sleeping mat, porridge for stiff staples (ugali, fufu, nsima), soup/sauce for the stew or relish eaten with the staple.
5. **Limit: the non-European checklists are adaptations of the American CDI and keep its frame.** No checklist has a mortar, a baby sling, firewood, a water well or charcoal, so this method can't find them. In Apupiwe, mortar, well and charcoal have no word; firewood composes (fire + wood). The baby sling shows up only indirectly, through 'carry on the back' (Cantonese, Mandarin, Japanese) and the kanga. Kiswahili and Kigiriama are the most locally adapted lists, and they supply most of the EVERYDAY rows.

## Part 5: regional rebalance (2026-10-13)

16 texts added from the regions the first 20 missed (Tagalog, Yoruba, Tamil, Korean, Bengali, Vietnamese, Persian, Mandarin ×2, Hausa, Amharic, Thai, Indonesian, Hindi, Arabic, Quechua), same method as part2b (one translator per text across sizes; cold readers; two scorers). Exact meaning per size:

| Texts | today | 1,000 | 1,500 | 2,000 |
|---|---|---|---|---|
| all (36) | 80.0% | 85.3% | 88.2% | 88.3% |
| first 01–20 (20) | 84.4% | 88.1% | 90.2% | 89.7% |
| new 21–36 (16) | 75.3% | 82.2% | 86.0% | 86.8% |
| East Asia (6) | 75.7% | 81.2% | 84.9% | 86.2% |
| SE Asia (5) | 83.3% | 90.7% | 92.6% | 93.5% |
| South Asia (4) | 76.0% | 79.5% | 84.9% | 86.3% |
| West Asia (4) | 78.1% | 81.1% | 85.2% | 84.6% |
| Africa (5) | 83.9% | 91.5% | 91.0% | 91.9% |
| Americas (1) | 51.3% | 69.2% | 79.5% | 79.5% |
| Europe (11) | 83.6% | 86.8% | 89.5% | 88.0% |
(Region counts are texts; the Americas have only one text, a Quechua recipe, so that row is noise.)

**What it shows.**
1. **The size holds.** Over all 36 texts the gains flatten at about 1,500 (80.0 → 85.3 → 88.2 → 88.3%). The new texts start lower (75.3% today vs 84.4%) and gain more at each step, but they also flatten after 1,500 (86.0 → 86.8%).
2. **The concept list has a non-European blind spot, and it is mostly the kitchen.** The recipes lose most: even at 2,000 roots there is no word for frying, soaking, chopping, rinsing or slicing, and no seasonings beyond salt and onion (garlic is "small white onion", ginger "hot root", chili "hot green fruit"). Text frequency undercounts home cooking everywhere, which is why these sit below the frequency cut.
3. **What else the translators had to say with phrases** (`part2b/notes-T5`…`T8`): farming (crop, sow, plant, rice paddy), health (disease as a noun, fever, chills), society (fast, monk, elder, naming ceremony), qualities (tasty, necessary, typical), time (recently, annual, a while), and small words (together, "the more… the more", "really").
4. **The rest of the long tail is culture-bound** (hilsa, phở, jiaozi, pounded yam, teff, ginseng): borrowings under the borrowing rule, not roots.
5. With the non-European checklist comparison (stage 6), the candidates to add go through the ladders: most pass the deep-layer test as household and daily-life concepts found across cultures.

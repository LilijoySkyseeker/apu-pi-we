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

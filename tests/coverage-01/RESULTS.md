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

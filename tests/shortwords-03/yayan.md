# ya~yan: can BEFORE and YOUKNOW be separated for free? (2026-10-16)

**Question** (design log 2026-10-16, last entry): BEFORE = **ya** and YOUKNOW = **yan** differ only by a final -n
(22% in the worst listener variant; they never share a position). Separate them only if it's free: one word moves,
nothing else changes, and the robust score doesn't get worse.

**Answer: no move qualifies.** Nothing changes; **ya** and **yan** stay.

## Method

`yayan.py` (this folder) takes the adopted layer `runs/sens-g-mid-lock-0.01-control-1.tsv` (= `data/grammar.tsv`
today; `rebuild.py score` reports 0 changed) and tries every single-word move of YOUKNOW, then of BEFORE, to every
other syllable, all other words fixed. Variant set: `confusion2.variants()` as it defaults now (48, av/lp off),
selected with the new `SW_VARIANTS=default` in `rebuild.py` (its `all` still means 50). Run:
`SW_VARIANTS=default python3 yayan.py`; every move is in `yayan-moves.tsv`.

A move qualifies if it (1) leaves the two forms no longer a merger-type pair, (2) passes `hard_ok` (onset, digits
open, no shared form, no merger with a word sharing a position, not `offensive.blocked`), (3) adds no merger-type
pair with any short word, shared position or not (trading ya~yan for another such pair isn't a separation), and
(4) has a robust score equal or better.

## Result

Adopted layer, 48 variants: **robust 0.3134**, penalties (offensive tie-break 36, one-feature 15, operator 0),
objective 0.4454, 14 merger-type pairs in all, none between words sharing a position. (With 50 variants,
`SW_VARIANTS=all`, the same layer scores 0.3120.)

| | moves | taken | no onset | blocked | shared-position merger | legal |
|---|---:|---:|---:|---:|---:|---:|
| YOUKNOW (yan) | 139 | 68 | 10 | 5 | 3 | 53 |
| BEFORE (ya) | 139 | 68 | 10 | 5 | 55 | 1 |

Every legal move separates the pair; only two add no new merger-type pair; **none keeps the robust score**.
Best legal moves:

| move | robust | change | new merger-type pairs | offensive tie-break |
|---|---:|---:|---|---:|
| YOUKNOW yan → **lo** | 0.3137 | +0.0004 | none | 37 (+1) |
| YOUKNOW yan → tin | 0.3141 | +0.0008 | INSTRUCT, WE.excl | 37 |
| YOUKNOW yan → ken | 0.3142 | +0.0009 | MORE, RESULT | 37 |
| YOUKNOW yan → len | 0.3143 | +0.0010 | ONGOING | 36 |
| YOUKNOW yan → sen | 0.3144 | +0.0010 | FROM | 37 |
| BEFORE ya → **lo** (its only legal move) | 0.3244 | +0.0110 | none | 37 (+1), one-feature 18 (+3) |

The nearest miss, YOUKNOW → **lo**, is 0.0004 worse (about 0.1%) and adds one offensive tie-break match, so it
fails the rule as set. Taking it anyway would be the author's call: the cost is small, but so is the gain the
model sees (the 22% is one variant of 48, between two words that never share a position).

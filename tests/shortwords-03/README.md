# Short-word rebuild, rerun on today's setup (2026-10-15)

Question: the dry run (`tests/shortwords-02/`) rerun with what changed since, so the author can make Decision 2 (full rebuild, a middle option, or the minimal patch) and settle the name **apu pi we**. Task: `PROMPT.md` (with its addendum: the new word ENDEAR). Nothing outside this folder is changed.

## Progress (resume here)

- [x] copied `positions.py`, `rebuild.py` from shortwords-02 (its results untouched); rebuild.py: blocked = hard rule H5, matches = C3 tie-break, `SW_VARIANTS`/`SW_OVERRIDE`, `--lock`, `reopt`, `score`, `report name=file`
- [x] `positions.py` substitution rerun (15:17–15:52; `extend` added the UDHR frame the quote fix let through) → `substitution.tsv`, `frames.txt` (329 frames), `adjacency.tsv`, `corpus-counts.tsv`; `modmod.tsv`, `operators-extra.tsv`. Checked after the restart: complete (4,893 rows as in the dry run; the 4 bogus frames "1\" … "4\" gone, 11 new frames, one of them the UDHR quote frame).
- [x] restart (addendum): ENDEAR added: `positions.py endear` → `endear.tsv`; rebuild.py: word ENDEAR (freq 1.0), position P16, in every option (patch: forced into the change set like MODMOD). Runs of the stopped run (no ENDEAR) are void; `runs/patch-*-anneal.tsv`, `runs/patch-*-pol*.tsv` are leftovers from it.
- [x] host crash ~16:26, resumed 21:00. Checked every file: all `runs/full-s1..12`, `full-lock-s1..12`, `mid-0.02-s1..12`, `mid-lock-0.02-s1..12`, `mid-0.04-s1`, `mid-lock-0.04-s1` have 71 lines and a "wrote" line in their log; `patch.tsv`, `patch-lock.tsv` complete (log ends "wrote", 16:14); `full.tsv`/`full-lock.tsv` picked (s9, lock s1). Killed mid-run: hold-out `-ha` batch (no files written). Since then rebuild.py writes layers atomically and `runs.sh`/`checks.sh` skip any command whose `--out` file exists, so a step is resumed by rerunning it.
- [x] patch free / locked (200k steps per change set)
- [x] full free / locked (12 seeds × 1.5M steps)
- [x] keep sweep 0.02, 0.04 from the patch (`runs.sh mid`): picked mid-0.02 = s11 (25 changes), mid-lock-0.02 = s2; mid-0.04 = s11 (14 changes), mid-lock-0.04 = the patch (all 12 seeds stuck). 11 of 12 free seeds at 0.04 and 6–7 of 12 at 0.02 never left the patch.
- [x] `FROM=0.02 KEEPS=0.04 runs.sh mid-alt` (0.04 also started from mid-0.02, added: is the patch a trap?): best from there 1.343 (free) / 1.359 (locked), worse than the patch-started picks, so mid-0.04 = s11 (14 changes) and mid-lock-0.04 = the locked patch stand. `KEEPS=0.01 runs.sh mid` (added third point: gap between 25 and 66 changes): mid-0.01 = s8 (34 changes), mid-lock-0.01 = s8.
- [x] second host crash ~21:35, resumed 23:00. Checked: `patch-ha.tsv`, `patch-hb.tsv`, `full-ha.tsv` (s6) and `runs/full-ha-s1..12`, `runs/full-hb-s1,8,11` complete (71 lines, log ends "wrote"); the other `full-hb` seeds were cut off and wrote no file. Ran at most 6 processes at once from here.
- [x] interrupted again ~23:11 (session stop, not a crash). Checked 23:13: every `runs/*-h[ab]-s*.tsv` present had 71 lines and a "wrote" log line (full-ha/hb 12 + 12, mid-0.01-ha 12, mid-0.02-ha 12); `mid-0.04-ha` had been cut off (no files). The owner (relayed with the resume request, 23:12) said the crashes were unrelated and the full 16 cores may be used, so the remaining steps ran with `P=16`.
- [x] hold-out check: `P=16 KEEPS="0.01 0.02 0.04" checks.sh holdout` → `holdout.txt` (23:18; picks full-ha s6, full-hb s6, mid-0.01-ha s8 / hb s2, mid-0.02-ha s11 / hb s12, mid-0.04-ha s10 / hb s3)
- [x] sensitivity and drop test (23:20–23:35) for full, mid-lock-0.01, mid-lock-0.02. Two passes per layer: annealing (`NAME=full`, `mid-lock-0.01` …) and greedy (`NAME=g-…`, `OPTS` + `--T0 0`, added: see "Sensitivity"). Commands: `LAYER=mid-lock-0.01.tsv NAME=g-mid-lock-0.01 OPTS="--keep 0.01 --lock OF,ALL --T0 0" P=16 checks.sh sens`, then the same with `drop`; full: `OPTS="--T0 0"`. `LAYERS="full.tsv full-lock.tsv mid-0.01.tsv mid-lock-0.01.tsv mid-0.02.tsv mid-lock-0.02.tsv mid-0.04.tsv mid-lock-0.04.tsv patch.tsv patch-lock.tsv" checks.sh sens-score` → `sens-score.txt`; the same layers scored with `SW_VARIANTS=no-av` / `no-lp` → `drop-score.txt`. Summaries: `checks.py vsctl NAME`, `checks.py rank`.
- [x] report (this file)
- [ ] author: Decision 2 and the name (end of this file)

## Headline

| option | words changed (of 67 existing) | robust score (lower is better) | merger pairs | offensive tie-break matches (C3) | the name | ENDEAR |
|---|---|---|---|---|---|---|
| today (MODMOD, ENDEAR at their best free forms) | 0 | **0.692** | 12 (+5 vowel-only words) | 36 | apu pi we | (yon) |
| **full rebuild** | 66 | **0.243** | 0 | 33 | apu yin fen | lin |
| full rebuild, name locked | 65 | 0.246 | 0 | 34 | **apu pi we** | bi |
| middle, keep 0.01 | 34 | 0.311 | 0 | 36 | apu wen fun | fo |
| **middle, keep 0.01, name locked** | 37 | **0.307** | 0 | 34 | **apu pi we** | fi |
| middle, keep 0.02 | 25 | 0.361 | 0 | 35 | apu yin we | fo |
| middle, keep 0.02, name locked | 24 | 0.381 | 0 | 36 | **apu pi we** | lo |
| middle, keep 0.04 | 14 | 0.422 | 0 | 39 | apu pan we | fo |
| middle, keep 0.04, name locked (= the locked patch: no seed left it) | 12 | 0.560 | 0 | 39 | **apu pi we** | si |
| **minimal patch** (every merger pair removed) | 11 | **0.549** | 0 | 39 | apu pin we | gen |
| minimal patch, name locked | 12 | 0.560 | 0 | 39 | **apu pi we** | si |

Robust score: mean of the worst quarter of the 50 model variants (`confusion2.variants()`, now with src-av and src-lp), each variant's cost divided by its median over 400 random layers, so 1.0 is a random layer. Not comparable with the dry run's numbers (48 variants, other positions). No option uses a blocked form (`offensive.blocked`: hard rule). MODMOD and ENDEAR are new everywhere and not counted as changes.

**Cost of the name lock** (pi = OF, we = ALL keep their forms):

| option | free → locked robust score | words changed | verdict |
|---|---|---|---|
| full | 0.243 → 0.246 (+0.004) | 66 → 65 | within seed noise (free seeds 0.243–0.255, locked 0.244–0.258) |
| keep 0.01 | 0.311 → 0.307 (−0.003) | 34 → 37 | free: the locked run scored better |
| keep 0.02 | 0.361 → 0.381 (+0.020) | 25 → 24 | real cost, and the locked layer keeps **pi~ti** (OF/D1, 9.5% best, 29% worst variant) |
| keep 0.04 | 0.422 → 0.560 (+0.138) | 14 → 12 | the locked sweep never left the patch; the free one escaped by moving **pi** |
| patch | 0.549 → 0.560 (+0.010) | 11 → 12 | one extra word |

The lock costs nothing in the full rebuild and at keep 0.01, about 0.01–0.02 in the patch and at keep 0.02, and only at keep 0.04 is it large (a search trap, not a property of **pi**).

Ten most frequent words (to, yen, me, wan, pi, gun, mu, mon, tun, wun): the full rebuilds change 10 and 9; mid-0.01 changes 4 (**yen me pi mu**), mid-lock-0.01 2 (**me → nun**, **mu → su**), mid-0.02 4, mid-lock-0.02 1 (**me**), mid-0.04 2, the patch 1 (**pi**), the locked patch 0.

**Main findings.**
1. **The ordering is the dry run's:** full < middle < patch, and the curve is steep at first: 11 changes 0.55 → 14 changes 0.42 → 25 changes 0.36 → 34–37 changes 0.31 → 66 changes 0.24. It survives the hold-out check and every parameter's range (below).
2. **The forms are still not determined.** Twelve seeds of the full rebuild agree on 2.7% of words (locked 7.5%); twelve of mid-lock-0.01 on 22%, and only 4 words are kept in all 12 (two of them the locked pair). The best-by-objective pick of mid-lock-0.01 happens to keep **to, yen, wan, gun, mon, tun, wun**, but only 2 of 12 seeds keep **to**. The keep dial sets *how many* words change, not *which*.
3. **The two new listener groups change no form** of the recommended layer (drop test). They matter only for the layers that keep today's p/t, f/p and voicing pairs: src-av is the worst variant of the patch.

## Method

As in the dry run (`../shortwords-02/README.md` "Method": rules H1–H4, positions, weights, robust objective, annealer, patch by minimum vertex covers), with these changes. **added** marks my choices.

| part | source |
|---|---|
| offensive filter: `offensive.blocked` (5 one-syllable forms: ku kun lan lun lon, plus REJECTED) is hard rule H5; `offensive.matches` is a tie-break of 0.002 each (the dry run's "C3 mode") | design log 2026-10-15 (tiered filter), goal C3 |
| 50 variants from `tools/confusion2.variants()` (src-av, src-lp added), CVaR 0.25, normalised by random-layer medians | design log 2026-10-15; `research/notes/confusion-data.md` §8.5, §9.5 |
| positions: GF substitution rerun with the fixed `positions.py` (329 frames; "command not parsed" no longer counts as a parse, quote marks handled) | task item 3 (fix of 2026-10-15) |
| frequencies unchanged | task item 4 (checked 2026-10-15, `tests/grammar-rebuild/codex/`) |
| **ENDEAR**: one-syllable grammar word after a noun or a name; freq 1.0; position from 5 hand frames (`endear.tsv`: *totu X sin obu*, *to nagu totu X*, *en mara X sin obu*, *en mara X , tin obu*, *tin obu , en mara X*); a word shares its position if it parses in at least one frame | author, task addendum 2026-10-15; freq 1.0 **added** (unmeasured; child-directed speech would be higher, ordinary text lower) |
| ENDEAR shares a position with 48 of the 67 other grammar words and digits: all pronouns, determiners, digits, relation words except **pi**, the linkers, the phrase operators, **en**, **bu**. It doesn't with the 19 that can't end a noun phrase: speech acts and politeness (**min so tin fon de yo ba nun a**), **kon**, **sin le gun**, **pi**, **man**, the derivation markers **no ge du pu** | computed (`endear.tsv`) |
| annealing: full 12 seeds × 1.5M steps (dry run's C3 setting); middle 12 seeds × 400k steps from the patch (dry run); best of 12 by objective | dry run |
| patch: 200k annealing steps per minimum change set (dry run 6,000) | **added**: at 6,000 the objective stayed ~0.02 above what longer runs found |
| keep sweep: 0.01 added to 0.02 and 0.04; 0.04 also started from mid-0.02 | **added**: the gap between 25 and 66 changes; is the patch a trap at 0.04 (it isn't: the restarts scored worse) |
| name lock: `--lock OF,ALL` (keep today's form; their pairs still obey H1–H5) | task |
| hold-out split: half-a / half-b stratified (half of the 32 Latin-hypercube draws, half of the rest), fixed seed 7 | **added** (notes §6.6 gives no split) |
| sensitivity parameters: voice_mult, L2_voicing_m, reseg_n_V, gem_n_N, coda_loss, coda_add, glide_hiatus (front and back together), V_ratio, L2_mid_m, E_C, C_none_after_vowel, each at its low and high end in every v2 variant | **added** from notes §6.5 ("voicing and the -n junctions") and §7 (biggest uncertainties) |
| layers checked: full, mid-lock-0.01, mid-lock-0.02 | **added**: the free optimum and the two name-locked middle candidates |

## Old → new forms

`forms.tsv` has every word in every option; `results.txt` marks C3 tie-break matches. Changed forms are in bold. mid-lock-0.04 is identical to patch-lock and left out.

| word | freq | old | full | full-lock | mid-0.01 | mid-lock-0.01 | mid-0.02 | mid-lock-0.02 | mid-0.04 | patch | patch-lock |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q | 4 | min | **du** | **ki** | min | **bi** | min | min | min | min | min |
| REQUEST | 2 | so | **lo** | **nu** | **bun** | **ta** | **me** | **bun** | so | so | so |
| INSTRUCT | 1.5 | tin | **li** | **lo** | **ben** | **ti** | **bun** | **bi** | **si** | **pun** | tin |
| ADVISE | 1 | fon | **ta** | **ta** | fon | fon | fon | fon | fon | fon | fon |
| INTEND | 2 | de | **be** | **be** | **sa** | **me** | de | de | de | de | de |
| WARN | 0.5 | yo | **ne** | **to** | yo | yo | yo | yo | **len** | yo | yo |
| WH | 3 | yu | **nen** | **ya** | yu | yu | yu | yu | yu | yu | yu |
| UNSPEC | 1 | bo | **wi** | **da** | bo | **pa** | bo | bo | bo | **son** | **son** |
| NOT | 7 | mu | **su** | **sen** | **su** | **su** | **su** | mu | **yon** | mu | mu |
| CONF | 1.5 | kon | **bo** | **bo** | **win** | **pe** | kon | kon | kon | kon | kon |
| I | 10 | to | **tun** | **men** | to | to | to | to | to | to | to |
| YOU | 8 | me | **fi** | **yi** | **nun** | **nun** | **mu** | **nan** | me | me | me |
| WE.incl | 3 | pen | **tan** | **so** | **pon** | **kan** | **pon** | **fun** | pen | **bon** | pen |
| WE.excl | 3 | din | **nan** | **te** | din | din | din | din | din | din | **gen** |
| HE/SHE | 8 | wan | **mu** | **lin** | wan | wan | wan | wan | wan | wan | wan |
| OBVIATIVE | 2 | yi | **de** | **ma** | **son** | yi | **fun** | yi | yi | yi | yi |
| LOGOPHOR | 1 | sun | **gan** | **wan** | **san** | **gen** | **fen** | **pon** | sun | sun | sun |
| PLURAL | 4 | la | **no** | **gin** | **gen** | la | la | la | la | la | la |
| THIS | 4 | tan | **wun** | **tin** | tan | **win** | tan | tan | tan | tan | tan |
| THAT.dem | 3 | ben | **sin** | **non** | **ten** | ben | ben | ben | **gen** | ben | **pun** |
| ALL | 3 | we | **fen** | we | **fun** | we | we | we | we | we | we |
| SOME | 2 | in | **ya** | **tan** | **yon** | **go** | **yon** | **yon** | **pon** | **yon** | **yon** |
| PART | 1 | kin | **yu** | **ko** | kin | kin | kin | kin | kin | kin | kin |
| NONE | 1 | fa | **don** | **ton** | fa | **fen** | fa | fa | fa | fa | fa |
| DONE | 3 | sin | **me** | **le** | sin | sin | sin | sin | sin | sin | sin |
| ONGOING | 2 | le | **da** | **nan** | **me** | le | le | **pan** | le | le | le |
| OF | 8 | pi | **yin** | pi | **wen** | pi | **yin** | pi | **pan** | **pin** | pi |
| AT | 5 | mon | **ni** | **sa** | mon | mon | mon | mon | mon | mon | mon |
| TO | 5 | tun | **fun** | **fe** | tun | tun | tun | tun | tun | tun | tun |
| FROM | 3 | se | **fo** | **win** | se | se | se | se | se | se | se |
| WITH | 3 | gan | **nun** | **sun** | gan | **nan** | gan | gan | gan | gan | gan |
| FOR | 3 | li | **la** | **ne** | li | **fan** | **ten** | li | li | li | li |
| BEFORE | 1.5 | ya | **pin** | **bon** | ya | ya | ya | ya | ya | ya | ya |
| AFTER | 1.5 | wo | **son** | **den** | wo | **kon** | wo | wo | wo | wo | wo |
| AND | 9 | yen | **wan** | **mun** | **yin** | yen | **lin** | yen | yen | yen | yen |
| OR | 2 | lu | **le** | **do** | lu | lu | lu | **men** | lu | lu | lu |
| BUT | 2 | un | **yo** | **kan** | **ba** | **ka** | **do** | **pen** | **ten** | **ten** | **ten** |
| IF | 2 | don | **pu** | **la** | don | don | don | don | don | don | don |
| BECAUSE | 1.5 | gi | **ke** | **po** | **la** | **bo** | gi | gi | gi | gi | gi |
| THAT.comp | 5 | wun | **bi** | **ba** | wun | wun | wun | wun | wun | wun | wun |
| WHO.rel | 4 | man | **mon** | **nin** | **pan** | **fun** | man | man | man | man | man |
| BE | 8 | gun | **ti** | **mi** | gun | gun | gun | gun | gun | gun | gun |
| MORE | 3 | ke | **fan** | **yun** | ke | ke | ke | ke | ke | **pan** | ke |
| VERY | 3 | bi | **gen** | **gu** | **de** | **ten** | bi | **win** | bi | bi | **bin** |
| LIKE | 3 | fu | **lu** | **lu** | **fen** | **son** | **son** | **fo** | **son** | fu | fu |
| GENERIC | 3 | go | **pon** | **pun** | go | **dan** | go | go | go | go | go |
| ONLY | 3 | na | **ye** | **won** | **gi** | **ga** | na | **ten** | na | na | na |
| WHILE | 2 | nin | **kon** | **ken** | **pin** | **min** | **pin** | nin | nin | nin | nin |
| EXCLAIM | 1.5 | ba | **yan** | **yan** | **bi** | ba | **len** | **sun** | ba | ba | ba |
| SELF | 3 | nen | **ka** | **mo** | nen | nen | nen | **nun** | nen | nen | nen |
| POLITE | 3 | nun | **ba** | **wa** | **fan** | **fin** | **fan** | **fan** | nun | nun | nun |
| IT | 5 | bu | **wen** | **dun** | **pe** | **bun** | **pe** | **len** | **bun** | bu | bu |
| AGENT | 4 | no | **min** | **di** | no | no | no | no | no | no | no |
| RESULT | 2 | ge | **din** | **yen** | **len** | **gi** | **gen** | **gen** | **pin** | ge | **pan** |
| TOOL | 3 | du | **go** | **fan** | du | du | du | du | du | du | du |
| PLACE | 3 | pu | **se** | **fin** | pu | pu | pu | pu | pu | **ken** | **fin** |
| NAME | 4 | en | **kin** | **gon** | **ti** | **fo** | **yan** | **yan** | **fun** | **yan** | **yan** |
| ALSO | 4 | fe | **gun** | **fu** | **nan** | **pon** | **nun** | fe | fe | fe | fe |
| EVEN | 3 | wi | **yon** | **gan** | wi | **yon** | wi | **son** | wi | wi | wi |
| FOCUS | 3 | o | **ten** | **fon** | **ma** | **lin** | **ti** | **ba** | **ti** | **ti** | **bon** |
| YOUKNOW | 3 | a | **won** | **son** | **le** | **yan** | **da** | **wi** | **ben** | **fan** | **fan** |
| MODMOD | 1 | — | dan | man | kon | tan | ko | fin | su | su | su |
| ENDEAR | 1 | — | lin | bi | fo | fi | fo | lo | fo | gen | si |
| D0 | 4 | po | **pe** | **ge** | **ye** | **ma** | **ba** | **su** | **mu** | po | po |
| D1 | 4 | fi | **gi** | **wu** | fi | **ni** | fi | **ti** | fi | fi | **di** |
| D2 | 4 | sa | sa | **tu** | **mu** | sa | sa | sa | sa | sa | sa |
| D3 | 4 | ka | **to** | **yo** | ka | **de** | ka | ka | ka | ka | ka |
| D4 | 4 | da | **ma** | **ka** | da | **mu** | **ye** | da | da | da | da |
| D5 | 4 | te | **wo** | **si** | **ni** | **wo** | **ni** | **ne** | te | te | te |

(Rows by frequency, as in `forms.tsv`.)

**ENDEAR's form** in each option: full **lin**, full-lock **bi**, mid-0.01 **fo**, mid-lock-0.01 **fi**, mid-0.02 **fo**, mid-lock-0.02 **lo**, mid-0.04 **fo**, patch **gen**, patch-lock (= mid-lock-0.04) **si**. Several are another word's old form: **fi** is today's "1", **bi** today's "very", **si** is free today.

**Reused forms.** The objective counts changes, not reuse, so new forms are often other words' old ones: mid-lock-0.01 has 14 (**Q = bi** was "very", **INTEND = me** was "you", **YOU = nun** was "please", **ENDEAR = fi** was "1", **D4 = mu** was "not" …), mid-0.02 5, mid-lock-0.02 6, full-lock 28, the patches 0. Grammar slots may reuse freed grammar forms (design log 2026-10-10, "the space is finite"), and nobody has learned v1 yet, but a learner of v1 would feel it.

## Pairs fixed

"Fixed" = no longer a merger and under 2% confusion for the worst v2 variant (symmetric). Per-pair numbers: `results.txt`.

| option | desk analysis's 16 pairs | model v2's 13 most robustly dangerous short pairs | shared pairs ≥ 10% in some variant |
|---|---|---|---|
| today | 0 | 0 | 28 |
| full | 16 | 13 | 4 |
| full-lock | 16 | 12 (left: **gu~wu** VERY/D1 5%) | 4 |
| mid-0.01 | 15 (left: **yo~wo** 3%) | 12 (left: **fen~pe** LIKE/IT 2%) | 10 |
| mid-lock-0.01 | 14 (left: **ya~yan** BEFORE/YOUKNOW 22%, final -n, the two never share a position; **bun~pu** IT/PLACE 2%) | 12 (left: **ti~kin** INSTRUCT/PART 2%) | 8 |
| mid-0.02 | 13 (left: **yo~wo**, **bo~ba**, **ya~da**, 3–4%) | 9 (left: **la~na** 28%, **bi~fi** 15%, **fa~sa** 9%, **de~gen** 2%) | 13 |
| mid-lock-0.02 | 11 (left: **pi~ti** OF/D1 29%, **de~ne** 5%, **yo~wo**, **yen~yan**, **fo~pu** 2–3%) | 7 (left: **pi~ti** 29%, **min~nin** 11%, **fa~sa**, **se~fe** 9%, **fo~pu**, **de~gen** 2%) | 9 |
| mid-0.04 | 12 (left: **de~te** voicing merger in different positions, **pen~gen**, **yi~wi**, **bun~pu**) | 6 | 21 |
| patch | 10 (left: **de~te**, **yo~wo**, **yi~wi**, **pin~fi**, **yen~yan**, **pin~bi**) | 3 (left: **to~po** 29%, **la~na** 28%, **fa~ba**, **fu~bu**, **bi~fi**, **min~nin** …) | 19 |
| patch-lock | 11 (left: **de~te**, **yo~wo**, **yi~wi**, **pi~bin**, **yen~yan**) | 4 | 19 |

Every option removes every merger pair (H4); the patches leave model v2's dangerous pairs that aren't mergers, since the patch rule only targets mergers. The worst pairs left in the middle options are one-feature vowel or liquid pairs that one variant (no mid vowels, or l/d) hears at 28% (`results.txt`, "closest shared-position pairs").

## Operators that would need renaming

- today, mid-0.04, mid-lock-0.04, the patch and the locked patch: **mesun** and **mena** (first syllable **me** = "you", which stands where they stand);
- full, full-lock, mid-0.01, mid-lock-0.01, mid-0.02, mid-lock-0.02: none (they all move **me**).

## Digit and content-word clashes (rule 4)

Content words (loans exempt) that would begin with a new digit syllable, re-formed later in the joint placement of the roots: full 24, full-lock 28, mid-0.01 15, **mid-lock-0.01 26** (**ma- ni- mu- de- wo-**: **mala makon nimo musu demi wonin** …), mid-0.02 15, mid-lock-0.02 19, mid-0.04 6, mid-lock-0.04 and patch-lock 4 (**digan dili dibon ditun**), patch 0. Lists: `results.txt`.

## Checks

### Hold-out (notes §6.6)

Each free option optimised on one half of the variants (25 each), then scored on both halves (`holdout.txt`):

| option | trained on a, scored on a / **on b** | trained on b, scored on b / **on a** | trained on all, scored on a / b |
|---|---|---|---|
| full | 0.223 / **0.241** | 0.247 / **0.240** | 0.236 / 0.247 |
| keep 0.01 | 0.301 / **0.308** | 0.305 / **0.319** | 0.299 / 0.319 |
| keep 0.02 | 0.329 / **0.343** | 0.331 / **0.330** | 0.350 / 0.368 |
| keep 0.04 | 0.538 / **0.556** (stuck at the patch) | 0.379 / **0.405** | 0.424 / 0.413 |
| patch | 0.538 / **0.556** | 0.554 / **0.542** | 0.538 / 0.556 |

**Verdict: the ranking survives.** On the held-out half the order is full < keep 0.01 < keep 0.02 < keep 0.04 ≤ patch both ways. A layer loses at most 0.026 on the half it wasn't trained on (keep 0.04, trained on b), 0.018 for the full rebuild and 0.014 for keep 0.01, while neighbouring options are 0.03–0.2 apart. The ranges aren't too wide to design against; per §6.6 the placement doesn't have to wait for a listening test.

### Sensitivity (notes §6.5)

Each parameter alone at its low and high end in every v2 variant, then the layer re-optimised from itself (100k steps), compared with a control rerun without the override.

- **First pass (annealing, T0 0.002, as `reopt` defaults): uninformative.** The controls themselves drift to different, equally good layers: mid-lock-0.01 moves 32 forms in each of 3 control seeds, mid-lock-0.02 15–20, full 0 or 61. No override moved more than the controls. This is finding 2 again: the layers sit on a wide plateau.
- **Second pass (greedy, `--T0 0`, added):** forms move only when the override makes a strict improvement available. Counted against the control with the same seed (`checks.py vsctl g-NAME`):

| parameter (end) | full | mid-lock-0.01 | mid-lock-0.02 |
|---|---|---|---|
| E_C (overall consonant error) high | 28 | 9 | 10 |
| V_ratio (vowel vs consonant error) low / high | 27 / 12 | 5 / 14 | 1 / 4 |
| coda_loss (final -n lost) low / high | 16 / 8 | 2 / 5 | 2 / 4 |
| L2_mid_m (no-mid-vowel listeners) low | 12 | 7 | 0 |
| coda_add high / low | 10 / 0 | 0 / 5 | 2 / 0 |
| E_C low | 3 | 7 | 1 |
| gem_n_N (n + nasal) low / high | 2 / 2 | 7 / 0 | 0 / 0 |
| voice_mult (voicing) low / high | 4 / 4 | 0 / 5 | 0 / 0 |
| L2_voicing_m, reseg_n_V, glide_hiatus, C_none_after_vowel (either end) | 0 | 0 | 0–1 |

Forms that move are mostly short swap chains: in mid-lock-0.01 the same five words (**WITH FOR VERY GENERIC IT**: nan, fan, ten, dan, bun) rotate under eight different overrides, so they are a near-tie, not a weak spot. Re-optimising under an override gains at most 0.019 (mid-lock-0.01, V_ratio high) and usually under 0.01. **Ranking of what to measure first:** the overall consonant error level (E_C), then the vowel-to-consonant error ratio (V_ratio), then the final -n terms (coda_loss, coda_add). Voicing, which §6.5 expected to lead, moves at most 5 forms.

**Option ranking under each parameter's ends** (`sens-score.txt`, `checks.py rank`): unchanged in 21 of the 22 runs. The one swap is between two near-equal layers, mid-0.01 and mid-lock-0.01, at V_ratio high (0.332 vs 0.336).

Side result: the greedy controls improve the picked layers slightly, since the best-of-12 annealing ends just short of a local optimum. Polished mid-lock-0.01 (9 forms swapped among already-changed words, still 37 changes): robust 0.307 → 0.304 (`runs/sens-g-mid-lock-0.01-control-1.tsv`). Polish the chosen layer with one greedy pass before adopting it.

### Drop test for the new listener groups

Design log: "if the variant changes no form in the short-word rerun, drop it". Each layer re-optimised without src-av and without src-lp, seeds 1–3, compared with the same-seed control:

| layer | without src-av | without src-lp |
|---|---|---|
| mid-lock-0.01 (recommended) | **0 forms** (greedy and annealing) | **0 forms** (greedy and annealing) |
| full | 0 | 0 |
| mid-lock-0.02 | 0 | 0 greedy; annealing 12–22, within its 15–21 seed drift (src-lp moves its score by 0.0005) |

For these layers neither group is among the worst quarter of variants (src-lp barely, for mid-lock-0.02), so the robust score hardly sees them. They do bite on the patch family: without src-av the patch scores 0.544 instead of 0.549 and the locked patch 0.553 instead of 0.560 (`drop-score.txt`), because src-av is their worst variant (it still hears **to~po** at 6%). **Verdict for the rule: both groups change no form of the recommended option, so by the log's rule both can be dropped.** Add-back trigger: choosing the patch or keep 0.04, where src-av is the worst variant, or a listening test that confirms a face-to-face pattern.

## For the author (decisions, one at a time)

**Decision 2: full rebuild, middle, or patch.**

- Problem: the short-word layer has 12 merger pairs and 5 vowel-only words; its robust score is 0.69 (a random layer is 1.0).
- Example: **pi~fi** ("of" / "1") is confused 7% by the best model and 43% by the worst variant, and the two share a position (*totu pi …* / *totu fi*).
- Options:
  - (a) **Full rebuild**: 66 changes, 0.243. Its forms are one arbitrary pick (2.7% agreement between seeds) and it changes all ten most frequent words.
  - (b) **Middle at keep 0.01**: 34–37 changes, 0.31; keeps 8 of the top 10. Recommended locked, so it keeps the name.
  - (c) **Middle at keep 0.02**: 24–25 changes, 0.36–0.38. Cheaper, but it leaves **la~na** 28% (free) or **pi~ti** 29% (locked).
  - (d) **Minimal patch**: 11–12 changes, 0.55–0.56. It leaves **to~po** 29%, **la~na** 28% and the **mesun/mena** clash.
- **Recommendation: (b), name locked (mid-lock-0.01), polished once.** It gets about 80% of the full rebuild's gain (0.69 → 0.31 vs → 0.24) with half the changes. It keeps the name at no cost and the frequent core (**to, yen, wan, pi, gun, mon, tun, wun, la, we**). Every merger and all but one of v2's dangerous pairs go, and **mesun/mena** need no renaming. The hold-out check and every parameter's range keep it in the same place. Its costs:
  - 14 forms move to another word's old form;
  - 26 content words start with a new digit syllable and must be re-formed in the root placement;
  - **ya~yan** (BEFORE/YOUKNOW, final -n) is confusable at 22% in the worst variant (the two never share a position);
  - most of its particular forms are one pick among equally good ones.

  If 37 changes are too many, (c) free (mid-0.02, 25 changes) is the next point, but it gives up the name (**apu yin we**).

**The name.** Keeping **apu pi we** costs nothing in the full rebuild (+0.004, inside seed noise) or at keep 0.01 (−0.003), about 0.01–0.02 in the patch and at keep 0.02, and a lot only at keep 0.04. Recommendation: keep **apu pi we**. Under the recommended option it's free, and **pi**'s danger pairs (**pi~bi**, **pi~fi**) are removed by changing **bi** and **fi** instead.

**ENDEAR** gets **fi** in the recommended layer (today's "1"; "1" becomes **ni**). If a reused digit form is unwelcome for a word of child-directed speech, lock or avoid it and rerun (one minute).

Add-back triggers for parts I added: the 0.01 keep point is in because the curve needed it. Drop it if the author picks 0.02 or 0.04. Re-run the annealing-based sensitivity only if the layers are ever made unique (for example by a tie-break on today's forms). The no-reuse rule (not built) comes in if the author wants freed forms avoided, as `words.py --avoid` does for roots.

## Files

`positions.py` (GF substitution, MODMOD, ENDEAR and operator frames, bigrams), `rebuild.py` (rules, objective, annealer, patch, reopt, score, report), `runs.sh` / `checks.sh` (resumable batches), `checks.py` (summaries: agree, diff, sens, drop, vsctl, rank), `results.txt` (all tables), `forms.tsv`; layers `full.tsv full-lock.tsv mid-{0.01,0.02,0.04}.tsv mid-lock-{0.01,0.02,0.04}.tsv patch.tsv patch-lock.tsv`, hold-out layers `*-ha.tsv *-hb.tsv`; check outputs `holdout.txt sens-score.txt drop-score.txt`, `runs/` (every seed and check run), `logs/`; inputs `substitution.tsv frames.txt adjacency.tsv corpus-counts.tsv modmod.tsv endear.tsv operators-extra.tsv`.

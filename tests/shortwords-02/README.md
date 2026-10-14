# Short-word rebuild, dry run on mishearing model v2 (2026-10-13)

Question: rebuilt from scratch under the corrected rules the author approved on 2026-10-13, what would the whole short-word layer look like? The layer is every grammar word, MODMOD and the digits 0–5. And how does that compare with the smallest patch that removes every merger pair? Nothing outside this folder is changed: no data, reference or lesson file.

## Progress (resume here)

- [x] `positions.py`: GF substitution test (72,302 parses, about 30 min on 14 cores; rerun 2026-10-13 22:40 on the grammar after "Grammar gap 1/2", which added one shared pair, **wi~sun**, and moved scores in the third decimal) → `substitution.tsv`, `frames.txt`; bigrams → `adjacency.tsv`, `corpus-counts.tsv`; `positions.py modmod` → `modmod.tsv`; `positions.py operators` → `operators-extra.tsv`
- [x] `rebuild.py`: rules, robust objective, annealer; `full` (both offensive modes), `patch`, the keep sweep, `report` → `results.txt`, `forms.tsv`; `positions` → `positions.md`
- [x] findings below
- [ ] author: the decisions at the end (offensive rule, which option, the name)

Rerun (from the repo root, inside `direnv exec . …`):
```
python3 tests/shortwords-02/positions.py            # slow; then: positions.py modmod; positions.py operators
python3 tests/shortwords-02/rebuild.py full --steps 400000 --seeds 1 --seed0 23 --out full-hard.tsv
python3 tests/shortwords-02/rebuild.py full --offensive c3 --steps 1500000 --seeds 1 --seed0 10 --out full-c3.tsv
python3 tests/shortwords-02/rebuild.py patch [--no-rule3] [--keep-words OF]
python3 tests/shortwords-02/rebuild.py full --offensive c3 --keep 0.02 --start patch.tsv --steps 400000 --seeds 1 --seed0 1 --out mid-26.tsv   # 0.04 → mid-18.tsv
python3 tests/shortwords-02/rebuild.py report; python3 tests/shortwords-02/rebuild.py positions
```
Annealing runs take 1–5 minutes each. I ran 12–16 seeds per option in parallel and kept the best by objective (logs were in /tmp; the kept seeds are named above).

## Headline

| option | words changed (of 67 existing) | robust score (lower is better) | merger pairs | offensive.py matches | the name |
|---|---|---|---|---|---|
| today (MODMOD at its best free form) | 0 | **0.691** | 13 (+5 vowel-only words) | 35 | apu pi we |
| **full rebuild**, offensive matches kept to a minimum (rule 6 as close as it can be met) | 66 | **0.313** | 0 | 17 | apu lu nan |
| full rebuild, offensive as a tie-breaker (goal C3) | 67 | **0.224** | 0 | 36 | apu wun fon |
| middle: keep today's form unless a change buys ≥ 0.02 (C3) | 26 | 0.330 | 0 | 39 | apu ma yin |
| middle: the same at ≥ 0.04 (C3) | 18 | 0.376 | 0 | 37 | apu fun we |
| **minimal patch** (every merger pair removed, rule 3 met) | 12 | **0.582** | 0 | 35 | apu pan we |
| minimal patch that keeps **pi** | 13 | 0.572 | 0 | 35 | **apu pi we** |
| minimal patch without rule 3 (leaves **in** vowel-only) | 11 | 0.577 | 0 | 34 | apu pan we |

The robust score is the mean of the worst quarter of the 48 model variants (best, 32 Latin-hypercube draws, 14 corners, v1). Each variant's cost (word confusion plus junction misparses) is divided by that variant's median over 400 random layers, so 1.0 is a random layer. MODMOD is new in every option and isn't counted as a change.

Ten most frequent words (to, yen, me, wan, pi, gun, mu, mon, tun, wun; **bu** ties at 5): the full rebuilds change all ten. mid-26 changes four (**yen me pi mu**), mid-18 two (**pi mu**), the patch one (**pi**), and the pi-keeping patch none. **la** (4) changes only in the full rebuilds.

**Main finding: the full rebuild's forms are not determined.** Two annealing runs of the same option agree on only about 5% of the words, which is chance level (16 runs in hard mode, 12 in C3 mode), while their scores sit within 0.28–0.33 and 0.22–0.27. The rules and the objective fix the *properties* of a good layer, not the forms. Any one full-rebuild layer is one pick among many equally good ones. That favours an option that keeps today's forms where they are as good: the keep sweep (C3 mode) traces the curve 12 changes 0.58 → 18 changes 0.38 → 26 changes 0.33 → 30 changes 0.31 → about 45 changes 0.27–0.30 → 67 changes 0.22. **Most of the gain comes from the first 18–26 changes.**

## Method

Each part with its source; **added** marks a choice I made, so check those first.

| part | source |
|---|---|
| inventory: 61 rows of `grammar.tsv`, MODMOD, digits 0–5 (68 words) | author, 2026-10-13 (task; `tests/shortwords-01/README.md` "Inventory") |
| H1 every word has a consonant onset | rule 3 (author) |
| H2 digits are open syllables (CV) | **inherited**: `build.py numbers3` ("one stressed open syllable each"); reference 2.11 is stated for open syllables |
| H3 no two short words share a form | rule 6 forbids same-slot homophones; I also forbid cross-slot ones, as today (**added**: today's layer has none, and 86% of pairs share a position anyway) |
| H4 two words sharing a position never differ only by voicing, f/p, glide vs none, or final -n | rule 2 (author); merger definitions as `tests/shortwords-01/analysis.py` (f~b isn't a merger there or here) |
| positions: named table (`positions.md` §1) ∪ GF substitution (§2) ∪ MODMOD frames | rule 1 (author). Table from reference 4.1, 4.3, 4.4, 5, 6, 7, 10, 13 and `grammar/Apupiwe.gf` categories; digits share the number slot with determiners (rule 4) |
| GF substitution: in 322 parsed frames (all reference examples, UDHR sentences ≤ 16 tokens), every short word replaced by every other; a pair shares a position if the swapped sentence still has a full (non-fragment) parse | **added** method for "real co-occurrence" |
| adjacency: short-word bigrams with no pause between, in the reference examples + UDHR (219 pairs, counts) | rule 5 (author); corpus choice **added** (the stories in `texts/` use old vocabulary, so they're left out) |
| robust objective: CVaR 0.25 over `confusion2.variants()`, cost / random-layer median | rule 5; `research/notes/confusion-data.md` §6.2–6.3 |
| word confusion: Σ W_ab f_a P_v(a heard as b), word-initial syllable matrix | §6.2 ("frequency × stakes × confusion") |
| W_ab = 0.1 + 0.9 × max(pooled substitution share, 0.5 if same row of the table) | **added**: how often a mishearing still parses (the share), floor 0.1 for pairs that never substitute |
| stakes: × 10 for pairs with NOT, × 3 digit–digit | **inherited** from `build.py` (NOT × 10 in the old optimizer; number weights 10/30). No person is recorded as the source. |
| junction risk: for each bigram (A, B), weight = corpus count scaled to the frequency units, × P_v((A,B) heard as (A',B')) over boundary events where A's final -n flips (incl. n + nasal) and A', B' are words | rule 5; `confusion2.Model.boundary` / `p_sequence`, same terms as `misparses` |
| frequencies: `grammar.tsv`; digits 4.0; MODMOD 1.0 | digits as `shortwords-01/analysis.py` (no recorded source); MODMOD **added** (guess) |
| soft: offensive form (`offensive.blocked`), 0.05 each ("hard" mode) or 0.002 (C3 mode) | rule 6 (author) vs goal C3; values **added** |
| soft: shared pair differing by one feature, 0.004 each; features = voicing, place, manner; vowel height, backness; coda | rule 2b (author); the feature system and weight are **added** |
| soft: form = first syllable of a two-syllable operator sharing its position, 0.02 each | rule 6 (author); operator positions from GF (and `operators-extra.tsv` for **wanme inwun wemen buni donon**, which no parsed frame contains) |
| search: simulated annealing (move / swap), legal greedy start; patch = all minimum vertex covers of the merger graph, each re-formed by the annealer, best kept | **added** |
| middle options: penalty per changed existing word (0.02, 0.04), started from the patch | **added** |

Not done (add-back triggers): the §6.6 hold-out check (optimize on half the variants, score on the other half) and the §6.5 one-at-a-time sensitivity; add them before adopting a layer. Junctions with content words (n + vowel-initial root) are left to the joint placement of ~1,500 roots, which re-forms the content words anyway. MODMOD isn't in the GF grammar; its position comes from 5 frames (`modmod.tsv`).

## The position table

Full table: `positions.md` (named positions with rule ids, per-word sharing, operators, bigrams). Summary:

- **15 named positions** (`positions.md` §1): call, linker, relation word, topic, if/when + trailing clause, speech act + politeness, clause operator, noun-phrase start (34 words: pronouns, derivation markers, **en**, determiners alone, digits, phrase operators), before the verb (10), after a content modifier (MODMOD), number slot (16: digits, **la**, determiners, **nen**), after the noun phrase (**pi**, **man**), joining words, number after **kon/mena/fu**, stance.
- **Measured, the grammar lets almost any short word stand where almost any other stands.** In real sentences 1,890 of 2,278 pairs (83%) can replace each other with the sentence still parsing as a full sentence; with the table, 1,956 (86%). That's the isolating design at work: content words take any role, subjects and objects can be left out, and fragments are sentences. A misheard grammar word usually gives another grammatical sentence. Only a few words are fenced off: **kon** and **a** share a position with few others; **ba, fon, yo, nun, un** with about half.
- So rule 2 applies to nearly every pair. It still fits: the merger relation isn't transitive (**pa~ba** and **pa~fa** merge, **ba~fa** don't; **pan~ban** merge, **pa~ban** don't), so a merger-free layer exists even with every pair sharing a position. I checked it feasible at every threshold down to "any shared context".
- Operators: by GF, **mesun** and **mena** share positions with **me** "you" (today's clash). **wanme/inwun/wemen** don't share with **wan/in/we** (`wan wan obu` doesn't parse), so the desk analysis's juncture worry about them isn't a same-position clash.

## Old → new forms

`forms.tsv` has every word in every option; `results.txt` has the same with offensive.py marks. Changed forms are in bold.

| word | freq | old | full | full-c3 | mid-26 | mid-18 | patch | patch-keep-pi |
|---|---|---|---|---|---|---|---|---|
| I | 10 | to | **lin** | **mu** | to | to | to | to |
| AND | 9 | yen | **no** | **ni** | **ten** | yen | yen | yen |
| YOU | 8 | me | **tin** | **wi** | **nun** | me | me | me |
| HE/SHE | 8 | wan | **yun** | **min** | wan | wan | wan | wan |
| OF | 8 | pi | **lu** | **wun** | **ma** | **fun** | **pan** | pi |
| BE | 8 | gun | **gi** | **le** | gun | gun | gun | gun |
| NOT | 7 | mu | **si** | **si** | **se** | **sin** | mu | mu |
| AT | 5 | mon | **so** | **fu** | mon | mon | mon | mon |
| TO | 5 | tun | **nun** | **ge** | tun | tun | tun | tun |
| THAT.comp | 5 | wun | **ni** | **la** | wun | wun | wun | wun |
| IT | 5 | bu | **lon** | **wan** | **lon** | **ti** | bu | bu |
| Q | 4 | min | **son** | **be** | min | min | min | min |
| PLURAL | 4 | la | **tu** | **yu** | la | la | la | la |
| THIS | 4 | tan | **fan** | **nen** | tan | tan | tan | tan |
| WHO.rel | 4 | man | **fin** | **me** | **me** | man | man | man |
| AGENT | 4 | no | **kun** | **gu** | no | no | no | no |
| NAME | 4 | en | **wi** | **ken** | **yan** | **yan** | **yan** | **yan** |
| ALSO | 4 | fe | **ye** | **te** | **nan** | fe | fe | fe |
| D0 | 4 | po | **sa** | **ye** | **ku** | **mu** | po | po |
| D1 | 4 | fi | **yo** | **so** | **ti** | fi | fi | **ku** |
| D2 | 4 | sa | **la** | **tu** | **ye** | sa | sa | sa |
| D3 | 4 | ka | **mi** | **fe** | ka | ka | ka | ka |
| D4 | 4 | da | **fe** | **ta** | da | da | da | da |
| D5 | 4 | te | **ko** | **wo** | **mu** | **su** | te | te |
| WH | 3 | yu | **ken** | **lon** | yu | yu | yu | yu |
| WE.incl | 3 | pen | **wu** | **ya** | **yon** | pen | pen | pen |
| WE.excl | 3 | din | **den** | **sun** | din | din | din | din |
| THAT.dem | 3 | ben | **ta** | **tin** | ben | **lon** | **gen** | **pun** |
| ALL | 3 | we | **nan** | **fon** | **yin** | we | we | we |
| DONE | 3 | sin | **mu** | **ga** | sin | **pon** | sin | sin |
| FROM | 3 | se | **ma** | **lu** | **wen** | se | se | se |
| WITH | 3 | gan | **sun** | **lin** | gan | gan | gan | gan |
| FOR | 3 | li | **gu** | **gon** | li | li | li | li |
| MORE | 3 | ke | **men** | **wen** | ke | ke | ke | **lon** |
| VERY | 3 | bi | **gon** | **mon** | bi | bi | bi | **pan** |
| LIKE | 3 | fu | **sen** | **no** | fu | **fo** | fu | fu |
| GENERIC | 3 | go | **fun** | **do** | go | go | go | go |
| ONLY | 3 | na | **ga** | **ton** | **pon** | na | na | na |
| SELF | 3 | nen | **be** | **ma** | nen | nen | nen | nen |
| POLITE | 3 | nun | **pe** | **po** | **su** | nun | nun | nun |
| TOOL | 3 | du | **ne** | **yin** | du | du | du | du |
| PLACE | 3 | pu | pu | **nun** | **bun** | pu | **ti** | **fin** |
| EVEN | 3 | wi | **bo** | **fan** | wi | wi | wi | wi |
| FOCUS | 3 | o | **kan** | **nan** | **san** | **ku** | **pin** | **ken** |
| YOUKNOW | 3 | a | **wun** | **sa** | **pan** | **fan** | **fin** | **fan** |
| REQUEST | 2 | so | **non** | **bun** | **pin** | **bun** | so | so |
| INTEND | 2 | de | **bi** | **ki** | de | de | **be** | **be** |
| OBVIATIVE | 2 | yi | **do** | **dan** | **fen** | yi | yi | yi |
| SOME | 2 | in | **te** | **ko** | **son** | **son** | **lon** | **yon** |
| ONGOING | 2 | le | **ba** | **yon** | le | le | le | le |
| OR | 2 | lu | **fon** | **dun** | lu | lu | lu | lu |
| BUT | 2 | un | **ka** | **tan** | **so** | **win** | **win** | **do** |
| IF | 2 | don | **we** | **kun** | don | don | don | don |
| WHILE | 2 | nin | **yi** | **fin** | nin | nin | nin | nin |
| RESULT | 2 | ge | **wan** | **den** | **gen** | **yon** | **ku** | ge |
| INSTRUCT | 1.5 | tin | **nu** | **di** | **fi** | **ye** | **fun** | **wu** |
| CONF | 1.5 | kon | **po** | **bo** | kon | kon | kon | kon |
| BEFORE | 1.5 | ya | **win** | **pen** | ya | ya | ya | ya |
| AFTER | 1.5 | wo | **bun** | **sen** | wo | wo | wo | wo |
| BECAUSE | 1.5 | gi | **ya** | **pa** | gi | gi | gi | gi |
| EXCLAIM | 1.5 | ba | **wo** | **ka** | ba | ba | ba | ba |
| ADVISE | 1 | fon | **to** | **ba** | fon | fon | fon | fon |
| UNSPEC | 1 | bo | **wen** | **pun** | bo | bo | **son** | **son** |
| LOGOPHOR | 1 | sun | **le** | **san** | sun | **gen** | sun | sun |
| PART | 1 | kin | **yan** | **kan** | kin | kin | kin | kin |
| NONE | 1 | fa | **won** | **gin** | fa | fa | fa | fa |
| MODMOD | 1 | (son) | len | yan | fin | ten | su | su |
| WARN | 0.5 | yo | **fen** | **gan** | yo | **ben** | yo | yo |

Many new forms are other words' old forms (**mu** "not" → "0" in mid-18). Grammar slots may reuse freed grammar forms (design log 2026-10-10, "the space is finite"); a learner of v1 would feel it, and today no one has learned it yet.

## Pairs fixed

"Fixed" = no longer a merger and under 2% confusion for the worst v2 variant (symmetric). Details per pair, with the best and worst values, are in `results.txt`.

| option | desk analysis's 16 pairs | model v2's 13 most robustly dangerous short pairs | shared pairs ≥ 10% in some variant |
|---|---|---|---|
| today | 0 / 16 | 0 / 13 | 30 |
| full | 14 (left: **do~bo** 6%, **win~wun** 3%) | 12 (left: NONE/EXCLAIM **won~wo** 22%, final -n; the two never share a position) | 15 |
| full-c3 | 15 (left: **dan~fan** 3%) | 13 | 1 |
| mid-26 | 14 (left: **yo~wo**, **fu~bun** 2–3%) | 8 (left: **min~nin** 11%, **fa~ba** 16%, **to~ku**, **fu~bun**, **de~gen** 2–3%) | 15 |
| mid-18 | 12 (left: glide pairs **yi~wi**, **yen~yan**, **win~wun**, **fo~pu**, 2–3%) | 6 (left: **la~na** 28%, **fa~ba** 16%, **bi~fi** 15%, **min~nin** 11%, **fa~sa**, **se~fe** 5%) | 16 |
| patch | 11 (left: the same glide pairs, **yo~wo**, **pen~gen**) | 4 (left: **to~po** 29%, **la~na** 28%, **fa~ba**, **fu~bu**, **bi~fi**, **ke~te**, **min~nin**, **fa~sa**, **se~fe**) | 23 |
| patch-keep-pi | 13 | 5 | 20 |

Every option removes every merger pair. The patches leave model v2's pairs that aren't mergers (**to~po**, **la~na**, **min~nin**), since the patch rule only targets mergers. The full rebuild in hard-offensive mode has a weakness the CVaR averages away: one listener variant (no mid vowels) confuses several new e/i and o/u pairs at 30–39% (**yi~ye**, **son~sun**, **we~wi**). The C3 rebuild has 5 one-feature pairs, against 36 in hard mode and 75 today.

## Operators that would need renaming

- today and all three patches: **mesun** and **mena** (first syllable **me** = "you", which stands where they stand);
- full, full-c3, mid-26: none;
- mid-18: **mesun**, **mena** (it keeps **me**).

## Constraints that can't all be met

1. **No offensive forms (rule 6) can't be met.** `offensive.blocked` matches 80 of the 140 one-syllable forms, 77 of the 130 with an onset, which leaves 53 forms for 68 words. At least 15 words must take a matching form; minimising them reaches 17. Many one-syllable matches are noise: English initialisms (*FA*, *FY*, *FU*), pronunciation spellings (*buh*, *nuh*), a Thai sentence particle (*wa*). Forcing the count down costs score: 0.313 against 0.224 with offensive as a tie-breaker, the role goal C3 gives it ("never overrides a cheaper or clearer form"). The tools treat it as a block, the goal as a tie-breaker; the two need reconciling.
2. **"Differ by more than one feature where the space allows" (rule 2b)** can only be approached. With 86% of pairs sharing a position, about 5–36 one-feature pairs remain (today 75).
3. **Digits and content words (rule 4) clash with today's lexicon.** Content words that would begin with a new digit syllable: full 30, full-c3 37, mid-26 24, mid-18 14 (**yo-, fe-, la-, ti-, mu-, su-** …; `results.txt`); the patch none (its 2 hits, **polisu** and **kamela**, are loans, which are exempt); the pi-keeping patch 5 (**ku-**: **kudu kusa kuwi kubo kuwun**, from 1 → **ku**). Those roots would need new forms; the planned joint placement of all roots does that anyway.
4. **Rule 1 as literally stated is weak:** "can stand in the same slot" holds for 86% of pairs. The hard rule is applied to all of them (it fits); the cost is graded by how often each pair substitutes.

## For the author (decisions, one at a time)

1. **Offensive filter for one-syllable words.** Problem: rule 6 can't be met (above), and it costs a third of the gain. Options: (a) C3 tie-breaker, as the goal says; (b) keep it near-hard (17 matches); (c) hand-prune the one-syllable matches (initialisms, spellings) and re-run. Recommendation: (a), or (c) if some matches are real slurs worth blocking.
2. **Full rebuild, middle or patch.** The full rebuild's forms are arbitrary (5% agreement between runs), so adopting one buys a score, not particular forms. Recommendation: a middle option. mid-26 (26 changes, 0.33) keeps **to, wan, gun, la, mon, tun, wun** and fixes 14 of 16 desk pairs; mid-18 keeps more but leaves **la~na**, **fa~ba**, **bi~fi**. The dial (penalty per change) is a single number to set; the patch (0.58) leaves most of v2's dangerous pairs.
3. **The name.** **pi** changes in every option except the 13-word patch that changes **bi** and **fi** (and **ke**) instead. The roadmap already says the name is settled last; the pi-keeping patch shows that keeping it costs one extra word.

Add-back triggers for the parts I added: the 0.1 floor weight if never-substituting pairs turn out to be misheard in a listening test; the one-feature system if the listening test shows other near pairs; the hold-out check before any layer is adopted.

## Files

`positions.py` (GF substitution, MODMOD and operator frames, bigrams), `rebuild.py` (rules, objective, annealer, patch, report), `positions.md` (position table), `results.txt` (all tables), `forms.tsv`, the layers `full-hard.tsv full-c3.tsv mid-26.tsv mid-18.tsv patch.tsv patch-keep-pi.tsv patch-no-rule3.tsv`, the inputs `substitution.tsv adjacency.tsv corpus-counts.tsv frames.txt modmod.tsv operators-extra.tsv`.

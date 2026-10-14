# Mishearing model v2: implementation and comparison with v1 (2026-10-13)

Question: what does model v2 (adopted by the author 2026-10-13, `research/notes/confusion-data.md` §5–7) change compared with v1 (`tools/confusion.py`), before the optimizers are switched over? No word and no data file is changed here.

## Progress (resume here)

- [x] `tools/confusion2.py`: model, best parameters, the §6 variants (48), junction functions; self-check passes (`python3 tools/confusion2.py`)
- [x] `check.py` → `results.txt`: (a) published matrices, (b) today's words, (c) the 16 merger pairs, (d) robustness, (e) junctions
- [x] findings below
- [ ] author reads the comparison; then switch `build.py` / `words.py` / the placement to `confusion2` (a later step)

Run: `direnv exec . python3 tests/confusion-v2/check.py > tests/confusion-v2/results.txt` (about 4 s).

## Method

`tools/confusion2.py` reads every rate and range from `research/notes/confusion-data/model-v2-params.tsv` and the consonant patterns from the `proj-*.tsv` matrices. The interface:

- `syllable_matrix(p, context)`: 140 × 140, same indexing as `build.Inventory` over 13 consonants. `context` = `pause`, a vowel (word-initial after a word ending in that vowel), `n` (after an n-final word), `internal` (non-initial syllable) or `initial` (word-initial, neighbour unknown: a weighted mix).
- `best_params()`, `v1_params()`, `variants()` (the §6 set: best, 32 Latin-hypercube draws, 5 single-source patterns, voicing ×0.1 and ×3, the worst listener of each of the 7 groups, v1), `worst_listener(group)`, `no_groups()`.
- `Model(p)`: `p_word`, `word_matrix`; junctions `boundary(v1, c1, o2)` (joint coda + onset at a word boundary, with n + vowel resegmentation and n + nasal), `p_sequence(sent, heard)` for word sequences, `misparses(w1, w2, vocab)` for the juncture check.

Parts and sources, with the choices I made while implementing marked. They're my own additions, so check them first:

| part | source |
|---|---|
| consonant substitutions: each source level-matched to E_C (as `project.py`), "heard no consonant" returned to the diagonal; mix4 = mean of 4 | notes §1.8, §5.1; reproduces the TSV's pair rates (voicing 2.7%, m-n 7.8%, l-n 4.5%, f-b 6.6%) |
| `mn55+mix`: MN55 for its 10 consonants, mix4 for l w j | **added**: the TSV names the category, not how to fill MN55's missing l w j |
| onset presence by junction | §5.3, TSV rates |
| none → C after a vowel or n (non-glides) uses `none_C_pause`, spread evenly over the 13 consonants | **added**: the TSV has the rate only after a pause |
| `initial` context = pause 0.20, after n 0.20, after each vowel 0.12 | **added**: n-final share from `grammar.tsv` + `lexicon.tsv` (0.25, frequency-weighted); pause share a guess |
| E_C scales the noise rates (pattern, C→none, none→C, coda, aspiration confusion); junction ambiguities and group levels m don't scale | **added** (reading of "rates at E_C = 0.20"; E_C stays 0.20 in every variant, as the TSV says) |
| listener groups overlaid as independent features: a share π of listeners confuse the pair at m (never lowering a cell) | §5.6; independence is **added** |
| aspiration: for the voicing group, word-initial rate = asp_share × asp_conf + (1 − asp_share) × L2_voicing_m; inside a word L2_voicing_m | design log 2026-10-13; `asp_conf` 0.35% (0.2–1%) from Yu & Do's Mandarin aspiration data (§1.8); `asp_share` 0.8 (0.5–0.95) is a **guess** |
| worst voicing listener also has asp_share at its low end | **added** (the worst case includes talkers who don't aspirate) |
| LHS: C_pattern spread evenly over its 6 categories; vowel shares Dirichlet, concentration 20 | TSV sampling rules; the concentration is **added** |
| v1 inside the variant set: `build.Inventory`'s construction from `confusion.py` | §6 ("continuity check") |

Not modelled (add-back triggers as in notes §6): syllable-count errors; vowel context on consonants; a junction inside a word (*munno*); misparses that move a word boundary (digit + word heard as one word stays with `tools/juncture.py`).

## Findings

**(a) Published data.** v2 reproduces the published matrices much better than v1, even on held-out data: rank correlation of the 78 consonant-pair confusions with each source, v1 0.37–0.57, v2 leaving that source out of the mix 0.47–0.80 (in-sample 0.58–0.88 on the four mixed sources). Mandarin is the exception on absolute error: its pattern (white noise: f-b, place) is unlike the other three, and no average matches it. v1's top pairs are MN55's d-g 21%, p-k/t-k/p-t 14%; v2's are p-t 10%, m-n 8%, t-k 7%, f-b 7%, d-g 6%. v1 put onset loss on w/j/l/f (3–5%) and p t k at 0.5%. After a pause the data say the reverse (p 17%, t 12.5%, k 12% for native listeners); v2 has p 12%, t/k 8.5% after a pause and 1.5% after a vowel. v2's vowel shares are closer than v1's to all four Cutler tables.

**(b) More dangerous under v2.** Pairs v1 rated near zero:
- **voicing**: short words **pi~bi** (of/very), **bu~pu** (it/place), **bo~po** (some/0), **pen~ben** (we/that), **ke~ge** (more/result), v1 ranks 168–2164 → v2 ranks 12–25; content **kudu~gudu** (big/liver), **duko~tuko** (turn/start), v1 rank ~100,000 → v2 rank 4–5.
- **l-n**: **la~na** (plural/only) 98 → 11.
- **voiced–voiceless across place**, which v1 had at ~0: **b-k**, **p-g**, **t-g** in content words (*beya~keya*, *aban~akan*, *nebe~neke*, *yikan~yiban*, *gake~gabe*, *penso~genso*, *soti~sogi*). v1 had these at rank ~100,000; in v2 they fill ranks 9–29. These words were placed under v1, so they sit exactly where v1 saw no risk.
- **f-b**: **fa~ba** (none/exclaim), **fu~bu** (like/it), **bi~fi** (very/1), ranks 50–56 → 6–8.

**(b) Overrated by v1.** v1's guessed approximant rates (l-w, l-j, w-j 6%) and onset loss on glides: **li~wi**, **yi~wi**, **yu~lu**, **yi~li**, **la~ya**, **we~le** (v1 top 15 → v2 rank 75–90); content *wulon~yulo*, *lula~yulo*, *lowu~yawu*, *lewe~leyi*, *wase~afe*, *omen~oma*. Also MN55's f-s and f-k (*fa~ka*, *ke~fe*, *se~fe*, *fon~kon*) and d-g (*de~ge* is v1's #1 at 33%, v2 #10 at 5.7%). Rank agreement v1 vs v2: 0.76 (short words), 0.67 (content). Only 5 of v2's top 20 content pairs are in v1's top 20.

**(c) The 16 merger pairs** (symmetric confusion, %, word-initial):

| pair | v1 | v2 | no groups | voicing listener, typical | worst listener of the pair's group | after i / u |
|---|---|---|---|---|---|---|
| tin~din, de~te | 0.0 | 1.4–1.5 | 1.2–1.3 | 2.0–2.2 | 18–19 (voicing) | – |
| ke~ge | 0.0 | 2.9 | 2.9 | 2.9 | 19 (voicing) | – |
| bo~po, pen~ben, pi~bi, bu~pu | 0.4 | 4.0–4.4 | 3.2–3.4 | 3.2–3.4 | 18–19 (voicing), 36–38 (no p) | – |
| pi~fi, fu~pu | 6.7 | 7.2 | 4.3 | – | 43 (no f) | – |
| yo~o, ya~a, yen~en | 2.8 | 2.6–2.9 | – | – | – | 8.7–9.5 after i/e; 0.3 after a pause |
| wo~o, un~wun | 2.8 | 2.6–2.8 | – | – | – | 8.7–9.3 after u/o |
| yo~wo, yi~wi | 5.1–5.3 | 1.1 | – | – | – | – |

The aspiration decision works as intended in the model: a typical aspiration-language listener (reference talkers aspirate 80% of the time) confuses tin~din about 2%, close to everyone else, so the voicing group adds almost nothing word-initially. The worst case (m = 0.40 and half the talkers not aspirating) is 18–19%. The no-p (Arabic-type) and no-f listeners are the worst listeners for the p/b/f pairs (36–43%). The glide pairs are context-dependent: about 9% after a matching vowel, under 1% elsewhere. yo~wo and yi~wi, which v1 rated as the worst glide pairs, are 1% in v2.

**(d) Robustness.** Across the 47 v2 variants the short-word ranking correlates with the best estimate at 0.60 at the lowest (median 0.88), the content ranking at 0.44 (median 0.78); best's top 10 short pairs keep a median of 6 in a variant's top 10, best's top 20 content pairs 15. The consonant pattern moves the ranking most: the Mandarin white-noise pattern and MN55 keep only 42–65% of the best estimate's top pairs. Then come V_ratio, voice_mult and L2_voicing_m. The guessed junction rates matter only to short words. 46 short-word pairs and 105 content pairs enter some variant's top 10/20.

Most robustly dangerous (worst rank over all v2 variants, including the worst listeners):
- short words: **ke~te** (more/5, never below rank 26), **tin~kin** (instruct/part), **min~nin** (Q/while), **pi~fi** (of/1), **fu~pu** (like/place), **la~na** (plural/only), **fa~sa** (none/2), **se~fe** (from/also), **to~po** (I/0), **fa~ba**, **fu~bu**, **bi~fi**, **de~ge**;
- content: **uwan~yuwan** (star/yuan), **soto~foto** (north/photo), **gulo~yulo** (wind/euro), **kudu~gudu** (big/liver), **kanko~anko**, **kegu~egu**, **duko~tuko**, **imu~gimu**, **kiyo~kilo**.

Only under one variant: mid-vowel pairs (*neke~niki*, *kiti~kete*) for listeners without mid vowels; l pairs (*dili~lini*, *dandi~lanli*) for listeners without l; voicing pairs (*tin~din*, *de~te*, *konke~gonge*) for the worst voicing listener.

**(e) Junctions.** No n + vowel or n + nasal misparse exists among today's words: the existing juncture rules (no grammar-word pair differing only by -n) already prevent them. All 1,980 boundary misparses at ≥ 2% are glide/hiatus ones, about 8% each, e.g. *se a* ~ *se ya* (from + you-know / from + before), *o o* ~ *o wo*, *so o* ~ *so wo*. They come from the vowel-initial grammar words **a, o, en, in, un**.

## For the author

1. **Aspiration share** (`asp_share`, 0.8, a guess) and **L2_voicing_m** now mean "confusion when p t k are *not* aspirated". With aspiration made explicit, its adopted range (0.02–0.40) may be too low for unaspirated tokens, where an aspiration-language listener hears both as one category. The model doesn't change this; it's a question for the listening test.
2. The parts marked **added** in the method table need a yes or no, mainly the `initial` junction mix (pause share guessed) and treating listener groups as independent.
3. Next step (roadmap): switch `build.py` / `words.py` / the placement to `confusion2` with the CVaR objective of §6.3. Expected effect: voicing, b-k and l-n minimal pairs get pushed apart; approximant pairs get freed.

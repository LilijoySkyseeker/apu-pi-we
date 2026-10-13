# A5: Complexity and over-building

Area: goal C1 costs — learning effort (B7) vs everyday effort (B8); guarantees B3, B10; non-goal N4 ("define everything").

## Counts

| Item | Count | Source |
|---|---|---|
| Native root words | 483 | lexicon.tsv (547 rows − 23 loan − 21 number − 20 unit); matches learn.md's own figure |
| Borrowed/loan words | 23 | lexicon.tsv field=loan |
| Core number words (digits, place, group, point/minus/power) | 27 | numbers.tsv |
| Senary (base-6) unit roots | 20 | lexicon.tsv field=unit |
| Senary (base-6) numeral words | 9 | numbers.tsv kind=senary (nobi, miko, niyu, yiyo, gife, yuli, kufe, bafo, genwi) |
| One-syllable grammar words | 61 | grammar.tsv |
| Two-syllable "operator" grammar words | 15 | language.md §13 (genso, wanme, inwun, wemen, konsin, buntu, tason, nedin, mesun, manni, buni, donon, lanno, anko, nuwen) |
| Established fixed compounds | 52 | compounds.tsv |
| **Total distinct forms to memorise individually** | **≈ 690** | 483+23+61+15+52+27+9, i.e. everything above with nothing left to productive rule |
| Distinct bulleted/numbered grammatical statements, §1–12 of language.md (a floor count of "rules"; many bullets bundle several sub-rules) | **159** (7 numbered principles + 152 bulleted statements) | counted directly from language.md |
| Optional/special pragmatic systems present (of the 10 named in the task prompt as things to check for) | **10 of 10** present | speech acts, confidence/evidentiality, source marking, stance, politeness, inclusive/exclusive, logophoric/obviative, titles, aspect, doubling — see §2 below |

Phoneme inventory is small and genuinely simple: 5 vowels, 13 consonants, syllable shape (C)V(n), no tone, no morphology ("words never change form") — this part clearly earns its B2/B7/B10 keep and is not re-litigated below.

## Severity totals (13 findings below)

- High: 2
- Medium: 7
- Low: 4

## Findings

**F1. Invented base-6 (senary) measurement/numeral system.** [High]
Evidence: 20 `unit.*` roots (lexicon.tsv) + 9 senary numeral words (numbers.tsv: nobi, miko, niyu…), a separate reading rule (`senali` + digits, §9.2), referenced as "the senary system" in §8.3/§9.3, alongside ordinary measurement already fully served by borrowed SI names (§9.3: "measurements use borrowed international unit names"). Problem: this duplicates a function the language already has, adds ~29 words plus a whole parallel numeral grammar, and does it with a base no major language uses as primary — a direct conflict with B5 ("built from what many languages share"), not just an N4 violation. No B-criterion requires inventing a new counting base. Direction: delete; keep SI borrowing as the one measurement path.

**F2. Confidence marked as a mandatory 6-point sixths scale.** [High]
Evidence: §6.1 — `kon` + po/fi/sa/ka/da/te/ufo/bo (7 words + "don't know"), plus half-steps (`kon te mimi te`) and an overlapping exact-percentage path (`pasentu`). It sits in clause-operator slot 5, a core sentence-template position, and interacts with counterfactuals (`don kon po`, §12) and "might/must" (§6.1). Problem: ordinary speech needs a handful of certainty bands; forcing a non-decimal, discrete 6-way scale onto every hedge is precision machinery closer to a forecaster's toolkit than everyday talk, and it forces speakers to fake precision they don't have. B3 only requires that a precise way *exist* — not that the default, frequently-used form be this fine-grained. Direction: simplify the default to 3–4 coarse words (certain / likely / unsure / unlikely); keep number+`pasentu` for when real precision is wanted (already exists, satisfies B3 and N4 together).

**F3. Doubling (Principle 5) is not one rule but six memorised idioms.** [Medium]
Evidence: §1.5 states doubling "widens or strengthens any word," then lists `mu mu` (emphatic, explicitly *not* double-negation), `nun nun` (extra deference — fits), `yo yo` (emergency — a category jump, not "very warned"), `genso genso` ("the whole turn is not literal" — a scope change, not intensity), `nen nen` ("each other" — an unrelated meaning), `feko feko` ("exactly so" — fits). Problem: 4 of 6 listed cases don't follow the stated meaning at all, so the "rule" is really a closed list of idioms wearing a rule's clothing — exactly the "little to memorise" guarantee (B7) failing on its own flagship predictability device. Direction: either relabel as a short closed list of idioms (stop calling it productive), or prune `nen nen`/`genso genso`/`yo yo` and use ordinary words/phrases for "each other," "whole turn ironic," "emergency."

**F4. Three-way obviative/logophoric 3rd-person tracking (`wan`/`yi`/`sun`).** [Medium]
Evidence: §10.3, grammar.tsv (OBVIATIVE, LOGOPHOR classes), lesson 5. `wan` = current discourse topic, `yi` = "the other one, not the topic," `sun` = logophoric in reported speech — a genuine discourse-obviation system, a feature only a minority of the world's languages (e.g. Algonquian) grammaticalize, bolted onto what's otherwise a plain SVO pronoun set. Problem: it requires continuous real-time bookkeeping of "who is currently the topic" by both speaker and listener, paid on every sentence with two third parties — a frequent, not occasional, cost — for a precision gain that B3 already guarantees is achievable another way ("name it again when unclear," §10.3 itself says so). This trades B8 against a guarantee that doesn't need this specific mechanism. Direction: demote `yi`/`sun` from the core pronoun table to "use when needed," and rely on naming + context as the default, per the language's own escape clause.

**F5. `gun` ("is") compresses six position-gated licensing patterns into one word.** [Medium]
Evidence: §4.7 lists state, noun-predicate, place, event-undergoer/passive-like, clause-initial-only existential, and dropped-subject-"to be"-after-{man, verb, li, yen/lu/un} — six distinct rules, gated purely by syntactic position, two of which (bare existential, bare-subject "to be") are patches whose only job is to resolve the ambiguity the overloading itself creates. Problem: looks like one simple copula, is actually six memorised, position-dependent micro-rules — the kind of "arbitrary, doesn't follow from meaning" case the brief asks to flag. Direction: keep `gun`, but state the two patch-cases as one consistent rule ("bare `gun`, nothing preceding it in its clause, is existential/generic") instead of scattering position-specific carve-outs across the section.

**F6. `pi`'s narrow-scope default forces a "repeat the head" workaround.** [Medium]
Evidence: §5.2 — "a list joined by yen or lu is outside [pi's scope]... To cover every item, repeat the head: `enpa pi pume yen enpa pi lite pi nosen`." Problem: an arbitrary scope default creates systematic ambiguity for an everyday construction (naming two things of X), patched by making the speaker repeat the head noun rather than by fixing the grammar — a rule that exists only to patch a side effect of another rule (brief item 2/3), and it costs real words every time it bites (B8). Direction: merge — give `pi` list scope by default (the more useful, more common reading) and require a marked form for the narrow reading instead.

**F7. Relative/trailing-clause attachment flips with sentence position.** [Medium]
Evidence: §4.4, with two mirror-image worked examples: a clause at the *start* of a sentence attaches to the main clause; the same clause at the *end* attaches to the innermost clause unless a pause closes it first — and the same split is repeated for predicates joined by `yen`/`lu`/`un`. Problem: two different defaults depending only on linear position, each its own memorised case with its own "unless a pause" escape hatch, not derivable from the stated "heads first" or "heavy goes last" principles — and it is frequent (any sentence combining a time/reason clause with a relative clause), so the cost isn't marginal. Direction: pick one default (innermost-clause attachment, pause to override) instead of a position-dependent split.

**F8. Evidential marking (`wanme`/`inwun`/`wemen`) duplicates lexical verbs and is itself rare.** [Medium]
Evidence: §6.1; all three are frequency tier 1 (rarest) in lexicon.tsv. Problem: a dedicated optional grammatical slot for information-source is grammaticalized in only about a quarter of the world's languages (Aikhenvald 2004), so it is far from something "many languages share" (B5); the language's own frequency tier confirms it's rarely needed; and `nagu`/`iko`/`oyi` already say "I saw/was told/figured" without any grammar. This is precision machinery nobody needs often — exactly the case the brief and N4 ask to flag for "leave to real use." Direction: delete from the clause-operator grammar; it survives fine as ordinary verbs for anyone who wants it.

**F9. The 14-slot sentence template front-loads rare-case machinery onto every learner.** [Medium]
Evidence: §4.1's table, restated in learn.md lesson 14, with further internal sub-orderings (openers' own order, pre-verb operator order, two-stance-word order). learn.md itself says "you'll rarely use every part." Problem: Principle 1 promises "the common case costs nothing," but the *learning* cost is paid up front for the full 14-slot, multiply-nested grammar regardless of how rarely most slots combine — a mismatch between how the systems are taught/specified (as one monolithic template) and how often they're used. Direction: keep the full template as the reference, but split out a 6–7 slot "common case" grammar (subject–verb–object plus `mu`/aspect/one relation phrase) as the thing actually taught first; learn.md already does this reasonably — the risk is language.md presenting it as one undifferentiated table.

**F10. Politeness-emergency carve-out.** [Low]
Evidence: §10.2, "In an emergency (`yo yo`), no `nun` is expected." Problem: a patch rule whose only job is to stop the politeness system and the warning speech-act from colliding. Low cost since it only removes an obligation, and politeness marking itself is well-motivated (L2/C2: carrying existing cultures' near-universal politeness conventions). Direction: leave; it earns its place, only the exception is overhead and it's cheap overhead.

**F11. Determiner-attachment default + `tun` workaround.** [Low]
Evidence: §5.2 — a bare determiner right after a noun/pronoun binds to it, so giving someone a bare determiner as the *recipient* needs `tun` to escape the default. Same shape as F6 but rarer (bare-determiner recipients are uncommon). Direction: leave; low frequency, low cost.

**F12. Stance-word-stacking order exception.** [Low]
Evidence: §7.2, "If two stance words occur, `min` comes last." A single memorised exception for a rare case (two stance particles in one sentence). Direction: leave.

**F13. Two-syllable grammar words are a double exception.** [Low]
Evidence: §2/§13 — the otherwise clean rule "grammar words are unstressed monosyllables" gets a 15-word carve-out that is simultaneously stressed *and* bisyllabic, just to fit words that don't scan as one syllable. Problem: every one of these 15 is an exception to two systems at once (sound-class-by-word-type, and the grammar-word class). It's a small, closed, listed set, so the cost is bounded. Direction: leave as a documented closed class (which is already how §13 presents it); not worth forcing to one syllable.

## What's missing that the goal requires (brief)

The language never works through how clause operators compose with negation scope beyond slot order: slot 5 (`kon`, source) precedes slot 7 (`mu`), but no example shows whether `kon ka` ... `mu` X means "even odds that not-X" versus "not confident that X" — a very ordinary thing to want to say (B3 requires a precise way to exist for *anything*), and the interaction is left to be inferred from template position rather than stated. This is a specification gap, not a missing word; worth one worked example in §6 or §12.

## Comparison with other languages (rough figures)

- **Toki Pona**: 120 root words in the original 2014 book, 137 in the 2021 *Toki Pona Dictionary*'s "essential" list — the most extreme minimalist comparator, achieved by deliberately giving up precision. [Toki Pona Dictionary / Glossika summary]
- **Esperanto**: marketed since 1905 on "the sixteen rules" (*Fundamento de Esperanto*), though linguists note the real grammar in use is substantially larger than 16 rules; core vocabulary is commonly cited in the 500–900 root-morpheme range, multiplied by productive affixation. [Fundamento de Esperanto / "Sixteen Rules" discussion, lojban.org and UCSD summary]
- **English, for comparison on vocabulary load (not grammar)**: the General Service List's ~2,000 word families cover roughly 80–95% of ordinary spoken/written text, depending on register — the standard benchmark for "how much vocabulary is enough." [GSL/NGSL summaries]
- **Grammaticalized evidentiality** (relevant to F8): obligatory in roughly a quarter of the world's languages, i.e. a minority feature, not something "many languages share." [Aikhenvald 2004, as summarized in secondary sources]

Against these: this language's **483 native roots** sit close to Esperanto's root count, which is reasonable given both rely on derivation rather than raw vocabulary. But its **≈159-statement grammar** (floor count, §1–12 of language.md) is an order of magnitude past Esperanto's "16 rules" banner, even granting that Esperanto's real-world grammar is bigger than its own marketing claim. For a design whose B7 explicitly promises "little to memorise," landing an order of magnitude past the most famous historical claim to exactly that promise is worth naming plainly, independent of whether any individual rule above is itself well-motivated.

## Proposed measurement for learning effort (B7) and everyday effort (B8), for a separate evaluation document

**Learning effort (B7):**
1. *Time-to-competence trial*: have naive adult volunteers study from learn.md for the guide's own stated budget (15–20 min/day × 4 weeks ≈ 8–10 hours), then test them, without notes, against a fixed task battery (e.g. translate N held-out sentences each way, hold a 5-minute scripted conversation). Pass mark: proposed as ≥80% of volunteers reach a stated accuracy threshold (e.g. 80% correct) within the stated time budget — if the guide's own claimed study time doesn't get most learners there, either the grammar or the guide needs to shrink.
2. *Rule-count and patch-rate audit* (as done in this report): count distinct bulleted/numbered grammatical statements, and separately count how many exist only to resolve ambiguity created by another rule (patch rules — F5–F7, F10–F12 above). Pass mark: proposed patch-rule share < 10% of total rules; total rule count tracked release-to-release and expected to fall, not grow, as the language matures (each new rule should delete at least as much as it adds).
3. *Comparator ratio*: total memorisable items (this report's ≈690) and rule-count (≈159) tracked against the Esperanto/Toki Pona figures above as an explicit outer bound, not a target — pass mark proposed as "no more than 2× the leanest comparator judged to meet the same guarantees, unless each excess item is tied to a named B-criterion" (this report ties each finding to one).

**Everyday effort (B8):**
1. *Cost-per-meaning on a fixed corpus*: use example-udhr.md (already a full parallel text) and measure syllables/words per clause against the English original and, if available, against the same UDHR articles in Esperanto/Toki Pona/a natural-language control. Pass mark: proposed average syllables-per-clause within ~1.3× of natural-language baselines for the same meaning.
2. *Production friction*: record fluent speakers producing a fixed task battery aloud; count hesitations, self-corrections and time-on-task. Pass mark: no more hesitation/self-correction than a matched natural-language control group doing the same task.
3. *Real-use frequency of optional systems*: from the UDHR text (and any future corpus), measure how often each optional system (confidence scale, evidentials, doubling, senary) actually appears. Pass mark proposed: any optional system appearing in under, say, 2% of a representative corpus is evidence it fails "how often would a speaker use it" (task item 2) and is a deletion candidate per N4, regardless of how defensible it looks on paper.

## Top 8 findings (two lines each)

1. **Senary measurement/numeral system** [High] — a whole invented base-6 system (29 words) duplicates the already-sufficient borrowed-SI path and contradicts B5 (no major language uses base-6). Delete.
2. **Confidence as a mandatory 6-point sixths scale** [High] — grammaticalizes false precision in a core, frequently-used slot where 3–4 coarse words would do; exact probability already exists via numbers+`pasentu`. Simplify.
3. **Doubling is 6 idioms, not 1 rule** [Medium] — 4 of 6 listed doublings contradict the stated "widens or strengthens" meaning (`nen nen`="each other", `genso genso`=scope change, `yo yo`=category jump). Relabel as idioms or prune.
4. **Three-way obviative/logophoric pronouns (`wan`/`yi`/`sun`)** [Medium] — a rare, cross-linguistically minority discourse-tracking system paid on every sentence with two third parties, when naming already covers the same need. Demote to optional use.
5. **`gun` packs six position-gated rules into "one simple word"** [Medium] — state/noun/place/passive/existential/dropped-subject uses are each separately memorised and position-sensitive; two are pure patches. Consolidate the patches into one rule.
6. **Relative/trailing-clause attachment flips with sentence position** [Medium] — same clause type attaches differently depending only on whether it's at the start or end of the sentence, each with its own "unless a pause" escape hatch. Pick one default.
7. **Evidential marking duplicates lexical verbs and is itself rare** [Medium] — `wanme`/`inwun`/`wemen` are tier-1 (rarest) words marking a feature only ~25% of languages grammaticalize at all; ordinary verbs already say the same thing. Delete from grammar.
8. **14-slot sentence template front-loads rare-case machinery** [Medium] — the full template (plus nested sub-orderings) is taught/specified as one block even though "you'll rarely use every part"; the common case should cost what it actually costs. Split common-case grammar from the full reference.

Full counts, all 13 findings, the missing-specification gap, comparison figures and measurement proposals are in the sections above.

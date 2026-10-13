Screen Apupiwe's whole dictionary against its word-decision ladders, and produce the material the author will decide from. Don't change any word; propose.

Repo `/home/agent/work/repos/universal-language/`. Read first: `docs/goal.md`, `docs/vocabulary-method.md` (section 0 is the two ladders; sections 1–5 explain the method), `docs/language.md` §11 (names, loans, new words). Words: `data/lexicon.tsv` (gloss, field, tier, form; field `loan` marks loans), `data/compounds.tsv`, `data/antonyms.tsv`. Tools: `tools/names.py` adapts a pronunciation (broad IPA) to the language's sounds; run Python through `direnv exec /home/agent/work/repos/universal-language python3 …` from `tools/`. Web search is allowed and needed. Ignore `data/senary.tsv`. Don't edit anything in the repo except creating files under `tests/lexicon-ladder-01/`; don't commit.

Part 1, the loans (highest priority; do this first and save it before Part 2):
For each loan in lexicon.tsv (field `loan`), and any other word that looks borrowed:
- Ladder 2 rung 1: is it an international standard term (SI unit, ISO, chemical element, scientific name)? If so, name the standard and its form.
- Rung 2, the panel test: give the everyday word for the meaning in each of these 20 languages (no English: it is the bias being tested): Mandarin, Japanese, Korean, Vietnamese, Thai, Indonesian, Tagalog, Hindi, Bengali, Tamil, Persian, Arabic, Turkish, Russian, Spanish, French, Swahili, Hausa, Yoruba, Quechua. Say for each whether it shares the loan's international form (a recognisably cognate form, not just a translation). Pass = shared in at least 12 of 20, across at least 4 of these regions: East Asia, Southeast Asia, South Asia, West Asia/North Africa, Europe, Sub-Saharan Africa, the Americas. Source each word (dictionary or Wiktionary link) or mark it from memory.
- If it passes: the panel's median pronunciation (broad IPA) and the form `names.py` gives for it, next to today's form.
- If it fails: rung 3, a proposal built from existing words (only words in lexicon.tsv/compounds.tsv), short and clear; or rung 4, "needs a new root", with its frequency tier.
Write `tests/lexicon-ladder-01/loans.md`: a summary table (loan, today's form, standard?, panel count and regions, verdict, proposed form) and the full panel data below it.

Part 2, boundary candidates (Ladder 1):
Go through every root and compound. Flag only real candidates, with evidence:
- rung 1: the meaning should follow an international standard's boundaries but doesn't;
- rung 2: the word or its boundary rests on a belief known to be wrong (goal C4), or bakes a current theory into a basic word;
- rung 3: one word lumps two meanings that are both frequent, come up in the same contexts, and are either action-relevant to tell apart or often not told apart by context. Known candidates: dunan "month; moon", apu "word; language" (also the language's name), lite pi nosen "religion" (fairness: "way of God"). Also check every gloss with ";" or "," that joins two senses;
- the reverse: two roots where the ladder says one (rung 4 data says ≥50% lumped and nothing above applies).
For each candidate: the word, the rung, the evidence (sources), what splitting/merging/changing would cost, and the options.
Write `tests/lexicon-ladder-01/boundaries.md`: candidates ranked by how strongly the ladder points to a change, then a short list of borderline cases you rejected and why.

Save progress as you go (usage limits may interrupt you): keep `tests/lexicon-ladder-01/PROGRESS.md` with what's done and what's left, and continue from it if it exists. Final report: the loan verdicts (pass/fail counts, the failures with proposals) and the top 10 boundary candidates.

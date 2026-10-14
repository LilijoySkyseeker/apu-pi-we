# Unknown unknowns: a wide pass by a different model (2026-10-14)

Task: `unknown-unknowns-prompt.md`. Find considerations, risks and unusual ideas the project hasn't raised. Written by Claude Fable 5.1, a different model from the one that designed the language (same company, so overlapping priors; see §4). Working note, terse.

## Progress

- [x] Read goal, reference, roadmap, design log (all), rationale, vocabulary method, drift, the three survey notes, the judge's verdict.
- [x] Searched docs, research notes and reviews for the fields the prompt names (sign, deaf, blind, whisper, song, lip-reading, child speech, aphasia, heritage speakers, hearing loss, keyboards, spelling aloud, articulation, humour, swearing…) so items already covered are dropped or cited.
- [x] Four small measurements on today's word lists (child-merger collisions among grammar words, random-form neighbour rate, typo neighbours, labial–coronal order). Numbers are in the items; commands are not kept (one-off, reproducible from the description).
- [x] Items written and ranked (§1), long shots (§2), process risks (§3), things checked and found covered (§4).
- Done. Nothing left open in this note; each item names its own cheap check.

Ratings: **plausibility** that the item matters for the goal (low / medium / high) × **effect** if it does (small / medium / large). Ranked by the product, judgement not arithmetic. "Covered" cites the file where the project already has it; items fully covered were dropped.

---

## 1. Ranked items

### 1. The deferred listening test is blocked by a tooling choice, not by people

- **What.** Two things the roadmap treats as unavailable are purchasable. (a) **Listeners.** The deferral says recruiting listeners "needs people who know the project" (design log 2026-10-13, "the listening test is deferred"). A two-alternative forced-choice listening task is a standard crowdsourced experiment: Prolific or similar platforms filter participants by first language; 64 trials take ten minutes; 60 listeners from three or more L1 families cost on the order of $150–300, and none needs to know the project exists. (b) **Voice.** Listening test 01 died on synthesisers (Piper, Kokoro, MBROLA) that couldn't release a word-initial g before u. Apupiwe's sound system is close to a subset of Japanese: five vowels, (C)V(N), no clusters, and the reference stress (one high syllable, then a step down, no lengthening) is the Japanese pitch-accent pattern *atamadaka* (頭高). Open-source Japanese TTS (VOICEVOX) gives per-mora pitch control, so the reference prosody can be dialled in exactly. Gaps: *l* comes out as [ɾ] (the names rule already maps r → l, so this is the declared nearest sound), *f* as [ɸ] (loan katakana ファ フィ フェ フォ exist), *si* needs スィ, *ti/tu/di/du* exist as loan kana, *yi* and *wu* don't exist. A human reader is still better, but this removes the blocker for the author's own ear and for stimulus generation.
- **Why it matters.** B2 is a guarantee; the judge ranked a human listening test the single most important repair (C-verdict §"three most important changes"), and every word form now rests on an unvalidated model (rationale §11). The author, the one real learner, has never heard the reference pronunciation.
- **Plausibility high; effect large.**
- **Cheap check.** Price a Prolific study (10 minutes × 60 participants, L1 filters); install VOICEVOX and synthesise the ten reference sentences and the listening-01 pairs; let the author listen.
- **Covered?** Partly: the human test and the TTS failures are recorded (`tests/listening-01/README.md`, rationale §9.4, roadmap "Later"). The crowdsourcing route and the Japanese-TTS route are not.

### 2. Children's speech merges the contrasts the grammar-word layer rests on

- **What.** The L1-merger idea (auxlangs R1) is about *adults'* first languages. Children acquiring Apupiwe natively will, for two to four years, apply the normal developmental mergers: voiceless and voiced stops both produced with short-lag VOT (the aspirated long-lag category is acquired last: Macken & Barton 1980), velar fronting (k → t, g → d), gliding of /l/ (l → y or w), stopping of fricatives (f → p, s → t), typically resolved by age 4–6 (Smit et al. 1990 norms). Against today's one-syllable words and digits: **VOT merger** collapses 7 pairs (te 5 / de, po 0 / bo, pi / bi, tin / din, ke / ge, pen / ben, bu / pu); **gliding** 5 sets (yu / lu, li / yi / wi, le / we, la / ya, wo / yo); **f → p** 2 (pi / fi 1, fu / pu); **velar fronting** 3 (kin / tin, te / ke, ge / de). So the design's answer to the voicing problem (aspiration, 2026-10-13) leans on the very VOT category children get last, and a three-year-old's "pi" and "bi", "te" and "de", "la" and "ya" are one word to the parent.
- **Why it matters.** P3 and C2: the insides are designed for children who grow up with it, and the first years of native use are parent–child talk. Transient, so it rarely becomes change, but it is the part of the "native" claim no test has touched (human-01 "Not covered: children").
- **Plausibility high (the mergers are universal); effect medium** (grammar layer, for a few years per child; worse if the short-word rebuild doesn't know about it).
- **Cheap check.** Add a "child merger" key (VOT, gliding, fronting, stopping) beside the drift and L1 keys in the short-word rebuild and report collisions per same-slot group; read Smit et al. 1990 and Macken & Barton 1980 for the ages.
- **Covered?** No. `drift.md` and `research/notes/confusion-data.md` have no child-production data; the L1 key (roadmap, auxlangs R1) is a different population and a different merger set.

### 3. Pitch-only stress is a single-cue system, and four everyday registers remove the cue

- **What.** Stress is "a higher pitch on the stressed syllable", explicitly *not* longer (2.6), for drift reasons (`stress-and-sound-change.md`: lengthening reads as a word end). Natural stress languages use pitch, duration and intensity redundantly. Pitch alone is gone or overridden in: **whisper** (no F0; whispered-stress studies find listeners fall back on duration and intensity, which here carry nothing), **singing** (melody overrides; lullabies and children's songs are core native use, P3), **monopitch voices** (aged, Parkinsonian, flat affect), and it **shares the channel with intonation and emotion** (2.8): the author's own reading test heard the stress rise as a question. Stress is the word-boundary cue the design relies on: 143 of 537 content words "already sound like two grammar words, and stress separates them" (design log, grammar rebuild). The design-log argument for no tone, "tone dies in whispering", applies verbatim to pitch stress and was not applied.
- **Why it matters.** B2 (segmentation), B10 (an English or Dutch learner produces stress as length and loudness by habit), P3 (song, whisper to a sleeping child).
- **Plausibility high that the cue vanishes in those registers; effect medium** (context still segments most of the time; Mattys et al. 2005 found stress matters most exactly when context is poor).
- **Cheap check.** Whisper and hum the ten reference sentences to a listener (or the author to themself after a day): can word boundaries be found? Literature: Heeren & van Heuven on whispered stress; Japanese pitch accent in song (singers largely ignore it; listeners cope by context). Decide whether the reference variety should *allow* a small duration cue as a harmless variant rather than exclude it.
- **Covered?** Only the design side (`stress-and-sound-change.md` §recommendation 1; rationale §2). The registers that lose pitch are not discussed anywhere.

### 4. Heritage-speaker attrition is the right model for Apupiwe's natives, and it predicts what erodes

- **What.** The project's evidence on natives is Esperanto's denaskuloj (n = 8, Bergen 2001) and creoles. The larger literature is on heritage speakers: children who acquire a minority language at home and a majority language outside, which is exactly what a native Apupiwe speaker would be (auxlangs §1.1: natives are "bilingual children in families"). Its findings are specific: syntax–discourse *interface* properties erode even in near-native speakers while core syntax holds (Sorace's interface hypothesis); evidentiality is lost or simplified in heritage Turkish (Arslan, de Kok & Bastiaanse 2017); aspect in heritage Russian (Polinsky 2006); honorific and politeness systems in heritage Korean; pronoun choice becomes over-explicit (overt pronouns where natives drop). Apupiwe's topic-based **wan/yi/bu**, its evidentials, **kon**, **manni**, **nun** and the stance slot are all interface or optional systems, so this literature predicts their fate more directly than Bergen's eight children do.
- **Why it matters.** B9 and the drift watch list; C2 (the insides are for natives, and these are the natives there would be).
- **Plausibility high; effect medium** (the systems are optional or already allow naming the referent; the prediction mostly sharpens the watch list and the add-back triggers).
- **Cheap check.** Read Sorace 2011 ("Pinning down the concept of interface"), Montrul 2016 (*The Acquisition of Heritage Languages*), Polinsky 2018; add a "heritage" column to `drift.md`'s watch list with the attested outcome per system.
- **Covered?** The watch list has kon, politeness, aspect and pronoun tracking (`drift.md`), from grammaticalisation and Esperanto evidence; the heritage framing and the interface prediction are absent (no hit for "heritage" outside unrelated uses).

### 5. The model scores substitutions; the common noise event is a lost syllable, and the lost syllable is a grammar word

- **What.** `confusion.py`/`confusion2.py` model sound-for-sound confusion within a word (plus coda loss and weak onsets). A burst of noise, an overlap at a turn start, a cough or a dropped packet removes a whole unstressed monosyllable. In Apupiwe those monosyllables carry polarity (**mu**), the speech act (**min**, **yo**, **tin**), scope (**na**, **wi**) and reference (**wan/yi**). Losing **mu** flips the meaning; losing **min** turns a question into a statement; losing **yo** turns a warning into a remark; and nothing in the sentence shows that a word is missing (statements are unmarked, so a sentence with a dropped particle is still well formed). The design's answers (doubling **mu mu**, the end tag **min**, **yo yo**) exist but are optional and unmeasured.
- **Why it matters.** B1, B2 (the goal says "words are hard to mishear"; a whole-word dropout is the mishearing with the largest effect per event), and the aviation sources the speech acts rest on (rationale 4.3).
- **Plausibility high (syllable dropouts are the normal form of channel loss in conversation; Dingemanse et al. 2015: open repair rises to ~78% under noise and overlap); effect medium–large** (polarity and act).
- **Cheap check.** Deletion audit on the UDHR and a casual text: delete each grammar word in turn and classify the result (unchanged / changed meaning / ungrammatical and thus detectable). The share "changed meaning, still grammatical" is the undetectable-loss rate. Then decide whether polarity deserves redundancy by default (a stressed or two-syllable negator, or sanctioning **mu mu** as the plain form) against its Zipf cost.
- **Covered?** Partly: the judge's B9 "deletion test" is about commas (C-verdict §4); drift item 8 sanctions **mu mu**; rationale 3.2 has only phoneme-level coda and onset loss.

### 6. The language cannot read its own writing aloud across cultures

- **What.** Letters used as labels, foreign letters in names, symbols in pass-through notation (@ . / # _ %) and arithmetic signs are "read as the speaker's culture reads them" (3.4, 11.5). Two native speakers from different cultures spelling a surname, dictating an email address, a password, a flight code or "3 × 4 = 12" have no shared way to do it, and eight Latin letters (c h j q r v x z) have no sound in the language at all. B4 says writing carries the same meaning as speech; for the pass-through class it carries more, and speech cannot carry it back. L3 already supplies the answer: the ICAO spelling alphabet is the de facto international standard for spelling aloud (and was tested with listeners of several languages in noise, `high_stakes_domains.md` §2), and its digit forms are a standard too.
- **Why it matters.** B4, B6, P4 (online life is handles, codes and addresses), B3.
- **Plausibility high (the gap is certain); effect small–medium** (frequent, but speakers would borrow local letter names; the cost is cross-cultural).
- **Cheap check.** Give a translator agent an email address, a Vietnamese surname and a short equation to say aloud; see what it invents. Then decide: ICAO words adapted by `names.py` (L3, rung 1), or a native 26-letter list.
- **Covered?** No decision; 3.4 and 11.5 defer to culture. `channel_perception.md` §6 and `high_stakes_domains.md` §2 have the ICAO research but only as evidence about digits.

### 7. Audiovisual perception reverses the model's ranking: the face restores place and cannot show voicing

- **What.** The confusion model is audio-only. In real noise people watch the speaker's face, worth roughly +15 dB of signal-to-noise (Sumby & Pollack 1954). Visemes group consonants by place: p/b/m are one viseme, t/d/n/s/l near one, k/g/y another. So the face recovers exactly the feature the design treats as weakest (place) and gives nothing for the feature it leans on (voicing, nasality). For a face-to-face listener the dangerous pairs are the voicing pairs (pi/bi, ke/ge, tin/din, pen/ben, bu/pu, and digits po/bo if bo ever neighbours a number) and same-place nasal/oral pairs (mon/bon, pen/men), and the "fragile" place pairs are safer than the model says. Lip-reading is also how hard-of-hearing speakers, a share of any lifetime population, hear.
- **Why it matters.** B2; the short-word rebuild is about to re-place ~70 forms on the audio model.
- **Plausibility high (well established); effect medium** (it pushes in the same direction as auxlangs R1 on voicing pairs, so the practical change is to weight them more, not to reverse anything).
- **Cheap check.** Add an audiovisual listener group to `confusion2.py` from a published AV confusion matrix (Binnie, Montgomery & Jackson 1974; Grant & Walden 1996) and see whether the rebuild's ranking of pairs changes.
- **Covered?** No ("audiovisual", "lip" and "McGurk" occur nowhere in docs or research).

### 8. Lifetime speakers age; presbycusis is a listener group the model lacks

- **What.** C2 says natives "learn it once and use it for life". Age-related hearing loss removes energy above 2–4 kHz, which carries the f/s distinction and consonant place; it also raises reliance on lip-reading (item 7). Grammar words with f and s onsets form a cluster (fe fa fu fon fi; so se sin sun sa), and **fa/sa** was already the worst pair in the model. Model v2 has listener groups by first language only.
- **Why it matters.** B2 for a quarter of any adult population at any time; the judge's note that /f/ is the least-supported consonant (C-verdict §Sounds) compounds it.
- **Plausibility high (everyone ages); effect medium** (f/s onsets in the short-word layer; content words have more redundancy).
- **Cheap check.** Add a high-frequency-loss listener group to `confusion2.py` from hearing-impaired confusion matrices (Bilger & Wang 1976; Dubno & Dirks); or reuse Miller & Nicely's low-pass conditions, already summarised in `channel_perception.md` §1.
- **Covered?** No. `conversational_repair.md` cites one hearing-loss repair study; the model has no such group.

### 9. B2 is a property of the seed; words coined after it are unoptimised

- **What.** "Open word space is a feature" (design log 2026-10-13) assumes new roots come through `words.py`. Natives don't run tools; they coin by compounding, clipping, borrowing and sound symbolism, and they land wherever they land. Today's placed roots are extremely sparse: of 3,106 single-feature neighbours (voicing, e/i, o/u, m/n, f/p, l/y/w, ±final n) of the 517 roots, only 6 (0.2%) are real words, so almost every mishearing produces a non-word, which the listener can detect and repair. A random *free* two-syllable form has a real single-feature neighbour 14.3% of the time; at 1,500 roots it will be higher. Each native coinage therefore eats into the error-detecting margin, and B2 decays with vocabulary growth rather than holding.
- **Why it matters.** B2 and B9 together: a guarantee that only the designer's tool can maintain is not one that "survives its speakers changing it".
- **Plausibility high that natives coin without the tool; effect medium** (gradual; natural languages live with far denser neighbourhoods).
- **Cheap check.** Compute the undetectable-error rate (share of single-feature neighbours that are real words) for the 1,500-root placement and publish it as the B2 metric beside pairwise confusion; then try to state a one-line coinage rule a speaker could follow without a tool ("a new word may not share its first syllable with a word in the same field") and measure how much of the tool's protection it keeps.
- **Covered?** Partly: open word space and speakers' shortening and borrowing are decided (design log 2026-10-13); the consequence for B2 is not stated, and no error-detection metric exists.

### 10. "ok" passes through, and "ok" is the yes-word the design excluded

- **What.** 3.4 lets chat abbreviations and interjections pass through, naming *ok* first. *Ok* is the most international word there is and means "yes, agreed". The echo-answer design exists because answers to negative questions flip across languages (rationale 4.3), and the pass-through reimports the ambiguity in the most frequent answer word. The computer-vocabulary test already rendered the button "OK" as **tayu** "agree" and "Cancel" as **mu muge**, so a de facto yes-word exists in the lexicon too (`tests/computer-vocab-01/translation.md`).
- **Why it matters.** B1 (negative questions), B6 (software dialogs need one-word Yes/No/OK/Cancel; echo answers don't fit a button).
- **Plausibility high (natives will say ok); effect small–medium**.
- **Cheap check.** None needed to see the gap. Decide the reference reading of **ok**/**tayu** after a negative question (agree with the proposition as stated, as in Japanese *hai*, or agree with the polarity, as in English *yes*), and translate a standard UI string set (Yes / No / OK / Cancel / Undo / Back / Next) once.
- **Covered?** No; 4.8.6 and 3.4 don't meet.

### 11. The speech-act particle sits where listeners miss words: the start of the turn

- **What.** Overlap in conversation concentrates at turn transitions, and attention is lowest before the listener has locked on; "what?" repairs disproportionately target the first word. Dingemanse et al. 2015: open repair ("huh?") rises from 39% to ~76% under overlap. Apupiwe puts the highest-stakes monosyllables (**min**, **yo**, **tin**, **so**) at slot 3, right after any opener, with statements unmarked, so a particle lost at the turn start leaves a well-formed statement (item 5). Sentence-final particles, the WALS majority (rationale 4.3 records this as the minority position chosen for early signalling), may partly be an adaptation to this. The design already has a final **min** tag and a stance slot.
- **Why it matters.** B1 and the safety rationale for **yo** and **tin** (Tenerife, Avianca; rationale 4.3): a warning is most often shouted into an overlap.
- **Plausibility medium; effect medium** (large for **yo**, small for the rest).
- **Cheap check.** Turn-transition overlap rates (Levinson & Torreira 2015; Schegloff 2000) and where in the turn open repair targets fall (Kendrick 2015, already in `conversational_repair.md`). If it holds, consider letting the act particle be repeated at the end (as Spanish ¿…? brackets both ends), at least for **yo** and **tin**, as a convention rather than a rule.
- **Covered?** The early-signal argument and the WALS count are recorded (rationale 4.3); the attention and overlap risk is not.

### 12. The optimiser models the ear and not the mouth

- **What.** Lojban's parser author found the language "physically hard to speak" despite a letter-level distinctness filter (auxlangs §1.4); the survey drew the perception lesson (test with listeners) but not the production one. Speech-motor research gives usable constraints: the labial–coronal effect (across languages and in babbling, *pata* beats *tapa*; MacNeilage & Davis 2000; Rochet-Capellan & Schwartz 2007), same-place sequences with different manner (*tasa*, *nata*) costing more than place alternation, and consonant-harmony pressure in child speech. Today's lexicon already runs labial–coronal 100 : coronal–labial 49 by chance, and 39 roots (7.5%) repeat their consonant (**kuku**-type), which is easy to say and to babble but is also what toddlers produce for *everything*. None of this is scored; the ~1,500-root joint placement is the one cheap moment to add a production term as a tie-break.
- **Why it matters.** B10 and P3 (what children babble first and what adults can say fast), B8 indirectly (fast speech).
- **Plausibility medium; effect small–medium.**
- **Cheap check.** Add a production-cost term to `words.py` as a tie-break only (like C3): penalise coronal–labial order and same-place different-manner sequences; report how many placements it changes. Read MacNeilage & Davis 2000 for the effect sizes.
- **Covered?** No ("articulatory" appears only as "place of articulation").

### 13. The written channel has its own noise: one-key typos and autocorrect

- **What.** P4 makes online writing a primary channel, mostly on phones. The drift keys and confusion model are sound-based; the written form's errors are keyboard-adjacent substitutions and dictionary autocorrect. On QWERTY, one-key typos landing on another real word are rare today (19 of 4,858 possible, 0.4%, 18 words), so the lexicon is robust to typos by accident. Autocorrect is the bigger problem: a phone with an English dictionary will rewrite non-English forms (**guyi**, **nawi**, **tiwu**) and leave the many grammar words that *are* English words (to, me, a, in, we, no, so, man, gun, don, la). The fix is user-side (add a dictionary), but it is a real first-contact cost for the author and anyone sharing it.
- **Why it matters.** P4, B4, B10.
- **Plausibility high that it bites; effect small.**
- **Cheap check.** Type the UDHR's first three articles on a phone with English autocorrect on and count corruptions; report the typo-neighbour rate after the 1,500-root placement.
- **Covered?** No ("keyboard", "autocorrect" occur nowhere; "typo" hits are "typology").

### 14. A design rule stops relative clauses from being followed; nothing stops a speech-act particle from being heard as a hesitation

- **What.** 2.10 puts hesitation sounds outside the sound system, but the universal filled pause is a central or low vowel ("uh", "ah", "eh", "ano"), and the two vowel-only grammar words are **a** ("you know", stance slot) and **o** (focus, before any word). A speaker's "a…" at a sentence end is the stance word; "o…" before a word is focus. The rebuild already plans a consonant-initial form for **a** on other grounds (vowel-initial fragility); the hesitation argument is a second, independent reason, and applies to **o** too.
- **Plausibility medium; effect small.**
- **Cheap check.** None; fold into the short-word rebuild's reasons for **a** and **o**.
- **Covered?** The form change for **a** is queued (design log 2026-10-13, speech-act words); the reason here is new, and **o** is not included.

### 15. Probability is a late concept; the native child can't use **kon** for years, and will learn it as a set of hedges

- **What.** Children handle verbal probability from about 7–10 (Piaget & Inhelder); numeric chance later. A native child hears **kon fi**, **kon te**, **kon ka** as parents' hedging words long before the sixths mean anything, so the native acquisition path *is* drift item 1 (collapse to favourite values used as degree words). Optional, so cost is nil; the point is that the drift is not a risk but the acquisition order.
- **Plausibility high; effect small** (already the watch list's prediction).
- **Cheap check.** None needed; note it against drift item 1 as the mechanism.
- **Covered?** Drift item 1 and the watch list (`drift.md`) predict the outcome; the acquisition mechanism is not named.

---

## 2. Long shots

Kept because rare ideas are the point of this pass; none is worth work now.

- **Puns, rhyme and word-play.** A lexicon with 0.2% single-feature neighbours is designed against puns; five vowels and a V/n-only ending make rhyme nearly free and so nearly worthless as craft; every content word is a trochee or dactyl, so iambic metres are impossible. N5 and the B6 deletion say art comes from use, and that stands; the one native-relevant angle is that sound-play (rhyming games, minimal-pair jokes) is part of children's phonological development. No action; a curiosity to record.
- **Swearing contaminates its roots.** Natives will build swear words from the taboo roots (**bodu**, **wento**, **kono**, **nosen**, as the Restraint review expects), and taboo spreads to homophones and near-homophones (English *ass*, *cock*; Allan & Burridge). The sparse lexicon makes this cheaper than in natural languages. No action.
- **Agrammatic aphasia and isolating grammar.** Broca-type aphasia drops function words; in Apupiwe that drops polarity, acts and tense but keeps roles (fixed SVO by position is what agrammatic speakers rely on anyway; Bates's cue-validity work). Chinese agrammatism shows classifier and function-word omission in an isolating language. Suggests the language degrades gracefully for roles and badly for polarity, the same shape as item 5. No action.
- **Stuttering** clusters on word-initial stressed syllables and stop onsets; every content word starts with one, and the reference aspirates p t k there. Probably neutral (most languages are similar). No action.
- **Dyslexia** is milder in transparent orthographies (Paulesu et al. 2001; Seymour 2003): a benefit already earned by one letter per sound. The alphabet keeps three of the four mirror letters (b d p). Record as a plus.
- **Doubling versus child reduplication.** Children and caregivers reduplicate for diminutives and first words (*mama*, *wawa*); the grammar makes doubling mean "wider or stronger". A toddler's **totu totu** is "doggy", not "very dog". Harmless; natives will sort it out.
- **p is the rarest consonant** in the lexicon (31 of 1,290 consonant tokens; 16 word-initial) although it is among the commonest stops in the world's languages. Probably the digit **po**, the grammar words **pi pu pen** and the offensive filter squeezed it. Check `words.py`'s scores for p-initial forms before the big placement; nothing else.
- **Transliteration tables for other scripts.** Speakers in Cyrillic, Arabic, Devanagari, Hangul and kana cultures will write it in their scripts whatever L3 says (Esperanto in Cyrillic; everything in katakana). A one-page canonical table per script costs nothing and prevents divergent spellings; some scripts can't write *yi*, *wu* or *si*. Only if sharing reaches such readers.
- **Search invisibility.** "apu pi we" and most grammar words are common words in other languages; text in the language can't be found by searching for it. The one-word name *Apupiwe* solves it for the project; a corpus tag would be needed for texts. No action.
- **Reading "." aloud and in digits.** The full stop is also the decimal point; "**dili 3. 5 guyi**" is readable only by the space. Edge case; note in the writing rules if it ever bites.
- **A canonical spoken form for the 18 letters' *names*** is part of item 6; the long-shot version is a native alphabet song, which children in every literate culture get and which fixes letter order and names in one go. Comes free once item 6 is decided.

---

## 3. Process: ways the project could be fooling itself

- **The "different model" premise is thinner than it looks.** This pass was run on a Claude model from the same company as the designer, trained on much the same material; the blind spots most likely to be shared are the ones neither of us can see (the Toki Pona form prior the judge found, A3 5.3, is an example of a prior that only an outside reader caught). The judge's own repair (C-verdict, evidence base, 7) stands: at least one reviewer who is not a Claude model.
- **"[author]" as a source can overstate independence.** Nearly every decision is a choice among options Claude framed, presented one at a time, at a pace of dozens a day. The rationale's labelling rule (Claude-sourced parts are the most worth doubting) is right, but the framing of the options is Claude-sourced even when the pick is the author's. Cheap check: count decisions in the design log where the author chose an option Claude did not recommend, or rejected all options (**ba** restored, lineage weighting, base 10, the goal's ranking are examples). If the count is low, "author decides" is ratification, and the five-steps rule about Claude's requirements applies to the option sets too.
- **The real first speaker community is LLM instances.** The learner guide tells the author to practise with an AI given the reference; the translators are AIs; the docs-for-agents rework (roadmap) exists because agents produced wrong Apupiwe. Whatever the agents' systematic errors are (they missed **kiyo**; they default to English loans; they pivot through English senses of grammar words that are English words: *to, me, man, gun, don*) will be what the author learns. Cheap check: before the author starts learning, run the planned agent-documentation through a fresh agent on the thirty most frequent constructions and score it; treat its error list as the first "dialect".
- **Every frequency the design uses is a frequency of English-gloss equivalents.** Grammar-word Zipf (15 languages, equivalents supplied by an agent), root ranks (coverage list), modern-use boundaries: all go through glosses chosen by an English-dominant process. The design knows this (rationale §11, auxlangs V3); the untested step is whether an agent asked in Mandarin or Yoruba for "the everyday word for X" returns the same ranking. One re-run of the grammar-rebuild frequency table from prompts in two non-English languages would show the size of the effect.
- **Review → repair → review is a treadmill the goal's own rules warn about.** Each pass yields ~20 items; the roadmap holds dozens; the tooling (14 tools, a spec compiler, a formal grammar, a lessons checker) is step 5 built early. The author made these choices and they are defensible for a thought experiment whose product *is* the evidence it collects (auxlangs lesson 10). One-line flag only: the dog-owner test for each tool is "did the author learn or share anything with it this week?".

---

## 4. Looked for and found covered (so the author knows it was checked)

Sign and gesture (N1; sign loci and pointing with **tan/ben** are in the design log); bilingual natives and transfer (auxlangs §1.1, R1); L1 voicing and f=p mergers (roadmap, shortwords-01); derivation markers widening, class rebuilding, particle hardening (auxlangs R2–R4, `drift.md`); pauses carrying grammar and **kiyo** (C-verdict, design log 3a); loans in adapted form (auxlangs R5); endearment/diminutive (globasa row 30); imitative and nursery forms (globasa §8.3); correlatives, never/often/later (design log, inventory 2); modifier of a modifier (design log 2026-10-13); verbs with no object (globasa row 21); rates and percent (roadmap); yes/no words rejected for negative questions (rationale 4.3; the pass-through gap is item 10); humour and art left to use (B6 deletion); swearing (Restraint review); telephone band and noise (C-verdict §4, `channel_perception.md`); English-centred instruments (rationale §11, auxlangs V3); AI readers paraphrasing better than people (coverage decision); the shared Toki Pona prior (A3 5.3); the name (roadmap); "ok" and emoji passing through (3.4, but see item 10); the short-word layer's vowel-only and glide pairs (C-verdict); keeping a segmental alternative wherever a pause is the only cue (auxlangs R6); crowd-free human tests deferred (design log 2026-10-13; see item 1 for why the deferral's trigger is wrong).

---

## 5. Top ten, one line each

1. The listening test isn't blocked by people: crowdsourced L1-filtered listeners cost ~$200, and Japanese pitch-accent TTS (VOICEVOX) can produce the reference pronunciation the other synthesisers couldn't.
2. Children's developmental mergers (short-lag VOT, l→y/w, k→t, f→p) collapse 17 pairs or sets among today's grammar words and digits for the first years of native use; the aspiration fix leans on the VOT category children learn last.
3. Pitch-only stress has no backup cue: whisper, song, monopitch voices and question intonation remove or crowd it, and it is the word-boundary cue; "tone dies in whispering" applies to it too.
4. Heritage-speaker research (Sorace, Montrul, Polinsky, Arslan) is the right model for Apupiwe's natives and predicts that interface systems (topic pronouns, evidentials, kon, politeness) erode first.
5. The model scores substitutions; the common channel event is a lost unstressed syllable, and losing **mu**, **min** or **yo** leaves a well-formed sentence with the opposite meaning; run a grammar-word deletion audit.
6. The language can't read its own writing aloud across cultures (letter names, the eight absent Latin letters, @ . / # and arithmetic); L3 points at the ICAO spelling alphabet.
7. Face-to-face listeners lip-read: the face restores place and can't show voicing, so the audio model under-rates exactly the voicing pairs the short-word rebuild is about to re-place.
8. Lifetime speakers age; add a presbycusis listener group (loss above 2–4 kHz) to confusion2, which hits the f/s grammar words first.
9. B2 is a property of the seed: 0.2% of placed words' single-feature neighbours are real words, but a random free form has one 14% of the time, and natives coin without the tool; publish an undetectable-error metric and a tool-free coinage rule.
10. "ok" passes through as the yes-word the echo-answer design excluded (and the UI test already coined **tayu** for OK); decide what it means after a negative question.

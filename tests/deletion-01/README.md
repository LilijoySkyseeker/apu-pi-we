# Deletion audit (deletion-01)

**Question.** When one short grammar word is lost to noise, does the listener get a signal (the rest stops making sense, so repair starts), or does a normal sentence with another meaning remain? Decided by the author 2026-10-15 (design log, last entry; `research/notes/unknown-unknowns.md` items 5, 11, 14). Speakers adapt to noise they notice and the language already offers redundant forms (**mu mu**, end tag **min**, **yo yo**); this audit is about losses nobody notices. A grammar change only if Apupiwe is clearly worse than natural languages at signalling a loss.

**Short answer.** Almost nothing signals a lost short word: 84% of deletions still parse as a full sentence. But most of those losses barely change the meaning, and the losses that do change it are the same ones natural languages have: the negator (**mu**: 44 of 44 losses leave the opposite sentence, as with English *can't*, Spanish *no* and Mandarin 不) and the yes/no question particle (**min**: 19 of 19 leave a statement, as with Mandarin 吗). Apupiwe isn't clearly worse than English, Spanish or Mandarin for negation. For questions it's about as fragile as Mandarin, which is weaker than English or Spanish. It's somewhat worse in two places: its speech-act particles come first in the sentence (77% of them), where overlap swallows words, and **yo** and **yu** are single unstressed syllables where natural languages use stressed words. The smallest response is to teach the redundant forms for high-stakes talk (**mu mu**, the end tag **min**, **yo yo**, readback). No grammar change.

## Method, and the source of each part

| Part | Source |
|---|---|
| Frames: every reference example and every UDHR sentence of at most 16 tokens that the GF grammar parses, built with `tests/shortwords-02/positions.py` (imported, not copied) | PROMPT (author's audit, design log 2026-10-15) |
| plus the casual texts of `tests/coverage-01`: talk and chat texts 01–10 and 21–28, base-vocabulary versions (`part2b/ap-base/`), sentences of at most 16 tokens, without quotes, digits, clock times or emoticons, where they parse | PROMPT. Which texts count as casual (talk + chat, not news or how-to) and the base version (no placeholder roots) are **added** |
| Quote marks are stripped from frames, and GF error lines no longer count as parses | **added** fix: `positions.py` counts GF's "command not parsed" line as a tree, which gave it 5 false frames (`1\`, `2\`, `3\`, `4\` and a reference sentence ending in `."`) |
| Delete each grammar word (`grammar.tsv`) and each digit 0–5 in turn, then parse the remainder with `grammar/Apupiwe.pgf` | PROMPT. Two-syllable operators (**genso**, **kiyo** …) left out, **added**: they're stressed and the question is about one short syllable |
| Classes: (i) no parse = detectable; (ii) parses only as a fragment (FragNP/FragAdv/FragAP) where the original had a full reading = weakly detectable; (iii) a full parse = undetectable | PROMPT. Fragment test as in `positions.py` |
| "Strained" (column `strained`, figures in brackets below): every full reading of the remainder puts more roots in an unusual role (a thing-word as a verb …) than the original's most natural reading did | **added**: GF lets any root take any role (4.2.3), so a parse alone is generous |
| **en**: the parser can't read a name without **en** (it becomes an unknown token), so these losses are set to undetectable and barely changed | **added**: reference 11.1 makes a bare name the casual form |
| Meaning of an undetectable loss: changed (polarity, speech act, tense/aspect, reference, scope, role, number, structure), unspecified (a dropped pronoun that context may supply) or barely changed. Set by a rule from the word's class (`meaning()` in `deletion.py`) with context exceptions: a doubled word (**mu mu**), **mu** with **fa**, a determiner after a noun | PROMPT ("by rule from the word's class"). The rules, exceptions and the "unspecified" label are **added** |
| Hand checks on samples (`handcheck.tsv`, 211 losses): B barely changed, C plainly changed and still natural, O odd enough that a listener would likely notice | PROMPT. Using each class's share of C as a factor on the rule's "changed" share in the ranking is **added** |
| Stakes: 3 for negation (**mu**, **fa**), speech acts (**min**, **so**, **tin**, **fon**, **de**, **yu**) and warning (**yo**); 1 for politeness (**nun**) and stance (**a**, end-tag **min**) | PROMPT |
| Stakes for everything else: 1 for **ba** (emotion, grouped with emphasis in 1.6), **la tan ben bo bi fe o nen gun wun un yen en**; 2 for the rest, digits included | **added**, no named source |
| Frequency: `grammar.tsv` `freq`; digits 4.0 each | inherited from shortwords-02, whose README records no source for either |
| Rank: frequency × stakes × share of losses that are undetectable and plainly changed (hand-corrected); a dropped pronoun counts at 0.06, the share of the 16 hand-checked pronoun losses that misled | PROMPT for the product. Reading "undetectable" as "undetectable and changed", and the pronoun weight, are **added** |
| **min** split into act, end tag and indirect "whether"; the six digits pooled into one ranked row | **added** (the prompt asks for the act particle and the end tag separately) |
| Positions: where each speech-act particle stands in every corpus sentence, parsed or not | PROMPT |
| Natural-language comparison by hand | PROMPT; from memory, see below |

One flag: the stakes for words outside the prompt's list, the hand-correction factors and the pronoun weight move the ranking a lot, and they're my own choices. They're cheap to change in `deletion.py`, and only the top of the ranking matters for the verdict.

Rerun: `direnv exec ~/work/repos/universal-language python3 tests/deletion-01/deletion.py` (about a minute with 14 GF processes; it writes `cache.json` and `english.json` as caches, which can be deleted).

## Files

- `deletion.tsv`: one row per deleted token (1,600): frame, source, word, function, position, the remainder, result, strained, meaning label, stakes, and the English of the original's and the remainder's most natural reading.
- `frames.tsv`: the 469 frames with the original readings: number of trees, full or fragment-only, roles, English.
- `words.tsv`: the per-word summary and ranking. Columns: tokens; detectable / weak / undetectable counts; `undet_share` and `undet_share_strict` (not strained); `changed_share` (rule), `hand_factor`, `changed_share_hand`; `unspecified_share`; stakes; harm per token; score.
- `positions.tsv`: speech-act particles and **nun**, first word or not.
- `handcheck.tsv`: the hand-judged samples. `sample.txt`: a random 60 of the undetectable losses with English, for reading.

## Results

**Frames.** 469 in all: 196 reference sentences, 125 UDHR sentences and 148 casual sentences. The casual texts give 222 sentences without quotes, digits, clock times or emoticons; 45 are longer than 16 tokens, and 148 of the remaining 172 distinct sentences parse. By text: 01 19, 02 11, 03 6, 04 10, 05 27, 06 5, 07 9, 08 1, 09 2, 10 3, 21 13, 23 25, 24 4, 25 4, 27 3, 28 6 (22 and 26 have nothing usable). 395 frames have a full reading and 74 only a fragment reading.

**Deletions: 1,600 tokens.**

| | share |
|---|---|
| detectable (no parse) | 16% (263) |
| weakly detectable (fragment only) | 0.06% (1) |
| undetectable (full parse) | 84% (1,336); 70% if strained parses are excluded |
| undetectable, meaning changed by the class rule | 46% |
| the same, corrected by the hand checks | 21% |
| undetectable, pronoun dropped (context usually restores it) | 18% |
| undetectable, barely changed | 20% |

The shares are about the same in each source: reference 85%, UDHR 85% and casual 81% undetectable. The fragment class hardly ever occurs, because the grammar almost always finds a full reading. What breaks a parse is mostly a dangling word: the number after **kon** (all 4 **kon** losses are detected), a clause left without its verb, or **wun**, **don** or **gi** taken away from their clause.

**Hand checks** (`handcheck.tsv`). These are the shares of rule-"changed" losses that a reader judged plainly changed and still natural (C). Each tally is B / C / O.

| class | sample | B / C / O | C share |
|---|---|---|---|
| relation words (pi mon tun li gan fu se) | 30 | 15 / 6 / 9 | 0.20 |
| **yu** | 14 | 0 / 11 / 3 | 0.79 |
| digits | 14 | 5 / 6 / 3 | 0.43 |
| **we** | 8 | 4 / 4 / 0 | 0.50 (UDHR's generic "every person" → "a person" barely changes) |
| **man** | 8 | 3 / 1 / 4 | 0.12 |
| **yen** | 8 | 6 / 1 / 1 | 0.12 |
| **no ge du pu** | 10 | 5 / 3 / 2 | 0.30 |
| **ke** (all) | 12 | 4 / 4 / 4 | 0.33 |
| **le** (all) | 10 | 7 / 3 / 0 | 0.30 |
| **lu** (all) | 11 | 3 / 0 / 8 | 0.00 (a lost "or" leaves nonsense such as "tikun weki", or a list that is still a list) |
| **un** (all) | 3 | 3 / 0 / 0 | 0.00 (sentence-initial "but" after a pause) |
| **sin** | 15 | 1 / 14 / 0 | 0.93 (in a set past frame the loss is harmless) |
| dropped pronoun, casual texts | 16 | 15 / 1 / 0 | 0.06 |

The losses of **mu**, **min**, **so**, **tin**, **de**, **fon**, **yo**, **na** and **wi** were read in full (`deletion.tsv`). All change the meaning as the rule says. **so** and **de** losses are often mild in context: **pen isi** "we go" for "let's go", **to dinyo we** "I carry it all" for "I'll carry it all".

The O column matters: about a third of relation-word losses and half of **man** and **lu** losses parse in GF but read as nonsense (**yidu musu wan se wan** "take thing her from her"), so a human listener would probably notice them. GF's verdict of "undetectable" is an upper bound.

**Per word: the ten highest-ranked** (score = freq × stakes × undetectable-and-changed share, hand-corrected; * fewer than 5 tokens; full table in `words.tsv`):

| rank | word | gloss | freq | tokens | undetectable (not strained) | changed: rule → hand | stakes | score | what changes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **mu** | not | 7.0 | 44 | 100% (100%) | 98% → 98% | 3 | 20.5 | polarity |
| 2 | **min** (act) | question | 3.0 | 19 | 100% (100%) | 100% → 100% | 3 | 9.1 | speech act |
| 3 | **yu** | what/which | 3.0 | 32 | 91% (91%) | 91% → 72% | 3 | 6.4 | question → statement |
| 4 | **na** | only | 3.0 | 6 | 100% (100%) | 100% → 100% | 2 | 6.0 | scope |
| 5 | **so** | request | 2.0 | 17 | 100% (100%) | 100% → 100% | 3 | 6.0 | speech act |
| 6 | **wi** | even | 3.0 | 3* | 100% (100%) | 100% → 100% | 2 | 6.0 | scope |
| 7 | **de** | commit | 2.0 | 4* | 100% (100%) | 100% → 100% | 3 | 6.0 | speech act |
| 8 | **sin** | done | 3.0 | 38 | 100% (100%) | 100% → 90% | 2 | 5.4 | tense/aspect |
| 9 | **tin** | instruct | 1.5 | 4* | 100% (100%) | 100% → 100% | 3 | 4.5 | speech act |
| 10 | **in** | some | 2.0 | 1* | 100% (100%) | 100% → 100% | 2 | 4.0 | quantity |

Next come **fon** (3.0), **we** (2.7), **pi** (2.6) and the digits (2.3). **pi** has the most tokens and 81% of its losses are undetectable, but the hand check finds only 16% plainly changed. High frequency doesn't make it high risk.

**The words asked for:**

| word | tokens | undetectable | plainly changed | rank | note |
|---|---|---|---|---|---|
| **mu** | 44 | 100% | 98% | 1 | every loss gives the opposite (**mu upe** → **upe**; **tin mu kusa** → **tin kusa**). The one exception is **to mu ibe totu fa**, where **fa** still negates |
| **min** (act) | 19 | 100% | 100% | 2 | a question becomes a statement (**min me la nawi pasu wulon** → "you eat the wet food") |
| **min** (end tag) | 3* | 100% | 100% (stance) | 40 | "…, right?" is lost; low stakes |
| **min** "whether" | 3* | 100% | 100% | 24 | **to mu lugo wun min wan obu** → "I don't know that she's coming" |
| **yo** | 1* | 100% | 100% | 22 | **yo nun osa le obu** → "(politely) the water is coming": the warning goes, the danger stays in the words |
| **tin** | 4* | 100% | 100% | 9 | **tin nun mu nuta** → **nun mu nuta** "(it) doesn't fear"; a lost **tin** before **mu** gives a negative statement |
| **so** | 17 | 100% | 100% | 5 | request → statement, often mild (**so pen isi** → "we go") |
| **na** | 6 | 100% | 100% | 4 | "only" is lost: **ewo sa lenu bedan na don …** "only if" → "if" |
| **wi** | 3* | 100% | 100% | 6 | "even if" → "if" |
| **a** | 2* | 100% | 0% | 61 | stance "you know" is lost; nothing else changes |
| **o** | 3* | 100% | 0% | 60 | focus is lost; nothing else changes |

For words with few tokens the outcome comes from the grammar rather than the sample: the act particle, **nun** and the stance slot are optional (4.1, 7.1.2), so taking one out always leaves a well-formed statement. The small counts show how rare these words are in the corpus. They aren't the reason for the 100%.

**Item 14 (a and o heard as hesitation).** This audit measures loss, not insertion. By the same rule, though, an *inserted* **a** (a hesitation heard as "you know") or **o** (heard as focus) only adds stance or emphasis, the lowest-stakes changes in the table. That weakens the case for changing the form of **a** or **o** on hesitation grounds. The form change already queued for **a** rests on other reasons.

**Item 11 (positions).** In all 563 corpus sentences (reference, UDHR up to 16 tokens, and casual; parsed or not), the speech-act particles come first in the sentence 49 times out of 64 (77%): **min** 17 of 23, **so** 16 of 19, **tin** 6 of 6, **de** 4 of 7, **fon** 3 of 4, **yo** 1 of 1, **ba** 2 of 4. Most of the rest follow an opener or a call and its pause (11), or **genso**/**ba** (2). **nun** comes first 19 times out of 41.

Does the end-tag **min** appear in the corpus? Yes, 4 times, always as the stance "right?" and never as a repeat of a question's opening **min**. It occurs once in the reference (**wan sin oyi bu, a min**) and three times in the casual texts (**tin mu yaga pasu … , min**; **…, kon te yegon feli guge, min**; **…, gun mu denku, min**). The reference also has **kon ka wan sin oyi bu, min** (7.2.6), but `spec.py examples` doesn't extract it, so it's missing from the frames. In the full corpus (UDHR at any length), doubled **mu mu** occurs once (a long UDHR sentence, not a frame) and **yo yo** never. No sentence has both the opening and the final **min**.

## Natural-language comparison (by hand, from memory)

**Everything in this section is from memory**: my own judgments of the sentences, not checked against a corpus, a source or a native speaker.

| language | item | sentence | one word lost | what the listener gets |
|---|---|---|---|---|
| English | negator | *I don't know* | *I do know* | well-formed only with stress on *do*; unstressed it sounds off: **weakly detectable** |
| | | *She isn't coming* / *I can't swim* | *She is coming* / *I can swim* | the opposite, well-formed: **undetectable** (can/can't is a known trap even with nothing lost) |
| | | *I haven't seen anyone* | *I have seen anyone* | ungrammatical (*anyone* needs a negative): **detectable** |
| | | *Don't touch it* | *Touch it* | the opposite command: **undetectable** |
| | question | *Are you coming?* | *You coming?* | still a question (inverted order or rising pitch over the whole sentence): **nothing lost** |
| | | *Where are you going?* | *Are you going?* | still a question, a different one |
| | warning | *Careful, it's hot* | *It's hot* | a statement, but the danger is in the words; shouted warnings carry their prosody |
| Spanish | negator | *No sé* | *Sé* | "I know": **undetectable** |
| | | *No vino nadie* | *Vino nadie* | ungrammatical (postverbal *nadie* needs *no*): **detectable** |
| | | *No lo toques* | *Lo toques* | subjunctive with no negation or main verb: not a command, **detectable** |
| | question | *¿Vienes?* | (no word to lose) | intonation only; noise can hide the final rise, but no single word carries the question |
| | warning | *¡Cuidado, quema!* | *Quema* | "it burns": the danger is in the words |
| Mandarin | negator | 我不知道 | 我知道 | "I know": **undetectable** |
| | | 我没去 | 我去 | "I go / I'll go": **undetectable** |
| | | 别动 | 动 | "move": **undetectable** |
| | | 一个人都没来 | 一个人都来 | odd (都 with "one person" needs the negative): **detectable** |
| | question | 你去吗? | 你去 | a statement: **undetectable** (a 吗 question needn't rise) |
| | | 你去不去? | 你去去 | ill-formed: **detectable** |
| | warning | 小心，地滑 | 地滑 | "the floor's slippery": the danger is in the words (小心 is two stressed syllables) |

Reading across: every language has a short negator whose loss leaves the opposite sentence. The natural languages get partial redundancy from negative concord and polarity items (*anyone*, *nadie*, 都…没). Apupiwe has the same pattern with **mu … fa**, but **fa** is rarer than *anyone* or *nadie*. English and Spanish spread the yes/no question over word order and intonation, and Mandarin's 吗 is one unstressed syllable like **min**, though at the end. Natural warnings are stressed words or shouted prosody, while **yo** is one unstressed syllable. In all three languages the content of a warning usually still states the danger, and the same holds for Apupiwe.

## Verdict

**Is Apupiwe clearly worse than these natural languages at signalling a lost word?** No, not overall.

- **Negation (mu): no worse.** The loss is undetectable in all four languages in the common case. English and Spanish catch some losses through *any-* words and negative concord (*nadie*), and Spanish catches some through the subjunctive of negative commands. Apupiwe's only built-in echo is **fa** (and **mu mu**), so it's at most slightly worse. The stakes are the highest in the table, which is why **mu** ranks first by a wide margin.
- **Yes/no questions (min): as fragile as Mandarin, weaker than English and Spanish.** All 19 losses become statements. Two things soften this: an answer is expected, so a statement from the asker draws a reply or an echo either way, and 2.8 already allows a rising tone, which carries the question across the whole sentence.
- **Turn start (item 11): somewhat worse.** 77% of act particles come first, the position overlap swallows. Mandarin's 吗 and English and Spanish intonation sit at or over the end. The end-tag **min** puts a second marker at the end; it's in the language but used only as a stance tag.
- **Warning (yo): somewhat worse in form, not in effect.** It's one unstressed syllable against stressed words in natural languages. In the one example, as in natural warnings, the danger stays in the content. Real alarms are shouted, and **yo yo** is the emergency form.
- **Question words (yu): somewhat worse.** An unstressed syllable in place, where English *what* and Mandarin 什么 are stressed. Of the hand-checked losses, 11 of 14 become plain statements. Some losses leave a dangling **fu**, **wifu** or **se kemu**, which a listener may catch.
- **Everything else is low.** **na** and **wi** change scope (low to medium stakes, rare words). Losing **sin** changes tense the way English loses *-ed* in fast speech. Relation words, **man**, **yen**, **lu** and pronouns mostly either barely change the meaning or leave nonsense a listener notices. **nun**, **a**, **o**, **fe**, **bi**, **la** and **gun** barely change it.

**Smallest response, as recommendations only:**

1. **Teach the redundant forms for high-stakes talk; no grammar change** (recommended). In lessons and the reference's notes on noise, as aviation teaches "negative" and readback: **mu mu** when a "not" must not be missed; the end-tag **min** on a yes/no question whose answer matters (**min me lugo bu, min**), which also covers the turn-start loss; **yo yo** for real danger; and an echo answer (4.8.6) as readback. Cost: nothing in the default forms, and one syllable plus a pause when a speaker chooses it. Add-back trigger for a grammar change: a listening test or real use where losses of **mu** or **min** go unnoticed more often than in a natural-language baseline.
2. **Nothing** is defensible. The losses that matter are the ones every language has, and speakers adapt to noise they notice (design log 2026-10-15).
3. **Grammar change**, not recommended. Possible changes: (a) a two-syllable or obligatorily doubled negator (+1 syllable on every negative, at freq 7 the costliest word in the table); (b) an obligatory end-tag **min** (+1 syllable and a pause on every yes/no question); (c) stress on **yu** or **yo**, a prosody rule with no syllable cost but an exception to 2.4. Only (c) is cheap; it can wait for a listening test.

Items 11 and 14 can be decided with these numbers: for 11, the end-tag convention in recommendation 1 rather than moving the particle; for 14, no change to **a** or **o** on hesitation grounds.

## Found along the way (for the roadmap)

- `tests/shortwords-02/positions.py` counts GF error output ("command not parsed") as a parse, which gave it 5 false frames (`1\` … `4\` from UDHR article numbering, and a reference sentence ending in `."`). Its substitution counts include these frames. The fix (accept only lines starting with `MkUtt`, strip quote marks) is in `deletion.py`.
- `spec.py examples` misses **kon ka wan sin oyi bu, min.** (7.2.6), so `gf_check.py` doesn't check it either. The sentence parses with the intended reading.
- **sun** (logophor) has no token in any frame.

## Limits

- GF over-generates (any root in any role), so "undetectable" is an upper bound. The strained check removes some cases (84% → 70%), and the hand checks suggest a human notices about a third of relation-word losses.
- Meaning labels come from a rule plus small hand samples (8–30 per class) judged by one reader (me). The judgments are in `handcheck.tsv` for review.
- The corpus is mostly written and formal (UDHR), and the casual texts are AI translations. Speech-act particles are rare in it (**yo** 1 token, **tin** 4), so their numbers come from the grammar more than from the sample.
- Only whole-word loss is modelled, one word at a time, and every word is treated as equally likely to be lost. Stress, position and the listener's expectations aren't modelled.
- The natural-language comparison is a handful of sentences from memory, not a measurement.

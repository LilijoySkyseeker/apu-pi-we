# Multilanguage test 01: what have we missed?

Agreed with the user 2026-10-10, before any results. Goal: find gaps, not
score and not change anything.

## Languages

The most spoken by total speakers (Ethnologue 2025), English included
(user):
English, Mandarin, Hindi–Urdu (one spoken language), Spanish, Arabic
(Egyptian for spoken scenes, Standard for formal and written), French,
Bengali, Portuguese, Russian, Indonesian, Vietnamese. Vietnamese takes the
slot freed by merging Hindi and Urdu: it's the next by numbers that isn't a
near-relative of one already listed.

## Registers

Chosen to cover the dimensions that drive variation (Biber's
multidimensional analysis, plus power/solidarity):

1. Close and casual: friends, family (involved, situation-dependent).
2. Hierarchical: speaking up to a boss, an elder, an official (power).
3. Written for a stranger: instructions, technical, legal (informational,
   explicit, abstract).
4. Persuasive: argument, opinion, complaint (persuasion, stance, emotion).
5. Narrative: story or news (sequence, time, reported speech, tracking).

Dropped, with triggers: transactional (add back if stage 1 finds forms only
used in service encounters); emotional (add back if judges keep flagging lost
tone); urgent (add back if stage 1 shows urgency marking the politeness test
didn't probe).

## Stages

1. **Desk inventory.** One agent per language, prompted in that language. It
   lists what the language marks in each register, with examples, then checks
   each item against the grammar: carried, partly, not. Output:
   `inventory/<language>.md`, in English.
2. **Round trips.** Scope decided after stage 1. One scene per language that
   switches between two registers, aimed where stage 1 predicts the densest
   gaps. Writer → translator → back-translator → judge, all fresh agents
   prompted in the target language. Score 0–2 per line; cause L/T/E (as in
   roundtrip-01); plus stage 1's checklist.
3. **Synthesis (Claude).** Merge gaps, rank by how many languages mark them,
   report in English. No design changes.

## Bias controls

Every agent is prompted in the target language; each step is a fresh agent;
the back-translator never sees the source. The grammar and lexicon are in
English. That can't be avoided, so it's noted.

## Stage 2 scope (agreed 2026-10-10, after stage 1)

Seven scenes aimed at the stage 1 themes, each switching between two
registers. Writers aren't told the themes, only the registers.

| Language | Registers |
|---|---|
| Vietnamese | casual ↔ hierarchical |
| Hindi–Urdu | hierarchical ↔ narrative |
| Arabic (Egyptian) | casual ↔ hierarchical |
| Russian | casual ↔ persuasive |
| Mandarin | narrative ↔ written for a stranger |
| English | persuasive ↔ narrative |
| Spanish | written for a stranger ↔ persuasive |

The judge sees the source, the translation (with glosses) and the
back-translation, scores 0–2 per line, labels each loss L/T/E, and checks the
language's stage 1 top gaps: did each occur, and did it survive?

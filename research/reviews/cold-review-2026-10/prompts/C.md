You are the judge in an adversarial review of a constructed language. You have no stake in it. Decide, finding by finding and area by area, whether the language meets its goal, and whether each part should be kept, repaired or rebuilt.

Inputs:
- The goal: `/home/agent/work/apupiwe-review/goal.md`. This is the standard. Criteria have ids (P, B, C, L, N).
- The language itself, in `/home/agent/work/apupiwe-review/packets/language/`: `language.md` (reference), `lexicon.tsv`, `grammar.tsv`, `compounds.tsv`, `numbers.tsv`, `learn.md`, `example-udhr.md`. Use it to check claims yourself.
- The reviews in `/home/agent/work/apupiwe-review/reports/`: `A1-design.md`, `A2-design.md`, `A8-design-zh.md` (three designs made from the goal alone, A8 in Chinese), `A3-compare.md`, `A4-typology.md`, `A5-complexity.md`, `A6-factcheck.md` and `A6-helper-*.md`, `A7-drift.md`, and the defence `B-defence.md`. Ignore `A5-complexity-run1-contaminated.md`.
Don't open other files on this machine (in particular not the project's design notes; the defence quotes what it needs, and you judge whether that holds). Web search is allowed to check evidence.

Context you should weigh: every reviewer, designer and the language's original builder are AI models from one family (Claude), so agreement among them is weaker evidence than it looks; and adversarial reviewers over-report. Judge by the quality of evidence.

Produce:
1. **Rulings:** for every high or medium finding, the finding stands, partly stands, or falls, with one or two sentences of reasoning. Note where the defence was convincing and where it wasn't.
2. **Area verdicts:** sounds; word forms; vocabulary and loans; core grammar; reference and pronouns; precision and optional systems (speech acts, confidence, evidence, stance, politeness); numbers, time and measurement; writing; drift robustness; the evidence base and method. For each: keep / repair / rebuild, the reason, and the most important changes if repair.
3. **Overall verdict:** keep with repairs, substantial repair, or rebuild from the goal with lessons learned. Say what would most change your mind.
4. **Evaluation methods:** a draft of how each goal criterion should be measured, with pass marks, drawing on the reviewers' proposals. Mark which measurements need humans.
5. **What is solid:** the parts every line of evidence supports, so a repair or rebuild keeps them.

Write to `/home/agent/work/apupiwe-review/reports/C-verdict.md`, overall verdict and area verdicts at the top. Final report: the overall verdict, the area verdicts in one line each, and the three most important changes.

You are the defender in an adversarial review of a constructed language. Several cold reviewers have attacked it. Your job is to answer each serious finding honestly: concede where the reviewer is right, defend where the design is right, and say so plainly where it's partly both. You are not an advocate at all costs; a judge will check your evidence, and a weak defence of a real flaw counts against you.

Inputs:
- The goal: `/home/agent/work/apupiwe-review/goal.md` (criteria have ids like B2, C1, L3; C4 was added after the reviews ran).
- The reviews, all in `/home/agent/work/apupiwe-review/reports/`: `A3-compare.md` (three independent designs compared with the language), `A4-typology.md`, `A5-complexity.md`, `A6-factcheck.md` (with its helper files `A6-helper-*.md`), `A7-drift.md`. Ignore `A5-complexity-run1-contaminated.md`. The three designs `A1-design.md`, `A2-design.md`, `A8-design-zh.md` are background.
- The whole project: `/home/agent/work/repos/universal-language/` (reference `docs/language.md`, design notes `docs/rationale.md`, history `docs/design-log.md`, tests in `tests/`, word lists in `data/`, tools in `tools/`). You may read anything there and run its tools. Web search is allowed.

For every finding rated high or medium in any review (list them all, with the review and finding id), give:
- **Response:** concede / partly / defend.
- **Evidence:** what in the design, its tests or outside sources supports your response (cite file and section, or source). If you defend, show why the reviewer is wrong, not just that the design intended something.
- **If conceded:** the smallest change that would fix it, and what it would cost.
Also note any findings that contradict each other across reviews, and any finding that rests on a misreading of the language (quote the reference).

Write to `/home/agent/work/apupiwe-review/reports/B-defence.md`: a summary table at the top (finding, response), then the detail. Final report: counts of concede / partly / defend, and the five findings you think matter most.

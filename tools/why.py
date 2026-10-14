"""What does the project already say about a word, rule or idea? Run before proposing to add, change or
delete it (author, 2026-10-13), and cite what it finds.

  python tools/why.py ba            # every mention in the reasoning docs, with the line
  python tools/why.py "word order"

Searches the design log, rationale, goal, roadmap, vocabulary method, drift notes, the reference, research
notes and the cold review's verdict. A **bold** Apupiwe word is matched as a whole word.
"""
import glob, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DOCS = ["docs/design-log.md", "docs/rationale.md", "docs/goal.md", "docs/roadmap.md", "docs/vocabulary-method.md",
        "docs/drift.md", "docs/vocabulary-plan.md", "spec/reference.toml", "research/where-communication-fails.md",
        "research/reviews/cold-review-2026-10/reports/C-verdict.md"] + sorted(glob.glob("research/notes/*.md"))


def main(term):
    pat = re.compile(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", re.I)
    hits = 0
    for d in DOCS:
        p = os.path.join(ROOT, d)
        if not os.path.exists(p):
            continue
        for n, line in enumerate(open(p, encoding="utf-8"), 1):
            if pat.search(line):
                m = pat.search(line)
                a, b = max(0, m.start() - 160), m.end() + 220
                print(f"{d}:{n}: …{line[a:b].strip()}…")
                hits += 1
    print(f"\n{hits} mentions of '{term}'")


if __name__ == "__main__":
    main(" ".join(sys.argv[1:]))

# Roadmap

Agreed with the user 2026-10-10. The earlier roadmap (sections A–D) is done or
superseded; it's in git history and the design log.

**Why the project goes public:** to share it because it's cool, with people
who don't want a git repo or a markdown file. Others using or contributing is
a happy surprise, not a goal. It will later live on the user's own site,
skyseekerlabs.net, among other projects. So: a plain static site that can move
there by copying a folder, and no adoption or governance machinery.

## Order

1. **Consistency pass** (next):
   - **Separate the spec from its reasoning:** `language.md` states what the
     language *is*; why goes to `rationale.md`, history to the changelog
     (`design-log.md`).
   - **Mechanical checks:** every example passes `check.py`; the grammar
     table matches `grammar.tsv`; cross-references resolve.
   - **Fresh-eyes read** by a new agent, merged with the translators'
     ambiguity lists and `tests/regression-01/results.md`.
   - **Two piles:** clarifications, which Claude fixes and logs; design
     changes, which go to the user as one list.
   - **Learner guide** brought in line with the reference.
2. **Spec as structured source:** *2a done 2026-10-11:* `spec/reference.toml` (223 items with stable ids) generates `docs/language.md` (`tools/spec.py build/check/examples`). *2b done 2026-10-11:* `tools/parse.py`,
   a parser over grammar words that every example passes with one reading,
   and that lists readings to check "a precise way exists".
3. **Generated static site:** *built 2026-10-11 (`tools/site.py`, MkDocs Material, output in `build/site`); hosting not yet chosen.* reference, dictionary, learner guide
   (handwritten, examples checked), texts, design principles, changelog.
4. **Public:** licences checked first (Wiktionary-derived `offensive.tsv`
   is CC BY-SA, the CLICS-derived data CC BY), README, a short
   CONTRIBUTING ("work in progress, issues welcome"), GitHub repo, the site
   on GitHub Pages until skyseekerlabs.net exists.

**Deliberately not built,** each with an add-back trigger:
- a proof assistant: the parser misses contradictions;
- wiki software: non-git people want to edit;
- contribution governance: a real group forms;
- CI: the build is stable and the repo is public.

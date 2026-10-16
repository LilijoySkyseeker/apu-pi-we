# Short-word rebuild, rerun on today's setup (2026-10-15)

Question: the dry run (`tests/shortwords-02/`) rerun with what changed since, so the author can make Decision 2 (full rebuild, a middle option, or the minimal patch) and settle the name **apu pi we**. Task: `PROMPT.md`. Nothing outside this folder is changed.

## Progress (resume here)

- [x] copied `positions.py`, `rebuild.py` from shortwords-02 (its results untouched); rebuild.py: blocked = hard rule H5, matches = C3 tie-break, `SW_VARIANTS`/`SW_OVERRIDE`, `--lock`, `reopt`, `score`, `report name=file`
- [x] `positions.py` substitution rerun (15:17–15:52; `extend` added the UDHR frame the quote fix let through) → `substitution.tsv`, `frames.txt` (329 frames), `adjacency.tsv`, `corpus-counts.tsv`; `modmod.tsv`, `operators-extra.tsv`. Checked after the restart: complete (4,893 rows as in the dry run; the 4 bogus frames "1\" … "4\" gone, 11 new frames, one of them the UDHR quote frame).
- [x] restart (addendum): ENDEAR added: `positions.py endear` → `endear.tsv`; rebuild.py: word ENDEAR (freq 1.0), position P16, in every option (patch: forced into the change set like MODMOD). Runs of the stopped run (no ENDEAR) are void; `runs/patch-*-anneal.tsv`, `runs/patch-*-pol*.tsv` are leftovers from it.
- [ ] patch free / locked (200k steps per change set) — running
- [ ] full free / locked (12 seeds × 1.5M steps) — running
- [ ] keep sweep 0.02, 0.04 (+1) free / locked (12 seeds × 400k from the patch)
- [ ] hold-out check
- [ ] sensitivity
- [ ] drop test
- [ ] report, README

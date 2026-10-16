# Short-word rebuild, rerun on today's setup (2026-10-15)

Question: the dry run (`tests/shortwords-02/`) rerun with what changed since, so the author can make Decision 2 (full rebuild, a middle option, or the minimal patch) and settle the name **apu pi we**. Task: `PROMPT.md`. Nothing outside this folder is changed.

## Progress (resume here)

- [x] copied `positions.py`, `rebuild.py` from shortwords-02 (its results untouched); rebuild.py: blocked = hard rule H5, matches = C3 tie-break, `SW_VARIANTS`/`SW_OVERRIDE`, `--lock`, `reopt`, `score`, `report name=file`
- [x] `positions.py` substitution rerun (15:17–15:52; `extend` added the UDHR frame the quote fix let through) → `substitution.tsv`, `frames.txt` (329 frames), `adjacency.tsv`, `corpus-counts.tsv`; `modmod.tsv`, `operators-extra.tsv`. Checked after the restart: complete (4,893 rows as in the dry run; the 4 bogus frames "1\" … "4\" gone, 11 new frames, one of them the UDHR quote frame).
- [x] restart (addendum): ENDEAR added: `positions.py endear` → `endear.tsv`; rebuild.py: word ENDEAR (freq 1.0), position P16, in every option (patch: forced into the change set like MODMOD). Runs of the stopped run (no ENDEAR) are void; `runs/patch-*-anneal.tsv`, `runs/patch-*-pol*.tsv` are leftovers from it.
- [x] host crash ~16:26, resumed 21:00. Checked every file: all `runs/full-s1..12`, `full-lock-s1..12`, `mid-0.02-s1..12`, `mid-lock-0.02-s1..12`, `mid-0.04-s1`, `mid-lock-0.04-s1` have 71 lines and a "wrote" line in their log; `patch.tsv`, `patch-lock.tsv` complete (log ends "wrote", 16:14); `full.tsv`/`full-lock.tsv` picked (s9, lock s1). Killed mid-run: hold-out `-ha` batch (no files written). Since then rebuild.py writes layers atomically and `runs.sh`/`checks.sh` skip any command whose `--out` file exists, so a step is resumed by rerunning it.
- [x] patch free / locked (200k steps per change set)
- [x] full free / locked (12 seeds × 1.5M steps)
- [x] keep sweep 0.02, 0.04 from the patch (`runs.sh mid`): picked mid-0.02 = s11 (25 changes), mid-lock-0.02 = s2; mid-0.04 = s11 (14 changes), mid-lock-0.04 = the patch (all 12 seeds stuck). 11 of 12 free seeds at 0.04 and 6–7 of 12 at 0.02 never left the patch.
- [x] `FROM=0.02 KEEPS=0.04 runs.sh mid-alt` (0.04 also started from mid-0.02, added: is the patch a trap?): best from there 1.343 (free) / 1.359 (locked), worse than the patch-started picks, so mid-0.04 = s11 (14 changes) and mid-lock-0.04 = the locked patch stand. `KEEPS=0.01 runs.sh mid` (added third point: gap between 25 and 66 changes): mid-0.01 = s8 (34 changes), mid-lock-0.01 = s8.
- [ ] hold-out check: running `KEEPS="0.01 0.02 0.04" checks.sh holdout` (`logs/batch-holdout.log`; rerun the same command to resume) → `holdout.txt`
- [ ] sensitivity
- [ ] drop test
- [ ] report, README

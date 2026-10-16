#!/usr/bin/env bash
# Checks for the rerun (README.md "Checks"). From the repo root:  direnv exec . bash tests/shortwords-03/checks.sh STEP
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p runs logs
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P=${P:-15}
R="python3 rebuild.py"
# resumable (added after the host crash): a command whose --out file exists is skipped (rebuild.py writes atomically)
par() { while IFS= read -r c; do o=$(printf '%s\n' "$c" | sed -n 's/.*--out \([^ ]*\).*/\1/p'); [ -n "$o" ] && [ -f "$o" ] && continue; printf '%s\n' "$c"; done | xargs -P "$P" -I{} sh -c '{}'; }
# main model parameters (added: notes §7's biggest uncertainties and §6.5's candidates; glide_hiatus = front and back together)
SENS_PARAMS=${SENS_PARAMS:-"voice_mult L2_voicing_m reseg_n_V gem_n_N coda_loss coda_add glide_hiatus V_ratio L2_mid_m E_C C_none_after_vowel"}

case "$1" in
  sens)    # one-at-a-time sensitivity (notes §6.5): LAYER=file NAME=tag OPTS="reopt flags". Each parameter at its low and
           # high end in every v2 variant, re-optimised from the layer; controls: no override, seeds 1-3 (annealing noise)
    { for k in $SENS_PARAMS; do for v in low high; do
        echo "SW_OVERRIDE=$k=$v $R reopt --layer $LAYER $OPTS --steps ${STEPS:-100000} --seed 1 --out runs/sens-$NAME-$k-$v.tsv > logs/sens-$NAME-$k-$v.log 2>&1"
      done; done
      for s in 1 2 3; do
        echo "$R reopt --layer $LAYER $OPTS --steps ${STEPS:-100000} --seed $s --out runs/sens-$NAME-control-$s.tsv > logs/sens-$NAME-control-$s.log 2>&1"
      done; } | par ;;
  drop)    # drop test: LAYER NAME OPTS as for sens; re-optimise without src-av, without src-lp (and the control above)
    for vs in no-av no-lp; do for s in 1 2 3; do
      echo "SW_VARIANTS=$vs $R reopt --layer $LAYER $OPTS --steps ${STEPS:-100000} --seed $s --out runs/drop-$NAME-$vs-$s.tsv > logs/drop-$NAME-$vs-$s.log 2>&1"
    done; done | par ;;
  sens-score) # added: each option's layer scored at each parameter's low and high end (does the ranking hold?) -> sens-score.txt
    { $R score $LAYERS; for k in $SENS_PARAMS; do for v in low high; do SW_OVERRIDE=$k=$v $R score $LAYERS; done; done; } 2>/dev/null | grep '^SCORE' > sens-score.txt ;;
  holdout) # hold-out check (notes §6.6): each free option optimised on one half of the variants (half-a / half-b,
           # split in rebuild.py), then every layer scored on both halves -> holdout.txt. Resumable (runs.sh skips done runs).
    for H in a b; do SW_VARIANTS=half-$H TAG=-h$H bash runs.sh patch-free & done
    for H in a b; do SW_VARIANTS=half-$H TAG=-h$H bash runs.sh full-free; done
    wait
    for H in a b; do SW_VARIANTS=half-$H TAG=-h$H KEEPS="${KEEPS:-0.02 0.04}" bash runs.sh mid-free; done
    L=""; for H in a b; do for o in full mid-0.02 mid-0.04 patch; do L="$L $o-h$H.tsv"; done; done
    { for H in a b; do SW_VARIANTS=half-$H $R score $L full.tsv mid-0.02.tsv mid-0.04.tsv patch.tsv; done; } 2>/dev/null | grep '^SCORE' > holdout.txt ;;
  *) echo "unknown step $1"; exit 1 ;;
esac

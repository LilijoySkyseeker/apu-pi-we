#!/usr/bin/env bash
# Runs for the rerun (README.md). From the repo root:  direnv exec . bash tests/shortwords-03/runs.sh STEP
# Each annealing seed is its own process (as in the dry run: one seed per process, 12 in parallel, best kept).
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p runs logs
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1   # one core per process (added)
P=${P:-15}
R="python3 rebuild.py"
SEEDS=${SEEDS:-"1 2 3 4 5 6 7 8 9 10 11 12"}

par() { xargs -P "$P" -I{} sh -c '{}'; }

# best of a set of seed files by objective (header line) -> $1
pick() {
  out=$1; shift
  best=$(for f in "$@"; do echo "$(sed -n '1s/.*objective \([0-9.]*\).*/\1/p' "$f") $f"; done | sort -g | head -1 | cut -d' ' -f2)
  cp "$best" "$out"; echo "picked $best -> $out"
}

case "$1" in
  positions-extra)
    python3 positions.py modmod; python3 positions.py operators ;;
  patch)   # $VS variant set (default all); $TAG suffix
    # PSTEPS: annealing steps per minimum change set (added: 200k; the dry run's 6000 left the objective ~0.02 high)
    { echo "$R patch --steps ${PSTEPS:-200000} --out patch${TAG:-}.tsv > logs/patch${TAG:-}.log 2>&1"
      echo "$R patch --steps ${PSTEPS:-200000} --keep-words OF,ALL --out patch-lock${TAG:-}.tsv > logs/patch-lock${TAG:-}.log 2>&1"; } | par ;;
  full)    # full rebuild, free and locked; STEPS default 1500000 (dry run's full-c3)
    for s in $SEEDS; do
      echo "$R full --steps ${STEPS:-1500000} --seeds 1 --seed0 $s --out runs/full${TAG:-}-s$s.tsv > logs/full${TAG:-}-s$s.log 2>&1"
      echo "$R full --steps ${STEPS:-1500000} --seeds 1 --seed0 $s --lock OF,ALL --out runs/full-lock${TAG:-}-s$s.tsv > logs/full-lock${TAG:-}-s$s.log 2>&1"
    done | par
    pick full${TAG:-}.tsv runs/full${TAG:-}-s*.tsv; pick full-lock${TAG:-}.tsv runs/full-lock${TAG:-}-s*.tsv ;;
  mid)     # keep sweep from the patch: KEEPS="0.02 0.04"; 400k steps (dry run)
    for k in ${KEEPS:-0.02 0.04}; do for s in $SEEDS; do
      echo "$R full --keep $k --start patch${TAG:-}.tsv --steps ${STEPS:-400000} --seeds 1 --seed0 $s --out runs/mid-$k${TAG:-}-s$s.tsv > logs/mid-$k${TAG:-}-s$s.log 2>&1"
      echo "$R full --keep $k --start patch-lock${TAG:-}.tsv --lock OF,ALL --steps ${STEPS:-400000} --seeds 1 --seed0 $s --out runs/mid-lock-$k${TAG:-}-s$s.tsv > logs/mid-lock-$k${TAG:-}-s$s.log 2>&1"
    done; done | par
    for k in ${KEEPS:-0.02 0.04}; do
      pick mid-$k${TAG:-}.tsv runs/mid-$k${TAG:-}-s*.tsv; pick mid-lock-$k${TAG:-}.tsv runs/mid-lock-$k${TAG:-}-s*.tsv
    done ;;
  full-free)   # full rebuild, free only (hold-out, drop test); variant set from $SW_VARIANTS
    for s in $SEEDS; do
      echo "$R full --steps ${STEPS:-1500000} --seeds 1 --seed0 $s --out runs/full${TAG:-}-s$s.tsv > logs/full${TAG:-}-s$s.log 2>&1"
    done | par
    pick full${TAG:-}.tsv runs/full${TAG:-}-s*.tsv ;;
  mid-free)    # keep sweep, free only, from patch${TAG}.tsv
    for k in ${KEEPS:-0.02 0.04}; do for s in $SEEDS; do
      echo "$R full --keep $k --start patch${TAG:-}.tsv --steps ${STEPS:-400000} --seeds 1 --seed0 $s --out runs/mid-$k${TAG:-}-s$s.tsv > logs/mid-$k${TAG:-}-s$s.log 2>&1"
    done; done | par
    for k in ${KEEPS:-0.02 0.04}; do pick mid-$k${TAG:-}.tsv runs/mid-$k${TAG:-}-s*.tsv; done ;;
  patch-free)
    $R patch --steps ${PSTEPS:-200000} --out patch${TAG:-}.tsv > logs/patch${TAG:-}.log 2>&1 ;;
  *) echo "unknown step $1"; exit 1 ;;
esac
# hold-out check: SW_VARIANTS=half-a TAG=-ha bash runs.sh full-free | patch-free | mid-free, then
#   SW_VARIANTS=half-b python3 rebuild.py score ...   (and the reverse with half-b / -hb)
# drop test: SW_VARIANTS=no-av / no-lp with TAG=-noav / -nolp

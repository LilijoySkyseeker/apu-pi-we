#!/bin/sh
# g.sh REGEX: search the coverage index and coverage-02 candidates (ranks)
cd "$(dirname "$0")"
grep -iE "$1" coverage-index.tsv | cut -c1-160
grep -iE "^[0-9]+	[^	]*($1)" ../coverage-02/candidates.tsv | cut -f1-3,7 | head -8

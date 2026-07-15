#!/usr/bin/env bash
# movelog.sh — print candidate wiki/moves.log lines from git history.
#
# Mechanical helper for the move log (see schema/structure.md). It prints
# rename and delete events under wiki/, raw/, and designs/ since a given commit; the
# operator appends the relevant lines to wiki/moves.log and annotates delete
# tombstones with a disposition — the one judgment field:
#   (moved-to <path|peer::path>) | (merged-into <path>) | (superseded-by <path>) | (deleted)
#
# Usage: scripts/movelog.sh [<since-commit>]   # defaults to last 50 commits
set -euo pipefail
SINCE="${1:-HEAD~50}"
git log --reverse --date=short --pretty=format:'@%ad' --name-status \
    --diff-filter=RD -M "$SINCE"..HEAD -- wiki/ raw/ designs/ \
| awk '
  /^@/    { d=substr($0,2); next }
  /^R/    { printf "%s  moved    %s -> %s\n", d, $2, $3 }
  /^D/    { printf "%s  deleted  %s  (deleted)\n", d, $2 }
'

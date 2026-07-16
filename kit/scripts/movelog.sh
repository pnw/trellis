#!/usr/bin/env bash
# Print candidate move-log entries from Git history without modifying files.
# Usage: kit/scripts/movelog.sh [since-commit] [path ...]
set -euo pipefail

since="${1:-HEAD~50}"
if [[ $# -gt 0 ]]; then
  shift
fi
if [[ $# -gt 0 ]]; then
  paths=("$@")
else
  paths=("wiki")
fi

git log --reverse --date=short --pretty=format:'@%ad' --name-status \
  --diff-filter=RD -M "${since}"..HEAD -- "${paths[@]}" \
| awk '
  /^@/ { date=substr($0, 2); next }
  /^R/ { printf "%s  moved    %s -> %s\n", date, $2, $3 }
  /^D/ { printf "%s  deleted  %s  (deleted)\n", date, $2 }
'

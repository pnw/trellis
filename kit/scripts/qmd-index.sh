#!/usr/bin/env bash
# Optional local QMD index refresh for one or more content directories.
# Usage: kit/scripts/qmd-index.sh [directory ...]   # defaults to wiki
set -euo pipefail

root="$(git rev-parse --show-toplevel)"
cd "${root}"

qmd_version="2.5.3"
qmd=(npx --yes "@tobilu/qmd@${qmd_version}")
if [[ $# -gt 0 ]]; then
  directories=("$@")
else
  directories=("wiki")
fi

if [[ ! -f .qmd/index.yml ]]; then
  "${qmd[@]}" init
fi

for directory in "${directories[@]}"; do
  collection="$(basename "${directory}")"
  if ! "${qmd[@]}" collection show "${collection}" >/dev/null 2>&1; then
    "${qmd[@]}" collection add "${directory}"
  fi
done

"${qmd[@]}" update
if ! "${qmd[@]}" embed; then
  echo "qmd-index.sh: embeddings unavailable; lexical search remains usable" >&2
fi
"${qmd[@]}" status

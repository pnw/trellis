#!/usr/bin/env bash
# Idempotent local-search index refresh for wiki/ (Approach B2 in
# wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design.md).
#
# Safe to run repeatedly and from any environment: on first run it creates
# the local index and registers the wiki/ collection; on later runs it just
# re-syncs changed files. The index itself (.qmd/) is a derived, regenerable
# artifact and is gitignored, not committed — this script is the source of
# truth every agent/session reproduces identically.
#
# Embedding requires downloading models from huggingface.co. Where that host
# is blocked by network policy (observed in some sandboxed sessions), `qmd
# embed` fails and this script reports that but does not treat it as fatal:
# BM25 lexical search (`qmd search`) needs no downloaded model and still
# works. See wiki/agent-context/subtopics/retrieval/entities/qmd.md.
set -euo pipefail
cd "$(dirname "$0")/.."

QMD_VERSION="2.5.3"
QMD=(npx --yes "@tobilu/qmd@${QMD_VERSION}")

if [ ! -f .qmd/index.yml ]; then
  "${QMD[@]}" init
fi

if ! "${QMD[@]}" collection show wiki >/dev/null 2>&1; then
  "${QMD[@]}" collection add wiki
fi

"${QMD[@]}" update

if ! "${QMD[@]}" embed; then
  echo "qmd-index.sh: 'qmd embed' failed — semantic/hybrid search ('qmd query')" >&2
  echo "will be unavailable until it succeeds. This is commonly caused by" >&2
  echo "huggingface.co being unreachable under this environment's network" >&2
  echo "policy (models are hosted there), not a problem with the index itself." >&2
  echo "BM25 lexical search ('qmd search <query> -c wiki') still works with no" >&2
  echo "model download required. Fall back to Grep/Glob if qmd is unavailable" >&2
  echo "entirely." >&2
fi

"${QMD[@]}" status

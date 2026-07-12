# {{WIKI_NAME}} Wiki Agent Contract

This repository is a structured markdown wiki maintained by AI agents from immutable raw sources, instantiated from the Trellis wiki method (see `wiki-manifest.yaml` for upstream and pin). This file is the canonical cross-agent contract for every coding agent operating it — the instance owns this file; upstream changes to the method arrive via schema upgrades, not edits here.

## Goal

{{GOAL_SENTENCE — copy verbatim from wiki-manifest.yaml. This wiki has exactly one goal; content serving a different goal lives in a peer wiki and is cross-referenced.}}

## Core Rules

- Detailed schema reference lives in `schema/` (vendored from trellis): `page-format.md`, `page-types/`, `conventions.md`, `structure.md`, `ingest.md`, `lint.md`. `schema/` is normative; change it only via upstream sync or deliberate local divergence noted in the manifest.
- Never edit files under `raw/` in place — fidelity enables re-capture audits and change detection.
- Every substantive wiki claim traces to a raw source or source-capture page. Source-captures are source-isolated; contradictions are adjudicated downstream.
- `confidence` is derived, not asserted — ceiling comes from evidence tiers and independence of cited sources (`schema/page-format.md`). Wikis sharing an operator count as one source.
- Record every wiki/raw file move or delete in `wiki/moves.log` (tombstone dispositions; `scripts/movelog.sh` prints candidates). This wiki maintains only its outbound links; peer links use the `<peer>::` prefix per `schema/conventions.md`.
- Breadcrumbs over rails: workflows assume an agent with judgment; artifacts make judgment cheap and auditable, never replace it.

## Workflows

- **Ingest**: per `schema/ingest.md`; update `wiki/index.md` and append to `wiki/log.md` every time.
- **Query**: read `wiki/index.md` first; search `wiki/` directly; cite with wikilinks.
- **Lint**: `python3 scripts/lint.py` for the deterministic tier; judgment tier per `schema/lint.md`, including "does this content serve the goal?".
- **Upgrade**: run the canonical upgrade prompt from trellis `seed/interview.md` Step 3.

{{TOOL_ADAPTER_NOTES — CLAUDE.md wrapper, .kiro/ steering, etc., per the agents chosen in the manifest.}}

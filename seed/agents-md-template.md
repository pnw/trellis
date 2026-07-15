# {{WIKI_NAME}} Wiki Agent Contract

This repository is a structured markdown wiki maintained by AI agents from immutable raw sources, instantiated from the Trellis wiki method (see `wiki-manifest.yaml` for upstream and pin). This file is the canonical cross-agent contract for every coding agent operating it — the instance owns this file; upstream changes to the method arrive via schema upgrades, not edits here.

## Goal

{{GOAL_SENTENCE — copy verbatim from wiki-manifest.yaml. This wiki has exactly one goal; content serving a different goal lives in a peer wiki and is cross-referenced.}}

## Core Rules

- Detailed schema reference lives in `schema/` (vendored from trellis): `schema/wiki/` (`page-format.md`, `page-types/`, `conventions.md`, `ingest.md`, `lint.md`), `schema/structure.md`, and — if this instance carries the design surface — `schema/design/dossier.md`. `schema/` is normative; change it only via upstream sync or deliberate local divergence noted in the manifest.
- Never edit files under `raw/` in place — fidelity enables re-capture audits and change detection.
- Every substantive wiki claim traces to a raw source or source-capture page. Source-captures are source-isolated; contradictions are adjudicated downstream.
- `confidence` is derived, not asserted — ceiling comes from evidence tiers and independence of cited sources (`schema/wiki/page-format.md`). Wikis sharing an operator count as one source.
- Record every wiki/raw file move or delete (and design dossier-root move, where the design surface exists) in `wiki/moves.log` (tombstone dispositions; `scripts/movelog.sh` prints candidates). This wiki maintains only its outbound links; peer links use the `<peer>::` prefix per `schema/wiki/conventions.md`.
- Breadcrumbs over rails: workflows assume an agent with judgment; artifacts make judgment cheap and auditable, never replace it.
- Page creation follows the instigator tiers (`schema/wiki/page-types/registry.md`): source-captures at ingest, interpretive pages (construct, entity, synthesis, comparison, assessment) when their trigger fires — ingest is an occasion for interpretation, not a justification — and authored pages (decision, invariant) only on user instigation. Designs are not wiki pages: where the manifest sets `design_surface: true`, they live as `designs/{slug}/` dossiers per `schema/design/dossier.md` — lifecycle-governed, user-instigated, linked from wiki pages at dossier roots only. A dossier separates the target spec (`design.md`) from implementation scoping: live dossiers require `phases/phase-1.md`, `phases/later.md`, and `obligations.md` (`phases/` is a complete partition of the design's scope), and every dossier file carries a designed type from the surface's scoped vocabulary.

## Workflows

- **Ingest**: per `schema/wiki/ingest.md`, two-staged — Stage 1 captures the source (bounded, source-isolated, delegable); Stage 2 reviews vault-aware and routes per the instigator tiers. Update `wiki/index.md` and append to `wiki/log.md` every time.
- **Query**: read `wiki/index.md` first; search `wiki/` directly; cite with wikilinks.
- **Lint**: `python3 scripts/lint.py` for the deterministic tier; judgment tier per `schema/wiki/lint.md`, including "does this content serve the goal?".
- **Upgrade**: run the canonical upgrade prompt from trellis `seed/interview.md` Step 3.

{{TOOL_ADAPTER_NOTES — CLAUDE.md wrapper, .kiro/ steering, etc., per the agents chosen in the manifest.}}

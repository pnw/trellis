---
title: "Trellis: The Upstream Wiki-Method Repository"
type: design
description: Specification for Trellis, the new upstream repository holding the wiki method — normative schema, scripts, and instantiation seed as the distributable surface, plus a dogfood wiki whose subject is the method itself — with layout, governance, upgrade prompt, and bootstrap plan.
sources:
  - "[[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/designs/wiki-federation-and-inheritance]]"
  - "[[wiki/llm-wiki/designs/wiki-self-experimentation]]"
  - "[[wiki/llm-wiki/designs/project-wiki-template]]"
  - "[[wiki/llm-wiki/designs/project-wiki-application-guide]]"
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[wiki/llm-wiki/entities/open-knowledge-format]]"
tags: [llm-wiki, federation, portability, schema-design, meta-research, knowledge-management]
created: 2026-07-10
timestamp: 2026-07-10T18:00:00Z
confidence: low
novelty: exploratory
status: draft
---

# Trellis: The Upstream Wiki-Method Repository

Epistemic note: `confidence: low` — this specifies a repository that does not exist yet, grounded in owner-directed design conversations. Parent design: [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]] (problem statement, principles, federation rules); this page is the concrete repo specification.

## Name

**Trellis** — a deliberately light structure that guides growth without constraining it. Plants are trained along a trellis, not caged by it; the structure is cheap, visible, and prunable, and the growth it supports is the point. That is the breadcrumbs-over-rails principle as a physical object, and it names the relationship between the schema layer and the wikis that grow on it.

Naming context: **llm-wiki** remains the name of the researched pattern ([[wiki/llm-wiki/constructs/llm-wiki-pattern]], Karpathy's coinage) and **OKF** is Google's formalization ([[wiki/llm-wiki/entities/open-knowledge-format]]); Trellis is this practice's opinionated implementation lineage of that pattern — the thing a downstream wiki actually points at.

Alternates considered: *lattice* (structural but crystalline — implies rigidity and symmetry the method doesn't have), *rootstock* (the grafting/inheritance metaphor is apt but obscure, and collides with a blockchain project), *loom/warp* (schema as warp threads, content as weft — good metaphor, both names collide with well-known dev tools).

## Goal

One sentence, per the single-goal principle: **Develop and evidence the wiki method itself, through its own operation.**

Everything in the repo serves that goal. Research about *using* agents to build software lives downstream in `ai-research`; project-local knowledge lives in project wikis. Content that serves a different goal is reached by cross-wiki reference, never hosted.

## What Trellis Is — and Is Not

Trellis is a repository with two surfaces:

- **The distributable surface** — the normative schema, the scripts, and the instantiation seed. This is what downstream wikis vendor and follow breadcrumbs back to.
- **The lab** — a working wiki *about the method*, operating under the method, generating the operational evidence that justifies (or overturns) the norms.

Trellis is **not** a product, a framework, or a platform: no CLI, no SDK, no CI pipeline beyond lint, no runtime. The executor of every workflow — instantiation, upgrade, lint judgment tiers, reference checking — is an agent with judgment reading markdown. Tooling is added only when someone following a trail finds a marker missing (parent design, Phase 3).

## Repository Layout

```
trellis/
├── AGENTS.md               # contract for operating THIS wiki (the lab); not distributed
├── CLAUDE.md               # thin wrapper, as today
├── schema/                 # DISTRIBUTABLE — the normative layer
│   ├── page-format.md
│   ├── page-types/
│   │   ├── registry.md     # the full type vocabulary; the unit of subsetting is the file
│   │   ├── source-capture.md
│   │   ├── construct.md
│   │   ├── ... (one file per type)
│   │   └── invariant.md
│   ├── conventions.md
│   ├── structure.md
│   ├── ingest.md
│   └── lint.md
├── scripts/                # DISTRIBUTABLE — lint.py, qmd-index.sh, movelog.sh
├── seed/                   # DISTRIBUTABLE — instantiation layer
│   ├── interview.md        # the questionnaire skill an agent runs to create an instance
│   ├── manifest-template.yaml
│   ├── agents-md-template.md
│   └── pages/              # seed page templates (absorbs project-wiki-template)
├── wiki/                   # THE LAB — dogfood wiki; subject: the method
│   ├── index.md  log.md  moves.log  overview.md  roadmap.md
│   └── llm-wiki/ ...       # migrated topics, paths preserved
└── raw/                    # THE LAB — sources about the method
```

The boundary is directory-level and absolute: `schema/`, `scripts/`, `seed/` are what an instance inherits; `wiki/` and `raw/` are the lab and are reachable only by cross-wiki reference. `AGENTS.md` is per-instance (Trellis's own governs the lab; `seed/agents-md-template.md` is what instances start from and then own outright — resolving the parent design's open question: the contract is seeded, not inherited).

Migrated topics keep their current paths (`wiki/llm-wiki/`, and `wiki/agent-context/` if the owner confirms that disposition) — no renames during the move; any later restructuring goes through `moves.log` like any other move.

## Schema Governance

Per the parent design's Schema Governance section, applied here as operating rules for the lab:

- Schema files are normative and standalone — complete statements of the current rule, no back-references to rationale.
- Changes that weigh alternatives or rest on overturnable assumptions get a `decision` page in `wiki/llm-wiki/decisions/`; changes that don't, don't. Discovery is decision archaeology.
- Practice changes get hypothesis lines and verdicts per [[wiki/llm-wiki/designs/wiki-self-experimentation]], which moves here — its home is the method lab. (The rule of thumb separating the two artifacts: a hypothesis line has a revisit trigger; a decision page has weighed alternatives. A change can have both, either, or neither.)
- The wiki→schema direction is judgment only: lab findings motivate decisions, decisions change norms. No generation pipeline exists or is planned.

## Instantiation

An agent pointed at Trellis runs `seed/interview.md`: a short interrogate-then-confirm pass (goal statement first — an instance cannot exist without one; then page-type subset, link format, agent adapters, peers). The output is a new repository containing:

1. Vendored `schema/` (subsetted to the chosen types) and `scripts/`
2. `wiki-manifest.yaml` — the answers, persisted (format in the parent design)
3. Seed meta-pages from `seed/pages/` (index, overview with the goal stated, log, roadmap)
4. An `AGENTS.md` generated from the template, owned by the instance thereafter

## Upgrades

The canonical upgrade prompt, runnable by any downstream agent:

> Diff trellis `schema/` and `scripts/` from our pinned commit to upstream HEAD. Figure out what changed that matters for the slice this wiki uses (see `wiki-manifest.yaml`), apply it, run lint, bump the pin, and log what you did.

Trellis's obligations to make that cheap are exactly the three breadcrumbs: meaningful per-type file granularity (the diff reads by type), ordinary git history (plus whatever decision pages exist, for the "why"), and `wiki/moves.log` (forwarding addresses for anything that moved). No CHANGELOG contract, no migration notes, no version scheme beyond the commit SHA.

## Logs

Trellis runs the full three-log taxonomy from the parent design from day one — it is the method lab, so it dogfoods the method's own log design:

- `wiki/moves.log` — generated by `scripts/movelog.sh` from git rename/delete detection; tombstone dispositions (`moved-to`, `merged-into`, `superseded-by`, `deleted`) are the one judgment field, annotated when the move is made. Cross-repo departures use peer syntax in the disposition (e.g. a page leaving for a downstream wiki is tombstoned `moved-to <peer>::wiki/...`).
- `wiki/log.md` — the change journal, as today.
- `wiki/episodes.md` — optional narrative records, entry criteria per the parent design.

## Health

Two axes, per the parent design: **dogfood health** (continuous, first-party — the lab operating cleanly on a real research workload; genuine evidence, self-observed, capped at `medium`) and **instance health** (sparse, arms-length — instances existing, upgrades completing, downstream friction harvested as operational evidence; the only axis that can escape the cap). Neither substitutes for the other.

## Bootstrap Plan

One session's work, subsuming Phases 0–1 of the parent design's migration plan. Gate first: the owner decides the `wiki/agent-context/` disposition.

1. Owner creates the empty `trellis` repository.
2. Copy `schema/` and `scripts/` from `ai-research`; granulate `schema/page-types.md` into `schema/page-types/` during the copy (Phase 0 folded in); update `scripts/lint.py` for the new layout and the peer-link grammar (skip `::`-prefixed targets).
3. Write `seed/`: absorb [[wiki/llm-wiki/designs/project-wiki-template]] into `seed/pages/`, draft `interview.md` from [[wiki/llm-wiki/designs/project-wiki-application-guide]], add manifest and AGENTS.md templates.
4. Move lab content per the disposition table: `wiki/llm-wiki/` (plus `agent-context/` if confirmed), the `raw/` files their captures cite, and `raw/repos/` snapshots. Plain copies (cross-repo moves don't preserve git history); provenance is recorded instead — Trellis's first `log.md` entry states origin repo and commit, and `ai-research`'s new `moves.log` tombstones every departed page with `moved-to trellis::...`.
5. Write Trellis's wiki meta-files: `overview.md` stating the goal, fresh `index.md`, `log.md`, `roadmap.md` (carrying over the meta-experiment lines that belong to method practice), empty `moves.log`.
6. In `ai-research`: add `wiki-manifest.yaml` (instance #1, pinned to the bootstrap commit), rewrite links to departed pages as `trellis::`-prefixed, run lint in both repos to 0 errors.
7. Open one meta-experiment line in each repo: Trellis — "does the lab sustain a real workload post-split?"; ai-research — "does practice work accelerate once the meta-goal has moved out?"

## Open Questions

- Name confirmation — Trellis, or one of the alternates.
- `wiki/agent-context/` disposition (inherited from the parent design; gates bootstrap step 4).
- Does Trellis's dogfood wiki eventually want a `trellis` topic distinct from `llm-wiki` (method-specific designs vs. pattern research), or do the migrated topic paths stay indefinitely? Defer — a future move is cheap once `moves.log` exists.
- Should `seed/interview.md` also emit the SessionStart hook / `.claude` settings as an optional adapter, mirroring what `ai-research` runs today? Probably yes, as one interview question.

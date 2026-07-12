---
title: Trellis Repository Bootstrap Decisions
type: decision
description: "The repo-shape choices made when bootstrapping the upstream repository: the name Trellis, the two-surface layout, seeded rather than inherited AGENTS.md, path-preserving migration, and plain-copy provenance."
sources:
  - "[[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/decisions/adopt-single-goal-federation]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[wiki/llm-wiki/designs/wiki-federation-and-inheritance]]"
  - "[[wiki/llm-wiki/designs/trellis-repo-design]]"
tags: [llm-wiki, federation, portability, schema-design, knowledge-management]
created: 2026-07-12
timestamp: 2026-07-12T07:00:00Z
status: stable
---

# Trellis Repository Bootstrap Decisions

The concrete repo-shape choices behind this repository, extracted from the bootstrap blueprint ([[wiki/llm-wiki/designs/trellis-repo-design]], now deprecated) when the bootstrap executed and the design died into this record per [[wiki/llm-wiki/decisions/designs-die-into-decisions]].

## Context

The federation decision ([[wiki/llm-wiki/decisions/adopt-single-goal-federation]]) required an upstream repository to exist: a home for the normative schema, the scripts, the instantiation seed, and the method lab. The owner's review of the federation design closed with the directive to design and name that repository ([[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]). The blueprint's spec is now embodied by the repository itself and `AGENTS.md`; the choices that shaped it are recorded here.

## Decision

1. **The name is Trellis** — a deliberately light structure that guides growth without constraining it. Plants are trained along a trellis, not caged by it; the structure is cheap, visible, and prunable, and the growth it supports is the point. That is the breadcrumbs-over-rails principle as a physical object. Naming context: **llm-wiki** remains the name of the researched pattern ([[wiki/llm-wiki/constructs/llm-wiki-pattern]], Karpathy's coinage), **OKF** is the spec name ([[wiki/llm-wiki/entities/open-knowledge-format]]); Trellis is this practice's opinionated implementation lineage of the pattern — the thing a downstream wiki actually points at.
2. **Two-surface layout.** The distributable surface (`schema/`, `scripts/`, `seed/`) is what downstream instances vendor and follow breadcrumbs back to; the lab (`wiki/`, `raw/`) is the dogfood wiki whose subject is the method and is reachable only by cross-wiki reference. The boundary is directory-level and absolute — inheritance pulls the former and must never pull the latter.
3. **AGENTS.md is seeded, not inherited.** Trellis's own `AGENTS.md` governs only the lab and is not distributed. Instances generate theirs from `seed/agents-md-template.md` at instantiation and own it outright thereafter — the contract is per-instance state, not upstream-tracked schema.
4. **Migrated topics keep their paths.** Content moved from `ai-research` retains its directory paths (`wiki/llm-wiki/`, `wiki/agent-context/`) — no renames during the move. Any later restructuring goes through `wiki/moves.log` like any other move, which is cheap once the log exists.
5. **Plain-copy migration with recorded provenance.** Cross-repo moves are plain copies, not history-preserving git surgery. Provenance is recorded instead: Trellis's first `wiki/log.md` entry states the origin repo and commit, and ai-research tombstones every departed page in its `wiki/moves.log` with a `moved-to trellis::...` forwarding address.

## Alternatives Considered

- **Names**: *lattice* (structural but crystalline — implies rigidity and symmetry the method doesn't have), *rootstock* (the grafting/inheritance metaphor is apt but obscure, and collides with a blockchain project), *loom* / *warp* (schema as warp threads, content as weft — good metaphor, but both names collide with well-known dev tools).
- **Inherited AGENTS.md** — track the agent contract as distributable upstream content. Rejected: the contract encodes per-instance goal, workflows, and local facts; upstream tracking would either constrain instances or force a merge protocol (a rail). Seeding resolves the parent design's open question.
- **History-preserving migration** (subtree/filter-branch imports) — rejected: hostile ergonomics for a one-time move, and the provenance need is fully met by a log entry plus tombstones, which is the mechanism downstream wikis must exercise anyway.

## Consequences

- The repository exists as specified: bootstrap executed 2026-07-12 (commit `a08dbb3`), subsuming Phases 0–1 of the federation design's migration plan — schema granulated into `schema/page-types/` during the copy, `seed/` written, lab content moved, both repos linting clean.
- The distributable/lab boundary gives the upgrade prompt a clean referent: downstream diffs touch only `schema/` and `scripts/`.
- The blueprint design page is deprecated; the repo layout is documented by the repo itself and `AGENTS.md`, and this page holds the rationale.

## Invariants Established

None registered as pages. The directory-level distributable/lab boundary is a standing constraint, but its invariant page is deferred alongside the federation invariants ([[wiki/llm-wiki/decisions/adopt-single-goal-federation]], Invariants Established) until the split settles; the boundary rule lives normatively in `AGENTS.md` and `schema/structure.md`.

## Status

`stable` — accepted and executed 2026-07-12. Supersede with a new decision for any change to the name, the two-surface boundary, or the seeded-contract model.

## Related Artifacts

- [[wiki/llm-wiki/decisions/adopt-single-goal-federation]] — the founding split decision this one implements
- [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]] — the live federation design
- [[wiki/llm-wiki/designs/trellis-repo-design]] — the deprecated bootstrap blueprint this record replaced

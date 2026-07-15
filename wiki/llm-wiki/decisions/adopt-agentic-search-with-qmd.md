---
title: Adopt Agentic Search with QMD for Wiki Retrieval
type: decision
description: Chose grep-based agentic search as this wiki's default retrieval, with QMD-style local hybrid search as the graduation path — over embedding-RAG infrastructure and over building a bespoke index or MCP schema.
sources:
  - "[[designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/qmd]]"
related:
  - "[[designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]]"
  - "[[ai-research::wiki/intent-compiler/constructs/process-weights]]"
tags: [agent-context, retrieval, knowledge-management, tooling]
created: 2026-07-08
timestamp: 2026-07-08T03:00:00Z
status: stable
---

# Adopt Agentic Search with QMD for Wiki Retrieval

## Context

The wiki crossed ~100 pages (129 at time of writing), the threshold [[designs/knowledge-surfacing-design]] had named for graduating beyond a flat `index.md`. That page originally proposed building a `wiki/by-tag.md` and eventually a bespoke MCP meta-tool server or compiled typed-edge graph. Research done at the threshold ([[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]]) changed the picture: the real-world graduation path from a flat markdown wiki is grep-based agentic search first, then an off-the-shelf local hybrid-search tool — not custom index infrastructure. Multiple agents (Claude Code, Kiro, Codex) work in this repo, so whatever was chosen needed to be reproducible from committed config, not dependent on one environment's ad-hoc state.

## Decision

1. **Default retrieval is [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]** — `Grep`/`Glob`/`Read` directly over `wiki/`, no generated index beyond the existing `index.md`.
2. **Graduation path is QMD-style local hybrid search (Approach B2)**, implemented now via `scripts/qmd-index.sh` (pinned `qmd@2.5.3`, idempotent, gitignored `.qmd/`), wired into the cross-agent Ingest and Query workflows plus a Claude Code `SessionStart` hook.
3. **The Query Workflow is "try `qmd search`/`qmd query`, fall back to `Grep`/`Glob`"** — qmd is an optimization, never a dependency.

This was a *deliberate early build* of B2, ahead of the "wait for an observed agentic-search failure" trigger the design page itself records, made because the infrastructure is cheap and multi-agent reproducibility mattered more than waiting for proof of need.

## Alternatives Considered

- **Embedding-RAG (vector DB, chunking pipeline)** — rejected: this is what Anthropic removed from Claude Code for staleness, permission, and reliability reasons; overkill at this scale and adds a maintenance surface. Note the industry is actually *hybrid*, not anti-embedding (see the comparison page) — embeddings weren't rejected as worthless, just as the wrong first tool here.
- **Bespoke MCP meta-tool server / compiled typed-edge graph** — rejected for now: no real-world markdown-wiki-scale precedent found; high build-and-maintain cost; better suited to large heterogeneous *tool* libraries than a *document* corpus.
- **Build `wiki/by-tag.md`** (the design's original Approach A step) — rejected: superseded by BM25/hybrid search, which covers the cross-cutting-query need a generated tag index was meant to solve.
- **Wait for the stated trigger before building anything** — considered and consciously overridden by the owner; recorded as an exception to that invariant, not a silent one.

## Consequences

- Zero-maintenance default (agentic search) with a cheap, reproducible upgrade already in place.
- A real environment limitation surfaced and is documented: `qmd embed`/`qmd query` (semantic/hybrid) fail where `huggingface.co` is blocked by network policy; `qmd search` (BM25) works with no download. In such environments effective retrieval is BM25-plus-grep, not full hybrid. See [[wiki/agent-context/subtopics/retrieval/entities/qmd]].
- Building B2 ahead of the trigger is a one-time sanctioned exception to knowledge-surfacing-design's Invariant 5; overriding that invariant should stay a conscious, recorded choice rather than a habit — this decision is that record.
- If agentic search later demonstrably misses real queries, the hybrid layer is already wired and just needs a working model download.

## Status

`stable` (accepted, 2026-07-08). Supersede this decision if the wiki adopts a fundamentally different retrieval approach (e.g. a compiled graph) rather than merely turning on qmd's semantic layer.

## Related Artifacts

- [[designs/knowledge-surfacing-design]] — the design and its Implementation section
- [[wiki/agent-context/subtopics/retrieval/comparisons/coding-agent-retrieval-architectures]] — the vendor evidence behind the choice
- [[ai-research::wiki/intent-compiler/constructs/process-weights]] — the ceremony-scaling principle that made "don't overbuild" the default

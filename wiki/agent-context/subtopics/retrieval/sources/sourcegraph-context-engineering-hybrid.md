---
title: Sourcegraph — Context Engineering and Hybrid Retrieval
type: source-capture
evidence: vendor-claim
description: Sourcegraph's own framing that hybrid retrieval (grep, embeddings, and structural code-graph indexing selected per query type) is where enterprise coding-agent tools converged in 2026, directly contradicting a separate claim that Sourcegraph Amp "dropped vectors."
sources:
  - "[[raw/articles/sourcegraph-context-engineering-hybrid.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]]"
tags: [agent-context, retrieval, coding-agents, embeddings]
created: 2026-07-07
timestamp: 2026-07-07T22:00:00Z
status: draft
---

# Sourcegraph — Context Engineering and Hybrid Retrieval

## Source Identity

- Publisher: Sourcegraph (official blog and resources pages)
- URLs: sourcegraph.com/blog/context-engineering, sourcegraph.com/resources/context-compare, sourcegraph.com/blog/why-code-search-at-scale-is-essential-when-you-grow-beyond-one-repository
- Retrieved via WebSearch aggregation; direct fetch returned HTTP 403 in this session.

## Core Contribution

Frames the 2026 industry consensus on coding-agent retrieval as hybrid — combining grep, embeddings, and structural/graph indexing selected by query type — rather than a wholesale move away from embeddings, and describes Sourcegraph Amp's own architecture as built on SCIP-based structural code-graph indexing.

## Key Claims

- "Hybrid is the path most enterprise tools converge on" as of 2026; cites Cursor's own docs describing side-by-side "Instant Grep" and semantic search, agent-selected per query shape.
- Sourcegraph Amp (the agentic evolution of Cody) layers an agent atop Sourcegraph's code graph, backed by SCIP indexing — a static-analysis/structural indexing approach distinct from both raw grep and embeddings-based semantic search.
- Teams adopting Amp get this code graph "by default," positioned as a production-grade context layer for coding agents on large codebases.

## Evidence and Results

This is vendor positioning content (a company whose core product is code search describing why code search/graph indexing matters), not an independent study. The specific technical claim about SCIP-based indexing is a factual, checkable architecture description; the "hybrid is where the industry converged" framing is an interpretive claim serving Sourcegraph's own product narrative.

## Limitations and Caveats

- As Sourcegraph's own commercial content, the framing has an obvious interest in favoring structural/graph indexing (its own product) over the simpler grep-only story favored elsewhere.
- Could not be independently fetched in this session; reconstructed from WebSearch synthesis.

## Reliability Notes

Tiered `vendor-claim`: commercially motivated content from a vendor whose product is the thing being favorably framed. Notably, this source's *specific factual claims* about Cursor's hybrid architecture align with Cursor's own official documentation ([[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]]), which is independent corroboration for that particular claim even though the source itself is not neutral.

## Important References and Linked Material

- Cursor's own hybrid-architecture documentation: [[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]]

## Contribution Routing

- Directly contradicts, with a named counter-example (Cursor), the "vectors are dead" framing found in [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]'s secondary aggregation. Adjudicated in [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]], not here (source isolation).

## Extraction Notes

Built from WebSearch snippet synthesis across three distinct Sourcegraph URLs; not verified against the original pages directly.

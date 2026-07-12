---
title: Windsurf (Codeium) — Fast Context Indexing Architecture
type: source-capture
evidence: expert-analysis
description: Third-party technical coverage describing Windsurf's "Fast Context" system as embeddings-based RAG over locally-generated, incrementally-updated indexes — contradicting a separate secondary claim that Windsurf dropped vector search.
sources:
  - "[[raw/articles/windsurf-fast-context-architecture.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]"
tags: [agent-context, retrieval, coding-agents, embeddings]
created: 2026-07-07
timestamp: 2026-07-07T22:00:00Z
status: draft
---

# Windsurf (Codeium) — Fast Context Indexing Architecture

## Source Identity

- No single canonical Codeium documentation page was independently fetched in this session; this capture aggregates multiple third-party review/guide sites converging on the same technical description (Fast Context, local embeddings, incremental updates).

## Core Contribution

Describes Windsurf's "Fast Context" indexing system: local generation of embeddings for files, functions, classes, and type definitions, incrementally updated, feeding a RAG-style retrieval layer for its Cascade agent.

## Key Claims

- On opening a project, Windsurf generates embeddings for files/functions/classes/type-definitions and stores the index locally, updated incrementally.
- Retrieval is described as RAG: indexing the repository and using embeddings to find relevant code for a task, branded "Fast Context."
- Cascade additionally tracks recent actions (edits, terminal commands, linter warnings) for "flow-aware" context.
- Reported to regularly use 70-90% CPU on codebases over ~50K lines.

## Evidence and Results

No comparative benchmark was found; claims are architectural description from third-party coverage, not a primary vendor benchmark.

## Limitations and Caveats

- Aggregated from multiple third-party marketing/review sites (aiagentsquare.com, pinklime.io, and similar), not Codeium's own documentation directly — weaker provenance than a vendor's own docs page.
- The CPU-usage figure is anecdotal and unsourced beyond the aggregation.

## Reliability Notes

Tiered `expert-analysis` rather than `official-docs`: despite describing an official product, the underlying sources here are third-party write-ups rather than Codeium's own documentation, which this session could not directly fetch. Multiple independent write-ups converge on the same "Fast Context = local embeddings + RAG" description, which is reasonable corroboration for that specific claim, but not equivalent to a vendor-primary source.

## Important References and Linked Material

- None independently verified beyond the aggregated review sites listed in the raw capture.

## Contribution Routing

- Directly contradicts the claim (from a different single source) that Windsurf "dropped vectors" for pure grep-based search — see the adjudication in [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]].

## Extraction Notes

Built entirely from WebSearch snippet synthesis across several third-party sites; no primary Codeium documentation was reachable in this session.

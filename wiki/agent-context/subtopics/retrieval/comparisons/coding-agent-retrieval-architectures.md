---
title: Coding Agent Retrieval Architectures — A Vendor Comparison
type: comparison
description: How Claude Code, Cursor, Windsurf, GitHub Copilot, Sourcegraph Amp, and OpenAI Codex CLI actually retrieve code context in 2026 — correcting an overstated "industry abandoned embeddings" framing with vendor-documented architectures.
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/windsurf-fast-context-architecture]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/github-copilot-embedding-model-2026]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/sourcegraph-context-engineering-hybrid]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
  - "[[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/qmd]]"
tags: [agent-context, retrieval, coding-agents, embeddings]
created: 2026-07-07
timestamp: 2026-07-07T22:15:00Z
confidence: medium
status: draft
---

# Coding Agent Retrieval Architectures — A Vendor Comparison

## Comparison Question

When a request in this wiki asked whether "the industry, including Anthropic's own Claude Code, moved away from embeddings/MCP-schema complexity toward plain grep-based agentic search," an initial research pass captured that claim from a single aggregated secondary source without checking each named vendor's own documentation. This page does that check: how does each major coding agent actually retrieve code context, according to its own vendor material rather than a single blog's summary?

## Summary

The original claim was **overstated**. Anthropic's move away from embeddings in Claude Code is real and well-corroborated for Claude Code specifically. It is not a general industry trend: Cursor, Windsurf, and GitHub Copilot are all embeddings-first in their own documentation, and Sourcegraph Amp uses structural code-graph indexing (SCIP), not grep. The actual 2026 consensus, per Sourcegraph's own framing (itself a vendor with reason to favor its own approach, but corroborated independently by Cursor's own docs), is **hybrid retrieval** — grep for exact matches, embeddings or graph indexing for conceptual/structural queries, selected per query shape — with Claude Code as a genuine but unusually pure-grep outlier rather than the norm.

## Comparison Table

| System | Primary Mechanism | Embeddings Used? | Notable Detail |
|---|---|---|---|
| **Claude Code** | Agentic search (glob/grep/read) | No | Anthropic removed vector search in May 2025; reported to have "outperformed everything." [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]] |
| **Cursor** | Hybrid — "Instant Grep" + semantic search | Yes | Merkle-tree change detection feeds chunk embeddings in a dedicated vector DB (Turbopuffer); agent picks grep vs. semantic per query shape; 12.5% accuracy gain claimed from semantic search specifically. [[wiki/agent-context/subtopics/retrieval/sources/cursor-codebase-indexing-docs]] |
| **Windsurf (Codeium)** | Embeddings-first RAG ("Fast Context") | Yes | Local embeddings for files/functions/classes/types, incrementally updated; no grep-first framing found in vendor-adjacent coverage. [[wiki/agent-context/subtopics/retrieval/sources/windsurf-fast-context-architecture]] |
| **GitHub Copilot** | Embeddings-first with lexical fallback | Yes | Calls an embeddings API for diffs under 300 files (8s timeout, falls back to TF-IDF); skips embeddings entirely for 301-2,000-file diffs. Adaptive by scale, not grep-first. [[wiki/agent-context/subtopics/retrieval/sources/github-copilot-embedding-model-2026]] |
| **Sourcegraph Amp** | Structural code-graph (SCIP indexing) | No (uses static-analysis graph instead) | Neither pure grep nor embeddings — a third category, precise symbol/reference indexing via long-standing Sourcegraph code-search infrastructure. [[wiki/agent-context/subtopics/retrieval/sources/sourcegraph-context-engineering-hybrid]] |
| **OpenAI Codex CLI** | Filesystem-first agentic (reads working directory, builds context, plans) | Unclear/not confirmed | Consistent in spirit with agentic search, but this research pass found no explicit statement on embeddings use one way or the other — treat as unconfirmed, not corroborating either claim. |

## When Each Approach Wins

- **Pure agentic search (Claude Code)**: cheapest to build and maintain; strongest evidence base is source-code corpora with high identifier/filename overlap with likely queries, at scale (large codebases), where staleness and permission complexity of an embedding pipeline were the stated reasons for abandoning it.
- **Embeddings-first (Windsurf, GitHub Copilot)**: favored when conceptual/semantic queries ("where do we handle authentication retries?") are common and don't share vocabulary with the code itself.
- **Hybrid, query-shape-selected (Cursor)**: the vendor with the most explicit, documented dual-mode design — grep for exact symbols, embeddings for concepts.
- **Structural/graph indexing (Sourcegraph Amp)**: favored when precise symbol/reference relationships (call graphs, cross-repository references) matter more than either lexical or semantic similarity.

## Failure Modes

- Treating any single vendor's design choice as "the industry direction" without checking others — the specific failure this page exists to correct.
- Assuming a technique validated on large, actively-changing source-code repositories (millions of tokens, thousands of files) transfers unchanged to a much smaller, prose-heavy markdown knowledge base like this wiki (currently ~124 pages) — the corpus properties (code identifiers and imports vs. natural-language descriptions and tags) differ enough that the same conclusion shouldn't be assumed without checking.
- Citing a single aggregated secondary source for a multi-vendor claim, as the initial capture in this research pass did — corrected here by checking vendor-level sources directly, though even these remain WebSearch-aggregated rather than independently fetched (see each source's Extraction Notes) and warrant a future direct-fetch verification pass.

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] — the construct this page corrects the evidentiary scope of
- [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] — where this wiki's own retrieval strategy is decided
- [[wiki/agent-context/subtopics/retrieval/entities/qmd]] — notably itself a hybrid (BM25 + vector + rerank) tool, consistent with the hybrid consensus found here rather than a pure-grep one

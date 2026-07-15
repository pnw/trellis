---
title: Cursor — Semantic & Agentic Search (Official Docs)
type: source-capture
evidence: official-docs
description: Cursor's official documentation on codebase indexing, describing a hybrid architecture combining Merkle-tree-synced embeddings (Turbopuffer vector search) with grep-based "Instant Grep," selected per query shape — not a pure grep/agentic-search design.
sources:
  - "[[raw/articles/cursor-codebase-indexing-docs.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]"
tags: [agent-context, retrieval, coding-agents, embeddings]
created: 2026-07-07
timestamp: 2026-07-07T22:00:00Z
status: draft
---

# Cursor — Semantic & Agentic Search (Official Docs)

## Source Identity

- Publisher: Cursor (official documentation)
- URL: https://cursor.com/docs/context/codebase-indexing
- Retrieved via WebSearch aggregation; direct fetch returned HTTP 403 in this session.

## Core Contribution

Documents Cursor's codebase indexing architecture: a Merkle-tree change-detection system feeding chunk-level embeddings stored in a dedicated vector database (Turbopuffer), used alongside grep-based exact-match search, with the agent choosing which to use per query.

## Key Claims

- Cursor computes a Merkle tree of file hashes to detect changes; changed files are re-chunked and re-embedded, with unchanged chunks served from cache.
- Embeddings and metadata (not source code) are stored in Turbopuffer; source code stays local, with client-side file-path obfuscation before any metadata transmission.
- Cursor's own evaluation reports semantic search improves response accuracy by 12.5% on average and increases the retention rate of agent-produced code changes.
- The documentation page is titled "Semantic & Agentic Search," describing both an "Instant Grep" mode (exact symbols) and semantic search (conceptual queries), with the agent selecting based on query shape.

## Evidence and Results

The 12.5% accuracy figure is Cursor's own reported internal evaluation; no external replication was found in this research pass. As official documentation, the architectural description (what Cursor does) is more authoritative than the effectiveness claim (how much better it performs).

## Limitations and Caveats

- Direct fetch of the docs page was not possible in this session; content is reconstructed from WebSearch summaries of the page and corroborating third-party technical write-ups (Towards Data Science, Engineer's Codex), not verified against the raw page HTML.
- The 12.5% figure lacks a disclosed benchmark methodology in what could be recovered here.

## Reliability Notes

Tiered `official-docs`: authoritative for what Cursor's retrieval architecture actually is (design-intent), which is the load-bearing claim for this capture. The effectiveness claim (12.5% improvement) is a vendor's self-reported number and should be weighted accordingly — see the scoped-claims rule in `schema/wiki/page-format.md`.

## Important References and Linked Material

- Cursor's companion blog post on secure indexing: https://cursor.com/blog/secure-codebase-indexing (not independently fetched)

## Contribution Routing

- Directly corrects the framing in [[wiki/agent-context/subtopics/retrieval/sources/claude-code-agentic-search-vs-rag]]'s secondary-source claim that Cursor "dropped vectors" — Cursor's own documentation shows a hybrid architecture, not an embeddings-free one. This adjudication belongs in [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]], not in either source-capture (source isolation).

## Extraction Notes

Built from WebSearch snippet synthesis; the Merkle-tree/Turbopuffer architectural description is corroborated across multiple independent secondary write-ups converging on the same technical details, which increases confidence in the WebSearch synthesis's accuracy despite the lack of a direct fetch.

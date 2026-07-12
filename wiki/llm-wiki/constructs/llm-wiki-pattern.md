---
title: LLM Wiki Pattern
type: construct
description: A knowledge management pattern where an LLM agent builds and maintains a structured markdown wiki from raw sources. Introduced by Karpathy, April 2026.
sources:
  - "[[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]]"
  - "[[wiki/llm-wiki/sources/open-knowledge-format-spec]]"
related:
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[wiki/llm-wiki/comparisons/llm-wiki-vs-rag]]"
  - "[[wiki/llm-wiki/entities/andrej-karpathy]]"
  - "[[wiki/llm-wiki/entities/open-knowledge-format]]"
tags: [llm-wiki, knowledge-management, agents, curation]
created: 2026-04-16
timestamp: 2026-07-04T21:23:00Z
confidence: medium
novelty: emerging
coined_by: "Andrej Karpathy (April 2026)"
---

# LLM Wiki Pattern

## Definition

A knowledge management pattern where an LLM agent builds and maintains a structured markdown wiki from raw source documents. Humans curate what sources go in. The LLM handles all organization, cross-referencing, summarization, and maintenance.

> "The LLM writes and maintains all of the data of the wiki. I rarely touch it directly." — Andrej Karpathy

## Why It Matters

Knowledge bases collapse because maintenance cost is too high. Building one has three steps: **collect** (easy), **organize** (hard), **maintain** (impossible at scale). LLMs are uniquely good at the bookkeeping — filing, cross-referencing, summarizing, updating, flagging contradictions — tirelessly and at near-zero marginal cost.

## Mechanism / Structure

Uses a [[wiki/llm-wiki/constructs/three-layer-architecture]]:
1. `raw/` — Immutable source documents (never modified by the LLM)
2. `wiki/` — LLM-generated and maintained markdown pages
3. Schema file — Defines structure, conventions, and workflows

Three core operations (compiler analogy):
- **Ingest** — Process new sources into wiki pages. A single ingest can cascade updates across 10-15+ related pages.
- **Query** — Ask questions; LLM navigates via index, reads targeted pages, synthesizes answers with citations. Valuable answers get saved as new pages.
- **Lint** — Health checks for contradictions, orphan pages, missing concepts, stale claims.

## Distinctions

- Not a RAG system (see [[wiki/llm-wiki/comparisons/llm-wiki-vs-rag]]) — pre-compiles knowledge rather than retrieving at query time
- Not a traditional wiki — the LLM is the author, the human is the curator
- A pattern, not a product — works with any sufficiently capable LLM and any markdown-aware tooling
- Scale sweet spot: 50-200 sources. Beyond this, consider LLM Wiki v2 extensions or RAG.

## Evidence and Sources

- Karpathy's wiki: ~100 articles, ~400,000 words on a single topic
- 16M+ views on X, 5,000+ GitHub Gist stars
- Multiple community implementations within a week
- Formalized as [[wiki/llm-wiki/entities/open-knowledge-format]] by Google (June 2026)

## Related Artifacts

- [[wiki/llm-wiki/constructs/three-layer-architecture]] — the structural foundation
- [[wiki/llm-wiki/comparisons/llm-wiki-vs-rag]] — comparison with RAG
- [[wiki/llm-wiki/entities/andrej-karpathy]] — creator
- [[wiki/llm-wiki/entities/open-knowledge-format]] — formal specification
- [[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]] — primary source

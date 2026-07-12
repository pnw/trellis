---
title: LLM Wiki vs RAG
type: comparison
description: Comparison of the LLM Wiki pattern vs RAG — LLM Wiki wins at personal/team scale, RAG wins at enterprise scale.
sources:
  - "[[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]]"
related:
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
tags: [llm-wiki, rag, knowledge-management]
created: 2026-04-16
timestamp: 2026-07-04T21:23:00Z
confidence: low
---

# LLM Wiki vs RAG

## Comparison Question

When should you use an LLM Wiki (pre-compiled markdown knowledge base) vs. RAG (retrieval-augmented generation)?

## Summary

The [[wiki/llm-wiki/constructs/llm-wiki-pattern]] is a simpler alternative to RAG for personal/team-scale knowledge. It is essentially a **manual, traceable implementation of Graph RAG** without the infrastructure. RAG wins at enterprise scale; LLM Wiki wins at personal/team scale.

## Comparison Table

| Dimension | RAG | LLM Wiki | Implication |
|---|---|---|---|
| State | Stateless — each query independent | Stateful — knowledge compounds over time | LLM Wiki improves with use |
| Infrastructure | Vector DB, embedding pipeline, retrieval logic | Folder of `.md` files | LLM Wiki: zero infrastructure |
| Cross-references | Discovered ad-hoc per query | Pre-built by the LLM, always available | LLM Wiki: always-available graph |
| Maintenance | Embedding updates, index rebuilds | LLM updates pages on every ingest | LLM Wiki: maintenance is built-in |
| Token cost per query | High (retrieve + re-rank + generate) | Low (read index + targeted pages) | LLM Wiki: cheaper per query |
| Traceability | Chunk-level citations (often lossy) | Source-level citations back to `raw/` | LLM Wiki: stronger provenance |
| Scale sweet spot | Enterprise (millions of documents) | Personal/team (sub-100K tokens of wiki) | Different tools for different scales |
| Contradictions | Undetected — conflicting chunks coexist | Flagged during lint operations | LLM Wiki: active consistency checking |

## When to Use RAG

- Millions of documents that can't be pre-compiled
- Frequently changing documents where re-ingesting the entire wiki is impractical
- Sub-second query latency at scale
- Multi-team access with different permission levels

## When to Use LLM Wiki

- Fewer than ~100-200 source documents
- Knowledge compounding matters — each source improves all future queries
- Traceability required (every claim → raw source)
- Zero infrastructure desired (just a folder + LLM)
- Consistency checks (lint) valued over retrieval speed

## Failure Modes

- **LLM Wiki at enterprise scale:** Context window limits, ingest cascade costs, no concurrent multi-user access
- **RAG at personal scale:** Over-engineered infrastructure for a problem that fits in one context window; loses cross-references and consistency checking

## Related Artifacts

- [[wiki/llm-wiki/constructs/llm-wiki-pattern]] — the pattern being compared
- [[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]] — source for this comparison

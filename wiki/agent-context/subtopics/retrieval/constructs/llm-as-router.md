---
title: LLM-as-Router
type: construct
description: "Pattern where the LLM itself semantically routes queries to relevant knowledge nodes by reading a lightweight index, replacing keyword matching or embedding similarity."
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[designs/knowledge-surfacing-design]]"
tags: [agent-context, agents, architecture, retrieval]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: medium
novelty: emerging
aka: ["semantic routing", "LLM-based index routing", "model-as-navigator"]
---

# LLM-as-Router

## Definition

A retrieval pattern where the LLM reads a lightweight index (node IDs, descriptions, keywords, tags) and uses its full semantic understanding to decide which nodes are relevant to the current task — replacing traditional keyword matching (BM25) or embedding similarity search.

The LLM becomes the routing engine, not just the consumer of retrieved content.

## Why It Matters

For structured, domain-specific content (agent skill files, wiki pages, knowledge bases), LLM semantic understanding far outperforms:
- **Keyword matching**: can't handle synonyms, paraphrases, or implicit relevance
- **Embedding similarity**: optimized for general semantic similarity, not task-specific routing decisions
- **Manual routing rules**: brittle, require maintenance, can't handle novel queries

The pattern requires no fine-tuning — any instruction-following model can perform it from a one-paragraph system prompt addition. The index serves as the "menu" the LLM reads to make routing decisions.

## Mechanism / Structure

**Workflow (from ObjectGraph Algorithm 1):**

1. Agent reads index string (~30–150 tokens depending on wiki size)
2. LLM selects node IDs relevant to the current task (semantic matching)
3. Filter by confidence threshold (e.g., θ=0.80)
4. Apply skip-if-known filter (session memory of previously visited nodes)
5. Resolve dependency edges (auto-fetch prerequisites)
6. Fetch content at appropriate depth (dense or full)

**Key insight:** The index search is performed *by the LLM*, not by a separate retrieval system. This means:
- No embedding model needed
- No vector database needed
- No retrieval pipeline needed
- Just a text index in the context window

**Applied to this wiki:**
- The agent reads `wiki/index.md` (~500 tokens) or `wiki/by-tag.md` (~600 tokens)
- The LLM decides which pages are relevant based on descriptions
- Only those pages are read in full

## Distinctions

- Not a RAG retriever (no embedding, no vector DB, no chunking)
- Not keyword search (semantic, handles paraphrase and implication)
- Not a fine-tuned classifier (works zero-shot with any instruction-following model)
- The LLM is both router AND consumer — same model, different passes
- Requires the index to fit in context (works at wiki/skill-library scale, not web-scale)

## Evidence and Sources

- ObjectGraph: "the index search is performed by the LLM, not by a keyword-matching algorithm… far superior to BM25 or embedding similarity for the structured, domain-specific content of agent files" — [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]
- Ablation: index routing accounts for the majority of token savings (82% combined with dense layer)
- The Meta-Tool Pattern (Synaptic Labs) uses the same mechanism: tool descriptions serve as the routing index the LLM reads — [The Meta-Tool Pattern](https://blog.synapticlabs.ai/bounded-context-packs-meta-tool-pattern)

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — the broader model this mechanism serves
- [[designs/knowledge-surfacing-design]] — design approaches using LLM-as-Router
- [[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]] — the problem this solves at the routing layer
- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] — what the index should contain (only what aids routing)

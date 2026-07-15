---
title: Retrieval-as-Reasoning
type: construct
description: "Paradigm where retrieval behaves like reasoning — agents search, read, traverse links, and decide when evidence is sufficient — rather than one-shot context fetching."
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/retrieval-as-reasoning-llm-wiki]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]]"
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
  - "[[designs/knowledge-surfacing-design]]"
tags: [agent-context, retrieval, agents, knowledge-graph]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: medium
novelty: emerging
coined_by: "Haoliang Ming et al. (Tencent/WeChat, 2026)"
aka: ["agent-native retrieval", "iterative retrieval", "retrieval as search"]
---

# Retrieval-as-Reasoning

## Definition

A retrieval paradigm where the agent's interaction with external knowledge behaves like multi-step reasoning rather than one-shot context fetching. The agent iteratively searches, reads, traverses links, and decides when evidence is sufficient — rather than receiving a pre-packaged context payload.

Contrast with "retrieval-as-lookup": embed query → find similar chunks → inject into prompt → generate answer.

## Why It Matters

Traditional RAG treats retrieval as a single step before generation. But complex questions require multi-hop evidence gathering: finding a page, following its links to related pages, assessing whether enough evidence exists, and sometimes correcting the knowledge structure when retrieval fails. This is reasoning over a knowledge graph, not lookup in an index.

## Mechanism / Structure

**LLM-Wiki implementation (Ming et al., 2026):**

1. **Compile** documents into structured wiki pages with bidirectional cross-links
2. **Expose** three operations as tool calls: search, read, follow-link
3. **Agent reasons** about which links to follow and when evidence is sufficient
4. **Error Book** records retrieval failures, triggering structural corrections (self-evolution)

**Key differences from RAG:**

| Dimension | Retrieval-as-Lookup (RAG) | Retrieval-as-Reasoning |
|-----------|---------------------------|------------------------|
| Steps | Single retrieval pass | Multi-step traversal |
| Knowledge format | Flat chunks with embeddings | Compiled pages with typed links |
| Agent role | Passive consumer of results | Active navigator making decisions |
| Failure handling | Silent (bad chunks, bad answer) | Error Book triggers corrections |
| Interface | embed → search → inject | search → read → follow-link (tool calls) |

**Results:**
- Outperforms HippoRAG 2, LightRAG, GraphRAG by 2.0–8.1 F1 points
- Especially strong on multi-document structured queries (AuthTrace)
- Generalizes beyond chain-style multi-hop reasoning

## Distinctions

- Not the same as multi-hop QA (which may still use single-pass retrieval with chain-of-thought)
- Not the same as agentic RAG (which adds an agent loop but may still use flat chunks)
- The key difference is *compiled knowledge with typed links* + *tool-calling interface* + *self-correction*
- Related to but distinct from [[wiki/llm-wiki/constructs/llm-wiki-pattern]] — Karpathy's pattern is about knowledge *production*; this is about knowledge *consumption* by agents

## Evidence and Sources

- LLM-Wiki achieves SOTA on HotpotQA, MuSiQue, 2WikiMultiHopQA — [[wiki/agent-context/subtopics/retrieval/sources/retrieval-as-reasoning-llm-wiki]]
- Outperforms HippoRAG 2, LightRAG, GraphRAG by 2.0–8.1 F1 points (same source)
- Best overall accuracy on AuthTrace (multi-document structured queries)

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]] — the routing mechanism used at the search step
- [[wiki/llm-wiki/constructs/llm-wiki-pattern]] — the production side (compile knowledge into wiki); this is the consumption side
- [[designs/knowledge-surfacing-design]] — Approach B (MCP Meta-Tool) implements this via tool calls
- [[wiki/llm-wiki/comparisons/llm-wiki-vs-rag]] — the broader comparison this paradigm contributes to

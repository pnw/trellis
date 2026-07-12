---
title: "Source: Retrieval as Reasoning — Self-Evolving Agent-Native Retrieval via LLM-Wiki"
type: source-capture
evidence: empirical-primary
description: "Proposes LLM-Wiki, an agent-native retrieval system that compiles documents into structured wiki pages with bidirectional links and self-correction, outperforming HippoRAG 2, LightRAG, and GraphRAG."
sources:
  - "[[raw/papers/retrieval-as-reasoning-llm-wiki.md]]"
related:
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/retrieval-as-reasoning]]"
tags: [agent-context, llm-wiki, retrieval, knowledge-graph, agents]
created: 2026-07-04
timestamp: 2026-07-04T22:43:00Z
---

# Retrieval as Reasoning — Self-Evolving Agent-Native Retrieval via LLM-Wiki

## Source Identity

- Raw source: [[raw/papers/retrieval-as-reasoning-llm-wiki.md]]
- Source type: paper
- Author(s): Haoliang Ming, Feifei Li, Xiaoqing Wu, Wenhui Que (WeChat, Tencent Inc.)
- Published: 2026-05-25
- Original URL: https://arxiv.org/abs/2605.25480
- Scope: Agent-native retrieval system that treats external knowledge as compilable, composable, self-evolving structure rather than a static retrieval index

## Core Contribution

Operationalizes the "Retrieval-as-Reasoning" paradigm: instead of one-shot context fetching (traditional RAG), agents should search, read, traverse links, and decide when evidence is sufficient. LLM-Wiki compiles documents into structured wiki pages with bidirectional links, exposes search/read/link-following as tool-calling operations, and introduces an "Error Book" for persistent self-correction of the knowledge structure.

## Key Claims

- Current RAG systems expose a "retrieval-as-lookup" interface ill-suited to iterative reasoning agents
- Knowledge should be treated as compilable and composable (not a flat chunk index)
- LLM-Wiki compiles documents into structured wiki pages with bidirectional cross-links
- Standard tool-calling interfaces (search, read, follow-link) enable agent reasoning over the knowledge structure
- An "Error Book" enables persistent structural and semantic self-correction (the knowledge evolves)
- LLM-Wiki achieves state-of-the-art on HotpotQA, MuSiQue, and 2WikiMultiHopQA
- Outperforms HippoRAG 2, LightRAG, and GraphRAG by 2.0–8.1 F1 points
- Especially strong on multi-document structured queries (AuthTrace benchmark)
- Compilation-based retrieval generalizes beyond chain-style multi-hop reasoning

## Evidence and Results

**Multi-hop QA Benchmarks:**
- Outperforms HippoRAG 2, LightRAG, GraphRAG by 2.0–8.1 F1 points on HotpotQA, MuSiQue, 2WikiMultiHopQA
- Best overall accuracy on AuthTrace (multi-document structured queries)

**Key Architecture:**
- Documents compiled into wiki pages (not chunked)
- Bidirectional links between related concepts
- Tool-calling interface: search, read, follow-link operations
- Error Book: persistent record of retrieval failures that triggers structural corrections

## Methodology

- Evaluated on standard multi-hop QA benchmarks: HotpotQA, MuSiQue, 2WikiMultiHopQA
- Additional evaluation on AuthTrace for multi-document structured queries
- Compared against: HippoRAG 2, LightRAG, GraphRAG (and presumably NaiveRAG)
- 15 pages, 3 figures, 10 tables, 1 algorithm

## Limitations and Caveats

- Paper from Tencent/WeChat — may have proprietary components not fully disclosed
- Compilation step has upfront cost (similar to GraphRAG construction)
- Self-evolving mechanism (Error Book) adds ongoing maintenance overhead
- Benchmarks are primarily QA-focused — not tested on knowledge base navigation or workspace-context tasks
- Does not compare against pre-compiled wikis used as direct context (the Karpathy pattern)

## Important References and Linked Material

- [HippoRAG 2](https://arxiv.org/abs/2405.14831) — Memory-augmented RAG baseline
- [LightRAG (Guo et al., 2025)](https://arxiv.org/abs/2501.06713) — Lightweight graph+text RAG
- [GraphRAG (Edge et al., 2024)](https://arxiv.org/abs/2404.16130) — Community-based global RAG
- LLM-Wiki concept is closely related to but distinct from Karpathy's LLM Wiki pattern — this is an academic formalization focused on retrieval rather than personal knowledge management

## Contribution Routing

- Creates: `[[wiki/agent-context/subtopics/retrieval/constructs/retrieval-as-reasoning]]` — the paradigm shift from retrieval-as-lookup to retrieval-as-reasoning
- Updates: `[[wiki/llm-wiki/constructs/llm-wiki-pattern]]` — academic validation of compilation-based knowledge approach
- Informs: comparison between wiki-based retrieval and traditional RAG approaches

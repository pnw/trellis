---
title: Domain-Centric Knowledge Fusion
type: construct
description: "Pre-summarizing knowledge at each tag/domain level so retrieval returns synthesized global context rather than raw fragments."
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/tagrag-tag-guided-hierarchical-knowledge-graph-rag]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/hierarchical-tag-chains]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
tags: [agent-context, tags, knowledge-graph, retrieval]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: medium
novelty: emerging
coined_by: "Wenbiao Tao et al. (TagRAG, ACL 2026)"
---

# Domain-Centric Knowledge Fusion

## Definition

The practice of pre-summarizing knowledge at each domain tag level during knowledge graph construction, so that at retrieval time the system returns synthesized global context rather than raw document fragments. Each domain tag carries a fused summary of all knowledge connected to it.

## Why It Matters

Without fusion, retrieval returns disconnected fragments that the LLM must synthesize on the fly (expensive, error-prone). With fusion, each domain tag already carries a pre-computed global view of its subdomain. The retrieval result is immediately useful as context.

This is analogous to how this wiki's synthesis pages work: a synthesis page pre-integrates multiple sources so a reader doesn't have to. Domain-centric fusion automates this at the tag level.

## Mechanism / Structure

**TagRAG formulation:**

```
summary = LLM(Chain(v_d), Neighbors(v_d))
```

Where:
- v_d = a domain tag
- Chain(v_d) = the domain tag chain it belongs to (higher-level context)
- Neighbors(v_d) = object tags linked to this domain tag (specific knowledge)

The summary combines:
1. **Domain information on chains** — high-level context from parent/sibling domain tags
2. **Specialized knowledge in objects** — specific facts from connected object tags

After vectorizing summaries, you get a "domain-centric knowledge retrieval library":
```
K = {(tag_i, summary_i, embedding_i)} for all domain tags
```

**Retrieval flow:**
1. Query → embed → cosine similarity against summary embeddings
2. Top-k domain tags retrieved with their fused summaries
3. Chain traversal adds higher-level summaries
4. Combined context sent to LLM for answer generation

## Distinctions

- Not the same as document summarization (which compresses individual documents)
- Not the same as community summaries in GraphRAG (which require expensive community detection)
- Operates at the *tag level*, not the document level — cuts across documents
- The fusion happens at *construction time*, not query time — retrieval is fast
- Related to but different from wiki synthesis pages: those are human/LLM-authored full pages; fusion produces compact summaries (~100 tokens) for retrieval routing

## Evidence and Sources

- TagRAG ablation: removing knowledge fusion (using only domain tag descriptions) causes "even larger drop" than removing chain integration — [[wiki/agent-context/subtopics/retrieval/sources/tagrag-tag-guided-hierarchical-knowledge-graph-rag]]
- Both components (chain hierarchy + knowledge fusion) are necessary for full performance (same source)
- Construction remains 14.6× faster than GraphRAG despite the fusion step (same source)

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/hierarchical-tag-chains]] — the structural substrate on which fusion operates
- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — fused summaries serve as the "dense pass" layer
- [[designs/knowledge-surfacing-design]] — Approach C could implement fusion at each tag level

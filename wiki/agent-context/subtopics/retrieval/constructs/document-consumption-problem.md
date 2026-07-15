---
title: Document Consumption Problem
type: construct
description: "The fundamental mismatch between linear document formats designed for human readers and the retrieval-oriented needs of LLM agents, formalized as the Full-Read Assumption."
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/context-compounding]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]]"
tags: [agent-context, architecture, token-optimization]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: medium
novelty: coined
coined_by: "Mohit Dubey (ObjectGraph, 2026)"
aka: ["Full-Read Assumption", "format mismatch problem"]
---

# Document Consumption Problem

## Definition

The structural mismatch between document formats designed for human linear reading and LLM agents that need selective retrieval. Formalized as the "Full-Read Assumption": a document format F satisfies this assumption if the minimum cost of retrieving *any* content from a document formatted as F is O(n), where n is the total token count.

Every existing document format (Markdown, JSON, YAML, llms.txt) satisfies the Full-Read Assumption — to get any piece of information, you must inject the entire document.

## Why It Matters

The problem manifests in three failure modes:

1. **Token inflation** — A 600-line deployment runbook costs ~1,800 tokens. The content relevant to a specific task is ~80 tokens (4.4% utilization). The other 95.6% is waste.
2. **Context compounding** — In multi-turn loops, injected documents are re-transmitted on every API call (stateless APIs). See [[wiki/agent-context/subtopics/retrieval/constructs/context-compounding]].
3. **Role blindness** — In multi-agent systems, all consumers receive identical content regardless of their role or need.

## Mechanism / Structure

**Formal model:** Let D be a document of n tokens, partitioned into k semantic sections. An agent task τ has a relevance set R(τ) ⊆ {1,…,k} where |R(τ)| ≪ k. Under the Full-Read Assumption, cost is always O(n) regardless of |R(τ)|.

**Six required properties** to solve the problem (no single existing format satisfies all six):

| Property | Meaning |
|----------|---------|
| P1: Selective Retrieval | Retrieve relevant content without loading all content |
| P2: Compounding Elimination | Prevent super-linear cost growth in multi-turn loops |
| P3: Typed Edges | Express typed relationships between content units |
| P4: Role Scoping | Serve different content to different agent roles |
| P5: Executable Assertions | Encode validation logic in the format itself |
| P6: Human Readability | Readable without tooling |

## Distinctions

- Not the same as "too much context" (a quantity problem) — this is a *structural* problem about format capabilities
- Not solvable by compression alone (which preserves the injection model)
- Not solvable by RAG alone (which requires vector infrastructure and loses typed relationships)
- The [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] is the solution pattern; this construct defines the problem

## Evidence and Sources

- Formalized in ObjectGraph paper with mathematical model — [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]
- Empirically validated: 92% token reduction when the problem is solved (same source)
- ETH Zurich finding that architectural overviews hurt performance is a symptom of this problem — [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — the solution pattern
- [[wiki/agent-context/subtopics/retrieval/constructs/context-compounding]] — failure mode #2 in detail
- [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]] — why the wasted tokens actively harm accuracy
- [[designs/knowledge-surfacing-design]] — design approaches that solve this problem for OKF wikis

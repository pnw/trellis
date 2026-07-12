---
title: Context Compounding
type: construct
description: "Super-linear token cost growth in multi-turn agent loops caused by stateless API re-transmission of conversation history including previously-read documents."
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[ai-research::wiki/token-economics/syntheses/token-cost-optimization]]"
tags: [agent-context, token-optimization, cost-optimization]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: medium
novelty: coined
coined_by: "Mohit Dubey (ObjectGraph, 2026)"
aka: ["context compounding problem", "multi-turn token inflation"]
---

# Context Compounding

## Definition

The super-linear growth of token costs in multi-turn agentic workflows caused by the statelessness of LLM APIs. Every document read is appended to conversation history, which must be re-transmitted in full on every subsequent API call. A single 1,800-token document read in turn 1 costs 1,800 × (T - 1) additional tokens across the remaining turns.

## Why It Matters

A five-turn loop involving three document reads can compound an original 1,800-token document into 15,000+ tokens of transmission overhead. At turn 5, full-injection Markdown accumulates 46,000 tokens vs. 1,260 for progressive-disclosure approaches — a 36.5× difference. This is the primary cost driver in agentic workflows, exceeding per-document costs by an order of magnitude.

## Mechanism / Structure

**Formal model:**

```
C_total = Σ(t=1 to T) h_t = Σ(t=1 to T) (h_0 + Σ(j≤t) c_j)
```

Where:
- h_t = history token count at turn t
- h_0 = initial context (system prompt, instructions)
- c_j = cost of operation j (document read, tool output, etc.)

For m document reads of n tokens each in a T-turn workflow:

```
C_compound = T · h_0 + m · n · (T - t_read + 1)
```

This grows super-linearly in both T and n.

**Example:** 5-turn loop, one 1,800-token document read at turn 1:
- Markdown (full injection): ≈ 9,000 tokens in transmission overhead alone
- ObjectGraph (progressive disclosure): ≈ 234 tokens per access, no compounding with Architecture B (context isolation)

## Distinctions

- Not the same as "large context windows solve this" — compounding means cost grows with *turns*, not just document size
- Not the same as token cost per query — this is about *cumulative* cost across a workflow
- Distinct from prompt caching (which mitigates cost but doesn't eliminate the structural problem)
- Architecture B (Router/Executor split) eliminates compounding by design: the Executor receives zero tool-call history

## Evidence and Sources

- ObjectGraph evaluation: 46,000 tokens (Markdown) vs. 1,260 tokens (Architecture B) at turn 5 — [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]
- Xiao et al. (2026) achieve 39.9–59.7% input token reduction on coding agents through trajectory reduction (cited in ObjectGraph)

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]] — the parent problem this is a failure mode of
- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — the solution pattern (read only what's needed)
- [[ai-research::wiki/token-economics/syntheses/token-cost-optimization]] — broader strategies for reducing LLM costs
- [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] — design approaches that address compounding

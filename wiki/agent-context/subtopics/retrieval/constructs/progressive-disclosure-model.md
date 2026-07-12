---
title: Progressive Disclosure Model (Agent Context)
type: construct
description: "A layered reading-depth model for agent document consumption: index (routing) → dense (keywords) → full (complete content), enabling 60–95% token reduction."
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]]"
  - "[[ai-research::wiki/intent-compiler/constructs/progressive-disclosure]]"
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
tags: [agent-context, progressive-disclosure, token-optimization, architecture]
created: 2026-07-04
timestamp: 2026-07-04T22:43:00Z
confidence: medium
novelty: emerging
coined_by: "Dubey & Open Gigantic (ObjectGraph, 2026); builds on established UX concept"
aka: ["PDM", "three-pass reading", "index-dense-full model"]
---

# Progressive Disclosure Model (Agent Context)

## Definition

A structured approach to agent document consumption where content is organized into multiple reading depths. An agent reads only the shallowest layer needed to route its query, then selectively deepens into specific nodes. The canonical formulation has three passes:

1. **Index pass** (~30 tokens): Node IDs, types, scopes, confidence scores, and keywords — enough to route a query without loading any content
2. **Dense pass** (~12 tokens/node): Compressed keyword summaries — enough to confirm relevance
3. **Full pass** (~180 tokens/node): Complete prose, code, steps, and warnings — loaded only when needed

## Why It Matters

The fundamental problem: agents using traditional documents pay O(n) cost to retrieve any content, even if only a tiny fraction is relevant. A typical deployment runbook costs 1,800 tokens; the relevant content for a specific task is ~80 tokens (4.4% utilization). Progressive disclosure converts this from O(n) to O(k) where k ≪ n is the number of relevant nodes.

The impact compounds in multi-turn loops: without progressive disclosure, a 5-turn workflow re-transmitting 3 documents accumulates 46,000 tokens. With progressive disclosure: 1,260 tokens (36.5× reduction).

## Mechanism / Structure

**Cost model:**

```
C_og(τ) = C_index + |M(τ)| · c̄_dense + |F(τ)| · c̄_full
```

Where:
- C_index ≈ 30 + 6k tokens (k = number of nodes)
- M(τ) = nodes matched at dense level
- F(τ) ⊆ M(τ) = nodes requiring full-pass reading
- c̄_dense ≈ 12 tokens, c̄_full ≈ 180 tokens

For typical values (n=1,800, |M(τ)|=2, |F(τ)|=1): C_og = 234 tokens, Savings = 87.0%

**Ablation finding:** Index routing + dense layer account for 82% of total token savings. The index pass alone provides most of the routing value.

**Applied to this wiki:**
- Index pass = `wiki/index.md` (page titles + descriptions)
- Dense pass = frontmatter (type, tags, description, confidence)
- Full pass = reading the page body

## Distinctions

- Not the same as document compression (which removes content permanently)
- Not the same as RAG chunking (which breaks documents into fragments without semantic typing)
- Not the same as lazy loading (performance optimization) — this is about *cognitive routing* for agents
- Related to but distinct from [[ai-research::wiki/intent-compiler/constructs/progressive-disclosure]] which applies to human UX and process design; this construct applies specifically to agent document consumption
- OKF's `index.md` + `description` field implements a simpler 2-level version of this model
- Not the only option: [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] skips staged disclosure entirely by searching the raw corpus directly with generic file primitives — reportedly the choice Claude Code and several peer coding agents converged on for corpora far larger than this model's own worked examples assume

## Evidence and Sources

- ObjectGraph (Dubey, 2026): 92% token reduction, 36.5× multi-turn reduction
- The "less-is-more effect": removing irrelevant content improves accuracy by 2.8% even at equivalent token budgets (reduced attention dilution)
- Consistent with ETH Zurich finding that architectural overviews (full-dump approach) hurt performance

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/llm-as-router]] — the routing mechanism that operates on the index layer
- [[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]] — the problem this solves
- [[ai-research::wiki/intent-compiler/constructs/progressive-disclosure]] — the general UX principle applied to different domain
- [[wiki/llm-wiki/constructs/three-layer-architecture]] — the wiki production architecture (raw → wiki → schema) vs. this consumption architecture (index → dense → full)

## Open Questions

- What is the optimal index granularity for wikis of different sizes? (32 pages vs. 200 pages vs. 1000 pages)
- Does a tag-based index layer perform better than a topic-based one for cross-cutting queries?
- How should confidence scores influence routing decisions?

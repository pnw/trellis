---
title: Attention Dilution
type: construct
description: "The phenomenon where irrelevant content in an LLM's context window actively degrades accuracy — not just wastes tokens. The 'less-is-more effect.'"
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
tags: [agent-context, token-optimization, context-engineering]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: high
novelty: emerging
aka: ["less-is-more effect", "context noise", "lost in the middle"]
---

# Attention Dilution

## Definition

The phenomenon where irrelevant content in an LLM's context window actively degrades task accuracy — not merely wastes tokens. Adding content that is not relevant to the current task makes the model *worse* at the task, even when the relevant content is also present.

## Why It Matters

This overturns the naive assumption that "more context is always better" or at worst neutral. It means context engineering is not just a cost optimization — it's an *accuracy* optimization. Every irrelevant token injected carries a measurable accuracy penalty.

The ETH Zurich study found this concretely: architectural overviews in AGENTS.md files increased inference cost AND encouraged broader file traversal without improving task success. The content wasn't neutral — it was actively harmful.

## Mechanism / Structure

**Empirical evidence:**
- ObjectGraph: removing irrelevant content improves accuracy by 2.8% even at equivalent token budgets — [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]
- ETH Zurich: LLM-generated context files (containing redundant/discoverable information) reduced task success by 0.5–2% — [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]
- "Lost in the middle" phenomenon: rules placed in the middle of long context files are dropped by agents — [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]

**Related research (cited in ObjectGraph):**
- FatCat (2025) notes Markdown's alignment with LLM pretraining priors reduces attention dilution — but only when content is relevant
- Gao et al. (2026) find that removing non-essential content from agent skill bodies improves task performance by 2.8%

**Mechanisms (hypothesized):**
1. Attention heads distribute weight across all tokens — irrelevant tokens "steal" attention from relevant ones
2. The model must reason about what to ignore, consuming reasoning capacity
3. Irrelevant content may trigger spurious associations or override intended behavior

## Distinctions

- Not the same as "context window limit" — dilution happens well within capacity
- Not the same as "token cost" — this is about *accuracy*, not economics
- The "lost in the middle" effect is a specific manifestation: content at the edges gets more attention than content in the middle
- Distinct from [[wiki/agent-context/subtopics/retrieval/constructs/context-compounding]] which is about *cost*; attention dilution is about *quality*

## Evidence and Sources

- +2.8% accuracy improvement from removing irrelevant content (ObjectGraph) — [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]
- -0.5% to -2% task success from injecting redundant context (ETH Zurich) — [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]
- Architectural overviews hurt: "do not provide effective overviews" (ETH Zurich via Augment) — [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]
- Signal-to-noise ratio of context windows is "critical to their success" (Ardalis, 2026)

## Related Artifacts

- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] — the heuristic for what to include (only what won't dilute)
- [[wiki/agent-context/subtopics/retrieval/constructs/document-consumption-problem]] — the structural problem that causes dilution
- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — the solution (load only relevant content)
- [[ai-research::wiki/token-economics/syntheses/token-cost-optimization]] — attention dilution means token reduction is also accuracy improvement

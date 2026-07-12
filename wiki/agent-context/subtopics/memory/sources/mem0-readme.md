---
title: "Mem0 README"
type: source-capture
evidence: official-docs
description: Official Mem0 README describing a memory layer for personalized AI — ADD-only single-pass extraction, entity linking, fused multi-signal retrieval, temporal ranking, and self-reported benchmark results.
sources:
  - "[[raw/articles/mem0-readme.md]]"
related:
  - "[[wiki/llm-wiki/comparisons/llm-wiki-vs-agent-memory]]"
tags: [agent-memory, personalization, retrieval, temporal-reasoning]
created: 2026-07-08
timestamp: 2026-07-08T05:00:00Z
status: stable
---

# Mem0 README

## Source Identity

- Raw source: [[raw/articles/mem0-readme.md]]
- Source type: documentation page (project README)
- Author(s): Mem0 (company, YC S24)
- Published/retrieved: retrieved 2026-07-08
- Original URL: https://github.com/mem0ai/mem0
- Scope: memory-layer positioning, April 2026 algorithm redesign, benchmark results, features

## Core Contribution

Describes an "intelligent memory layer" that gives assistants and agents persistent, personalized memory — remembering user preferences and adapting over time — with a 2026 algorithm redesign built around accumulation rather than revision.

## Key Claims

1. **ADD-only extraction (April 2026):** one LLM call per interaction; memories only accumulate — no UPDATE/DELETE, nothing is overwritten. Conflicts are resolved at *retrieval* time by temporal reasoning that ranks the right dated instance for queries about current state, past events, or plans.
2. **Entity linking:** entities are extracted, embedded, and linked across memories to boost retrieval.
3. **Multi-signal retrieval:** semantic, BM25 keyword, and entity matching scored in parallel and fused — single-pass, no agentic loops.
4. **Multi-level memory scopes:** user, session, and agent state retained separately.
5. **Self-reported benchmarks:** LoCoMo 91.6, LongMemEval 94.8 (~6.8K tokens per query), BEAM 64.1 at 1M tokens; evaluation framework open-sourced for reproduction.

## Limitations and Caveats

- Benchmark numbers are the vendor's own runs of its own algorithm; the open-sourced eval framework mitigates but does not replace independent replication.

## Reliability Notes

`official-docs`: authoritative for design intent (how Mem0 works). The benchmark results are effectiveness claims and carry `vendor-claim` weight for downstream derivation despite living in an official README.

## Contribution Routing

- [[wiki/llm-wiki/comparisons/llm-wiki-vs-agent-memory]] — ADD-only accumulation vs curated adjudication is the sharpest single contrast with the wiki's reconciliation model
- Future: independent LongMemEval/LoCoMo replications would upgrade the effectiveness claims

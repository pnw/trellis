---
title: "Graphiti README"
type: source-capture
evidence: official-docs
description: Official Graphiti (Zep) README describing temporal context graphs — facts with validity windows, entities that evolve, and full provenance back to the raw episodes that produced them.
sources:
  - "[[raw/articles/graphiti-readme.md]]"
related:
  - "[[wiki/llm-wiki/comparisons/llm-wiki-vs-agent-memory]]"
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
tags: [agent-memory, knowledge-graphs, temporal-reasoning, provenance]
created: 2026-07-08
timestamp: 2026-07-08T05:00:00Z
status: stable
---

# Graphiti README

## Source Identity

- Raw source: [[raw/articles/graphiti-readme.md]]
- Source type: documentation page (project README)
- Author(s): Zep (company; Graphiti is its open-source engine)
- Published/retrieved: retrieved 2026-07-08
- Original URL: https://github.com/getzep/graphiti
- Scope: temporal context graph framework — data model, contrast with static knowledge graphs and RAG

## Core Contribution

Defines the *context graph*: a temporal graph of entities, relationships, and facts where every fact carries a validity window and everything traces back to the raw data that produced it — purpose-built for agents operating on evolving, real-world information.

## Key Claims

1. **Validity windows:** each fact records when it became true and when (if ever) it was superseded — "Kendra loves Adidas shoes (as of March 2026)." Facts are superseded, not silently overwritten.
2. **Episodes as provenance:** everything in the graph traces back to *episodes*, the raw source data it was extracted from.
3. **Evolving entities:** entity summaries are updated over time rather than frozen at first extraction.
4. **Continuous integration:** user interactions and enterprise data are integrated as they arrive, contrasted with static knowledge graphs and one-shot RAG.
5. **Prescribed and learned ontology:** the schema can be declared up front, discovered from data, or both.
6. A peer-reviewed-track paper exists (arXiv 2501.13956), not captured here.

## Limitations and Caveats

- README describes design intent; no effectiveness evidence beyond adoption signals (GitHub stars, hiring notes).

## Reliability Notes

`official-docs`: authoritative for the data model and intended behavior of Graphiti/Zep; effectiveness comparisons with RAG are the vendor characterizing competitors.

## Contribution Routing

- [[wiki/llm-wiki/comparisons/llm-wiki-vs-agent-memory]] — validity windows and episodes-as-provenance are the two ideas most directly transferable to the wiki's freshness and raw-layer design
- Future: capture the Graphiti arXiv paper for empirical grounding

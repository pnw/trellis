---
title: "Source: How to Build Karpathy's LLM Wiki (Starmorph)"
type: source-capture
evidence: expert-analysis
description: Comprehensive guide to Karpathy's LLM Wiki pattern covering full architecture, setup, tooling, community ecosystem, and criticisms.
sources:
  - "[[raw/articles/karpathy-llm-wiki-knowledge-base-guide.md]]"
related:
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
  - "[[wiki/llm-wiki/comparisons/llm-wiki-vs-rag]]"
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[wiki/llm-wiki/entities/andrej-karpathy]]"
tags: [llm-wiki, knowledge-management, tooling]
created: 2026-04-16
timestamp: 2026-07-04T21:23:00Z
---

# How to Build Karpathy's LLM Wiki: The Complete Guide

## Source Identity

- Raw source: [[raw/articles/karpathy-llm-wiki-knowledge-base-guide.md]]
- Source type: article
- Author(s): Dylan Boudro (Starmorph)
- Published: April 2026
- Original URL: https://starmorph.com/llm-wiki/
- Scope: Comprehensive guide to the LLM Wiki pattern — architecture, setup, tooling, community, criticisms

## Core Contribution

A comprehensive guide to Andrej Karpathy's LLM Wiki pattern — a workflow where an LLM agent builds and maintains a structured markdown knowledge base from raw sources. Covers the full architecture, setup with Claude Code and Obsidian, comparison to RAG, community implementations, intellectual lineage, and criticisms.

## Key Claims

- The LLM Wiki is a **pattern, not a product**. Humans curate what goes in, the LLM handles all organization, cross-referencing, summarization, and maintenance.
- Karpathy's post (April 2026) went viral — 16M+ views on X, 5,000+ GitHub Gist stars in days.
- His wiki on a single research topic reached ~100 articles and ~400,000 words without him writing any of it directly.
- The pattern uses a **compiler analogy**: `raw/` is source code, the LLM is the compiler, `wiki/` is the executable output, lint is tests, queries are runtime.
- The LLM Wiki is a **manual, traceable implementation of Graph RAG** — without the graph database, entity extraction pipeline, or ontology engineering.
- Works best at personal/team scale: 50-200 source documents.

## Evidence and Results

- Karpathy's own wiki: ~100 articles, ~400,000 words on a single research topic
- Community adoption: multiple implementations within a week (llmwiki, obsidian-wiki, second-brain, wiki-skills, LLM Wiki v2)
- 16M+ views on X post, 5,000+ GitHub Gist stars

## Limitations and Caveats

Criticisms noted in the article:
- The grunt work of organizing IS the learning (counter: wiki is reference, not replacement for thinking)
- Context window degradation at 200K-300K tokens (mitigation: index-based navigation)
- Model collapse risk from repeated rewriting (mitigation: immutable `raw/` layer + lint + git)
- Complexity ceiling at 50-200 sources (mitigation: LLM Wiki v2 extensions or RAG)

## Important References and Linked Material

### Primary Sources
- [Karpathy's X post](https://x.com/karpathy/status/2039805659525644595) — The viral post that introduced the LLM Wiki concept (16M+ views)
- [Karpathy's LLM Wiki Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — The follow-up GitHub Gist with full pattern details (5,000+ stars)
- [Vannevar Bush — "As We May Think" (1945)](https://www.theatlantic.com/magazine/archive/1945/07/as-we-may-think/303881/) — The Memex essay Karpathy references as intellectual lineage

### Tools & Projects Referenced
- [Obsidian Web Clipper](https://obsidian.md/clipper) — Browser extension to convert web articles to markdown for `raw/`
- [Markdownload](https://github.com/deathau/markdownload) — Alternative browser extension for saving pages as markdown
- [QMD](https://github.com/tobi/qmd) — Local markdown search engine (BM25 + vector + LLM re-rank) by Tobi Lutke
- [Dataview](https://github.com/blacksmithgu/obsidian-dataview) — Obsidian plugin for structured queries across wiki frontmatter
- [Marp](https://marp.app) — Convert markdown wiki pages to presentation slides

### Related Standards & Projects
- [llms.txt](https://llmstxt.org/) — Jeremy Howard's website-level standard for helping LLMs understand your site
- [docs-for-llms](https://github.com/simonw/docs-for-llms) — Simon Willison's build scripts for LLM-friendly concatenated documentation

### Community Implementations
- [lucasastorian/llmwiki](https://github.com/lucasastorian/llmwiki) — Upload docs, connect Claude via MCP, have it write your wiki
- [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) — Framework for AI agents to build Obsidian wikis
- [NicholasSpisak/second-brain](https://github.com/NicholasSpisak/second-brain) — LLM-maintained personal knowledge base for Obsidian
- [ussumant/llm-wiki-compiler](https://github.com/ussumant/llm-wiki-compiler) — Compiles markdown knowledge files into topic-based wikis
- [kfchou/wiki-skills](https://github.com/kfchou/wiki-skills) — Claude Code skills implementing the Karpathy pattern
- [LLM Wiki v2 Gist](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) — Extended pattern with memory lifecycle and confidence scoring

### Research Papers
- [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110)
- [Agentic Retrieval-Augmented Generation: A Survey](https://arxiv.org/abs/2501.09136)
- [Survey on Knowledge-Oriented RAG](https://arxiv.org/abs/2503.10677)
- [PersonalAI: Knowledge Graph Storage for LLM Agents](https://arxiv.org/abs/2506.17001)

### Coverage & Discussion
- [VentureBeat — Karpathy shares LLM Knowledge Base architecture](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)
- [Analytics India Magazine — Karpathy Moves Beyond RAG](https://analyticsindiamag.com/ai-news/andrej-karpathy-moves-beyond-rag-builds-llm-powered-personal-knowledge-bases)
- [HN: LLM Wiki discussion](https://news.ycombinator.com/item?id=47640875) — Source of the criticisms section

## Contribution Routing

- `[[wiki/llm-wiki/constructs/llm-wiki-pattern]]` — defines the core pattern construct
- `[[wiki/llm-wiki/constructs/three-layer-architecture]]` — defines the architecture construct
- `[[wiki/llm-wiki/comparisons/llm-wiki-vs-rag]]` — supports the comparison
- `[[wiki/llm-wiki/entities/andrej-karpathy]]` — supports the entity page

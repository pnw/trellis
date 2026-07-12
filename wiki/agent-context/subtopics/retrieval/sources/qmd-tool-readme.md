---
title: QMD — Local Hybrid Search Tool README
type: source-capture
evidence: official-docs
description: Official README for QMD, an open-source, on-device hybrid (BM25 + vector + LLM rerank) search tool for markdown knowledge bases with a built-in MCP server, created by Shopify's Tobi Lütke.
sources:
  - "[[raw/articles/qmd-tool-readme.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/entities/qmd]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]]"
tags: [agent-context, retrieval, knowledge-management, tools]
created: 2026-07-07
timestamp: 2026-07-07T20:00:00Z
status: draft
---

# QMD — Local Hybrid Search Tool README

## Source Identity

- Publisher: official project README
- URL: https://github.com/tobi/qmd
- Author: Tobi Lütke (Shopify co-founder/CEO)
- License: MIT

## Core Contribution

Documents QMD, an open-source, entirely local (on-device) hybrid search tool purpose-built for markdown knowledge bases, notes, and documentation, with a native MCP server for direct agent integration.

## Key Claims

- Combines BM25 full-text search (SQLite FTS5), vector semantic search (node-llama-cpp with GGUF models), and LLM re-ranking, fused via reciprocal rank fusion and position-aware blending.
- Runs entirely on-device — no external API calls, no cloud vector database.
- Ships an MCP server (stdio or HTTP transport) so Claude Desktop/Claude Code and other MCP clients can call `search`, `get`, and related tools directly.
- Positioned for personal/team-scale knowledge bases and documentation, not web-scale corpora; no explicit page-count ceiling is stated.

## Evidence and Results

This is documentation, not a benchmark report — no comparative performance numbers against alternative retrieval approaches are included.

## Limitations and Caveats

- Requires Node.js 22+ or Bun 1.0+; embedding/rerank models (~2GB) auto-download on first use.
- Custom embedding models require a full re-index — no incremental migration path documented.
- Tree-sitter code parsing is optional and format-specific, suggesting less mature support for code-heavy corpora than for prose/markdown.

## Reliability Notes

Tiered `official-docs`: authoritative for what the tool is and how it is designed and used; not evidence of effectiveness relative to alternatives (no such claims are made in the README itself). Authored by a named, identifiable, technically credible individual (Tobi Lütke), which supports authenticity but does not substitute for independent evaluation.

## Important References and Linked Material

- Recommended as the graduation path beyond a flat index by [[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]].
- Community forks/integrations noted but not independently verified: `lazyqmd` TUI, `ehc-io/qmd` fork, a DeepWiki-generated docs site, and an `openclaw/skills` marketplace listing.

## Contribution Routing

- Grounds the new [[wiki/agent-context/subtopics/retrieval/entities/qmd]] entity page.
- Provides a concrete "existing implementation" for the local-hybrid-search option in [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]].

## Extraction Notes

Retrieved via direct WebFetch of the GitHub README; GitHub URLs were reliably fetchable in this session while most other hosts (Anthropic, arXiv, Medium, most blogs) returned HTTP 403.

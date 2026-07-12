---
title: QMD
type: entity
description: An open-source, on-device hybrid search tool (BM25 + vector + LLM rerank) for markdown knowledge bases with a native MCP server, created by Shopify's Tobi Lütke.
sources:
  - "[[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]]"
  - "[[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]"
tags: [agent-context, retrieval, knowledge-management, tools, mcp]
created: 2026-07-07
timestamp: 2026-07-08T01:30:00Z
confidence: low
novelty: emerging
aka: ["Query Markdown"]
---

# QMD

## Identity

QMD ("Query Markdown") is an open-source, MIT-licensed command-line tool that indexes and searches markdown documents, notes, and documentation entirely on-device — no cloud vector database or external API calls. Created by Tobi Lütke (Shopify co-founder/CEO). [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]]

- **Created by**: Tobi Lütke
- **Repository**: github.com/tobi/qmd
- **License**: MIT
- **Core technique**: hybrid retrieval — BM25 full-text (SQLite FTS5) + vector semantic search (node-llama-cpp, GGUF models) + LLM re-ranking, combined via reciprocal rank fusion

## Relevance to the Wiki

QMD is explicitly recommended by Andrej Karpathy's own primary gist on the LLM Wiki pattern as the graduation path once a flat `index.md` stops scaling (past roughly 100 sources / a few hundred pages) — in preference to standing up embedding-based RAG infrastructure. [[wiki/agent-context/subtopics/retrieval/sources/karpathy-llm-wiki-gist-primary]] That is precisely the scale this wiki has just reached (114 pages as of 2026-07-07), which makes QMD a directly relevant candidate tool for [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]'s Approach B, rather than the from-scratch bespoke discover/read meta-tool schema that design previously assumed would need to be built.

## Associated Artifacts

### Architecture

Query pipeline: query expansion -> parallel retrieval across BM25 and vector backends -> reciprocal rank fusion -> position-aware blending -> local LLM reranking of the fused candidates. [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]]

### Integration

Ships a native Model Context Protocol server (stdio or HTTP transport), so [[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]] clients such as Claude Code and Claude Desktop can call `search`, `get`, and related tools directly without a custom-built MCP server. [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]]

### Requirements

Node.js 22+ or Bun 1.0+; auto-downloads ~2GB of embedding/rerank models on first use; requires a full re-index if the embedding model is changed. [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]]

## Notes

- Positioned for personal/team-scale knowledge bases, not web-scale corpora; no explicit page-count ceiling is documented.
- Confidence is `low` in this wiki's terms: grounded in the tool's own README (official-docs, design-intent only) plus one practitioner's recommendation (Karpathy's gist, expert-analysis) — no independent effectiveness evaluation of QMD specifically was found in this research pass.
- Community signals (a `lazyqmd` TUI, an `ehc-io/qmd` fork, a DeepWiki documentation site, an agent-skill marketplace listing) suggest early third-party adoption but were not independently verified.

## Directly Tested Against This Wiki (2026-07-08)

Installed (`npx @tobilu/qmd@2.5.3`) and run against this wiki's 133 markdown files in the sandboxed session that authored this page — see [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]'s Implementation section for the full account. Findings:

- `qmd init`, `qmd collection add`, and `qmd update` worked as documented and are idempotent; `qmd update` (not re-running `collection add`) is the correct repeatable resync command.
- `qmd search` (BM25 lexical) worked immediately with no model download and returned relevant results (e.g., a natural-language query about agent index graduation correctly surfaced this wiki's own design page at 90% score).
- `qmd embed` — and therefore `qmd query`, the hybrid/semantic mode — failed in this environment: its embedding, reranking, and query-expansion models are hosted on `huggingface.co`, which this sandboxed session's network egress policy blocks (a proxy-level CONNECT-tunnel 403, confirmed not to be a Hugging Face gating issue). This is specific to this environment's network policy, not a defect in QMD.
- Practical consequence: in network-restricted sandboxes like this one, QMD currently only delivers its BM25 lexical layer, not the full hybrid pipeline the tool is designed to provide. A local machine or a less-restricted environment would likely get the full pipeline. This wiki now treats egress-free retrieval as a standing constraint: [[wiki/agent-context/subtopics/retrieval/invariants/sandbox-compatible-retrieval]].

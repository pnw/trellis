# QMD — Local Hybrid Search Engine for Markdown Knowledge Bases

- Source URL: https://github.com/tobi/qmd
- Author: Tobi Lütke (Shopify co-founder/CEO)
- License: MIT
- Retrieved via: WebFetch (direct, successful), 2026-07-07

## What It Is

QMD ("Query Markdown") is a command-line search tool that indexes markdown documents, meeting notes, and documentation entirely locally. Described by its creator as "an on-device search engine for everything you need to remember."

## Architecture

Combines three search technologies, all running on-device:

- BM25 full-text search via SQLite FTS5 for keyword matching.
- Vector semantic search using node-llama-cpp with GGUF embedding models.
- LLM re-ranking to refine results through relevance scoring.

Query pipeline: query expansion -> parallel retrieval across both backends (full-text and vector) -> reciprocal rank fusion -> position-aware blending -> a local reranker model produces final ranking.

## Installation and Usage

```
npm install -g @tobilu/qmd
```

Core commands: `qmd collection add` (register directories to index), `qmd embed` (generate vector embeddings), `qmd search` / `qmd vsearch` / `qmd query` (keyword, semantic, or hybrid search), `qmd get` (retrieve specific documents). Output formats include CLI, JSON, CSV, and Markdown for agent integration.

## Corpus Scale

Positioned for personal or team-scale knowledge bases and documentation repositories rather than web-scale corpora. No explicit page-count ceiling is stated in the README.

## MCP Server Integration

Exposes a Model Context Protocol server compatible with Claude Desktop and Claude Code. Supports stdio (default) or HTTP transport; the HTTP daemon mode avoids repeated model loading across clients (`qmd mcp --http --daemon`).

## Requirements and Limitations

- Requires Node.js 22+ or Bun 1.0+.
- Embedding/rerank models (~2GB total) auto-download on first use.
- Custom embedding models must be swapped before re-indexing (no incremental model migration).
- Tree-sitter code parsing is optional and format-specific.

## Ecosystem Signals (not independently verified, noted from search results)

Community forks and integrations exist, including a `lazyqmd` TUI, an `ehc-io/qmd` fork focused on MCP hybrid search, a DeepWiki-generated documentation site, and a listed skill in an agent-skill marketplace (openclaw/skills) — suggesting active, if early-stage, third-party adoption as of mid-2026.

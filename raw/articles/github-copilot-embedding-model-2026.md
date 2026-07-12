# GitHub — New Copilot Embedding Model (2025-2026)

- Source URL: https://github.blog/news-insights/product-news/copilot-new-embedding-model-vs-code/
- Publisher: GitHub (official blog)
- Retrieved via: WebSearch aggregation (direct WebFetch returned HTTP 403 in this session), 2026-07-07
- Corroborating secondary coverage: InfoQ (2025-10), MEXC News, Medium (Kajal Sharma)

## What Changed

GitHub introduced a new embedding model for Copilot code search, used across Copilot's Chat, agent, edit, and ask modes. The model converts a repository's code into vector embeddings so Copilot can semantically search and reference it, using an OpenAI embedding model specialized for code.

## Reported Performance

Cited as a 37.6% improvement in retrieval quality, doubled throughput, and an 8x reduction in index size relative to the prior model. Training used contrastive learning (InfoNCE loss) and Matryoshka Representation Learning, including hard negatives (code that looks correct but isn't), enabling multi-granularity embeddings (fragments through whole files).

## Adaptive Fallback Architecture (Key Finding)

Copilot's code search is not embeddings-only: when eligible, it calls GitHub's `/embeddings/code_search` API for semantically ranked chunks from the indexed commit. For diffs under 300 files, embeddings search is attempted with an 8-second timeout, falling back to TF-IDF (lexical search) if exceeded. For diffs between 301-2,000 files, embeddings are skipped entirely in favor of TF-IDF alone.

## Relevance

This is a third data point (alongside Cursor and Windsurf) directly contradicting the framing that industry-leading coding agents abandoned embeddings for pure grep/agentic search. GitHub Copilot is embeddings-first with a lexical (TF-IDF) fallback specifically for scale/latency reasons — the inverse framing of "grep by default, embeddings as an exception."

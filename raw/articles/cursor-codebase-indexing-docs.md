# Cursor — Semantic & Agentic Search (Official Docs)

- Source URL: https://cursor.com/docs/context/codebase-indexing
- Publisher: Cursor (official documentation)
- Retrieved via: WebSearch aggregation (direct WebFetch returned HTTP 403 in this session), 2026-07-07
- Corroborating secondary sources found in the same search pass: "Securely indexing large codebases" (Cursor's own blog, https://cursor.com/blog/secure-codebase-indexing), "How Cursor Actually Indexes Your Codebase" (Towards Data Science), "How Cursor Indexes Codebases Fast" (Engineer's Codex)

## Core Indexing Process

When codebase indexing is enabled, Cursor scans the opened folder and computes a Merkle tree of hashes of all valid files. When a file changes, Cursor splits it into syntactic chunks, which are converted into embeddings for semantic search.

## Embedding Storage

Chunk embeddings are cached by content — unchanged chunks hit the cache and are not re-embedded. Embeddings and metadata are stored in a vector database (Turbopuffer), optimized for fast semantic search across millions of code chunks. The Merkle tree lets sync operations walk only branches where hashes differ, minimizing re-transfer.

## Reported Performance

Cursor's own evaluation reports semantic search improved response accuracy by 12.5% on average, produced code changes more likely to be retained in codebases, and raised overall request satisfaction — described as "one of the biggest drivers of agent performance."

## Privacy Design

Only embeddings and metadata are stored in the cloud; original source code stays on the local machine and is never stored on Cursor's servers or in Turbopuffer. File paths are obfuscated client-side (path masking) before transmission.

## Hybrid Retrieval

The documentation page is explicitly titled "Semantic & Agentic Search," and secondary coverage (Cursor's own docs, per search synthesis) describes both an "Instant Grep" mode for exact symbols and a semantic-search mode for conceptual queries, with the agent choosing between them based on query shape — i.e., Cursor runs both agentic (grep-based) and embeddings-based semantic search as complementary modes, not one instead of the other.

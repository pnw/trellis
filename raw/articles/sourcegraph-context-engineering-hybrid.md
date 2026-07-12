# Sourcegraph — Context Engineering and Hybrid Retrieval (2026)

- Source URLs: https://sourcegraph.com/blog/context-engineering, https://sourcegraph.com/resources/context-compare, https://sourcegraph.com/blog/why-code-search-at-scale-is-essential-when-you-grow-beyond-one-repository
- Publisher: Sourcegraph (official blog/resources)
- Retrieved via: WebSearch aggregation (direct WebFetch returned HTTP 403 in this session), 2026-07-07

## Core Claim

Rather than choosing exclusively between grep-based agentic search and embeddings, "hybrid is the path most enterprise tools converge on" as of 2026. Cited example: Cursor's own docs describe both "Instant Grep" (for exact symbols) and semantic search (for conceptual queries) side by side, with the agent choosing based on query shape.

## Sourcegraph Amp's Architecture

Amp (the agentic evolution of Cody, 2025-2026) layers an agent atop Sourcegraph's longstanding code graph, backed by SCIP (structural/symbol) indexing — a precise, static-analysis-based indexing approach distinct from both raw grep and embeddings-based semantic search. Sourcegraph frames this as a production-grade context layer for coding agents operating on large codebases, with teams adopting Amp getting the code graph "by default."

## Framing Note

One secondary source aggregated in this search pass repeats the claim that "Windsurf, Cline, Devin, and Sourcegraph Amp dropped vectors for tool-driven search" as part of a broader "2026 shift" narrative. Sourcegraph's own comparison resource and context-engineering blog, by contrast, frame the actual 2026 consensus as hybrid retrieval (grep + embeddings + structural/graph indexing, selected per query type) rather than a wholesale rejection of embeddings — directly at odds with the "vectors are dead" framing found elsewhere in this same research pass.

## Relevance

This is the most direct evidence found in this session that the "industry abandoned embeddings" claim, as originally captured via a single aggregated blog source, overstates a real but narrower phenomenon (Claude Code's specific, unusually pure-grep design choice) into a general industry trend that the vendors' own documentation does not support.

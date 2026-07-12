# LLM Wiki Pattern — Karpathy's Original Gist (Primary Source)

- Source URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Author: Andrej Karpathy
- Retrieved via: WebFetch (HTML-to-markdown conversion, summarized by fetch tool), 2026-07-07
- Capture note: This is the primary gist itself, distinct from the Starmorph secondary guide already captured at [[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]]. The fetch tool returned a summarized extraction rather than the full verbatim gist text; content below is that extraction, not a byte-for-byte copy.

## Core Pattern

Karpathy's gist describes building persistent, LLM-maintained knowledge bases as an alternative to traditional RAG. Rather than retrieving raw documents at query time, the system maintains a structured wiki that synthesizes and interlinks information. Core framing: "The wiki is a persistent, compounding artifact."

## Architecture (Three Layers)

1. Raw sources — immutable document collection
2. Wiki — LLM-generated markdown files (summaries, entities, concepts)
3. Schema — configuration document defining conventions and workflows

## Scaling Considerations

**Index-based retrieval limitations:** a flat `index.md` file works "surprisingly well at moderate scale (~100 sources, ~hundreds of pages)" but the gist suggests moving to structured search infrastructure beyond that threshold.

**Search infrastructure:** for larger wikis, the recommendation is tools like `qmd` (local search with BM25/vector hybrid search) rather than embedding-based RAG infrastructure, emphasizing on-device processing.

## Notable Implementation Feedback (Gist Comments)

- Community member `@distorx` reported running this pattern in production with "4000+ interlinked concepts," noting that the lint pass became essential — "drift — the agent under-updating cross-references on ingest" was their biggest failure mode.
- `@blurman-ai` found that single-file wikis outperformed multi-page systems for code repositories, suggesting compression effectiveness depends on whether pages reduce or expand the source material.

## Key Operational Patterns

- Ingest: process new sources, update 10-15 related pages in one pass.
- Query: search wiki, synthesize answers, file valuable results back as new pages.
- Lint: periodic health checks for contradictions, staleness, orphaned pages, and coverage gaps.

The community emphasized that successful implementations require disciplined linting and that the schema document becomes "the single most important file in the repo."

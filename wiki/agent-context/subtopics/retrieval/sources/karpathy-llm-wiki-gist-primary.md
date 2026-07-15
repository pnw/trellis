---
title: LLM Wiki Pattern — Karpathy's Original Gist
type: source-capture
evidence: expert-analysis
description: Karpathy's primary gist on the LLM Wiki pattern, including explicit scale guidance (flat index works to ~100 sources/hundreds of pages) and a recommendation to graduate to local hybrid search tools rather than embedding-RAG infrastructure.
sources:
  - "[[raw/articles/karpathy-llm-wiki-gist-primary.md]]"
related:
  - "[[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]]"
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
  - "[[designs/knowledge-surfacing-design]]"
tags: [llm-wiki, knowledge-management, scale, retrieval]
created: 2026-07-07
timestamp: 2026-07-07T20:00:00Z
status: draft
---

# LLM Wiki Pattern — Karpathy's Original Gist

## Source Identity

- Author: Andrej Karpathy
- Format: GitHub gist
- URL: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

This is the primary gist itself, distinct from [[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]] (a Starmorph secondary guide *about* the gist, already captured in this wiki). It contains scale guidance and comment-thread production feedback not present in the secondary guide.

## Core Contribution

Describes the LLM Wiki pattern — persistent, LLM-maintained markdown knowledge bases as an alternative to query-time RAG — and, distinctively for this capture, gives explicit guidance on when the flat-index approach stops working and what to replace it with.

## Key Claims

- The wiki is framed as "a persistent, compounding artifact," distinct from ephemeral retrieval.
- A flat `index.md` works "surprisingly well at moderate scale (~100 sources, ~hundreds of pages)."
- Beyond that scale, the recommendation is local hybrid-search tooling such as `qmd` (BM25 + vector + rerank, on-device) rather than standing up embedding-based RAG infrastructure.
- Core operational loop: ingest (process new sources, update 10-15 related pages per pass), query (search, synthesize, file results back), lint (periodic health checks for contradictions, staleness, orphans, coverage gaps).

## Evidence and Results

No systematic measurement is presented in the gist itself; the scale threshold and tooling recommendation read as the author's own practitioner judgment rather than a benchmarked result. Corroborating production feedback appears in the comment thread:

- `@distorx` reports running the pattern at "4000+ interlinked concepts" in production, naming cross-reference drift on ingest as the dominant failure mode and lint as the essential mitigation.
- `@blurman-ai` reports that single-file wikis outperformed multi-page systems specifically for code repositories, suggesting the multi-page benefit is conditional on whether pages compress or expand the source material.

## Limitations and Caveats

- This capture is based on a WebFetch tool's summarized extraction of the gist, not a verified byte-for-byte copy of the original text — see Extraction Notes.
- The ~100-source/hundreds-of-pages threshold and the `qmd` recommendation are the originator's stated practice, not an independently measured benchmark.
- Comment-thread feedback (`@distorx`, `@blurman-ai`) is anecdotal, single-deployment, and not independently verifiable from this capture alone.

## Reliability Notes

Tiered `expert-analysis` rather than higher: this is a practitioner's own design-pattern write-up and community discussion, not a controlled study. It carries real weight as the *originating* source for the pattern this entire wiki topic is built on, which matters for design-intent claims ("what the pattern recommends") even though it says nothing about effectiveness beyond the author's own stated experience.

## Important References and Linked Material

- `qmd` — see [[wiki/agent-context/subtopics/retrieval/entities/qmd]] and [[wiki/agent-context/subtopics/retrieval/sources/qmd-tool-readme]].

## Contribution Routing

- Directly informs the "Recommendation for This Wiki" section of [[designs/knowledge-surfacing-design]] — this wiki has just crossed the ~100-page threshold this gist names.
- Corroborates (independently, as a primary source vs. the existing secondary guide) [[wiki/llm-wiki/constructs/llm-wiki-pattern]].

## Extraction Notes

Retrieved via WebFetch, which returns a markdown conversion summarized by an intermediate model rather than a guaranteed verbatim copy. Direct verification against the raw gist HTML was not performed in this session.

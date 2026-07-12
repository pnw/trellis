---
title: Claude Code's Move From Vector Search to Agentic Search
type: source-capture
evidence: expert-analysis
description: Report that Anthropic removed vector search/embeddings from Claude Code in May 2025 in favor of grep/glob-driven agentic search, with industry follow-on at Cursor, Windsurf, Cline, Devin, and Sourcegraph Amp.
sources:
  - "[[raw/articles/claude-code-agentic-search-vs-rag.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]]"
  - "[[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]]"
tags: [agent-context, retrieval, coding-agents, embeddings]
created: 2026-07-07
timestamp: 2026-07-07T20:00:00Z
status: draft
---

# Claude Code's Move From Vector Search to Agentic Search

## Source Identity

- Reported interview: Gergely Orosz, "Building Claude Code with Boris Cherny," Pragmatic Engineer newsletter, https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
- This capture is built from a WebSearch aggregation of that interview plus several corroborating secondary write-ups (see raw file for the full list) — not a direct fetch of the original interview.

## Core Contribution

Reports that Anthropic removed vector search from Claude Code in May 2025, replacing an embeddings/vector-database retrieval pipeline with grep/glob-driven "agentic search," and that several other coding-agent products followed the same path.

## Key Claims

- Claude Code originally used RAG plus a local vector database.
- Anthropic replaced this with agentic search (model-driven glob/grep/read, iteratively gathering evidence) and, per Boris Cherny, the result "outperformed everything. By a lot."
- Stated reasons for abandoning the embeddings approach: staleness (indexes going out of date), permission/security complexity, and reliability issues — not primarily a raw-quality argument against embeddings.
- Cursor hired engineers involved in the original decision; Windsurf, Cline, Devin, and Sourcegraph Amp are reported to have also dropped vector-based retrieval for code understanding.

## Evidence and Results

No benchmark numbers are reported in this capture — the claims are qualitative practitioner statements ("outperformed everything") rather than a measured comparison. This is a materially weaker evidentiary basis than a controlled study, despite the strength of the claim.

## Limitations and Caveats

- This wiki could not directly fetch the primary interview in this session (pragmaticengineer.com returned HTTP 403); the claims here are mediated through a search engine's synthesis, which may compress or slightly distort direct quotes.
- "Outperformed everything" is not quantified — no accuracy, latency, or cost numbers are attached to the comparison.
- The claim that Cursor/Windsurf/Cline/Devin/Sourcegraph Amp "dropped vectors" is reported secondhand in aggregated blog coverage, not confirmed against each product's own documentation.

## Reliability Notes

Tiered `expert-analysis`: an industry interview relayed through an independent, well-regarded technical newsletter (not Anthropic's own marketing), corroborated by multiple independent secondary write-ups converging on the same claim. Not `empirical-primary`/`empirical-secondary` because no systematic measurement is presented — this is a practitioner account of a design decision, however consequential.

## Important References and Linked Material

- Related community technical discussion: "Why Grep Beat Embeddings in Our SWE-Bench Agent (Lessons from Augment)" — https://567-labs.github.io/systematically-improving-rag/talks/colin-rag-agents/ (not independently fetched in this session; worth capturing directly in a future pass if this claim needs firmer grounding).

## Contribution Routing

- Grounds the new [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] construct.
- Directly relevant to [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]'s approach comparison — this is real-world evidence for a "no bespoke index infrastructure" option the design previously did not consider.

## Extraction Notes

Retrieved via WebSearch synthesis rather than direct article fetch; treat verbatim quotes ("outperformed everything. By a lot.") as approximately, not exactly, reproduced.

---
title: Anthropic — Code Execution with MCP
type: source-capture
evidence: vendor-claim
description: Anthropic's official engineering post proposing agents call MCP tools by writing and executing code against a filesystem-style API rather than passing tool calls/results directly through context, reporting large token reductions.
sources:
  - "[[raw/articles/anthropic-code-execution-with-mcp.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/model-context-protocol]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/mcp-code-execution-community-discussion]]"
tags: [agent-context, mcp, tool-use, token-optimization]
created: 2026-07-07
timestamp: 2026-07-07T20:00:00Z
status: draft
---

# Anthropic — Code Execution with MCP

## Source Identity

- Publisher: Anthropic (official engineering blog)
- URL: https://www.anthropic.com/engineering/code-execution-with-mcp
- Published: 2025-11-07 (per third-party citation; not independently confirmed against the original page)

## Core Contribution

Proposes that agents call MCP tools indirectly — by writing and executing code against MCP servers presented as a discoverable filesystem/code API in a sandboxed runtime — instead of routing every tool call and its full response through the model's context directly.

## Key Claims

- Direct tool calling is context-expensive: every tool definition and every response occupies tokens.
- Presenting MCP servers as code-callable APIs (agent lists servers, reads tool-definition files, writes code to invoke them) lets an agent handle more tools and larger intermediate results within the same context budget.
- A cited example workflow dropped from roughly 150,000 tokens (direct tool-call approach) to roughly 2,000 tokens (code-execution approach) — approximately 98.7% reduction.

## Evidence and Results

The reported figure is a single illustrative workflow, not a benchmark suite with a stated methodology, sample size, or comparison baseline beyond the one example. No confidence interval, task diversity, or failure-mode accounting is presented in what could be recovered for this capture.

## Limitations and Caveats

- This capture could not directly fetch anthropic.com in this session (HTTP 403); content is reconstructed from WebSearch summaries and a GitHub community discussion quoting the post, not verified against the original text.
- As a vendor's own engineering post about its own product, the reported number is self-selected and unaudited by this wiki.

## Reliability Notes

Tiered `vendor-claim`: this is Anthropic's own report about its own platform's efficiency, presented as an engineering case study rather than a controlled experiment with disclosed methodology. Per this wiki's scoped-claims rule, it is authoritative for design-intent claims (what the code-execution-with-MCP pattern is and how it works) but weak on its own for the effectiveness claim (98.7% reduction) — that claim gains independent corroboration from [[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]] and [[wiki/agent-context/subtopics/retrieval/sources/mcp-code-execution-community-discussion]], both third-party deployments reporting similar-magnitude reductions.

## Important References and Linked Material

- Community validation: [[wiki/agent-context/subtopics/retrieval/sources/mcp-github-production-code-execution-results]]
- Community discussion and dissent: [[wiki/agent-context/subtopics/retrieval/sources/mcp-code-execution-community-discussion]]
- Companion release: [[wiki/agent-context/subtopics/retrieval/sources/anthropic-advanced-tool-use]]

## Contribution Routing

- Upgrades [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]], which previously cited this same 98.7% figure only secondhand via a Synaptic Labs blog post rather than a direct capture of Anthropic's own post.
- Strengthens Approach B evidence in [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]].

## Extraction Notes

Reconstructed from WebSearch snippets and a GitHub discussion quoting the original post's problem/solution framing; the specific token figures should be treated as approximate pending a direct-fetch verification pass.

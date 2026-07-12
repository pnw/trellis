---
title: Anthropic — Advanced Tool Use (Tool Search Tool)
type: source-capture
evidence: vendor-claim
description: Anthropic's official post introducing the Tool Search Tool — an API feature letting Claude discover deferred-loading tools on demand rather than loading every tool definition upfront, reported at 85% token reduction.
sources:
  - "[[raw/articles/anthropic-advanced-tool-use-tool-search.md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]]"
tags: [agent-context, mcp, tool-use, token-optimization]
created: 2026-07-07
timestamp: 2026-07-07T20:00:00Z
status: draft
---

# Anthropic — Advanced Tool Use (Tool Search Tool)

## Source Identity

- Publisher: Anthropic (official engineering blog)
- URL: https://www.anthropic.com/engineering/advanced-tool-use
- Published: 2026 (exact date not confirmed in this session)

## Core Contribution

Introduces a "Tool Search Tool" feature for the Claude Developer Platform: tools can be marked `defer_loading: true`, making them discoverable on demand rather than always present in context, alongside a "programmatic tool calling" capability released in the same post.

## Key Claims

- Developers still declare the full tool library to the API; `defer_loading: true` tools are excluded from the always-loaded set and surfaced only when the model's discovery step selects them.
- Reported result: approximately 85% reduction in token usage attributable to tool definitions, with no reduction in the tools actually available to the model.

## Evidence and Results

As with the companion code-execution post, the reported percentage is presented as a headline result without a disclosed benchmark methodology recoverable in this capture — no task suite, sample size, or baseline configuration detail was found.

## Limitations and Caveats

- Direct fetch of anthropic.com was not possible in this session (HTTP 403); this capture is reconstructed from WebSearch summaries only, with no corroborating third-party discussion located (unlike the code-execution post, which had independent GitHub validation).
- No stated limitations or failure modes for the Tool Search Tool itself were found in available secondary coverage.

## Reliability Notes

Tiered `vendor-claim`: single-source, vendor-authored, effectiveness claim about the vendor's own platform feature, with no independent corroboration found in this research pass (contrast with [[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]], which has third-party validation). Treat the 85% figure as provisional until an independent report surfaces.

## Important References and Linked Material

- Companion release: [[wiki/agent-context/subtopics/retrieval/sources/anthropic-code-execution-with-mcp]]

## Contribution Routing

- Adds a second, more current, directly-shipped implementation example to [[wiki/agent-context/subtopics/retrieval/constructs/meta-tool-pattern]] (Anthropic's own platform feature, not just Claude Skills as a downstream consumer of the pattern).

## Extraction Notes

Built entirely from WebSearch snippet synthesis; no direct or third-party fetch was available to cross-check the figures in this session.

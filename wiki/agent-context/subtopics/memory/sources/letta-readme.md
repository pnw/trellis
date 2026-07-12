---
title: "Letta README"
type: source-capture
evidence: official-docs
description: Official Letta (formerly MemGPT) README positioning stateful agents with self-improving memory, agent-managed memory blocks, and memory skills for continual learning.
sources:
  - "[[raw/articles/letta-readme.md]]"
related:
  - "[[wiki/llm-wiki/comparisons/llm-wiki-vs-agent-memory]]"
tags: [agent-memory, stateful-agents, continual-learning, memgpt]
created: 2026-07-08
timestamp: 2026-07-08T05:00:00Z
status: stable
---

# Letta README

## Source Identity

- Raw source: [[raw/articles/letta-readme.md]]
- Source type: documentation page (project README)
- Author(s): Letta (company; project formerly MemGPT)
- Published/retrieved: retrieved 2026-07-08
- Original URL: https://github.com/letta-ai/letta
- Scope: project positioning, CLI/SDK quickstart, memory framing

## Core Contribution

Positions Letta as infrastructure for "AI with advanced memory that can learn and self-improve over time" — stateful agents whose memory persists across sessions and is managed by the agent itself rather than reconstructed per conversation.

## Key Claims

1. Agents are *stateful*: created once with an ID, then resumed across sessions — state and memory live server-side (cloud, local, or self-hosted app server), not in the prompt.
2. Memory is seeded with structured blocks at agent creation (the quickstart's `human` and `persona` fields) and evolves from there.
3. Advanced memory and continual learning ship as pre-built *skills and subagents* — memory management is agent-executed behavior, not a fixed pipeline.
4. The project is the successor to MemGPT and is model-agnostic.

## Limitations and Caveats

- The README has pivoted to CLI/SDK onboarding; the memory *architecture* itself (the MemGPT-lineage tiered core/recall/archival model) is described in external docs and the MemGPT paper, neither captured here. This capture supports positioning claims only.

## Reliability Notes

`official-docs`: authoritative for what Letta is and intends; no effectiveness evidence present. Self-improvement claims are aspiration-grade marketing language within an otherwise factual README.

## Contribution Routing

- [[wiki/llm-wiki/comparisons/llm-wiki-vs-agent-memory]] — the OS-tiered, agent-managed memory pattern as one of three comparison anchors
- Future: capture the MemGPT paper (arXiv) for the actual architecture at an empirical tier

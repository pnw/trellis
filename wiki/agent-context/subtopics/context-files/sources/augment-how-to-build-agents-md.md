---
title: "Source: How to Build Your AGENTS.md (2026)"
type: source-capture
evidence: expert-analysis
description: "Industry synthesis on context file best practices: only include non-inferable details, structure for machine parsing, accept ~20% token overhead tradeoff. Cites ETH Zurich study extensively."
sources:
  - "[[raw/articles/augment-how-to-build-agents-md.md]]"
related:
  - "[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
tags: [agent-context, context-engineering, agents, cost-optimization]
created: 2026-07-04
timestamp: 2026-07-04T22:43:00Z
---

# How to Build Your AGENTS.md (2026)

## Source Identity

- Raw source: [[raw/articles/augment-how-to-build-agents-md.md]]
- Source type: article (industry guide)
- Author(s): Ani Galstian (Augment Code)
- Published: 2026-03-31 (updated 2026-06-18)
- Original URL: https://www.augmentcode.com/guides/how-to-build-agents-md
- Scope: Comprehensive guide to writing effective AGENTS.md files, synthesizing academic research (ETH Zurich), GitHub analysis of 2,500+ repos, and OpenAI/Anthropic documentation

## Core Contribution

Synthesizes the ETH Zurich findings with industry practice into actionable guidance. Key insight: AGENTS.md should contain only what agents cannot discover independently ("non-inferable details"). Provides a template, identifies failure patterns, and quantifies the cost tradeoff (~20% inference overhead regardless of file quality).

## Key Claims

- AGENTS.md is converging as a cross-tool standard (replacing CLAUDE.md, .cursorrules, copilot-instructions.md fragmentation)
- OpenAI pioneered the format for Codex; donated to Agentic AI Foundation (AAIF) under Linux Foundation in December 2025
- LLM-generated context files are net negative: -0.5% to -2% task success at +20-23% cost
- Human-curated files: +4% task success at up to +19% cost
- "Non-Obvious Patterns" section delivers the highest signal-to-noise ratio
- Architectural overviews hurt more than they help (encourage broader file traversal without improving success)
- Context file bloat reduces task success — rules accumulate, rarely removed
- "Lost in the middle" phenomenon: agents ignore CLAUDE.md instructions in long sessions
- Prompt caching is the primary mitigation for token overhead (90% cheaper cache reads)
- Start splitting into subdirectory files when exceeding 150-200 lines
- More deeply nested files take precedence per Codex spec

## Evidence and Results

**ETH Zurich study data (cited):**
- 5/8 tested settings: LLM-generated files reduced success
- +2.45 to +3.92 additional steps per task with auto-generated files
- Removing all docs then re-adding LLM-generated file: +2.7% (proves redundancy)

**GitHub analysis of 2,500+ repos:**
- "Never commit secrets" = most common helpful constraint
- Six core sections that consistently improve agent behavior

**Cost model (Claude Sonnet 4.6 pricing):**
- 1,000 tasks/month: ~$45 overhead
- 10,000 tasks/month: ~$450 overhead
- 100,000 tasks/month: ~$4,500 overhead

**Tool comparison matrix:**
- CLAUDE.md: Plain Markdown, built-in auto-memory, no AGENTS.md interop
- Cursor .mdc: YAML frontmatter, agent-decided rule inclusion (description field)
- copilot-instructions: Plain Markdown, path-specific .instructions.md files
- .windsurf/rules: Plain Markdown, memories

## Methodology

Industry synthesis article combining: academic research (ETH Zurich paper), platform documentation (OpenAI Codex, GitHub Copilot, Anthropic), GitHub analysis of 2,500+ real repositories, and production examples from open-source repos (Vercel Next.js, Inngest, CBMC, NetCore).

## Limitations and Caveats

- Augment Code has commercial interest (Context Engine product) — article positions automated solutions favorably
- ETH Zurich findings are for coding tasks specifically — may not apply to knowledge navigation
- The "non-inferable" heuristic is context-dependent (what's inferable changes with model capability)
- Template is heavily oriented toward software development repos, not knowledge bases
- Article doesn't distinguish between context files for coding vs. context files for knowledge retrieval

## Important References and Linked Material

- [ETH Zurich paper](https://arxiv.org/abs/2602.11988) — Primary academic source for effectiveness claims
- [AGENTS.md spec repo](https://github.com/agentsmd/agents.md) — Specification and standard
- [GitHub blog: Lessons from 2,500+ repositories](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) — Empirical patterns
- [OpenAI Codex: AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) — Platform documentation
- [Anthropic: Effective Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Guidance on context management in long sessions

## Contribution Routing

- Updates: `[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]` — provides industry context around ETH Zurich findings
- Informs: design of this wiki's own steering files (what to include/exclude)
- Context for: the tradeoff between context richness and token efficiency

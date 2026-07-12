---
title: "How to Build Your AGENTS.md (2026): The Context File That Makes AI Coding Agents Actually Work"
source: https://www.augmentcode.com/guides/how-to-build-agents-md
retrieved: 2026-07-04
authors: Ani Galstian (Augment Code)
published: 2026-03-31
updated: 2026-06-18
---

AGENTS.md is a Markdown file placed at the root of a repository that provides AI coding agents with persistent, project-specific operational guidance: build commands, coding conventions, testing rules, and constraints the agent cannot infer from the codebase alone. Building an effective AGENTS.md requires writing only what agents cannot discover independently, structuring rules for machine parsing rather than human readability, and accepting a measurable inference-cost trade-off that pays off only when the file is human-curated rather than auto-generated.

## TL;DR

The central question isn't whether to create an AGENTS.md. It's whether yours will improve agent performance or just add token overhead. The ETH Zurich study found that LLM-generated context files reduced task success rates by approximately 3% on average, increased inference costs by over 20%, and required 2-4 additional reasoning steps. Human-curated files provided a marginal 4% performance gain, but still incurred the same token overhead. This guide covers the structure, content decisions, and modular organization that determines which side of that line your file lands on, plus how tools like Intent address the maintenance problem manual files can't solve at scale.

## Why AI Coding Agents Need a Context File

Every coding agent, whether Claude Code, Cursor, GitHub Copilot, or Codex, starts each session blind to your project's specific conventions. The agent knows how to write Python or TypeScript in general, but it does not know that your team uses Pixi instead of pip, that your API client never throws exceptions, or that the vendor/ directory should never be modified.

Before AGENTS.md emerged as a standard, teams maintained a patchwork of tool-specific files to communicate these constraints. An Augment blog post describes the experience: "Open a typical project that's been through a few months of AI-assisted development. You'll find some combination of CLAUDE.md, .cursorrules, and copilot-instructions.md, AGENTS.md, and maybe a Gemini.md for good measure. Almost the same content in each one. Slowly drifting apart."

The spec repo defines AGENTS.md as "Think of AGENTS.md as a README for agents: a dedicated, predictable place to provide context and instructions to help AI coding agents work on your project." OpenAI helped pioneer the AGENTS.md format for Codex, and in December 2025, it was donated to the Agentic AI Foundation (AAIF), a directed fund under the Linux Foundation, alongside Anthropic donating the Model Context Protocol (MCP) and Block donating Goose.

| File | Primary Audience | Purpose |
|------|-----------------|---------|
| README.md | Human developers | Project overview, installation, usage |
| CONTRIBUTING.md | Human contributors | How to submit PRs, code style for humans |
| AGENTS.md | AI coding agents | Build commands, test runners, conventions, constraints for autonomous agents |

## The Quality Threshold: What ETH Zurich Found About Context File Effectiveness

The ETH study evaluated multiple coding agents and LLMs across two benchmarks, comparing LLM-generated and developer-written context files and their performance relative to no repository context. The findings challenge two common practices.

**LLM-generated context files hurt performance.** In 5 out of 8 tested settings, LLM-generated files reduced task success rates. Agents took 2.45 to 3.92 additional steps per task, and inference costs increased by 20% to 23%.

**Developer-written context files help, but modestly.** Human-curated files outperformed LLM-generated files for all four agents tested, with a gain of roughly 4 percentage points on the AGENTbench benchmark.

| Context File Type | Cost Increase | Task Success Change |
|-------------------|---------------|---------------------|
| LLM-generated (auto-init) | +20 to 23% | −0.5% (SWE-bench Lite) to −2% (AGENTbench) |
| Developer-written (human-curated) | Up to 19% (shorter files, lower cost than LLM-generated) | Marginal improvement (AGENTbench) |
| No context file | Baseline | Baseline |

A critical follow-up experiment removed all other documentation from the repository before re-evaluating. Under those conditions, LLM-generated files improved performance by 2.7%, confirming the core insight: LLM-generated context files are redundant with existing documentation that agents already access independently. Duplicating that content adds cost without adding signal.

### What "Non-Inferable Details" Means in Practice

The study concludes that human-written files should describe only minimal requirements, custom-built commands, and specific tooling choices, while avoiding content that agents can already discover independently.

| Content Type | Include? | Reason |
|--------------|----------|--------|
| Custom build commands not documented elsewhere | Yes | Non-inferable |
| Highly specific tooling choices (e.g., pixi instead of pip) | Yes | Non-inferable |
| Codebase overviews and architecture summaries | No | Agents find these independently |
| Anything already in README or existing docs | No | Redundant; increases steps and cost |

Architectural overviews "do not provide effective overviews," per the study: removing an "Architecture" section while keeping only commands, constraints, and non-standard patterns produces the same agent behavior at a lower token budget.

## Core Sections for Every AGENTS.md

GitHub analysis and OpenAI docs converge on the sections that consistently improve agent behavior. Each section targets a specific class of agent errors.

### Section 1: Stack Definition With Exact Versions

Without version constraints, the agent defaults to whichever API conventions are most represented in training data.

### Section 2: Executable Commands With Full Flags

Place commands early; the agent references them repeatedly throughout a task.

### Section 3: Coding Conventions and Patterns

One real snippet showing your style beats three paragraphs describing it. The most valuable convention to document is the counterintuitive one.

### Section 4: Testing Rules

For complex build systems, exact commands matter more than guidelines.

### Section 5: "Don't Touch" Zones and Permission Boundaries

"Never commit secrets" was the most common helpful constraint across 2,500+ repositories per GitHub analysis. A three-tier system gives the agent an explicit priority hierarchy when rules interact.

### Section 6: Non-Standard Tooling

AGENTS.md delivers the highest ROI for tools underrepresented in LLM training data.

## Tool-Specific Variants: CLAUDE.md, .cursorrules, and copilot-instructions.md

AGENTS.md is converging as a cross-tool standard.

| Feature | CLAUDE.md | Cursor .mdc | copilot-instructions | .windsurf/rules |
|---------|-----------|-------------|---------------------|-----------------|
| Format | Plain Markdown | Markdown with required YAML frontmatter | Plain Markdown | Plain Markdown |
| Multi-file support | Yes | Not documented as .cursor/rules/ | Yes, .github/instructions/ | Not documented |
| File-based scoping | User vs. project level | — | Path-specific .instructions.md | — |
| Auto-memory | Built-in | Unknown | Yes (Copilot Memory) | Yes (Memories) |
| Agent-decided rule inclusion | No | Yes (description field) | No | No |
| AGENTS.md interop | No (uses CLAUDE.md) | Yes | Yes | Unknown |

## Modular Rules: When and How to Split Your Context File

A monolithic AGENTS.md loads every rule into the agent's context on every invocation. Start with a single file; split it into subdirectories when it exceeds 150-200 lines.

Per the Codex spec, more deeply nested files take precedence in case of conflicting instructions.

## The Cost Tradeoff: Roughly 20% Inference Overhead

| Metric | Value |
|--------|-------|
| Inference cost increase (LLM-generated context files) | 20 to 23% |
| Inference cost increase (developer-provided context files) | Up to 19% |
| Reasoning token increase (GPT-series, LLM-generated files) | +14% to +22% |
| Reasoning token increase (GPT-series, human-written files) | +2% to +20% |

Prompt caching is the primary mitigation; cache reads are 90% cheaper than standard input pricing.

## Failure Patterns That Undermine AGENTS.md

**Auto-generated files perform worse than no file.** LLM-generated files reduced task success rates by 0.5% to 2% while increasing inference costs by over 20%.

**Context file bloat reduces task success.** More rules do not produce better performance. The file accumulates contradictory patches and one-off fixes.

**Silent rule dropout in long sessions.** Documented Claude Code issues report agents ignoring CLAUDE.md instructions, the "lost in the middle" phenomenon. Keep files short, place critical rules early, and start new sessions for new tasks.

**Stale structural references actively mislead.** Context files documenting repository structure become liabilities when the codebase changes. Architectural overviews increased inference cost and encouraged broader file traversal without improving task success.

## From Manual Context Files to Automated Context Management

Manual AGENTS.md files face a fundamental maintenance challenge: context files drift as codebases evolve, and there is no automated way to detect staleness.

Intent takes this further with spec-driven development. Instead of maintaining a static instruction file that agents read before acting, Intent introduces living specs that agents update as they work.

| Dimension | Manual AGENTS.md | Intent's Context Engine |
|-----------|------------------|------------------------|
| Maintenance | The developer writes and updates manually | Agents update the living spec as they work |
| Scope | Single Markdown file at repo root | Real-time semantic index across hundreds of thousands of files |
| Staleness risk | Requires manual remediation after refactors | Real-time indexing |
| Work isolation | Shared across all work | Per-workspace git worktrees |
| Dependency tracking | Not built-in | Cross-service dependency tracking |

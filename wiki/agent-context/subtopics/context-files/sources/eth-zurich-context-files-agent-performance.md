---
title: "Source: Evaluating AGENTS.md — Are Repository-Level Context Files Helpful?"
type: source-capture
evidence: empirical-primary
description: "ETH Zurich study finding that LLM-generated context files hurt agent performance (-0.5 to -2%) while increasing costs (+20-23%); human-curated files help marginally (+4%)."
sources:
  - "[[raw/papers/eth-zurich-context-files-agent-performance.md]]"
related:
  - "[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]"
tags: [agent-context, context-engineering, cost-optimization, agents]
created: 2026-07-04
timestamp: 2026-07-04T22:43:00Z
---

# Evaluating AGENTS.md — Are Repository-Level Context Files Helpful?

## Source Identity

- Raw source: [[raw/papers/eth-zurich-context-files-agent-performance.md]]
- Source type: paper
- Author(s): Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev (ETH Zurich, LogicStar.ai)
- Published: 2026-02-17
- Original URL: https://arxiv.org/abs/2602.11988
- Scope: Empirical evaluation of context files (AGENTS.md, CLAUDE.md, etc.) on AI coding agent performance across multiple agents and benchmarks

## Core Contribution

First rigorous empirical evaluation of whether repository-level context files actually help coding agents. Challenges the widespread assumption that more context improves performance. Finds that LLM-generated context files are net negative (worse performance at higher cost), while human-curated files offer only marginal benefit. Establishes the principle that context files should contain only "non-inferable details."

## Key Claims

- LLM-generated context files reduced task success rates in 5 out of 8 tested settings
- LLM-generated files increased inference costs by 20–23% and required 2.45–3.92 additional reasoning steps per task
- Human-curated files provided ~4 percentage point improvement on AGENTbench
- Human-curated files still incur up to 19% inference cost overhead
- When all other documentation is removed from a repository, LLM-generated files improve performance by 2.7% — proving they are redundant with existing documentation
- Architectural overviews do not provide effective guidance: removing "Architecture" sections while keeping commands/constraints produces same agent behavior at lower token cost
- The only content that consistently helps: custom build commands, non-standard tooling choices, and constraints the agent cannot discover independently ("non-inferable details")
- "Lost in the middle" phenomenon: agents in long sessions drop rules from context files

## Evidence and Results

**Task Success:**

| Context File Type | SWE-bench Lite | AGENTbench |
|---|---|---|
| LLM-generated | −0.5% | −2.0% |
| Human-curated | Marginal | +4.0% |
| No file (baseline) | 0% | 0% |

**Cost Overhead:**

| Metric | LLM-generated | Human-curated |
|---|---|---|
| Inference cost increase | +20 to 23% | Up to 19% |
| Reasoning token increase (GPT-series) | +14% to +22% | +2% to +20% |
| Additional steps per task | +2.45 to +3.92 | Not reported separately |

**Critical ablation:** Removing all repository documentation, then re-adding LLM-generated files → +2.7% improvement. This confirms files are redundant with docs agents already read.

## Methodology

- Multiple coding agents evaluated (at least 4, specific names via Augment article: likely includes Claude, GPT-series)
- Two benchmarks: SWE-bench Lite, AGENTbench
- Comparison conditions: no context file (baseline), LLM-generated context file (auto-init), developer-written context file
- Controlled ablation removing other repository documentation

## Limitations and Caveats

- Study focused on coding agents — results may not generalize to knowledge-retrieval agents or wiki navigation agents
- "Human-curated" files were from real repositories — quality varies
- The +4% improvement for human-curated files is modest and may not justify the maintenance cost for all teams
- Does not evaluate context files for knowledge bases (only code repositories)
- The "non-inferable" heuristic is useful but not formally defined — what's inferable depends on the agent's capabilities

## Important References and Linked Material

- [AGENTS.md spec repo](https://github.com/agentsmd/agents.md) — The standard being evaluated
- [GitHub analysis of 2,500+ repositories](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/) — Patterns from real-world AGENTS.md files
- [Anthropic: Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — Related industry guidance on context management

## Contribution Routing

- Creates: `[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]` — the core finding about when/how context files help
- Updates: `[[ai-research::wiki/token-economics/syntheses/token-cost-optimization]]` — adds evidence about context overhead costs
- Informs: design decisions for this wiki's steering files (what to include, what to omit)

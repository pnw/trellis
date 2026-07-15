---
title: "Source: AGENTS.md Efficiency Study"
type: source-capture
evidence: empirical-primary
description: "Paper finding AGENTS.md associated with lower median runtime and reduced output tokens for AI coding agents on pull-request tasks."
sources:
  - "[[raw/papers/agents-md-efficiency.md]]"
related:
  - "[[designs/agent-context-portability]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]"
tags: [agent-context, context-engineering, cost-optimization, agents]
created: 2026-07-06
timestamp: 2026-07-06T00:00:00Z
---

# AGENTS.md Efficiency Study

## Source Identity

- Raw source: [[raw/papers/agents-md-efficiency.md]]
- Source type: paper
- Author(s): Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude
- Published: 2026-01-28; revised 2026-03-30
- Original URL: https://arxiv.org/abs/2601.20404
- Local PDF: `raw/papers/pdf/agents-md-efficiency.pdf`
- Extracted text: `raw/papers/pdf/agents-md-efficiency.txt`
- Scope: Runtime and token-use effects of AGENTS.md on AI coding agents handling GitHub pull requests

## Core Contribution

The paper provides a counterweight to studies emphasizing startup context cost: in its paired pull-request setting, a root AGENTS.md correlated with faster median execution and lower output token use for a Codex-based agent.

## Key Claims

- The study analyzed 10 repositories and 124 pull requests.
- Agents were run under two conditions: with AGENTS.md and without AGENTS.md.
- The study began from a corpus of repositories with agent instruction files, filtered to repositories with a single root AGENTS.md, then retained files containing conventions/best practices, architecture/project structure, or project-description content.
- The final task set used small merged PRs: additions plus deletions no greater than 100 LoC, no more than five modified files, code changes only, and PRs created after AGENTS.md was introduced.
- The agent was OpenAI Codex using gpt-5.2-codex.
- Each task was run in isolated Docker environments from the pre-merge commit.
- With AGENTS.md, median wall-clock time decreased from 98.57s to 70.34s, a 28.64% reduction.
- With AGENTS.md, median output tokens decreased from 2,925 to 2,440, a 16.58% reduction.
- Mean output tokens decreased from 5,744.81 to 4,591.46, a 20.08% reduction.
- Mean total tokens decreased from 687,632.13 to 619,321.70, a 9.93% reduction, while median total tokens slightly increased.
- The paper reports statistically significant differences for wall-clock time and output tokens using a Wilcoxon signed-rank test.
- The authors performed a manual sanity check on 50 sampled PR tasks to ensure outputs were non-empty, non-trivial code changes consistent with intended tasks, but they did not conduct a full correctness evaluation.

## Implications

Useful context can reduce downstream wandering and output verbosity. The best cross-platform design should therefore minimize duplicated startup context while preserving concise, task-shaping instructions that prevent expensive exploration.

## Limitations

- The study evaluates one Codex-based agent configuration, not Kiro, Claude Code, or multiple model families.
- The PR set is intentionally constrained to small code changes; results may not transfer to larger refactors or multi-module tasks.
- The paper measures operational efficiency, not semantic correctness, maintainability, or developer acceptance.
- The extracted text is full-paper text from the local PDF, but table and two-column ordering artifacts remain in the raw extraction.

## Contribution Routing

- Updates: `[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]`
- Creates: `[[designs/agent-context-portability]]`

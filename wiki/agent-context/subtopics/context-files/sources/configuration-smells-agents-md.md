---
title: "Source: Configuration Smells in AGENTS.md Files"
type: source-capture
evidence: empirical-primary
description: "Paper cataloging common smells in AGENTS.md and CLAUDE.md files, including Lint Leakage, Context Bloat, Skill Leakage, and Conflicting Instructions."
sources:
  - "[[raw/papers/configuration-smells-agents-md.md]]"
related:
  - "[[designs/agent-context-portability]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]"
tags: [agent-context, context-engineering, agents, maintenance]
created: 2026-07-06
timestamp: 2026-07-06T00:00:00Z
---

# Configuration Smells in AGENTS.md Files

## Source Identity

- Raw source: [[raw/papers/configuration-smells-agents-md.md]]
- Source type: paper
- Author(s): Helio Victor F. dos Santos, Vitor Costa, Joao Eduardo Montandon, Luciana Lourdes Silva, Marco Tulio Valente
- Published: 2026-06-14; revised 2026-06-19
- Original URL: https://arxiv.org/abs/2606.15828
- Local PDF: `raw/papers/pdf/configuration-smells-agents-md.pdf`
- Extracted text: `raw/papers/pdf/configuration-smells-agents-md.txt`
- Scope: Configuration smells in coding-agent context files such as AGENTS.md and CLAUDE.md

## Core Contribution

The paper provides a smell taxonomy for agent configuration files and shows that common maintenance failures are widespread in real AGENTS.md and CLAUDE.md files.

## Key Claims

- The study identifies six configuration smells for coding-agent configuration files.
- The six smells are Context Bloat, Skill Leakage, Lint Leakage, Blind References, Init Fossilization, and Conflicting Instructions.
- The smell catalog was derived from a grey literature review of 14 selected documents plus inspection of pull-request discussions.
- The prevalence analysis covers 100 popular open-source repositories with root AGENTS.md or CLAUDE.md files: 39 AGENTS.md and 61 CLAUDE.md.
- The authors initially collected 760 commits touching the files, filtered to 383 linked pull requests, and manually inspected 17 relevant PR discussions.
- They found 207 total smell instances.
- At least one smell appeared in 91 of 100 analyzed files.
- Lint Leakage affected 62% of analyzed files.
- Context Bloat affected 42% of analyzed files.
- Skill Leakage affected 35% of analyzed files.
- Blind References affected 16% of analyzed files.
- Init Fossilization affected 24% of analyzed files.
- Conflicting Instructions affected 28% of analyzed files, but its LLM-based detector had lower precision than the other LLM-detected smells.
- Context Bloat used a 200-line threshold; Init Fossilization used a one-commit threshold.
- Skill Leakage, Lint Leakage, Blind References, and Conflicting Instructions were detected with Gemini 3.1 Flash Lite prompts and then manually reviewed.
- Apriori association rules showed that Conflicting Instructions plus Skill Leakage predicted Context Bloat with 0.83 confidence.

## Implications

Cross-platform context design should avoid duplicating large manifests across tools. Duplication increases drift risk, contradictory rules, and context bloat. Thin wrappers around one canonical source are preferable when the wrapper uses native import or discovery semantics.

## Limitations

- Smell identification depends partly on grey-literature selection, manual annotation, and LLM-based detection.
- The dataset is limited to popular open-source repositories and root-level AGENTS.md/CLAUDE.md files.
- The paper measures smell prevalence, not direct downstream task success or agent cost impact.
- The extracted text is full-paper text from the local PDF, but table and two-column ordering artifacts remain in the raw extraction.

## Contribution Routing

- Creates: `[[designs/agent-context-portability]]`
- Updates: `[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]`

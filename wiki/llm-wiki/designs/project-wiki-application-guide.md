---
title: Project Wiki Application Guide
type: design
description: "Operational guide for using this research wiki as a repertoire of agentic workflow knowledge and adapting it into project-specific implementation wikis."
sources:
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]]"
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/retrieval-as-reasoning-llm-wiki]]"
related:
  - "[[wiki/llm-wiki/designs/project-wiki-template]]"
  - "[[wiki/llm-wiki/designs/multi-agent-project-wiki-pattern]]"
  - "[[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
  - "[[ai-research::wiki/intent-compiler/designs/intent-compiler-design]]"
tags: [llm-wiki, agent-workflows, context-engineering, implementation, templates]
created: 2026-07-06
timestamp: 2026-07-06T00:00:00Z
confidence: medium
novelty: exploratory
status: draft
---

# Project Wiki Application Guide

## Purpose

Turn this research wiki into a multi-agent implementation aid: a reusable repertoire of AI-tool concepts, agent workflow patterns, context-loading practices, and process designs that can be adapted into a project-specific coordination wiki.

## System Boundary

**Inside:** Durable knowledge that helps multiple agents implement projects together: workflow patterns, architectural rationale, role boundaries, handoff contracts, evaluation rubrics, known failure modes, and reusable templates.

**Outside:** Live project state, issue queues, secrets, generated logs, exact API state, and code details that can be discovered directly from the repository.

## Core Model

Use this wiki as a source library, not as a monolithic prompt. For each implementation project:

1. Read `wiki/index.md` to identify relevant concepts and designs.
2. Select only the pages needed for the project phase.
3. Adapt the selected ideas into a local project wiki or `AGENTS.md`.
4. Keep project-specific pages grounded in the local codebase and current implementation decisions.
5. Feed lessons learned back into this research wiki only when they generalize beyond one project.

This follows the [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]: index first, selected pages second, full source material only when necessary.

## Components

### Research Repertoire

The existing wiki remains the broad repertoire:

- [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] for exposing knowledge to agents.
- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] for deciding what belongs in agent context.
- [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]] for avoiding context bloat.
- [[ai-research::wiki/intent-compiler/designs/intent-compiler-design]] for structuring ambiguous implementation work.
- [[ai-research::wiki/token-economics/syntheses/token-cost-optimization]] for token-conscious implementation practices.

### Project Adaptation Layer

Each target codebase should get a compact local layer, optimized for multi-agent coordination:

- `AGENTS.md` for high-priority operational rules.
- `wiki/project-overview.md` for durable project context.
- `wiki/task-graph.md` for shared task state, dependencies, and ownership.
- `wiki/agents/` for role-specific instructions and boundaries.
- `wiki/handoffs/` for structured transfers between agents or context windows.
- `wiki/decisions/` for architectural decisions and tradeoffs.
- `wiki/workflows/` for repeatable agent workflows.
- `wiki/evals/` for acceptance criteria and regression checks.
- `wiki/error-book.md` for repeated mistakes and remediation patterns.
- `wiki/sources/` for raw or lightly captured project material.

### Feedback Layer

Implementation discoveries should be routed by scope:

- Local-only behavior stays in the project wiki.
- Reusable agent workflow lessons become candidate pages in this research wiki.
- Evidence that contradicts an existing pattern becomes an assessment or update trigger.

## Workflow / Data Flow

```
implementation task
  -> read this wiki index
  -> choose relevant repertoire pages
  -> create or update project-local context
  -> implement in the codebase
  -> run project checks
  -> record durable decisions locally
  -> promote generalized lessons back to this wiki
```

## Invariants

1. The project codebase remains authoritative for current behavior.
2. The project wiki records why decisions were made and how agents should navigate the work.
3. This research wiki stores reusable patterns, not every project-specific fact.
4. Agents should load the smallest context set that can answer the task.
5. Any high-impact claim should trace back to raw sources or project artifacts.
6. Maintenance must be owned; stale agent context is worse than missing context.

## Application Modes

| Mode | Use When | Wiki Output |
|------|----------|-------------|
| Quick implementation | Task is narrow and code reveals most context | Short `AGENTS.md` update or no wiki change |
| Ambiguous feature | Requirements, architecture, or validation are unclear | Intent artifact, decision page, workflow checklist |
| Multi-agent project | Several agents or sessions need shared context | Project overview, task graph, handoff notes |
| Research-heavy build | Implementation depends on external tools or papers | Source captures, synthesis, design page |
| Reusable pattern found | Lesson applies across projects | Promote distilled pattern into this research wiki |

## Related Constructs

- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] defines what belongs in persistent agent guidance.
- [[wiki/agent-context/subtopics/retrieval/constructs/retrieval-as-reasoning]] explains why agents should search, read, traverse, and decide sufficiency.
- [[wiki/llm-wiki/designs/multi-agent-project-wiki-pattern]] defines the coordination layer for multi-agent projects.
- [[ai-research::wiki/intent-compiler/constructs/process-weights]] helps choose how much process to apply.
- [[ai-research::wiki/intent-compiler/subtopics/semantic-ir/constructs/typed-reverse-transitions]] provides a model for routing validation failures to the right upstream artifact.

## Evidence and Rationale

- The LLM wiki effectiveness synthesis argues that wiki value comes from repeated reuse, source-grounded context, and selective loading rather than broad accumulation: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]].
- The Codex thread adds that the wiki should sit inside a larger AI project stack with tools, evals, observability, and governance: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]].
- AGENTS.md guidance and ETH Zurich findings caution against redundant or auto-generated agent context: [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]], [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]].
- Retrieval-as-reasoning research supports multi-step navigation over flat one-shot retrieval: [[wiki/agent-context/subtopics/retrieval/sources/retrieval-as-reasoning-llm-wiki]].

## Open Design Questions

- Which project artifacts should be standardized first: `AGENTS.md`, decisions, workflows, evals, or handoff notes?
- What is the minimum project wiki that measurably improves implementation quality?
- How should lessons learned be promoted from a project wiki back into this research wiki without creating noise?
- Should project-specific adaptations use the same OKF page schema or a smaller subset?

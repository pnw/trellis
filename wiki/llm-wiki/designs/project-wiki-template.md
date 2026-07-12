---
title: Project Wiki Template
type: design
description: "Reusable structure for adapting this AI research wiki into a codebase-specific knowledge base for agentic implementation workflows."
sources:
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]]"
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
related:
  - "[[wiki/llm-wiki/designs/project-wiki-application-guide]]"
  - "[[wiki/llm-wiki/designs/multi-agent-project-wiki-pattern]]"
  - "[[wiki/agent-context/subtopics/context-files/entities/agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
tags: [llm-wiki, templates, agent-workflows, implementation]
created: 2026-07-06
timestamp: 2026-07-08T12:00:00Z
confidence: medium
novelty: exploratory
status: draft
---

# Project Wiki Template

## Purpose

Provide a compact, adaptable wiki structure for a codebase where multiple AI agents will implement features, maintain context across sessions, coordinate work, and reuse project-specific knowledge without loading irrelevant material.

## System Boundary

**Inside:** Stable project context, rationale, workflows, decisions, evaluation rules, and agent-navigation guidance.

**Outside:** Secrets, live operational data, sprint status, raw logs, generated artifacts without interpretation, and implementation details already obvious from code.

## Core Model

The template has three layers:

1. **Front door context**: concise instructions and routing files that every agent can read cheaply.
2. **Coordination artifacts**: task graph, role pages, handoffs, evals, and error book.
3. **On-demand wiki pages**: project-specific pages loaded only when relevant to the task.

## Components

### Root Files

| File | Purpose | Keep Under |
|------|---------|------------|
| `AGENTS.md` | Non-inferable operational rules, commands, boundaries, and project-specific traps | 150-200 lines |
| `wiki/index.md` | Routing index with one-line descriptions for every page | Generated or reviewed on each ingest |
| `wiki/log.md` | Append-only record of meaningful wiki changes | Newest first |
| `wiki/overview.md` | Stable project synthesis and current system model | Updated after major decisions |
| `wiki/task-graph.md` | Shared task state, dependencies, owners, blockers, and acceptance checks | Updated by planner/reviewer |
| `wiki/error-book.md` | Recurring mistakes and remediation patterns | Updated after validation failures |

### Directories

| Directory | Purpose | Example Pages |
|-----------|---------|---------------|
| `wiki/sources/` | Raw-source captures or project material summaries | `api-contract-review.md`, `customer-workflow-notes.md` |
| `wiki/agents/` | Role-specific guidance and boundaries | `planner.md`, `implementer.md`, `reviewer.md`, `evaluator.md` |
| `wiki/handoffs/` | Agent/session transfer notes | `2026-07-06-auth-refactor.md` |
| `wiki/decisions/` | Durable architectural decisions and tradeoffs (ADRs); events that are immutable records, superseded rather than edited | `auth-boundary.md`, `queue-choice.md` |
| `wiki/invariants/` | Standing constraints that must always hold (state: living and repealable), each with enforcement mechanism and removal path | `single-writer-per-file.md`, `no-pii-in-logs.md` |
| `wiki/workflows/` | Repeatable agent implementation procedures | `feature-build-loop.md`, `bug-triage-loop.md` |
| `wiki/evals/` | Acceptance checks, regression suites, manual QA scripts | `checkout-regression.md` |
| `wiki/domain/` | Business concepts and vocabulary | `billing-cycle.md`, `account-state.md` |
| `wiki/architecture/` | Stable system maps and boundaries | `service-boundaries.md` |

### Minimal `AGENTS.md` Shape

```markdown
# Project Agent Guide

## Commands
- Install:
- Test:
- Lint:
- Run:

## Non-Obvious Patterns
- ...

## Boundaries
- ...

## Multi-Agent Coordination
- Check `wiki/task-graph.md` before starting work.
- Update a handoff note before stopping or transferring ownership.
- Record validation failures in `wiki/error-book.md` when they are likely to recur.

## Wiki Navigation
- Read `wiki/index.md` first.
- Read only pages relevant to the task.
- Update `wiki/log.md` after durable wiki changes.
```

## Workflow / Data Flow

```
new project
  -> create AGENTS.md and wiki/index.md
  -> create task graph, role pages, handoff template, and eval directory
  -> capture durable project context
  -> add decision/workflow/eval pages as they become necessary
  -> use index-first navigation in agent sessions
  -> prune stale pages during maintenance
```

## Invariants

1. If the code can answer it reliably, do not duplicate it in the wiki.
2. If a fact changes often, link to the live source instead of copying it.
3. If a page does not shape future decisions or workflows, it should probably stay out.
4. Every decision page should explain alternatives, rationale, and validation signals.
5. **Decisions and invariants are orthogonal registers.** A decision records a point-in-time *choice* made among alternatives (an event); an invariant records a standing constraint that must keep *holding* (state). Do not record an observed architectural constraint as a pseudo-decision — capture it as an invariant whose removal path documents what changing it would require; writing that removal analysis is what transforms an inherited constraint into a binding one. See the `decision` and `invariant` types in `schema/page-types.md`.
6. Every workflow page should name inputs, outputs, checks, and failure routing.
7. Every page should have a clear owner or maintenance trigger.
8. Every multi-agent handoff should identify changed files, open questions, risks, and the next action.

## Related Constructs

- [[ai-research::wiki/intent-compiler/designs/pilot-implementation-playbook]] uses `wiki/decisions/` from this template as the durable home for confirmed intent briefs during a pilot.
- [[wiki/agent-context/subtopics/context-files/entities/agents-md]] for root agent guidance.
- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] for context selection.
- [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]] for pruning irrelevant context.
- [[wiki/llm-wiki/constructs/three-layer-architecture]] for raw/wiki/schema separation.
- [[wiki/llm-wiki/designs/multi-agent-project-wiki-pattern]] for task graphs, role pages, handoffs, evals, and error books.

## Evidence and Rationale

- The LLM wiki effectiveness synthesis recommends durable, reusable, sourceable, decision-shaping content and warns against real-time or easily discoverable implementation details: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]].
- The Codex thread emphasizes recurring workflows, project reasoning, evals, observability, and governance as the practical integration points: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]].
- AGENTS.md research indicates human-curated, non-redundant context is more useful than generated broad overviews: [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]], [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]].

## Open Design Questions

- Should the default project template keep the full OKF frontmatter schema or use a lighter form?
- Which directories should be mandatory for very small projects?
- What lint checks best detect duplicated code facts or stale implementation claims?

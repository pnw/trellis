---
title: Multi-Agent Project Wiki Pattern
type: design
description: "Design pattern for adapting an LLM wiki into a shared context, coordination, handoff, and evaluation layer for multi-agent implementation projects."
sources:
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]]"
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
  - "[[ai-research::wiki/intent-compiler/sources/intent-compiler-deep-research-validation]]"
related:
  - "[[designs/project-wiki-template]]"
  - "[[designs/project-wiki-application-guide]]"
  - "[[ai-research::wiki/intent-compiler/constructs/agent-handoff]]"
  - "[[ai-research::wiki/intent-compiler/subtopics/semantic-ir/constructs/typed-reverse-transitions]]"
  - "[[designs/knowledge-surfacing-design]]"
tags: [llm-wiki, multi-agent, agent-workflows, context-engineering, implementation]
created: 2026-07-06
timestamp: 2026-07-15T12:00:00Z
status: draft
---

# Multi-Agent Project Wiki Pattern

## Purpose

Use a project-local LLM wiki as the shared memory, coordination surface, handoff protocol, and evaluation record for multiple agents implementing software in the same codebase.

## System Boundary

**Inside:** Shared project context, agent roles, task graph state, handoff notes, decisions, workflow contracts, validation reports, and reusable lessons.

**Outside:** Live ticket state, secrets, raw unreviewed transcripts, current production data, and exact implementation facts that the codebase already answers.

## Core Model

Multi-agent work fails when agents duplicate effort, diverge in assumptions, or lose state at handoff boundaries. The wiki provides a durable coordination layer:

1. A root context file routes every agent into the wiki.
2. A task graph tells agents what work exists and what depends on what.
3. Role pages define what each agent is allowed to change and what it must produce.
4. Handoff pages preserve decisions, open questions, and validation status across sessions.
5. Eval pages make acceptance criteria reusable and inspectable.

The pattern is deliberately artifact-first: agents coordinate through versioned files rather than raw conversation history.

## Components

| Component | Purpose |
|-----------|---------|
| `AGENTS.md` | Root rules, boundaries, commands, and wiki navigation |
| `wiki/overview.md` | Stable system model and current project intent |
| `wiki/task-graph.md` | Work decomposition, dependencies, owners, status, and blockers |
| `wiki/agents/` | Role-specific context for planner, implementer, reviewer, evaluator, researcher |
| `wiki/handoffs/` | Structured transfers between agents or context windows |
| `wiki/decisions/` | Architecture and product decisions with alternatives and rationale |
| `wiki/invariants/` | Cross-cutting constraints every agent must uphold — the rules a diff can violate without failing a test |
| `wiki/evals/` | Acceptance criteria, regression checks, manual QA, and benchmark prompts |
| `wiki/error-book.md` | Recurring mistakes, failed assumptions, and remediation patterns |

## Workflow / Data Flow

```
human intent
  -> planner updates task graph and context needs
  -> researcher gathers source-backed context when needed
  -> implementer reads assigned task + relevant context only
  -> reviewer checks diff against decisions and evals
  -> evaluator records validation results
  -> handoff captures residual state for the next agent/session
  -> reusable lessons update error-book or research repertoire
```

## Invariants

1. Every agent reads `AGENTS.md` and `wiki/index.md` before deeper context.
2. Every task has an owner, status, dependencies, and acceptance checks.
3. Every handoff names completed work, changed files, open questions, risks, and next action.
4. Agents read role-relevant context rather than the whole wiki.
5. Validation findings route back to the artifact that caused them, not just to the last agent that touched code.
6. Only one agent or explicitly coordinated group should own a file-level edit at a time.
7. The wiki records durable coordination state; ephemeral chat stays out unless distilled.

## Role Model

| Role | Reads | Writes |
|------|-------|--------|
| Planner | overview, decisions, task graph | task graph, workflow pages |
| Researcher | sources, repertoire pages, open questions | source captures, syntheses |
| Implementer | assigned task, relevant decisions, evals | code, handoff notes |
| Reviewer | diff, decisions, evals, error book | review findings, task status |
| Evaluator | eval pages, acceptance criteria | validation reports, error book |
| Librarian | index, log, stale pages, link graph | index, log, wiki maintenance |

## Evidence and Rationale

- Kiro's synthesis emphasizes cross-agent organizational memory and the risk of knowledge fragmentation across disconnected sessions: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]].
- The Codex thread emphasizes that the wiki belongs in a larger AI project stack with tools, evals, observability, and governance: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]].
- ObjectGraph frames document structure as an agent traversal problem and discusses multi-agent handoff as a context-consumption use case: [[wiki/agent-context/subtopics/retrieval/sources/objectgraph-document-injection-to-knowledge-traversal]].
- Intent compiler validation identifies coordination failures, shared state, structured handoffs, and evaluation loops as first-class risks in multi-agent systems: [[ai-research::wiki/intent-compiler/sources/intent-compiler-deep-research-validation]].
- The only operational evidence in this vault for any coordination invariant is negative: on 2026-07-08 two parallel agent sessions each added a conflicting `invariant` page-type definition, and the merge landed with live conflict markers in the shared contract files — violating invariant 6 (single writer per file) before this pattern was ever deployed. [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]] rates "multi-session concurrency is workable with git alone" plausible-but-unvalidated on exactly that n=1, and the one instance required manual reconciliation of contradictory normative definitions.

## Open Design Questions

- Should the task graph be markdown, YAML frontmatter, or a generated view over task pages?
- What locking or ownership convention is enough to prevent conflicting agent edits?
- Can the coordination invariants be enforced by anything cheaper than convention? The 2026-07-08 collision suggests convention alone fails silently.
- How much role-specific context should be duplicated in `wiki/agents/` versus linked from shared pages?
- What eval metrics best prove the wiki is improving multi-agent throughput rather than adding ceremony?

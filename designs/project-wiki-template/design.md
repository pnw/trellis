---
title: Project Wiki Template
type: design
description: "Reference layout and rationale for a codebase-specific project wiki instance: coordination meta-files, registry-typed knowledge pages, topics, and a project design surface."
sources:
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]]"
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
related:
  - "[[designs/project-wiki-application-guide]]"
  - "[[designs/multi-agent-project-wiki-pattern]]"
  - "[[wiki/agent-context/subtopics/context-files/entities/agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
tags: [llm-wiki, templates, agent-workflows, implementation]
created: 2026-07-06
timestamp: 2026-07-15T12:00:00Z
status: draft
---

# Project Wiki Template

## Purpose

Provide a compact, adaptable wiki structure for a codebase where multiple AI agents will implement features, maintain context across sessions, coordinate work, and reuse project-specific knowledge without loading irrelevant material.

## System Boundary

**Inside:** Stable project context, rationale, workflows, decisions, evaluation rules, and agent-navigation guidance.

**Outside:** Secrets, live operational data, sprint status, raw logs, generated artifacts without interpretation, and implementation details already obvious from code.

## Reconciliation with the Schema-Inheritance Model

Earlier drafts of this template prescribed free-form directories (`wiki/workflows/`, `wiki/evals/`, `wiki/domain/`, `wiki/architecture/`) alongside `wiki/task-graph.md` and `wiki/error-book.md`, while the instantiation model says instances vendor `schema/` and subset the page-type registry, with knowledge pages living in typed folders. The two are reconciled as follows (adopted 2026-07-12, pending pilot validation):

1. **Coordination meta-files are exempt from the type system**, exactly as `index.md`, `log.md`, and `roadmap.md` already are in the research wiki: `task-graph.md`, `error-book.md`, and the `handoffs/` directory are operational state and journals, not knowledge artifacts. They carry no type frontmatter and are excluded from graph metrics — consistent with the operational finding that append-only journals must be excluded from connectivity checks: [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]].
2. **Knowledge pages use registry types; designs use the design surface.** What earlier drafts called `wiki/decisions/` and `wiki/invariants/` are exactly the registry's `decision` and `invariant` types; a "workflow" page is a design (a process design) and lives as a dossier under the project's `designs/` surface per `schema/design/dossier.md`; an "eval" page is typed by its content — usually `invariant` for standing acceptance rules or `assessment` for validation results.
3. **`domain/` and `architecture/` are topics**, containing typed pages (e.g. `wiki/domain/entities/billing-cycle.md`), not special directories.
4. A project wiki's manifest records its `page_types` subset; a typical pilot subset is `[source-capture, synthesis, decision, invariant]`, plus `design_surface: true` for the `designs/` dossiers.

## Relationship to seed/

`seed/pages/` in this repo ships the materialized skeletons (index, log, overview, roadmap, moves.log); this design page is the rationale and full layout reference. If they disagree, `seed/` is what instances actually get — fix whichever is wrong.

## Core Model

The template has three layers:

1. **Front door context**: concise instructions and routing files that every agent can read cheaply.
2. **Coordination meta-files**: task graph, handoff notes, error book, and role guidance — operational state outside the type system.
3. **On-demand typed knowledge pages**: registry-typed project pages in type folders and topics, loaded only when relevant to the task.

## Components

### Root Files

| File | Register | Purpose |
|------|----------|---------|
| `AGENTS.md` | Agent context | Non-inferable operational rules, commands, boundaries, and project-specific traps; keep under 150-200 lines |
| `wiki/index.md` | Meta (exempt) | Routing index with one-line descriptions for every page; reviewed on each ingest |
| `wiki/log.md` | Meta (exempt) | Append-only record of meaningful wiki changes, newest first |
| `wiki/roadmap.md` | Meta (exempt) | Forward-looking backlog, pruned as items resolve |
| `wiki/moves.log` | Meta (exempt) | Mechanical move/delete record with tombstone dispositions |
| `wiki/overview.md` | Typed (`synthesis`) | Stable project synthesis and current system model; updated after major decisions |
| `wiki/task-graph.md` | Meta (exempt) | Shared task state, dependencies, owners, blockers, and acceptance checks; updated by planner/reviewer |
| `wiki/error-book.md` | Meta (exempt) | Recurring mistakes and remediation patterns; updated after validation failures |

### Directories

| Directory | Register | Contents |
|-----------|----------|----------|
| `wiki/sources/` | Type folder (`source-capture`) | Raw-source captures or project material summaries: `api-contract-review.md`, `customer-workflow-notes.md` |
| `wiki/decisions/` | Type folder (`decision`) | Durable architectural decisions and tradeoffs (ADRs); events that are immutable records, superseded rather than edited: `auth-boundary.md`, `queue-choice.md` |
| `wiki/invariants/` | Type folder (`invariant`) | Standing constraints that must always hold (state: living and repealable), each with enforcement mechanism and removal path; includes standing acceptance rules from the old "evals" bucket: `single-writer-per-file.md`, `no-pii-in-logs.md` |
| `wiki/assessments/` | Type folder (`assessment`) | Validation results, regression findings, and manual QA outcomes — the evaluative half of the old "evals" bucket: `checkout-regression-2026-07.md` |
| `wiki/handoffs/` | Meta (exempt) | Agent/session transfer notes: `2026-07-06-auth-refactor.md` |
| `designs/` (repo root) | Design surface | System designs and process designs as dossiers — the old "workflow" pages: `designs/feature-build-loop/design.md`, `designs/bug-triage-loop/design.md` (`schema/design/dossier.md`) |
| `wiki/agents/` | Agent context | Role-specific guidance and boundaries — adapters like `AGENTS.md`, not knowledge pages: `planner.md`, `implementer.md`, `reviewer.md`, `evaluator.md` |
| `wiki/domain/` | Topic | Business concepts and vocabulary as typed pages: `wiki/domain/entities/billing-cycle.md` |
| `wiki/architecture/` | Topic | Stable system maps and boundaries as typed pages: `wiki/architecture/syntheses/service-boundaries.md` |

Which type folders actually appear follows the manifest's `page_types` subset; small projects should start with the pilot subset and add types only when a page demands one.

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
  -> run seed/interview.md (manifest, skeleton, agent adapters)
  -> add task graph, role pages, and handoff template as coordination needs appear
  -> capture durable project context in typed pages
  -> add decision/invariant/assessment pages and design dossiers as they become necessary
  -> use index-first navigation in agent sessions
  -> prune stale pages during maintenance
```

## Invariants

1. If the code can answer it reliably, do not duplicate it in the wiki.
2. If a fact changes often, link to the live source instead of copying it.
3. If a page does not shape future decisions or workflows, it should probably stay out.
4. Coordination meta-files carry no type frontmatter and are excluded from graph metrics; every other wiki page carries a registry type from the manifest's `page_types` subset.
5. Every decision page should explain alternatives, rationale, and validation signals.
6. **Decisions and invariants are orthogonal registers.** A decision records a point-in-time *choice* made among alternatives (an event); an invariant records a standing constraint that must keep *holding* (state). Do not record an observed architectural constraint as a pseudo-decision — capture it as an invariant whose removal path documents what changing it would require; writing that removal analysis is what transforms an inherited constraint into a binding one. See the `decision` and `invariant` types in `schema/wiki/page-types/registry.md` and their per-type files.
7. Every process design (the old "workflow" pages, now `designs/` dossiers) should name inputs, outputs, checks, and failure routing.
8. Every page should have a clear owner or maintenance trigger.
9. Every multi-agent handoff should identify changed files, open questions, risks, and the next action.

## Related Constructs

- [[ai-research::wiki/intent-compiler/designs/pilot-implementation-playbook]] uses `wiki/decisions/` from this template as the durable home for confirmed intent briefs during a pilot.
- [[wiki/agent-context/subtopics/context-files/entities/agents-md]] for root agent guidance.
- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] for context selection.
- [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]] for pruning irrelevant context.
- [[wiki/llm-wiki/constructs/three-layer-architecture]] for raw/wiki/schema separation.
- [[designs/multi-agent-project-wiki-pattern]] for task graphs, role pages, handoffs, evals, and error books.

## Evidence and Rationale

- The LLM wiki effectiveness synthesis recommends durable, reusable, sourceable, decision-shaping content and warns against real-time or easily discoverable implementation details: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]].
- The Codex thread emphasizes recurring workflows, project reasoning, evals, observability, and governance as the practical integration points: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]].
- AGENTS.md research indicates human-curated, non-redundant context is more useful than generated broad overviews: [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]], [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]].
- The meta-file exemption rests on operational evidence that append-only journals and operational state distort graph metrics when counted as knowledge pages: [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]].

## Open Design Questions

- Does the meta-file exemption hold up in the pilot, or do task graphs want typed pages?
- Which directories should be mandatory for very small projects?
- What lint checks best detect duplicated code facts or stale implementation claims?

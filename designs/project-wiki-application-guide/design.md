---
title: Project Wiki Application Guide
type: design
description: "Content-curation and feedback guide for project wikis: selecting repertoire pages from the source wikis phase by phase, and routing lessons back to the wiki whose goal they serve."
sources:
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]]"
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
  - "[[wiki/agent-context/subtopics/retrieval/sources/retrieval-as-reasoning-llm-wiki]]"
related:
  - "[[designs/project-wiki-template]]"
  - "[[designs/multi-agent-project-wiki-pattern]]"
  - "[[designs/wiki-federation-and-inheritance]]"
  - "[[designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
  - "[[ai-research::wiki/intent-compiler/designs/intent-compiler-design]]"
tags: [llm-wiki, agent-workflows, context-engineering, implementation, templates]
created: 2026-07-06
timestamp: 2026-07-15T12:00:00Z
status: draft
---

# Project Wiki Application Guide

## Purpose

Guide the two jobs the instantiation flow does not do when a project wiki is created: curating repertoire content from the source wikis into the new instance, and routing lessons back out. Creating the instance itself (structure, manifest, agent adapters) is `seed/interview.md`'s job; this guide covers what to put in it and what to send back.

The source wikis are currently two — the ai-research peer is the practice repertoire (building software with AI agents: intent-compiler, ai-sdlc, token-economics, architecture-diagrams), and trellis is the method repertoire (wiki operation, agent context, retrieval, epistemic schema). After the pilot there will be several; the rules below are written per source wiki, not for these two specifically. The peer-link mechanics and inheritance model live in [[designs/wiki-federation-and-inheritance]].

## System Boundary

**Inside:** Curation — which repertoire pages a project wiki should import or link at each project phase — and promotion: which lessons leave the project wiki and where they land.

**Outside:** Instance creation (structure, manifest, agent adapters — owned by `seed/interview.md`), live project state, issue queues, secrets, generated logs, and code details that can be discovered directly from the repository.

## Core Model

Use the source wikis as source libraries, not as a monolithic prompt. For each implementation project:

1. Read each relevant source wiki's index to identify applicable concepts and designs.
2. Select only the pages needed for the current project phase.
3. Adapt the selected ideas into the project wiki or `AGENTS.md` — by peer link where the page can be read in place, by local distillation where the project needs an adapted version.
4. Keep project-specific pages grounded in the local codebase and current implementation decisions.
5. Feed lessons back to the source wikis only when they generalize beyond the one project, routed by goal (see Feedback and Promotion).

This follows the [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]: index first, selected pages second, full source material only when necessary.

## Components

### Source Repertoires

The core repertoire pointers, by source wiki:

From trellis (method repertoire):

- [[designs/knowledge-surfacing-design]] for exposing knowledge to agents.
- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] for deciding what belongs in agent context.
- [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]] for avoiding context bloat.

From ai-research (practice repertoire):

- [[ai-research::wiki/intent-compiler/designs/intent-compiler-design]] for structuring ambiguous implementation work.
- [[ai-research::wiki/token-economics/syntheses/token-cost-optimization]] for token-conscious implementation practices.

### Curation by Phase

Select from the source wikis in the order the project needs them, not up front:

1. **Bootstrap** (immediately after `seed/interview.md` has produced the instance): populate `AGENTS.md` using [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] as the filter for what goes in, and [[designs/knowledge-surfacing-design]] for how agents will find the rest.
2. **Planning and ambiguity resolution**: pull [[ai-research::wiki/intent-compiler/designs/intent-compiler-design]] and [[ai-research::wiki/intent-compiler/constructs/process-weights]] when requirements, architecture, or validation are unclear.
3. **Implementation**: pull [[ai-research::wiki/token-economics/syntheses/token-cost-optimization]] for token-conscious practices; keep per-task context selection disciplined per [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]].
4. **Validation and review**: pull [[ai-research::wiki/intent-compiler/subtopics/semantic-ir/constructs/typed-reverse-transitions]] for routing validation failures to the right upstream artifact.
5. **Maintenance**: prune imports that stopped earning their context cost; a stale curated page is worse than none.

Record what was imported and from where — promotion needs a return address, and peer-link checks follow the source wiki's move log.

### Feedback and Promotion

Implementation discoveries route by the single-goal principle: each lesson goes to the wiki whose goal it serves.

- Lessons about **building software with AI agents** (process weights that worked, intent-artifact shapes, cost tradeoffs) promote to the ai-research practice wiki.
- Lessons about **running wikis, agent context, or knowledge practice** (schema friction, curation overhead, retrieval behavior) promote to trellis.
- **Project-local facts** stay in the project wiki.
- Evidence that contradicts an existing pattern becomes an assessment or update trigger in whichever source wiki holds the pattern.

## Workflow / Data Flow

```
implementation task
  -> read source wiki indexes
  -> choose relevant repertoire pages
  -> create or update project-local context
  -> implement in the codebase
  -> run project checks
  -> record durable decisions locally
  -> promote generalized lessons to the source wiki whose goal they serve
```

## Invariants

1. The project codebase remains authoritative for current behavior.
2. The project wiki records why decisions were made and how agents should navigate the work.
3. The source wikis store reusable patterns, not every project-specific fact.
4. Agents should load the smallest context set that can answer the task.
5. Any high-impact claim should trace back to raw sources or project artifacts.
6. Maintenance must be owned; stale agent context is worse than missing context.
7. Each promoted lesson lands in exactly one source wiki — the one whose goal it serves.

## Application Modes

| Mode | Use When | Wiki Output |
|------|----------|-------------|
| Quick implementation | Task is narrow and code reveals most context | Short `AGENTS.md` update or no wiki change |
| Ambiguous feature | Requirements, architecture, or validation are unclear | Intent artifact, decision page, workflow checklist |
| Multi-agent project | Several agents or sessions need shared context | Project overview, task graph, handoff notes |
| Research-heavy build | Implementation depends on external tools or papers | Source captures, synthesis, design dossier |
| Reusable pattern found | Lesson applies across projects | Promote distilled pattern to the source wiki whose goal it serves |

## Related Constructs

- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] defines what belongs in persistent agent guidance.
- [[wiki/agent-context/subtopics/retrieval/constructs/retrieval-as-reasoning]] explains why agents should search, read, traverse, and decide sufficiency.
- [[designs/multi-agent-project-wiki-pattern]] defines the coordination layer for multi-agent projects.
- [[designs/wiki-federation-and-inheritance]] defines the peer-link and inheritance mechanics curation and promotion run on.
- [[ai-research::wiki/intent-compiler/constructs/process-weights]] helps choose how much process to apply.
- [[ai-research::wiki/intent-compiler/subtopics/semantic-ir/constructs/typed-reverse-transitions]] provides a model for routing validation failures to the right upstream artifact.

## Evidence and Rationale

- The LLM wiki effectiveness synthesis argues that wiki value comes from repeated reuse, source-grounded context, and selective loading rather than broad accumulation: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]].
- The Codex thread adds that the wiki should sit inside a larger AI project stack with tools, evals, observability, and governance: [[wiki/llm-wiki/sources/llm-wiki-effectiveness-codex-thread]].
- AGENTS.md guidance and ETH Zurich findings caution against redundant or auto-generated agent context — the reason curation is selective and phase-driven rather than bulk import: [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]], [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]].
- Retrieval-as-reasoning research supports multi-step navigation over flat one-shot retrieval: [[wiki/agent-context/subtopics/retrieval/sources/retrieval-as-reasoning-llm-wiki]].

## Open Design Questions

- What is the minimum curated import set that measurably improves implementation quality?
- How should lessons be promoted from a project wiki back to the source wikis without creating noise?
- When several source wikis exist, how does a project agent discover which one holds a relevant pattern — per-wiki index reads, or a federated index?
- Should curation default to peer links or local distillation, and what triggers converting one to the other?

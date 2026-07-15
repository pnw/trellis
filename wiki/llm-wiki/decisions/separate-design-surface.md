---
title: Separate Design Surface
type: decision
description: "Designs leave the wiki: they become lifecycle-governed dossiers on a separate designs/ surface with their own schema, superseding the design page type and the designs-die-into-decisions doctrine."
sources:
  - "[[wiki/llm-wiki/sources/design-surface-separation-claude-code-thread]]"
related:
  - "[[designs/design-surface]]"
  - "[[wiki/llm-wiki/decisions/dossier-phasing-and-types]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]]"
  - "[[designs/wiki-federation-and-inheritance]]"
tags: [llm-wiki, schema-design, meta-research, governance, design-process]
created: 2026-07-15
timestamp: 2026-07-15T14:00:00Z
status: stable
---

# Separate Design Surface

> **Amended 2026-07-15** by [[wiki/llm-wiki/decisions/dossier-phasing-and-types]], reconciling a parallel session this decision was merged without seeing. Two points change: dossier files **do** carry declared types, from a vocabulary scoped to the design surface (overriding the no-`type` containment rule below), and the dossier gains a required phasing skeleton (`phases/phase-1.md`, `phases/later.md`, `obligations.md` on live dossiers). The two-surface architecture, lifecycle, linking rules, and migration below stand unchanged; the "parent-scoped types" deferral in Alternatives resolved the same day, in transposed form.

## Context

The owner's design process begins with a fan-out — several alternative design variations evaluated against each other — which the wiki's `design` type could not accommodate: its framing was a single authoritative future-state document. The initial proposal was an `alternatives/` directory *inside* the wiki's design pages; adversarial review showed that mechanism fought the folder/type invariant, the comparison type, the design lifecycle rule, and the moves-log contract. Working through why exposed the deeper misfit: designing is a workflow, not information capture, and the `design` type was the schema's one straddler — authored-tier but classified descriptive/epistemic, carrying evidence machinery a commitment never earns. [[wiki/llm-wiki/sources/design-surface-separation-claude-code-thread]]

## Decision

Designs are not wiki pages. The method now has two content surfaces with distinct governing rules:

1. **The wiki** stays evidence-governed: claim-shaped pages whose authority derives from sources, tiers, and independence. The `design` page type is removed from the registry (eight types remain).
2. **The design surface** (`designs/`) is lifecycle-governed: commitment-shaped dossiers whose authority derives from state (`draft | active | implemented | superseded | abandoned`), organized by containment — `designs/{slug}/design.md` plus optional `alternatives/` with a `weighing.md`. Normative spec: `schema/design/dossier.md`.
3. **The schema splits** to match: `schema/wiki/` and `schema/design/`, with `schema/structure.md` shared at the root. The surfaces share general conventions (kebab-case, root-relative wikilinks, provenance discipline where claims are made) while their specifics diverge.
4. **Reference direction:** designs cite wiki pages freely; wiki pages link only to dossier roots, never into dossier internals. Dossier-root moves get `moves.log` lines; dossier-internal churn does not.
5. **Lifecycle replaces death-into-decisions:** a design does not die into anything — at a terminal state it *changes tense*, freezing as the historical record of intent. Choices with lasting rationale still get wiki `decision` pages; a dossier's `weighing.md` is working analysis, not their replacement.

All nine existing design pages migrated to dossiers with tombstones in `wiki/moves.log`.

## Alternatives Considered

- **Status quo (designs stay a wiki type)** — rejected: every design-work need (fan-outs, containment, lifecycle) had to be contorted through evidence-governed machinery; the registry's own tier/family tables showed the type never fit.
- **`alternatives/` directories inside wiki design pages** (the thread's opening proposal) — rejected: breaks the folder/type invariant, adds a second nesting mechanism beside `subtopics/`, mislabels a comparison as an assessment by location, and creates artifacts with no defined death. Its core insight — structural grouping for fan-outs — is preserved in the dossier model.
- **Sibling draft designs + comparison + decision convention** (the review's counterproposal) — rejected as the resolution, though workable short-term: it solves fan-out discoverability socially rather than structurally, and leaves the deeper workflow-vs-capture tension in place.
- **Parent-scoped types across both surfaces** (a design-scoped `comparison` distinct from a wiki-scoped one) — deferred, not rejected: a type's identity is the question it answers; decide with concrete design-surface types in hand, not in the abstract.

## Consequences

- Design fan-outs get a native home: variants in `alternatives/`, adjudication in `weighing.md`, graduation by becoming `design.md` — no ceremony imposed on single-design work.
- The wiki's epistemic machinery no longer stretches over commitments; the instigator tiers simplify (authored tier: `decision`, `invariant`; design dossiers follow the same user-instigation rule from their own schema).
- Downstream instances gain a `design_surface` manifest flag; project wikis' "workflow pages" become dossiers.
- The relationship between a completed design and the wiki (graduation of its content) is **deliberately undefined** — a recorded obligation of [[designs/design-surface]], to be designed when direct experience with a completed design exists. Candidate hypothesis noted in-thread: a completed design is structurally a candidate ingest source.
- Dossiers risk becoming knowledge traps; the standing mitigation is the rule that durable byproducts of design work flow to the wiki via normal ingest/promotion.
- This decision supersedes [[wiki/llm-wiki/decisions/designs-die-into-decisions]] and repeals the design-lifecycle rule that decision added to the old `schema/page-types/design.md` (the file is removed with the type). That decision established no standing `invariant` pages, so none need disposition.

## Invariants Established

None registered yet. The reference-direction rule and the raw-immutability-style freeze on terminal designs are stated normatively in `schema/design/dossier.md` and enforced by lint (link direction) and convention (the freeze); promote either to an `invariant` page if it accrues a removal analysis worth citing.

## Status

`stable` — adopted 2026-07-15, applied the same day (schema split, type removal, nine-dossier migration). Supersedes [[wiki/llm-wiki/decisions/designs-die-into-decisions]].

## Related Artifacts

- [[designs/design-surface]] — the design this decision ratifies, first dossier authored under its own rules
- [[wiki/llm-wiki/sources/design-surface-separation-claude-code-thread]] — the grounding thread
- [[wiki/llm-wiki/decisions/designs-die-into-decisions]] — superseded

---
title: The Design Surface
description: "Separates designs from the wiki into lifecycle-governed dossiers under designs/, with their own schema, containment as the organizing principle, and native support for alternatives fan-outs."
sources:
  - "[[wiki/llm-wiki/sources/design-surface-separation-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/decisions/separate-design-surface]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
tags: [design-process, schema-design, meta-research, governance]
created: 2026-07-15
timestamp: 2026-07-15T12:00:00Z
status: implemented
---

# The Design Surface

This dossier is the first design authored under its own rules — the design of the surface it lives on. Normative detail is in `schema/design/dossier.md`; this document is the intent and rationale record. Status `implemented`: the surface shipped with the same change that ratified this design, so this document is frozen as the record of what was intended and why.

## Purpose

Give design work — fan-out of alternatives, evaluation, convergence, execution tracking — a native home that the wiki could not provide. The wiki is durable knowledge: claim-shaped, evidence-governed, organized as a typed artifact graph. Designing is a workflow: commitment-shaped, lifecycle-governed, and best organized by containment. Forcing designs through the wiki's machinery produced a type that never fit (authored-tier yet evidence-graded) and coping doctrines like designs-die-into-decisions.

## System Boundary

**Inside:** the `designs/` directory and its dossiers; the design-surface schema (`schema/design/dossier.md`); the dossier lifecycle; the alternatives/weighing structure; the reference-direction rule; dossier cataloging and move logging.

**Outside:** the wiki's typed artifact graph and epistemic machinery (unchanged); the full design *workflow* itself — this design captures the assets and their meaning, deliberately not the process that produces them, which the owner is refining separately; any graduation path from completed designs into the wiki (see Obligations).

## Core Model

- **One dossier per design**: `designs/{slug}/` containing `design.md` plus whatever the design needs. Role comes from position, not from a type field.
- **Lifecycle is the governing axis**: `draft → active → implemented | superseded | abandoned`. A design's authority comes from its state, not its citations. At a terminal state the design *changes tense* — it freezes as the historical record of intent, durable the way a decision record is durable, never living documentation of the shipped artifact.
- **Alternatives are native**: a fan-out puts variants of similar scope in `alternatives/`, adjudicated by a `weighing.md` (trade-offs, implications, obligations, cost, blast radius). Nothing prescribes that a design must start with alternatives; when it does, the initial idea is simply the first alternative, and the winner graduates into `design.md`.
- **Containment over graph**: within the wiki, relations are links along four axes; within a dossier, relations are structure. The two models coexist because the surfaces are separate.

## Components

- `schema/design/dossier.md` — the normative spec (format, lifecycle, linking rules, index and move conventions).
- `designs/index.md` — the surface's catalog.
- `scripts/lint.py` — deterministic checks: dossier integrity, required frontmatter, valid status, no wiki-surface epistemic fields, link resolution, and the wiki-side dossier-root-only rule.
- `wiki/moves.log` — dossier roots participate in the forwarding-address contract; dossier internals do not.

## Constraints / Invariants

1. **Reference direction.** Designs cite wiki pages freely (the wiki is the design surface's evidence library); wiki pages link only to dossier roots. Dossier internals are workspace and never external link targets.
2. **No epistemic machinery on designs.** `evidence`, `confidence`, and `novelty` are wiki-surface fields; their presence on a design file is a lint error. Empirical claims a design leans on live in the wiki and are cited there.
3. **Terminal designs freeze.** Post-terminal evolution is a new design or a decision, never an edit that changes the frozen record's meaning.
4. **Designs are user-instigated.** Agents draft and propose; they do not create dossiers unprompted — same instigation rule as the wiki's authored tier.

## Obligations

Downstream implications this design creates but deliberately does not resolve:

- **The wiki relationship is undefined.** No workflow exists for how a completed (`implemented`) design's durable content relates or graduates to the wiki. Premature to define without direct experience of a completed design under this model. Candidate hypothesis when the time comes: a completed design is structurally a candidate ingest source, so graduation may cost nothing new. Until then: the two surfaces are just separate things, and durable byproducts of design work flow to the wiki through normal ingest/promotion so dossiers do not become knowledge traps.
- **Scoped types are an open idea, not a mechanism.** Whether artifact kinds are parent-scoped — a design-scoped comparison ("which candidate do we build?") differing in structure from a wiki-scoped one ("when to use X vs Y?") while sharing a name and question-shape — is deferred until the design surface has enough concrete internal artifact kinds to decide with examples rather than in the abstract.
- **Downstream guidance will lag.** Project-wiki guidance (template, application guide, multi-agent pattern) was updated mechanically for the split; the pilot instantiation must validate that "workflow pages as dossiers" actually serves a project wiki.
- **The weighing document's shape is unspecified beyond its job.** Deliberate: let real fan-outs shape it before legislating sections.

## Evidence and Rationale

- The grounding thread, including the rejected alternatives (in-wiki `alternatives/` directories; a sibling-drafts convention) and the adversarial review of all three positions: [[wiki/llm-wiki/sources/design-surface-separation-claude-code-thread]].
- The ratifying decision and its consequences: [[wiki/llm-wiki/decisions/separate-design-surface]].
- The registry misfit that evidenced the split (design as the only authored-tier descriptive type) is now only visible in git history of the old `schema/page-types/registry.md` — by design, since schema files are standalone.
- The superseded lifecycle doctrine this design replaces, kept as history: [[wiki/llm-wiki/decisions/designs-die-into-decisions]].

## Open Design Questions

- Does the first real fan-out confirm the `alternatives/` + `weighing.md` shape, or does adjudication want a different structure?
- Does `designs/index.md` stay maintained in practice, or does the catalog want generation?
- Do design dossiers eventually want their own qmd collection tuning, or is the `designs` collection plus grep enough?
- Revisit trigger (mirrored in the roadmap meta-experiment log): after the next two or three design fan-outs, assess whether the surface split served design work and whether the wiki boundary held.

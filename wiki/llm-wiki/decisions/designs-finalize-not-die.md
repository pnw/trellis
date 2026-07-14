---
title: Designs Finalize, Not Die
type: decision
description: "Reversed the design-lifecycle doctrine: with spec and phasing separated by the directory form, a design describes desired state to measure against — at the end of its implementation lifecycle it becomes finalized and immutable (phase documents retained), superseded by later designs rather than collapsed into decision pages."
sources:
  - "[[raw/chats/design-as-directory-adversarial-review.md]]"
  - "[[wiki/llm-wiki/sources/design-as-directory-brain-dump]]"
related:
  - "[[wiki/llm-wiki/decisions/design-as-directory]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[wiki/llm-wiki/designs/wiki-self-experimentation]]"
tags: [llm-wiki, schema-design, design-docs, governance, knowledge-management]
created: 2026-07-14
timestamp: 2026-07-14T14:00:00Z
status: stable
---

# Designs Finalize, Not Die

## Context

[[wiki/llm-wiki/decisions/designs-die-into-decisions]] (2026-07-12) held that a blueprint design's descriptive content rots once its artifact ships — the artifact documents itself, so the design collapses into decision pages and is slimmed or deprecated. That doctrine was premised on the single-file design: a document that mixed durable specification with transient implementation description, whose descriptive half necessarily drifted against the shipped artifact.

The directory form ([[wiki/llm-wiki/decisions/design-as-directory]]) removed that premise. With phasing and scoping split out into subsidiary documents, `design.md` is no longer "that plus a transient implementation plan" — it is a standalone statement of desired state. During the adversarial review of the directory change, the owner drew the consequence explicitly: "the design doesn't need to die … because the design is now no longer a transient artifact which describes an implementation, but which describes desired state and which can be used to measure against" ([[raw/chats/design-as-directory-adversarial-review.md]]).

## Decision

Adopted 2026-07-14, normative in `schema/page-types/design.md` (Lifecycle: Designs Finalize) and `schema/page-format.md` (`status: finalized`):

1. **A design describes desired state the system is measured against.** It is not superseded by its own implementation; it remains the reference the implementation is checked against.
2. **Live designs revise freely.** While implementation is in progress, `design.md` may evolve, phases scope work against it, and `later.md`/`follow-ups.md` are pruned as items resolve.
3. **At the end of its lifecycle through implementation, a design is finalized and therefore immutable** (`status: finalized`). Phasing matters less at that point, but phase documents are **retained, not deleted** — the directory stands as the record of what was specified and how implementation was phased against it. Nothing in it is maintained further.
4. **Supersession replaces collapse.** As systems evolve, later designs supersede or amend earlier ones; a superseding design links its predecessor, and updating `status` plus that link is the only permitted edit to a finalized design.
5. **Decision pages are decoupled from the design lifecycle.** They still record choices and rejected alternatives whenever the rationale is worth preserving on its own; what is repealed is the mandatory collapse of a shipped design into them.

[[wiki/llm-wiki/decisions/designs-die-into-decisions]] is superseded and marked deprecated; the decision pages already produced under it remain valid rationale records.

## Alternatives Considered

- **Keep die-into-decisions alongside the directory form** — rejected: the doctrine solved drift between descriptive prose and shipped artifact, and the split already isolates the drift-prone content in subsidiary documents. Collapsing a clean target specification into decision pages would destroy exactly the measure-against reference the directory form was adopted to protect.
- **Delete phase documents at finalization** — rejected by the owner: there is no reason to; retained phase files cost nothing once immutable and preserve the phasing record ([[raw/chats/design-as-directory-adversarial-review.md]]). This reverses the prune-as-phases-ship rule briefly in force under the initial directory decision.
- **Fold finalization into `deprecated`** — rejected: finalized and superseded are different states. A finalized design is complete and still authoritative as the record the system was built against; a deprecated design has been replaced. Conflating them re-loses the distinction the lifecycle exists to express.
- **A `finalized` flag as prose convention instead of a `status` value** — rejected: lifecycle state is exactly what `status` is for, and downstream tooling should be able to read immutability mechanically.

## Consequences

- `schema/page-format.md` gains `status: finalized` (design pages only); the lifecycle section of `schema/page-types/design.md` is rewritten from Blueprints Die into Decisions to Designs Finalize.
- Finalized designs become a stable measurement surface: assessments can grade the system against them without chasing a moving spec.
- The immutability contract mirrors `raw/` fidelity: a finalized design directory is a frozen record, so drift is impossible by construction rather than pruned by judgment.
- The 07-12 doctrine's first applications stand unchanged: [[wiki/llm-wiki/designs/trellis-repo-design]] stays a deprecated routing stub and the extracted decision pages remain valid — this decision governs designs from the directory form onward, and nothing is resurrected.
- The design-lifecycle meta-experiment line (adopted 2026-07-12) closes in [[wiki/roadmap]] as superseded before an evidence verdict fired; the design-as-directory line inherits the lifecycle question with a new watch item: do finalized designs actually stay untouched, and does `later.md` pruning actually happen while live?

## Invariants Established

None as pages. Finalized-design immutability is a schema operating rule in `schema/page-types/design.md`; if it proves load-bearing enough to warrant an `invariant` page (like raw-source immutability), that is a later, separate ratification.

## Status

`stable` — adopted 2026-07-14, same session as [[wiki/llm-wiki/decisions/design-as-directory]], during its adversarial review.

## Related Artifacts

- [[wiki/llm-wiki/decisions/design-as-directory]] — the structural change that removed the old doctrine's premise
- [[wiki/llm-wiki/decisions/designs-die-into-decisions]] — the superseded doctrine (kept frozen as history)
- [[raw/chats/design-as-directory-adversarial-review.md]] — the grounding ruling
- [[wiki/llm-wiki/designs/wiki-self-experimentation]] — the governing protocol for this practice change

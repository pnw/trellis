---
title: Scoped Subtypes and the Roadmap Type
type: decision
description: "Typed the design directory's subsidiary documents without growing the top-level registry: a scoped-type mechanism (parent-owned {parent}/{name} types, defined in the parent spec) giving phases a design/phase type, plus one new top-level roadmap planning type shared by wiki/roadmap.md and a design's later.md/obligations.md; renamed follow-ups.md to obligations.md."
sources:
  - "[[raw/chats/design-scoped-types-and-naming.md]]"
related:
  - "[[wiki/llm-wiki/decisions/design-as-directory]]"
  - "[[wiki/llm-wiki/decisions/designs-finalize-not-die]]"
  - "[[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]]"
  - "[[wiki/llm-wiki/designs/wiki-self-experimentation]]"
tags: [llm-wiki, schema-design, design-docs, okf, governance]
created: 2026-07-14
timestamp: 2026-07-14T14:30:00Z
status: stable
---

# Scoped Subtypes and the Roadmap Type

## Context

The directory form ([[wiki/llm-wiki/decisions/design-as-directory]]) initially left a design's subsidiary documents (`phases/*.md`, the completion follow-ups file) untyped, and the adversarial review flagged that as a hole in the epistemics: unsourced, unlinted, retrieval-visible prose that agents consume at the highest-stakes moment. The owner agreed subsidiary documents should carry designed types, but was unwilling to pay the naive cost — adding page types to the top-level registry, where each new type touches the decision tree, the instigator tiers, the lint enums, a per-type spec file, and downstream subsetting. He rejected path-derived typing outright: "the whole point of OKF is that pages have designed types," not path-inferred ones ([[raw/chats/design-scoped-types-and-naming.md]]).

The task was to give every subsidiary file a real, declared, lintable type while keeping the top-level vocabulary a flat list of independently meaningful knowledge artifacts.

## Decision

Adopted 2026-07-14. Two mechanisms plus a rename, normative in `schema/page-types/registry.md`, `schema/page-types/design.md`, `schema/page-types/roadmap.md`, `schema/page-format.md`, `schema/structure.md`, `schema/lint.md`, `scripts/lint.py`, and the contract files (`AGENTS.md`, `seed/agents-md-template.md`).

1. **Scoped types** (`schema/page-types/registry.md`, Scoped Types): a top-level type whose directory form has subsidiary pages may define scoped types for them, namespaced `{parent}/{name}`. A scoped type is a real page type (declared in frontmatter) but is defined in the parent's spec file, excluded from the type decision tree, not independently subsettable, and skeleton-placed (exempt from folder/type agreement). It is the controlled-extensibility escape valve for component pages: the registry gains a mechanism paragraph, not a row per scoped type. Precedent: spec frontmatter is already a parent-scoped mini-schema.
2. **`design/phase`** (defined in `schema/page-types/design.md`): the scoped type for `phases/phase-{n}.md`. Required `title`, `type`, `description`, `created`, `timestamp`; optional `status` (`pending`/`in-progress`/`complete`, which gives phase state a home) and `related`; `sources` exempt; no epistemic fields.
3. **`roadmap`** (new top-level type, `schema/page-types/roadmap.md`): a planning type — a pruned, forward-looking backlog of intended work, asserted and provenance-free (`sources` not required, no epistemic fields). It is top-level rather than scoped because it has an instance outside any design: `wiki/roadmap.md`. Its other instances are a design's `phases/later.md` (deferred design scope) and `obligations.md` (induced external work). Typing `wiki/roadmap.md` retires its standing meta-file exemption.
4. **Rename `follow-ups.md` → `obligations.md`**: the owner's brain dump used "follow-up items" as the genus of two split concerns (deferred design scope vs. induced external work), so naming one species with the generic term invited the misfiling the split exists to prevent. `obligations` names the species — work the design obligates of other systems.
5. **Supporting rules carried in the same change**: skeleton-required/scoped pages sit outside the instigator tiers (governed by their container's spec); planning/scoped pages are exempt from `sources` and carry no `evidence`/`confidence`/`novelty`/`enforcement`; subsidiary pages are absent from `wiki/index.md` (the design's entry represents the directory); phases are numbered without zero-padding; and `phases/` is a **complete partition of the design's scope — phase-1 + phase-N + later = everything in `design.md`**, the verifiable target for the phases directory.

## Alternatives Considered

- **Path-derived typing** (the standard filename *is* the type, no frontmatter enum) — rejected by the owner: OKF's premise is that pages carry designed types, not types inferred from location. Scoped types get the same zero-registry-growth benefit while keeping the type declared in frontmatter.
- **Add each subsidiary type to the top-level registry** — rejected: a phase or roadmap-slot page answers a parent-scoped question ("what role within this design?"), not the global question the registry vocabulary answers ("what kind of knowledge artifact?"). Registering them makes every future ingest weigh branches that can never apply — how a controlled vocabulary stops being controlled.
- **A single `plan` type for all subsidiary documents, differentiated by filename** — rejected: it buys a real registry entry *and* a type too coarse to encode the phase-vs-roadmap distinction; and it would not cover `wiki/roadmap.md`.
- **`roadmap` as a scoped `design/roadmap` type** — rejected: `wiki/roadmap.md` is a roadmap outside any design, so the type must be top-level. Making it scoped would either exclude the wiki roadmap or duplicate the type.
- **Partition the registry into artifact vs. component families** — deferred: this generalizes the scoped mechanism but institutionalizes the slippery slope; revisit only if a second directory-form type demonstrates the same structure ([[wiki/roadmap]]).
- **Leave subsidiary documents untyped** (the round-1 position) — rejected: it was the epistemics hole the adversarial review identified, and the owner directed typing once a design-context structure was defined. This is that structure.

## Consequences

- Every file in a design directory now has a declared, lintable, OKF-legible type; the top-level registry grew by exactly one type (`roadmap`) plus one mechanism paragraph.
- `roadmap` enters the type system and `wiki/roadmap.md` becomes a typed page — the remaining root meta-files (`index`, `log`, `overview`, `episodes`) stay exempt as mechanical navigation/journal surfaces; the roadmap was the odd one out.
- `scripts/lint.py` validates subsidiary pages by skeleton slot (`phase-{n}` → `design/phase`; `later`/`obligations` → `roadmap`), exempts planning types from `sources` and folder/type agreement, excludes them from composition stats and orphan detection, and requires the `obligations.md` skeleton file.
- Composition stats (derived-per-capture) still measure only the nine knowledge-graph types — planning and scoped pages are structural and do not inflate the ratio the instigator-tier work established.
- No design directories exist in this lab yet (all seven designs are single-file legacy), so the subsidiary-typing rules are forward-looking; the only concrete application now is typing `wiki/roadmap.md`. First real exercise arrives with the first converted or new design (tracked in [[wiki/roadmap]]).
- Downstream wikis inherit the mechanism, the `roadmap` type, and `design/phase` through schema sync and the updated `seed/agents-md-template.md`.

## Invariants Established

None as pages. The scoped-type mechanism and the roadmap discipline are schema operating rules, canonical in `schema/page-types/registry.md` and `schema/page-types/roadmap.md`.

## Status

`stable` — adopted and implemented 2026-07-14, same session as [[wiki/llm-wiki/decisions/design-as-directory]] and [[wiki/llm-wiki/decisions/designs-finalize-not-die]], resolving the subsidiary-typing question those left open.

## Related Artifacts

- [[wiki/llm-wiki/decisions/design-as-directory]] — the directory form whose subsidiary documents this types
- [[wiki/llm-wiki/decisions/designs-finalize-not-die]] — the lifecycle reversal from the same session
- [[raw/chats/design-scoped-types-and-naming.md]] — the grounding thread and ruling
- [[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]] — the instigator-tier model these pages sit outside of

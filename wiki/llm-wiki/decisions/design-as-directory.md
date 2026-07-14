---
title: Design as Directory
type: decision
description: "Adopted the directory form for the design page type — a standard-named target spec (design.md) separated from untyped phase documents (phases/phase-1.md required, later.md grab bag) and non-phased completion follow-ups — with directory-path linking and opportunistic conversion of legacy single-file designs."
sources:
  - "[[wiki/llm-wiki/sources/design-as-directory-brain-dump]]"
related:
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]]"
  - "[[wiki/llm-wiki/designs/wiki-self-experimentation]]"
tags: [llm-wiki, schema-design, design-docs, governance]
created: 2026-07-14
timestamp: 2026-07-14T12:00:00Z
status: stable
---

# Design as Directory

## Context

The owner observed a recurring mixing of concerns in his own use of the `design` type: design documents combine a **target specification** (the future state, which gets complicated for mature software) with **phased scoping** (usually just the first phase, and legitimately more implementation-specific — e.g. which existing abstractions and interfaces are off-limits). The result is a design page that is no longer a standalone requirements document but that *plus* a transient implementation plan — sequencing content ("do this first", end-of-step follow-ups) entangled with the spec. Follow-up items themselves conflate two things: deferred design scope, and obligations the design imposes on the rest of the system after completion ([[wiki/llm-wiki/sources/design-as-directory-brain-dump]]).

## Decision

Adopted 2026-07-14, in the distributable layer: **a design is a directory, not a single file.** Normative in `schema/page-types/design.md` (Directory Form), with location, linking, frontmatter, and lint updates in `schema/structure.md`, `schema/conventions.md`, `schema/page-format.md`, `schema/lint.md`, `schema/page-types/registry.md`, and `scripts/lint.py`.

1. **Standard file names** so any consumer knows where to look: `design.md` (the target specification — the typed page, and the only one), `phases/phase-1.md` (first implementation scope), optional further `phases/phase-N.md`, `phases/later.md` (deferred design scope), optional `follow-ups.md`. Additional files are allowed; the standard names are reserved.
2. **`phases/phase-1.md` is required in every design directory**, including unphased designs, whose phase-1 states that phase 1 implements the design in full — making "no phases" and "forgot the phases" distinguishable by construction.
3. **`later.md` is a grab bag, not a phase-2**: it removes any obligation to roadmap subsequent phases while preventing deferred items from getting lost; deliberate phasing stays available.
4. **Completion follow-ups are split from deferred scope**: obligations the design imposes outside its own boundary go to non-phased `follow-ups.md`, not into `later.md` and not into the spec.
5. **Subsidiary documents are untyped**: no frontmatter, no `type`, not in the index — parts of one design artifact, transient scoping records rather than knowledge artifacts.
6. **Links target the directory path** (a target of the form `wiki/topic/designs/slug`, never `…/slug/design`), identical to the legacy single-file target, so conversion breaks no inbound links, including peer-wiki links.
7. **Legacy single-file designs convert opportunistically** — on next substantive revision or when phase/follow-up content is first needed — via mechanical move to `slug/design.md` plus `phases/phase-1.md`, recorded in `wiki/moves.log`. No bulk migration.

## Alternatives Considered

- **Keep the single file with dedicated sections** — rejected: it is the status quo failure; the spec stops being standalone, and transient scoping churn drives the typed page's `timestamp` and diffs ([[wiki/llm-wiki/sources/design-as-directory-brain-dump]]).
- **`phase-2.md` instead of `later.md`** — rejected in the source: naming the remainder a phase implies scoping work that is "not required or necessary" at that point; `later` is deliberately a grab bag.
- **Omit `phases/` for unphased designs** — rejected in the source: absence becomes ambiguous between "no phases" and "we forgot"; a trivial phase-1 stating full implementation is cheaper than the ambiguity.
- **Completion follow-ups as a section of `design.md`** — the source left placement open ("either part of the design or as a separate non-phased document"); standardized as `follow-ups.md` because the standard-name contract is the directory's point and the spec stays a pure target specification. Agent-resolved detail, reviewable.
- **Typed pages for phase documents** — rejected: phases are transient scoping records on a shorter clock than the artifact graph; typing them would push implementation plans into the index and the epistemic machinery, recreating the mixing at the vault level.
- **Bulk migration of existing designs** — deferred in favor of opportunistic conversion: the directory-path link convention makes conversion invisible to inbound links, and manufacturing phase-1 files for already-operative protocol designs would be empty ceremony (rails, not breadcrumbs). Agent-resolved detail, reviewable.

## Consequences

- `design.md` regains its role as a standalone requirements document; implementation specificity (existing-boundary constraints, first-slice scoping) has a sanctioned home that is not the spec.
- The design lifecycle sharpens: [[wiki/llm-wiki/decisions/designs-die-into-decisions]] operates on `design.md`, while phase files are pruned as phases ship (remainders move to `later.md` or a successor phase) rather than accumulating as history.
- `scripts/lint.py` now recognizes design directories (keyed and linked by directory path), errors on incomplete skeletons (missing `design.md` or `phases/phase-1.md`) and on typed subsidiary files, and treats explicit `…/design` links as directory links for orphan counting.
- This lab's seven live single-file designs remain valid and unconverted; the first conversion under the rule is the natural first test (tracked in [[wiki/roadmap]]).
- Downstream wikis inherit the form through schema sync; this is the second post-split schema change riding the three-breadcrumb inheritance path ([[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]]).
- Consistent with [[wiki/llm-wiki/decisions/designs-die-into-decisions]], no blueprint design page was created: the change shipped directly as schema, and this decision is its rationale record.

## Invariants Established

None. The directory skeleton and untyped-subsidiary rules are schema operating rules, canonical in `schema/page-types/design.md`; per the invariant spec they are not restated as invariant pages.

## Status

`stable` — adopted and implemented 2026-07-14. Meta-experiment line open in [[wiki/roadmap]]; revisit at the first design created or converted under the rule.

## Related Artifacts

- [[wiki/llm-wiki/sources/design-as-directory-brain-dump]] — the instigating owner brain dump
- [[wiki/llm-wiki/decisions/designs-die-into-decisions]] — the lifecycle rule the split sharpens
- [[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]] — the instigator-tier context (design remains authored-tier)
- [[wiki/llm-wiki/designs/wiki-self-experimentation]] — the governing protocol for this practice change

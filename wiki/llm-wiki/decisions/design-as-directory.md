---
title: Design as Directory
type: decision
description: "Adopted the directory form for the design page type — a standard-named target spec (design.md) separated from typed subsidiary pages and non-phased completion obligations, every standard file required — with directory-path linking and opportunistic conversion of legacy single-file designs. Amended same-day across two review rounds (obligations naming, scoped subsidiary types)."
sources:
  - "[[wiki/llm-wiki/sources/design-as-directory-brain-dump]]"
  - "[[raw/chats/design-as-directory-adversarial-review.md]]"
related:
  - "[[wiki/llm-wiki/decisions/scoped-subtypes-and-roadmap-type]]"
  - "[[wiki/llm-wiki/decisions/designs-finalize-not-die]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]]"
  - "[[wiki/llm-wiki/designs/wiki-self-experimentation]]"
tags: [llm-wiki, schema-design, design-docs, governance]
created: 2026-07-14
timestamp: 2026-07-14T14:00:00Z
status: stable
---

# Design as Directory

## Context

The owner observed a recurring mixing of concerns in his own use of the `design` type: design documents combine a **target specification** (the future state, which gets complicated for mature software) with **phased scoping** (usually just the first phase, and legitimately more implementation-specific — e.g. which existing abstractions and interfaces are off-limits). The result is a design page that is no longer a standalone requirements document but that *plus* a transient implementation plan — sequencing content ("do this first", end-of-step follow-ups) entangled with the spec. Follow-up items themselves conflate two things: deferred design scope, and obligations the design imposes on the rest of the system after completion ([[wiki/llm-wiki/sources/design-as-directory-brain-dump]]).

## Decision

Adopted 2026-07-14, in the distributable layer: **a design is a directory, not a single file.** Normative in `schema/page-types/design.md` (Directory Form), with location, linking, frontmatter, and lint updates in `schema/structure.md`, `schema/conventions.md`, `schema/page-format.md`, `schema/lint.md`, `schema/page-types/registry.md`, and `scripts/lint.py`.

1. **Standard file names** so any consumer knows where to look: `design.md` (the target specification), `phases/phase-1.md` (first implementation scope), optional further `phases/phase-N.md`, `phases/later.md` (deferred design scope), `obligations.md`. Additional files are allowed; the standard names are reserved.
2. **Every standard file is required** (amended 2026-07-14 — the adversarial review showed the null-check principle was applied inconsistently, and the owner extended it to all standard files): empty concerns are stated, never inferred from a missing file. An unphased design's `phase-1.md` states that phase 1 implements the design in full; a fully-phased `later.md` says the phases cover the design; a design with no induced obligations says so in `obligations.md`. "None" and "forgot" are distinguishable by construction, everywhere.
3. **`phases/` is a complete partition of the design's scope**: phase-1 + phase-N + later = everything in `design.md`. `later.md` is the remainder that closes the partition — a grab bag, not a phase-2 — so deliberate phasing stays available but is never required.
4. **Completion obligations are split from deferred scope**: work the design imposes outside its own boundary goes to non-phased `obligations.md`, not into `later.md` and not into the spec. The name states the species (obligations induced on other systems), not the genus (any "follow-up"), so it is not confused with `later.md`'s deferred design scope (renamed from `follow-ups.md` 2026-07-14; see [[wiki/llm-wiki/decisions/scoped-subtypes-and-roadmap-type]]). Both files are **scoped roadmaps**: localized versions of `wiki/roadmap.md`'s dynamics — pruned as items resolve or graduate into phases, never append-only.
5. **Subsidiary documents are typed pages** (amended 2026-07-14; the initial decision left them untyped): `phases/phase-{n}.md` carries a scoped `design/phase` type and `later.md`/`obligations.md` carry the top-level `roadmap` type — pages have designed types, not path-inferred ones. They are skeleton-placed and absent from the index. Mechanism in [[wiki/llm-wiki/decisions/scoped-subtypes-and-roadmap-type]].
6. **Links target the directory path** (a target of the form `wiki/topic/designs/slug`, never `…/slug/design`), identical to the legacy single-file target, so conversion breaks no inbound links, including peer-wiki links.
7. **Legacy single-file designs convert opportunistically** — on next substantive revision or when phase/obligation content is first needed — via mechanical move to `slug/design.md` plus the required skeleton, recorded in `wiki/moves.log`. No bulk migration.

## Alternatives Considered

- **Keep the single file with dedicated sections** — rejected: it is the status quo failure; the spec stops being standalone, and transient scoping churn drives the typed page's `timestamp` and diffs ([[wiki/llm-wiki/sources/design-as-directory-brain-dump]]).
- **`phase-2.md` instead of `later.md`** — rejected in the source: naming the remainder a phase implies scoping work that is "not required or necessary" at that point; `later` is deliberately a grab bag.
- **Omit `phases/` for unphased designs** — rejected in the source: absence becomes ambiguous between "no phases" and "we forgot"; a trivial phase-1 stating full implementation is cheaper than the ambiguity.
- **Completion obligations as a section of `design.md`** — the source left placement open ("either part of the design or as a separate non-phased document"); standardized as its own file because the standard-name contract is the directory's point and the spec stays a pure target specification. Agent-resolved detail, reviewable.
- **Typed pages for phase documents** — initially deferred, resolved 2026-07-14 in [[wiki/llm-wiki/decisions/scoped-subtypes-and-roadmap-type]]: subsidiary pages now carry designed types (scoped `design/phase`, top-level `roadmap`) via the scoped-type mechanism, which adds the types without growing the top-level registry. Path-derived typing was rejected — OKF's premise is that pages have designed types.
- **Bulk migration of existing designs** — deferred in favor of opportunistic conversion: the directory-path link convention makes conversion invisible to inbound links, and manufacturing phase-1 files for already-operative protocol designs would be empty ceremony (rails, not breadcrumbs). Agent-resolved detail, reviewable.

## Consequences

- `design.md` regains its role as a standalone requirements document; implementation specificity (existing-boundary constraints, first-slice scoping) has a sanctioned home that is not the spec.
- The lifecycle consequence was drawn same-day in the adversarial review: with spec and phasing separated, `design.md` is no longer a transient description of an implementation, so designs **finalize as immutable records** instead of dying into decisions — [[wiki/llm-wiki/decisions/designs-finalize-not-die]], superseding [[wiki/llm-wiki/decisions/designs-die-into-decisions]].
- `scripts/lint.py` now recognizes design directories (keyed and linked by directory path), errors on incomplete skeletons (any missing standard file) and on wrongly-typed subsidiary pages, and treats explicit `…/design` links as directory links for orphan counting.
- This lab's seven live single-file designs remain valid and unconverted; the first conversion under the rule is the natural first test (tracked in [[wiki/roadmap]]).
- Downstream wikis inherit the form through schema sync; this is the second post-split schema change riding the three-breadcrumb inheritance path ([[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]]).
- No blueprint design page was created: the change shipped directly as schema, and this decision is its rationale record.

## Invariants Established

None. The directory skeleton and subsidiary-typing rules are schema operating rules, canonical in `schema/page-types/design.md` and `schema/page-types/registry.md`; per the invariant spec they are not restated as invariant pages.

## Status

`stable` — adopted and implemented 2026-07-14, amended the same day across two review rounds. Round 2 (adversarial review, [[raw/chats/design-as-directory-adversarial-review.md]]): the null check extends to every standard file, `later.md`/`obligations.md` carry scoped-roadmap semantics, and the lifecycle consequence became [[wiki/llm-wiki/decisions/designs-finalize-not-die]]. Round 3 (naming and typing, [[raw/chats/design-scoped-types-and-naming.md]]): `follow-ups.md` renamed to `obligations.md`, and subsidiary pages typed via [[wiki/llm-wiki/decisions/scoped-subtypes-and-roadmap-type]]. Meta-experiment line open in [[wiki/roadmap]]; revisit at the first design created or converted under the rule.

## Related Artifacts

- [[wiki/llm-wiki/sources/design-as-directory-brain-dump]] — the instigating owner brain dump
- [[wiki/llm-wiki/decisions/designs-finalize-not-die]] — the lifecycle reversal this split enabled
- [[wiki/llm-wiki/decisions/scoped-subtypes-and-roadmap-type]] — the typing mechanism for the subsidiary pages
- [[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]] — the instigator-tier context (design remains authored-tier)
- [[wiki/llm-wiki/designs/wiki-self-experimentation]] — the governing protocol for this practice change

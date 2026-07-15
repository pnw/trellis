---
title: Dossier Phasing and Surface-Scoped Types
type: decision
description: "Reconciled two parallel sessions on the design-type rethink: dossiers gain a required phasing skeleton (phases/phase-1 + later + obligations, a complete partition of the design's scope) and a type vocabulary scoped to the design surface (design|phase|roadmap|alternative|weighing), amending the separation decision's no-type containment rule."
sources:
  - "[[raw/chats/design-phasing-reconciliation.md]]"
  - "[[wiki/llm-wiki/sources/design-as-directory-brain-dump]]"
  - "[[raw/chats/design-as-directory-adversarial-review.md]]"
  - "[[raw/chats/design-scoped-types-and-naming.md]]"
related:
  - "[[wiki/llm-wiki/decisions/separate-design-surface]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[designs/design-surface]]"
tags: [llm-wiki, schema-design, design-process, okf, governance]
created: 2026-07-15
timestamp: 2026-07-15T14:00:00Z
status: stable
---

# Dossier Phasing and Surface-Scoped Types

## Context

The owner ran two parallel sessions on the same brain dump ([[wiki/llm-wiki/sources/design-as-directory-brain-dump]]) and they resolved it differently. The session behind [[wiki/llm-wiki/decisions/separate-design-surface]] (merged first) answered the *fan-out* problem: designs left the wiki for lifecycle-governed dossiers, organized by containment, with no `type` field on design files. The other session answered the *mixing* problem the dump actually opened with — target specification entangled with transient phased scoping — via a standard-named phasing skeleton, a null-check rule (every standard file required, empty concerns stated), typed subsidiary pages, and a scoped-type mechanism to type them without registry growth ([[raw/chats/design-as-directory-adversarial-review.md]], [[raw/chats/design-scoped-types-and-naming.md]]).

The merged dossier model left the mixing problem unsolved — its `design.md` still carried an Obligations section and had no phasing story — and the two sessions ruled oppositely on typing: "pages must have types" versus "role from position, not from a type field." The owner directed a reviewed reconciliation and ruled on the conflicts ([[raw/chats/design-phasing-reconciliation.md]]).

## Decision

Adopted 2026-07-15, all in `schema/design/dossier.md` (with `scripts/lint.py` enforcement); amends [[wiki/llm-wiki/decisions/separate-design-surface]] without disturbing the two-surface architecture:

1. **The dossier gains the phasing skeleton.** `phases/phase-1.md` (first implementation scope — where existing-boundary constraints and "what will have been built" get specific), optional deliberate `phase-N.md` files, `phases/later.md` (deferred design scope), and `obligations.md` (work the design's completion imposes outside its boundary — the species, not the "follow-up" genus). `design.md` stays a pure target specification: no Obligations section, no sequencing content.
2. **`phases/` is a complete partition of the design's scope: phase-1 + phase-N + later = everything in `design.md`** — the verifiable target. `later.md` is the remainder that closes the partition; both roadmap files are pruned as items resolve, never append-only.
3. **The null check, scoped to live dossiers.** Every standard file is required while a dossier is `draft` or `active`, with empty concerns stated. Terminal dossiers are frozen records: the freeze rule forbids adding files, so they are exempt by construction — which is also what made migration honest (no skeleton backfill into `implemented`/`superseded` dossiers; the seven live dossiers were backfilled).
4. **The design surface carries its own type vocabulary, scoped to dossiers:** `design | phase | roadmap | alternative | weighing`, defined in the dossier spec, never valid on wiki pages (and wiki types never valid on the surface). Every standard dossier file declares its type; skeleton slot and declared type must agree (lint-checked). This overrides the separation decision's no-type rule — pages have designed types on every surface — while keeping its containment insight: the path fixes location, the type makes the file self-describing.
5. **Freeze retains the phasing record.** At a terminal state the whole dossier freezes — phase documents are retained, not deleted; while live, a completed phase's remainder moves to `later.md` or a successor phase.
6. **The wiki registry is untouched** (eight types). No `roadmap` wiki type: the surface split obviates the sharing motivation, and the design-side roadmap files are typed by the surface vocabulary. `wiki/roadmap.md` remains a meta-file.

## Alternatives Considered

- **Containment without declared types** (the merged spec's rule) — overruled by the owner: "pages must have types," and a spec merged in ignorance of a parallel ruling cannot claim ratification against it. The declared type is deliberate redundancy: self-description for consumers that read content without paths ([[raw/chats/design-phasing-reconciliation.md]]).
- **Path-derived typing** — rejected earlier in the thread lineage: the point of OKF-style pages is designed types, not inferred ones ([[raw/chats/design-scoped-types-and-naming.md]]).
- **A `roadmap` wiki registry type shared across surfaces** — adopted in the unmerged session, dropped here: with two surfaces, a type cannot span them, and the design surface's own vocabulary covers `later.md`/`obligations.md`. Whether `wiki/roadmap.md` should be typed under the pages-must-have-types principle is deferred to [[wiki/roadmap]].
- **Wiki-parent scoped types (`design/phase`)** — the unmerged session's mechanism, transposed rather than dropped: with `design` no longer a wiki type, "scoped to a parent type" became "scoped to a surface." This resolves, in transposed form, the scoped-types deferral recorded in [[wiki/llm-wiki/decisions/separate-design-surface]].
- **Skeleton required on all dossiers including terminal** — rejected: it would force invented phase history into frozen records, violating the freeze rule the surface is built on.
- **`finalized` lifecycle state** — folded into `implemented`: the merged enum is richer (`abandoned`, `active`/`draft` split) and its terminal-freeze semantics already are finalization.

## Consequences

- The brain dump's two halves are now both solved on one model: fan-outs via `alternatives/` (separation session), spec/phasing separation via `phases/` + `obligations.md` (this lineage) — and the two mechanisms compose: alternatives are draft-state workspace, phases are post-ratification scoping.
- `scripts/lint.py` validates dossier files by skeleton slot (type agreement, required fields, phase/lifecycle status enums, epistemic fields still errors), requires the skeleton on live dossiers only, and keeps the dossier-root-only link rule.
- All ten dossiers carry `type: design`; the seven live dossiers carry backfilled skeletons (backfill noted in file bodies; [[designs/wiki-federation-and-inheritance]]'s skeleton is the first with real deferred scope — its Phase 2–3 roadmap and invariant-page obligations).
- The unmerged session's wiki-frame artifacts (a `roadmap` registry type, `design/phase` under a wiki parent, a `finalized` status, registry scoped-type clause) were not carried; its raw record is preserved in full across the three prior chat captures.
- Downstream instances with `design_surface: true` inherit the skeleton and type vocabulary through `schema/design/dossier.md`.

## Invariants Established

None as pages. The partition rule, null check, and surface-type agreement are schema operating rules in `schema/design/dossier.md`, lint-enforced.

## Status

`stable` — adopted and implemented 2026-07-15, reconciling the parallel-session divergence the same day the separation merged.

## Related Artifacts

- [[wiki/llm-wiki/decisions/separate-design-surface]] — the amended base decision (two-surface architecture unchanged)
- [[wiki/llm-wiki/sources/design-as-directory-brain-dump]] — the shared instigating dump
- [[raw/chats/design-phasing-reconciliation.md]] — the reconciliation rulings
- [[designs/design-surface]] — the frozen dossier of the separation (its body predates this amendment by design)

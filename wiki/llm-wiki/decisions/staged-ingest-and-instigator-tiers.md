---
title: Staged Ingest and Instigator Tiers
type: decision
description: "Adopted three instigator tiers (capture/interpretive/authored) governing who creates which page types and when, a two-stage ingest that ends capture before vault-aware review, spec frontmatter on page-type files, and lint composition stats — correcting derived-layer sprawl observed across downstream instances."
sources:
  - "[[wiki/llm-wiki/sources/staged-ingest-instigator-tiers-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
  - "[[wiki/llm-wiki/designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/designs/wiki-self-experimentation]]"
  - "[[wiki/llm-wiki/decisions/adopt-single-goal-federation]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
tags: [llm-wiki, schema-design, ingest, governance, knowledge-management]
created: 2026-07-13
timestamp: 2026-07-13T12:00:00Z
status: stable
---

# Staged Ingest and Instigator Tiers

## Context

The owner operates several downstream instances of this method (~4–5), and reported that in them agents treat synthesizing captured material into derived document types as their primary job, producing wikis of "obtuse and wordy documents in a crazy graph" ([[wiki/llm-wiki/sources/staged-ingest-instigator-tiers-claude-code-thread]]). Measurements taken during the review found this lab itself healthy — 0.77 derived pages per capture in the research topic, median construct/entity inbound-link degree ~7 — which localized the defect: instances sharing only the vendored schema and the operator reproduce the failure, so the missing guidance lived in the operator's head rather than the distributable layer. The registry's decision tree answered "what type is this page?" but nothing in the schema answered "should this page exist, and on whose initiative?" ([[wiki/llm-wiki/sources/staged-ingest-instigator-tiers-claude-code-thread]]).

## Decision

Adopted 2026-07-13, all in the distributable layer:

1. **Instigator tiers** (`schema/page-types/registry.md`): page types classify into three tiers by who instigates creation — **capture** (`source-capture`: ingest-instigated, one per meaningful source), **interpretive** (`construct`, `entity`, `synthesis`, `comparison`, `assessment`: agent- or user-instigated when a trigger fires), and **authored** (`design`, `decision`, `invariant`: user-instigated; agents draft and propose but do not create unprompted).
2. **Interpretive-tier rules**: ingest is an occasion for interpretation, not a justification; the promotion test asks whether the wiki will reason with a concept again independent of its introducing source (recurrence is retrospective evidence, novel load-bearing concepts are prospective evidence, mere mention is neither); single-source promotion is priced by the existing confidence-derivation rules, not prohibited.
3. **Two-stage ingest** (`schema/ingest.md`): Stage 1 (capture) is bounded, source-isolated, and delegable to a capture agent with no vault context, ending at the source-capture with routing *candidates*; Stage 2 (review and routing) is vault-aware, consumes the capture instead of the raw source, and owns the user discussion, promotion decisions, contradiction detection, backlink audit, and confidence re-derivation. The stage boundary is normative even when one agent executes both.
4. **Spec frontmatter**: files under `schema/page-types/` carry minimal machine-readable frontmatter (`spec`, `type`, `tier`, `instigators`, `status`, `updated`) as a diffable upgrade surface for downstream wikis.
5. **Composition observability**: `scripts/lint.py` prints per-type page counts and per-topic derived-per-capture ratios as stats — explicitly never findings or targets.

## Alternatives Considered

- **Recurrence gate** (a construct requires ≥2 citing captures) — rejected: a rail duplicating existing machinery. The confidence derivation rules already price single-source pages (`medium` ceiling at best), and genuinely novel single-source concepts are legitimate promotions; the owner: a single ingest is "allowed, even expected where appropriate," to spawn interpretive pages ([[wiki/llm-wiki/sources/staged-ingest-instigator-tiers-claude-code-thread]]).
- **Hard pipeline — ingest must stop at capture, mandatory separate synthesis pass** — rejected: deferred synthesis with no named trigger leaves contradiction adjudication ownerless, and a mandated pipeline violates breadcrumbs-over-rails. Retained instead as a normative stage boundary with judgment concentrated at review.
- **A dedicated "gestalt" super-type for holistic interpretation** — rejected: it would recreate the monolithic editorializing the owner's early iterations outgrew, and the wordiest, least-navigable pages are already the large integrative ones. The gestalt is the derived graph itself; the existing interpretive types are its parts ([[wiki/llm-wiki/sources/staged-ingest-instigator-tiers-claude-code-thread]]).
- **Composition quotas or target ratios** ("most material should be source capture") — rejected as Goodhart-able; the owner withdrew the framing in favor of observability. Stats are printed, never enforced.
- **Leaving guidance to per-instance prompt iteration** — rejected: the failure reproduces across instances that share only schema and operator, so prompt-level fixes do not travel; the correction must live in the vendored surface (`schema/`, `seed/agents-md-template.md`).

## Consequences

- A context-free Stage 1 capture agent mechanically enforces [[wiki/llm-wiki/constructs/source-isolation]] — the capture cannot import vault framing it never saw — and gives ingest a bounded, independently judgeable unit of work.
- Contradiction detection is now an explicit Stage 2 responsibility (a context-free capturer cannot see the vault); adjudication remains downstream in syntheses/assessments, never in captures.
- The legacy "discuss before writing anything" step relocates to Stage 2, where interpretation actually happens — preserving its original purpose (the user weighs in on interpretation) in its proper place.
- Downstream wikis inherit the tiers through schema sync plus the updated `seed/agents-md-template.md`; this is the first post-split schema change, so it also arms the three-breadcrumb inheritance exercise ([[wiki/llm-wiki/decisions/adopt-single-goal-federation]]).
- Follow-on obligations (tracked in [[wiki/roadmap]]): ingest the downstream friction reports so the motivating evidence becomes citable rather than owner anecdata; revisit the interpretive tier's plural-instigator blurriness once downstream data exists; decide whether spec frontmatter extends beyond `schema/page-types/`.
- Consistent with [[wiki/llm-wiki/decisions/designs-die-into-decisions]], no blueprint design page was created: the change shipped directly as schema, and this decision is its rationale record.

## Invariants Established

None. The tier table and the occasion-not-justification rule are schema operating rules, canonical in `schema/page-types/registry.md` and `schema/ingest.md`; per the invariant spec they are not restated as invariant pages.

## Status

`stable` — adopted and implemented 2026-07-13. Meta-experiment line open in [[wiki/roadmap]] with a downstream-data revisit trigger.

## Related Artifacts

- [[wiki/llm-wiki/sources/staged-ingest-instigator-tiers-claude-code-thread]] — the grounding thread
- [[wiki/llm-wiki/constructs/source-isolation]] — the invariant-construct the staged capture operationalizes
- [[wiki/llm-wiki/designs/evidence-tier-schema]] — the pricing machinery the promotion rules lean on
- [[wiki/llm-wiki/designs/wiki-self-experimentation]] — the governing protocol for this practice change
- [[wiki/llm-wiki/decisions/adopt-single-goal-federation]] — the federation context that makes downstream friction arms-length evidence

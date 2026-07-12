---
title: Evidence Tier Schema
type: design
description: This wiki's two-axis epistemic schema — a required evidence tier on source-captures and rule-derived confidence on downstream pages — adapted from Admiralty, ICD 203, and GRADE.
sources:
  - "[[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]]"
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
  - "[[wiki/llm-wiki/entities/open-knowledge-format]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
tags: [epistemics, schema-design, provenance, evidence-grading, lint]
created: 2026-07-07
timestamp: 2026-07-12T07:00:00Z
confidence: low
novelty: exploratory
status: stable
---

# Evidence Tier Schema

Epistemic note (GRADE-style): by this schema's own derivation rules, confidence is `low` — the design traces to an LLM-generated design conversation and is unpiloted here — yet the recommendation to adopt was strong, because it adapts long-established frameworks and the cost of adoption is one frontmatter field plus lint rules. Certainty of evidence and strength of recommendation are separate axes; this page is the worked example.

## Purpose

Replace the single self-asserted `confidence` scalar — which conflated source authority, claim credibility, freshness, and usefulness — with a two-axis schema in which source reliability is asserted once at ingest and claim credibility is derived by rule. Adopted into `AGENTS.md` and `schema/page-format.md` on 2026-07-07. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

## System Boundary

**Inside:** The `evidence` field on source-captures, the `confidence` derivation rules for downstream pages, the Reliability Notes convention, independence rules, and the corresponding lint checks.

**Outside:** Freshness governance (handled by `timestamp` + lint staleness rules), usefulness (revealed by inbound links, never asserted), and claim-level inline citation (already required by the contract).

## Core Model

Two axes, two layers — the wiki's page-type structure carries the Admiralty two-axis system distributed across layers:

```
raw source (immutable)
  -> source-capture: evidence tier        ← reliability axis, assigned in isolation at ingest
  -> synthesis / construct / design /
     assessment / comparison: confidence  ← credibility axis, derived from cited sources
```

The credibility axis lives downstream because assigning it requires the cross-vault view (independence, corroboration, contradiction) — placing it on captures would violate [[wiki/llm-wiki/constructs/source-isolation]], rot as new sources arrive, and aggregate at the wrong granularity. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

## Components

### `evidence` tiers (source-captures, required)

A six-tier reliability scale assigned once at ingest from the source's *type*, adjustable downward GRADE-style on capture-time signals. The tier list, definitions, and adjustment rule are normative in `schema/page-format.md`; the rationale for assigning it in isolation is that reliability is a property of the source alone, which is what keeps the field compatible with source isolation.

### `confidence` derivation (non-source pages)

A three-level credibility ceiling derived from the count, tier, and independence of the page's cited sources — never asserted above it. The ceiling table, the independence rule, and the scoped-claims rule are normative in `schema/page-format.md`; this page keeps only their motivations. The independence rule exists because corroboration counting without it produced the motivating inconsistency below — non-independent sources multiplying into false confidence, with an LLM synthesis cited alongside the sources it summarized as the canonical circular-reporting shape. The scoped-claims rule exists because self-descriptive sources are authoritative about their own design intent but structurally conflicted about their own effectiveness, so the two claim scopes must hit different ceilings.

### Reliability Notes (source-capture section)

Within-source credibility signals assessable from the source alone: methodology transparency, sample size, conflict of interest, firsthand vs relayed claims, internal consistency. Justifies tier adjustments; keeps the capturer's judgment structurally separate from reportage.

### Lint enforcement

Lint enforces field placement, tier validity, derivation ceilings, and independence honesty; full rules in `schema/lint.md`.

## Workflow / Data Flow

```
ingest source
  -> assign evidence tier (type gives starting tier; Reliability Notes may lower it)
  -> route contributions downstream
  -> re-derive confidence on touched pages (corroboration can raise; contradiction lowers)
  -> lint verifies: tiers present, ceilings respected, independence honest
```

## Invariants

1. `evidence` is assignable from the source alone — never requires the cross-vault view (preserves source isolation).
2. `confidence` is derived, never asserted above its ceiling.
3. Independence is required for corroboration; derivation chains and shared interests collapse to one source.
4. Freshness and usefulness are never assertable fields.
5. A frontmatter field earns its place only if it changes agent behavior (schema-level [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]).

## Related Constructs

- [[wiki/llm-wiki/constructs/source-isolation]] — the invariant that fixes which axis lives where
- [[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]] — the framework survey this design adapts
- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] — the field-earns-its-place test

## Evidence and Rationale

- Two-axis convergence across Admiralty, ICD 203, and GRADE; claim-level trust from Wikipedia practice; computed/decaying trust from product patterns: [[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]].
- Motivating inconsistency: pages sourced entirely from vendor documentation carried `confidence: high` under the old corroboration-count definition, because non-independent corroboration was counted. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

## Open Design Questions

- Should confidence derivation be fully scripted (computable from frontmatter alone) or remain a lint judgment with scripted flagging?
- Do effectiveness-vs-design-intent claim scopes need a structured representation, or is the prose rule enough?
- Should `evidence` tier ordering be strict, or should `official-docs` and `expert-analysis` be treated as incomparable outside their scopes?
- When primary framework documents are ingested, do any tier definitions need correction?

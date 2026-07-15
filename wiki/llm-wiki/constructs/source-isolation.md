---
title: Source Isolation
type: construct
description: The invariant that a source-capture records only what its source says plus capture-time assessment derivable from the source alone — epistemic isolation that keeps captures regenerable, corroboration independent, and maintenance write-once.
sources:
  - "[[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]"
related:
  - "[[designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]]"
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
tags: [epistemics, provenance, knowledge-management, data-pipelines, ingest]
created: 2026-07-07
timestamp: 2026-07-07T17:30:00Z
confidence: low
novelty: exploratory
status: stable
aka: ["staging layer", "source-isolated capture", "epistemic isolation"]
---

# Source Isolation

## Definition

Source isolation is the invariant that a source-capture page records only what its one source says, plus capture-time assessment derivable from that source alone. The capture may *point to* other pages (related links, contribution routing) but never *imports, endorses, or reconciles with* them — the isolation is epistemic, not navigational. Cross-source adjudication happens downstream in syntheses and assessments. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

## Why It Matters

Source-captures exist so downstream pages can consume condensed, "clean" representations instead of re-reading raw sources. Isolation is what makes that safe, for four reasons: [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

1. **Regenerability.** An isolated capture is a pure function of its raw source — auditable, correctable, and regenerable from the raw file alone. Cross-vault leakage makes it a function of (source + vault state at capture time), destroying provenance.
2. **Fault isolation.** A bad downstream claim traces to two suspects — the source lied, or the capture misread it — rather than N.
3. **Corroboration independence.** Derived confidence (see [[designs/evidence-tier-schema]]) requires captures to be independent measurements. Harmonizing a capture with existing vault content manufactures artificial agreement — the knowledge-base equivalent of circular reporting in intelligence analysis.
4. **Write-once maintenance.** An isolated capture never goes stale relative to the vault, only relative to its immutable source — so re-review effort concentrates entirely on downstream pages.

## Mechanism / Structure

- The capture body divides into **faithful reportage** (Core Contribution, Key Claims, Evidence and Results, Methodology) and **capture-time assessment** (Limitations, Reliability Notes, Extraction Notes) — the capturer speaking, still derivable from the source alone. The groups stay structurally separate so downstream consumers can distinguish source voice from capturer voice.
- The `evidence` tier is assignable at ingest precisely because it is a property of the source in isolation; claim credibility is not, which is why `confidence` lives downstream. [[designs/evidence-tier-schema]]
- Contradiction handling: the ingest workflow routes contradictions to a downstream synthesis or assessment (citing both sources) and may leave a pointer in the capture — never the adjudication itself.

## Distinctions

- **Analogous to, and named after, the staging layer** in ELT/medallion data architecture: cleaned, normalized, per-source, no cross-source joins — with syntheses as the integrated tier. Also parallels the raw-reporting vs finished-intelligence separation in intelligence tradecraft.
- **Not navigational isolation** — links and routing pointers are encouraged; only cross-source claims are prohibited.
- **Not free** — isolation defers reconciliation: the same fact captured from three sources is written three times, and contradictions resolve only at synthesis. This is the intended trade: reconciliation is the analytical value-add and should be visible on the page that performs it.

## Evidence and Sources

- Ratified with refinements after explicit challenge ("should this invariant be questioned?") in [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]].
- The invariant predates the name: it appeared in this wiki's ingest rules from early on ("do not synthesize across the vault inside the source-capture"); this construct records the rationale and the epistemic/navigational refinement.
- Reasoning-level support only; no empirical study of isolation vs non-isolation capture quality is known to this vault.

## Related Artifacts

- [[designs/evidence-tier-schema]] — depends on this invariant for axis placement
- [[wiki/llm-wiki/constructs/three-layer-architecture]] — the layer model this invariant hardens
- [[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]] — the framework survey supplying the circular-reporting rationale

## Open Questions

- Should terminology mapping ("what this source calls X, this wiki calls Y") be allowed in captures as controlled aliasing, or does it count as importing vault framing?
- At what vault scale does deferred reconciliation (duplicate facts across captures) become expensive enough to need tooling support?

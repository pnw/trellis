---
title: "Claude Code Thread: Epistemic Metadata, Evidence Tiers, and Source Isolation"
source: claude-code-thread
created: 2026-07-07
captured: 2026-07-07
---

# Claude Code Thread: Epistemic Metadata, Evidence Tiers, and Source Isolation

Continuation of the 2026-07-07 Claude Code review session (see [[raw/chats/intent-refinement-claude-code-thread.md]]). The owner asked what research and product offerings say about categorizing authority/provenance/usefulness, after agreeing the wiki's `confidence` tag was ambiguous.

## User Prompt 1

> What else do you have to say about the repo? You also mentioned some ambiguity or inconsistency regarding the confidence tag, which I agree with. That was a lightweight attempt at categorizing something along the lines of authority, provenance, usefulness, and/or some combination or variation of that. What does the research or existing product offerings have to offer us in this area and what is your assessment?

## Claude Response 1 (condensed)

### Additional repo observations

- The lint loop is broken: the only lint report predates two schema migrations and a topic restructure.
- Deterministic checks (wikilink resolution, frontmatter validation, folder/type agreement) should be scripted, not agent-performed; reserve agent lint for judgment tiers.
- `wiki/index.md` hand-duplicates every page description; should be generated from frontmatter.
- Schema authority in the wrong place: the authoritative `confidence` definition (corroboration count) lived only in `.kiro/steering/page-format.md`, invisible to Claude Code and Codex sessions.

### Frameworks survey

Every mature framework independently concluded the problem needs at least two orthogonal axes, never one scalar:

- **NATO/Admiralty system**: source reliability (A–F, track record) × information credibility (1–6, independent corroboration). A reliable source can relay unconfirmed information; a dubious source can be right.
- **ICD 203** (US intelligence analytic standards): separates confidence (quality of the evidence base) from likelihood (probability the claim is true); conflating them in one statement is prohibited.
- **GRADE** (evidence-based medicine): evidence starts at a tier from study design and is adjusted by factors (bias risk, inconsistency, indirectness). Separately: certainty of evidence ≠ strength of recommendation — you can strongly recommend action on moderate evidence when the cost of acting is low.
- **Wikipedia**: no page-level confidence, deliberately. Per-claim verifiability with source-type tiers (reliable-sources guidance, perennial sources list) and dispute maintenance tags.
- **Digital gardens / LessWrong**: prose epistemic-status headers plus maturity stages (seedling/evergreen); prose forces honesty and avoids false precision.
- **Notion verified pages / Confluence content states**: trust = ownership + expiry; verification decays automatically rather than being asserted.
- **RAG evaluation products** (groundedness/faithfulness scores): confidence computed as citation coverage rather than asserted.

### Assessment

The wiki's `confidence` scalar conflates four things — source authority, claim credibility, freshness, usefulness. Proposal:

1. `evidence` tier on source-captures only (source axis): empirical-primary / empirical-secondary / official-docs / expert-analysis / vendor-claim / llm-generated.
2. `confidence` on downstream pages derived by rule: ceiling from best cited tier; `high` requires ≥2 independent sources; independence excludes shared authorship/commercial interest and derivation (circular reporting).
3. Freshness: timestamp + lint staleness rules, no new field.
4. Usefulness: never asserted; revealed by inbound links/reuse (orphan lint).
5. Recommendation strength (GRADE's second axis): a one-line prose epistemic note on design pages.

Field test: a field earns its place only if it changes agent behavior.

## User Prompt 2

> It makes sense that this is only relevant to source capture documents… why not have both if the original metrics from nato?

## Claude Response 2 (condensed)

Both Admiralty axes are right, but the wiki's page-type structure already *is* the two-axis system, distributed across layers: source-capture = reliability axis; synthesis/construct/design = credibility axis (derived confidence). Putting credibility on source-captures would fail three ways:

1. **Violates source isolation**: credibility is inherently cross-source (independence, corroboration, consistency with holdings); the contract says captures must not synthesize across the vault. Even in original intelligence practice the credibility digit is assigned by the receiving analyst relative to existing holdings.
2. **Rots on the wrong page**: credibility changes when *other* sources arrive; if it lived on captures, every ingest would obligate re-scoring old captures.
3. **Wrong granularity**: Admiralty scores individual information items; one number for a whole document is a lossy aggregate (a paper's headline result, methods claims, and speculation have different credibility).

What a capture *can* legitimately carry: within-source credibility signals assessable in isolation — methodology transparency, sample size, conflict of interest, firsthand vs relayed, internal consistency — as a prose Reliability Notes section that may justify a GRADE-style downward tier adjustment.

## User Prompt 3

> Interesting. Should that invariant of source capture being an isolated process be questioned? The motivation was to first capture and stage information and claims from the raw sources as condensed information with the idea that downstream processes would use that in favor of the raw source. Ie it's "clean" data whatever that means. That makes me think no, we retain that invariant right?

## Claude Response 3 (condensed)

Retain it. The pattern is exactly the staging layer of an ELT pipeline (silver tier in medallion architecture: cleaned, per-source, no cross-source joins; syntheses are the gold tier). The reasons transfer one-for-one:

1. **Regenerability**: an isolated capture is a pure function of its raw source — auditable and regenerable from the raw file alone. Cross-vault leakage makes it a function of (source + vault state at capture time), destroying provenance.
2. **Fault isolation**: bad claims trace to two suspects (source lied, capture misread) instead of N.
3. **Independence preservation**: derived confidence depends on captures being independent measurements. Harmonizing with the vault during capture manufactures artificial agreement — circular reporting, the failure the Admiralty independence requirement guards against.
4. **Cheap maintenance semantics**: isolated captures never go stale relative to the vault, only relative to their immutable source — effectively write-once.

Honest cost: isolation defers reconciliation; the same fact captured from three sources is written three times, and contradictions resolve only at synthesis. That is the right trade — reconciliation is the analytical value-add and should be visible on the page that performs it.

Two refinements to the invariant:

1. **Isolation is epistemic, not navigational.** The body records only what this source says; it may point to, but never import, endorse, or reconcile with, what other pages say. Adjudication happens downstream; the ingest workflow routes it there.
2. **Separate reportage from capture-time assessment** inside the capture, so downstream pages can safely prefer the capture over the raw source ("clean data" = schema-conformant, faithful, judgment-free reportage, with capture-time assessment quarantined in its own section and derivable from the source alone).

## User Prompt 4 (capture request)

> Yes to all of the above and make sure to update the repo steering. Refactor the shared agent files as needed. My intention was to have a fully agent-agnostic set of directions and it looks like we missed that mark

Implementation at capture time: created the shared `schema/` layer (page-format, page-types, conventions, structure, ingest, lint) as agent-agnostic canonical reference; reduced `.kiro/` steering and skills to thin wrappers; updated `AGENTS.md`; added `evidence` tiers across existing source-captures; adjusted downstream confidence values violating the new derivation ceiling.

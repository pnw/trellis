---
title: Epistemic Metadata Frameworks
type: synthesis
description: What intelligence analysis, evidence-based medicine, Wikipedia, PKM practice, and knowledge products teach about grading source reliability and claim credibility in a knowledge base.
sources:
  - "[[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]"
  - https://en.wikipedia.org/wiki/Admiralty_code
  - https://www.dni.gov/files/documents/ICD/ICD%20203%20Analytic%20Standards.pdf
  - https://gdt.gradepro.org/app/handbook/handbook.html
  - https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources
  - https://www.notion.com/help/wiki-verified-pages
related:
  - "[[wiki/llm-wiki/designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
tags: [epistemics, provenance, knowledge-management, evidence-grading, trust]
created: 2026-07-07
timestamp: 2026-07-07T17:30:00Z
confidence: medium
status: stable
---

# Epistemic Metadata Frameworks

## Central Question

How should a knowledge base grade the trustworthiness of what it holds — source authority, claim credibility, freshness, and usefulness — and what do mature disciplines and products teach about doing it without false precision?

## Current Synthesis

### The convergent finding: two orthogonal axes, never one scalar

Every mature framework independently separates *how reliable the source is* from *how credible the claim is*:

- The **NATO/Admiralty grading system** rates each item on source reliability (A–F, track record) × information credibility (1–6, independent corroboration). A reliable source can relay unconfirmed information; a dubious source can be right. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]
- **ICD 203** (US intelligence analytic standards) separates *confidence* (quality of the evidence base) from *likelihood* (probability the claim is true) and prohibits conflating them in a single statement. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]
- **GRADE** (evidence-based medicine) starts evidence at a tier set by study design and adjusts it by named factors (bias risk, inconsistency, indirectness, imprecision). It further separates *certainty of evidence* from *strength of recommendation*: one can strongly recommend acting on moderate evidence when the cost of acting is low. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

### Claim-level beats page-level

**Wikipedia** deliberately has no page-level confidence. Trust is per-claim verifiability (inline citation) combined with source-type tiers (reliable-sources guidance, perennial sources list) and dispute maintenance tags. A page-level scalar is a lossy aggregate of information the page already carries at claim level once inline citation is enforced. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

### Trust is computed or decays — not asserted

Product patterns externalize trust rather than asking authors to self-assess:

- **Notion verified pages / Confluence content states**: trust = named owner + expiry date; verification decays automatically unless renewed.
- **RAG evaluation** (groundedness/faithfulness scoring): confidence computed as citation coverage — the fraction of claims with supporting evidence — which is mechanically checkable.
- **Community systems** (votes, accepted answers): corroboration signals aggregated from use.

The common thread: self-asserted scalars drift; computed or decaying trust stays honest. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

### Prose beats enums at the margin

Digital-garden and LessWrong practice uses freeform epistemic-status headers ("epistemic status: speculation, written quickly") plus maturity stages. Prose forces honesty and avoids false precision where an enum would invite unearned exactness. Best used for GRADE's second axis — recommendation strength on design pages — rather than replacing structured fields. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

### Application to LLM wikis

For an agent-maintained wiki, two additional constraints apply:

1. **A field earns its place only if it changes agent behavior** — the schema-level analogue of [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]. A source tier an agent can filter on qualifies; an asserted usefulness rating does not.
2. **The credibility axis must live where the cross-vault view exists.** Source reliability is assignable at ingest in isolation; claim credibility requires seeing the whole vault (independence, corroboration, contradiction) and so belongs on downstream synthesis-layer pages — which also preserves [[wiki/llm-wiki/constructs/source-isolation]]. Even in original intelligence practice, the credibility digit is assigned by the receiving analyst relative to existing holdings. [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]

This wiki's adoption of these findings is specified in [[wiki/llm-wiki/designs/evidence-tier-schema]].

## Supporting Evidence

- Framework survey and mapping: [[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]].
- Framework primary documents (not yet captured in raw/ — see Update Triggers): Admiralty code, ICD 203, GRADE handbook, Wikipedia reliable-sources guidance, Notion verified pages.

## Tensions and Contradictions

- The framework details are recalled from model knowledge; primary documents are cited as external URLs but not yet captured. Per this wiki's own derivation rules, this synthesis is capped at `confidence: medium` until the primary documents are ingested.
- Scalar tier ordering is inherently lossy: `official-docs` outranks `expert-analysis` for design-intent claims about the documented system but not for effectiveness claims. The schema handles this with scoped-claim rules rather than a finer enum.

## Implications

- One epistemic scalar cannot serve a multi-source knowledge base; the minimum viable structure is a source-reliability tier plus a derived claim-credibility value.
- Independence is the load-bearing concept in corroboration: sources sharing authorship, commercial interest, or derivation chains count as one source (circular reporting).
- Freshness and usefulness need no assertable fields: timestamps + lint staleness rules, and inbound-link/orphan detection, respectively.

## Related Artifacts

- [[wiki/llm-wiki/designs/evidence-tier-schema]] — the schema this synthesis grounds
- [[wiki/llm-wiki/constructs/source-isolation]] — why the credibility axis cannot live on captures
- [[wiki/llm-wiki/entities/open-knowledge-format]] — the base format this extends

## Update Triggers

- Ingest of primary framework documents (Admiralty/AJP-2.1, ICD 203, GRADE handbook) — would raise confidence and may correct framework details
- Pilot evidence on whether evidence tiers change agent behavior in practice
- New product patterns for knowledge trust (agent memory systems, provenance standards like W3C PROV)

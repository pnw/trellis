---
title: "Claude Code Thread: Epistemic Metadata and Source Isolation"
type: source-capture
description: Claude Code thread surveying epistemic-grading frameworks (Admiralty, ICD 203, GRADE, Wikipedia, product patterns), designing the two-axis evidence/confidence schema, and ratifying the source-isolation invariant.
sources:
  - "[[raw/chats/epistemic-metadata-claude-code-thread.md]]"
related:
  - "[[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]]"
  - "[[wiki/llm-wiki/designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
  - "[[ai-research::wiki/intent-compiler/sources/intent-refinement-claude-code-thread]]"
tags: [epistemics, knowledge-management, provenance, schema-design]
created: 2026-07-07
timestamp: 2026-07-07T17:30:00Z
evidence: llm-generated
status: stable
---

# Claude Code Thread: Epistemic Metadata and Source Isolation

## Source Identity

- Raw source: [[raw/chats/epistemic-metadata-claude-code-thread.md]]
- Source type: chat transcript
- Author(s): project owner + Claude Code session (claude-fable-5)
- Published/retrieved: 2026-07-07
- Scope: continuation of the wiki review thread; covers additional repo findings, epistemic-grading frameworks, the evidence/confidence schema design, and the source-isolation invariant

## Core Contribution

Surveys how established disciplines and products grade knowledge trust, concludes the wiki's `confidence` scalar conflated four dimensions, designs a two-axis replacement (`evidence` on source-captures, derived `confidence` downstream), and ratifies the source-isolation invariant with two refinements (epistemic-not-navigational isolation; reportage/assessment separation).

## Key Claims

1. Every mature epistemic-grading framework — NATO/Admiralty, ICD 203, GRADE — uses at least two orthogonal axes (source reliability vs claim credibility/likelihood), never one scalar.
2. Wikipedia deliberately has no page-level confidence: trust is per-claim verifiability plus source-type tiers.
3. Product patterns externalize trust: Notion/Confluence as ownership + expiry (decaying verification); RAG evaluation as computed citation coverage; community systems as corroboration signals — trust is computed or decays, not asserted.
4. The wiki's `confidence` field conflated source authority, claim credibility, freshness, and usefulness.
5. The two Admiralty axes map to the wiki's page layers, not to two fields on one page: source-capture carries the reliability axis (`evidence`), downstream pages carry the credibility axis (derived `confidence`). Credibility on a capture would violate source isolation, rot as new sources arrive, and aggregate at the wrong granularity.
6. Source isolation should be retained: it is the staging layer of an ELT pipeline, and it preserves regenerability, fault isolation, corroboration independence (no circular reporting), and write-once maintenance semantics.
7. The isolation invariant refined: epistemic, not navigational — captures may point to other pages but never import, endorse, or reconcile with them; reportage and capture-time assessment stay structurally separate.
8. A frontmatter field earns its place only if it changes agent behavior.

## Evidence and Results

The thread's framework descriptions (Admiralty grades, ICD 203 confidence/likelihood separation, GRADE tiers and adjustment factors, Wikipedia source-tier practice, Notion verification) are recalled from model knowledge, not from captured raw sources — see Reliability Notes.

## Limitations and Caveats

- LLM-assisted design conversation; the schema design is reasoning, not evidence.
- No pilot has measured whether the evidence/confidence split improves wiki quality or agent behavior.

## Reliability Notes

`llm-generated` tier. The framework summaries reference well-established, decades-stable public doctrine (Admiralty/NATO grading, ICD 203, GRADE), which lowers hallucination risk, but none of the framework documents are captured in `raw/` yet — claims about their details should be verified against primary documents before load-bearing use. Suggested captures listed below.

## Important References and Linked Material

- [NATO AJP-2.1 / Admiralty grading system](https://en.wikipedia.org/wiki/Admiralty_code) — the two-axis source reliability × information credibility system.
- [ICD 203 Analytic Standards](https://www.dni.gov/files/documents/ICD/ICD%20203%20Analytic%20Standards.pdf) — confidence vs likelihood separation, estimative language.
- [GRADE handbook](https://gdt.gradepro.org/app/handbook/handbook.html) — evidence certainty tiers, adjustment factors, certainty vs recommendation strength.
- [Wikipedia: Reliable sources guidance](https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources) — per-claim verifiability and source-type tiers.
- [Notion verified pages](https://www.notion.com/help/wiki-verified-pages) — ownership + expiry as trust mechanism.

## Contribution Routing

- [[wiki/llm-wiki/syntheses/epistemic-metadata-frameworks]] — frameworks synthesis
- [[wiki/llm-wiki/designs/evidence-tier-schema]] — the adopted schema design
- [[wiki/llm-wiki/constructs/source-isolation]] — the ratified invariant as a construct
- `AGENTS.md` and `schema/` — contract and schema-layer updates implemented from this thread

---
title: "Claude Code Thread: Federation Design Review — Breadcrumbs Over Rails"
type: source-capture
evidence: llm-generated
description: Owner review of the federation design ratifying simplifications — standalone normative schema with optional decision archaeology, prompt-based inheritance over deterministic pipelines, dogfood health as real health — and directing creation of the named upstream repo.
sources:
  - "[[raw/chats/wiki-federation-review-claude-code-thread.md]]"
related:
  - "[[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]"
  - "[[designs/wiki-federation-and-inheritance]]"
  - "[[designs/trellis-repo-design]]"
tags: [llm-wiki, federation, meta-research, schema-design, knowledge-management]
created: 2026-07-10
timestamp: 2026-07-10T18:00:00Z
status: stable
---

# Claude Code Thread: Federation Design Review — Breadcrumbs Over Rails

## Source Identity

- Raw source: [[raw/chats/wiki-federation-review-claude-code-thread.md]]
- Source type: chat transcript (agent-condensed, owner statements verbatim)
- Author(s): project owner + Claude Code session (claude-fable-5)
- Published/retrieved: 2026-07-10
- Scope: owner review of the first federation design draft, simplification directives, and the directive to design and name the upstream repository

## Core Contribution

The owner's corrective pass over the federation design, which surfaced the design philosophy the first draft violated: mechanisms exist to make agent judgment cheap to apply and easy to audit — breadcrumbs — not to constrain it into determinism — rails. Also ratifies dogfood health as genuine (not merely instrumental) health for the upstream repo.

## Key Claims

1. Dogfood health is real health, not a vanity metric: the upstream wiki is healthy when it itself is healthy, because it dogfoods the method; a second instance is expected but is not the sole health criterion.
2. The schema is normative; the earlier "each page type is a design" idea was motivated by capturing motivations for changes, not by wanting a derivation pipeline. A deterministic wiki→schema pipeline is the wrong approach.
3. Schema pages must be standalone — no back-references from schema files to decision pages. Decision archaeology (going to the decisions folder and digging) is the accepted discovery mode.
4. Rationale capture is wanted only for *certain* decisions — an easy, simple way to record why, so it can be re-evaluated later against new information or empirical data. Decisions are "additional context for the future," superseded as needed.
5. Co-evolution circularity is acknowledged and accepted: wiki contents contribute to the schema's design, and the schema shapes what the wiki captures.
6. Inheritance today is a prompt — "figure out what changed upstream that's useful for the slice we picked for this wiki and update yourself" — and the goal is lightweight breadcrumb-following, explicitly not an "over engineered, perfectly constrained and perfectly deterministic system."
7. Directive: write the design for the new repo and give it a name.

## Evidence and Results

Conversational; owner statements of intent and design philosophy. No empirical content.

## Limitations and Caveats

- Speech-to-text transcription artifacts throughout the owner's messages (reading notes in the raw file); normalization is the capturer's interpretation.
- The assistant being corrected is the same agent that condensed this transcript and revised the designs.

## Reliability Notes

`llm-generated` tier. Owner-quoted passages are verbatim and carry owner authority for design direction and philosophy; assistant summaries are the corrected party's own account. Condensed transcript, declared as such in the raw file.

## Important References and Linked Material

- None external; all references are vault-internal.

## Contribution Routing

- [[designs/wiki-federation-and-inheritance]] — revision (breadcrumbs-over-rails principle, schema governance, inheritance, cross-wiki lint, phasing, health metrics)
- [[designs/trellis-repo-design]] — new design (the directed deliverable)

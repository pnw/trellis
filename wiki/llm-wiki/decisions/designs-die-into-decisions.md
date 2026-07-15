---
title: Designs Die into Decisions
type: decision
description: "Design-lifecycle doctrine: once a blueprint design's artifact ships, the artifact plus a decision record supersede its descriptive content — the design is slimmed to what is still operative, or deprecated."
sources:
  - "[[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/decisions/adopt-single-goal-federation]]"
  - "[[wiki/llm-wiki/decisions/trellis-repo-bootstrap]]"
  - "[[designs/wiki-federation-and-inheritance]]"
  - "[[designs/trellis-repo-design]]"
tags: [llm-wiki, schema-design, meta-research, knowledge-management, governance]
created: 2026-07-12
timestamp: 2026-07-15T12:00:00Z
status: deprecated
---

# Designs Die into Decisions

## Context

An a-priori review of all nine design pages in this vault (2026-07-12, following the split) found that design pages serve four distinct jobs: an **operative protocol** agents follow (e.g. [[designs/wiki-self-experimentation]]), a **blueprint** for something not yet built, a **rationale record** for choices already made, and a **description of an existing artifact**. Only the last rots: once a blueprint's artifact ships, the descriptive content duplicates the artifact itself — the repo, the schema file, the script — and duplicates are future contradictions, this vault's own standing drift finding. The blueprint job ends at shipping; the rationale job does not, but rationale kept inside a design page is entangled with description that will drift. The schema-governance doctrine from the owner review already pointed at the answer: rationale worth keeping goes in decision pages, discovered by decision archaeology, while normative and descriptive surfaces stay standalone ([[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]).

## Decision

When a design's artifact ships, the design **dies into a decision**:

1. Collapse the design's historical and rationale content — alternatives weighed, naming, shape choices, execution record — into one or more `decision` pages.
2. Slim the design to what is still live: operative protocol other pages follow, and blueprint content for parts not yet built. If nothing live remains, deprecate the design with a pointer to its decisions.
3. The shipped artifact plus the decision record together supersede the descriptive content; the artifact documents itself.

First application is this very batch: [[designs/trellis-repo-design]] deprecated into [[wiki/llm-wiki/decisions/trellis-repo-bootstrap]], and [[designs/wiki-federation-and-inheritance]] slimmed to the live design with its executed phases and alternatives moved to [[wiki/llm-wiki/decisions/adopt-single-goal-federation]].

## Alternatives Considered

- **Leave designs as mixed history-plus-spec documents** — rejected: the descriptive half drifts against the shipped artifact, and readers cannot tell operative rule from stale blueprint ([[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]] records where accumulating unpruned apparatus led).
- **A generated design changelog** (mechanically track what shipped and when) — rejected as a rail: the collapse is a judgment call about which content is still operative, exactly the kind of judgment breadcrumbs-over-rails says to keep with the agent ([[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]).

## Consequences

- Design pages stay trustworthy as live specs; a `stable` design describes something you can follow or build today.
- Rationale remains discoverable by decision archaeology — the decisions folder, the index, and search — with no back-links required from artifacts to their decisions.
- The corresponding normative one-paragraph lifecycle rule is being added to `schema/page-types/design.md` by a parallel edit; per the standalone-schema doctrine, that file states the rule without referencing this page.

## Status

`deprecated` — superseded 2026-07-15 by [[wiki/llm-wiki/decisions/separate-design-surface]]. Designs left the wiki for their own lifecycle-governed surface; a design no longer dies into decisions but freezes as a historical record of intent at its terminal state. The lifecycle rule this decision added to the (now removed) `design` page-type spec is repealed. This decision established no invariant pages, so none need disposition. The record below stands as history.

## Related Artifacts

- [[wiki/llm-wiki/decisions/adopt-single-goal-federation]] and [[wiki/llm-wiki/decisions/trellis-repo-bootstrap]] — the first decisions produced by applying this doctrine
- [[designs/trellis-repo-design]] — the first design deprecated under it
- [[designs/wiki-federation-and-inheritance]] — the first design slimmed under it

---
title: "Claude Code Thread: Staged Ingest and Instigator Tiers"
type: source-capture
description: "Owner hypothesis that ingest over-produces derived pages (evidence: 4–5 downstream instances), corpus measurements testing it, and the converged instigator-tier model — three tiers by who creates which page types and when, with a two-stage ingest."
sources:
  - "[[raw/chats/staged-ingest-instigator-tiers-claude-code-thread.md]]"
related:
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
  - "[[wiki/llm-wiki/designs/evidence-tier-schema]]"
tags: [llm-wiki, ingest, schema-design, knowledge-management, governance]
created: 2026-07-13
timestamp: 2026-07-13T12:00:00Z
evidence: llm-generated
---

# Claude Code Thread: Staged Ingest and Instigator Tiers

## Source Identity

- Raw source: [[raw/chats/staged-ingest-instigator-tiers-claude-code-thread.md]]
- Source type: chat transcript (condensed; owner messages verbatim)
- Author(s): the wiki owner and a Claude Code session agent
- Published/retrieved: 2026-07-13
- Scope: a hypothesis-review thread on ingest behavior and page-type creation guidance, ending in a directive to implement the converged model

## Core Contribution

The thread contributes an owner-observed failure mode of the method as distributed — downstream wiki instances accumulating "obtuse and wordy" agent-instigated derived pages — and converges on a corrective model: page types classified into three **instigator tiers** (capture / interpretive / authored) governing who creates which page types and when, plus a **two-stage ingest** whose first stage is a bounded, source-isolated, delegable capture and whose second stage is vault-aware review and routing.

## Key Claims

- The owner operates roughly 4–5 downstream wiki instances of this method, and in them agents treat synthesis into derived document types as their primary job, leaving those wikis "mostly incomprehensible"; this experience, not this lab's corpus, motivated the hypothesis.
- The owner's earlier wiki iterations were almost exclusively source-capture with light editorializing; his usage outgrew that, and he judges the pendulum has now swung too far toward derived-page production.
- Corpus measurements taken in-thread: this lab held 81 typed pages at measurement (35 source-captures); the research topic `agent-context` showed 26 captures / 20 derived pages (0.77 derived per capture) while the self-referential method topic `llm-wiki` showed 9 / 24 (2.7); captures averaged ~480 words against ~1,470 for designs; construct/entity inbound-link degree had a median of ~7 with only 3 of 23 pages at ≤1.
- From those measurements, the thread argued the lab itself shows no premature-promotion problem, so the defect localizes to the distributable layer: the instigator discipline existed only in the operator's head, and instances sharing only the schema and operator reproduce the failure.
- The converged model: capture tier (`source-capture`, ingest-instigated, delegable to a context-free capture agent — impartiality and source isolation being the point); interpretive tier (`construct`, `entity`, `synthesis`, `comparison`, `assessment` — agent- or user-instigated when a trigger fires); authored tier (`design`, `decision`, `invariant` — user-instigated; the owner: arbitrary agent-driven designs and decisions "is more my responsibility").
- Ingest is an occasion for interpretation, not a justification: a new source legitimately raises the question of derived-layer change at every ingest, and interpretation may proceed at ingest review — but asking the question is not answering yes.
- A single source is "allowed, even expected where appropriate" to spawn interpretive pages — a novel concept is valuable because it is meaningful, not because it recurred; frequency has utility for substantiating and contextualizing, not gating. A count-based recurrence gate was considered and rejected in-thread as a rail duplicating the existing confidence-derivation pricing.
- Contradiction between captures is expected and healthy; the operational assignment is that a context-free capture agent cannot detect vault-level contradictions, so detection belongs to the vault-aware review stage.
- The "discuss with the user before writing" ingest step is a legacy of pre-type prompt iterations; its purpose (user weighs in on interpretation) relocates to the review stage.
- Per-type composition metrics are worth having as an observable heuristic "circumstantially useful in the context of other empirical information," but must not be a hard metric or goal.
- Schema files should carry their own frontmatter (owner suggestion, endorsed minimally in-thread with the federation upgrade path as consumer).

## Evidence and Results

The corpus statistics above were measured directly against this repository's working tree during the thread (file counts by type folder, frontmatter type counts, word counts via `wc -w`, inbound wikilink degree via `grep`), and are reproducible from repo state at the capture date. The downstream-instance observations are the owner's firsthand operational experience, reported in-thread; the instances themselves are not visible to this repository.

## Limitations and Caveats

- The downstream failure-mode evidence is owner-reported anecdata across ~4–5 instances that share one operator and agent stack; under this wiki's own independence rules that counts as a single source, and no instance artifacts are captured here yet.
- The lab corpus measured is one day post-split from the combined vault the owner's frustration partly formed on; pre-split behavior is only indirectly represented.
- The thread's assessments of cause (guidance gap in the distributable layer) are reasoning over the measurements, not a controlled comparison.

## Reliability Notes

Condensed transcript captured from within the session by the session's own agent; owner statements are verbatim, agent responses are self-condensed — `llm-generated` tier per the verbatim-chat rule regardless of content quality. The in-thread corpus numbers are mechanically derived and independently re-derivable from the repository at the capture-date commit, which strengthens them relative to the tier label.

## Contribution Routing

- [[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]] — the decision this thread grounds (user-instigated in Prompt 4)
- Roadmap: ingest downstream friction reports as raw sources; explore middle-tier instigator blurriness; note-craft/page-granularity candidate topic gains a live motivation
- Candidate synthesis input if future sources engage staged capture pipelines (episodes, atomic-note practices, ELT staging analogies)

## Extraction Notes

Owner messages use quote-reply formatting (nested blockquotes in the raw file); one level of quoting was added mechanically during capture. Minor typos in owner messages ("Can’t out a number", "birth token", "as new information is interested") are preserved verbatim in the raw file and read as "put", "both token", and "ingested" respectively.

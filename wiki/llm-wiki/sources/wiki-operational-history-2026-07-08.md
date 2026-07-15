---
title: "Wiki Operational History Snapshot (through 2026-07-08)"
type: source-capture
evidence: empirical-primary
description: Point-in-time extract of this repository's own operational record — commit history with change stats, page counts, lint results, and the verbatim operation journal — snapshotted as first-party evidence about llm-wiki practice.
sources:
  - "[[raw/repos/ai-research-operational-history-2026-07-08.md]]"
related:
  - "[[wiki/llm-wiki/constructs/operational-evidence]]"
  - "[[designs/wiki-self-experimentation]]"
  - "[[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]]"
tags: [llm-wiki, meta-research, operations, epistemics, self-experimentation]
created: 2026-07-08
timestamp: 2026-07-08T03:30:00Z
status: stable
---

# Wiki Operational History Snapshot (through 2026-07-08)

## Source Identity

- Raw source: [[raw/repos/ai-research-operational-history-2026-07-08.md]]
- Source type: repo snapshot / extract
- Author(s): repository history (multiple agent sessions, owner-merged); extract assembled mechanically by a Claude Code session
- Published/retrieved: extracted 2026-07-08 at commit 5c911d4
- Scope: full commit history with per-commit change stats, current page/source counts, all recorded lint results, and the verbatim `wiki/log.md` journal

## Core Contribution

The first snapshotted operational record of this wiki: what practices changed, when, at what size of change, and what quality signals (lint) showed before and after. Serves as the citable evidence base for assessments about the wiki's own knowledge-base practices.

## Key Claims

1. The repo went from first ingest (2026-04-16) to 133 wiki pages and 63 source-captures by 2026-07-08, with the bulk of structural evolution concentrated in 2026-07-04 through 2026-07-08.
2. Three structural migrations (topic-first typed folders; repository-root wikilinks; schema/ layer extraction) plus two schema adoptions (evidence tiers; roadmap file) occurred within five days, each leaving lint at 0 errors afterward.
3. The retroactive confidence-ceiling audit found 27 of 113 pages above the new derivation ceiling — the pre-schema asserted scalar overstated support on roughly a quarter of the vault.
4. A lint tooling bug (journal counted as an incoming link) masked 6 real orphan pages until fixed on 2026-07-08.
5. Environment egress policy blocked semantic-model downloads for the qmd retrieval tool while lexical search worked, shaping the retrieval implementation.
6. Multiple agent sessions (Fable, Sonnet, Kiro-configured) operated on the same vault within one 24-hour window, including one divergence on `main` that required a rebase merge of parallel work.

## Evidence and Results

The raw extract separates three provenance grades: **mechanical** (git log with shortstat, page counts — regenerable by re-running commands at commit 5c911d4), **journal** (verbatim `wiki/log.md`, agent-authored and owner-merged), and **observed** (lint outputs recorded from session transcripts, not independently regenerable).

## Methodology

Extract assembled by script: `git log --reverse --shortstat` on `origin/main`, file counts via `find`/`grep`, journal copied verbatim. No narrative interpretation was added inside the mechanical sections.

## Limitations and Caveats

- Single project, single owner, ~12 weeks of history — n=1 in every direction.
- The journal grade is agent-narrated: it records what agents said they did and why, which is not the same as an independent observation of what happened. The mechanical grade is the stronger evidence.
- Lint results predating `scripts/lint.py` used different (agent-judged) check definitions and are not directly comparable to script results.

## Reliability Notes

`empirical-primary`: this is original, systematic observational data with reproducible extraction for its mechanical sections. Two standing caveats cap its downstream use: (1) all first-party operational snapshots of this wiki share authorship and project identity — they count as **one source** under the independence rule, so no accumulation of self-observations alone can push a downstream page past `medium`; (2) the observer is the operator — agents both performed and recorded the work, with owner review at merge time (the "AI abstraction layer" constraint). Prefer citing the mechanical sections over the journal where both cover an event.

## Important References and Linked Material

- None external; the source is this repository itself.

## Contribution Routing

- [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]] — first verdict assessment drawing on this record
- [[wiki/llm-wiki/constructs/operational-evidence]] — the construct this capture instantiates
- Future: subsequent snapshots (same extraction method, later commits) enable before/after comparisons per experiment

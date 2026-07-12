---
title: Sandbox-Compatible Retrieval
type: invariant
description: No load-bearing step of this wiki's query workflow may require network egress at query time — every retrieval path must degrade to tools that work in a sandboxed session.
sources:
  - "[[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]"
  - "[[wiki/agent-context/subtopics/retrieval/entities/qmd]]"
  - "[[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]]"
  - "[[wiki/llm-wiki/constructs/operational-evidence]]"
tags: [retrieval, tooling, sandboxing, local-first, network-policy]
created: 2026-07-08
timestamp: 2026-07-08T12:00:00Z
confidence: medium
enforcement: convention
status: stable
---

# Sandbox-Compatible Retrieval

## Statement

At every point in time, every load-bearing step of this wiki's query and ingest workflows must be executable without network egress beyond the repository itself. Network-dependent retrieval features (embedding downloads, hosted models, remote indexes) may be *additive* — used when available — but may never become the only way to answer a query or complete an ingest step.

## Scope

Binds the Query Workflow and the search-index step of the Ingest Workflow (`AGENTS.md`, `schema/conventions.md`, `schema/ingest.md`) and any future retrieval tooling adopted for this vault. It governs the wiki's *operation*, not its content: pages may discuss network-dependent tools freely.

## Rationale

This vault is operated by agents inside sandboxed sessions whose network policy is outside the operator's control. A retrieval path that hard-depends on egress fails exactly where the wiki is used most. The constraint buys: workflows that behave identically across Codex, Kiro, and Claude Code sessions regardless of environment policy; zero-setup querying (`Grep`/`Glob`/`Read` always work); and freedom to adopt tools like QMD without them becoming a fragile dependency. Without it, a single tooling upgrade could silently make the wiki unqueryable in its primary operating environment. [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]

## Enforcement

`convention` — the fallback rule documented in the Query Workflow (`AGENTS.md`, `schema/conventions.md`): treat `qmd` as an optimization, never a dependency, and fall back to `Grep`/`Glob`/`Read` directly against `wiki/`. That canonical statement is the mechanism; this page does not restate it, it records the standing constraint behind it. Nothing automated verifies that new workflow steps stay egress-free — a new schema or tooling change must be checked against this invariant by the agent making it.

## Violation Modes

- A workflow step is written to hard-depend on `qmd query`/embeddings (or any downloaded model), and breaks in sandboxed sessions where the model host is blocked. Detected as a query- or ingest-workflow failure in exactly the environments least equipped to debug it.
- Subtler form: documentation or steering examples that show only the network-dependent path, training agents into a dependency the schema formally avoids.
- Cost: the wiki becomes unqueryable or un-maintainable in its primary operating environment until an agent rediscovers the fallback.

## Removal Path

**Origin: discovered-and-ratified.** Nobody decided this constraint; it was observed on 2026-07-08 when `qmd embed`/`qmd query` failed in a sandboxed session because their GGUF models are hosted on `huggingface.co`, which the session's network policy blocks — while BM25 `qmd search` worked with no downloads ([[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]). Writing the fallback rule into the cross-agent query workflow was the ratification: the environment imposes the condition, but treating egress-free retrieval as *binding on workflow design* is this wiki's own commitment, and this analysis is what makes it binding rather than merely observed.

**What removal would require:** either (a) the operating environments' network policies durably allowing the model hosts, or (b) vendoring the embedding models into the environment or repository so no egress is needed. Both are outside or partially outside the vault's control; (b) is actionable but carries repo-size and license considerations.

**Effects of removal:** hybrid semantic retrieval (`qmd query`) could become the default query path rather than an opportunistic enhancement; `scripts/qmd-index.sh` would gain an embed step; the fallback language in `AGENTS.md`/`schema/conventions.md` could be relaxed from "never a dependency" to "preferred path with fallback." This is a two-way door — cheap to relax and cheap to reinstate — so the invariant should be re-checked whenever the environment picture changes, rather than defended indefinitely.

## Exceptions

`qmd search` (BM25 lexical, SQLite-local, no downloads) is already egress-free and sits inside the invariant, not outside it. Optional enhancements may use the network when a session happens to allow it; the invariant binds only what the workflows *depend on*. No other exceptions.

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]] — the design this invariant constrains (Approach 0 / B2 layering is its direct expression)
- [[wiki/agent-context/subtopics/retrieval/entities/qmd]] — the tool whose environment failure surfaced the constraint
- [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]] — lists "environment egress policy is a first-class tooling constraint" as plausible-but-unvalidated; that item tests this invariant
- [[wiki/llm-wiki/constructs/operational-evidence]] — the evidence class backing it

## Evidence and Sources

The single source is the wiki's own operational record, [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]] (`empirical-primary`): the observed qmd model-download failure under session network policy, and the subsequent adoption of the lexical-plus-fallback workflow. One empirical source, n=1 environment — `confidence: medium` per the derivation rules, and the generalization beyond this sandbox type is untested.

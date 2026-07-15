---
title: Adopt Single-Goal Wikis with Federation
type: decision
description: Split the dual-mandate repository into trellis (upstream method lab) and ai-research (downstream instance #1), federated by peer-prefixed links, outbound-only link responsibility, move-log forwarding, and manifest-pinned vendored schema.
sources:
  - "[[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]"
related:
  - "[[designs/wiki-federation-and-inheritance]]"
  - "[[wiki/llm-wiki/decisions/trellis-repo-bootstrap]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]]"
tags: [llm-wiki, federation, meta-research, knowledge-management, epistemics]
created: 2026-07-12
timestamp: 2026-07-12T07:00:00Z
status: stable
---

# Adopt Single-Goal Wikis with Federation

The founding decision of the repository split. The live design it produced is [[designs/wiki-federation-and-inheritance]]; this page freezes the choice, the rejected paths, and the execution record.

## Context

One repository (`ai-research`) served two goals under one roof: the owner's **practice reference** for building software with AI agents, and the **laboratory** for evolving llm-wiki knowledge-base practice. The 2026-07-10 outside-observer critique ([[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]) surfaced the costs of the dual mandate:

- Meta-work had outgrown object-level work, competing for the same sessions, and neither goal's health could be measured because both were scored against the same repo.
- Evaluator and evaluated were fused: the system evolving the schema was also the system evaluated by it, so the arms-length evidence [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]] named as its own Missing Evidence structurally could not come from inside one repo.
- Content membership was unprincipled: "does this page belong here?" had no test when the wiki had two purposes.

The owner concurred with the identity-crisis finding and ratified **one goal per wiki**: a wiki spans many topics but has exactly one goal, which is the membership test for content, the denominator for health metrics, and the first field of the instantiation manifest.

## Decision

Split the repository into two single-goal wikis and federate them:

- **`trellis`** — upstream: system-of-record for the wiki method (normative `schema/`, `scripts/`, instantiation `seed/`) plus the dogfood lab wiki whose subject is the method itself. Goal: develop and evidence the wiki method through its own operation.
- **`ai-research`** — downstream instance #1. Goal: the owner's practice reference for building software with AI agents.

Federation mechanics, as designed in [[designs/wiki-federation-and-inheritance]]:

- **Peer-prefixed cross-wiki links**, resolved through the manifest's `peers` block; unprefixed wikilinks stay intra-wiki.
- **Outbound-only link responsibility**: a wiki lints and maintains only its own outbound links, including cross-wiki ones.
- **Move-log forwarding addresses**: `wiki/moves.log` records every move/delete with a tombstone disposition, so peers checking outbound links follow the trail instead of relying on stable paths.
- **Manifest-pinned vendored schema**: downstream instances vendor a plain copy of the subsetted `schema/` and `scripts/`, pinned to an upstream commit in `wiki-manifest.yaml`.
- **Three-breadcrumb inheritance** — the manifest pin, granular per-type schema files, and the move log — plus a canonical upgrade prompt (in `seed/interview.md`) that any downstream agent runs to diff, apply, lint, re-pin, and log.

## Alternatives Considered

- **Goal-tagging within one repo** — tag pages by which goal they serve. Rejected: no distribution story, evaluator and evaluated stay fused, and the membership test remains advisory.
- **Monorepo with two wiki roots** — rejected: agents load contracts per-repo, so the boundary agents actually experience stays blurred, and "point a new wiki at the upstream repo" has no clean referent.
- **Schema-only extraction (no dogfood wiki upstream)** — publish `schema/` plus scripts as a bare template repo. Rejected: it loses the lab — the method research needs its own evidence base, and a practices repo with no real workload violates the workload-stays-real invariant of [[designs/wiki-self-experimentation]].
- **First-draft rails** (rejected at the 2026-07-10 owner review, [[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]): a change-classification taxonomy, upstream CHANGELOG and migration-note contracts, mandatory schema↔decision linkage, a pairing lint, a cross-wiki lint tier, and a wiki→schema generation pipeline. All replaced by breadcrumbs plus agent judgment; recorded here so they are not re-proposed.

## Consequences

- Each repo's health is measurable against its own single goal: `ai-research` on object-level throughput (above all, the pilot), `trellis` on dogfood health plus instance health.
- Downstream friction becomes arms-length operational evidence — instances existing, upgrades completing, friction reports harvested from downstream logs — structurally separated from self-observation for the first time, and the only evidence axis that can ever escape the `medium` cap.
- Same-operator wikis still count as **one source** for independence purposes: citing a claim across repos that share an operator adds no corroboration. This closes the confidence-laundering loophole the split would otherwise open; the rule is now normative in `schema/wiki/page-format.md`.
- Executed 2026-07-12: trellis bootstrap commit `a08dbb3`; ai-research migration merged at `a56a97d`. Both repos lint clean; departed pages are tombstoned in ai-research's `wiki/moves.log` with `moved-to trellis::...` forwarding addresses.

## Invariants Established

Two standing constraints originate here: **single-goal-per-wiki** (new content must serve the wiki's stated goal; checked at the lint judgment tier) and **outbound-only-links** (a wiki maintains only its own outbound references). Their `invariant` pages are deliberately not yet written — deferred until the split settles enough that the rules' final wording and enforcement are stable; the roadmap tracks writing them. Until then the rules live normatively in `schema/wiki/conventions.md` and the two repos' agent contracts.

## Status

`stable` — accepted at the 2026-07-10 owner ratification, executed 2026-07-12. Supersede with a new decision if the goals are ever re-fused or a different distribution mechanism replaces vendored-schema federation; the superseding decision must dispose of the two invariants named above.

## Related Artifacts

- [[designs/wiki-federation-and-inheritance]] — the live federation design (principles, topology, inheritance, log taxonomy)
- [[wiki/llm-wiki/decisions/trellis-repo-bootstrap]] — the repo-shape decisions of the upstream repository
- [[wiki/llm-wiki/decisions/designs-die-into-decisions]] — the design-lifecycle doctrine this batch first applied
- [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]] — the pre-split evidence record the critique drew on

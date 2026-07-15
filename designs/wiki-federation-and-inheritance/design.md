---
title: Wiki Federation and Schema Inheritance
type: design
description: The live federation design for the llm-wiki practice — one goal per wiki, the method dogfooded in its own upstream repository (Trellis), breadcrumb-based schema inheritance for downstream instances, and outbound-only cross-wiki references with move-log forwarding.
sources:
  - "[[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/decisions/adopt-single-goal-federation]]"
  - "[[wiki/llm-wiki/decisions/trellis-repo-bootstrap]]"
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[designs/trellis-repo-design]]"
  - "[[designs/project-wiki-template]]"
  - "[[designs/project-wiki-application-guide]]"
  - "[[designs/multi-agent-project-wiki-pattern]]"
  - "[[designs/wiki-self-experimentation]]"
  - "[[designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]]"
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[designs/agent-context-portability]]"
tags: [llm-wiki, federation, portability, schema-design, meta-research, knowledge-management]
created: 2026-07-10
timestamp: 2026-07-15T12:00:00Z
status: active
---

# Wiki Federation and Schema Inheritance

Epistemic note: the grounding is thin by the wiki's own tiers — the design traces to owner-directed design conversations ([[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]], [[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]). Revised 2026-07-12 post-execution: the split is done, the historical content moved to decision pages under the then-current design-lifecycle doctrine ([[wiki/llm-wiki/decisions/designs-die-into-decisions]], since superseded), and what remains here is the live design — the standing principles, the topology, and the mechanisms agents operate today. One split's worth of operation is not yet corroboration.

## Problem Statement

One repository served two goals — practice reference and wiki-method lab — and the 2026-07-10 outside-observer critique showed the dual mandate made health unmeasurable, fused evaluator and evaluated, and left content membership unprincipled ([[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]). The founding choice, its full context, and the rejected alternatives are recorded in [[wiki/llm-wiki/decisions/adopt-single-goal-federation]]; this page is the resulting design, executed 2026-07-12 and live since.

## Design Principle: One Goal Per Wiki

A wiki may span many topics and subtopics, but it has exactly **one goal**, stated in its overview page. The goal is the membership test for content, the denominator for health metrics, and the first field of the instantiation manifest — an instance cannot be created without stating it.

Consequence: content serving a different goal lives in a different wiki and is reached by **cross-wiki reference**, which is what makes federation (below) load-bearing rather than optional. Adopted 2026-07-12; the corresponding `invariant` page (`enforcement: manual` — checked at the lint judgment tier: does new content serve the stated goal?) is deferred until the split settles ([[wiki/llm-wiki/decisions/adopt-single-goal-federation]], Invariants Established).

## Design Principle: Breadcrumbs Over Rails

Every mechanism in this design assumes an agent with judgment as the executor. Artifacts exist to make that judgment cheap to apply and easy to audit afterward — breadcrumbs — never to constrain it into determinism — rails. Determinism is reserved for what is already mechanical: git history, the generated move log, the existing deterministic lint tier. When a proposed mechanism includes a classification taxonomy, a required linkage, or a pipeline, the default answer is no; the question is only ever "what trail marker would have made the judgment cheaper?" ([[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]] — this design's own first draft, which specified change-classification taxonomies, migration-note contracts, and pairing lints, is the evidence that agents re-add rails unless the principle is written down.)

## Target Topology

| Repo | Role | Goal (one sentence) |
|------|------|---------------------|
| `trellis` (this repo) | Upstream: system-of-record for the wiki method, plus its dogfood wiki | Develop and evidence the wiki method itself, through its own operation |
| `ai-research` | Downstream instance #1 (as of 2026-07-12) | The owner's practice reference for building software with AI agents |
| pilot project wiki (future) | Downstream instance #2 | Per [[ai-research::wiki/intent-compiler/designs/pilot-implementation-playbook]] — project-local knowledge for one pilot codebase |

Trellis carries the distributable surface (granular `schema/`, `scripts/`, the `seed/` instantiation layer) and a wiki whose *subject is the method* — the `wiki/llm-wiki/` and `wiki/agent-context/` topics, the self-experimentation protocol, operational-evidence snapshots, and verdict assessments. The repo itself and `AGENTS.md` document the layout; the repo-shape rationale lives in [[wiki/llm-wiki/decisions/trellis-repo-bootstrap]]. The dogfood recursion is the point: the method's own wiki is the method's first proof, and the boundary between the distributable structural layer and the descriptive research *about* it stays razor-sharp because downstream inheritance pulls the former and must never pull the latter.

Content membership follows the goal test: a page belongs here if its primary question is about knowledge-base practice (the method), and in `ai-research` if it is about building software with agents (the practice). The split-time disposition of every page is recorded in the bootstrap log and the two repos' move logs.

## Schema Governance: Standalone Norms, Decision Archaeology

1. **Granular schema files** — one normative spec per type in `schema/wiki/page-types/{type}.md` (required fields, expected sections, folder mapping, lint rules) plus `schema/wiki/page-types/registry.md` listing the full type vocabulary. The per-type file is the unit downstream instances subset, and the granularity is what makes an upgrade diff readable.
2. **Schema files are normative and standalone.** A schema file states the current rule completely and carries no back-references to rationale, history, or decision pages. What downstream vendors is norms, never the lab's reasoning about them.
3. **Rationale is captured as decision pages — sometimes.** When a schema change weighs alternatives or rests on assumptions that new information or empirical data could overturn, a `decision` page in this dogfood wiki records the motivation, to be re-evaluated and superseded on its own clock. When a change doesn't warrant that, it just happens. No decision-per-change requirement, no pairing lint, no linkage from schema to decisions — discovery is **decision archaeology**: the decisions folder, the index, and search. ([[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]])
4. **Co-evolution is accepted, not engineered away.** Wiki contents inform schema decisions; the schema shapes what the wiki captures. The loop is safe because it passes through judgment (and, when worth keeping, a decision record with provenance) rather than through a deterministic derivation — there is no wiki→schema pipeline, and none is planned.

## Instantiation: Questionnaire → Manifest

Creating a wiki = pointing an agent at this repo and running `seed/interview.md`. This is an intent brief for a wiki instance — the same interrogate-then-confirm shape as [[ai-research::wiki/intent-compiler/designs/intent-refinement-stage]], applied to wiki creation. The answers persist as `wiki-manifest.yaml` at the instance root:

```yaml
upstream:
  repo: <trellis repo URL>
  pin: <upstream commit at last sync>
goal: One sentence. Required — the single-goal principle enforced at birth.
page_types: [source-capture, construct, synthesis, design, decision, invariant]  # subset of upstream registry
link_format: root-relative-wikilink   # or markdown-relative, per instance choice
agents: [claude-code, kiro, codex]    # which adapter layers to generate
peers:
  trellis: {repo: <URL>, pin: <commit>}   # named wikis this instance may cross-reference
```

The manifest is a breadcrumb store, not a contract: it records what "the slice we picked for this wiki" *is* — provenance (what was inherited, from which commit), scope (which page types this instance carries), and the peer registry cross-wiki links resolve against — so the upgrade prompt has a durable referent. [[designs/project-wiki-template]] was absorbed as the seed-content layer the questionnaire ships (`seed/pages/`); [[designs/project-wiki-application-guide]]'s adaptation guidance became the interview script. v0 is an agent-run procedure (a skill in this repo), not a CLI tool.

## Inheritance and Upgrades: Three Breadcrumbs and a Prompt

Downstream instances **vendor** the schema (a plain copy of the subsetted `schema/` files plus scripts), pinned by the manifest. Upgrading is the owner's existing practice, made cheaper — a prompt:

> Diff trellis `schema/` and `scripts/` from our pinned commit to upstream HEAD. Figure out what changed that matters for the slice this wiki uses (see `wiki-manifest.yaml`), apply it, run lint, bump the pin, and log what you did.

The design's entire job here is the three breadcrumbs that make that prompt cheap to execute well:

1. **The manifest pin** — "what changed upstream" is a concrete `git diff <pin>..HEAD`, not a guess.
2. **Granular per-type schema files** — the diff reads as "the `construct` type changed, which you carry; the `comparison` type changed, which you don't."
3. **The move log** — broken references have forwarding addresses (see Log Taxonomy).

No change-classification taxonomy, no upstream migration-note contract, no formal CHANGELOG obligation: upstream's git history plus whatever decision pages exist are the changelog, and the executing agent supplies the judgment it would have supplied anyway. The evidence this works without automation is this vault's own record — three structural migrations in five days at 0 lint errors, all agent-executed ([[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]], finding 4).

Rejected mechanisms: git submodules/subtrees (hostile ergonomics, no subsetting); a package registry (overkill at n≤3 instances); monorepo with shared schema (breaks the "point a new wiki at the upstream repo" distribution story and re-fuses the goals at the repo boundary where agents load contracts).

## Cross-Wiki References

Single-goal wikis force the knowledge graph to span repos. The normative rules — peer-link syntax (a wikilink target of the form `trellis::wiki/...`, resolved through the manifest's `peers` block), lint skipping of `::` targets, outbound-only link responsibility, and the cross-wiki independence rule — now live in `schema/wiki/conventions.md` (Cross-Wiki (Peer) Links) and `schema/wiki/page-format.md` (confidence derivation). What stays here is the rationale:

- **Why outbound-only:** an agent working in one wiki never needs another wiki's cooperation to keep its own graph clean; inbound links are the linking wiki's problem by symmetry.
- **Why no cross-wiki lint tool:** an agent asked to check external references follows the peer's move log — that's the whole mechanism. If manually following the trail ever proves error-prone in practice, that observed failure is the trigger for tooling, not before.
- **Why same-operator wikis are one source:** without the rule, the split would open a confidence-laundering loophole — self-derived claims corroborating themselves across repo lines, circular reporting with extra steps. The self-observation `medium` cap survives federation until a genuinely independent operator exists.

## Log Taxonomy

Three logs, aligned to the provenance grades in [[wiki/llm-wiki/constructs/operational-evidence]] (mechanical > journal > observed):

| File | Grade | Content | Maintenance |
|------|-------|---------|-------------|
| `wiki/moves.log` | Mechanical | Renames, moves, deletes — `date, old-path, new-path \| tombstone(disposition)` | **Generated** from git (`--diff-filter=RD --find-renames`); tombstone dispositions (`merged-into X`, `superseded-by Y`, `deleted`) are the one judgment field, annotated at delete time |
| `wiki/log.md` | Journal | Change journal — what was created/updated, where, why (unchanged from today) | Appended per ingest, as now |
| `wiki/episodes.md` | Narrative | Bounded accounts of unbounded activity: research deep dives, corrections, session retrospectives | Optional, per-session, with entry criteria — the 2026-07-07 retrieval-claim corrigendum narrative is the exemplar; routine ingests do not qualify |

The move log is what downstream wikis consume when checking their outbound references (each wiki publishes forwarding addresses instead of promising stable paths). All three are journals for graph-metric purposes and are excluded from connectivity counts, generalizing the orphan-check fix ([[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]], finding 5).

## Migration Plan

Each phase opens a meta-experiment line per [[designs/wiki-self-experimentation]] and is separately abortable.

- **Phases 0–1 — executed 2026-07-12.** Schema granulation and the split itself; see [[wiki/llm-wiki/decisions/trellis-repo-bootstrap]] and the bootstrap entry in [[wiki/log]].
- **Phase 2 — instantiation validation.** The interview skill exists (`seed/interview.md`) and `ai-research` is retrofitted as formal instance #1; the remaining validation is creating the pilot project wiki as instance #2 — which couples this design to the roadmap's standing highest-value item (running the pilot) instead of competing with it. Adopt `episodes.md` (independent of the split; cheap).
- **Phase 3 — nothing, until the trail fails.** There is no planned machinery beyond the breadcrumbs above. When someone following a trail finds a marker missing — an upgrade diff that was genuinely hard to read, a reference check that manual move-log following got wrong — that observed failure names the next breadcrumb. Build it then.

## Health After the Split

Each repo's health is scored against its own single goal, on two distinct evidence axes:

- **`ai-research`**: object-level throughput — ingests, syntheses, and above all the pilot actually running. Post-split there is no second goal to absorb sessions; the pilot is that repo's clearest health signal.
- **`trellis`**: *dogfood health* — the continuous, first-party signal that the method works, produced by this repo operating on a real research workload (lint clean, experiments opening and closing, real queries answered). This is genuine health, not proxy: the repo's subject is the method, so its own operation exercises its subject. It is also self-observed, so claims built on it stay capped at `medium` per the independence rule.
- **`trellis`, second axis**: *instance health* — sparse, arms-length signal from downstream wikis (instances existing, upgrades completing, friction reports harvested from downstream logs as operational evidence). Same operator for now, so still capped — but structurally separated for the first time, and the only axis that can ever escape the cap (an external adopter would land here).

## What This Design Does Not Fix

- **The pilot is still unrun.** The split sharpens that debt rather than discharging it: post-split, `ai-research`'s only goal is the practice, and the pilot is its clearest health signal.
- **Independence.** Same owner, same agents, more repos — the `medium` cap stands until an external operator adopts the method.
- **Ceremony risk.** The moving parts are deliberately few (a generated log, a one-time manifest, optional episodes), but if federation ceremony ever exceeds the one-line/one-assessment budget of [[designs/wiki-self-experimentation]], that is a finding against this design and belongs in its verdict assessment.
- **YAGNI exposure.** Portability machinery still runs ahead of a second *independent* instance. The mitigations stand: the identity crisis was an *observed* failure (not speculative), Phase 2's second instance is the roadmap's named next step, and Phase 3 is explicitly nothing-until-failure.

## Alternatives Considered

Recorded in [[wiki/llm-wiki/decisions/adopt-single-goal-federation]] — goal-tagging within one repo, monorepo with two wiki roots, schema-only extraction without a dogfood wiki, and the rejected first-draft rails.

## Open Design Questions

- **Retrieval across wikis** — query workflow becomes "own wiki first, one hop to peers via the manifest"; is qmd multi-collection indexing worth wiring, or is per-wiki search plus the peer registry enough at n≤3?
- **Does `episodes.md` subsume `raw/chats/`?** Proposed answer: no — `raw/chats/` holds owner conversations (sources, ingestable), `episodes.md` holds agent session narratives (operational record). Keep separate.
- **Move-log format details** — whether the log is per wiki root or per repo, and regeneration vs. append-on-commit.

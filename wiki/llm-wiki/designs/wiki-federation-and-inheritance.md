---
title: Wiki Federation and Schema Inheritance
type: design
description: The next evolution of the llm-wiki practice — one goal per wiki, the wiki method extracted into its own dogfooding upstream repository (Trellis), breadcrumb-based schema inheritance for downstream instances, and outbound-only cross-wiki references with move-log forwarding.
sources:
  - "[[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/designs/trellis-repo-design]]"
  - "[[wiki/llm-wiki/designs/project-wiki-template]]"
  - "[[wiki/llm-wiki/designs/project-wiki-application-guide]]"
  - "[[wiki/llm-wiki/designs/multi-agent-project-wiki-pattern]]"
  - "[[wiki/llm-wiki/designs/wiki-self-experimentation]]"
  - "[[wiki/llm-wiki/designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]]"
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[wiki/agent-context/subtopics/context-files/designs/agent-context-portability]]"
tags: [llm-wiki, federation, portability, schema-design, meta-research, knowledge-management]
created: 2026-07-10
timestamp: 2026-07-10T18:00:00Z
confidence: low
novelty: exploratory
status: draft
---

# Wiki Federation and Schema Inheritance

Epistemic note: `confidence: low` by this vault's own rules — the design traces to owner-directed design conversations ([[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]], [[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]) and nothing here has been implemented. Revised 2026-07-10 after owner review; the review's simplifications are incorporated. Status stays `draft` until the two remaining judgment calls in Open Design Questions are decided.

## Problem Statement

This repository serves two goals under one roof: a **practice reference** for building software with AI agents (AI SDLC, intent compiler, architecture diagrams, token economics) and a **laboratory** for evolving llm-wiki knowledge-base practice (the llm-wiki topic, the schema layer, the self-experimentation protocol). The 2026-07-10 outside-observer critique surfaced the costs of the dual mandate, and the owner concurred ([[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]):

- Meta-work and object-level work compete for the same sessions, and neither goal's health can be measured because both are scored against the same repo.
- The system that evolves the schema is also the system evaluated by it — the arms-length evidence [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]] lists as its own Missing Evidence ("a second project adopting any of these practices — the only route past `medium`") structurally cannot come from inside one repo.
- Content membership is unprincipled: "does this page belong here?" has no test when the wiki has two purposes.
- [[wiki/llm-wiki/designs/project-wiki-template]] is a one-shot instruction document — it can seed a new wiki once but gives downstream instances no way to detect or inherit upstream schema improvements.

## Design Principle: One Goal Per Wiki

A wiki may span many topics and subtopics, but it has exactly **one goal**, stated in its overview page. The goal is the membership test for content, the denominator for health metrics, and the first field of the instantiation manifest — an instance cannot be created without stating it.

Consequence: content serving a different goal lives in a different wiki and is reached by **cross-wiki reference**, which is what makes federation (below) load-bearing rather than optional. On adoption, this principle becomes an `invariant` page in the upstream wiki (`enforcement: manual` — checked at the lint judgment tier: does new content serve the stated goal?).

## Design Principle: Breadcrumbs Over Rails

Every mechanism in this design assumes an agent with judgment as the executor. Artifacts exist to make that judgment cheap to apply and easy to audit afterward — breadcrumbs — never to constrain it into determinism — rails. Determinism is reserved for what is already mechanical: git history, the generated move log, the existing deterministic lint tier. When a proposed mechanism includes a classification taxonomy, a required linkage, or a pipeline, the default answer is no; the question is only ever "what trail marker would have made the judgment cheaper?" ([[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]] — this design's own first draft, which specified change-classification taxonomies, migration-note contracts, and pairing lints, is the evidence that agents re-add rails unless the principle is written down.)

## Target Topology

| Repo | Role | Goal (one sentence) |
|------|------|---------------------|
| `trellis` (new) | Upstream: system-of-record for the wiki method, plus its dogfood wiki | Develop and evidence the wiki method itself, through its own operation |
| `ai-research` (this repo) | Downstream instance #1 | The owner's practice reference for building software with AI agents |
| pilot project wiki (future) | Downstream instance #2 | Per [[ai-research::wiki/intent-compiler/designs/pilot-implementation-playbook]] — project-local knowledge for one pilot codebase |

The `trellis` repo carries: the schema layer (granulated per below), `scripts/`, the agent contracts, the instantiation seed layer, and a wiki whose *subject is the method* — the current `wiki/llm-wiki/` topic content, the self-experimentation protocol, operational-evidence snapshots, and verdict assessments. Full repo specification: [[wiki/llm-wiki/designs/trellis-repo-design]]. The dogfood recursion is the point: the method's own wiki is the method's first proof, and the boundary between the distributable structural layer and the descriptive research *about* it must stay razor-sharp because downstream inheritance pulls the former and must never pull the latter.

### Content Disposition

Rule: a page moves if its **primary question is about knowledge-base practice** (the method); it stays if its primary question is about **building software with agents** (the practice). When in doubt, it stays — moving later is cheap once the move log (below) exists.

| Content | Disposition | Rationale |
|---------|-------------|-----------|
| `wiki/llm-wiki/` (all types) | Move | The method is the subject |
| `wiki/agent-context/` (context-files, retrieval, memory) | Move — *judgment call* | Its question is how agents consume knowledge and context — the consumption side of the method. Alternative: keep `context-files` here as general agent practice; the split is defensible either way |
| `wiki/ai-sdlc/`, `wiki/intent-compiler/`, `wiki/architecture-diagrams/`, `wiki/token-economics/` | Stay | Practice content |
| `raw/` files | Follow their source-captures | Provenance moves with the capture that cites it |
| `raw/repos/` operational snapshots | Move | Evidence about the method |
| `schema/`, `scripts/lint.py`, `scripts/qmd-index.sh` | Move to upstream; vendored copy stays here | See Inheritance |
| `wiki/index.md`, `log.md`, `overview.md`, `roadmap.md` | Stay in each wiki (per-instance files) | Every instance has its own |

## Schema Governance: Standalone Norms, Decision Archaeology

1. **Granular schema files** — `schema/page-types.md` splits into `schema/page-types/{type}.md` (one normative spec per type: required fields, expected sections, folder mapping, lint rules) plus `schema/page-types/registry.md` listing the full type vocabulary. The per-type file is the unit downstream instances subset, and the granularity is what makes an upgrade diff readable.
2. **Schema files are normative and standalone.** A schema file states the current rule completely and carries no back-references to rationale, history, or decision pages. What downstream vendors is norms, never the lab's reasoning about them.
3. **Rationale is captured as decision pages — sometimes.** When a schema change weighs alternatives or rests on assumptions that new information or empirical data could overturn, a `decision` page in the upstream dogfood wiki records the motivation, to be re-evaluated and superseded on its own clock. When a change doesn't warrant that, it just happens. No decision-per-change requirement, no pairing lint, no linkage from schema to decisions — discovery is **decision archaeology**: the decisions folder, the index, and search. ([[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]])
4. **Co-evolution is accepted, not engineered away.** Wiki contents inform schema decisions; the schema shapes what the wiki captures. The loop is safe because it passes through judgment (and, when worth keeping, a decision record with provenance) rather than through a deterministic derivation — there is no wiki→schema pipeline, and none is planned.

## Instantiation: Questionnaire → Manifest

Creating a wiki = pointing an agent at the upstream repo and answering an interview. This is an intent brief for a wiki instance — the same interrogate-then-confirm shape as [[ai-research::wiki/intent-compiler/designs/intent-refinement-stage]], applied to wiki creation. The answers persist as `wiki-manifest.yaml` at the instance root:

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

The manifest is a breadcrumb store, not a contract: it records what "the slice we picked for this wiki" *is* — provenance (what was inherited, from which commit), scope (which page types this instance carries), and the peer registry cross-wiki links resolve against — so the upgrade prompt has a durable referent. [[wiki/llm-wiki/designs/project-wiki-template]] is absorbed as the seed-content layer the questionnaire ships; [[wiki/llm-wiki/designs/project-wiki-application-guide]]'s adaptation guidance becomes the interview script. v0 is an agent-run procedure (a skill in the upstream repo), not a CLI tool.

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

Single-goal wikis force the knowledge graph to span repos. Rules:

1. **Outbound-only responsibility** (invariant candidate). A wiki lints its own outbound links, including cross-wiki ones; it neither knows nor cares who links in. An agent working in one wiki never needs another wiki's cooperation to keep its own graph clean.
2. **Syntax**: peer-prefixed wikilinks — a double-bracket link whose target reads `trellis::wiki/llm-wiki/constructs/source-isolation` — where the peer name before `::` resolves through the manifest's `peers` block. Unprefixed wikilinks stay intra-wiki and keep today's semantics. (Note: today's linter parses every double-bracket span in a page body as an intra-wiki link, with no code-span exemption — writing one literal example in this very page broke lint. The peer-prefix grammar must be added to `scripts/lint.py`'s link parser at the split so peer links are skipped rather than failing resolution.)
3. **There is no cross-wiki lint tool.** An agent asked to check external references follows the peer's move log — that's the whole mechanism. If manually following the trail ever proves error-prone in practice, that observed failure is the trigger for tooling, not before.
4. **Epistemics across the boundary**: citing a peer's source-capture imports its `evidence` tier at face value, but independence counting treats wikis operated by the same owner/agents as **one source** — otherwise the split creates a circular-reporting loophole where self-derived claims corroborate themselves across repo lines. The self-observation `medium` cap survives federation until a genuinely independent operator exists.

## Log Taxonomy

Three logs, aligned to the provenance grades in [[wiki/llm-wiki/constructs/operational-evidence]] (mechanical > journal > observed):

| File | Grade | Content | Maintenance |
|------|-------|---------|-------------|
| `wiki/moves.log` | Mechanical | Renames, moves, deletes — `date, old-path, new-path \| tombstone(disposition)` | **Generated** from git (`--diff-filter=RD --find-renames`); tombstone dispositions (`merged-into X`, `superseded-by Y`, `deleted`) are the one judgment field, annotated at delete time |
| `wiki/log.md` | Journal | Change journal — what was created/updated, where, why (unchanged from today) | Appended per ingest, as now |
| `wiki/episodes.md` | Narrative | Bounded accounts of unbounded activity: research deep dives, corrections, session retrospectives | Optional, per-session, with entry criteria — the 2026-07-07 retrieval-claim corrigendum narrative is the exemplar; routine ingests do not qualify |

The move log is what downstream wikis consume when checking their outbound references (each wiki publishes forwarding addresses instead of promising stable paths). All three are journals for graph-metric purposes and are excluded from connectivity counts, generalizing the orphan-check fix ([[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]], finding 5).

## Migration Plan

Each phase opens a meta-experiment line per [[wiki/llm-wiki/designs/wiki-self-experimentation]] and is separately abortable. The concrete bootstrap procedure lives in [[wiki/llm-wiki/designs/trellis-repo-design]].

- **Phase 0 — schema granulation.** Split `schema/page-types.md` into per-type files + registry; update `scripts/lint.py` and references. May be executed standalone in this repo or folded into the bootstrap.
- **Phase 1 — the split.** Create the `trellis` repo; move content per the disposition table; seed both repos' `moves.log` with the move itself; add `wiki-manifest.yaml` and the peer declaration here; rewrite severed links as peer-prefixed cross-references; both repos lint clean. The split is the first live exercise of the move-log and cross-reference breadcrumbs — dogfood by construction.
- **Phase 2 — instantiation.** Write the interview skill upstream; validate it twice: retrofit this repo as formal instance #1, then create the pilot project wiki as instance #2 — which couples this design to the roadmap's standing highest-value item (running the pilot) instead of competing with it. Adopt `episodes.md` (independent of the split; cheap).
- **Phase 3 — nothing, until the trail fails.** There is no planned machinery beyond the breadcrumbs above. When someone following a trail finds a marker missing — an upgrade diff that was genuinely hard to read, a reference check that manual move-log following got wrong — that observed failure names the next breadcrumb. Build it then.

## Health After the Split

Each repo's health is scored against its own single goal, on two distinct evidence axes:

- **`ai-research`**: object-level throughput — ingests, syntheses, and above all the pilot actually running. Post-split there is no second goal to absorb sessions; the pilot is this repo's clearest health signal.
- **`trellis`**: *dogfood health* — the continuous, first-party signal that the method works, produced by the repo operating on a real research workload (lint clean, experiments opening and closing, real queries answered). This is genuine health, not proxy: the repo's subject is the method, so its own operation exercises its subject. It is also self-observed, so claims built on it stay capped at `medium` per the independence rule.
- **`trellis`, second axis**: *instance health* — sparse, arms-length signal from downstream wikis (instances existing, upgrades completing, friction reports harvested from downstream logs as operational evidence). Same operator for now, so still capped — but structurally separated for the first time, and the only axis that can ever escape the cap (an external adopter would land here).

## What This Design Does Not Fix

- **The pilot is still unrun.** The split sharpens that debt rather than discharging it: post-split, this repo's only goal is the practice, and the pilot is its clearest health signal.
- **Independence.** Same owner, same agents, more repos — the `medium` cap stands until an external operator adopts the method.
- **Ceremony risk.** The new moving parts are deliberately few (a generated log, a one-time manifest, optional episodes), but if bootstrap ceremony exceeds the one-line/one-assessment budget of [[wiki/llm-wiki/designs/wiki-self-experimentation]], that is a finding against this design and belongs in its verdict assessment.
- **YAGNI exposure.** Portability machinery ahead of a second instance is the same shape as the QMD early graduation. The mitigations are the trigger: the identity crisis is an *observed* failure (not speculative), Phase 2's second instance is already the roadmap's named next step, and Phase 3 is explicitly nothing-until-failure.

## Alternatives Considered

- **Goal-tagging within one repo** — tag pages by which goal they serve. Rejected: no distribution story, evaluator and evaluated stay fused, and the membership test remains advisory.
- **Monorepo with two wiki roots** — rejected: agents load contracts per-repo, so the boundary agents actually experience stays blurred, and "point a new wiki at the upstream repo" has no clean referent.
- **Schema-only extraction (no dogfood wiki upstream)** — publish `schema/` + scripts as a bare template repo. Rejected: it loses the lab — the method research needs its own evidence base, and a practices repo with no real workload violates the workload-stays-real invariant of [[wiki/llm-wiki/designs/wiki-self-experimentation]].
- **First-draft rails** (rejected 2026-07-10 owner review): change-classification taxonomy, upstream migration-note and CHANGELOG contracts, mandatory schema↔decision linkage, pairing lint, a cross-wiki lint tier, a wiki→schema generation pipeline. All replaced by breadcrumbs plus agent judgment; recorded here so they are not re-proposed. ([[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]])

## Open Design Questions

- **Disposition of `wiki/agent-context/`** — move (recommended: its question is the method's consumption side) or split it, keeping `context-files` here? Owner call before Phase 1.
- **Cross-wiki independence rule** — the "same operator counts as one source across wikis" rule above needs explicit ratification; it is the guard against confidence laundering via federation.
- **Retrieval across wikis** — query workflow becomes "own wiki first, one hop to peers via the manifest"; is qmd multi-collection indexing worth wiring, or is per-wiki search plus the peer registry enough at n≤3?
- **Does `episodes.md` subsume `raw/chats/`?** Proposed answer: no — `raw/chats/` holds owner conversations (sources, ingestable), `episodes.md` holds agent session narratives (operational record). Keep separate.
- **Move-log format details** — whether the log is per wiki root or per repo, and regeneration vs. append-on-commit.

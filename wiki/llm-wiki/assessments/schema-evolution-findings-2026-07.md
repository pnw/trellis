---
title: "Schema Evolution Findings, July 2026"
type: assessment
description: First operational-evidence verdict on this wiki's practice changes — what the evidence-tier adoption, schema-layer refactor, migrations, and lint tooling actually revealed, from the repo's own record.
sources:
  - "[[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]"
related:
  - "[[designs/wiki-self-experimentation]]"
  - "[[wiki/llm-wiki/constructs/operational-evidence]]"
  - "[[designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
  - "[[designs/agent-context-portability]]"
tags: [llm-wiki, meta-research, epistemics, self-experimentation, schema-design, lint]
created: 2026-07-08
timestamp: 2026-07-08T03:30:00Z
confidence: medium
status: stable
---

# Schema Evolution Findings, July 2026

## Scope

Verdicts and findings from this wiki's 2026-07-04 → 2026-07-08 practice-evolution burst — three structural migrations, the evidence-tier schema adoption, the schema-layer refactor, and the lint tooling — drawn from the snapshotted operational record [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]. Retroactive per the protocol in [[designs/wiki-self-experimentation]]: these changes predate the hypothesis-line habit, but the record covers their before/after.

## Bottom Line

The practice changes earned their keep, and the strongest findings are the uncomfortable ones: the pre-schema confidence scalar overstated support on roughly a quarter of the vault, agent-authored corroboration counting laundered vendor documentation into high confidence, and tooling assumptions (a journal counted as discovery links) silently masked real defects. Self-observation caps these at `medium` confidence — but they are this vault's first non-`llm-generated` evidence about its own core topic.

## Validated

1. **Asserted epistemic scalars inflate; derived ones bite.** The retroactive confidence-ceiling audit found 27 of 113 pages (~24%) above what their cited sources support, concentrated in llm-generated-only design pages and vendor-doc-sourced product pages. A self-assessed enum with a definition nobody re-checks drifts optimistic; a derivation rule found the drift in one pass. [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]
2. **Independence, not corroboration count, is the load-bearing concept.** The motivating defect — a page reaching `high` because six vendor documents "corroborated" each other — was a definition bug, not an authoring lapse: the old rule counted sources; nothing required them to be independent. [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]
3. **Canonical semantics in a tool adapter will drift.** The authoritative `confidence` definition lived only in `.kiro/steering/`, invisible to the other two agents operating the vault — and usage drifted from it until the schema-layer refactor moved semantics to shared ground. Direct operational confirmation of the portability rule in [[designs/agent-context-portability]]: duplicated or tool-siloed manifests are future contradictions. [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]
4. **Structural migration is cheap at this scale with agent labor.** Three migrations (typed folders, root-relative wikilinks, schema-layer extraction) plus a 50-page frontmatter backfill landed in five days with lint at 0 errors after each — the "schema can evolve during use" premise of the llm-wiki pattern held in practice at ~130 pages. [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]
5. **Graph metrics need journal exclusions.** The orphan check counted `wiki/log.md` — which mentions nearly every page at creation — as an incoming link, masking 6 real orphans until the exclusion was added. Append-only journals are provenance, not discovery, and must be excluded from connectivity metrics. [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]

## Plausible but Unvalidated

- **The deterministic/judgment lint split is the right boundary.** One scripted run replaced the agent re-deriving mechanical checks, and no judgment-tier regression has surfaced — but only days have passed.
- **Environment egress policy is a first-class tooling constraint.** The qmd semantic-model download was blocked by network policy while lexical search worked; one instance, but it suggests knowledge-tool choices for agent-operated vaults must be evaluated inside the target sandbox, not on a laptop.
- **Multi-session concurrency is workable with git alone.** One same-day divergence on `main` (parallel Fable/Sonnet sessions) resolved with an ordinary rebase and a one-file journal conflict. Nothing broke — but the coordination invariants in [[designs/multi-agent-project-wiki-pattern]] remain untested beyond n=1.

## Speculative

- Whether the evidence-tier schema *changes agent behavior* (the field-earns-its-place test it was adopted under) — no ingest has yet run end-to-end under the new rules by an agent that didn't design them.

## Contradictions / Risks

- Observer-operator conflation: the agents that made these changes produced the record and wrote this assessment, with owner review at merge. The mechanical sections of the snapshot mitigate but do not remove this.
- Survivorship framing: the record naturally documents changes that were kept; abandoned approaches (e.g., the unbuilt `by-tag.md` index) leave thinner traces.

## Missing Evidence

- An end-to-end ingest under the new schema by a fresh agent session (tests finding 3's fix and the speculative item together).
- A second project adopting any of these practices — the only route past `medium` for all of the above.
- Before/after cost data: change stats exist, but token/time costs of the migrations were not recorded.

## Related Artifacts

- [[designs/wiki-self-experimentation]] — the protocol this assessment is the first instance of
- [[designs/evidence-tier-schema]] — subject of findings 1–2; its confidence remains capped pending external corroboration, per its own rules
- [[wiki/llm-wiki/constructs/operational-evidence]] — the evidence class used here

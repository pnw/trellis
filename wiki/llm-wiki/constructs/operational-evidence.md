---
title: Operational Evidence
type: construct
description: First-party operational records — logs, git history, lint outputs, session transcripts — used as empirical sources for evaluating and evolving the very practices that produced them.
sources:
  - "[[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]]"
related:
  - "[[designs/wiki-self-experimentation]]"
  - "[[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]"
  - "[[designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
tags: [llm-wiki, meta-research, epistemics, self-experimentation, provenance]
created: 2026-07-08
timestamp: 2026-07-08T03:30:00Z
confidence: low
novelty: exploratory
status: stable
aka: ["dogfooding evidence", "lab-notebook evidence", "first-party operational record"]
coined_by: "This project (owner + Claude Code thread, 2026-07-08)"
---

# Operational Evidence

## Definition

Operational evidence is a knowledge base's own operational record — its operation journal, version-control history, lint/quality outputs, and session transcripts — treated as an empirical source for evaluating the practices that produced it. It is what a lab notebook is to a lab: first-party, contemporaneous, and about the process itself. [[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]]

## Why It Matters

For a wiki whose subject includes its own methods, operational evidence is the only path to non-`llm-generated` evidence about those methods short of external replication. Every page in this vault's llm-wiki topic is otherwise sourced from LLM conversations and secondhand guides — capped at `low`/`medium` by the vault's own derivation rules. The operational record is what converts practice-tinkering into findings: the retroactive confidence audit (27 of 113 pages above ceiling), the vendor-doc corroboration laundering, and the tool-adapter schema drift were all discovered *operationally*, not read in a source. [[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]] [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]

## Mechanism / Structure

Record types, strongest first:

1. **Mechanical** — git history with change stats, file counts, script outputs. Regenerable by re-running commands at a pinned commit; verifiable independent of any narrator.
2. **Journal** — the operation log: agent-authored, owner-merged narration of what was done and why. Contemporaneous but narrated.
3. **Observed** — session-transcript facts (tool outputs seen during a session) that are real but not independently regenerable.

To be citable, operational evidence is snapshotted into `raw/` (e.g., `raw/repos/`) at a pinned commit and captured like any other source, with the provenance grade of each section marked — see [[designs/wiki-self-experimentation]] for the workflow and [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]] for the first instance.

### Epistemic Handling

- The snapshot capture carries `evidence: empirical-primary` — it is original systematic observation with reproducible extraction ([[designs/evidence-tier-schema]]).
- **All first-party snapshots of the same project share authorship and identity: they count as one source under the independence rule.** No accumulation of self-observation can push a downstream page past `medium`; only external corroboration (another project adopting the practice, an independent study) unlocks `high`.
- The observer is the operator — and here, an AI operator narrating to a reviewing owner ("AI is an abstraction layer removed from me"). The discipline that keeps this honest is preferring mechanical records over journal narration wherever both cover an event.

## Distinctions

- **Not `llm-generated` despite being largely agent-authored** — the discriminator is verifiability against repository state, not who typed it. A deep-research report cannot be re-derived; a shortstat can.
- **Not independent corroboration for itself** — a practice cannot vouch for itself however many snapshots exist; the independence rule enforces this structurally.
- **Not telemetry** — no instrumentation is implied; the records are artifacts the workflow already produces (commits, journal entries, lint runs), captured rather than collected.
- **Prior art under other names** — lab notebooks, software dogfooding, DevOps DORA-style delivery telemetry, and action research all rest on the same move; the framing here is its application to agent-maintained knowledge bases.

## Evidence and Sources

- Coined in [[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]] after the owner ratified practice-evolution as a first-class goal of this wiki.
- First instance: [[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]].
- Unvalidated as a practice: whether deliberate operational-evidence capture actually improves practice decisions is itself an open experiment (see the meta-experiment log in [[wiki/roadmap]]).

## Related Artifacts

- [[designs/wiki-self-experimentation]] — the protocol that produces and consumes this evidence
- [[designs/evidence-tier-schema]] — the tiering and independence rules that govern it
- [[wiki/llm-wiki/constructs/source-isolation]] — why snapshots go to `raw/` instead of citing live, mutating files

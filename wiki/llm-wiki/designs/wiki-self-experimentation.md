---
title: Wiki Self-Experimentation
type: design
description: The protocol by which this wiki evolves its own knowledge-base practices as a first-class research activity — hypothesis on change, operational-evidence snapshot, verdict assessment, confidence cascade.
sources:
  - "[[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/constructs/operational-evidence]]"
  - "[[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]"
  - "[[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]]"
  - "[[wiki/llm-wiki/designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
tags: [llm-wiki, meta-research, self-experimentation, methodology, knowledge-management]
created: 2026-07-08
timestamp: 2026-07-08T03:30:00Z
confidence: low
novelty: exploratory
status: stable
---

# Wiki Self-Experimentation

Epistemic note: by this vault's own rules, confidence is `low` — the protocol traces to an LLM-assisted design conversation and one day of deliberate use — while the recommendation to adopt was strong: every step reuses existing machinery (roadmap lines, raw snapshots, source-captures, assessments), so the ceremony cost is near zero.

## Purpose

Make the evolution of this wiki's own knowledge-base practices scientific and methodical rather than incidental. The llm-wiki pattern is directional, not an implementation spec; this wiki is the pilot instance where its implementation specifics get invented, tested, and evidenced. This protocol is what separates deliberate practice research from unrecorded tinkering. [[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]]

## System Boundary

**Inside:** Practice changes to this wiki (schema, workflows, tooling, conventions), their hypotheses and revisit triggers, operational-evidence snapshots, verdict assessments, and the resulting confidence updates.

**Outside:** The research content itself (the other topics), and the separate codebase pilot ([[ai-research::wiki/intent-compiler/designs/pilot-implementation-playbook]]) — same loop shape, different subject.

## Core Model

```
practice change (schema, workflow, tooling, convention)
  -> one hypothesis line in the roadmap meta-experiment log:
       what changed, expected benefit, revisit trigger
  -> operate normally (the workload IS the experiment)
  -> at the trigger: snapshot operational record into raw/repos/
       (mechanical > journal > observed, provenance marked)
  -> source-capture the snapshot (empirical-primary, reliability-noted)
  -> verdict assessment: kept / revised / reverted, with findings
  -> re-derive confidence on llm-wiki practice pages the verdict touches
  -> prune the roadmap line
```

## Components

- **Meta-experiment log** — a subsection of [[wiki/roadmap]]'s Wiki Self-Maintenance section. One line per open experiment; pruned on verdict. Not a new file, not a new page type.
- **Operational-evidence snapshots** — `raw/repos/` extracts at a pinned commit, per [[wiki/llm-wiki/constructs/operational-evidence]]. First instance: [[raw/repos/ai-research-operational-history-2026-07-08.md]].
- **Verdict assessments** — `wiki/llm-wiki/assessments/` pages citing the snapshot capture. First instance: [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]].

## Invariants

1. **A change without a hypothesis line is tinkering, not an experiment.** Tinkering is allowed — but it cannot later be claimed as evidence.
2. **Verdicts cite snapshots, not live files.** The journal and git history mutate; assessments cite a pinned `raw/` extract so they stay regenerable (source isolation applied to self-observation).
3. **Mechanical over narrated.** Where git and the journal both cover an event, cite git. This is the standing answer to the "AI is an abstraction layer removed from me" constraint: the owner can verify a shortstat without trusting any narrator.
4. **Self-observation caps at `medium`.** All first-party snapshots count as one source under the independence rule; claiming more requires external corroboration.
5. **The workload stays real.** Meta-findings are only meaningful while genuine research flows through the wiki — a practices lab with no content is a terrarium. Practice changes ride alongside content work; they do not replace it.
6. **Ceremony budget: one line to open, one assessment to close.** If an experiment needs more process than that, the experiment is probably too big.

## Workflow Notes

- Retroactive experiments are legitimate: a practice adopted without a hypothesis line can still get a verdict assessment if the operational record covers its before/after (the evidence-tier schema, adopted 2026-07-07, got exactly this treatment).
- Verdicts can be partial — "kept, with these observed costs" is a finding; forced binary conclusions overstate n=1 evidence.
- Subsequent snapshots reuse the same extraction method at later commits so per-experiment before/after comparisons stay mechanical.

## Evidence and Rationale

- Ratified as a first-class goal by the owner in [[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]] — including the motivations (practice research on a directionally-specified pattern; intrinsic interest; phone-sized workability) that make low ceremony a hard requirement.
- The protocol's value premise — that the operational record already contains real findings — is demonstrated rather than assumed: see [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]].

## Open Design Questions

- What snapshot cadence is right — per-experiment triggers only, or also a periodic (monthly?) baseline extract?
- Should the deterministic parts of a verdict (page counts, lint deltas between snapshots) be scripted like `scripts/lint.py`?
- Does the meta-experiment log stay prunable in practice, or does it accumulate like the open-question backlog it lives beside?
- When the practices stabilize, do the verdict assessments consolidate into a synthesis ("what running an llm-wiki actually requires") — the roadmap's "empirical self-study" candidate topic?

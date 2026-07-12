---
title: Trellis Method Overview
type: synthesis
description: High-level synthesis of the Trellis wiki method — the llm-wiki pattern lineage, this method's epistemic schema and self-experimentation practice, agent context and retrieval research, and the federation model.
sources:
  - "[[wiki/llm-wiki/sources/karpathy-llm-wiki-knowledge-base-guide]]"
  - "[[wiki/llm-wiki/sources/llm-wiki-effectiveness-deep-research]]"
  - "[[wiki/llm-wiki/sources/epistemic-metadata-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-as-lab-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-operational-history-2026-07-08]]"
  - "[[wiki/llm-wiki/sources/wiki-federation-claude-code-thread]]"
  - "[[wiki/llm-wiki/sources/wiki-federation-review-claude-code-thread]]"
related:
  - "[[wiki/llm-wiki/constructs/llm-wiki-pattern]]"
  - "[[wiki/llm-wiki/designs/evidence-tier-schema]]"
  - "[[wiki/llm-wiki/designs/wiki-self-experimentation]]"
  - "[[wiki/llm-wiki/designs/wiki-federation-and-inheritance]]"
  - "[[wiki/llm-wiki/designs/trellis-repo-design]]"
  - "[[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]"
  - "[[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]]"
tags: [llm-wiki, knowledge-management, epistemics, agent-context, federation, meta-research]
created: 2026-07-12
timestamp: 2026-07-12T04:30:00Z
status: stable
---

# Trellis Method Overview

## Goal

**Develop and evidence the wiki method itself, through its own operation.** This repository is the upstream home of the Trellis wiki method: the distributable schema, scripts, and instantiation seed live beside this lab wiki, whose research workload *is* the method's test bed. Content that serves a different goal — the owner's software-building practice, project-local knowledge — lives in peer wikis (see Federation below) and is reached by cross-reference, never hosted here.

This wiki was split out of `ai-research` on 2026-07-12 precisely because two goals in one repo made both unmeasurable ([[wiki/llm-wiki/designs/wiki-federation-and-inheritance]]). Its health reads on two axes: dogfood health (the lab operating cleanly on a real workload — genuine but self-observed evidence, capped at `medium` per the independence rule) and instance health (downstream wikis existing and upgrading — the only axis that can escape the cap).

## Current Synthesis

### The Pattern Lineage

The [[wiki/llm-wiki/constructs/llm-wiki-pattern]] — Karpathy's April 2026 workflow where LLM agents build structured markdown knowledge bases from raw sources — is directional rather than an implementation spec; Google's [[wiki/llm-wiki/entities/open-knowledge-format]] formalizes the format layer but not the practice. Trellis is this lineage's opinionated implementation: a [[wiki/llm-wiki/constructs/three-layer-architecture]] (immutable `raw/`, agent-maintained `wiki/`, normative `schema/`) extended with a two-axis epistemic schema ([[wiki/llm-wiki/designs/evidence-tier-schema]]): source-captures carry a required `evidence` tier, downstream pages derive `confidence` from tier and *independence* of cited sources, and [[wiki/llm-wiki/constructs/source-isolation]] keeps captures regenerable and corroboration honest.

### The Method Studies Itself

Deliberate practice evolution is this wiki's object-level work, governed by [[wiki/llm-wiki/designs/wiki-self-experimentation]] (hypothesis line on change, operational-evidence snapshot, verdict assessment) with [[wiki/llm-wiki/constructs/operational-evidence]] as the evidence class. First verdict: [[wiki/llm-wiki/assessments/schema-evolution-findings-2026-07]] — asserted confidence scalars inflate (~24% of pages over ceiling), independence not corroboration count is load-bearing, tool-siloed schema semantics drift. Self-observation caps all of it at `medium`; downstream instances are the route past the cap.

### How Agents Consume Wikis

The `agent-context` topic covers the consumption side: [[wiki/agent-context/subtopics/retrieval/constructs/agentic-search]] (grep/glob over the raw corpus) is the default retrieval mode with QMD-style local hybrid search as the graduation path ([[wiki/llm-wiki/decisions/adopt-agentic-search-with-qmd]], [[wiki/agent-context/subtopics/retrieval/designs/knowledge-surfacing-design]]); context-file research ([[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]], the ETH Zurich findings) grounds what belongs in agent contracts; and the memory-systems captures delimit what a curated wiki is *not* ([[wiki/llm-wiki/comparisons/llm-wiki-vs-agent-memory]]).

### Federation

One goal per wiki; many topics per wiki; wikis cross-reference through peer-prefixed links; each wiki maintains only its outbound links, publishing forwarding addresses in `wiki/moves.log`. Instantiation is an interview (`seed/interview.md`) whose answers persist as `wiki-manifest.yaml`; inheritance is three breadcrumbs (manifest pin, per-type schema files, move log) plus a prompt. Design principle throughout: **breadcrumbs over rails** — artifacts make agent judgment cheap and auditable, never replace it. [[wiki/llm-wiki/designs/wiki-federation-and-inheritance]] [[wiki/llm-wiki/designs/trellis-repo-design]]

## Tensions and Contradictions

- All method evidence is currently self-observed or single-operator; the `medium` confidence cap stands until an external operator adopts the method.
- The federation machinery (peer links, move log, manifest) shipped with the split itself as its first exercise — n=1, and the same session built and used it.
- The lab's workload-stays-real invariant is untested post-split: the method research must keep flowing here now that the practice research lives elsewhere.

## Update Triggers

- A downstream instance completes an upgrade using the breadcrumbs (first real inheritance test).
- The pilot project wiki is instantiated via `seed/interview.md` (first real instantiation test).
- Any external operator adopts the method (lifts the independence cap).

See [[wiki/roadmap]] for the open backlog and the meta-experiment log.

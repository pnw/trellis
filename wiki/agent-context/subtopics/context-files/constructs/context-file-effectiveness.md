---
title: Context File Effectiveness
type: construct
description: "The empirical question of when repository-level agent context files help coding agents versus when they add cost, redundancy, or distraction."
sources:
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
related:
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]]"
  - "[[wiki/agent-context/subtopics/context-files/entities/agents-md]]"
  - "[[wiki/llm-wiki/designs/project-wiki-template]]"
tags: [agent-context, context-engineering, agents, cost-optimization]
created: 2026-07-06
timestamp: 2026-07-06T00:00:00Z
confidence: high
novelty: emerging
coined_by: "Gloaguen et al. (ETH Zurich, 2026)"
aka: ["repository context files", "agent context file utility", "AGENTS.md effectiveness"]
---

# Context File Effectiveness

## Definition

Context file effectiveness is the measured impact of repository-level agent guidance files, such as AGENTS.md or CLAUDE.md, on task success, cost, reasoning steps, and agent behavior.

## Why It Matters

Agent context files are usually treated as harmless project memory. The ETH Zurich study challenges that assumption: LLM-generated context files can reduce task success while increasing cost, and human-curated files provide only modest gains unless they contain details agents cannot infer independently: [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]].

For this wiki, the implication is practical: a project template should create a small front door for non-obvious operational guidance, then route agents to deeper wiki pages only when needed.

## Mechanism / Structure

| Context Type | Expected Effect | Reason |
|--------------|-----------------|--------|
| LLM-generated broad overview | Negative or wasteful | Often duplicates code/docs and increases attention load |
| Human-curated operational guidance | Modestly positive | Captures commands, boundaries, and counterintuitive local rules |
| Non-inferable details | Highest value | Provides facts the agent cannot reliably derive from repository inspection |
| Large architectural summaries | Often low value | Agents can usually inspect code structure directly |

The pattern is not "more context helps." It is "specific, non-redundant context helps when it changes the agent's next action."

## Distinctions

- Different from [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]], which is the content-selection rule.
- Different from [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]], which explains one mechanism by which irrelevant context can harm accuracy.
- Different from [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]], which describes how context should be loaded at different depths.

## Evidence and Sources

- LLM-generated context files reduced task success in most tested settings and increased inference cost by 20-23%: [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]].
- Human-curated context files improved AGENTbench success by about 4 percentage points while still adding cost overhead: [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]].
- Augment's AGENTS.md synthesis recommends emphasizing commands, boundaries, and non-obvious patterns rather than broad architectural summaries: [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]].

## Related Artifacts

- [[wiki/agent-context/subtopics/context-files/entities/agents-md]] — the emerging standard file format.
- [[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]] — the selection rule for what belongs in context files.
- [[wiki/llm-wiki/designs/project-wiki-template]] — applies this construct to project-specific wiki structure.

## Open Questions

- How much of the ETH Zurich result transfers from coding repos to research wikis?
- What is the best metric for deciding whether a project context file is worth its token overhead?
- Can lint checks detect redundant or inferable context before it degrades agent performance?

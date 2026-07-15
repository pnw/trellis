---
title: Non-Inferable Details
type: construct
description: "The principle that agent context files should contain only information the agent cannot discover independently — custom commands, non-standard tooling, counterintuitive constraints."
sources:
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
related:
  - "[[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]]"
  - "[[designs/knowledge-surfacing-design]]"
tags: [agent-context, context-engineering, design-patterns]
created: 2026-07-05
timestamp: 2026-07-05T13:27:00Z
confidence: high
novelty: emerging
coined_by: "Gloaguen et al. (ETH Zurich, 2026); term crystallized by Augment Code"
aka: ["non-discoverable details", "minimal context principle"]
---

# Non-Inferable Details

## Definition

The principle that agent context files (AGENTS.md, CLAUDE.md, steering files, etc.) should contain only information the agent cannot discover independently from the codebase, documentation, or environment. Everything else is redundant and actively harmful (increases cost, may decrease accuracy via [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]]).

## Why It Matters

The ETH Zurich study proved empirically that LLM-generated context files — which typically contain architectural overviews, code style descriptions, and other *inferable* information — reduce task success while increasing costs. The fix isn't better-written context files; it's *less* content that targets only what the agent genuinely cannot figure out on its own.

This principle directly governs what belongs in this wiki's `.kiro/steering/` files.

## Mechanism / Structure

**What qualifies as non-inferable:**

| Include | Reason |
|---------|--------|
| Custom build commands not documented elsewhere | Agent can't discover `pixi run` if it's never seen pixi |
| Non-standard tooling choices | Agent defaults to the most common tool in training data |
| Counterintuitive architectural decisions | "This API never throws — don't use try/catch" |
| Constraints that look wrong but are intentional | "Never modify vendor/ even if it seems outdated" |
| Permission boundaries | "Ask before adding dependencies" |

**What does NOT qualify (already inferable):**

| Exclude | Reason |
|---------|--------|
| Architectural overviews | Agent finds these from code structure and existing docs |
| Code style that matches .editorconfig or linters | Already enforced by tooling |
| Information already in README | Redundant; adds cost without signal |
| Domain model descriptions | Agent reads the code |
| Standard tooling (npm, pytest, cargo) | Agent already knows conventions |

**The redundancy test:** When ETH Zurich removed all other documentation from repos, LLM-generated context files improved performance by 2.7%. This proves the files were redundant with documentation agents already access.

## Distinctions

- Not "keep context files short" (a length heuristic) — it's about *content selection*. A short file full of inferable details still hurts.
- Not "don't document anything" — it's about what goes in the *agent-facing* file specifically
- The principle is context-dependent: what's inferable depends on model capabilities, available tools, and existing documentation
- Applies to steering files, not to source-capture or wiki pages (which serve a different purpose)

## Evidence and Sources

- ETH Zurich: LLM-generated files (containing inferable content) reduced success by 0.5–2% at +20-23% cost — [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]
- ETH Zurich: removing Architecture sections while keeping commands/constraints produces same agent behavior at lower cost — [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]
- Augment article: "Non-Obvious Patterns" section delivers highest signal-to-noise ratio — [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]
- GitHub analysis of 2,500+ repos: "Never commit secrets" = most common *helpful* constraint (non-inferable because there's no linter for it) — [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]

## Related Artifacts

- [[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]] — why inferable content is actively harmful, not just wasteful
- [[designs/knowledge-surfacing-design]] — design approaches informed by this principle
- [[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]] — the structural solution (load only what's needed)

## Open Questions

- Does the non-inferable threshold shift as models get more capable? (What's non-inferable for GPT-4o may be inferable for a future model)
- For a knowledge wiki (vs. code repo), is the principle different? Wiki pages *are* the documentation — the "redundancy with existing docs" argument doesn't apply the same way.

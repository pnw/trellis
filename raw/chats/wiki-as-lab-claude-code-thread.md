---
title: "Claude Code Thread: The Wiki as Its Own Laboratory"
source: claude-code-thread
created: 2026-07-08
captured: 2026-07-08
---

# Claude Code Thread: The Wiki as Its Own Laboratory

Continuation of the 2026-07-07/08 Claude Code review session (see [[raw/chats/intent-refinement-claude-code-thread.md]] and [[raw/chats/epistemic-metadata-claude-code-thread.md]]). After the assistant repeatedly warned against meta-work ("no more faffing about with the wiki's own machinery"), the owner reframed the purpose of that work.

## Owner Reframing

> Fair point about faffing about. However I find it interesting in its own right and while the goal of the wiki contents may not have progressed, one of my other goal with this wiki is to use this research topic as a pilot for experimenting and evolving my knowledge base practices based on the llm-wiki idea since it's vague and conceptually directional more than implementation specifics. That's why I keep asking about and refining the wiki meta. Also it's fun and I can do it on my phone while multitasking

## Claude Response (condensed)

The reframing dissolves most of the "meta-recursion" critique. If the repo is a laboratory for knowledge-base practice itself — the llm-wiki idea being directional rather than an implementation spec — then schema evolution is not overhead on the research; it *is* the research. The evidence-tier schema, source-isolation ratification, schema-layer refactor, and roadmap are working implementation specifics the llm-wiki concept lacks. The narrowed warning: meta-experiments only produce meaningful findings because a real research workload flows through the wiki — a practices lab with no content is a terrarium.

Two consequences of taking the lab goal seriously:

1. **An uncaptured evidence stream.** Everything in the llm-wiki topic is sourced from LLM conversations and secondhand guides — capped at low/medium by the wiki's own schema. But the repo's operational history is first-party empirical evidence about the pattern: the log records every practice change, git records what it cost, lint records whether quality held. Concrete findings already produced: retroactive confidence derivation re-scored 27 of 113 pages; the corroboration-count confidence definition let vendor docs launder into high confidence; canonical schema semantics buried in a tool adapter drifted from practice. The upgrade is deliberateness: when a practice changes, record hypothesis and revisit trigger (one roadmap line); when a verdict exists, write it as an assessment citing a snapshotted operational record. This converts meta-tinkering into the vault's first non-llm-generated evidence on its own core topic — a second pilot that fits in a pocket.

2. **The lab goal must be stated where agents can see it.** Neither the AGENTS.md Core Mission nor the overview named "evolve knowledge-base practice through this wiki's own operation" as a first-class goal, which is why the assistant kept scoring schema evolution as drift — and any future agent reading the contract cold would do the same. The goal passes the non-inferable-details test.

## Owner Capture Request

> Interesting. Let's capture that dynamic in the wiki then, including any insights or wiki pages that can be captured as meta sources and evidence, whatever that means. I would like to be scientific and methodical where possible but sometimes AI is an abstraction layer removed from me. Btw update from main before making changes

The owner's caveat — "AI is an abstraction layer removed from me" — was taken as a design constraint at capture time: the operational record is largely agent-authored and owner-reviewed at merge, so meta sources must separate what is mechanically verifiable (git history, lint output) from what is agent-narrated (motivations, assessments), and reliability notes must say which is which.

## Implementation at Capture Time

Created: the operational-evidence construct, the wiki-self-experimentation design (the methodology), a mechanical operational-history snapshot in `raw/repos/`, its source-capture, and a first findings assessment. Stated the lab goal in the AGENTS.md Core Mission and the overview's Purpose section (which a parallel session had just added, covering the personal-reference and day-job purposes but not the lab purpose).

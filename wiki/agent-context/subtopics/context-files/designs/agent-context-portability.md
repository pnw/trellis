---
title: Agent Context Portability
type: design
description: "A cross-platform pattern for keeping agent instructions portable across Codex, Claude Code, Kiro, and other coding agents without duplicating drifting manifests."
sources:
  - "[[wiki/agent-context/subtopics/context-files/sources/openai-codex-agents-md-docs]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/claude-code-memory-docs]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/kiro-steering-docs]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/configuration-smells-agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/agents-md-efficiency]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/claude-code-agentic-manifests]]"
  - "[[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]]"
related:
  - "[[wiki/agent-context/subtopics/context-files/entities/agents-md]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/context-file-effectiveness]]"
  - "[[wiki/agent-context/subtopics/context-files/constructs/non-inferable-details]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/progressive-disclosure-model]]"
  - "[[wiki/agent-context/subtopics/retrieval/constructs/attention-dilution]]"
tags: [agent-context, context-engineering, agents, portability]
created: 2026-07-06
timestamp: 2026-07-12T07:00:00Z
confidence: medium
novelty: emerging
---

# Agent Context Portability

## Definition

Agent context portability is the design problem of writing one set of project instructions that works across multiple coding agents while preserving each tool's native loading semantics, routing features, and precedence rules. Also called agent-agnostic context, portable agent instructions, cross-agent manifests, or agent manifest interoperability.

## Design Thesis

Use `AGENTS.md` as the canonical cross-agent instruction file, then add the thinnest native wrapper each tool needs. Codex should read `AGENTS.md` directly through its documented discovery chain; Claude should use `CLAUDE.md` with `@AGENTS.md` import or a symlink; Kiro should either read `AGENTS.md` directly for always-on baseline guidance or use `.kiro/steering/*.md` files as routing wrappers for Kiro-only inclusion modes. This pattern follows Codex's AGENTS.md discovery behavior, Claude's documented AGENTS.md import pattern, and Kiro's documented support for both AGENTS.md and steering inclusion modes: [[wiki/agent-context/subtopics/context-files/sources/openai-codex-agents-md-docs]], [[wiki/agent-context/subtopics/context-files/sources/claude-code-memory-docs]], [[wiki/agent-context/subtopics/context-files/sources/kiro-steering-docs]].

## Direct File vs Pointer File

| Pattern | Kiro | Codex | Claude Code | Assessment |
|---|---|---|---|---|
| Native canonical `AGENTS.md` | Always included, but no Kiro inclusion modes | Best native path | Not read directly | Best baseline for cross-platform portability |
| `CLAUDE.md` imports `@AGENTS.md` | Not relevant | Not needed | Native documented import | Best Claude wrapper |
| `.kiro/steering/*.md` duplicates AGENTS.md content | Native Kiro routing | Invisible unless configured as fallback or manually read | Invisible unless imported/read | High drift risk |
| `.kiro/steering/*.md` says "read AGENTS.md" | Kiro may comply, but this is weaker than native inclusion or file reference | Invisible | Invisible | Useful only as a Kiro prompt-level router |
| `.kiro/steering/*.md` with `#\[\[file:AGENTS.md\]\]` | Native Kiro file reference | Invisible | Invisible | Strongest Kiro pointer form when Kiro routing is needed |
| Separate full `AGENTS.md`, `CLAUDE.md`, `.kiro/steering` copies | All tools see native files | All tools see native files | All tools see native files | Worst maintenance profile because smells and contradictions compound |

The difference between a pointer and an import matters. Claude's `@AGENTS.md` import is documented as expansion into context at launch, while a plain sentence that says "read AGENTS.md" merely asks the model to take an action. Kiro's `#\[\[file:AGENTS.md\]\]` file-reference syntax is closer to a native file reference than a prose instruction, but Kiro's AGENTS.md support may be simpler when the guidance should always load: [[wiki/agent-context/subtopics/context-files/sources/claude-code-memory-docs]], [[wiki/agent-context/subtopics/context-files/sources/kiro-steering-docs]].

## Recommended Repository Layout

```text
AGENTS.md                  # canonical, concise, cross-agent baseline
CLAUDE.md                  # @AGENTS.md plus Claude-only notes, if any
.kiro/steering/
  product.md               # Kiro-only, inclusion: always, thin or domain-specific
  api.md                   # Kiro-only, inclusion: fileMatch or auto
  deep-workflow.md         # Kiro-only, inclusion: manual
.claude/rules/
  api.md                   # Claude path-scoped equivalent only when needed
```

For a small project, the minimum viable version is just `AGENTS.md` plus `CLAUDE.md` containing `@AGENTS.md`. Add Kiro steering only when Kiro's conditional inclusion modes are materially useful, and keep Kiro steering as a routing layer rather than a second canonical copy: [[wiki/agent-context/subtopics/context-files/sources/openai-codex-agents-md-docs]], [[wiki/agent-context/subtopics/context-files/sources/claude-code-memory-docs]], [[wiki/agent-context/subtopics/context-files/sources/kiro-steering-docs]].

## Capability Matrix

| Capability | Codex | Claude Code | Kiro |
|---|---|---|---|
| Canonical file | `AGENTS.md` | `CLAUDE.md` | `.kiro/steering/*.md` or `AGENTS.md` |
| Reads AGENTS.md directly | Yes | No | Yes |
| Native import/pointer | Configurable fallback filenames, not import expansion | `@path` imports, recursive to four hops | `#\[\[file:...\]\]` file references |
| Path or file conditionality | Directory hierarchy and overrides | `.claude/rules/` with `paths` | `fileMatchPattern` |
| Semantic auto-inclusion | Not documented for AGENTS.md | Skills/rules distinction, not AGENTS.md semantic routing | `inclusion: auto` with `name` and `description` |
| Manual inclusion | Ask/read files or commands | Skills/manual prompting | `inclusion: manual` with `#file` or slash command |
| Byte/size guidance | 32 KiB default combined project-doc cap | Target under 200 lines per CLAUDE.md | Focused files; no AGENTS.md inclusion modes |

This matrix records Codex, Claude Code, and Kiro loading semantics as documented mid-2026 and is the most rot-prone content on this page — re-verify against current vendor docs before relying on it.

## Effectiveness Rationale

The empirical evidence does not say "more persistent context is better." ETH Zurich found that LLM-generated context files reduced success in most tested settings and increased inference cost by 20-23%, while human-curated files helped only modestly and should focus on minimal, non-inferable requirements: [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]].

The AGENTS.md efficiency study adds a nuance: in pull-request tasks, AGENTS.md was associated with 28.64% lower median runtime and 16.58% lower output-token consumption, suggesting that concise guidance can reduce downstream wandering even if it costs startup tokens: [[wiki/agent-context/subtopics/context-files/sources/agents-md-efficiency]].

The configuration-smells study explains why duplicated cross-tool manifests are risky: Lint Leakage, Context Bloat, Skill Leakage, and Conflicting Instructions are already widespread in AGENTS.md and CLAUDE.md files, with Context Bloat affecting 42% of studied files and Conflicting Instructions co-occurring with other smells: [[wiki/agent-context/subtopics/context-files/sources/configuration-smells-agents-md]].

Claude manifest mining shows that real Claude manifests already contain commands, technical notes, and high-level architecture, which overlaps heavily with AGENTS.md content and increases the case for canonicalization rather than duplication: [[wiki/agent-context/subtopics/context-files/sources/claude-code-agentic-manifests]].

## Implementation Rules

1. Put only durable, non-inferable, cross-agent facts in `AGENTS.md`: commands, constraints, non-standard tools, architectural "gotchas," and review/test expectations: [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]], [[wiki/agent-context/subtopics/context-files/sources/augment-how-to-build-agents-md]].
2. Make `CLAUDE.md` a native import wrapper: `@AGENTS.md`, followed only by Claude-specific behavior that should not affect other tools: [[wiki/agent-context/subtopics/context-files/sources/claude-code-memory-docs]].
3. Use Kiro steering for conditional routing, not duplication. Prefer `fileMatch`, `manual`, or `auto` when the content is too specific or too large to belong in always-on AGENTS.md: [[wiki/agent-context/subtopics/context-files/sources/kiro-steering-docs]].
4. When Kiro steering needs canonical content, prefer a native file reference such as `#\[\[file:AGENTS.md\]\]` over prose that merely asks Kiro to read another file: [[wiki/agent-context/subtopics/context-files/sources/kiro-steering-docs]].
5. Do not rely on Codex to read `.kiro/steering/` or `CLAUDE.md` unless `project_doc_fallback_filenames` is explicitly configured; Codex's default path is AGENTS.md and AGENTS.override.md: [[wiki/agent-context/subtopics/context-files/sources/openai-codex-agents-md-docs]].
6. Treat every duplicate agent manifest as a future contradiction unless a test or lint process proves it is generated from the canonical source: [[wiki/agent-context/subtopics/context-files/sources/configuration-smells-agents-md]].

## Open Questions

- Kiro documents AGENTS.md as always included, but the available docs do not quantify whether a steering file that references AGENTS.md behaves identically to native AGENTS.md inclusion in long sessions: [[wiki/agent-context/subtopics/context-files/sources/kiro-steering-docs]].
- The available empirical studies evaluate AGENTS.md/CLAUDE.md broadly, not Kiro steering indirection specifically: [[wiki/agent-context/subtopics/context-files/sources/eth-zurich-context-files-agent-performance]], [[wiki/agent-context/subtopics/context-files/sources/agents-md-efficiency]].
- Cross-agent wrappers should be evaluated with task-level metrics: task success, elapsed time, input tokens, output tokens, number of tool calls, whether required instructions were followed, and whether irrelevant instructions were used.

## Proposed Evaluation Harness

Test four configurations across the same repository tasks:

| Condition | Files |
|---|---|
| Baseline | No persistent agent manifest |
| Canonical | `AGENTS.md` only, plus Claude `@AGENTS.md` wrapper |
| Kiro pointer | `.kiro/steering/portable.md` with `#\[\[file:AGENTS.md\]\]` |
| Duplicated native | Full `AGENTS.md`, `CLAUDE.md`, and Kiro steering copies |

Run each condition on Kiro, Codex, and Claude Code where possible. Score not only completion, but instruction adherence and context cost. The hypothesis is that canonical plus native wrappers will beat duplicated native copies on maintenance and contradiction risk, while Kiro's direct AGENTS.md vs file-reference steering difference will mainly show up in conditionality and context budget rather than raw instruction comprehension.

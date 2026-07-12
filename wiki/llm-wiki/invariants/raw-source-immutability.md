---
title: Raw Source Immutability
type: invariant
description: Files under raw/ are never edited in place — fidelity to the original is what makes re-capture audits and upstream change detection possible.
sources:
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
related:
  - "[[wiki/llm-wiki/constructs/three-layer-architecture]]"
  - "[[wiki/llm-wiki/constructs/source-isolation]]"
  - "[[wiki/llm-wiki/designs/evidence-tier-schema]]"
tags: [llm-wiki, provenance, curation, knowledge-management]
created: 2026-07-08
timestamp: 2026-07-08T03:00:00Z
enforcement: convention
status: stable
---

# Raw Source Immutability

## Statement

Files in `raw/` are never edited in place. New raw files may be added during ingest; existing ones are treated as read-only originals. Incidental non-source assets that serve neither of `raw/`'s purposes (e.g. browser-save scripts and styles) may be pruned, but genuine source content is never altered.

## Scope

Applies to every file under `raw/` — articles, papers, PDFs and their text extractions, chat transcripts, repo snapshots, datasets. It governs the boundary between the immutable source layer and the agent-owned `wiki/` layer of the [[wiki/llm-wiki/constructs/three-layer-architecture]]. It does **not** restrict `wiki/`, which agents own and rewrite freely.

Out of scope: correcting a genuinely corrupt capture (wrong file saved, truncated download) is a re-capture, not an in-place edit — replace the file wholesale and note it, rather than hand-patching prose.

## Rationale

`raw/` exists for exactly two purposes, and both depend on the bytes matching the original:

1. **Re-capture audits** — regenerating or checking a source-capture page against its original requires the original to be unchanged. If `raw/` drifts, the audit compares against a moved target.
2. **Upstream change detection** — `raw/` files are copies of upstream sources; detecting that an upstream source changed requires a faithful baseline to diff against. Editing the baseline destroys the signal.

Immutability is also what lets [[wiki/llm-wiki/constructs/source-isolation]] hold: a source-capture is regenerable from its raw source only if that source is stable, and `evidence` tiers assigned at ingest ([[wiki/llm-wiki/designs/evidence-tier-schema]]) stay meaningful only if the thing they rate doesn't shift underneath them.

## Enforcement

`convention` — the operating rule is canonical in `AGENTS.md` (Directory Contract), `schema/ingest.md` (Key Rules), and `schema/structure.md`; this page does not restate that rule, it records the standing constraint behind it — the scope boundaries, violation costs, and removal analysis the canonical one-liners don't carry. Not yet mechanically checked: `scripts/lint.py` does not diff `raw/` against git history. A future deterministic check could flag modifications (as opposed to additions) to tracked `raw/` files in a diff; until then it relies on agent discipline and human review.

## Violation Modes

- Silent prose edits to a captured article make its source-capture no longer regenerable and quietly invalidate any future upstream-change diff.
- Hand-fixing a PDF text extraction couples the "original" to one agent's interpretation, defeating the point of keeping the raw extraction separate from the wiki summary.
- Pruning genuine source content (not just incidental assets) under the "incidental assets may be pruned" allowance erodes provenance; when unsure whether an asset is incidental, keep it.

## Removal Path

**Origin: decided.** The rule was authored into the vault's operating contract (`AGENTS.md` Directory Contract) at creation, before `decision` pages existed, so there is no establishing decision page to invert — this section carries the analysis instead.

**What removal would require:** abandoning at least one of `raw/`'s two purposes. If re-capture audits were dropped (e.g. captures declared authoritative and raw copies disposable) and upstream change detection moved elsewhere (e.g. content hashes or upstream URLs plus fetch-on-demand), in-place editing would stop destroying anything the wiki depends on. Both substitutes weaken provenance: hashes detect drift but can't show *what* changed, and fetch-on-demand fails for dead links and paywalled or since-edited sources.

**Effects of removal:** source-captures stop being regenerable, `evidence` tiers rate a moving target, and [[wiki/llm-wiki/constructs/source-isolation]] loses its stability premise — this invariant is load-bearing for the whole provenance layer, so treat it as effectively permanent while the [[wiki/llm-wiki/constructs/three-layer-architecture]] stands.

## Exceptions

Two bounded carve-outs, both already stated in the canonical rule:

- **Incidental non-source assets** (browser-save scripts, styles) serving neither of `raw/`'s purposes may be pruned; when unsure whether an asset is incidental, keep it.
- **Corrupt-capture replacement**: a wrong or truncated capture is fixed by wholesale re-capture with a note, never by hand-editing prose — a replacement, not an edit.

## Related Artifacts

- [[wiki/llm-wiki/constructs/three-layer-architecture]] — the raw/wiki/schema separation this invariant guards
- [[wiki/llm-wiki/constructs/source-isolation]] — the downstream invariant that depends on stable raw sources
- [[wiki/llm-wiki/designs/evidence-tier-schema]] — evidence tiers assume the rated source doesn't change after ingest

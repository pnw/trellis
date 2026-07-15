---
title: "Owner Brain Dump: Rethinking the Design Type as a Directory"
type: source-capture
description: "Owner observation that design pages mix a target specification with transient phased scoping, and the corrective realization that a design is a directory — a standard-named target spec plus phase documents (phase-1, later) and split-out completion follow-ups."
sources:
  - "[[raw/chats/design-as-directory-brain-dump.md]]"
related:
  - "[[wiki/llm-wiki/decisions/designs-die-into-decisions]]"
  - "[[wiki/llm-wiki/decisions/staged-ingest-and-instigator-tiers]]"
tags: [llm-wiki, schema-design, design-docs, knowledge-management]
created: 2026-07-14
timestamp: 2026-07-14T12:00:00Z
evidence: expert-analysis
---

# Owner Brain Dump: Rethinking the Design Type as a Directory

## Source Identity

- Raw source: [[raw/chats/design-as-directory-brain-dump.md]]
- Source type: speech-to-text owner brain dump, single message, verbatim (dictation artifacts preserved)
- Author: the wiki owner
- Published/retrieved: 2026-07-14
- Scope: a self-observed failure mode in how the owner uses the `design` page type, and a proposed structural correction

## Core Contribution

The dump names a mixing-of-concerns failure in single-file design documents — target specification entangled with phased implementation scoping — and contributes the corrective realization that **in the wiki a design is not a single file but a directory**: a standard-named target spec (`design.md`) plus supporting documents that speak to the phasing of implementation against it (`phases/phase-1.md`, `phases/later.md`), with completion follow-ups split out as a separate non-phased concern.

## Key Claims

- The owner's design documents in practice combine a target specification with phased scoping; the target future state "gets really complicated, especially for a mature software product," while the phased scoping usually limits itself to the first phase.
- Phase scoping is where implementation legitimately gets specific — especially when modifying an existing system and designing "within the boundaries of existing abstractions or interfaces that should not be touched as part of the design."
- The failure: the design page stops being a standalone requirements document and instead tries to be that *plus* a transient implementation plan. The objection is not technical detail (which a design may need) but sequencing content — "do this first," what will have been implemented at the end of the first step, and the follow-up items then necessary.
- Follow-up items are of two kinds: follow-ups to implement other aspects of the design (deferred design scope), and follow-ups to the completion of the design itself — "things that are out of scope of the design, but which the design subsequently requires of the rest of the system." The owner concluded mid-dump that these two concerns should themselves be split, the latter captured either in the design or as a separate non-phased document.
- Proposed shape: a design directory containing a standard-named target spec ("target spec or design.MD") and a nested `phases/` subdirectory with at least a `phase-1.md` capturing the first implementation scope — "often the most necessary to understand in design iterations" — plus a `later.md` grab bag.
- `later.md` is deliberately not a `phase-2`: at the current point in the process it is "not required or necessary to identify the scope of subsequent phases or roadmap all of that out" — though nothing should prevent deliberate phasing if desired.
- Unphased designs keep the same pattern: `phase-1.md` simply states that phase 1 implements the design to its fullest. "That obviates any questions about if there are no phased documents because there are no phases or are there no phase documents because we forgot."
- Standard file names are the point of the directory: any consumer "knows where to look to find the information it's looking for," without restricting the directory to only those files.

## Evidence and Results

No systematic data; the dump is grounded in the owner's firsthand experience authoring and consuming design documents in this method's wikis and in mature-software design work. No corpus measurements were taken in the dump itself.

## Limitations and Caveats

- Single-operator experience report; no downstream-instance or third-party corroboration.
- The failure mode is asserted from recall, not demonstrated against specific design pages in this or a downstream wiki.
- The proposal was thought through mid-dictation ("on second thought"), so the follow-ups placement question is left explicitly open in the source.

## Reliability Notes

`expert-analysis`: a practitioner experience report with argumentation and no systematic data. Unlike this wiki's condensed chat captures, the raw file is the owner's own words verbatim (speech-to-text), so no model interpretation precedes the provenance boundary; the tier reflects source type, not fidelity concerns.

## Contribution Routing

- [[wiki/llm-wiki/decisions/dossier-phasing-and-types]] — where this dump's phasing model landed, reconciled onto the design surface (the dump was worked in two parallel sessions; the other produced [[wiki/llm-wiki/decisions/separate-design-surface]])
- `schema/design/dossier.md` — the normative landing place for the phasing skeleton
- Candidate later input to any note-craft/page-granularity topic (page-vs-directory artifact granularity)

## Extraction Notes

Speech-to-text artifacts in the raw file, read in context: "faced scoping" → "phased scoping"; "The target specter finds the future state" → "the target spec defines the future state"; "capturing them first implementation scope" → "capturing the first implementation scope"; "No thinking about a situation" → "Now thinking about a situation"; "express in phase. One that phase one" → "express in phase-1 that phase one". The leading "- [ ]" is a dictation-workflow checkbox, not content.

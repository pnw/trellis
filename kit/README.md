# Trellis Kit

This directory contains optional ways to apply the Trellis specifications. It
is not part of Wiki or Design conformance.

| Directory | Purpose |
|---|---|
| `skills/` | Agent workflows for scaffolding, ingest, query, lint, and design creation. |
| `templates/` | Starting files copied into a project and then owned by that project. |
| `adapters/` | Thin tool-specific loading wrappers. |
| `scripts/` | Optional deterministic validation and maintenance tools. |

The normative documents are [`../specs/wiki.md`](../specs/wiki.md) and
[`../specs/design.md`](../specs/design.md). When the kit and a specification
disagree, the specification wins.

Skills and templates use the draft 0.1 contracts in this repository. A release
of the kit should pin the corresponding immutable Wiki and Design tag URLs.

## Conditional Specification Loading

`templates/repository/AGENTS.md` is a thin task router and
`templates/repository/trellis.yaml` declares installed artifact classes and
their versioned specification URLs. Keep only installed mappings in the
manifest. Do not place complete specifications in always-loaded repository
guidance.

Authoring and semantic-review skills read the selected specification once while
its full text remains in active context, reloading after context compaction when
semantic work continues. Ordinary Wiki queries and deterministic lint runs
operate without it. Load both specifications only for work that semantically
spans both artifact classes. Invoke a skill explicitly, such as
`$create-design-dossier`, when automatic task routing would be ambiguous.

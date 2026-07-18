# Trellis Agent Routing

This repository may contain Trellis Wiki artifacts, Trellis Design artifacts,
or both. `trellis.yaml`, when present, declares the installed artifact classes
and their selected specification versions.

## Specification Loading

- Before creating, changing, repairing, or semantically reviewing a Trellis
  Wiki artifact, ensure the selected Wiki specification is in active context,
  normally from `trellis.wiki.specification`.
- Before creating, changing, repairing, or semantically reviewing a Trellis
  Design dossier, ensure the selected Design specification is in active
  context, normally from `trellis.design.specification`.
- Do not load a specification for ordinary artifact queries, navigation, or a
  deterministic lint run.
- Load both specifications only when the task semantically changes or reviews
  both artifact classes.
- Do not reload a specification while its full text remains in active context.
  If context compaction summarizes or drops it, reload it before further
  semantic artifact work.
- Words such as "wiki" or "design" do not trigger loading unless the work
  concerns the corresponding Trellis artifact.

## Artifact Entry Points

- Read a Wiki's `index.md` and `overview.md` before broad Wiki work.
- Read a dossier's `design.md` before working on its subsidiary documents.

## Agent Commentary

A heading whose text is exactly `TODO(agent)` is transient human commentary.
Read its containing section and nearby context, then act, ask, or leave it
unchanged. If acted on, remove the whole TODO section and report the outcome.

## Project-Specific Rules

<!-- Add commands, boundaries, and non-inferable local constraints here. -->

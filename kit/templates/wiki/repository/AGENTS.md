# Wiki Agent Guide

This repository contains a Trellis Wiki conforming to the version declared in
`wiki/index.md`. The standalone specification is the normative artifact
contract; project-specific instructions below govern how agents apply it here.

## Purpose and Scope

Read `wiki/overview.md` before changing wiki content. Keep content within its
single governing goal and stated scope.

## Core Rules

- Read `wiki/index.md` before broad searches.
- Preserve every acquired source under `wiki/raw/`; never replace a snapshot.
- Keep source captures isolated to one source.
- Use the correct topic/type directory and frontmatter contract.
- Use relative Markdown links.
- Update timestamps and the root index after meaningful changes.
- Use `evidence` on source captures and derived `confidence` only on constructs
  and entities.
- Link every factual claim, data point, and attributed finding to its support.
- Count sources by independence, not file or repository count; wikis maintained
  by the same owner and agents count as one source.
- Create source captures during ingest. Create interpretive pages only when the
  wiki will reason with their content again. Create decisions and invariants
  only at user request or ratification.
- Adjudicate contradictions in synthetic pages, never inside a source capture.

## Agent Commentary

A heading whose text is exactly `TODO(agent)` is transient human commentary.
Read its containing section and nearby context, then act, ask, or leave it
unchanged. If acted on, remove the whole TODO section and report the outcome.

## Optional Kit

<!-- Record installed Trellis skills, scripts, or tool adapters here. -->

## Project-Specific Rules

<!-- Add commands, boundaries, and non-inferable local constraints. -->

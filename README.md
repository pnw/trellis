# Trellis

Trellis publishes two independent, agent- and human-readable specifications:

- [Trellis Wiki](specs/wiki.md) — a typed, provenance-preserving Wiki format
  conforming to Open Knowledge Format (OKF).
- [Trellis Design](specs/design.md) — a progressive dossier format for target
  specifications with optional implementation phases, prerequisites,
  obligations, alternatives, and supporting assets.

Each specification is a standalone document. An agent can create a conforming
artifact from the raw URL without cloning this repository or installing tools.

The specifications are currently 0.1 drafts. Released versions use independent
immutable-by-policy tags:

```text
https://raw.githubusercontent.com/pnw/trellis/wiki-v0.1.0/specs/wiki.md
https://raw.githubusercontent.com/pnw/trellis/design-v0.1.0/specs/design.md
```

Until those tags are released, use the files in this repository rather than
assuming the example tag URLs exist.

## Repository Layout

```text
specs/
  wiki.md                       # Normative Wiki specification
  design.md                     # Normative Design specification
kit/
  skills/                       # Optional agent workflows
  templates/                    # Optional scaffold files
  adapters/                     # Optional tool-specific loading wrappers
  scripts/                      # Optional validators and helpers
```

Only `specs/` is normative. The [optional kit](kit/README.md) applies the specs
but does not define conformance.

The existing root `wiki/`, `raw/`, and `designs/` directories are legacy lab
content excluded from the 0.1 framework. Their migration is intentionally a
separate change; consumers must not treat them as specification examples.

## Use

To create a wiki, give an agent the raw Wiki specification and a purpose:

> Read this specification and create a Trellis Wiki for this project:
> `<versioned raw wiki URL>`

To create a design:

> Read this specification and create a Trellis Design for this change:
> `<versioned raw design URL>`

For scaffolding, ingest, query, lint, or design-authoring workflows, install or
copy only the relevant components from `kit/`.

## Versioning

Wiki and Design evolve independently with semantic versions:

- `wiki-v<major>.<minor>.<patch>`
- `design-v<major>.<minor>.<patch>`

Release tags are never moved or deleted. A patch clarifies without changing
conformance, a minor release adds backward-compatible capabilities, and a major
release changes required structure or semantics.

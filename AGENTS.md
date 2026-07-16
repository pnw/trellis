# Trellis Maintainer Contract

Trellis is the upstream repository for two independent specifications and an
optional application kit.

## Normative Boundary

- `specs/wiki.md` is the complete Trellis Wiki specification.
- `specs/design.md` is the complete Trellis Design specification.
- The specs are independently versioned and MUST NOT normatively depend on one another or on repository-local rationale.
- A released spec must be usable from its version-tagged raw URL alone.
- `kit/` is non-normative. Skills, templates, adapters, and scripts consume the
  specs and must not redefine them. When the kit disagrees with a spec, the spec
  wins.

## Change Rules

- Specification changes require user agreement.
- Keep the documents declarative, self-contained, concise, and explicit about
  motivation, goals, non-goals, terminology, structure, document contracts,
  conformance, examples, and versioning.
- Use standard relative Markdown links.
- Apply semantic versioning independently to Wiki and Design. Do not move or
  delete a released version tag.
- Update kit consumers and validation fixtures when a specification contract
  changes, but do not make the specification depend on them.
- Optional features belong in `kit/`, not in the minimum conforming artifact.

## Validation

- Run `python3 kit/scripts/lint.py wiki <wiki-path>` for deterministic Wiki
  checks.
- Run `python3 kit/scripts/lint.py design <dossier-path>` for deterministic
  Design checks.
- Validate skill packages with the skill-creator validator when they change.
- Review the judgment rules that deterministic scripts cannot prove.

## Legacy Lab Boundary

The existing root `wiki/`, `raw/`, and `designs/` directories are legacy lab
content awaiting a separate migration. They are not part of the 0.1 framework,
must not be used as normative examples, and must not be edited unless the user
explicitly requests that follow-up.

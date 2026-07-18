---
name: create-design-dossier
description: Create or extend an OKF-conformant Trellis Design dossier. Use when a user asks to design a system, feature, protocol, workflow, or change; compare design alternatives; or add implementation phases after approving the design work.
---

# Create a Design Dossier

1. Before semantic dossier work, ensure the complete Design specification
   selected by the project is in active context. Resolve it from an explicit
   user selection, `trellis.design.specification` in
   `trellis.yaml`, or, in this repository, `../../../specs/design.md`. Prefer an
   immutable version-tagged URL. Do not reload while its full text remains in
   active context; reload after compaction before further semantic work.
2. Proceed only when the user requested or ratified design creation. Establish
   the target's purpose, system boundary, core model, components, architecture,
   workflow or data flow, constraints and invariants, behavioral statements or
   acceptance criteria, decisions, evidence and rationale, and open design
   questions. Adapt, combine, or reorder headings when the content remains
   clear and complete.
3. Create only `<slug>/design.md` by default. Use
   `../../templates/design/design.md` as an editable starting point. If the
   project uses the optional routing kit, add or update only the Design mapping
   in `trellis.yaml`.
4. Add a progressive enhancement only when the design needs it:
   - `phases/` requires numbered phases plus `later.md`, covering the target;
   - `prerequisites.md` records gates on the whole design or named phases;
   - `obligations.md` records consequences outside the target boundary;
   - `alternatives/` requires one or more candidates for one shared question
     and scope plus `evaluation.md`; evaluate every candidate against its
     authoritative `design.md` baseline, even when there is only one.
5. Keep `design.md` authoritative. Phases scope it; alternatives do not override
   it; evaluation may state that judgment remains unresolved. Make each
   alternative self-contained, whether it changes the whole target or a bounded
   part, and include its Scope, Prerequisites, Obligations, and Downstream
   Impacts. Do not put epistemic grading fields on dossier documents.
6. Use relative Markdown links, treat `design.md` as the only stable external
   link target, put every supporting file under `assets/`, and update timestamps
   after meaningful changes.
7. Run `python3 ../../scripts/lint.py design <path-to-dossier>` when available.
8. Present the target and any enhancements for review. Do not begin
   implementation unless the user also requested it. At a terminal state,
   preserve the entire dossier as history.

#!/usr/bin/env python3
"""Optional deterministic validator for Trellis Wiki and Design 0.1 drafts.

Usage:
    python3 kit/scripts/lint.py wiki path/to/wiki
    python3 kit/scripts/lint.py design path/to/design-dossier

Requires PyYAML. Judgment checks remain agent or human work.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path
from urllib.parse import unquote

try:
    import yaml
except ImportError:
    print("error: PyYAML is required (`python3 -m pip install pyyaml`)", file=sys.stderr)
    raise SystemExit(2)


FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.S)
H2 = re.compile(r"^##\s+(.+?)\s*$", re.M)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
WIKILINK = re.compile(r"\[\[[^\]]+\]\]")
EXTERNAL_SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")

COMMON_TOPIC_FIELDS = {"title", "type", "description", "sources", "timestamp", "tags"}
TOPIC_TYPES = {
    "source-capture": "sources",
    "construct": "constructs",
    "entity": "entities",
    "synthesis": "syntheses",
    "assessment": "assessments",
    "comparison": "comparisons",
    "decision": "decisions",
    "invariant": "invariants",
}
EVIDENCE = {
    "empirical-primary",
    "empirical-secondary",
    "official-docs",
    "expert-analysis",
    "vendor-claim",
    "llm-generated",
}
NOVELTY = {"established", "emerging", "exploratory", "coined"}
CONFIDENCE = {"high", "medium", "low"}
INTERPRETIVE_STATUS = {"draft", "stable", "deprecated"}
DECISION_STATUS = {"proposed", "accepted", "superseded"}
INVARIANT_STATUS = {"proposed", "active", "retired"}
DESIGN_STATUS = {"draft", "active", "implemented", "superseded", "abandoned"}
PHASE_STATUS = {"pending", "in-progress", "complete"}

SOURCE_HEADINGS = [
    "Source Identity",
    "Core Contribution",
    "Key Claims",
    "Evidence and Results",
    "Methodology",
    "Limitations and Caveats",
    "Reliability Notes",
    "Important References",
    "Contribution Routing",
    "Extraction Notes",
]
DECISION_HEADINGS = [
    "Context",
    "Decision",
    "Alternatives Considered",
    "Consequences",
    "Invariants Established",
]
INVARIANT_HEADINGS = [
    "Statement",
    "Scope",
    "Rationale",
    "Enforcement",
    "Violation Modes",
    "Removal Path",
    "Exceptions",
]
OVERVIEW_HEADINGS = ["Purpose", "Scope", "Navigation", "Current Understanding"]
DESIGN_HEADINGS = [
    "Motivation",
    "Goals",
    "Non-goals",
    "Terminology",
    "Design",
    "Constraints",
    "Open Questions",
]
PHASE_HEADINGS = [
    "Scope",
    "Deliverables",
    "Completion Criteria",
    "Dependencies and Constraints",
    "Design Coverage",
]
ALTERNATIVE_HEADINGS = ["Summary", "Design", "Strengths", "Costs and Risks", "Consequences"]
EVALUATION_HEADINGS = [
    "Decision Question",
    "Criteria",
    "Comparison",
    "Judgment",
    "Unresolved Questions",
]


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, path: Path | str, message: str) -> None:
        self.errors.append(f"{path}: {message}")

    def warning(self, path: Path | str, message: str) -> None:
        self.warnings.append(f"{path}: {message}")

    def emit(self) -> int:
        for item in self.errors:
            print(f"ERROR   {item}")
        for item in self.warnings:
            print(f"WARNING {item}")
        print(f"lint: {len(self.errors)} errors, {len(self.warnings)} warnings")
        return 1 if self.errors else 0


def load_document(path: Path, report: Report) -> tuple[dict, str] | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        report.error(path, f"cannot read UTF-8 Markdown ({exc})")
        return None
    match = FRONTMATTER.match(text)
    if not match:
        report.error(path, "missing YAML frontmatter")
        return None
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        report.error(path, f"invalid YAML frontmatter ({exc})")
        return None
    if not isinstance(data, dict):
        report.error(path, "frontmatter must be a mapping")
        return None
    return data, text[match.end() :]


def check_fields(path: Path, data: dict, required: set[str], report: Report) -> None:
    for field in sorted(required):
        if field not in data or data[field] is None or data[field] == "":
            report.error(path, f"missing required field `{field}`")


def valid_timestamp(value: object) -> bool:
    if isinstance(value, datetime):
        return value.tzinfo is not None
    if isinstance(value, date):
        return False
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def check_timestamp(path: Path, data: dict, report: Report) -> None:
    if "timestamp" in data and not valid_timestamp(data["timestamp"]):
        report.error(path, "`timestamp` must be an ISO 8601 datetime with timezone")


def check_exact_headings(path: Path, body: str, expected: list[str], report: Report) -> None:
    actual = H2.findall(body)
    if actual != expected:
        report.error(path, f"second-level headings must be exactly {expected}; found {actual}")


def clean_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " \"" in target:
        target = target.split(" \"", 1)[0]
    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target)


def check_links(path: Path, body: str, report: Report) -> set[Path]:
    resolved: set[Path] = set()
    if WIKILINK.search(body):
        report.error(path, "custom wikilinks are not allowed; use relative Markdown links")
    for raw in MARKDOWN_LINK.findall(body):
        target = clean_link_target(raw)
        if not target or target.startswith("#") or EXTERNAL_SCHEME.match(target):
            continue
        destination = (path.parent / target).resolve()
        if not destination.exists():
            report.error(path, f"broken relative link `{raw}`")
        else:
            resolved.add(destination)
    return resolved


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def validate_wiki(root: Path) -> int:
    report = Report()
    root = root.resolve()
    if not root.is_dir():
        report.error(root, "wiki directory does not exist")
        return report.emit()

    for required in (root / "index.md", root / "overview.md", root / "raw"):
        if not required.exists():
            report.error(relative(required, root), "required bundle artifact is missing")

    typed_pages: set[Path] = set()
    index_targets: set[Path] = set()

    index_path = root / "index.md"
    if index_path.exists():
        loaded = load_document(index_path, report)
        if loaded:
            data, body = loaded
            if data.get("okf_version") != "0.1":
                report.error("index.md", "must declare `okf_version: \"0.1\"`")
            if str(data.get("trellis_wiki_version")) != "0.1.0":
                report.error("index.md", "must declare `trellis_wiki_version: \"0.1.0\"`")
            index_targets = check_links(index_path, body, report)

    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if path == index_path:
            continue
        if path.name == "index.md":
            text = path.read_text(encoding="utf-8")
            if FRONTMATTER.match(text):
                report.error(rel, "only the root index may contain frontmatter")
            check_links(path, text, report)
            continue
        if path.name == "log.md":
            text = path.read_text(encoding="utf-8")
            if FRONTMATTER.match(text):
                report.error(rel, "log.md must not contain frontmatter")
            check_links(path, text, report)
            continue

        loaded = load_document(path, report)
        if not loaded:
            continue
        data, body = loaded
        ptype = data.get("type")
        if not isinstance(ptype, str) or not ptype:
            report.error(rel, "missing non-empty `type`")
            continue
        check_timestamp(rel, data, report)

        if root / "raw" in path.parents:
            check_fields(rel, data, {"type", "resource", "timestamp"}, report)
            if ptype != "raw-source":
                report.error(rel, "Markdown under raw/ must use `type: raw-source`")
            continue

        typed_pages.add(path.resolve())
        if path == root / "overview.md":
            check_fields(rel, data, {"title", "type", "description", "sources", "timestamp"}, report)
            if ptype != "overview":
                report.error(rel, "overview.md must use `type: overview`")
            if not isinstance(data.get("sources"), list):
                report.error(rel, "`sources` must be a YAML list")
            check_exact_headings(rel, body, OVERVIEW_HEADINGS, report)
            check_links(path, body, report)
            continue

        check_fields(rel, data, COMMON_TOPIC_FIELDS, report)
        if not isinstance(data.get("sources"), list):
            report.error(rel, "`sources` must be a YAML list")
        if not isinstance(data.get("tags"), list):
            report.error(rel, "`tags` must be a YAML list")
        if "related" in data and not isinstance(data.get("related"), list):
            report.error(rel, "`related` must be a YAML list")

        expected_folder = TOPIC_TYPES.get(ptype)
        if expected_folder:
            if path.parent.name != expected_folder:
                report.error(rel, f"type `{ptype}` must live in `{expected_folder}/`")
        elif not ptype.startswith("x-"):
            report.error(rel, f"unknown Trellis type `{ptype}`")

        if ptype == "source-capture":
            if data.get("evidence") not in EVIDENCE:
                report.error(rel, "missing or invalid `evidence`")
            for forbidden in ("confidence", "novelty", "related", "status"):
                if forbidden in data:
                    report.error(rel, f"`{forbidden}` is not allowed on a source capture")
            check_exact_headings(rel, body, SOURCE_HEADINGS, report)
            raw_sources = []
            for source in data.get("sources", []):
                if isinstance(source, str) and not EXTERNAL_SCHEME.match(source):
                    target = (path.parent / source).resolve()
                    if root / "raw" in target.parents and target.exists():
                        raw_sources.append(target)
            if not raw_sources:
                report.error(rel, "source capture must cite an existing file under raw/")
        elif ptype in {"construct", "entity"}:
            check_fields(rel, data, {"novelty", "confidence", "status", "related"}, report)
            if data.get("novelty") not in NOVELTY:
                report.error(rel, "missing or invalid `novelty`")
            if data.get("confidence") not in CONFIDENCE:
                report.error(rel, "missing or invalid `confidence`")
            if data.get("status") not in INTERPRETIVE_STATUS:
                report.error(rel, "missing or invalid interpretive `status`")
        elif ptype in {"synthesis", "assessment", "comparison"}:
            check_fields(rel, data, {"status", "related"}, report)
            if data.get("status") not in INTERPRETIVE_STATUS:
                report.error(rel, "missing or invalid interpretive `status`")
            if "confidence" in data:
                report.error(rel, f"`confidence` is not allowed on {ptype}")
        elif ptype == "decision":
            check_fields(rel, data, {"status", "related"}, report)
            if data.get("status") not in DECISION_STATUS:
                report.error(rel, "missing or invalid decision `status`")
            check_exact_headings(rel, body, DECISION_HEADINGS, report)
        elif ptype == "invariant":
            check_fields(rel, data, {"status", "related"}, report)
            if data.get("status") not in INVARIANT_STATUS:
                report.error(rel, "missing or invalid invariant `status`")
            if "enforcement" in data:
                report.error(rel, "invariant enforcement belongs in the body, not frontmatter")
            check_exact_headings(rel, body, INVARIANT_HEADINGS, report)

        check_links(path, body, report)

    missing_from_index = typed_pages - index_targets
    for path in sorted(missing_from_index):
        report.error(relative(path, root), "typed page is missing from the root index")

    return report.emit()


def dossier_slot(path: Path, root: Path) -> str | None:
    rel = path.relative_to(root).as_posix()
    if rel == "design.md":
        return "design"
    if re.fullmatch(r"phases/phase-[1-9][0-9]*\.md", rel):
        return "phase"
    if rel == "phases/later.md":
        return "roadmap"
    if rel == "obligations.md":
        return "obligations"
    if rel == "alternatives/evaluation.md":
        return "evaluation"
    if re.fullmatch(r"alternatives/[^/]+\.md", rel):
        return "alternative"
    return None


def validate_design(root: Path) -> int:
    report = Report()
    root = root.resolve()
    if not root.is_dir():
        report.error(root, "design dossier does not exist")
        return report.emit()
    if not (root / "design.md").exists():
        report.error("design.md", "required target specification is missing")

    phases = root / "phases"
    if phases.exists():
        numbered = sorted(phases.glob("phase-*.md"))
        if not numbered or not (phases / "phase-1.md").exists():
            report.error("phases/", "must contain numbered phases beginning with phase-1.md")
        if not (phases / "later.md").exists():
            report.error("phases/", "must contain later.md")
        report.warning("phases/", "verify numbered phases plus later.md cover the complete design target")

    alternatives = root / "alternatives"
    if alternatives.exists():
        candidates = [p for p in alternatives.glob("*.md") if p.name != "evaluation.md"]
        if len(candidates) < 2:
            report.error("alternatives/", "must contain at least two candidate documents")
        if not (alternatives / "evaluation.md").exists():
            report.error("alternatives/", "must contain evaluation.md")

    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if path.name == "index.md":
            text = path.read_text(encoding="utf-8")
            if FRONTMATTER.match(text):
                report.error(rel, "dossier index.md must not contain frontmatter")
            check_links(path, text, report)
            continue
        loaded = load_document(path, report)
        if not loaded:
            continue
        data, body = loaded
        check_fields(rel, data, {"title", "type", "description", "timestamp"}, report)
        check_timestamp(rel, data, report)
        slot = dossier_slot(path, root)
        ptype = data.get("type")
        if slot:
            if ptype != slot:
                report.error(rel, f"structural position requires `type: {slot}`")
        elif not isinstance(ptype, str) or not ptype.startswith("x-"):
            report.error(rel, "non-standard Markdown assets must use an `x-` extension type")

        if slot == "design":
            check_fields(rel, data, {"status", "trellis_design_version"}, report)
            if data.get("status") not in DESIGN_STATUS:
                report.error(rel, "missing or invalid design `status`")
            if str(data.get("trellis_design_version")) != "0.1.0":
                report.error(rel, "must declare `trellis_design_version: \"0.1.0\"`")
            check_exact_headings(rel, body, DESIGN_HEADINGS, report)
        elif slot == "phase":
            check_fields(rel, data, {"status"}, report)
            if data.get("status") not in PHASE_STATUS:
                report.error(rel, "missing or invalid phase `status`")
            check_exact_headings(rel, body, PHASE_HEADINGS, report)
        elif slot == "roadmap":
            check_exact_headings(rel, body, ["Deferred Scope"], report)
        elif slot == "obligations":
            check_exact_headings(rel, body, ["Obligations"], report)
        elif slot == "alternative":
            check_exact_headings(rel, body, ALTERNATIVE_HEADINGS, report)
        elif slot == "evaluation":
            check_exact_headings(rel, body, EVALUATION_HEADINGS, report)

        check_links(path, body, report)

    return report.emit()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=("wiki", "design"))
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    return validate_wiki(args.path) if args.kind == "wiki" else validate_design(args.path)


if __name__ == "__main__":
    raise SystemExit(main())

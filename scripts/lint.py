#!/usr/bin/env python3
"""Deterministic lint tier for the research wiki (see schema/lint.md).

Checks frontmatter validity, wikilink resolution, epistemic-field placement,
folder/type agreement, confidence ceilings, orphans, and staleness.
Judgment checks (contradictions, circular reporting, isolation violations)
are agent work and out of scope here.

Exit code: 1 if any errors, 0 otherwise (warnings never fail the run).
"""

import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"

TYPES = {"source-capture", "construct", "entity", "synthesis", "design",
         "assessment", "comparison", "decision", "invariant"}
EVIDENCE_TIERS = {"empirical-primary", "empirical-secondary", "official-docs",
                  "expert-analysis", "vendor-claim", "llm-generated"}
EMPIRICAL = {"empirical-primary", "empirical-secondary"}
CONFIDENCE = {"high", "medium", "low"}
ENFORCEMENT = {"automated", "manual", "convention", "external", "unenforced"}
REQUIRED = ["title", "type", "description", "sources", "created", "timestamp"]
NOVELTY_TYPES = {"construct", "design", "entity"}
TYPE_FOLDER = {"source-capture": "sources", "construct": "constructs",
               "entity": "entities", "synthesis": "syntheses",
               "design": "designs", "assessment": "assessments",
               "comparison": "comparisons", "decision": "decisions",
               "invariant": "invariants"}
META_FILES = {WIKI / "index.md", WIKI / "log.md", WIKI / "overview.md", WIKI / "roadmap.md", WIKI / "episodes.md"}
STALE_DAYS = 30

WIKILINK = re.compile(r"\[\[([^\]|#]+)")


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields, sources, in_sources = {}, [], False
    for line in m.group(1).split("\n"):
        if in_sources:
            if line.startswith("  - "):
                sources.append(line[4:].strip().strip('"'))
                continue
            in_sources = False
        kv = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1), kv.group(2).strip().strip('"')
            fields[key] = val
            if key == "sources":
                in_sources = True
    fields["_sources"] = sources
    return fields


def link_resolves(target):
    t = target.strip()
    return (ROOT / t).exists() or (ROOT / (t + ".md")).exists()


def design_dir_of(path):
    """Return the design directory Path when *path* sits inside one
    (…/designs/<slug>/…), else None. Single-file designs (…/designs/<slug>.md)
    are not inside a design directory."""
    dirs = path.relative_to(ROOT).parts[:-1]
    if "designs" in dirs:
        i = len(dirs) - 1 - dirs[::-1].index("designs")
        if i < len(dirs) - 1:
            return ROOT.joinpath(*dirs[: i + 2])
    return None


def main():
    errors, warnings = [], []
    pages = {}  # rel path (no .md) -> frontmatter
    bodies = {}

    for path in sorted(WIKI.rglob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text()
        bodies[rel] = text
        if path in META_FILES:
            continue
        ddir = design_dir_of(path)
        if ddir is not None and path != ddir / "design.md":
            # subsidiary design document (phases/, follow-ups.md, …):
            # an untyped part of the design artifact, not a page
            fm = parse_frontmatter(text)
            if fm and "type" in fm:
                errors.append(f"{rel}: subsidiary design file carries 'type' "
                              f"— only design.md is a typed page")
            continue
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: no frontmatter")
            continue
        fm["_file"] = rel
        # a design directory's page is keyed (and linked) by the directory path
        key = ddir.relative_to(ROOT).as_posix() if ddir is not None else rel[:-3]
        pages[key] = fm

        for field in REQUIRED:
            if field not in fm:
                errors.append(f"{rel}: missing required field '{field}'")

        ptype = fm.get("type")
        if ptype and ptype not in TYPES:
            errors.append(f"{rel}: invalid type '{ptype}'")

        if ptype == "source-capture":
            ev = fm.get("evidence")
            if ev is None:
                errors.append(f"{rel}: source-capture missing 'evidence'")
            elif ev not in EVIDENCE_TIERS:
                errors.append(f"{rel}: invalid evidence tier '{ev}'")
            if "confidence" in fm:
                errors.append(f"{rel}: 'confidence' not allowed on source-capture")
        elif ptype in TYPES:
            if "evidence" in fm:
                errors.append(f"{rel}: 'evidence' only allowed on source-captures")
            conf = fm.get("confidence")
            if conf and conf not in CONFIDENCE:
                errors.append(f"{rel}: invalid confidence '{conf}'")

        if ptype in NOVELTY_TYPES and "novelty" not in fm:
            errors.append(f"{rel}: {ptype} missing 'novelty'")

        if ptype == "invariant":
            enf = fm.get("enforcement")
            if enf is None:
                errors.append(f"{rel}: invariant missing 'enforcement'")
            elif enf not in ENFORCEMENT:
                errors.append(f"{rel}: invalid enforcement '{enf}'")
        elif "enforcement" in fm:
            errors.append(f"{rel}: 'enforcement' only allowed on invariants")

        folder = "designs" if ddir is not None else path.parent.name
        if ptype in TYPE_FOLDER and folder != TYPE_FOLDER[ptype]:
            errors.append(f"{rel}: type '{ptype}' but folder '{folder}/'")
        if folder == "sources" and ptype != "source-capture":
            errors.append(f"{rel}: non-source page inside sources/")

    # design directories must carry the standard skeleton — every standard
    # file is required; empty concerns are stated, never inferred from absence
    for d in sorted(p for p in WIKI.rglob("*")
                    if p.is_dir() and p.parent.name == "designs"):
        drel = d.relative_to(ROOT).as_posix()
        for req in ("design.md", "phases/phase-1.md", "phases/later.md",
                    "follow-ups.md"):
            if not (d / req).exists():
                errors.append(f"{drel}/: design directory missing {req}")

    # broken wikilinks (all wiki pages incl. meta files)
    for rel, text in bodies.items():
        for target in set(WIKILINK.findall(text)):
            if "::" in target:
                continue  # peer-wiki link — checked by following the peer's moves.log, not here
            if not link_resolves(target):
                errors.append(f"{rel}: broken wikilink [[{target}]]")

    # confidence ceilings
    for key, fm in pages.items():
        conf = fm.get("confidence")
        if fm.get("type") == "source-capture" or conf not in CONFIDENCE:
            continue
        caps, domains, llm = [], set(), False
        for s in fm["_sources"]:
            if s.startswith("[["):
                target = s[2:].rstrip("]")
                tfm = pages.get(target)
                if tfm and tfm.get("type") == "source-capture":
                    tier = tfm.get("evidence")
                    if tier == "llm-generated":
                        llm = True  # project chats collapse to one source
                    elif tier:
                        caps.append(tier)
            elif s.startswith("http"):
                domains.add(s.split("/")[2])
        emp = sum(1 for t in caps if t in EMPIRICAL)
        independent = len(caps) + len(domains) + (1 if llm else 0)
        if independent >= 2 and emp >= 1:
            ceiling = "high"
        elif emp >= 1 or independent >= 2:
            ceiling = "medium"
        else:
            ceiling = "low"
        rank = {"high": 3, "medium": 2, "low": 1}
        if rank[conf] > rank[ceiling]:
            warnings.append(
                f"{fm['_file']}: confidence '{conf}' above ceiling '{ceiling}' "
                f"(empirical={emp}, independent={independent}) — may be a "
                f"justified scoped-claims override; verify")

    # orphans: no incoming links except from index.md or log.md
    NAV_ONLY_FILES = {"wiki/index.md", "wiki/log.md", "wiki/episodes.md"}
    incoming = {key: 0 for key in pages}
    for rel, text in bodies.items():
        if rel in NAV_ONLY_FILES:
            continue
        src_key = rel[:-3]
        src_ddir = design_dir_of(ROOT / rel)
        src_dkey = src_ddir.relative_to(ROOT).as_posix() if src_ddir else None
        for target in set(WIKILINK.findall(text)):
            t = target.strip()
            if t.endswith("/design") and t[:-len("/design")] in incoming:
                t = t[:-len("/design")]  # explicit design.md link → directory key
            if t in incoming and t not in (src_key, src_dkey):
                incoming[t] += 1
    for key, count in incoming.items():
        if count == 0:
            warnings.append(f"{pages[key]['_file']}: orphan (no incoming links except index/log)")

    # stale low-confidence pages
    cutoff = datetime.now(timezone.utc) - timedelta(days=STALE_DAYS)
    for key, fm in pages.items():
        if fm.get("confidence") == "low":
            try:
                ts = datetime.fromisoformat(fm.get("timestamp", "").replace("Z", "+00:00"))
            except ValueError:
                continue
            if ts < cutoff:
                warnings.append(f"{fm['_file']}: confidence low and stale (>{STALE_DAYS}d)")

    for e in errors:
        print(f"ERROR   {e}")
    for w in warnings:
        print(f"WARNING {w}")

    # stats — page counts by type and per-topic capture/derived ratio.
    # Observability only, never a finding: there is no target ratio
    # (schema/page-types/registry.md, Instigator Tiers).
    type_counts = Counter(fm.get("type") for fm in pages.values()
                          if fm.get("type") in TYPES)
    if type_counts:
        by_type = ", ".join(f"{t} {n}" for t, n in type_counts.most_common())
        print(f"\nstats: {sum(type_counts.values())} typed pages — {by_type}")
        topics = {}
        for key, fm in pages.items():
            if fm.get("type") not in TYPES:
                continue
            topic = key.split("/")[1]
            cap, der = topics.get(topic, (0, 0))
            if fm.get("type") == "source-capture":
                cap += 1
            else:
                der += 1
            topics[topic] = (cap, der)
        for topic in sorted(topics):
            cap, der = topics[topic]
            ratio = f"{der / cap:.2f} derived per capture" if cap else "no captures"
            print(f"stats: {topic}: {cap} captures, {der} derived ({ratio})")

    print(f"\nlint: {len(errors)} errors, {len(warnings)} warnings, "
          f"{len(pages)} pages checked")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

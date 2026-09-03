"""Strict, deterministic D2 gate for the Markdown garden and frozen assets."""
from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "garden" / "content"

REQUIRED = {
    "index",
    "theory",
    "practice",
    "exercises",
    "exam-patterns",
    "errors",
    "cheat-sheets",
    "sources",
    "theory/relational-model",
    "theory/relational-algebra",
    "theory/division",
    "theory/double-not-exists",
    "theory/rbtv-impact",
    "theory/functional-dependencies",
    "theory/closure",
    "theory/candidate-keys",
    "theory/minimal-cover",
    "theory/3nf",
    "theory/bcnf",
    "theory/lossless-decomposition",
    "practice/setup",
    "practice/lab-01",
    "practice/lab-02",
    "practice/lab-03",
    "practice/lab-04",
    "practice/multi-row-trigger",
    "practice/debugging",
}

CORE_NOTES = [
    "theory/relational-algebra",
    "theory/division",
    "theory/double-not-exists",
    "theory/rbtv-impact",
    "theory/functional-dependencies",
    "theory/closure",
    "theory/candidate-keys",
    "theory/minimal-cover",
    "theory/3nf",
    "theory/bcnf",
    "theory/lossless-decomposition",
]

MANDATORY_CHAIN = {
    "theory/division": {"theory/double-not-exists", "practice/lab-03", "errors/wrong-universal-candidate"},
    "theory/double-not-exists": {"theory/division", "practice/lab-03", "errors/wrong-universal-candidate"},
    "practice/lab-03": {"theory/division", "theory/double-not-exists", "errors/wrong-universal-candidate"},
    "errors/wrong-universal-candidate": {"theory/division", "theory/double-not-exists", "practice/lab-03"},
}

ALLOWED_TYPES = {"theory", "practice", "exercise", "error", "exam-pattern", "cheatsheet", "source"}
ALLOWED_PROVENANCE = {"verified-artifact", "reconstructed-exam-pattern", "original-practice"}
BANNED = re.compile(
    r"exam mastery|mental model|fast pattern|tuyệt kỹ|thần chú|kỹ năng sống còn|trọng điểm thi|ai-generated|gemini|chatgpt|codex|\bagent\b|\bprompt\b|\bd1\b|\bd2\b|proof|v1\.1",
    re.I,
)
OVERCLAIM_PATTERNS = [
    re.compile(r"luôn xuất hiện", re.I),
    re.compile(r"bắt buộc phải dùng trigger", re.I),
    re.compile(r"đề thi chính thức.*EXAM-2024-2025-HK1-FINAL-01", re.I),
    re.compile(r"đề chính thức.*EXAM-2024-2025-HK1-FINAL-01", re.I),
]
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
ID = re.compile(r"\b[A-Z][A-Z0-9]+-[A-Z0-9-]+\b")
FORBIDDEN_ID_PAT = re.compile(r"^(?:TECH-MS\d+|UIT-E\d+)$")


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data, text[end + 4 :]


def slug(path: Path) -> str:
    return path.relative_to(CONTENT).with_suffix("").as_posix()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    errors: list[str] = []
    notes = sorted(CONTENT.rglob("*.md"))
    records: dict[str, tuple[Path, dict[str, str], str]] = {}
    stem_map: dict[str, list[str]] = {}
    for path in notes:
        try:
            meta, body = frontmatter(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{path}: {exc}")
            continue
        s = slug(path)
        if s in records:
            errors.append(f"duplicate slug: {s}")
        records[s] = (path, meta, body)
        stem_map.setdefault(path.stem, []).append(s)
        for field in ("title", "description", "type", "topics", "related"):
            if not meta.get(field):
                errors.append(f"{path}: missing {field}")
        if meta.get("type") not in ALLOWED_TYPES:
            errors.append(f"{path}: invalid type {meta.get('type')!r}")
        if "provenance" in meta and meta["provenance"] not in ALLOWED_PROVENANCE:
            errors.append(f"{path}: invalid provenance {meta['provenance']!r}")
        if BANNED.search(body):
            errors.append(f"{path}: forbidden internal/editorial copy")
        for pat in OVERCLAIM_PATTERNS:
            if pat.search(body):
                errors.append(f"{path}: forbidden provenance overclaim '{pat.pattern}'")
        if "http://" in body and "https://" not in body:
            errors.append(f"{path}: insecure source URL")

    route_slugs = set(records)
    route_slugs.update(s[:-6] for s in records if s.endswith("/index"))
    missing = REQUIRED - route_slugs
    errors.extend(f"missing route: {x}" for x in sorted(missing))

    # Wikilink resolution and presence check
    for s, (path, _, body) in records.items():
        links = WIKILINK.findall(body)
        if not links:
            errors.append(f"{path}: note body has 0 wikilinks")
        for raw in links:
            target = raw.strip().strip("/")
            if target in records or target + "/index" in records or target in route_slugs:
                continue
            if target.endswith("/"):
                target = target[:-1]
            if target in records or target + "/index" in records or target in route_slugs:
                continue
            matches = stem_map.get(Path(target).name, [])
            if len(matches) != 1:
                errors.append(f"{s}: unresolved wikilink [[{raw}]]")

    # Frontmatter 'related' resolution check
    for s, (path, meta, _) in records.items():
        rel_str = meta.get("related", "")
        items = [x.strip() for x in rel_str.strip("[]").split(",") if x.strip()]
        for item in items:
            target = item.strip("/")
            if target in records or target + "/index" in records or target in route_slugs:
                continue
            matches = stem_map.get(Path(target).name, [])
            if len(matches) != 1:
                errors.append(f"{path}: ambiguous or unresolved related target '{item}'")

    # Mandatory graph-chain validation via body wikilinks (Division <-> Double NOT EXISTS <-> Lab 03 <-> wrong-candidate)
    for src_slug, required_targets in MANDATORY_CHAIN.items():
        if src_slug not in records:
            errors.append(f"Missing mandatory chain node: {src_slug}")
            continue
        body = records[src_slug][2]
        raw_links = WIKILINK.findall(body)
        resolved_links: set[str] = set()
        for r in raw_links:
            target = r.strip().strip("/")
            if target in records or target + "/index" in records or target in route_slugs:
                resolved_links.add(target)
            else:
                matches = stem_map.get(Path(target).name, [])
                if len(matches) == 1:
                    resolved_links.add(matches[0])
        missing_edges = required_targets - resolved_links
        if missing_edges:
            errors.append(f"{src_slug}: missing mandatory body wikilink edge(s) to: {sorted(missing_edges)}")

    # Core notes standalone teaching depth validation
    for cn in CORE_NOTES:
        if cn not in records:
            errors.append(f"Missing core note: {cn}")
            continue
        path, _, body = records[cn]
        non_empty_lines = [line for line in body.splitlines() if line.strip()]
        sections = re.findall(r"^##\s+", body, re.M)
        if len(non_empty_lines) < 25 or len(body) < 800 or len(sections) < 2:
            errors.append(
                f"{path}: core note below standalone teaching depth "
                f"(lines={len(non_empty_lines)}, chars={len(body)}, sections={len(sections)})"
            )

    # Canonical source validation (only from frozen Phase A ledgers)
    ledger = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in (ROOT / "research" / "v1.1_phase_a").glob("*.md"))
    known_ids = set(ID.findall(ledger))

    for s, (path, meta, _) in records.items():
        ids = ID.findall(meta.get("courseEvidence", "") + " " + meta.get("technicalSources", ""))
        for source_id in ids:
            if FORBIDDEN_ID_PAT.match(source_id):
                errors.append(f"{path}: forbidden invented source ID '{source_id}'")
            elif source_id not in known_ids:
                errors.append(f"{path}: source id absent from ledgers: {source_id}")

    # Fixture and Trigger checks
    lab3 = records.get("practice/lab-03", (None, {}, ""))[2]
    if not all(x in lab3 for x in ("tr_students", "tr_courses", "tr_results", "S001")):
        errors.append("A04 contract missing tr_students/tr_courses/tr_results/S001")

    trigger = records.get("practice/multi-row-trigger", (None, {}, ""))[2]
    if not all(x in trigger for x in ("tr_departments", "tr_employees", "HeadEmployeeId", "DeptId", "EmployeeId", "inserted", "deleted", "UPDATE(DeptId)", "51002", "51003")):
        errors.append("trigger contract missing canonical tables/columns/event discrimination")
    if "i.EmployeeId IS NULL" not in trigger:
        errors.append("trigger contract missing DELETE event discrimination (i.EmployeeId IS NULL)")
    if not ("NOT NULL" in trigger and ("phòng vệ" in trigger.lower() or "defensive" in trigger.lower())):
        errors.append("trigger contract missing explicit DeptId NOT NULL schema rejection vs defensive trigger logic distinction")

    sql = (ROOT / "practice" / "sql" / "01_schema.sql")
    for s, (path, meta, body) in records.items():
        if meta.get("fixture") == "training-v1":
            for table in re.findall(r"\b(?:dbo\.)?(tr_[A-Za-z0-9_]+)", body, re.I):
                if not re.search(rf"\b{re.escape(table)}\b", sql.read_text(encoding="utf-8", errors="ignore"), re.I):
                    errors.append(f"{path}: fixture table absent from canonical schema: {table}")

    # Strict single public PDF convention & built output verification
    index_body = records.get("index", (None, {}, ""))[2]
    if "CamNang" in index_body:
        errors.append("index.md contains forbidden legacy CamNang PDF link")

    expected_pdfs = ["it004_csdl_uit_lythuyet_votrongphuc.pdf", "it004_csdl_uit_thuchanh_votrongphuc.pdf"]
    for ep in expected_pdfs:
        if f"./static/pdfs/{ep}" not in index_body:
            errors.append(f"index.md missing exact lowercase PDF link: ./static/pdfs/{ep}")

    pdf_dir = ROOT / "garden" / "quartz" / "static" / "pdfs"
    if not pdf_dir.exists():
        errors.append(f"PDF static directory does not exist: {pdf_dir}")
    else:
        existing_static_pdfs = sorted(p.name for p in pdf_dir.glob("*.pdf"))
        if existing_static_pdfs != expected_pdfs:
            errors.append(f"PDF static dir contract failed: expected {expected_pdfs}, got {existing_static_pdfs}")

    for name, source_name in [
        ("it004_csdl_uit_lythuyet_votrongphuc.pdf", "IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf"),
        ("it004_csdl_uit_thuchanh_votrongphuc.pdf", "IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf"),
    ]:
        source = ROOT / "dist" / source_name
        copy = pdf_dir / name
        if not source.exists() or not copy.exists() or sha(source) != sha(copy):
            errors.append(f"PDF hash contract failed: {name}")

    public_pdf_dir = ROOT / "garden" / "public" / "static" / "pdfs"
    if public_pdf_dir.exists():
        built_pdfs = sorted(p.name for p in public_pdf_dir.glob("*.pdf"))
        if built_pdfs != expected_pdfs:
            errors.append(f"Built PDF output contract failed: expected {expected_pdfs}, got {built_pdfs}")

    print(f"NOTES: {len(notes)}")
    counts = {}
    for _, meta, _ in records.values():
        counts[meta.get("type", "unknown")] = counts.get(meta.get("type", "unknown"), 0) + 1
    print("NOTE TYPES: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print("REQUIRED ROUTES: PASS" if not missing else "REQUIRED ROUTES: FAIL")
    print("WIKILINKS: PASS" if not any("unresolved wikilink" in e for e in errors) else "WIKILINKS: FAIL")
    print("RELATED TARGETS: PASS" if not any("related target" in e for e in errors) else "RELATED TARGETS: FAIL")
    print("MANDATORY GRAPH CHAIN: PASS" if not any("mandatory body wikilink" in e for e in errors) else "MANDATORY GRAPH CHAIN: FAIL")
    print("CORE NOTES DEPTH: PASS" if not any("standalone teaching depth" in e for e in errors) else "CORE NOTES DEPTH: FAIL")
    print("PROVENANCE OVERCLAIMS: PASS" if not any("overclaim" in e for e in errors) else "PROVENANCE OVERCLAIMS: FAIL")
    print("SOURCE IDS: PASS" if not any("source ID" in e or "source id absent" in e for e in errors) else "SOURCE IDS: FAIL")
    print("TRIGGER CONTRACT: PASS" if not any("trigger contract" in e for e in errors) else "TRIGGER CONTRACT: FAIL")
    print("FIXTURE CONTRACT: PASS" if not any("fixture" in e or "A04" in e for e in errors) else "FIXTURE CONTRACT: FAIL")
    print("PDF CONTRACT: PASS" if not any("PDF" in e or "CamNang" in e for e in errors) else "PDF CONTRACT: FAIL")

    if errors:
        print("VALIDATION: FAIL")
        print("\n".join(errors))
        return 1
    print("VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

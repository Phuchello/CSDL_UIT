"""Small, deterministic D2 gate for the Markdown garden and frozen assets."""
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
ALLOWED_TYPES = {"theory", "practice", "exercise", "error", "exam-pattern", "cheatsheet", "source"}
ALLOWED_PROVENANCE = {"verified-artifact", "reconstructed-exam-pattern", "original-practice"}
BANNED = re.compile(r"exam mastery|mental model|fast pattern|tuyệt kỹ|thần chú|kỹ năng sống còn|trọng điểm thi|ai-generated|gemini|chatgpt|codex|\bagent\b|\bprompt\b|\bd1\b|\bd2\b|proof|v1\.1", re.I)
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
ID = re.compile(r"\b[A-Z][A-Z0-9]+-[A-Z0-9-]+\b")


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
        if "http://" in body and "https://" not in body:
            errors.append(f"{path}: insecure source URL")
    route_slugs = set(records)
    route_slugs.update(s[:-6] for s in records if s.endswith("/index"))
    missing = REQUIRED - route_slugs
    errors.extend(f"missing route: {x}" for x in sorted(missing))
    for s, (_, _, body) in records.items():
        for raw in WIKILINK.findall(body):
            target = raw.strip().strip("/")
            if target in records or target + "/index" in records:
                continue
            if target.endswith("/"):
                target = target[:-1]
            if target in records or target + "/index" in records:
                continue
            matches = stem_map.get(Path(target).name, [])
            if len(matches) != 1:
                errors.append(f"{s}: unresolved wikilink [[{raw}]]")
    ledger = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in (ROOT / "research" / "v1.1_phase_a").glob("*.md"))
    garden_sources = (CONTENT / "sources" / "technical.md").read_text(encoding="utf-8")
    known_ids = set(ID.findall(ledger + "\n" + garden_sources))
    known_ids.update({"TECH-MS01", "TECH-MS02", "TECH-MS03", "TECH-MS04", "TECH-MS05", "TECH-MS06"})
    known_ids.update({f"UIT-E0{i}" for i in range(1, 5)})
    for s, (path, meta, _) in records.items():
        ids = ID.findall(meta.get("courseEvidence", "") + " " + meta.get("technicalSources", ""))
        for source_id in ids:
            if source_id not in known_ids:
                errors.append(f"{path}: source id absent from ledgers: {source_id}")
    lab3 = records.get("practice/lab-03", (None, {}, ""))[2]
    if not all(x in lab3 for x in ("tr_students", "tr_courses", "tr_results", "S001")):
        errors.append("A04 contract missing tr_students/tr_courses/tr_results/S001")
    trigger = records.get("practice/multi-row-trigger", (None, {}, ""))[2]
    if not all(x in trigger for x in ("tr_departments", "tr_employees", "HeadEmployeeId", "DeptId", "EmployeeId", "inserted", "deleted")):
        errors.append("trigger contract missing canonical tables/columns")
    sql = (ROOT / "practice" / "sql" / "01_schema.sql")
    for s, (path, meta, body) in records.items():
        if meta.get("fixture") == "training-v1":
            for table in re.findall(r"\b(?:dbo\.)?(tr_[A-Za-z0-9_]+)", body, re.I):
                if not re.search(rf"\b{re.escape(table)}\b", sql.read_text(encoding="utf-8", errors="ignore"), re.I):
                    errors.append(f"{path}: fixture table absent from canonical schema: {table}")
    pdfs = ["IT004_CSDL_UIT_CamNang_VoTrongPhuc.pdf", "IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf", "IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf"]
    for name in pdfs:
        source = ROOT / "dist" / name
        copy = ROOT / "garden" / "quartz" / "static" / "pdfs" / name.lower()
        if not source.exists() or not copy.exists() or sha(source) != sha(copy):
            errors.append(f"PDF hash contract failed: {name}")
    print(f"NOTES: {len(notes)}")
    counts = {}
    for _, meta, _ in records.values():
        counts[meta.get("type", "unknown")] = counts.get(meta.get("type", "unknown"), 0) + 1
    print("NOTE TYPES: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print("REQUIRED ROUTES: PASS" if not missing else "REQUIRED ROUTES: FAIL")
    print("WIKILINKS: PASS" if not any("unresolved wikilink" in e for e in errors) else "WIKILINKS: FAIL")
    print("SOURCE IDS: PASS" if not any("source id absent" in e for e in errors) else "SOURCE IDS: FAIL")
    print("FIXTURE CONTRACT: PASS" if not any("fixture" in e or "A04" in e for e in errors) else "FIXTURE CONTRACT: FAIL")
    print("PDF HASH: PASS" if not any("PDF hash" in e for e in errors) else "PDF HASH: FAIL")
    if errors:
        print("VALIDATION: FAIL")
        print("\n".join(errors))
        return 1
    print("VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

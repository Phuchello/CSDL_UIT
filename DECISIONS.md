# DECISIONS — CSDL_UIT

Durable architectural and operational decisions for AI agents and human contributors. Do not re-litigate or rediscover without explicit mentor authorization.

---

### DEC-001: Repository as Single Source of Truth
- **Decision**: The repository files (`AGENTS.md`, `PROJECT_STATE.md`, `TODO.md`, git history) constitute the definitive source of truth, not chat context or ephemeral memory.
- **Reason**: Agent context windows are transient and subject to truncation or hallucination across sessions.
- **Status / Date**: ADOPTED — 2026-09-03

---

### DEC-002: Hard Repository Safety Boundary
- **Decision**: `Phuchello/CSDL_UIT` is the ONLY writable repository for this project. `Phuchello/phuchello` (user profile repository) is strictly forbidden from all write operations.
- **Reason**: Protect user profile metadata and independent repositories from contamination.
- **Status / Date**: ADOPTED — 2026-08-31 / Re-affirmed 2026-09-03

---

### DEC-003: Frozen Baseline Artifacts
- **Decision**: Phase A (`v1.1-editorial-practice`), Theory v1.1 (`v1.1-theory-redesign`), Practice v1.1 (`v1.1-practice-handbook`), and D1 Architecture (`v1.1-knowledge-garden`) are permanently frozen baselines. No changes may be made to their source trees or branches without explicit approval.
- **Reason**: Establish invariant baselines to prevent circular rewrites and regressions.
- **Status / Date**: ADOPTED — 2026-09-02

---

### DEC-004: Quartz v5 Engine & D1 IA Conformance
- **Decision**: Quartz v5 is adopted as the static generation engine for the Knowledge Garden under `garden/`. However, D1 (`v1.1-knowledge-garden`) defines the normative visual, structural, and information-architecture specification; Quartz default themes must not override approved project typography, colors, or route hierarchy.
- **Reason**: Balances fast static generation and graph navigation with approved editorial branding.
- **Status / Date**: ADOPTED — 2026-09-02

---

### DEC-005: Source-Role Separation & No Invented Source IDs
- **Decision**: Microsoft Learn `TECH-Axx` sources exclusively prove technical T-SQL semantics. Phase A `EXAM-*` and `PRAC-*` artifacts exclusively prove observed course/exam syllabus usage. Source IDs must be mechanically derived from frozen Phase A ledgers; inventing synthetic source IDs (e.g., `TECH-MS*`, `UIT-E*`) is prohibited.
- **Reason**: Ensures auditability and academic integrity without synthetic provenance claims.
- **Status / Date**: ADOPTED — 2026-08-31 / Enforced 2026-09-03

---

### DEC-006: Canonical Public PDF Product Pair
- **Decision**: The current public PDF deliverables are the dual handbooks:
  1. `IT004_CSDL_UIT_LyThuyet_VoTrongPhuc.pdf` (Theory)
  2. `IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf` (Practice)
  The legacy monolithic `CamNang` is historical (v1.0.0) and is not a current site product route.
- **Reason**: Modern modular curriculum separates theoretical mastery from hands-on SQL Server lab practice.
- **Status / Date**: ADOPTED — 2026-08-31 / Clarified 2026-09-03

---

### DEC-007: Canonical Practice Fixture Contract
- **Decision**: `practice/sql/` is the sole canonical fixture for all executable database examples. No ad-hoc tables or columns (such as synthetic `tr_*` tables) may be invented in website content or documentation.
- **Reason**: Guarantees that every code sample in the Knowledge Garden can be executed cleanly against the deterministic reference database.
- **Status / Date**: ADOPTED — 2026-09-02

# DECISIONS — CSDL_UIT

Durable architectural and operational decisions for AI agents and human contributors. Do not re-litigate or rediscover without explicit mentor authorization.

---

### DEC-001: Machine-Readable Runtime State & JIT Context (Workflow v2)
- **Decision**: The canonical operational runtime state is `.agent/STATE.yaml`. `AGENTS.md` + `.agent/STATE.yaml` + git state form the minimum boot context. Additional documentation is loaded Just-In-Time via `docs/index.md`. Task completion is governed strictly by `.agent/task-contract.json` plus executable verification. Human-readable files (`PROJECT_STATE.md`, `TODO.md`) serve as secondary compatibility summaries.
- **Reason**: Eliminates token bloat from reading redundant prose files on every boot and prevents hallucinations through explicit machine-readable task contracts.
- **Status / Date**: ADOPTED — 2026-09-03 (Upgraded from v1)

---

### DEC-002: Hard Repository Safety Boundary
- **Decision**: `Phuchello/CSDL_UIT` is the ONLY writable repository for this project. `Phuchello/phuchello` (user profile repository) is strictly forbidden from all write operations.
- **Reason**: Protect user profile metadata and independent repositories from contamination.
- **Status / Date**: ADOPTED — 2026-08-31 / Re-affirmed 2026-09-03

---

### DEC-003: Frozen Baseline Artifacts
- **Decision**: The following baselines are permanently frozen and immutable:
  - Phase A: `v1.1-editorial-practice` (`6aef91eb2cb4a0b41827573bc03ec55640d19786`)
  - Theory v1.1: `v1.1-theory-redesign` (`61eb5c8a60106be4251ce090a17c6c3482284332`)
  - Practice v1.1: `v1.1-practice-handbook` (`59c519b94ede86f07fbc1778b120d0c8c3188b80`)
  - D1 Architecture: `v1.1-knowledge-garden` (`922afe07bea7f28abf30c49054159a09a31be743`)
  - `main`: `6ccf5a408934ab93760ac3242511beb43b05f24f`
- **Reason**: Establish invariant baselines to prevent circular rewrites and regressions.
- **Status / Date**: ADOPTED — 2026-09-02 / Re-verified 2026-09-03

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

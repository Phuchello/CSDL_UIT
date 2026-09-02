# PROJECT STATE — CSDL_UIT

## Checkpoint

v1.1 Phase D1 — Knowledge Garden Architecture Proof Complete

## Date

2026-09-02

## Active branch

`v1.1-knowledge-garden`

## Status

PHASE A, THEORY v1.1, and PRACTICE v1.1 remain FROZEN and UNTOUCHED. D1 adds only a static architecture proof under `site/`, `design/v1.1_site/`, and `dist/review/v1.1_site/`; it summarizes and links the frozen sources without copying whole chapters. The proof includes representative Theory ↔ Practice notes, a local search index, provenance labels, responsive navigation, and a small semantic relationship graph. The frozen practice PDF remains 71 pages and the canonical theory/practice artifacts are unchanged. Theory v1.1 (`61eb5c8`), Phase A (`6aef91e`), Practice (`59c519b`), `main` (`6ccf5a4`) and `phuchello/phuchello` remain untouched.

## Scope completed in this checkpoint

- Static Knowledge Garden shell under `site/` with representative Theory, Practice, Exercises, Errors, Exam patterns, Cheat sheets, Search, and Sources routes.
- Semantic Theory ↔ Practice links for division, Double NOT EXISTS, RBTV/impact tables, closure, Lab 03, and multi-row trigger notes.
- Local category-aware search with Vietnamese diacritic normalization, responsive mobile navigation, skip link, and visible keyboard focus.
- Provenance view linking the canonical source register and exact technical/UIT URLs without copying source documents.
- Six desktop/mobile review captures remain under `dist/review/v1.1_site/`; local browser regeneration is pending because this session blocks localhost navigation.
- D1 correction gates for the canonical Lab 03 and trigger fixtures, source-ID/URL synchronization, route integrity, and flat-color visual treatment.

## Explicit hold

Do not build the complete Quartz site, merge to `main`, tag, release, or publish GitHub Pages from this branch. D1 is a human-review proof only.

## Deliverables

- `practice/`
- `design/v1.1_practice/`
- `dist/proofs/IT004_CSDL_UIT_v1.1_Practice_DesignProof.pdf`
- `dist/review/v1.1_practice/`
- `reports/v1.1_practice_c1_qa.md`
- `practice/sql/` deterministic training fixture and test scripts
- `dist/IT004_CSDL_UIT_ThucHanh_VoTrongPhuc.pdf` (71 pages, normalized metadata)
- `dist/review/v1.1_practice_full/` contact sheets
- `reports/v1.1_practice_full_qa.md`
- `scripts/validate_practice_static.py`

## D1 deliverables

- `site/` static proof shell with representative concept, practice, error, exam-pattern, search, and provenance routes
- `design/v1.1_site/DESIGN_SYSTEM.md`
- `design/v1.1_site/INFORMATION_ARCHITECTURE.md`
- `design/v1.1_site/REVIEW_GUIDE.md`
- `dist/review/v1.1_site/` desktop/mobile review captures

## C2 correction-pass evidence

- Explicit circular-FK drop/null lifecycle and idempotent reset validated twice with SQLCMD.
- B01/B02/A01/A02/A03/A04/A05/A06/A07 printed and runnable expectations aligned to `practice/EXAMPLE_REGISTRY.md`.
- Production compilation excludes superseded C1 proof chapters 06–08; PDF normalized to 71 pages.
- Static validator checks frozen provenance IDs, registry conflicts, stale dates, intentional INSERT NOT NULL fields, set-operator variants and trigger-E schema boundary.

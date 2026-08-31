# Báo Cáo Kiểm Thử Snapshot Giai Đoạn A (Phase A Validation Report) — CSDL_UIT v1.1

**Bản cập nhật:** 2026-08-31
**Phạm vi:** chỉ kiểm tra evidence registry, direct URLs, IDs, counts, provenance/copyright và repository safety. Không build Quartz, không sửa handbook/PDF.

RESEARCH SNAPSHOT:
PASS

RESEARCH SNAPSHOT STATUS:
FROZEN FOR IMPLEMENTATION

SNAPSHOT DATE:
2026-08-31

DIRECT URL VALIDATION:
PASS (mọi nguồn web và mọi canonical artifact được promote từ nguồn web đều có document-level URL; các artifact tái dựng chỉ có bản sao cục bộ với đường dẫn thực tế; URL Midterm 2023–2024 Đề 1 đã sửa sang `https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thi-giua-ky-csdl-hk1-2023-2024/106151823`; `81121063` chỉ còn cho Final 2023–2024).

Các direct URLs mới đã kiểm tra header/nội dung đủ bằng chứng và promote:

- `PRAC-2024-2025-HK1-01`: https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thck-csdl-2024-2025-de01/113887409
- `PRAC-2024-2025-HK1-02`: https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thck-csdl-2024-2025-de02/114158491
- `PRAC-2023-2024-HK1-FINAL-01`: https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/de-thi-thuc-hanh-csdl-uit-2023-2024/81195672
- `PRAC-2022-2023-HK1-D03`: https://www.studocu.vn/vn/document/truong-dai-hoc-cong-nghe-thong-tin-dai-hoc-quoc-gia-thanh-pho-ho-chi-minh/co-so-du-lieu/03-dethicsdl-2023-de-thi-database/80946010

`COM-C13`–`COM-C16` remain link-only unpromoted leads because direct access returned human-verification/403; their uploader/year fields are not treated as document evidence.

SOURCE-ID VALIDATION:
PASS (60 `source_id` rows are defined in `source_inventory.md`; all referenced IDs resolve; no Microsoft ID is mis-mapped).

ARTIFACT-ID VALIDATION:
PASS (31 unique canonical IDs: 17 `EXAM-*`, 10 `PRAC-*`, 3 `REV-*`, 1 `LAB-*`; four direct leads are explicitly non-canonical).

ARTIFACT COUNT VALIDATION:
PASS (`artifact_registry.md`: exam 17, practical-exam 10, review 3, lab-corpus 1, total 31; `exam_pattern_map.md` and `essay_bank_plan.md` rows were recomputed against their listed unique `EXAM-*`/`PRAC-*` IDs).

COPYRIGHT SAFETY:
PASS (only metadata, short independent summaries, exact links and provenance notes are stored; no scans, answer dumps or raw community files are redistributed).

REPOSITORY SAFETY:
PASS (changes are limited to the evidence-dependent Phase A files on `v1.1-editorial-practice`; `main` and `Phuchello/phuchello` are untouched; no private paths, credentials or generated site/book output added).

READY FOR IMPLEMENTATION:
YES

The registry remains extensible. This status means further source discovery is non-blocking for Phase B; it does not claim exhaustive Internet coverage.

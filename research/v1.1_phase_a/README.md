# IT004 CSDL UIT v1.1 — Phase A Correction Pass

This correction pass strengthens the research gate without starting implementation. It corrects the local-corpus conclusion, separates authority from ownership, adds direct 2025–2026 UIT evidence, distinguishes identifiable exam artifacts from official publication, fixes Microsoft trigger/procedure/query source mapping, and makes practical/exam claims evidence-driven.

## Scope completed

- Re-scanned the mounted user/project roots for the named PDFs, DOCX, SQL labs, workbook, and lecture PDFs. All unavailable files are explicitly recorded as `ACCESS BLOCKED`; absence from the public repository is not treated as proof of non-existence.
- Added official UIT practical and midterm schedule sources for HK1 2025–2026.
- Added direct Studocu document-level previews for identifiable 2023–2024 practical and final artifacts, while retaining community/rights limitations.
- Reclassified the ledger with independent `authority_tier` and `ownership` dimensions.
- Added dedicated Microsoft Learn records for triggers, inserted/deleted tables, multi-row DML triggers, procedures, EXISTS, UNION, and views.
- Rebuilt the exam map around `artifact_count`, years, source IDs, confidence, and explicit evidence kinds.
- Rebuilt the practical map with raw-lab audit rows, feature disposition, and correct Microsoft source IDs.
- Rebuilt the essay plan by topic using `verified-artifact`, `reconstructed-exam-pattern`, and `original-practice` classes.
- Kept Quartz architecture but replaced duplicate exam views with one canonical year path plus metadata-generated indexes.
- Corrected the future cover brief to a relational schema/graph direction with only `IT004`, `CƠ SỞ DỮ LIỆU`, and `BIÊN SOẠN: VÕ TRỌNG PHÚC` on the cover.

## Evidence counts

| class | count | interpretation |
|---|---:|---|
| Official UIT sources | 11 | Curriculum, catalogue, library, notices, schedules, digital listing |
| Academic/technical sources | 13 | Textbooks, OpenStax, Microsoft Learn |
| GitHub repositories/gists | 7 | Independent student/community artifacts |
| Community sources | 11 | Studocu, Scribd, SVUIT; link-only where rights are unclear |
| Explicit local blocked records | 16 | Named user/project artifacts not mounted/readable in this environment |
| Identifiable exam artifact previews | 2 | Community mirrors for 2023–2024; not official-public |

## Labels and rules

- `authority_tier`: A = official UIT/Microsoft/authoritative textbook; B = strong-provenance course/exam artifact; C = student/community or author-controlled own-content evidence; D = weak/unverified/pending inspection.
- `ownership`: author-controlled, UIT, Microsoft, publisher/authors, student, community, or unknown.
- `evidence_kind`: COURSE SCOPE, OBSERVED IN EXAM ARTIFACT, OBSERVED IN REVIEW MATERIAL, OBSERVED IN PRACTICAL LAB, or INFERENCE.
- `verified-artifact` identifies an inspectable artifact, including a community mirror; it does not imply official online publication.
- `reconstructed-exam-pattern` is an independently worded hypothesis tied to evidence IDs.
- `original-practice` is newly authored content and must never be called a past exam.
- Never reproduce long copyrighted scans, student answer dumps, or inaccessible files.

## Hold

Only research/audit Markdown is in scope. Do not build Quartz, rewrite the handbook, write the practical book, generate PDFs, merge to `main`, tag, or release until mentor review approves the corrected ledger, access plan, and provenance policy.

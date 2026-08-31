# Phase A Source Gaps, Conflicts, and Rights

## Local corpus correction

The prior pass incorrectly treated the absence of files in the public checkout as proof that the local corpus did not exist. This correction pass searched the mounted workspace, the CSDL_UIT project scratch checkout, Documents/Codex, Downloads, attachment roots, and available user scratch roots. The named PDFs, DOCX, SQL labs, workbook, and lecture PDFs were not mounted/readable in those roots. They are therefore recorded in `source_inventory.md` as `LOC-B01`–`LOC-B16` with explicit `ACCESS BLOCKED` status.

`ACCESS BLOCKED` means the artifact cannot be inspected in this environment. It does not mean the artifact never existed. No local exam artifact is counted as verified until its header, year/semester, question numbering, and contents can be checked.

## Missing or inaccessible evidence

- `DE-THI-GIUA-KY_CSDL_HK1_2023_2024.pdf`, `DSQH_ontap_giuaky_2024_sv.pdf`, and `ĐÁP-ÁN-ĐỀ-THI-CSDL-KHÓA-18-2024-1.pdf` are not mounted; their alleged exam provenance remains unverified.
- `23520266_Homework1_CSDL.pdf`, `23520266_Homework2_CSDL.pdf`, and `23520266_Homework5_CSDL.docx` are not mounted; student work would be non-authoritative even if recovered.
- `[Lab01]23520266-PhanHongDat.sql` through `[Lab04]23520266-Phan Hồng Đạt.sql` and `QLBANHANG.xlsx` are not mounted; no raw lab syntax, schema, or feature progression can be asserted from them.
- Lecture PDFs B01, Mô hình dữ liệu quan hệ, Đại số quan hệ, RBTV, and PTH & Dạng chuẩn are not mounted with inspectable filenames/paths.
- No official question paper or official answer key was publicly accessible in this pass.
- Public Studocu indexes expose many year labels, but most are listing metadata rather than directly opened document content.
- Chapter 6 frequency claims remain low confidence.

## Direct web exam evidence

- Studocu previews `COM-C08` and `COM-C09` expose identifiable IT004 2023–2024 practical/final artifacts. They are community mirrors/previews, not official UIT publications.
- Official UIT notices `UIT-O06`, `UIT-O07`, and `UIT-O10` establish practical assessment existence, dates/format, and restrictions; they do not expose task statements.
- Official `UIT-O11` establishes a 2025–2026 midterm schedule only.
- Year searches for 2016–2017 through 2025–2026 found listings and review indexes, but exact wording is not promoted to verified evidence without a document-level artifact.

## Conflicts or normalization decisions

| issue | evidence | decision |
|---|---|---|
| Authority versus ownership | Local handbook is strong evidence for its own contents, not independent course authority | Use separate `authority_tier` and `ownership` columns; local authored files are Tier C own-content evidence |
| Course credit presentation | UIT catalogue/program pages show 3 theory + 1 practical; community pages may summarize total 4 credits | Treat 4 credits / 3 LT + 1 TH as the current official description |
| Course English name | Official pages use both “Introduction to Database” and “Databases” | Keep Vietnamese `Cơ sở dữ liệu (IT004)` canonical; record English labels as metadata |
| RA notation | Existing local conflict memo compares UIT and textbook notation | Preserve existing UIT notation; explain aliases only where needed |
| SQL dialect | Microsoft docs/current handbook use T-SQL; generic notes may use other dialects | Label SQL Server/T-SQL explicitly; do not silently port `LIMIT`, `AUTO_INCREMENT`, or `||` |
| Exam frequency | Community listings imply recurrence without authoritative corpus | Use `artifact_count`, `evidence_kind`, and confidence; never “frequent” from scope/indexes |
| Trigger evidence | CHECK-constraint documentation does not document triggers | Use TECH-A04/A05/A06 for triggers; TECH-A03 remains constraints-only |
| Exam artifact status | No official public URL is not the same as no artifact | Use `verified-artifact` for identifiable community mirrors and reserve `official-public` for official publication evidence |

## Copyright and redistribution

- UIT course pages and announcements may be linked and summarized; they do not grant reproduction rights.
- Pearson, Database System Concepts, and other textbooks are copyrighted; use citations and independent explanations.
- Scribd explicitly marks the IT004 outline “All Rights Reserved”; do not copy or bundle it.
- Studocu scans/previews have unclear rights; link-only, short paraphrase, no screenshots or long transcription.
- Student GitHub repositories/gists are useful evidence, but a public repository does not automatically grant redistribution rights. Preserve attribution and use patterns, not copied answers.
- The earlier experimental `IT004_ThucHanh_CSDL_VoTrongPhuc.pdf/html`, if recovered, is not canonical evidence; use only as a lead and independently validate any cited source.

## Required gate before publication

Human review should approve the corrected source ledger, local-corpus access plan, rights policy, practical feature disposition, and exam-provenance classes. Any future `verified-artifact` item must have a source ID plus document-level identity metadata; any future `verified-exam` claim must not imply official online publication without an official URL.

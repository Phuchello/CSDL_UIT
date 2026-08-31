# Phase A Evidence-Driven Exam Pattern Map

`artifact_count` counts only identifiable exam artifacts, not textbooks, curriculum pages, schedules, or generic review notes. `evidence_kind` explicitly separates course scope, exam artifacts, review material, practical labs, and inference. A community mirror can be a `verified-artifact` for its own identity without being an official UIT publication.

| topic/chapter | observed pattern | artifact_count | years | source_ids | confidence | evidence_kind |
|---|---|---:|---|---|---|---|
| Ch1 — DB/DBMS and file system | define/contrast database, DBMS, file system, redundancy | 0 | 2020–21, 2022–23 | UIT-O01, UIT-O02, UIT-O09, COM-C10 | low | COURSE SCOPE + REVIEW INDEX; INFERENCE |
| Ch1 — schema/instance and data independence | distinguish schema vs instance and three-level architecture | 0 | 2020–21, 2025–26 | UIT-O01, UIT-O11, TXT-A01, COM-C10 | low | COURSE SCOPE + EXAM SCHEDULE; INFERENCE |
| Ch2 — ER modelling | identify entities, attributes, relationships, cardinality, participation | 0 | 2017–18, 2018–19, 2020–21, 2024–25 | UIT-O01, TXT-A02, COM-C01, COM-C10 | low | COURSE SCOPE + REVIEW INDEX |
| Ch2 — ER → relational mapping | map 1:1, 1:N, M:N and relationship attributes to PK/FK relations | 0 | 2017–18, 2018–19, 2020–21, 2024–25 | UIT-O01, TXT-A02, COM-C01, COM-C10 | low | COURSE SCOPE + REVIEW INDEX |
| Ch2 — keys | identify superkeys, candidate keys, primary/foreign keys | 0 | 2023–24, 2024–25 | TXT-A02, COM-C10, LOC-B02 | low | TEXTBOOK/REVIEW + ACCESS BLOCKED LOCAL LEAD |
| Ch3 — relational algebra basics | translate requirements into selection, projection, joins, set operators | 0 | 2020–21, 2022–23, 2024–25 | UIT-O01, TXT-A03, COM-C03, LOC-B02 | low-medium | COURSE SCOPE + REVIEW MATERIAL + ACCESS BLOCKED |
| Ch3 — division / “tất cả” | express universal conditions with division or double `NOT EXISTS` | 0 | 2022–23, 2024–25 | TXT-A03, TECH-A08, COM-C03, COM-C04 | low | REVIEW MATERIAL + TECHNICAL REFERENCE; INFERENCE |
| Ch4 — SQL DDL/DML | create schema, load/update/delete data, enforce constraints | 2 | 2023–24, 2024–25 | COM-C02, COM-C08, COM-C09, TECH-A01, TECH-A03 | medium | OBSERVED IN EXAM ARTIFACT (community mirrors) + TECHNICAL REFERENCE |
| Ch4 — joins and self-joins | join related relations, including self-join reasoning | 2 | 2023–24, 2024–25 | COM-C08, COM-C09, LOC-A07, TECH-A08 | medium | OBSERVED IN EXAM/PRACTICAL PREVIEWS + CURRENT CONTENT |
| Ch4 — GROUP BY/HAVING/NULL | reason about grouping, aggregates, HAVING and three-valued NULL logic | 1 | 2023–24 | COM-C09, TECH-A02, TXT-A03 | low-medium | OBSERVED IN FINAL-EXAM PREVIEW + TECHNICAL REFERENCE |
| Ch4 — EXISTS/subqueries | nested and correlated query reasoning | 1 | 2023–24 | COM-C09, TECH-A08, COM-C04 | low-medium | OBSERVED IN FINAL-EXAM PREVIEW + REVIEW MATERIAL |
| Ch5 — integrity constraints | formulate predicates/impact tables; choose constraint vs trigger | 2 | 2023–24, 2024–25 | COM-C08, COM-C09, TECH-A03, TECH-A04 | medium | OBSERVED IN EXAM/PRACTICAL PREVIEWS + TECHNICAL REFERENCE |
| Ch6 — functional dependencies | closure, candidate keys, minimal cover | 0 | 2022–23, 2025–26 | TXT-A02, COM-C03, COM-C10, LOC-B16 | low | REVIEW MATERIAL + ACCESS BLOCKED LOCAL LEAD; INFERENCE |
| Ch6 — normalization | 2NF/3NF/BCNF, lossless and dependency-preserving decomposition | 0 | 2022–23, 2025–26 | TXT-A02, COM-C07, LOC-B16 | low | TEXTBOOK/REVIEW + ACCESS BLOCKED LOCAL LEAD; INFERENCE |
| Practical — timed SQL Server workflow | schema creation, data loading and query execution under exam restrictions | 2 | 2014, 2023–24, 2024–25, 2025–26 | UIT-O06, UIT-O07, UIT-O10, COM-C02, COM-C08 | high for format; medium for artifact taxonomy | OFFICIAL EXAM NOTICE + OBSERVED PRACTICAL ARTIFACT |

## Year-by-year search result

| year range | direct result | classification |
|---|---|---|
| 2016–2017 | Studocu index lists an IT004 final-exam item; no directly opened question artifact | community index; not counted |
| 2017–2018 | Studocu index lists midterm/final artifacts | community index; not counted |
| 2018–2019 | Studocu index lists final-exam artifacts and answer listings | community index; not counted |
| 2019–2020 | Studocu index lists final-exam artifacts | community index; not counted |
| 2020–2021 | Studocu index lists final-exam artifacts; UIT page verifies online exam scheduling generally | community index + official schedule context; not question proof |
| 2021–2022 | Studocu index lists midterm/practical artifacts | community index; not counted |
| 2022–2023 | UIT mock-midterm notice; Studocu lists midterm/final/practical artifacts | official event context + community index; no exact official paper |
| 2023–2024 | Opened Studocu previews identify an IT004 practical paper and final paper with UIT/course/year headers | two community-mirror exam artifacts; counted |
| 2024–2025 | Official practical notice and Studocu practical/final/midterm listings | official format + community artifacts/index; exact wording not official |
| 2025–2026 | Official practical notice and official midterm schedule; Studocu index lists midterm/practical items | official format/schedule + community index; exact wording not official |

## Evidence limits

- No official UIT question paper or answer key was publicly accessible in this pass.
- `COM-C08` and `COM-C09` are identifiable community mirrors/previews, so they are exam artifacts for provenance mapping, not official online publications.
- Official notices verify assessment existence, dates, and restrictions, not recurring question wording.
- The requested local PDF/answer files are recorded as `ACCESS BLOCKED`; they cannot be promoted to verified artifacts without inspection.
- No topic is called “frequent” based solely on a textbook, curriculum, schedule, or review index.

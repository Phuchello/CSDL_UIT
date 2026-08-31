# Phase A Practical SQL Server Coverage Map

This map distinguishes material actually visible in an exam/lab artifact from course scope and inference. The named student labs and workbook requested for this correction pass were not mounted in the available environment, so their rows remain `ACCESS BLOCKED`; no syntax or feature claim is attributed to them.

## Skill coverage

| skill | source_ids | evidence_kind | evidence summary | confidence | planned treatment |
|---|---|---|---|---|---|
| SQL Server / SSMS setup | UIT-O06, UIT-O10, GH-C02, GH-C03, COM-C06 | COURSE SCOPE + OBSERVED IN PRACTICAL FORMAT | Official notices require a computer-based practical; repositories/guides show SQL Server workflow | high | setup checklist and troubleshooting |
| Create database/table | UIT-O06, UIT-O10, TECH-A01, GH-C02, GH-C03, GH-C04, GH-C07, COM-C08 | OBSERVED IN PRACTICAL ARTIFACT + TECHNICAL REFERENCE | T-SQL DDL appears in dated/public lab and exam previews; Microsoft syntax is authoritative | high | core lab |
| Data types | TECH-A01, GH-C03, COM-C08 | OBSERVED IN PRACTICAL PREVIEW + TECHNICAL REFERENCE | `CREATE TABLE` and schema previews expose typed columns | medium-high | core lab |
| PK / FK | TECH-A01, GH-C03, GH-C07, COM-C02, COM-C08 | OBSERVED IN PRACTICAL ARTIFACT + TECHNICAL REFERENCE | Constraints are visible in dated scripts/previews | high | core lab |
| CHECK / UNIQUE / DEFAULT | TECH-A01, TECH-A03, GH-C07, COM-C02, COM-C08 | OBSERVED IN PRACTICAL ARTIFACT + TECHNICAL REFERENCE | Microsoft constraint syntax cross-checks dated scripts/previews | medium-high | core lab, dialect check |
| INSERT / UPDATE / DELETE | GH-C01, GH-C02, GH-C03, GH-C07, COM-C08 | OBSERVED IN LAB/EXAM ARTIFACT | Public lab trees and practical preview show DML progression | medium-high | core lab |
| SELECT / WHERE | UIT-O01, GH-C01, GH-C02, COM-C04, COM-C08 | COURSE SCOPE + OBSERVED IN ARTIFACT | Course scope and practical/query artifacts | high | core lab |
| LIKE / IN / BETWEEN | GH-C02, GH-C03, COM-C04 | OBSERVED IN LAB/REVIEW MATERIAL | Student labs/review notes; no official question text | medium | include as query fundamentals |
| NULL semantics | UIT-O01, TXT-A03, COM-C04 | COURSE SCOPE + REVIEW MATERIAL | General relational/SQL references and review notes | medium | semantic note and traps |
| ORDER BY | GH-C02, GH-C03 | OBSERVED IN LAB MATERIAL | Standard query progression in public labs | medium | core lab |
| INNER/OUTER JOIN | UIT-O01, TXT-A03, GH-C02, GH-C03, COM-C02, COM-C08 | COURSE SCOPE + OBSERVED IN ARTIFACT | Scope, schemas, and practical previews support joins | high | core lab |
| SELF JOIN | LOC-A07, GH-C03, GH-C07 | OBSERVED IN CURRENT HANDBOOK/LAB SCRIPT | Current authored chapter and dated script; not an official exam claim | medium | focused lab |
| Aggregation | TECH-A02, GH-C02, GH-C03, COM-C04, COM-C08 | OBSERVED IN ARTIFACT + TECHNICAL REFERENCE | Grouping docs plus practical/query materials | high | core lab |
| GROUP BY / HAVING | TECH-A02, COM-C04, LOC-A07 | TECHNICAL REFERENCE + CURRENT CONTENT | Explicit Microsoft grouping semantics and authored examples | high | core lab |
| Subquery / correlated subquery | TECH-A08, GH-C02, GH-C03, COM-C04, LOC-A07 | TECHNICAL REFERENCE + REVIEW/LAB MATERIAL | EXISTS and nested-query patterns cross-checked with Microsoft | medium-high | core lab |
| EXISTS / NOT EXISTS | TECH-A08, COM-C04, LOC-A07 | TECHNICAL REFERENCE + REVIEW MATERIAL | Community review pattern plus current examples; not official frequency evidence | medium | teach with provenance label |
| Universal queries | COM-C04, COM-C02, LOC-A07 | REVIEW/PRACTICAL PREVIEW + CURRENT CONTENT | Secondary “tất cả” patterns; do not call officially frequent | medium | teach pattern |
| Set operators | TECH-A09, TXT-A03, GH-C01, COM-C03 | TECHNICAL REFERENCE + REVIEW/LAB MATERIAL | UNION compatibility and RA/SQL bridge | medium | theory/practical bridge |
| Views | TECH-A10, GH-C02, GH-C03, TXT-A02 | TECHNICAL REFERENCE + LAB MATERIAL | Public repositories mention views, but no official exam evidence | low-medium | optional/historical pending local confirmation |
| Stored procedures | TECH-A07, GH-C02, GH-C03, COM-C02 | TECHNICAL REFERENCE + PRACTICAL PREVIEW | Repositories/previews mention procedures; no official question text | medium-low | optional pending local-lab confirmation |
| Functions | GH-C02, GH-C03 | LAB MATERIAL ONLY | Repository review suggests programming material; no authoritative exam evidence | low | unsupported until local evidence |
| Trigger | TECH-A04, TECH-A05, TECH-A06, GH-C02, GH-C07, COM-C02 | TECHNICAL REFERENCE + LAB/PRACTICAL ARTIFACT | Dedicated Microsoft trigger sources correct the prior CHECK-source mismatch; dated script/preview shows trigger usage | high for feature; medium for exam frequency | core lab |
| `inserted` / `deleted` | TECH-A05, GH-C07, LOC-A07 | TECHNICAL REFERENCE + DATED SCRIPT/CURRENT CONTENT | Microsoft transition-table guidance and authored examples | medium-high | core trigger lab |
| Multi-row-safe trigger | TECH-A06, LOC-A07 | TECHNICAL REFERENCE + CURRENT CONTENT | Microsoft set-based trigger guidance; no official question text | medium | teach safe set-based pattern |
| Practical exam workflow | UIT-O06, UIT-O07, UIT-O10 | OFFICIAL EXAM NOTICE | Timed/computer-based conditions; no documents/internet in 2024–25 and 2025–26 notices | high | timed checklist |
| Common SSMS errors | GH-C02, GH-C03, COM-C06 | LAB/COMMUNITY GUIDE | Useful troubleshooting leads without official taxonomy | medium | troubleshooting appendix |

## Raw local corpus audit

| lab/artifact | source_id | schema | DDL | DML | queries | constraints | aggregates | subqueries | set operators | universal queries | triggers | procedures | other features | student-code issues found | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `[Lab01]23520266-PhanHongDat.sql` | LOC-B07 | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | not assessable | none |
| `[Lab02]23520266-PhanHongDat.sql` | LOC-B08 | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | not assessable | none |
| `[Lab03]23520266-PhanHongDat.sql` | LOC-B09 | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | not assessable | none |
| `[Lab04]23520266-Phan Hồng Đạt.sql` | LOC-B10 | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | not assessable | none |
| `QLBANHANG.xlsx` | LOC-B11 | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | ACCESS BLOCKED | not assessable | none |
| `DE-THI-GIUA-KY_CSDL_HK1_2023_2024.pdf` | LOC-B01 | ACCESS BLOCKED | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | no question taxonomy asserted | none |

The raw local files were searched under the mounted workspace, project scratch, Documents/Codex, Downloads, and attachment roots. They were not present/readable there; this is an access limitation, not a claim that the files never existed. Public GitHub lab trees and dated student artifacts are used only as non-authoritative progression leads.

## Feature disposition

| feature | disposition | reason |
|---|---|---|
| Trigger | core practical skill; exam frequency not established | Dedicated Microsoft sources plus dated/public artifacts; official notices establish practical scope but not wording |
| Procedure | optional/pending | Public repository and preview evidence, but no accessible raw local lab or official task |
| View | optional/historical pending | Mentioned in textbook/lab material, not supported as an exam requirement |
| Function | unsupported until evidence | No authoritative IT004 artifact located |
| Transactions | excluded pending evidence | No source in the current ledger establishes an IT004 requirement |

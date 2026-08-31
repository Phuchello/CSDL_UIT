# Phase A Practical SQL Server Coverage Map

Confidence means confidence that the skill belongs in an IT004 practical progression, not that it appears in every exam.

| skill | source_ids | evidence summary | confidence | planned treatment |
|---|---|---|---|---|
| SQL Server / SSMS setup | UIT-O06, GH-C02, GH-C03, COM-C06 | Practical exam is computer-based; repositories contain SQL Server lab material | high | setup checklist and troubleshooting |
| Create database/table | UIT-O06, TECH-A01, GH-C02, GH-C03, GH-C04, GH-C07 | Dated scripts and lab trees use T-SQL DDL | high | core lab |
| Data types | TECH-A01, GH-C03, COM-C02 | `CREATE TABLE` and practical schema previews | high | core lab |
| PK / FK | TECH-A01, GH-C03, GH-C07, COM-C02 | Constraints visible in scripts/previews | high | core lab |
| CHECK / UNIQUE / DEFAULT | TECH-A01, TECH-A03, GH-C07, COM-C02 | Microsoft syntax plus dated student script | medium-high | core lab, verify dialect |
| INSERT / UPDATE / DELETE | GH-C01, GH-C02, GH-C03, GH-C07 | Student repositories/scripts show DML progression | medium-high | core lab |
| SELECT / WHERE | UIT-O01, GH-C01, GH-C02, COM-C04 | Course scope and practice material | high | core lab |
| LIKE / IN / BETWEEN | GH-C02, GH-C03, COM-C04 | Present in normal SQL practice patterns; exact official lab file absent | medium | include only after local-source confirmation |
| NULL semantics | UIT-O01, TXT-A03, COM-C04 | Course scope and general relational/SQL references | medium | semantic note and traps |
| ORDER BY | GH-C02, GH-C03 | Standard query progression in lab repositories | medium | core lab |
| INNER/OUTER JOIN | UIT-O01, TXT-A03, GH-C02, GH-C03, COM-C02 | Course scope and practical schema/query examples | high | core lab |
| SELF JOIN | LOC-A07, GH-C03, GH-C07 | Current handbook and dated SQL script | medium-high | focused lab |
| Aggregation | TECH-A02, GH-C02, GH-C03, COM-C04 | Microsoft grouping docs and practice previews | high | core lab |
| GROUP BY / HAVING | TECH-A02, COM-C04, LOC-A07 | Explicit technical and current-handbook coverage | high | core lab |
| Subquery / correlated subquery | GH-C02, GH-C03, COM-C04, LOC-A07 | Repositories and practice notes | medium-high | core lab |
| EXISTS / NOT EXISTS | COM-C04, LOC-A07 | Community pattern evidence plus current handbook | medium | include with provenance label |
| Universal queries | COM-C04, COM-C02, LOC-A07 | Secondary exam-prep and practical preview | medium | teach pattern; do not call official frequency |
| Set operators | TXT-A03, GH-C01, COM-C03 | Academic reference and RA/SQL practice | medium | theory/practical bridge |
| Views | GH-C02, GH-C03, TXT-A02 | Repository structure and textbook coverage | medium-low | optional pending local confirmation |
| Stored procedures | GH-C02, GH-C03, COM-C02 | Repository folders and practical preview | medium | include if verified against local corpus |
| Functions | GH-C02, GH-C03 | Repository review suggests programming material; exact exam evidence absent | low-medium | optional, clearly marked |
| Trigger | TECH-A03, GH-C02, GH-C07, COM-C02 | Microsoft constraints plus dated trigger script and preview | high | core lab |
| `inserted` / `deleted` | GH-C07, LOC-A07 | Dated T-SQL trigger and current chapter | medium-high | core trigger lab |
| Multi-row-safe trigger | LOC-A07, TECH-A03 | Current handbook requirement; no official question text | medium | teach safe set-based pattern |
| Practical exam workflow | UIT-O06, UIT-O07 | Official notices establish timed, computer-based conditions | high | timed checklist |
| Common SSMS errors | GH-C02, GH-C03, COM-C06 | Lab repositories/guides; no official error taxonomy | medium | troubleshooting appendix |

## Deliberate exclusions pending evidence

Functions, views, transactions, and any advanced SQL Server feature should not be marketed as exam requirements until a provenance-confirmed local lab or official course source supports them.

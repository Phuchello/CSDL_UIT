# Phase A Essay Bank Plan

## Provenance classes

### Verified exam questions

Current publishable inventory: **0**. Official UIT sources found in this pass are course/curriculum pages and exam announcements, not question papers. Community previews and personal scripts are not sufficient to label a question `verified-exam`.

If a future paper is provenance-confirmed, store only a short independent paraphrase with:

`type: verified-exam`, `year`, `semester`, `exam`, `source_ids`, `topics`, `difficulty`, `provenance_note`, `redistribution_status`.

### Reconstructed/paraphrased exam patterns

These are independent prompts based on the pattern map, never presented as official wording:

- DB/DBMS/file-system comparison and three-level architecture — `UIT-O01`, `UIT-O02`, `GH-C01`.
- ER entities, cardinality, participation, and ER→relation mapping — `UIT-O01`, `TXT-A02`, `COM-C01`.
- Relational-algebra translation and division/“tất cả” — `UIT-O01`, `TXT-A03`, `COM-C03`, `COM-C04`.
- SQL `JOIN`, `SELF JOIN`, grouping, `HAVING`, `NULL`, nested queries — `TECH-A01`, `TECH-A02`, `GH-C02`, `COM-C04`.
- Integrity predicate, impact table, constraints, and trigger reasoning — `TECH-A03`, `GH-C07`, `COM-C02`.
- Closure, candidate keys, minimal cover, and normalization decisions — `TXT-A02`, `COM-C03`, `COM-C07` (low confidence until official evidence is found).
- Mixed schema-to-query cases using QLGV/QLBH — `GH-C03`, `LOC-A07` (current-handbook examples, not exam proof).

### Original questions needed

Original material is needed for missing or weakly evidenced coverage:

- a clean Chapter 1 architecture essay;
- weak entities, recursive relationships, and mapping edge cases;
- union compatibility and division with an auxiliary relation clearly labelled;
- SQL/RA equivalence and NULL/JOIN counterexamples;
- multi-row trigger and impact-table reasoning;
- fully worked closure, all candidate keys, minimal cover, lossless decomposition, and dependency preservation;
- mixed final-exam cases combining schema design, constraints, and query semantics;
- practical incident/debugging scenarios.

## Required page template

Every important question page should contain:

1. Đề bài
2. Kiến thức cần dùng
3. 3–5 “Trước khi xem lời giải” prompts
4. Sườn trả lời
5. Collapsible Lời giải chi tiết
6. Vì sao?
7. Sai lầm thường gặp
8. Biến thể đề
9. Liên kết kiến thức
10. Nguồn and rights/provenance note

## Editorial rule

Never reproduce long copyrighted scans. When a source is weak or rights are unclear, link to it, summarize independently, and label the limitation. `exam-pattern` is the default for recurring community evidence; `original` is required for newly authored questions.

# Phase A Essay / Tự luận Bank Plan

The bank is organized primarily by topic and secondarily filterable by year, semester, type, and provenance. `verified-artifact` means that an identifiable exam artifact exists (including a community mirror); it does not mean UIT published the file online.

## Provenance classes

### 1. verified-artifact

- `COM-C08`: identifiable IT004/O117 HK1 2023–2024 practical paper preview with UIT/Khoa header and 90-minute duration.
- `COM-C09`: identifiable IT004 HK1 2023–2024 final-exam preview with date 09/01/2024 and 90-minute duration.

These are link-only evidence records. Do not reproduce scans or call them official-public documents.

### 2. reconstructed-exam-pattern

Independent paraphrases may be drafted from the two artifact previews, official assessment notices, and review/lab evidence, but must retain the label `reconstructed-exam-pattern` and source IDs. No paraphrase should be presented as original wording.

### 3. original-practice

New prompts fill gaps where no identifiable artifact supports a claim. They must be labelled `original-practice`, not “past exam”.

## Topic-first coverage plan

| topic | observed artifact count | years | source_ids | planned question count | priority |
|---|---:|---|---|---:|---|
| Ch1 Tổng quan: DB/DBMS, file system, schema/instance, data independence | 0 | 2020–21, 2022–23, 2025–26 (indexes/schedules) | UIT-O01, UIT-O02, UIT-O09, UIT-O11, COM-C10 | 4 original + 1 reconstructed | high |
| Ch2 ER / mô hình quan hệ / ER→relation / keys | 0 | 2017–18 through 2024–25 (review indexes) | UIT-O01, TXT-A02, COM-C01, COM-C10, LOC-B02 | 5 original + 1 reconstructed | high |
| Ch3 Đại số quan hệ: translation, union compatibility, division/“tất cả” | 0 | 2022–23, 2024–25 (review material) | UIT-O01, TXT-A03, TECH-A09, COM-C03, COM-C04, LOC-B02 | 6 original + 1 reconstructed | high |
| Ch4 SQL reasoning: NULL, JOIN/SELF JOIN, GROUP BY/HAVING, EXISTS | 2 | 2023–24 | COM-C08, COM-C09, TECH-A02, TECH-A08, LOC-A07 | 6 reconstructed + 4 original | high |
| Ch5 RBTV / impact tables / trigger reasoning | 2 | 2023–24, 2024–25 | COM-C08, COM-C09, TECH-A03, TECH-A04, TECH-A05, TECH-A06 | 4 reconstructed + 4 original | high |
| Ch6 PTH / khóa / chuẩn hóa: closure, candidate keys, minimal cover | 0 | 2022–23, 2025–26 (review/index only) | TXT-A02, COM-C03, COM-C07, LOC-B06, LOC-B16 | 8 original | high |
| Ch6 decomposition: lossless and dependency preservation, 2NF/3NF/BCNF | 0 | 2022–23, 2025–26 (review/index only) | TXT-A02, COM-C07, LOC-B06, LOC-B16 | 6 original | high |
| Mixed exams: schema design → constraints → RA/SQL explanation | 2 | 2023–24 | COM-C08, COM-C09, LOC-A07 | 4 reconstructed + 4 original | medium-high |

## Required page metadata

```yaml
type: verified-artifact # reconstructed-exam-pattern | original-practice
year: 2023-2024
semester: HK1
exam_type: final
source_ids: [COM-C09]
provenance: community-mirror-preview
topics: [sql, joins, group-by]
difficulty: unknown
```

Each question page should contain: Đề bài; knowledge needed; 3–5 “before solution” prompts; answer outline; collapsible detailed solution; why; common errors; variants; meaningful Wikilinks; and a rights/provenance note. Long scans, answer dumps, and verbatim copyrighted text are excluded.

## Editorial rules

- Never infer frequency from curriculum scope or a textbook.
- Preserve `verified-artifact`, `reconstructed-exam-pattern`, and `original-practice` labels in filenames/frontmatter.
- If an accessible local exam file is later recovered, add its exact filename, document fingerprint, and provenance before changing any count.
- Student answers and scripts are pattern evidence only, never authoritative solutions.

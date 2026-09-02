---
title: Lab 03 — truy vấn nâng cao
description: Double NOT EXISTS, tập hợp, ngày tháng và NULL trên fixture training-v1.
type: practice
topics: [advanced-query, division, exists, null, set-operators]
related: [division, double-not-exists, wrong-universal-candidate, not-in-null, unsafe-date-equality]
provenance: verified-artifact
fixture: training-v1
technicalSources: [TECH-MS04]
---
# Lab 03 — truy vấn nâng cao

Fixture dùng đúng các bảng `tr_students`, `tr_courses`, `tr_results`; mã sinh viên mẫu là `S001`. Đây là mô tả tĩnh của script, chưa phải kết quả đã chạy.

```sql
SELECT s.StudentId
FROM dbo.tr_students AS s
WHERE NOT EXISTS (
  SELECT 1 FROM dbo.tr_courses AS c
  WHERE NOT EXISTS (
    SELECT 1 FROM dbo.tr_results AS r
    WHERE r.StudentId = s.StudentId AND r.CourseId = c.CourseId
  )
);
```

Kiểm tra miền ứng viên, NULL và mốc ngày trước khi thêm `DISTINCT`; liên kết ý tưởng là [[division]].

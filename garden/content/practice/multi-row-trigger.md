---
title: Multi-row trigger
description: Mẫu trigger an toàn cho inserted/deleted chứa nhiều dòng.
type: practice
topics: [trigger, multi-row, sql-server]
related: [rbtv-impact, lab-04, scalar-trigger, multi-row-trigger-failure, debugging]
provenance: original-practice
fixture: training-v1
technicalSources: [TECH-MS05]
---
# Multi-row trigger

Fixture trigger contract dùng `tr_departments`, `tr_employees`, `HeadEmployeeId`, `DeptId`, `EmployeeId`. Quy tắc ví dụ: không cho xoá trưởng bộ phận đang được tham chiếu; mọi kiểm tra phải JOIN theo tập `inserted`/`deleted`.

```sql
-- conceptual pattern; STATIC until executed in SQL Server
IF EXISTS (
  SELECT 1
  FROM deleted AS d
  JOIN dbo.tr_departments AS dep ON dep.HeadEmployeeId = d.EmployeeId
)
  THROW 50001, 'Cannot remove a department head', 1;
```

Các case được chấp nhận/từ chối là hợp đồng kiểm thử, không phải runtime claim. Liên kết [[debugging]].

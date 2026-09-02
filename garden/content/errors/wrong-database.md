---
title: Wrong database context
description: Object exists elsewhere but current database is wrong.
type: error
topics: [sql-server, debugging]
related: [setup, invalid-object-column]
provenance: original-practice
---
# Wrong database context

**Symptom:** `Invalid object name` dù bảng đã tạo. **Cause:** SSMS đang ở database khác. **Verify:** `SELECT DB_NAME()` và `sys.tables`. **Fix:** thêm `USE` hoặc chọn đúng context. **Related:** [[setup]].

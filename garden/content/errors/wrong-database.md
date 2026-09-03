---
title: Sai ngữ cảnh cơ sở dữ liệu (Wrong Database Context)
description: Object exists elsewhere but current database is wrong.
type: error
topics: [sql-server, debugging]
related: [setup, invalid-object-column]
provenance: original-practice
---
# Sai ngữ cảnh cơ sở dữ liệu (Wrong Database Context)

**Symptom:** `Invalid object name` dù bảng đã tạo. **Cause:** SSMS đang ở database khác. **Verify:** `SELECT DB_NAME()` và `sys.tables`. **Fix:** thêm `USE` hoặc chọn đúng context. **Related:** [[setup]].

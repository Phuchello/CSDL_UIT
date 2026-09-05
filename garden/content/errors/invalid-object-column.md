---
title: Sai tên bảng hoặc tên cột (Invalid Object / Column)
description: SQL Server không phân giải được tên object hoặc cột.
type: error
topics: [sql-server, schema]
related: [wrong-database, lab-01]
provenance: original-practice
---
# Sai tên bảng hoặc tên cột (Invalid Object or Column)

**Symptom:** Msg 208/207. **Cause:** sai schema, alias hoặc tên cột. **Verify:** `sys.tables`, `sys.columns`, và alias trong câu lệnh. **Fix:** dùng tên canonical; không đoán cột. **Related:** [[wrong-database]].

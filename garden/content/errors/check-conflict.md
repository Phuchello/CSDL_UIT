---
title: CHECK constraint conflict
description: Giá trị không thoả miền nghiệp vụ.
type: error
topics: [constraints, check]
related: [lab-01, debugging]
provenance: original-practice
---
# CHECK constraint conflict

**Symptom:** DML bị rollback. **Cause:** biểu thức CHECK sai với giá trị nhập. **Verify:** đọc định nghĩa constraint trong `sys.check_constraints`. **Fix:** dữ liệu hợp lệ hoặc điều chỉnh constraint có chủ đích. **Related:** [[lab-01]].

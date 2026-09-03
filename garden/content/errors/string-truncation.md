---
title: Lỗi cắt cụt chuỗi dữ liệu (String Truncation)
description: Chuỗi dài hơn kiểu dữ liệu đích.
type: error
topics: [data-types, ddl]
related: [lab-01, debugging]
provenance: original-practice
---
# Lỗi cắt cụt chuỗi dữ liệu (String Truncation)

**Symptom:** Msg 2628. **Cause:** độ dài cột không đủ. **Verify:** `sys.columns.max_length` và `DATALENGTH`. **Fix:** sửa dữ liệu hoặc schema có kiểm soát; không cắt âm thầm. **Related:** [[lab-01]].

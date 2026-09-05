---
title: Trùng lặp khóa chính hoặc UNIQUE (Duplicate Key)
description: Giá trị định danh bị lặp.
type: error
topics: [constraints, keys]
related: [theory/candidate-keys, practice/lab-01]
provenance: original-practice
---
# Trùng lặp khóa chính hoặc UNIQUE (Duplicate Key)

**Symptom:** Msg 2627/2601. **Cause:** key đã tồn tại. **Verify:** SELECT theo key trước khi ghi. **Fix:** dùng key mới hoặc UPSERT có quy tắc rõ. **Related:** [[theory/candidate-keys|Khóa ứng viên]].

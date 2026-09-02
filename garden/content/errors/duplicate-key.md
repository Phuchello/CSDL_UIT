---
title: Duplicate PK or UNIQUE
description: Giá trị định danh bị lặp.
type: error
topics: [constraints, keys]
related: [candidate-keys, lab-01]
provenance: original-practice
---
# Duplicate PK or UNIQUE

**Symptom:** Msg 2627/2601. **Cause:** key đã tồn tại. **Verify:** SELECT theo key trước khi ghi. **Fix:** dùng key mới hoặc UPSERT có quy tắc rõ. **Related:** [[candidate-keys]].

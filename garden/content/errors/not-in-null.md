---
title: Bẫy tập rỗng khi dùng NOT IN với giá trị NULL
description: NULL trong miền loại trừ làm predicate thành UNKNOWN.
type: error
topics: [null, not-in, three-valued-logic]
related: [double-not-exists, null-comparison, division]
provenance: original-practice
---
# Bẫy tập rỗng khi dùng NOT IN với giá trị NULL

**Symptom:** `NOT IN` loại hết kết quả. **Cause:** tập con có NULL. **Verify:** `WHERE key IS NULL` trong subquery. **Fix:** lọc NULL hoặc dùng [[double-not-exists]]. **Related:** [[division]].

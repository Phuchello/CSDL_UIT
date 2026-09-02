---
title: Unsafe date equality
description: So sánh datetime bằng dấu bằng làm mất dòng cùng ngày.
type: error
topics: [dates, datetime, sql-server]
related: [date-conversion, lab-03]
provenance: original-practice
---
# Unsafe date equality

**Symptom:** lọc ngày có kết quả thiếu. **Cause:** datetime chứa time component. **Verify:** xem min/max time. **Fix:** dùng khoảng nửa mở `>= @d AND < DATEADD(day, 1, @d)`. **Related:** [[date-conversion]].

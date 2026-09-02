---
title: Date conversion
description: Literal ngày phụ thuộc format hoặc language.
type: error
topics: [dates, conversion, sql-server]
related: [unsafe-date-equality, lab-03]
provenance: original-practice
---
# Date conversion

**Symptom:** Msg 241. **Cause:** literal mơ hồ. **Verify:** thử `TRY_CONVERT(date, value, style)`. **Fix:** dùng kiểu tham số hoặc ISO unambiguous. **Related:** [[unsafe-date-equality]].

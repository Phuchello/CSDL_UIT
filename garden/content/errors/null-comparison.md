---
title: NULL comparison
description: So sánh với NULL cho UNKNOWN thay vì TRUE.
type: error
topics: [null, three-valued-logic]
related: [not-in-null, unsafe-date-equality]
provenance: verified-artifact
courseEvidence: [UIT-O02]
---
# NULL comparison

**Symptom:** `= NULL` không trả dòng. **Cause:** SQL dùng ba giá trị TRUE/FALSE/UNKNOWN. **Verify:** kiểm tra `IS NULL`/`IS NOT NULL`. **Fix:** dùng predicate NULL đúng ngữ nghĩa. **Related:** [[not-in-null]].

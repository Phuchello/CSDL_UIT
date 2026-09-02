---
title: Scalar subquery returns more than one row
description: Subquery ngữ cảnh vô hướng trả nhiều dòng.
type: error
topics: [subquery, sql]
related: [debugging, lab-03]
provenance: original-practice
---
# Scalar subquery returns more than one row

**Symptom:** Msg 512. **Cause:** giả định uniqueness không đúng. **Verify:** chạy subquery độc lập và đếm dòng. **Fix:** dùng JOIN/EXISTS, aggregate có chủ ý hoặc ràng buộc uniqueness. **Related:** [[debugging]].

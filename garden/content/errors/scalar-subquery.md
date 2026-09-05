---
title: Truy vấn con vô hướng trả về nhiều hơn một dòng (Scalar Subquery)
description: Subquery ngữ cảnh vô hướng trả nhiều dòng.
type: error
topics: [subquery, sql]
related: [debugging, lab-03]
provenance: original-practice
---
# Truy vấn con vô hướng trả về nhiều hơn một dòng (Scalar Subquery)

**Symptom:** Msg 512. **Cause:** giả định uniqueness không đúng. **Verify:** chạy subquery độc lập và đếm dòng. **Fix:** dùng JOIN/EXISTS, aggregate có chủ ý hoặc ràng buộc uniqueness. **Related:** [[debugging]].

---
title: Wrong universal-query candidate domain
description: Miền ứng viên không phải tập cần trả trong câu hỏi “tất cả”.
type: error
topics: [division, universal-query, exists]
related: [division, double-not-exists, lab-03]
provenance: original-practice
---
# Wrong universal-query candidate domain

**Symptom:** câu “tất cả” trả thiếu hoặc thừa. **Cause:** outer query lấy từ bảng yêu cầu thay vì tập ứng viên. **Verify:** viết rõ X và Y trước khi SQL. **Fix:** outer FROM là X, nested required là Y. **Related:** [[division]].

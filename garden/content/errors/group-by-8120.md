---
title: Msg 8120 — GROUP BY
description: Cột không aggregate và cũng không có trong GROUP BY.
type: error
topics: [group-by, aggregation]
related: [lab-02, unexpected-duplicates]
provenance: original-practice
---
# Msg 8120 — GROUP BY

**Symptom:** Msg 8120. **Cause:** SELECT trộn cột chi tiết với aggregate không hợp lệ. **Verify:** đối chiếu từng biểu thức SELECT. **Fix:** thêm vào GROUP BY hoặc aggregate đúng ý nghĩa. **Related:** [[unexpected-duplicates]].

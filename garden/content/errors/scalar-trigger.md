---
title: Scalar trigger variable
description: Trigger đọc một giá trị từ tập inserted/deleted.
type: error
topics: [trigger, multi-row]
related: [multi-row-trigger, multi-row-trigger-failure, rbtv-impact]
provenance: original-practice
---
# Scalar trigger variable

**Symptom:** trigger bỏ sót hoặc xử lý sai batch. **Cause:** `SELECT @x = col FROM inserted` giả định một dòng. **Verify:** kiểm thử hai dòng trong một statement. **Fix:** set-based JOIN/EXISTS trên cả tập. **Related:** [[multi-row-trigger]].

---
title: Lỗi gán biến vô hướng trong Trigger (Scalar Trigger Variable)
description: Trigger đọc một giá trị từ tập inserted/deleted.
type: error
topics: [trigger, multi-row]
related: [multi-row-trigger, multi-row-trigger-failure, rbtv-impact]
provenance: original-practice
---
# Lỗi gán biến vô hướng trong Trigger (Scalar Trigger Variable)

**Symptom:** trigger bỏ sót hoặc xử lý sai batch. **Cause:** `SELECT @x = col FROM inserted` giả định một dòng. **Verify:** kiểm thử hai dòng trong một statement. **Fix:** set-based JOIN/EXISTS trên cả tập. **Related:** [[multi-row-trigger]].

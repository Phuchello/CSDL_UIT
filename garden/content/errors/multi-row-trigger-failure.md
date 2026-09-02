---
title: Multi-row trigger failure
description: Logic trigger đúng với một dòng nhưng sai với batch.
type: error
topics: [trigger, multi-row, inserted, deleted]
related: [multi-row-trigger, scalar-trigger, debugging]
provenance: original-practice
---
# Multi-row trigger failure

**Symptom:** batch INSERT/UPDATE vượt ràng buộc. **Cause:** kiểm tra theo dòng hoặc biến scalar. **Verify:** replay statement nhiều dòng, đọc inserted/deleted. **Fix:** aggregate/JOIN theo tập và rollback toàn statement khi vi phạm. **Related:** [[debugging]].

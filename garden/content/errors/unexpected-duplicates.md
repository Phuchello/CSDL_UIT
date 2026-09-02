---
title: Unexpected duplicate rows
description: JOIN hoặc bag semantics làm số dòng tăng.
type: error
topics: [join, duplicates, aggregation]
related: [lab-02, group-by-8120, relational-algebra]
provenance: original-practice
---
# Unexpected duplicate rows

**Symptom:** một đối tượng xuất hiện nhiều lần. **Cause:** bội số 1-n hoặc điều kiện JOIN thiếu. **Verify:** đếm trước/sau JOIN theo key. **Fix:** nối đúng key, aggregate ở đúng grain; chỉ dùng DISTINCT khi lặp là hợp lệ. **Related:** [[group-by-8120]].

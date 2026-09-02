---
title: Foreign-key conflict
description: DML vi phạm quan hệ tham chiếu.
type: error
topics: [constraints, foreign-key]
related: [lab-01, rbtv-impact]
provenance: original-practice
---
# Foreign-key conflict

**Symptom:** INSERT/UPDATE/DELETE bị từ chối. **Cause:** parent thiếu hoặc child còn tham chiếu. **Verify:** JOIN tìm orphan/reference. **Fix:** đúng thứ tự DML hoặc sửa khóa hợp lệ. **Related:** [[rbtv-impact]].

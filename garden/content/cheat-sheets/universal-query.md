---
title: Universal query cheat sheet
description: Bốn bước kiểm tra câu hỏi “tất cả”.
type: cheatsheet
topics: [division, exists]
related: [division, double-not-exists, wrong-universal-candidate]
provenance: original-practice
---
# Universal query

1. Chọn miền ứng viên X. 2. Liệt kê miền yêu cầu Y. 3. Tìm X không có Y thiếu bằng double `NOT EXISTS`. 4. Kiểm tra Y rỗng, NULL và duplicate. Liên kết [[division]].

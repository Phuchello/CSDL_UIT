---
title: Candidate keys
description: Superkey tối thiểu và cách kiểm tra bằng bao đóng.
type: theory
topics: [candidate-keys, keys, closure]
related: [functional-dependencies, closure, minimal-cover, 3nf]
provenance: verified-artifact
courseEvidence: [UIT-O05]
---
# Candidate keys

Candidate key là superkey không có thuộc tính thừa. Quy trình: tìm thuộc tính bắt buộc ở mọi khóa, thử bổ sung, tính closure, rồi loại tối thiểu. Một quan hệ có thể có nhiều khóa ứng viên; chọn một làm PK không xoá các khóa thay thế.

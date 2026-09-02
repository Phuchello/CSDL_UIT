---
title: Attribute closure
description: Thuật toán tính X+ để kiểm tra suy dẫn và khóa.
type: theory
topics: [closure, functional-dependencies]
related: [candidate-keys, minimal-cover, 3nf]
provenance: verified-artifact
courseEvidence: [UIT-O05]
---
# Attribute closure

Bắt đầu `X+ = X`; lặp các FD có vế trái nằm trong closure và thêm vế phải cho đến khi ổn định. Nếu `X+` chứa toàn bộ thuộc tính thì `X` là superkey; kiểm tra tối thiểu để có candidate key. Xem [[candidate-keys]].

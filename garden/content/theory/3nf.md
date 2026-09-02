---
title: 3NF
description: Điều kiện 3NF và phân biệt với BCNF.
type: theory
topics: [3nf, normalization]
related: [bcnf, lossless-decomposition, dependency-preservation, candidate-keys]
provenance: verified-artifact
courseEvidence: [UIT-O05]
---
# 3NF

Với mọi FD không tầm thường `X → A`, 3NF yêu cầu `X` là superkey **hoặc** `A` là thuộc tính prime (nằm trong một candidate key). Vì vậy 3NF có thể giữ dependency preservation mà BCNF không luôn giữ được.

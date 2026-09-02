---
title: BCNF
description: Điều kiện mạnh hơn của BCNF và cách phát hiện FD vi phạm.
type: theory
topics: [bcnf, normalization]
related: [3nf, lossless-decomposition, functional-dependencies]
provenance: verified-artifact
courseEvidence: [UIT-O05]
---
# BCNF

BCNF yêu cầu với mọi FD không tầm thường `X → A`, `X` phải là superkey. Mọi BCNF đều là 3NF; chiều ngược lại không đúng khi vế phải là thuộc tính prime nhưng vế trái chưa là superkey.

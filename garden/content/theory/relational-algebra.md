---
title: Relational algebra
description: Các toán tử chọn, chiếu, nối và phép tập làm cơ sở cho SQL.
type: theory
topics: [relational-algebra, selection, projection, join]
related: [division, double-not-exists, exam-patterns/relational-algebra]
provenance: verified-artifact
courseEvidence: [UIT-O02]
---
# Relational algebra

Chọn `σ` lọc bộ; chiếu `π` chọn thuộc tính; nối ghép bộ theo điều kiện; hợp, giao, hiệu yêu cầu union-compatible. Chiếu có thể loại bản sao theo ngữ nghĩa tập.

SQL thường biểu diễn cùng ý định nhưng có bag semantics, vì vậy [[unexpected-duplicates]] và `DISTINCT` cần được cân nhắc.

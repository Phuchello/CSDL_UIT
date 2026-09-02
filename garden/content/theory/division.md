---
title: Division — “tất cả”
description: Mẫu phép chia cho câu hỏi mọi đối tượng đều thoả điều kiện.
type: theory
topics: [division, universal-query]
related: [double-not-exists, lab-03, wrong-universal-candidate, universal-query]
provenance: verified-artifact
courseEvidence: [UIT-O03]
---
# Division — “tất cả”

Với `R(X,Y)` và `S(Y)`, `R ÷ S` trả các `X` ghép với **mọi** `Y` trong `S`. Trong SQL, tư duy tương đương là tìm ứng viên không có phản ví dụ:

```sql
SELECT c.CustomerId
FROM Customers AS c
WHERE NOT EXISTS (
  SELECT 1 FROM RequiredItems AS r
  WHERE NOT EXISTS (
    SELECT 1 FROM Purchases AS p
    WHERE p.CustomerId = c.CustomerId AND p.ItemId = r.ItemId
  )
);
```

Miền ứng viên phải là tập cần trả; đọc [[wrong-universal-candidate]] trước khi tối ưu.

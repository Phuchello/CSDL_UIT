---
title: 3NF
description: Điều kiện dạng chuẩn 3 (Third Normal Form), phân biệt với 2NF và BCNF, và tính chất bảo toàn phụ thuộc hàm.
type: theory
topics: [3nf, normalization]
related: [theory/bcnf, theory/lossless-decomposition, theory/candidate-keys, theory/functional-dependencies]
provenance: verified-artifact
courseEvidence: [UIT-O05, LOC-LEC-LONG-CH06]
---
# 3NF (Third Normal Form)

Dạng chuẩn 3 (3NF) giải quyết triệt để vấn đề phụ thuộc bắc cầu (transitive dependency) của các thuộc tính không khóa, đồng thời đảm bảo luôn tồn tại phép phân rã bảo toàn cả thông tin lẫn phụ thuộc hàm.

## 1. Định nghĩa hình thức

Lược đồ quan hệ $R$ với tập phụ thuộc hàm $F$ đạt **Dạng chuẩn 3 (3NF)** khi và chỉ khi với mọi phụ thuộc hàm không tầm thường $X \rightarrow A \in F^+$ ($A \notin X$), ít nhất một trong hai điều kiện sau thỏa mãn:
1. $X$ là một siêu khóa (superkey) của $R$.
2. $A$ là một thuộc tính khóa (prime attribute — tức $A$ thuộc vào ít nhất một [[theory/candidate-keys|khóa ứng viên]] của $R$).

*Lưu ý:* Định nghĩa trên tự động bao hàm dạng chuẩn 2NF (không tồn tại phụ thuộc bộ phận vào khóa con).

## 2. Ý nghĩa và điều kiện cứu vãn

Điều kiện thứ hai ("$A$ là thuộc tính khóa") là đặc trưng phân biệt quan trọng nhất giữa 3NF và [[theory/bcnf|BCNF]]:
- Nếu vế trái $X$ không phải là siêu khóa, 3NF vẫn chấp nhận phụ thuộc hàm đó nếu thuộc tính vế phải $A$ là thuộc tính khóa.
- Nhờ điều kiện này, mọi lược đồ quan hệ luôn có thể phân rã thành tập các quan hệ con đạt 3NF vừa **bảo toàn thông tin nối (lossless join)** vừa **bảo toàn phụ thuộc hàm (dependency preservation)**.

## 3. Ví dụ kinh điển: Đạt 3NF nhưng vi phạm BCNF

Xét quan hệ $R(A, B, C)$ với tập phụ thuộc hàm $F = \{AB \rightarrow C, C \rightarrow B\}$:
- **Tập khóa ứng viên:** Tính bao đóng ta tìm được 2 khóa: $Key_1 = AB$, $Key_2 = AC$.
- **Tập thuộc tính khóa:** $\{A, B, C\}$ (mọi thuộc tính đều là thuộc tính khóa).
- **Kiểm tra từng FD:**
  - $AB \rightarrow C$: Vế trái $AB$ là siêu khóa $\rightarrow$ Thỏa mãn điều kiện 1.
  - $C \rightarrow B$: Vế trái $C$ không phải siêu khóa, nhưng vế phải $B$ là thuộc tính khóa (thuộc khóa $AB$) $\rightarrow$ Thỏa mãn điều kiện 2.
- **Kết luận:** Quan hệ $R$ đạt **3NF**. Tuy nhiên, $R$ vi phạm [[theory/bcnf|BCNF]] vì tại $C \rightarrow B$, $C$ không phải là siêu khóa.

Xem quy trình phân rã tại [[theory/lossless-decomposition|Phân rã bảo toàn thông tin]] và bảng tổng hợp quy tắc tại [[cheat-sheets/normalization|Normalization cheat sheet]].

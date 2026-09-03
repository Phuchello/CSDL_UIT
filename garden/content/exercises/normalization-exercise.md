---
title: "Bài tập rèn luyện — Phân tích & Chuẩn hóa lược đồ (Normalization)"
description: Bài tập phân tích bao đóng, tìm khóa ứng viên, xác định dạng chuẩn 3NF/BCNF và phân rã.
type: exercise
topics: [closure, candidate-keys, 3nf, bcnf]
related: [theory/closure, theory/candidate-keys, theory/minimal-cover, theory/3nf, theory/bcnf, theory/lossless-decomposition]
provenance: original-practice
---
# Bài tập rèn luyện — Phân tích & Chuẩn hóa lược đồ (Normalization)

## Đề bài mẫu chuẩn mực
Cho lược đồ quan hệ $R(A, B, C, D, E)$ với tập phụ thuộc hàm $F = \{A \rightarrow BC, CD \rightarrow E, B \rightarrow D, E \rightarrow A\}$.
1. Tính bao đóng của thuộc tính $A$.
2. Tìm tất cả các [[theory/candidate-keys|khóa ứng viên]] của quan hệ $R$.
3. Xác định dạng chuẩn cao nhất của $R$ (giữa [[theory/3nf|3NF]] và [[theory/bcnf|BCNF]]).

## Lời giải chi tiết từng bước

### 1. Tính bao đóng $\{A\}^+$
Áp dụng thuật toán [[theory/closure|Bao đóng thuộc tính]]:
- Vòng 0: $A^{(0)} = \{A\}$
- Vòng 1: Áp dụng $A \rightarrow BC \implies A^{(1)} = \{A, B, C\}$
- Vòng 2: Áp dụng $B \rightarrow D \implies A^{(2)} = \{A, B, C, D\}$
- Vòng 3: Áp dụng $CD \rightarrow E \implies A^{(3)} = \{A, B, C, D, E\} = R$
- Vòng 4: Không còn thuộc tính mới $\rightarrow$ Dừng.

**Kết luận:** $\{A\}^+ = ABCDE = R$. Do đó, $A$ là một siêu khóa của $R$. Vì $A$ là thuộc tính đơn lẻ nên $A$ là một khóa ứng viên.

### 2. Tìm tất cả khóa ứng viên
Phân loại tập thuộc tính theo $L, R, N, LR$:
- $L = \emptyset$ (không có thuộc tính nào chỉ ở vế trái).
- $R = \emptyset$ (không có thuộc tính nào chỉ ở vế phải).
- $N = \emptyset$.
- $LR = \{A, B, C, D, E\}$.

Dựa vào các FD:
- Từ $E \rightarrow A$, ta có $E^+ = (E \rightarrow A) \cup A^+ = ABCDE \implies E$ là khóa ứng viên thứ 2.
- Từ $B \rightarrow D$, xét $BC$: $BC \rightarrow BCD \rightarrow BCDE \rightarrow A \implies (BC)^+ = ABCDE \implies BC$ là khóa ứng viên thứ 3.
- Xét $CD$: $CD \rightarrow CDE \rightarrow A \implies (CD)^+ = ABCDE \implies CD$ là khóa ứng viên thứ 4.

**Tập các khóa ứng viên:** $\{A, E, BC, CD\}$.
**Tập thuộc tính khóa (Prime):** $\{A, B, C, D, E\}$ (mọi thuộc tính đều là thuộc tính khóa).

### 3. Xác định dạng chuẩn cao nhất
- Xét $B \rightarrow D$: Vế trái $B$ có $B^+ = BD \neq R \implies B$ không phải là siêu khóa.
  - Tuy nhiên, vế phải $D$ là thuộc tính khóa (thuộc khóa $CD$).
  - Do đó $B \rightarrow D$ thỏa mãn điều kiện cứu vãn của 3NF.
- Tương tự, $CD \rightarrow E$: $CD$ là khóa ứng viên $\rightarrow$ thỏa mãn.
- **Kết luận:** Quan hệ $R$ đạt **3NF** nhưng **không đạt BCNF** (do $B \rightarrow D$ có vế trái không phải siêu khóa).

Xem thêm phương pháp phân rã tại [[theory/lossless-decomposition|Phân rã không mất mát thông tin]] và bảng tra cứu tại [[cheat-sheets/normalization|Bảng tra chuẩn hóa dữ liệu]].

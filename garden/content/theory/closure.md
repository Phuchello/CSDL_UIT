---
title: Bao đóng thuộc tính (Attribute Closure)
description: Định nghĩa hình thức của bao đóng thuộc tính, thuật toán lặp điểm bất động, dry-run từng bước và 3 ứng dụng thực chiến.
type: theory
topics: [closure, functional-dependency, candidate-keys, normalization]
related: [theory/functional-dependencies, theory/candidate-keys, theory/minimal-cover, theory/3nf, theory/bcnf]
provenance: verified-artifact
courseEvidence: [UIT-O02, LOC-LEC-LONG-CH06]
---
# Bao đóng thuộc tính (Attribute Closure $X^+$)

Bao đóng của một tập thuộc tính là công cụ tính toán cơ bản và hiệu quả nhất trong lý thuyết chuẩn hóa cơ sở dữ liệu quan hệ. Nhờ thuật toán bao đóng, ta có thể kiểm tra một phụ thuộc hàm có được suy dẫn hay không mà không cần áp dụng thủ công hệ tiên đề Armstrong.

## 1. Định nghĩa toán học hình thức

Cho lược đồ quan hệ $R(U)$, tập phụ thuộc hàm $F$ và một tập con thuộc tính $X \subseteq U$.
**Bao đóng của tập thuộc tính $X$ đối với $F$**, ký hiệu là $X^+_F$ (hoặc viết gọn là $X^+$), là tập hợp tất cả các thuộc tính $A \in U$ có thể được suy dẫn logic từ $X$ thông qua $F$:

$$X^+_F = \{A \in U \mid F \models X \rightarrow A\}$$

- **Tính chất cơ bản:**
  1. $X \subseteq X^+$ (mọi thuộc tính ban đầu luôn nằm trong bao đóng theo luật phản xạ).
  2. Nếu $X \subseteq Y$ thì $X^+ \subseteq Y^+$ (tính đơn điệu).
  3. $(X^+)^+ = X^+$ (tính lũy đẳng - idempotent).

## 2. Thuật toán lặp tìm điểm bất động (Fixed-point Iteration Algorithm)

Thuật toán tính $X^+$ có độ phức tạp thời gian đa thức $O(|F| \cdot |U|)$:

- **Bước 1 (Khởi tạo):** Đặt tập kết quả $X^{(0)} = X$.
- **Bước 2 (Lặp):** Tại vòng lặp thứ $k+1$, duyệt qua từng phụ thuộc hàm $V \rightarrow W \in F$:
  $$\text{Nếu } V \subseteq X^{(k)} \implies X^{(k+1)} = X^{(k)} \cup W$$
- **Bước 3 (Điều kiện dừng):** Thuật toán dừng lại khi không có thuộc tính mới nào được thêm vào ($X^{(k+1)} = X^{(k)}$) hoặc khi $X^{(k)} = U$. Đặt $X^+ = X^{(k)}$.

## 3. Bảng Dry-run tính toán minh họa chi tiết từng bước

Cho lược đồ $R(A, B, C, D, E)$ với tập phụ thuộc hàm $F$:
$$F = \{A \rightarrow BC, \; CD \rightarrow E, \; B \rightarrow D, \; E \rightarrow A\}$$
Tính bao đóng $\{A\}^+$:

| Vòng lặp | $X^+$ hiện tại | Phụ thuộc hàm thỏa mãn vế trái | Thuộc tính mới bổ sung |
| :---: | :---: | :---: | :---: |
| **0** | $\{A\}$ | Khởi tạo ban đầu | $-$ |
| **1** | $\{A, B, C\}$ | $A \rightarrow BC$ (do $A \subseteq \{A\}$) | $B, C$ |
| **2** | $\{A, B, C, D\}$ | $B \rightarrow D$ (do $B \subseteq \{A, B, C\}$) | $D$ |
| **3** | $\{A, B, C, D, E\}$ | $CD \rightarrow E$ (do $CD \subseteq \{A, B, C, D\}$) | $E$ |
| **4** | $\{A, B, C, D, E\}$ | Đã chứa toàn bộ thuộc tính của $R$ | Dừng |

**Kết luận:** $\{A\}^+ = ABCDE = U$. Vì bao đóng của $A$ chứa toàn bộ thuộc tính của $R$, nên $A$ là một siêu khóa (superkey) của lược đồ $R$.

## 4. Ba ứng dụng thực chiến trong phân tích CSDL

Thuật toán bao đóng thuộc tính được ứng dụng trong 3 bài toán sống còn:
1. **Kiểm tra phụ thuộc hàm $X \rightarrow Y$ có thuộc $F^+$ không:**
   - Tính $X^+$.
   - Nếu $Y \subseteq X^+$ thì $X \rightarrow Y$ đúng ($F \models X \rightarrow Y$). Ngược lại thì sai.
2. **Kiểm tra một tập thuộc tính $K$ có phải là Siêu khóa (Superkey) không:**
   - Tính $K^+$.
   - Nếu $K^+ = U$ thì $K$ là một siêu khóa.
3. **Tìm tất cả các Khóa ứng viên (Candidate Keys) và Phủ tối thiểu:**
   - Là bước cốt lõi trong thuật toán tìm khóa tối thiểu và kiểm tra thuộc tính dư thừa bên vế trái khi tìm phủ tối thiểu.

Xem chi tiết thuật toán tìm toàn bộ khóa tại [[theory/candidate-keys|Khóa ứng viên]], thuật toán rút gọn [[theory/minimal-cover|Phủ tối thiểu]], và áp dụng đánh giá dạng chuẩn tại [[theory/3nf|3NF]] và [[theory/bcnf|BCNF]].

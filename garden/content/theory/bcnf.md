---
title: BCNF
description: Điều kiện Dạng chuẩn Boyce-Codd (BCNF), thuật toán kiểm tra siêu khóa và bài toán đánh đổi bảo toàn phụ thuộc hàm.
type: theory
topics: [bcnf, normalization]
related: [theory/3nf, theory/lossless-decomposition, theory/candidate-keys, theory/functional-dependencies]
provenance: verified-artifact
courseEvidence: [UIT-O05, LOC-LEC-LONG-CH06]
---
# BCNF (Boyce-Codd Normal Form)

Dạng chuẩn Boyce-Codd (BCNF) là phiên bản chuẩn hóa chặt chẽ hơn của [[theory/3nf|3NF]], loại bỏ hoàn toàn mọi dị thường cập nhật phát sinh từ việc các thuộc tính phụ thuộc vào các tập con không phải là siêu khóa.

## 1. Định nghĩa hình thức

Lược đồ quan hệ $R$ với tập phụ thuộc hàm $F$ đạt **Dạng chuẩn Boyce-Codd (BCNF)** khi và chỉ khi:
Với mọi phụ thuộc hàm không tầm thường $X \rightarrow A \in F^+$ ($A \notin X$), $X$ bắt buộc phải là một **siêu khóa (superkey)** của $R$.

Nói cách khác: Vế trái của mọi phụ thuộc hàm không tầm thường bắt buộc phải chứa một [[theory/candidate-keys|khóa ứng viên]].

## 2. So sánh BCNF và 3NF: Sự đánh đổi lý thuyết

- **Tính bao hàm:** Mọi lược đồ đạt BCNF chắc chắn đạt 3NF. Ngược lại, một lược đồ đạt 3NF có thể vi phạm BCNF nếu tồn tại FD $X \rightarrow A$ trong đó $A$ là thuộc tính khóa nhưng $X$ không phải là siêu khóa.
- **Sự đánh đổi cốt lõi (Trade-off):**
  - Về 3NF: Luôn luôn tồn tại phép phân rã vừa **bảo toàn thông tin nối** vừa **bảo toàn phụ thuộc hàm**.
  - Về BCNF: Luôn luôn tồn tại phép phân rã bảo toàn thông tin nối, nhưng **không thể đảm bảo luôn bảo toàn phụ thuộc hàm**. Đôi khi ta buộc phải chọn giữa việc chấp nhận dư thừa ở mức 3NF hoặc mất khả năng kiểm tra phụ thuộc hàm nội tại trong từng bảng ở mức BCNF.

## 3. Ví dụ kiểm tra và thuật toán phân rã

Xét lược đồ $R(A, B, C)$ với $F = \{AB \rightarrow C, C \rightarrow B\}$:
1. **Tìm khóa:** Các khóa ứng viên là $AB$ và $AC$.
2. **Kiểm tra BCNF:**
   - $AB \rightarrow C$: $AB$ là khóa $\rightarrow$ Thỏa BCNF.
   - $C \rightarrow B$: $C^+ = BC \neq ABC \rightarrow C$ không phải là siêu khóa $\rightarrow$ Vi phạm BCNF!
3. **Phân rã về BCNF:**
   - Tách quan hệ con $R_1(C, B)$ theo phụ thuộc hàm vi phạm $C \rightarrow B$ (với khóa $C$).
   - Tạo quan hệ con còn lại $R_2(C, A) = R \setminus (\{B\})$.
   - Kiểm tra tính bảo toàn thông tin: $R_1 \cap R_2 = C$, là khóa của $R_1 \rightarrow$ Phân rã là **nối không mất mát thông tin (lossless join)**.
   - Kiểm tra phụ thuộc hàm: FD $AB \rightarrow C$ bị phân tán trên cả hai bảng $\rightarrow$ **Mất bảo toàn phụ thuộc hàm**.

Xem hướng dẫn thuật toán chi tiết tại [[theory/lossless-decomposition|Phân rã bảo toàn thông tin]] và bài tập thực hành tại [[exercises/normalization-exercise|Bài tập chuẩn hóa]].

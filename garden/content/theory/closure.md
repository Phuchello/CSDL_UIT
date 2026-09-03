---
title: Attribute closure
description: Thuật toán tính bao đóng thuộc tính X+ theo tập phụ thuộc hàm F và các ứng dụng kiểm tra suy dẫn, siêu khóa.
type: theory
topics: [closure, functional-dependencies]
related: [theory/candidate-keys, theory/minimal-cover, theory/3nf, theory/functional-dependencies]
provenance: verified-artifact
courseEvidence: [UIT-O05, LOC-LEC-LONG-CH06]
---
# Attribute closure (Bao đóng của tập thuộc tính $X^+$)

Bao đóng của tập thuộc tính là công cụ giải tích nền tảng nhất trong lý thuyết thiết kế cơ sở dữ liệu quan hệ, cho phép kiểm tra tính đúng đắn của phụ thuộc hàm và tìm khóa với độ phức tạp đa thức thay vì phải tính toán bao đóng tập phụ thuộc hàm $F^+$ với chi phí cấp số mũ.

## 1. Định nghĩa hình thức

Cho lược đồ quan hệ $R(U)$, tập phụ thuộc hàm $F$ và tập thuộc tính con $X \subseteq U$.
**Bao đóng của $X$ theo $F$**, ký hiệu là $X^+_F$ (hoặc ngắn gọn là $X^+$), là tập hợp toàn bộ các thuộc tính $A \in U$ có thể được suy dẫn logic từ $X$ dựa trên $F$:
$$X^+ = \{A \in U \mid F \vdash X \rightarrow A\}$$

## 2. Thuật toán tính bao đóng chuẩn mực

Thuật toán lặp điểm bất động (fixed-point iteration) thực hiện như sau:

1. **Khởi tạo:** Đặt $closX = X$.
2. **Vòng lặp:** Duyệt qua từng phụ thuộc hàm $Y \rightarrow Z \in F$:
   - Nếu $Y \subseteq closX$: Cập nhật $closX = closX \cup Z$.
3. **Điều kiện dừng:** Lặp lại Bước 2 cho đến khi qua một lượt duyệt toàn bộ tập $F$ mà kích thước tập $closX$ không tăng thêm.
4. **Kết quả:** Trả về $X^+ = closX$.

## 3. Các ứng dụng cốt lõi của bao đóng $X^+$

- **Kiểm tra tính suy dẫn của một FD bất kỳ:** Muốn kiểm tra $X \rightarrow Y$ có thỏa mãn trong $F^+$ hay không, ta tính $X^+$ và kiểm tra điều kiện $Y \subseteq X^+$.
- **Kiểm tra Siêu khóa (Superkey):** Nếu $X^+ = U$ thì $X$ chắc chắn là một siêu khóa của quan hệ $R$.
- **Xác định Khóa ứng viên (Candidate Keys):** Dùng thuật toán rẽ nhánh kết hợp $X^+$ để tìm siêu khóa tối thiểu (xem chi tiết tại [[theory/candidate-keys|Khóa ứng viên]]).
- **Tìm Phủ tối thiểu ($F_c$):** Dùng để kiểm tra và loại bỏ thuộc tính dư thừa ở vế trái cũng như các phụ thuộc hàm dư thừa (xem [[theory/minimal-cover|Phủ tối thiểu]]).

Cơ sở lý thuyết suy dẫn dựa trên hệ tiên đề xem tại [[theory/functional-dependencies|Phụ thuộc hàm & Tiên đề Armstrong]].

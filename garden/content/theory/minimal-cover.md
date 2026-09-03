---
title: Phủ tối thiểu (Minimal Cover)
description: Phủ tối thiểu (Canonical Cover Fc), 3 bước chuẩn hóa vế phải, loại thuộc tính dư vế trái và loại phụ thuộc hàm dư thừa.
type: theory
topics: [minimal-cover, functional-dependencies]
related: [theory/closure, theory/candidate-keys, theory/3nf, theory/lossless-decomposition, theory/functional-dependencies]
provenance: verified-artifact
courseEvidence: [UIT-O05, LOC-LEC-LONG-CH06]
---
# Phủ tối thiểu của tập phụ thuộc hàm (Minimal Cover $F_c$)

Phủ tối thiểu (hay Phủ chính tắc - Canonical Cover $F_c$) là dạng rút gọn chuẩn tắc của tập phụ thuộc hàm $F$, loại bỏ hoàn toàn mọi dư thừa về cả thuộc tính lẫn phụ thuộc hàm mà vẫn bảo toàn trọn vẹn ngữ nghĩa bao đóng $F_c^+ = F^+$.

## 1. Điều kiện hình thức của phủ tối thiểu

Tập phụ thuộc hàm $F_c$ được gọi là phủ tối thiểu của $F$ khi và chỉ khi thỏa mãn đồng thời 3 điều kiện:
1. **Đơn thuộc tính vế phải (Singleton RHS):** Mọi phụ thuộc hàm thuộc $F_c$ đều có vế phải gồm đúng 1 thuộc tính: $X \rightarrow A$ với $A \in U$.
2. **Không dư thừa thuộc tính vế trái (Left-irreducible):** Không tồn tại $X \rightarrow A \in F_c$ và $Y \subset X$ sao cho $(F_c \setminus \{X \rightarrow A\} \cup \{Y \rightarrow A\}) \equiv F_c$.
3. **Không dư thừa phụ thuộc hàm (Non-redundant):** Không tồn tại bất kỳ phụ thuộc hàm $X \rightarrow A \in F_c$ nào sao cho $(F_c \setminus \{X \rightarrow A\}) \equiv F_c$.

## 2. Thuật toán 3 bước tìm $F_c$

Quá trình tìm $F_c$ phải tuân thủ nghiêm ngặt thứ tự 3 bước sau:

### Bước 1: Phân rã vế phải thành đơn thuộc tính
Áp dụng hệ quả phân rã của [[theory/functional-dependencies|Tiên đề Armstrong]], tách mọi phụ thuộc hàm có vế phải phức thành các phụ thuộc hàm đơn:
$$X \rightarrow \{A_1, A_2, \dots, A_k\} \implies X \rightarrow A_1, X \rightarrow A_2, \dots, X \rightarrow A_k$$

### Bước 2: Loại bỏ thuộc tính dư thừa ở vế trái
Với mỗi phụ thuộc hàm $X \rightarrow A$ trong đó $X$ có từ hai thuộc tính trở lên:
- Với mỗi thuộc tính $B \in X$, đặt tập con rút gọn $Y = X \setminus \{B\}$.
- Tính [[theory/closure|bao đóng]] $Y^+$ dựa trên tập phụ thuộc hàm hiện tại.
- **Nếu $A \in Y^+$:** Thuộc tính $B$ là dư thừa. Ta thay thế $X \rightarrow A$ bằng $Y \rightarrow A$.
- Lặp lại cho đến khi vế trái không còn thuộc tính dư thừa nào.

### Bước 3: Loại bỏ phụ thuộc hàm dư thừa
Xét từng phụ thuộc hàm $f = (X \rightarrow A)$ trong tập phụ thuộc hàm hiện tại:
- Giả định loại bỏ $f$, đặt tập còn lại là $G = F \setminus \{f\}$.
- Tính bao đóng $X^+_G$ của $X$ theo tập phụ thuộc hàm $G$.
- **Nếu $A \in X^+_G$:** Phụ thuộc hàm $f$ là dư thừa (vì nó có thể được suy dẫn từ các phụ thuộc hàm còn lại) $\rightarrow$ loại bỏ $f$ vĩnh viễn khỏi tập.
- **Nếu $A \notin X^+_G$:** Giữ nguyên $f$.

*Lưu ý:* Thứ tự duyệt các phụ thuộc hàm ở Bước 3 có thể cho ra các tập $F_c$ có hình thức khác nhau, nhưng tất cả đều có bao đóng tương đương $F^+$.

Xem ứng dụng tìm phủ tối thiểu trong tổng hợp dạng chuẩn [[theory/3nf|3NF]] và bài tập mẫu tại [[exercises/normalization-exercise|Bài tập chuẩn hóa]].

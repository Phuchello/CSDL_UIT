---
title: Bảng tra chuẩn hóa dữ liệu (Normalization)
description: Bảng tóm lược và quy trình kiểm tra tuần tự từ Phụ thuộc hàm đến dạng chuẩn BCNF.
type: cheatsheet
topics: [normalization, fd]
related: [theory/closure, theory/candidate-keys, theory/minimal-cover, theory/3nf, theory/bcnf, theory/lossless-decomposition]
provenance: original-practice
---
# Bảng tra chuẩn hóa dữ liệu (Normalization Cheat Sheet)

Bảng tra nhanh quy trình chuẩn hóa quan hệ trong phòng thi và bài tập:

1. **Kiểm tra Phụ thuộc hàm (FD)**: Dùng 6 tiên đề Armstrong (Phản xạ, Tăng trưởng, Bắc cầu, Hợp, Tách, Giả bắc cầu) xem tại [[theory/functional-dependencies|Phụ thuộc hàm]].
2. **Tính bao đóng ($X^+$)**: Khởi tạo $X^+ = X$, duyệt các FD lặp cho đến khi tập thuộc tính không đổi (xem [[theory/closure|Thuật toán bao đóng]]).
3. **Tìm khóa ứng viên**: Phân loại thuộc tính thành $L, R, N, LR$. Tập bắt buộc là $L \cup N$. Nếu $(L \cup N)^+ = R$ thì đó là khóa duy nhất, ngược lại rẽ nhánh kết hợp với $LR$ (xem [[theory/candidate-keys|Khóa ứng viên]]).
4. **Tìm phủ tối thiểu ($F_c$)**: Bước 1: Tách vế phải thành đơn thuộc tính. Bước 2: Loại thuộc tính dư vế trái. Bước 3: Loại phụ thuộc hàm dư thừa (xem [[theory/minimal-cover|Phủ tối thiểu]]).
5. **Kiểm định dạng chuẩn**:
   - [[theory/3nf|3NF]]: Mọi FD $X \rightarrow A$ không tầm thường đều có $X$ là siêu khóa HOẶC $A$ là thuộc tính khóa.
   - [[theory/bcnf|BCNF]]: Mọi FD $X \rightarrow A$ không tầm thường đều bắt buộc $X$ phải là siêu khóa.
6. **Phân rã (Decomposition)**: Áp dụng thuật toán phân rã bảo toàn thông tin nối (xem [[theory/lossless-decomposition|Phân rã bảo toàn thông tin]]).

Luyện tập bài tập mẫu có lời giải chi tiết tại [[exercises/normalization-exercise|Bài tập chuẩn hóa]].

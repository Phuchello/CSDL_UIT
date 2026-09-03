---
title: Lý thuyết (Theory)
description: Các nút lý thuyết cốt lõi của cơ sở dữ liệu quan hệ và chuẩn hóa.
type: theory
topics: [theory]
related: [theory/relational-model, theory/relational-algebra, theory/functional-dependencies, theory/3nf, theory/bcnf]
---
# Lý thuyết cơ sở dữ liệu (Theory)

Hệ thống lý thuyết nền tảng IT004 được cấu trúc theo lộ trình học thuật chặt chẽ:

1. **Nền tảng quan hệ**: [[theory/relational-model|Mô hình quan hệ]] $\rightarrow$ [[theory/relational-algebra|Đại số quan hệ]] $\rightarrow$ [[theory/division|Phép chia hình thức]].
2. **Kỹ thuật truy vấn tương đương**: [[theory/double-not-exists|Kỹ thuật Double NOT EXISTS]] và [[theory/rbtv-impact|Bảng tầm ảnh hưởng RBTV]].
3. **Lý thuyết thiết kế và chuẩn hóa**:
   - [[theory/functional-dependencies|Phụ thuộc hàm & Tiên đề Armstrong]]
   - [[theory/closure|Thuật toán bao đóng thuộc tính $X^+$]]
   - [[theory/candidate-keys|Tìm toàn bộ khóa ứng viên (Candidate Keys)]]
   - [[theory/minimal-cover|Tìm phủ tối thiểu (Minimal Cover $F_c$)]]
   - [[theory/3nf|Dạng chuẩn 3NF]] $\rightarrow$ [[theory/bcnf|Dạng chuẩn BCNF]] $\rightarrow$ [[theory/lossless-decomposition|Phân rã bảo toàn thông tin nối]].

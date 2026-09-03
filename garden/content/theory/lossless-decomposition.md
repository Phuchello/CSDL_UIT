---
title: Lossless decomposition
description: Phân rã không mất mát thông tin nối (Lossless-Join Decomposition) và bảo toàn phụ thuộc hàm (Dependency Preservation).
type: theory
topics: [lossless, dependency-preservation, normalization]
related: [theory/3nf, theory/bcnf, theory/minimal-cover, theory/functional-dependencies]
provenance: verified-artifact
courseEvidence: [UIT-O05, LOC-LEC-LONG-CH06]
---
# Lossless decomposition (Phân rã bảo toàn thông tin nối)

Khi chuẩn hóa lược đồ quan hệ để loại bỏ dư thừa và dị thường cập nhật, ta phân rã một quan hệ lớn thành nhiều quan hệ con. Hai tiêu chuẩn chất lượng độc lập đánh giá phép phân rã là: **Tính không mất mát thông tin nối** và **Tính bảo toàn phụ thuộc hàm**.

## 1. Phân rã nối không mất mát thông tin (Lossless-Join)

Phép phân rã lược đồ quan hệ $R$ thành tập các lược đồ con $\rho = \{R_1, R_2, \dots, R_k\}$ được gọi là **phân rã không mất mát thông tin** theo tập phụ thuộc hàm $F$ khi và chỉ khi với mọi thể hiện hợp lệ $r(R)$:
$$\pi_{R_1}(r) \bowtie \pi_{R_2}(r) \bowtie \dots \bowtie \pi_{R_k}(r) = r$$

Nếu phép phân rã bị mất mát (lossy), việc kết nối tự nhiên các bảng con sẽ tạo ra các bộ dữ liệu sai lệch không tồn tại trong thực tế (gọi là *spurious tuples* hay bộ giả).

### Định lý kiểm tra cho phân rã hai quan hệ:
Với phép phân rã thành hai quan hệ con $\rho = \{R_1, R_2\}$, phép phân rã là nối không mất mát thông tin khi và chỉ khi phần giao thuộc tính của chúng là siêu khóa của ít nhất một trong hai quan hệ con:
$$(R_1 \cap R_2) \rightarrow R_1 \in F^+ \quad \text{hoặc} \quad (R_1 \cap R_2) \rightarrow R_2 \in F^+$$

Nghĩa là: $(R_1 \cap R_2)^+$ phải bao hàm $R_1$ hoặc bao hàm $R_2$.

## 2. Bảo toàn phụ thuộc hàm (Dependency Preservation)

Phép phân rã $\rho = \{R_1, R_2, \dots, R_k\}$ được gọi là **bảo toàn phụ thuộc hàm** nếu việc thực thi các ràng buộc phụ thuộc hàm trên từng quan hệ con riêng lẻ đủ để bảo đảm toàn bộ tập phụ thuộc hàm gốc $F$:
$$\left(\bigcup_{i=1}^k \pi_{R_i}(F)\right)^+ = F^+$$

Nếu một phụ thuộc hàm có các thuộc tính bị phân tán ở các bảng con khác nhau mà không thể suy diễn từ các FD cục bộ, hệ quản trị cơ sở dữ liệu sẽ buộc phải thực hiện phép kết nối tốn kém (`JOIN`) mỗi khi có thao tác cập nhật dữ liệu để kiểm tra tính toàn vẹn.

## 3. Mối liên hệ với 3NF và BCNF

- **Thuật toán tổng hợp Bernstein (3NF Synthesis):** Sử dụng [[theory/minimal-cover|phủ tối thiểu $F_c$]] luôn đảm bảo sinh ra các quan hệ con đạt [[theory/3nf|3NF]] thỏa mãn **cả hai tiêu chuẩn**: vừa là Lossless-Join, vừa là Dependency Preservation.
- **Thuật toán phân rã BCNF:** Luôn luôn đảm bảo tính chất Lossless-Join, nhưng **không thể đảm bảo** luôn bảo toàn được phụ thuộc hàm (xem đánh đổi tại [[theory/bcnf|BCNF]]).

Xem thêm các tiên đề cơ sở tại [[theory/functional-dependencies|Phụ thuộc hàm]] và bảng kiểm định tại [[cheat-sheets/normalization|Normalization cheat sheet]].

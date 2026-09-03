---
title: Functional dependencies
description: Định nghĩa phụ thuộc hàm, phân loại tầm thường/không tầm thường và hệ tiên đề Armstrong.
type: theory
topics: [functional-dependencies, normalization]
related: [theory/closure, theory/candidate-keys, theory/minimal-cover, theory/3nf, theory/bcnf]
provenance: verified-artifact
courseEvidence: [UIT-O05, LOC-LEC-LONG-CH06]
---
# Functional dependencies (Phụ thuộc hàm & Tiên đề Armstrong)

Phụ thuộc hàm (Functional Dependency - FD) là công cụ toán học nền tảng dùng để biểu diễn các quy tắc ngữ nghĩa nghiệp vụ và ràng buộc dữ liệu trong mô hình quan hệ, là cơ sở khoa học để loại bỏ dư thừa qua các dạng chuẩn.

## 1. Định nghĩa hình thức

Cho lược đồ quan hệ $R(U)$ với $X, Y \subseteq U$.
Ta nói rằng **$X$ xác định hàm $Y$** (hoặc **$Y$ phụ thuộc hàm vào $X$**), ký hiệu là $X \rightarrow Y$, khi và chỉ khi trong mọi thể hiện quan hệ hợp lệ $r(R)$, với mọi cặp bộ dữ liệu $t_1, t_2 \in r$:
$$t_1[X] = t_2[X] \implies t_1[Y] = t_2[Y]$$

*Trực giác:* Nếu biết trước giá trị của tập thuộc tính $X$, ta luôn xác định duy nhất được giá trị của tập thuộc tính $Y$.

### Phân loại phụ thuộc hàm:
- **Tầm thường (Trivial):** Khi $Y \subseteq X$ (ví dụ: $AB \rightarrow A$). Phụ thuộc này luôn thỏa mãn trên mọi thể hiện dữ liệu mà không mang thông tin nghiệp vụ mới.
- **Không tầm thường (Non-trivial):** Khi $Y \not\subseteq X$.
- **Hoàn toàn không tầm thường (Completely non-trivial):** Khi $X \cap Y = \emptyset$.

## 2. Hệ tiên đề Armstrong (Armstrong's Axioms)

Năm 1974, William W. Armstrong chứng minh hệ 3 tiên đề suy diễn sau là **đúng đắn (sound)** và **đầy đủ (complete)** để suy ra mọi phụ thuộc hàm hợp lý từ một tập $F$:

1. **Luật Phản xạ (Reflexivity):** Nếu $Y \subseteq X \subseteq U$ thì $X \rightarrow Y$.
2. **Luật Tăng trưởng (Augmentation):** Nếu $X \rightarrow Y$ thì $XZ \rightarrow YZ$ với mọi $Z \subseteq U$.
3. **Luật Bắc cầu (Transitivity):** Nếu $X \rightarrow Y$ và $Y \rightarrow Z$ thì $X \rightarrow Z$.

### Ba hệ quả suy diễn thường dùng trong chứng minh:
- **Luật Hợp (Union):** Nếu $X \rightarrow Y$ và $X \rightarrow Z$ thì $X \rightarrow YZ$.
- **Luật Tách / Phân rã (Decomposition):** Nếu $X \rightarrow YZ$ thì $X \rightarrow Y$ và $X \rightarrow Z$.
- **Luật Giả bắc cầu (Pseudotransitivity):** Nếu $X \rightarrow Y$ và $WY \rightarrow Z$ thì $WX \rightarrow Z$.

Dựa trên các tiên đề này, ta xây dựng [[theory/closure|thuật toán bao đóng thuộc tính $X^+$]], xác định [[theory/candidate-keys|khóa ứng viên]], và tìm [[theory/minimal-cover|phủ tối thiểu $F_c$]] làm tiền đề cho chuẩn hóa [[theory/3nf|3NF]] và [[theory/bcnf|BCNF]].

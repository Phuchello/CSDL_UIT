---
title: Dạng đề quan sát — Chuẩn hóa dữ liệu (Normalization)
description: Mẫu bài tập Phụ thuộc hàm, bao đóng, khóa và chuẩn hóa dạng chuẩn trong đề thi UIT.
type: exam-pattern
topics: [exam, functional-dependencies, normalization]
related: [theory/closure, theory/candidate-keys, theory/minimal-cover, theory/3nf, theory/bcnf]
provenance: reconstructed-exam-pattern
courseEvidence: [EXAM-2023-2024-HK1-FINAL-01, LOC-LEC-LONG-CH06]
---
# Dạng đề quan sát — Chuẩn hóa dữ liệu (Normalization)

Trong cấu trúc đề thi Cuối kỳ UIT chuẩn mực (minh chứng qua `EXAM-2023-2024-HK1-FINAL-01` và bài giảng `LOC-LEC-LONG-CH06`), bài toán Phụ thuộc hàm và Chuẩn hóa thường chiếm từ 2.0 đến 3.0 điểm với chuỗi các bước kinh điển:

1. **Tính bao đóng tập thuộc tính**: Áp dụng thuật toán tìm [[theory/closure|Bao đóng X⁺]] dựa trên tập phụ thuộc hàm $F$.
2. **Tìm tất cả khóa ứng viên (Candidate Keys)**: Phân loại tập thuộc tính thành $L, R, N, LR$, xác định tập nguồn bắt buộc và thực hiện rẽ nhánh tìm toàn bộ khóa tối thiểu (xem [[theory/candidate-keys|Khóa ứng viên]]).
3. **Tìm phủ tối thiểu (Minimal Cover)**: Thực hiện chuẩn hóa vế phải 1 thuộc tính, loại bỏ thuộc tính dư thừa vế trái, và loại bỏ phụ thuộc hàm dư thừa (xem [[theory/minimal-cover|Phủ tối thiểu]]).
4. **Xác định dạng chuẩn cao nhất**: Kiểm tra từng phụ thuộc hàm đối chiếu với định nghĩa [[theory/3nf|3NF]] và [[theory/bcnf|BCNF]]. Nếu vi phạm, tiến hành phân rã bảo toàn thông tin nối (xem [[theory/lossless-decomposition|Phân rã không mất mát thông tin]]).

Kỹ năng cốt lõi là trình bày từng bước tính toán rõ ràng, chỉ rõ căn cứ tiên đề Armstrong hoặc bao đóng trung gian tại mỗi bước.

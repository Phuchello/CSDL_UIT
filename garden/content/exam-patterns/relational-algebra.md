---
title: Dạng đề quan sát — Đại số quan hệ (Relational Algebra)
description: Mẫu câu hỏi Đại số quan hệ về chọn, chiếu, nối, hợp và phép chia.
type: exam-pattern
topics: [exam, relational-algebra]
related: [theory/relational-algebra, theory/division, exercises/division-exercise]
provenance: reconstructed-exam-pattern
courseEvidence: [EXAM-2023-2024-HK1-MID-D1, LOC-LEC-LONG-CH03]
---
# Dạng đề quan sát — Đại số quan hệ (Relational Algebra)

Trong các đề thi giữa kỳ UIT (điển hình như đề thi giữa kỳ 2023–2024 Đề 1 và bài giảng `LOC-LEC-LONG-CH03`), dạng câu hỏi [[theory/relational-algebra|Đại số quan hệ]] thường chiếm từ 2.5 đến 4.0 điểm với các cấu trúc trọng tâm:

1. **Phép chọn ($\sigma$) và Chiếu ($\pi$)**: Lọc các dòng thỏa mãn điều kiện và chiếu các thuộc tính đầu ra tương ứng.
2. **Phép kết tự nhiên ($\bowtie$) và Kết có điều kiện ($\bowtie_\theta$)**: Ghép nối các quan hệ theo thuộc tính chung hoặc khóa ngoại.
3. **Phép trừ ($-$)**: Tìm các đối tượng *chưa từng* tham gia vào quan hệ (đòi hỏi hai biểu thức phải khả hợp).
4. **Phép chia ($\div$)**: Dạng bài tìm các thực thể gắn liền với *tất cả* các phần tử của một tập con (xem chi tiết kỹ thuật tại [[theory/division|Phép chia]] và bài mẫu tại [[exercises/division-exercise|Bài tập phép chia]]).

Khi làm bài, sinh viên cần xác định rõ biểu thức trung gian và kiểm tra điều kiện khả hợp (union-compatibility) trước khi áp dụng các phép toán tập hợp. Xem thêm căn cứ tại [[sources/course|Tài liệu học phần (Course Sources)]].

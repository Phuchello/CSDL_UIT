---
title: Lab 04 — trigger và toàn vẹn
description: Trigger, inserted/deleted và kiểm thử thao tác nhiều dòng.
type: practice
topics: [trigger, integrity, inserted, deleted]
related: [rbtv-impact, multi-row-trigger, debugging, multi-row-trigger-failure]
provenance: verified-artifact
fixture: training-v1
technicalSources: [TECH-MS05]
---
# Lab 04 — trigger và toàn vẹn

Bắt đầu từ impact table, viết điều kiện bị cấm, rồi kiểm thử INSERT/UPDATE/DELETE. Trigger phải xử lý tập trong `inserted` và `deleted`; một biến vô hướng chỉ tình cờ đúng với một dòng. Xem [[multi-row-trigger]].

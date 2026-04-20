---
title: "NerfBaselines"
layout: single
collection: projects
permalink: /projects/nerfbaselines/
language: "Python"
official_url: "https://nerfbaselines.github.io/"
code_url: "https://github.com/nerfbaselines/nerfbaselines"
docs_url: "https://nerfbaselines.github.io/"
topic: reconstruction
subtopic: datasets-benchmarks
resource_type: project
level: intermediate
sensors:
  - camera
inputs:
  - datasets
  - checkpoints
outputs:
  - benchmark-results
status: active
verified_at: 2026-04-20
summary_zh: "NerfBaselines 提供统一接口来运行和比较 NeRF 与 3DGS 方法，是复现实验和 benchmark 对齐的高价值工具。"
why_read: "如果你不想自己手工拼接不同方法的评测脚本，它是目前很实用的统一评测入口。"
prerequisites:
  - python
  - nerf basics
related:
  - nerfstudio
tags:
  - benchmark
  - nerf
  - 3dgs
---

## 项目简介

NerfBaselines 的价值不在“重新实现方法”，而在统一数据接口、指标和评测协议。

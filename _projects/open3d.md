---
title: "Open3D"
layout: single
collection: projects
permalink: /projects/open3d/
language: "C++ / Python"
official_url: "https://www.open3d.org/"
code_url: "https://github.com/isl-org/Open3D"
topic: reconstruction
subtopic: reconstruction-tools
resource_type: project
level: beginner
sensors:
  - camera
  - rgbd
  - lidar
inputs:
  - point-cloud
  - rgbd
outputs:
  - point-cloud
  - mesh
status: active
verified_at: 2026-04-20
summary_zh: "现代 3D 数据处理库，覆盖点云、网格、配准、可视化与部分重建能力，工程集成非常方便。"
why_read: "它是把重建结果接到数据处理、评估、可视化和下游应用时最好用的通用工具箱之一。"
prerequisites:
  - python
related: []
tags:
  - reconstruction
  - point-cloud
---

## 项目简介

Open3D 不是只做重建，但它非常适合串起点云处理、RGB-D 融合、注册和可视化。

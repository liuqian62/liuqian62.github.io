---
title: "2D Gaussian Splatting for Geometrically Accurate Radiance Fields"
collection: papers
permalink: /papers/2d-gaussian-splatting-paper/
authors: "Haoqiang Fan et al."
year: 2024
venue: "SIGGRAPH"
official_url: "https://surfsplatting.github.io/"
code_url: "https://github.com/hbb1/2d-gaussian-splatting"
topic: 3dgs
subtopic: 3dgs-geometry
resource_type: paper
level: advanced
sensors:
  - camera
inputs:
  - posed-images
outputs:
  - gaussians
  - surface
status: research-code
verified_at: 2026-04-20
summary_zh: "用 2D 定向盘元替代 3D 体高斯，强调几何一致性与更好的表面重建表现。"
why_read: "如果你关心几何精度而不只看渲染观感，2DGS 是理解这条分支的核心入口。"
prerequisites:
  - 3d-gaussian-splatting-paper
related: []
tags:
  - 3dgs
  - geometry
---

## 论文简介

2DGS 把表示方式调整为更偏表面化的盘元结构，是 3DGS 几何增强分支的重要代表。

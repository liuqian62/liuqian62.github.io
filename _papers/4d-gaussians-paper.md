---
title: "4D Gaussian Splatting for Real-Time Dynamic Scene Rendering"
collection: papers
permalink: /papers/4d-gaussians-paper/
authors: "Guanjun Wu et al."
year: 2024
venue: "CVPR"
official_url: "https://guanjunwu.github.io/4dgs/"
code_url: "https://github.com/hustvl/4DGaussians"
topic: 3dgs
subtopic: dynamic-3dgs
resource_type: paper
level: advanced
sensors:
  - camera
inputs:
  - video
outputs:
  - dynamic-gaussians
status: research-code
verified_at: 2026-04-20
summary_zh: "将动态场景表示扩展到时空维度，兼顾训练效率、存储效率与实时渲染。"
why_read: "它是 4DGS 方向最常被引用的代表资源，适合建立动态高斯路线的整体认识。"
prerequisites:
  - 3d-gaussian-splatting-paper
related: []
tags:
  - 3dgs
  - 4d
---

## 论文简介

4DGaussians 将高斯表示从空间扩展到时空，是动态场景 3DGS 的另一条关键路线。

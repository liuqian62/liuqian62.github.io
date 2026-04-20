---
title: "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
collection: papers
permalink: /papers/3d-gaussian-splatting-paper/
authors: "Bernhard Kerbl et al."
year: 2023
venue: "SIGGRAPH"
official_url: "https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/"
code_url: "https://github.com/graphdeco-inria/gaussian-splatting"
topic: 3dgs
subtopic: 3dgs-foundations
resource_type: paper
level: intermediate
sensors:
  - camera
inputs:
  - posed-images
outputs:
  - gaussians
status: foundational
verified_at: 2026-04-20
summary_zh: "3DGS 的奠基工作，提出显式高斯表示与高效 splatting 渲染，彻底改写实时新视角合成的主流路线。"
why_read: "所有后续 2DGS、动态 GS、GS-SLAM、压缩与 Web 部署基本都在回应这篇工作。"
prerequisites:
  - rendering
  - colmap
related:
  - gaussian-splatting
  - 3dgs-tutorial
tags:
  - 3dgs
---

## 论文简介

这篇工作把显式高斯表示和可微 splatting 渲染组合起来，在质量与效率之间取得了非常强的平衡。

## 阅读建议

建议先跑一遍官方实现，再回来看 densification、visibility-aware rendering 和训练流程。

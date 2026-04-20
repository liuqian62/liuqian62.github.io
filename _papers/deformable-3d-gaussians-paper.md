---
title: "Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction"
collection: papers
permalink: /papers/deformable-3d-gaussians-paper/
authors: "Ibrahim M. et al."
year: 2024
venue: "CVPR"
official_url: "https://ingra14m.github.io/Deformable-Gaussians/"
code_url: "https://github.com/ingra14m/Deformable-3D-Gaussians"
topic: 3dgs
subtopic: dynamic-3dgs
resource_type: paper
level: advanced
sensors:
  - camera
inputs:
  - monocular-video
outputs:
  - dynamic-gaussians
status: research-code
verified_at: 2026-04-20
summary_zh: "通过规范空间高斯与形变场建模动态场景，是动态 3DGS 早期代表作之一。"
why_read: "想理解动态 3DGS 的形变建模和时序一致性，这篇是非常好的起点。"
prerequisites:
  - 3d-gaussian-splatting-paper
related: []
tags:
  - 3dgs
  - dynamic
---

## 论文简介

论文面向单目动态重建，引入可形变高斯和规范空间表示，是动态 3DGS 的代表性入口。

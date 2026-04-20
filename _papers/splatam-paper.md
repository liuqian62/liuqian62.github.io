---
title: "SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM"
collection: papers
permalink: /papers/splatam-paper/
authors: "SplaTAM authors"
year: 2023
venue: "arXiv"
official_url: "https://arxiv.org/abs/2312.02126"
code_url: "https://github.com/spla-tam/SplaTAM"
topic: 3dgs
subtopic: 3dgs-slam
resource_type: paper
level: advanced
sensors:
  - rgbd
inputs:
  - rgbd-video
outputs:
  - pose
  - gaussians
status: research-code
verified_at: 2026-04-20
summary_zh: "将 3D 高斯显式表示引入在线 RGB-D SLAM，强调高保真重建与实时渲染。"
why_read: "它是 GS-SLAM 方向非常关键的早期代表，读它能快速把跟踪、建图和渲染连起来。"
prerequisites:
  - 3d-gaussian-splatting-paper
related: []
tags:
  - 3dgs
  - slam
---

## 论文简介

SplaTAM 展示了 3DGS 如何从离线表示走向在线 SLAM 场景，是阅读后续 GS-SLAM 工作的好起点。

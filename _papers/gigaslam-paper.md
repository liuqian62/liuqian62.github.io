---
title: "GigaSLAM: Large-Scale Monocular SLAM with Hierarchical Gaussian Splats"
collection: papers
permalink: /papers/gigaslam-paper/
authors: "Kai Deng et al."
year: 2025
venue: "arXiv"
official_url: "https://arxiv.org/abs/2503.08071"
topic: 3dgs
subtopic: large-scale-3dgs
resource_type: paper
level: advanced
sensors:
  - camera
inputs:
  - monocular-video
outputs:
  - pose
  - large-scale-map
status: experimental
verified_at: 2026-04-20
summary_zh: "GigaSLAM 面向大规模、无界户外场景，是 3DGS / NeRF 类 SLAM 向公里级环境扩展的代表性尝试。"
why_read: "如果你关心大场景和车载 / 户外环境下的高斯建图，这篇很值得放进专题入口。"
prerequisites:
  - gs-slam-paper
related: []
tags:
  - 3dgs
  - large-scale
  - slam
---

## 论文简介

这篇工作把层级式高斯表示引入更大尺度的单目 SLAM，是大场景高斯建图很好的观察点。

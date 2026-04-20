---
title: "COLMAP Tutorial"
layout: single
collection: tutorials
permalink: /tutorials/colmap-tutorial/
date: 2026-04-20
topic: reconstruction
subtopic: sfm-mvs
resource_type: tutorial
level: beginner
sensors:
  - camera
inputs:
  - images
outputs:
  - poses
  - sparse-point-cloud
official_url: "https://colmap.github.io/tutorial.html"
docs_url: "https://colmap.github.io/tutorial.html"
status: active
verified_at: 2026-04-20
summary_zh: "COLMAP 官方教程覆盖 feature extraction、matching、SfM、dense reconstruction 和 GUI / CLI 基本工作流。"
why_read: "如果你要从一组图片走到可用相机位姿和稀疏 / 稠密重建，这篇是最该先看的官方入口。"
prerequisites:
  - camera geometry
related:
  - colmap
tags:
  - reconstruction
  - colmap
---

## 教程定位

这条教程适合放在传统重建专题的第一屏，因为它直接连接“图片采集”和“后续 NeRF / 3DGS 数据准备”。

---
title: "nerfstudio"
layout: single
collection: projects
permalink: /projects/nerfstudio/
language: "Python"
official_url: "https://docs.nerf.studio/"
code_url: "https://github.com/nerfstudio-project/nerfstudio"
topic: reconstruction
subtopic: nerf
resource_type: project
level: beginner
sensors:
  - camera
inputs:
  - posed-images
outputs:
  - radiance-field
  - gaussians
status: active
verified_at: 2026-04-20
summary_zh: "面向 NeRF 与相关新表示的实验框架，文档完善，插件化设计强，社区采用度高。"
why_read: "如果团队后续要做可复现实验、基线跑通和方法迭代，nerfstudio 是很省时间的研究底座。"
prerequisites:
  - python
related:
  - gsplat
tags:
  - nerf
  - 3dgs
---

## 项目简介

nerfstudio 连接了 NeRF 和 3DGS 两条生态，是做实验与教学都很友好的框架。

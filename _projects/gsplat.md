---
title: "gsplat"
layout: single
collection: projects
permalink: /projects/gsplat/
language: "Python / CUDA"
official_url: "https://docs.gsplat.studio/main/"
code_url: "https://github.com/nerfstudio-project/gsplat"
topic: 3dgs
subtopic: 3dgs-foundations
resource_type: project
level: advanced
sensors:
  - camera
inputs:
  - posed-images
outputs:
  - gaussians
status: active
verified_at: 2026-04-20
summary_zh: "面向 Gaussian Splatting 的 CUDA 微分光栅化库，是很多新 3DGS 系统的高性能后端。"
why_read: "想做 3DGS 方法开发而不是只跑官方代码，gsplat 是更现代、更模块化的工程入口。"
prerequisites:
  - cuda
related:
  - nerfstudio
tags:
  - 3dgs
  - rendering
---

## 项目简介

gsplat 把高性能高斯光栅化能力独立成更模块化的后端，非常适合研究开发。

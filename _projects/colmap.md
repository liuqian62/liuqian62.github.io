---
title: "COLMAP"
layout: single
collection: projects
permalink: /projects/colmap/
language: "C++"
official_url: "https://colmap.github.io/"
code_url: "https://github.com/colmap/colmap"
topic: reconstruction
subtopic: reconstruction-tools
resource_type: project
level: intermediate
sensors:
  - camera
inputs:
  - images
outputs:
  - poses
  - point-cloud
status: mature-active
verified_at: 2026-04-20
summary_zh: "经典开源 SfM+MVS 工具链，支持 GUI 和 CLI，仍是重建与 3DGS 数据准备的事实标准之一。"
why_read: "几乎所有 3DGS / NeRF 工作流都默认兼容 COLMAP 输出，先掌握它能直接打通位姿和稀疏点云。"
prerequisites:
  - camera geometry
related:
  - gaussian-splatting
tags:
  - reconstruction
  - sfm
---

## 项目简介

COLMAP 是图片重建领域最常用的工具链之一，适合作为传统重建和神经表示数据准备的共同入口。

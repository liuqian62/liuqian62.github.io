---
title: "OpenMVS"
layout: single
collection: projects
permalink: /projects/openmvs/
language: "C++"
official_url: "https://openmvs.readthedocs.io/en/latest/"
code_url: "https://github.com/cdcseacave/openMVS"
topic: reconstruction
subtopic: reconstruction-tools
resource_type: project
level: intermediate
sensors:
  - camera
inputs:
  - calibrated-images
outputs:
  - dense-point-cloud
  - mesh
status: active
verified_at: 2026-04-20
summary_zh: "聚焦稠密点云、网格重建、网格优化与贴图，常与 openMVG 或 COLMAP 组合使用。"
why_read: "做传统摄影测量闭环时，它补齐了 SfM 之后到 mesh/texture 的后半段。"
prerequisites:
  - sfm
related: []
tags:
  - reconstruction
  - mvs
---

## 项目简介

OpenMVS 是传统图片重建工作流中把稀疏结果推向可交付网格的重要一环。

---
title: "GraphDECO Gaussian Splatting"
layout: single
collection: projects
permalink: /projects/gaussian-splatting/
language: "Python / CUDA"
official_url: "https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/"
code_url: "https://github.com/graphdeco-inria/gaussian-splatting"
topic: 3dgs
subtopic: 3dgs-foundations
resource_type: project
level: intermediate
sensors:
  - camera
inputs:
  - posed-images
outputs:
  - gaussians
status: foundational
verified_at: 2026-04-20
summary_zh: "GraphDECO 官方 3DGS 实现，是学习 densification、训练流程和渲染管线的第一入口。"
why_read: "看任何后续 3DGS 变体前，最好先把官方实现跑通。"
prerequisites:
  - colmap
related:
  - 3d-gaussian-splatting-paper
tags:
  - 3dgs
---

## 项目简介

这是最适合建立 3DGS 基础直觉的实现，也是很多教程和派生项目的起点。

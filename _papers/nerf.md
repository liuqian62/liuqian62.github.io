---
title: "NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis"
collection: papers
permalink: /papers/nerf/
authors: "Ben Mildenhall et al."
year: 2020
venue: "ECCV"
official_url: "https://arxiv.org/abs/2003.08934"
topic: reconstruction
subtopic: nerf
resource_type: paper
level: intermediate
sensors:
  - camera
inputs:
  - posed-images
outputs:
  - radiance-field
status: classic
verified_at: 2026-04-20
summary_zh: "NeRF 把连续体渲染带到三维场景重建主舞台，是理解后续神经场与 3DGS 叙事的起点。"
why_read: "读懂 NeRF，有助于理解 3DGS 为什么要改写场景表示和渲染效率。"
prerequisites:
  - rendering
  - camera geometry
related:
  - nerfstudio
tags:
  - reconstruction
  - nerf
---

## 论文简介

NeRF 通过多层感知机表示辐射场，并利用体渲染实现高质量新视角合成。

## 为什么要放在这个站里

即使你主要关注 3DGS，也需要把 NeRF 当成重要参照系，因为后续很多工具链、benchmark 和改进方向都在与它对比。

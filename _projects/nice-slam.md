---
title: "NICE-SLAM"
layout: single
collection: projects
permalink: /projects/nice-slam/
language: "Python"
official_url: "https://arxiv.org/abs/2112.12130"
code_url: "https://github.com/cvg/nice-slam"
topic: reconstruction
subtopic: slam-mapping
resource_type: project
level: advanced
sensors:
  - rgbd
inputs:
  - rgbd-video
outputs:
  - neural-map
status: research-code
verified_at: 2026-04-20
summary_zh: "代表性的神经隐式 SLAM 工作，通过分层场景表示提升大场景重建质量与可扩展性。"
why_read: "它是从传统 SLAM 过渡到 NeRF / GS-SLAM 叙事中的关键一站。"
prerequisites:
  - nerf
related: []
tags:
  - slam
  - neural
---

## 项目简介

NICE-SLAM 是理解 neural implicit mapping 的关键项目，对后续更高保真表示路线有明显影响。

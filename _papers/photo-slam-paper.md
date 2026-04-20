---
title: "Photo-SLAM: Real-time Simultaneous Localization and Photorealistic Mapping for Monocular, Stereo, and RGB-D Cameras"
collection: papers
permalink: /papers/photo-slam-paper/
authors: "Photo-SLAM authors"
year: 2024
venue: "CVPR"
official_url: "https://huajianup.github.io/research/Photo-SLAM/"
code_url: "https://github.com/HuajianUP/Photo-SLAM"
topic: 3dgs
subtopic: 3dgs-slam
resource_type: paper
level: advanced
sensors:
  - camera
  - rgbd
inputs:
  - video
outputs:
  - pose
  - map
status: research-code
verified_at: 2026-04-20
summary_zh: "融合显式几何特征与隐式光度特征，支持单目、双目和 RGB-D，相比纯隐式方案更偏实时与落地。"
why_read: "如果你想看 GS / 神经渲染如何往可部署 SLAM 系统靠拢，Photo-SLAM 很有代表性。"
prerequisites:
  - orb-slam3
related: []
tags:
  - 3dgs
  - slam
---

## 论文简介

Photo-SLAM 关注在不同相机模式下实现更接近真实部署的 photorealistic mapping。

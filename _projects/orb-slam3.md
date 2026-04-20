---
title: "ORB-SLAM3"
layout: single
collection: projects
permalink: /projects/orb-slam3/
language: "C++"
official_url: "https://github.com/UZ-SLAMLab/ORB_SLAM3"
code_url: "https://github.com/UZ-SLAMLab/ORB_SLAM3"
topic: reconstruction
subtopic: slam-mapping
resource_type: project
level: advanced
sensors:
  - camera
  - imu
  - rgbd
inputs:
  - video
outputs:
  - pose
  - map
status: mature-maintained
verified_at: 2026-04-20
summary_zh: "经典特征法 SLAM 系统，支持单目、双目、RGB-D 与惯导，是许多新式 SLAM 的基准线。"
why_read: "做 GS-SLAM 或 Photo-SLAM 相关调研时，ORB-SLAM3 是理解传统跟踪前端最稳的参考系。"
prerequisites:
  - slam basics
related: []
tags:
  - slam
---

## 项目简介

ORB-SLAM3 是从传统几何路线理解在线建图的重要入口，适合与 NICE-SLAM、Photo-SLAM 做对比阅读。

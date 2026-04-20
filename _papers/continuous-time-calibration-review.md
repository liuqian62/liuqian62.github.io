---
title: "Batch Continuous-Time Trajectory Estimation as Exactly Sparse Gaussian Process Regression"
collection: papers
permalink: /papers/continuous-time-calibration-review/
authors: "Timothy D. Barfoot et al."
year: 2014
venue: "RSS"
official_url: "https://www.roboticsproceedings.org/rss10/p01.pdf"
topic: sync
subtopic: continuous-time
resource_type: paper
level: advanced
sensors:
  - camera
  - lidar
  - imu
outputs:
  - trajectory
  - interpolation
status: classic
verified_at: 2026-04-20
summary_zh: "连续时间轨迹估计领域的代表性论文，用 GP 视角统一连续轨迹表示与稀疏优化，对异步多传感器融合影响很大。"
why_read: "站点如果要解释连续时间方法为何适合同步、插值和异步观测，这篇是很强的理论锚点。"
prerequisites:
  - optimization
  - estimation
related: []
tags:
  - sync
  - continuous-time
---

## 论文简介

这篇工作从高斯过程回归的角度讨论连续时间轨迹估计，为处理异步观测和高频 IMU / LiDAR 数据提供了统一视角。

## 阅读建议

不必一开始就啃完推导，可以先把它当成“为什么连续时间方法在同步问题里这么常见”的理论解释。

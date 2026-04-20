---
title: "A Flexible New Technique for Camera Calibration"
collection: papers
permalink: /papers/zhang-camera-calibration/
authors: "Zhengyou Zhang"
year: 2000
venue: "IEEE TPAMI"
official_url: "https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/zhan99.pdf"
topic: calibration
subtopic: camera
resource_type: paper
level: beginner
sensors:
  - camera
inputs:
  - calibration-board
outputs:
  - intrinsics
  - distortion
status: classic
verified_at: 2026-04-20
summary_zh: "Zhang 平面标定法奠定了现代相机内参标定的经典基线，至今仍是大量工具链的理论起点。"
why_read: "读它能快速建立对棋盘格/平面靶标相机标定的统一认识。"
prerequisites:
  - camera geometry
related:
  - opencv-camera-calibration-guide
tags:
  - calibration
  - camera
---

## 论文简介

这篇论文提出了只需平面标定板和多视角观测的相机标定方法，显著降低了传统三维标定物体的使用门槛。

## 为什么重要

- 它是 OpenCV 等主流工具链背后的理论基石之一。
- 它帮助理解内参与畸变参数是如何通过重投影误差被优化出来的。

## 阅读建议

先结合 OpenCV 官方教程理解实际工作流，再回来看论文里的模型假设和求解步骤。

---
title: "Camera Calibration With OpenCV"
layout: single
collection: tutorials
permalink: /tutorials/opencv-camera-calibration-guide/
date: 2026-04-20
topic: calibration
subtopic: camera
resource_type: tutorial
level: beginner
sensors:
  - camera
inputs:
  - calibration-board
outputs:
  - intrinsics
official_url: "https://docs.opencv.org/4.x/d4/d94/tutorial_camera_calibration.html"
code_url: "https://github.com/opencv/opencv/tree/4.x/samples/cpp/tutorial_code/calib3d/camera_calibration"
docs_url: "https://docs.opencv.org/4.x/d4/d94/tutorial_camera_calibration.html"
status: active
verified_at: 2026-04-20
summary_zh: "OpenCV 官方教程给出了从采集、角点检测到 calibrateCamera 与去畸变的完整入门流程。"
why_read: "它是工程里最常见、最低门槛、最容易落地复现的相机标定入口。"
prerequisites:
  - camera geometry
related:
  - zhang-camera-calibration
tags:
  - tutorial
  - calibration
---

## 为什么先看这篇

如果你只需要先把单目标定跑通，这篇官方教程就是最稳妥的起点。

## 你会学到什么

- 标定图像采集的基本要求
- 角点检测和参数求解
- 去畸变与结果验证

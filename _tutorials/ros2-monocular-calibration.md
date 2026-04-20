---
title: "ROS 2 Monocular Calibration Tutorial"
layout: single
collection: tutorials
permalink: /tutorials/ros2-monocular-calibration/
date: 2026-04-20
topic: calibration
subtopic: camera
resource_type: tutorial
level: beginner
sensors:
  - camera
inputs:
  - raw-image-topic
outputs:
  - camera-info
official_url: "https://docs.ros.org/en/rolling/p/camera_calibration/doc/tutorial_mono.html"
docs_url: "https://docs.ros.org/en/rolling/p/camera_calibration/doc/tutorial_mono.html"
status: active
verified_at: 2026-04-20
summary_zh: "ROS 2 官方单目标定教程展示了如何用 cameracalibrator 节点直接从图像 topic 完成标定并保存结果。"
why_read: "如果你的相机在 ROS 2 里跑，这条比通用 OpenCV 教程更贴近日常工程使用方式。"
prerequisites:
  - ros2
related:
  - opencv-camera-calibration-guide
tags:
  - calibration
  - ros2
---

## 教程定位

这条资源把相机标定从离线脚本工作流推进到 ROS2 在线工具工作流。

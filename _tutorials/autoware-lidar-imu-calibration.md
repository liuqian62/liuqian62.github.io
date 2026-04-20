---
title: "Autoware Lidar-Imu Calibration"
layout: single
collection: tutorials
permalink: /tutorials/autoware-lidar-imu-calibration/
date: 2026-04-20
topic: calibration
subtopic: lidar-imu
resource_type: tutorial
level: intermediate
sensors:
  - lidar
  - imu
inputs:
  - rosbag
outputs:
  - extrinsics
official_url: "https://autowarefoundation.github.io/autoware-documentation/latest/how-to-guides/integrating-autoware/creating-vehicle-and-sensor-model/calibrating-sensors/lidar-imu-calibration/"
code_url: "https://github.com/leo-drive/OA-LICalib"
docs_url: "https://autowarefoundation.github.io/autoware-documentation/latest/how-to-guides/integrating-autoware/creating-vehicle-and-sensor-model/calibrating-sensors/lidar-imu-calibration/"
status: active
verified_at: 2026-04-20
summary_zh: "Autoware 官方文档整理了基于 OA-LICalib 的 LiDAR-IMU 标定环境准备、采集规范与运行步骤。"
why_read: "它把论文工具转成了更接近量产 / 车端集成的可操作流程。"
prerequisites:
  - ros2
related: []
tags:
  - lidar
  - imu
  - calibration
---

## 教程定位

这是更偏工程交付的 LiDAR-IMU 资源，适合从研究原型走向真实系统集成。

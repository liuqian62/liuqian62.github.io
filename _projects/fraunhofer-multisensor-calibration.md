---
title: "Fraunhofer Multi-Sensor Calibration Toolbox"
layout: single
collection: projects
permalink: /projects/fraunhofer-multisensor-calibration/
language: "C++ / ROS 2"
official_url: "https://fraunhoferiosb.github.io/multisensor_calibration/"
code_url: "https://github.com/FraunhoferIOSB/multisensor_calibration"
docs_url: "https://fraunhoferiosb.github.io/multisensor_calibration/"
topic: calibration
subtopic: calibration-tools
resource_type: project
level: intermediate
sensors:
  - camera
  - lidar
inputs:
  - rosbag
outputs:
  - extrinsics
status: active
verified_at: 2026-04-20
summary_zh: "Fraunhofer IOSB 的通用多传感器标定工具箱支持 camera-lidar、lidar-lidar 等多种组合，并提供 ROS 2 支持。"
why_read: "它适合放在 tools 分类做通用工具箱代表，覆盖面比单一传感器对更广。"
prerequisites:
  - ros2
related: []
tags:
  - calibration
  - tools
---

## 项目简介

这是更偏“通用 toolbox”定位的标定项目，适合做主题页里的工程总入口。

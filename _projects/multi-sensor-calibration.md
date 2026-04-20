---
title: "multi_sensor_calibration"
layout: single
collection: projects
permalink: /projects/multi-sensor-calibration/
language: "C++ / Python"
official_url: "https://github.com/tudelft-iv/multi_sensor_calibration"
code_url: "https://github.com/tudelft-iv/multi_sensor_calibration"
topic: calibration
subtopic: radar-camera
resource_type: project
level: advanced
sensors:
  - camera
  - lidar
  - radar
inputs:
  - rosbag
outputs:
  - extrinsics
status: classic
verified_at: 2026-04-20
summary_zh: "TU Delft 这套工具面向 lidar、camera、radar 联合外参标定，是雷达相关开源资源里很有代表性的主流项目。"
why_read: "首版站点如果只选一个 radar calibration 条目，它最能兼顾代表性、完整度和可复现性。"
prerequisites:
  - calibration basics
related: []
tags:
  - calibration
  - radar
---

## 项目简介

这套工具很适合补齐站点里雷达相关标定的专题入口。

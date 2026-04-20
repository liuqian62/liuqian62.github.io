---
title: "imu_utils"
layout: single
collection: projects
permalink: /projects/imu-utils/
language: "C++"
official_url: "https://github.com/gaowenliang/imu_utils"
code_url: "https://github.com/gaowenliang/imu_utils"
topic: calibration
subtopic: imu
resource_type: project
level: beginner
sensors:
  - imu
inputs:
  - imu-log
outputs:
  - noise-parameters
status: stable
verified_at: 2026-04-20
summary_zh: "ROS 生态中非常常用的 IMU Allan 方差分析工具，可估计白噪声和 bias random walk 等参数。"
why_read: "很多 VIO / SLAM 系统成败都取决于 IMU 噪声参数是否先标准化。"
prerequisites:
  - imu basics
related: []
tags:
  - calibration
  - imu
---

## 项目简介

imu_utils 适合做 IMU 标定和噪声参数初始化，是很多 VIO 用户的第一站。

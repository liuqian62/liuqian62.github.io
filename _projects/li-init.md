---
title: "LI-Init"
layout: single
collection: projects
permalink: /projects/li-init/
language: "C++ / ROS"
official_url: "https://github.com/hku-mars/LiDAR_IMU_Init"
code_url: "https://github.com/hku-mars/LiDAR_IMU_Init"
topic: calibration
subtopic: lidar-imu
resource_type: project
level: advanced
sensors:
  - lidar
  - imu
inputs:
  - rosbag
outputs:
  - extrinsics
  - time-offset
status: active
verified_at: 2026-04-20
summary_zh: "LI-Init 是 HKU-MARS 的经典 LiDAR-IMU 初始化工具，可同时估计外参与时间偏移，并衔接 FAST-LIO。"
why_read: "做 LIO 系统时，它是理解 LiDAR-IMU 初始化与时空标定工程落地的高价值入口。"
prerequisites:
  - ros
  - lidar odometry
related:
  - autoware-lidar-imu-calibration
tags:
  - calibration
  - lidar
  - imu
---

## 项目简介

LI-Init 适合作为 LiDAR-IMU 标定和初始化专题里的核心项目，尤其适合和 FAST-LIO 生态一起理解。

---
title: "Kalibr"
layout: single
collection: projects
permalink: /projects/kalibr-multi-sensor-calibration/
language: "C++ / Python"
official_url: "https://github.com/ethz-asl/kalibr"
code_url: "https://github.com/ethz-asl/kalibr"
topic: calibration
subtopic: camera-imu
resource_type: project
level: intermediate
sensors:
  - camera
  - imu
inputs:
  - rosbag
outputs:
  - extrinsics
  - time-offset
status: classic
verified_at: 2026-04-20
summary_zh: "Kalibr 是视觉惯导标定事实标准工具，支持相机-IMU 空间与时间联合标定，并估计 IMU 内参。"
why_read: "做 camera-imu 标定几乎绕不开它，资料多、论文基础扎实、结果格式也被广泛接受。"
prerequisites:
  - ros
related:
  - unified-temporal-spatial-calibration
tags:
  - calibration
  - vio
---

## 项目简介

Kalibr 是相机、IMU 和多相机标定的常用事实标准工具，尤其适合 VIO、SLAM 和机器人系统。

## 推荐使用场景

- 相机-IMU 联合标定
- 多相机 rig 标定
- 需要估计时间偏移的离线流程

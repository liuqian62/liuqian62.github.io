---
title: "How to Use ros2_tracing to Trace and Analyze an Application"
layout: single
collection: tutorials
permalink: /tutorials/ros2-tracing-sync-diagnostics/
date: 2026-04-20
topic: sync
subtopic: sync-diagnostics
resource_type: tutorial
level: advanced
sensors:
  - camera
  - lidar
  - imu
inputs:
  - ros2-application
outputs:
  - trace-analysis
official_url: "https://docs.ros.org/en/humble/Tutorials/Advanced/ROS2-Tracing-Trace-and-Analyze.html"
code_url: "https://github.com/ros2/ros2_tracing"
docs_url: "https://docs.ros.org/en/humble/Tutorials/Advanced/ROS2-Tracing-Trace-and-Analyze.html"
status: active
verified_at: 2026-04-20
summary_zh: "ROS 2 官方 tracing 教程，展示如何采集和分析执行时序、回调耗时与系统级 trace 数据。"
why_read: "做同步问题排查时，它非常适合作为消息到了没、回调卡在哪、延迟抖动从哪来的诊断工具入口。"
prerequisites:
  - ros2
related: []
tags:
  - sync
  - ros2
  - diagnostics
---

## 教程定位

这条资源补的是“如何证明自己的问题真的是同步问题，而不是调度和回调链路造成的延迟”。

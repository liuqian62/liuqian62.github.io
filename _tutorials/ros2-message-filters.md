---
title: "ROS 2 Message Filters"
layout: single
collection: tutorials
permalink: /tutorials/ros2-message-filters/
date: 2026-04-20
topic: sync
subtopic: ros-message-sync
resource_type: tutorial
level: intermediate
sensors:
  - camera
  - lidar
  - imu
inputs:
  - ros2-messages
outputs:
  - synchronized-streams
official_url: "https://docs.ros.org/en/ros2_packages/humble/api/message_filters/doc/index.html"
code_url: "https://github.com/ros2/message_filters"
docs_url: "https://docs.ros.org/en/ros2_packages/humble/api/message_filters/doc/index.html"
status: active
verified_at: 2026-04-20
summary_zh: "ROS 2 message_filters 官方总览，覆盖 TimeSynchronizer、ApproximateTime、Cache 等常用同步与缓冲策略。"
why_read: "这是 ROS2 侧消息层对齐最该收的入口，能把同步策略和适用场景讲清楚。"
prerequisites:
  - ros2
related: []
tags:
  - sync
  - ros2
---

## 教程定位

这不是硬件同步教程，而是当设备时间戳已经进入 ROS2 系统后，如何在消息层做合理对齐的工程入口。

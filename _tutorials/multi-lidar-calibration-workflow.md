---
title: "Multi-Lidar Calibration Workflow"
layout: single
collection: tutorials
permalink: /tutorials/multi-lidar-calibration-workflow/
date: 2026-04-20
topic: calibration
subtopic: lidar
resource_type: tutorial
level: intermediate
sensors:
  - lidar
inputs:
  - multi-lidar point-clouds
outputs:
  - lidar-extrinsics
official_url: "https://www.mathworks.com/help/lidar/ug/multi-lidar-calibration-workflow.html"
docs_url: "https://www.mathworks.com/help/lidar/ug/multi-lidar-calibration-workflow.html"
status: active
verified_at: 2026-04-20
summary_zh: "该官方示例展示了用 hand-eye / AX=XB 思路进行多 LiDAR 相对位姿标定的完整流程。"
why_read: "它能帮助站点补齐纯 LiDAR 标定条目，而不只停留在多传感器外参。"
prerequisites:
  - point-cloud basics
related: []
tags:
  - lidar
  - calibration
---

## 教程定位

如果你的系统里有多个 LiDAR，这条资源可以帮你快速建立相对位姿标定的基本流程概念。

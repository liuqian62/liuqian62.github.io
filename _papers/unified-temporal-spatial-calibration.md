---
title: "Unified Temporal and Spatial Calibration for Multi-Sensor Systems"
collection: papers
permalink: /papers/unified-temporal-spatial-calibration/
authors: "Paul Furgale, Jorg Rehder, Roland Siegwart"
year: 2013
venue: "IROS"
official_url: "https://furgalep.github.io/bib/furgale_iros13.pdf"
code_url: "https://github.com/ethz-asl/kalibr"
topic: calibration
subtopic: spatiotemporal-calibration
resource_type: paper
level: advanced
sensors:
  - camera
  - imu
  - lidar
outputs:
  - extrinsics
  - time-offset
status: classic
verified_at: 2026-04-20
summary_zh: "这篇论文系统提出了多传感器时空联合标定框架，是后续 Kalibr 等方法的核心理论来源。"
why_read: "想把时间偏移和空间外参当成一个统一问题来理解，这篇几乎是必读。"
prerequisites:
  - optimization
  - rigid-body transforms
related:
  - kalibr-multi-sensor-calibration
tags:
  - calibration
  - sync
---

## 论文简介

论文把时间偏移和外参标定放进统一优化框架，是理解多传感器系统为何不能把“同步”和“标定”完全拆开的关键入口。

## 适合谁读

适合已经做过基础标定、希望理解 Kalibr 这类工具背后原理的读者。

---
title: "PTP Hardware Clock Infrastructure for Linux"
layout: single
collection: tutorials
permalink: /tutorials/ptp-hardware-clock-infrastructure/
date: 2026-04-20
topic: sync
subtopic: ptp-pps
resource_type: tutorial
level: advanced
sensors:
  - camera
  - lidar
  - imu
inputs:
  - ptp-hardware-clock
outputs:
  - synchronized-clocks
official_url: "https://docs.kernel.org/driver-api/ptp.html"
docs_url: "https://docs.kernel.org/driver-api/ptp.html"
status: stable
verified_at: 2026-04-20
summary_zh: "Linux 内核对 PHC 能力、用户态接口、驱动接口和外部事件/周期信号支持的权威说明。"
why_read: "适合解释为什么某些 NIC / SoC 能做硬件时间戳、外部时间戳和 PPS 配合。"
prerequisites:
  - linux
related:
  - linuxptp
tags:
  - sync
  - ptp
---

## 教程定位

如果你正在判断设备是否真的支持“硬件级时间同步”，这篇内核文档是最值得先看的官方依据。

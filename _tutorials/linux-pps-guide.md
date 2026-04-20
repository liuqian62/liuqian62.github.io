---
title: "Linux PPS - Pulse Per Second"
layout: single
collection: tutorials
permalink: /tutorials/linux-pps-guide/
date: 2026-04-20
topic: sync
subtopic: ptp-pps
resource_type: tutorial
level: intermediate
sensors:
  - camera
  - lidar
  - imu
inputs:
  - pps-signal
outputs:
  - synchronized-clocks
official_url: "https://docs.kernel.org/driver-api/pps.html"
docs_url: "https://docs.kernel.org/driver-api/pps.html"
status: stable
verified_at: 2026-04-20
summary_zh: "LinuxPPS 官方内核文档说明了 PPS 源、/dev/ppsX、GPIO/串口接入方式、测试方法及生成器支持。"
why_read: "站点如果要讲 GPS / PPS、外部秒脉冲或硬件对时，这篇是最合适的官方起点。"
prerequisites:
  - linux
related:
  - linuxptp
tags:
  - sync
  - pps
---

## 教程定位

PPS 常常是硬件同步里最容易被忽略但最实用的一环，这篇文档适合拿来做工程起步参考。

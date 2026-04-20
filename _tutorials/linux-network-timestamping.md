---
title: "Linux Network Timestamping"
layout: single
collection: tutorials
permalink: /tutorials/linux-network-timestamping/
date: 2026-04-20
topic: sync
subtopic: software-timestamping
resource_type: tutorial
level: advanced
sensors:
  - camera
  - lidar
  - imu
inputs:
  - network-packets
outputs:
  - timestamps
official_url: "https://docs.kernel.org/networking/timestamping.html"
docs_url: "https://docs.kernel.org/networking/timestamping.html"
status: stable
verified_at: 2026-04-20
summary_zh: "Linux 网络时间戳官方文档，解释 SO_TIMESTAMPING、软/硬时间戳和驱动 / 网卡相关行为。"
why_read: "讲软件时间戳时很难绕开它；它也是区分应用层打点、内核收发时间戳和硬件时间戳的最好官方依据。"
prerequisites:
  - linux networking
related: []
tags:
  - sync
  - timestamping
---

## 教程定位

这条资源适合放在“为什么消息时间戳不一定等于真实采集时间”的核心解释位置。

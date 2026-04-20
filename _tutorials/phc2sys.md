---
title: "phc2sys(8): synchronize two or more clocks"
layout: single
collection: tutorials
permalink: /tutorials/phc2sys/
date: 2026-04-20
topic: sync
subtopic: sync-diagnostics
resource_type: tutorial
level: intermediate
sensors:
  - camera
  - lidar
  - imu
inputs:
  - phc
outputs:
  - system-clock-sync
official_url: "https://www.linuxptp.org/documentation/phc2sys/"
code_url: "https://github.com/nwtime/linuxptp"
docs_url: "https://www.linuxptp.org/documentation/phc2sys/"
status: active
verified_at: 2026-04-20
summary_zh: "linuxptp 中负责系统时钟与 PHC 之间闭环同步的关键工具文档，常用于验证 PTP 是否真正传导到了 CLOCK_REALTIME。"
why_read: "很适合放进诊断专题，帮助读者判断网卡时钟同步了，但系统时间有没有真的跟上。"
prerequisites:
  - linuxptp
related:
  - linuxptp
tags:
  - sync
  - diagnostics
---

## 教程定位

这条资源特别适合解释“PTP 配通了”不等于“系统里所有时间源都已经对齐”。

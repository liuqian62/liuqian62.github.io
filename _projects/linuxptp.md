---
title: "The Linux PTP Project"
layout: single
collection: projects
permalink: /projects/linuxptp/
language: "C"
official_url: "https://www.linuxptp.org/"
code_url: "https://github.com/nwtime/linuxptp"
topic: sync
subtopic: ptp-pps
resource_type: project
level: intermediate
sensors:
  - camera
  - lidar
  - imu
inputs:
  - network-time
outputs:
  - synchronized-clocks
status: active
verified_at: 2026-04-20
summary_zh: "Linux 上最核心的 PTP 工具集合入口，覆盖 ptp4l、phc2sys、ts2phc 等。"
why_read: "做站点首版时，这是 PTP 工程实践最该先收的一条。"
prerequisites:
  - linux
related: []
tags:
  - sync
  - ptp
---

## 项目简介

linuxptp 提供了 Linux 侧 PTP 同步和 PHC 管理的核心工具，是硬件时间同步主题最重要的工程入口。

---
title: "月度更新 Monthly Updates"
permalink: /updates/
layout: single
author_profile: false
---

# 月度更新

最新动态聚焦高频变化区：`3DGS`、benchmark、工具链兼容性和标准化。

{% for item in site.data.monthly_updates.items %}
## {{ item.title }}

**分类**: {{ item.category }}

{{ item.summary }}

[查看来源]({{ item.url }})
{% endfor %}

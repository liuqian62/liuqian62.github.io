---
title: "Papers"
layout: single
collection: papers
permalink: /papers/
author_profile: false
---

# 论文 Papers

这里收录三维重建相关的代表论文。和主题页不同，这里按资源类型统一浏览；每条论文会同时标注 `topic` 与 `subtopic`，方便从论文反查到主题知识树。

{% for post in site.papers %}
  {% include archive-single.html %}
{% endfor %}

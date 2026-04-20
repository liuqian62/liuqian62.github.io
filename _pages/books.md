---
title: "Books"
layout: single
collection: books
permalink: /books/
author_profile: false
---

# 书籍 Books

书籍页偏向长期参考资料，适合建立几何、状态估计和视觉重建的系统基础。

{% for post in site.books %}
  {% include archive-single.html %}
{% endfor %}

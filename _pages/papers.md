---
title: "论文 Papers"
layout: single
collection: papers
permalink: /papers/
author_profile: false
---

# 📚 三维重建相关论文

本页面收录了三维重建领域的经典论文和最新研究，按主题分类整理。

## 📖 论文列表

{% for paper in site.papers reversed %}
- **{{ paper.title }}**  
  {% if paper.authors %}{{ paper.authors }}{% endif %}  
  {% if paper.year %}({{ paper.year }}){% endif %}  
  {% if paper.venue %} - *{{ paper.venue }}*{% endif %}  
  {% if paper.arxiv %} [arXiv]({{ paper.arxiv }}){% endif %}  
  {% if paper.code %} [Code]({{ paper.code }}){% endif %}  
  {% if paper.project %} [Project]({{ paper.project }}){% endif %}
{% endfor %}

---

## 📝 添加新论文

在 `_papers/` 目录下创建 Markdown 文件：

```markdown
---
title: "论文标题"
collection: papers
permalink: /papers/论文链接/
authors: "作者列表"
year: 2024
venue: "会议/期刊名称"
arxiv: "https://arxiv.org/abs/xxxx"
code: "https://github.com/xxx"
project: "https://project-page.com"
tags:
  - 3D重建
  - 深度学习
---

## 论文简介

简要介绍这篇论文的主要内容、方法和贡献。

## 学习笔记

记录学习这篇论文时的笔记和心得。
```

## 🏷️ 标签分类

{% tag_list papers %}

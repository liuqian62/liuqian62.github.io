---
title: "教程 Tutorials"
layout: single
collection: tutorials
permalink: /tutorials/
author_profile: false
---

# 📖 三维重建学习教程

本页面收录了三维重建领域的原创学习笔记和优质教程文章。

## 📝 教程列表

{% for tutorial in site.tutorials reversed %}
- **{{ tutorial.title }}**  
  {% if tutorial.date %}📅 {{ tutorial.date | date: "%Y-%m-%d" }}{% endif %}  
  {% if tutorial.difficulty %} | 难度: {{ tutorial.difficulty }}{% endif %}  
  {{ tutorial.excerpt }}  
  [阅读更多]({{ tutorial.url }})
{% endfor %}

---

## 📚 添加新教程

在 `_tutorials/` 目录下创建 Markdown 文件：

```markdown
---
title: "教程标题"
layout: single
collection: tutorials
permalink: /tutorials/教程链接/
date: 2024-01-01
difficulty: 初级/中级/高级
tags:
  - 教程
  - 三维重建
---

## 前言

介绍本教程的学习目标。

## 环境准备

### 依赖安装

## 核心内容

### 第一部分

### 第二部分

## 总结

## 参考资料
```

## 🏷️ 难度等级

- 🟢 **初级**：适合入门学习
- 🟡 **中级**：需要一定基础
- 🔴 **高级**：深入进阶内容

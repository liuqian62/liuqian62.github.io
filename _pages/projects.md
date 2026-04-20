---
title: "开源项目 Open Source Projects"
layout: single
collection: projects
permalink: /projects/
author_profile: false
---

# 🤖 三维重建开源项目推荐

本页面收录了三维重建领域的优秀开源项目和代码库。

## ⭐ 项目列表

{% for project in site.projects reversed %}
- **{{ project.title }}**  
  {% if project.stars %}⭐ Stars: {{ project.stars }}{% endif %}  
  {% if project.language %} | 🛠️ {{ project.language }}{% endif %}  
  {{ project.excerpt }}  
  {% if project.github %} [GitHub]({{ project.github }}){% endif %}  
  {% if project.docs %} [文档]({{ project.docs }}){% endif %}
{% endfor %}

---

## 📦 添加新项目

在 `_projects/` 目录下创建 Markdown 文件：

```markdown
---
title: "项目名称"
layout: single
collection: projects
permalink: /projects/项目链接/
stars: "⭐ 10k+"
language: "Python / C++"
github: "https://github.com/username/repo"
docs: "https://docs.example.com"
tags:
  - 开源
  - 三维重建
  - SLAM
---

## 项目简介

简要介绍这个项目的功能和特点。

## 主要特性

- 特性1
- 特性2
- 特性3

## 快速开始

```bash
git clone https://github.com/username/repo.git
cd repo
pip install -r requirements.txt
```

## 应用场景

## 学习资源
```

## 🛠️ 编程语言

- 🐍 Python
- ⚙️ C++
- 🦀 Rust
- 📦 TensorFlow / PyTorch

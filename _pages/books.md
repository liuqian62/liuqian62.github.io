---
title: "书籍推荐 Books"
layout: single
collection: books
permalink: /books/
author_profile: false
---

# 📚 三维重建相关书籍

本页面收录了三维重建领域的优质技术书籍。

## 📖 书籍列表

{% for book in site.books reversed %}
- **{{ book.title }}**  
  {% if book.author %}👤 {{ book.author }}{% endif %}  
  {% if book.publisher %} | 📅 {{ book.publisher }}{% endif %}  
  {% if book.rating %} | ⭐ {{ book.rating }}{% endif %}  
  {{ book.excerpt }}  
  {% if book.link %} [购买链接]({{ book.link }}){% endif %}
{% endfor %}

---

## 📚 添加新书籍

在 `_books/` 目录下创建 Markdown 文件：

```markdown
---
title: "书名"
layout: single
collection: books
permalink: /books/书籍链接/
author: "作者"
publisher: "出版社"
rating: "9.5/10"
link: "https://book-link.com"
tags:
  - 书籍
  - 三维重建
  - SLAM
---

## 书籍简介

简要介绍这本书的内容和特色。

## 适合人群

## 主要内容

### 第1篇：基础理论
### 第2篇：核心算法
### 第3篇：实践应用

## 读后感

## 精彩片段

## 参考价值
```

## 📚 推荐书单

### 🌟 入门书籍
- 《SLAM十四讲》- 高翔
- 《Computer Vision: Algorithms and Applications》

### 🚀 进阶书籍
- 《Multiple View Geometry in Computer Vision》
- 《State Estimation for Robotics》

### 🎓 深度学习相关
- 《Deep Learning》
- 《Computer Vision: Models, Learning, and Inference》

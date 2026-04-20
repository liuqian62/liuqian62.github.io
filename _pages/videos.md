---
title: "视频课程 Videos"
layout: single
collection: videos
permalink: /videos/
author_profile: false
---

# 🎬 三维重建视频课程

本页面收录了三维重建领域的优质视频教程和讲座。

## 📺 视频列表

{% for video in site.videos reversed %}
- **{{ video.title }}**  
  {% if video.platform %}📍 {{ video.platform }}{% endif %}  
  {% if video.duration %} | ⏱️ {{ video.duration }}{% endif %}  
  {% if video.instructor %} | 👨‍🏫 {{ video.instructor }}{% endif %}  
  {{ video.excerpt }}  
  {% if video.url %} [观看视频]({{ video.url }}){% endif %}
{% endfor %}

---

## 📹 添加新视频

在 `_videos/` 目录下创建 Markdown 文件：

```markdown
---
title: "视频标题"
layout: single
collection: videos
permalink: /videos/视频链接/
platform: "YouTube / Bilibili / Coursera"
duration: "2小时30分钟"
instructor: "讲师名称"
url: "https://video-url.com"
tags:
  - 视频课程
  - 三维重建
---

## 课程简介

简要介绍这个视频课程的内容。

## 课程大纲

### 第一部分
### 第二部分
### 第三部分

## 学习收获

## 相关资料
```

## 🎯 学习建议

1. 🎬 观看前先了解基础知识
2. 📝 做好学习笔记
3. 💻 跟着实践操作
4. 🤔 思考并提出问题
5. 📚 结合文档和论文深入学习

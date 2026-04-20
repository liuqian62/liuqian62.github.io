# 三维重建学习资源合集 | 3D Reconstruction Learning Resources

**3D Reconstruction Learning** - 基于 Jekyll 和 GitHub Pages 构建的三维重建学习资源导航网站

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📌 项目概述

| 属性 | 说明 |
|------|------|
| **网站类型** | 三维重建学习资源导航网站 |
| **技术框架** | Jekyll 4.x + GitHub Pages |
| **主题来源** | [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) |
| **部署平台** | GitHub Pages (免费托管) |
| **许可证** | MIT |
| **站点地址** | https://liuqian62.github.io |

### 关于作者
- **昵称**: lirich674
- **身份**: SLAM/三维重建 学习者
- **位置**: 成都
- **邮箱**: lirich674@gmail.com
- **GitHub**: [liuqian62](https://github.com/liuqian62)

---

## 🏗️ 技术架构

### 核心技术栈
```
静态站点生成器: Jekyll
前端模板:       Minimal Mistakes (SCSS)
标记语言:       Markdown (Kramdown)
样式语言:       SCSS
部署平台:       GitHub Pages
依赖管理:       Ruby Gems (Bundler)
```

### 项目结构
```
.
├── _config.yml          # 全局配置 (站点信息、作者、插件等)
├── _data/               # 数据文件 (导航、作者、UI文本)
├── _includes/           # 可复用组件 (页眉、页脚、侧边栏等)
├── _layouts/            # 页面布局模板
├── _pages/              # 页面 (论文、教程、项目、视屏、书籍)
├── _papers/             # 论文资源
├── _tutorials/          # 教程文章
├── _projects/           # 开源项目
├── _videos/             # 视频课程
├── _books/              # 书籍推荐
├── _sass/               # 样式文件 (主题核心)
├── assets/              # 静态资源 (CSS、JS、图片、字体)
└── Gemfile              # Ruby依赖配置
```

---

## 📂 内容模块

### 导航菜单
| 页面 | 路由 | 说明 |
|------|------|------|
| 首页 | `/` | 网站介绍和资源索引 |
| 论文 | `/papers/` | 经典论文和最新研究推荐 |
| 教程 | `/tutorials/` | 学习笔记和教程整理 |
| 开源项目 | `/projects/` | 优秀开源代码库推荐 |
| 视频课程 | `/videos/` | 视频教程和讲座链接 |
| 书籍 | `/books/` | 技术书籍整理 |

### 内容集合 (Collections)
| 集合 | 目录 | 说明 |
|------|------|------|
| Papers | `_papers/` | 论文资源 |
| Tutorials | `_tutorials/` | 教程文章 |
| Projects | `_projects/` | 开源项目 |
| Videos | `_videos/` | 视频课程 |
| Books | `_books/` | 书籍推荐 |

---

## 🚀 快速开始

### 环境要求
- Ruby >= 2.4
- Bundler
- Jekyll
- Git

### 本地运行

```bash
# 1. 克隆仓库
git clone https://github.com/liuqian62/liuqian62.github.io.git
cd liuqian62.github.io

# 2. 安装依赖
bundle install

# 3. 本地预览 (开发模式)
bundle exec jekyll serve --livereload

# 4. 访问 http://localhost:4000
```

### 部署流程
1. 将代码推送到 GitHub 仓库
2. 在仓库 Settings → Pages 中启用 GitHub Pages
3. 选择 `main` 分支作为源代码
4. 站点将自动构建并发布

---

## 🛠️ 常用配置

### 1. 修改站点信息 (`_config.yml`)
```yaml
title: "3D Reconstruction Learning"
description: "三维重建学习资源合集 · 论文 · 教程 · 开源项目 · 视频课程 · 书籍推荐"
url: "https://liuqian62.github.io"
```

### 2. 修改导航菜单 (`_data/navigation.yml`)
```yaml
main:
  - title: "首页"
    url: /
  - title: "论文"
    url: /papers/
  - title: "教程"
    url: /tutorials/
  - title: "开源项目"
    url: /projects/
  - title: "视频课程"
    url: /videos/
  - title: "书籍"
    url: /books/
```

### 3. 添加新论文
在 `_papers/` 目录创建 Markdown 文件：

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

### 4. 添加新教程
在 `_tutorials/` 目录创建 Markdown 文件：

```markdown
---
title: "教程标题"
layout: single
collection: tutorials
permalink: /tutorials/教程链接/
date: 2024-01-01
difficulty: 初级
tags:
  - 教程
  - 三维重建
---

## 前言

介绍本教程的学习目标。

## 环境准备

## 核心内容

## 总结
```

### 5. 添加新开源项目
在 `_projects/` 目录创建 Markdown 文件：

```markdown
---
title: "项目名称"
layout: single
collection: projects
permalink: /projects/项目链接/
stars: "⭐ 10k+"
language: "Python"
github: "https://github.com/username/repo"
docs: "https://docs.example.com"
tags:
  - 开源
  - 三维重建
---

## 项目简介

## 主要特性

## 快速开始
```

### 6. 添加新视频课程
在 `_videos/` 目录创建 Markdown 文件：

```markdown
---
title: "视频标题"
layout: single
collection: videos
permalink: /videos/视频链接/
platform: "YouTube"
duration: "2小时30分钟"
instructor: "讲师名称"
url: "https://video-url.com"
tags:
  - 视频课程
  - 三维重建
---

## 课程简介

## 课程大纲
```

### 7. 添加新书籍
在 `_books/` 目录创建 Markdown 文件：

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
---

## 书籍简介

## 适合人群

## 主要内容
```

---

## 🎯 学习路径建议

### 🌟 入门阶段
1. 阅读《SLAM十四讲》打好基础
2. 学习 ORB-SLAM 系列论文
3. 观看相关视频课程
4. 实践基础教程

### 🚀 进阶阶段
1. 深入学习 Multi-View Geometry
2. 学习深度学习在3D重建中的应用
3. 阅读最新顶会论文
4. 复现优秀开源项目

### 🎓 高级阶段
1. 关注最新研究进展
2. 参与开源项目贡献
3. 尝试改进现有方法
4. 发表自己的研究成果

---

## 📊 内容统计

| 类型 | 数量 | 说明 |
|------|------|------|
| 论文 | 📚 | 持续更新中 |
| 教程 | 📖 | 学习笔记整理 |
| 项目 | 🤖 | 开源代码推荐 |
| 视频 | 🎬 | 优质课程推荐 |
| 书籍 | 📚 | 经典书籍推荐 |

> 💡 **提示**: 每种资源类型都配有模板文件，方便快速添加新内容。

---

## 📝 许可证

本项目基于 [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) 主题，使用 **MIT License**。

详细内容请查看 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- **主题**: [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) by Michael Rose
- **模板**: [Academic Pages](https://github.com/academicpages/academicpages.github.io) by Stuart Geiger
- **托管**: [GitHub Pages](https://pages.github.com/)

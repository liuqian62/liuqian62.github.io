# 个人学术网站 | Personal Academic Website

**lirich674's Personal Website** - 基于 Jekyll 和 GitHub Pages 构建的学术个人网站

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## 📌 项目概述

| 属性 | 说明 |
|------|------|
| **网站类型** | 个人学术/技术博客网站 |
| **技术框架** | Jekyll 4.x + GitHub Pages |
| **主题来源** | [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) |
| **部署平台** | GitHub Pages (免费托管) |
| **许可证** | MIT |
| **站点地址** | https://liuqian62.github.io |

### 作者信息
- **昵称**: lirich674
- **身份**: SLAM 学习者
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
├── _pages/              # 页面 (关于、笔记、博客、简历等)
├── _posts/              # 博客文章 (Markdown格式)
├── _publications/      # 学术论文
├── _talks/              # 演讲/报告
├── _teaching/           # 教学经历
├── _portfolio/          # 项目作品集
├── _sass/               # 样式文件 (主题核心)
├── assets/              # 静态资源 (CSS、JS、图片、字体)
├── files/               # 可下载文件 (PDF等)
├── talkmap/              # 演讲地点地图可视化
├── markdown_generator/   # 批量生成Markdown的工具
└── Gemfile              # Ruby依赖配置
```

### 插件列表
| 插件名称 | 用途 |
|----------|------|
| jekyll-paginate | 分页功能 |
| jekyll-sitemap | 生成站点地图 |
| jekyll-gist | 嵌入GitHub Gist |
| jekyll-feed | RSS/Atom订阅 |
| jekyll-redirect-from | 重定向支持 |
| jekyll-archives | 归档功能 (可选) |

---

## 📂 内容模块

### 导航菜单
| 页面 | 路由 | 说明 |
|------|------|------|
| 首页/关于 | `/` | 个人介绍和项目统计 |
| 笔记 | `/notebook/` | 技术笔记整理 |
| 博客 | `/year-archive/` | 按年份归档的博客文章 |
| 简历 | `/cv/` | 个人简历 |
| 指南 | `/markdown/` | 使用指南 |

### 内容集合 (Collections)
| 集合 | 目录 | 说明 |
|------|------|------|
| Posts | `_posts/` | 博客文章 |
| Publications | `_publications/` | 学术论文 |
| Talks | `_talks/` | 演讲报告 |
| Teaching | `_teaching/` | 教学经历 |
| Portfolio | `_portfolio/` | 项目作品 |

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

### 1. 修改个人信息 (`_config.yml`)
```yaml
name: "lirich674"
title: "首页"
description: "personal description"
url: "https://liuqian62.github.io"

author:
  name: "lirich674"
  bio: "slam学习者"
  location: "Chengdu"
  email: "lirich674@gmail.com"
  github: "liuqian62"
```

### 2. 修改导航菜单 (`_data/navigation.yml`)
```yaml
main:
  - title: "笔记"
    url: /notebook/
  - title: "博客"
    url: /year-archive/
  - title: "简历"
    url: /cv/
  - title: "指南"
    url: /markdown/
```

### 3. 创建新文章
在 `_posts/` 目录创建 Markdown 文件，命名格式:
```
YYYY-MM-DD-title-of-post.md
```

### 4. 添加论文
在 `_publications/` 目录创建文件:
```markdown
---
title: "论文标题"
collection: publications
---
论文内容...
```

---

## 🔧 辅助工具

### 1. TalkMap - 演讲地图可视化
**功能**: 将演讲地点以交互式地图形式展示

**使用方式**:
```bash
cd talkmap
python talkmap.py
```

**依赖**: `getorg`, `geopy`

### 2. Markdown Generator - 批量生成工具
**功能**: 从 TSV 文件批量生成 Markdown 文件

**文件位置**: `markdown_generator/`

**支持类型**:
- `talks.tsv` → `_talks/*.md`
- `publications.tsv` → `_publications/*.md`

**使用方式**:
```bash
# 使用Jupyter Notebook
jupyter notebook markdown_generator/talks.ipynb

# 或使用Python脚本
python markdown_generator/talks.py
```

---

## 📊 内容概览

### 内容集合
| 集合 | 目录 | 说明 | 状态 |
|------|------|------|------|
| Publications | `_publications/` | 学术论文 | 📝 模板已就绪 |
| Talks | `_talks/` | 演讲报告 | 📝 模板已就绪 |
| Teaching | `_teaching/` | 教学经历 | 📝 模板已就绪 |
| Portfolio | `_portfolio/` | 项目作品 | 📝 模板已就绪 |
| Posts | `_posts/` | 博客文章 | 🗑️ 已清空 |
| Notebook | `notebook/` | 技术笔记 | 🔗 外部链接 |

> 💡 **提示**: 所有内容集合都配有参考模板，方便快速添加新内容。

---

## 📝 许可证

本项目基于 [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) 主题，使用 **MIT License**。

详细内容请查看 [LICENSE](LICENSE) 文件。

---

## 🙏 致谢

- **主题**: [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) by Michael Rose
- **模板**: [Academic Pages](https://github.com/academicpages/academicpages.github.io) by Stuart Geiger
- **托管**: [GitHub Pages](https://pages.github.com/)

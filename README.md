# 3D Reconstruction Learning Resources | 三维重建学习资源合集

> A curated knowledge hub for 3D Reconstruction, SLAM, Multi-Sensor Calibration, Time Synchronization, and 3D Gaussian Splatting.

**Live Site**: https://liuqian62.github.io  
**Author**: lirich674 (SLAM / 3D Reconstruction learner, Chengdu)  
**License**: MIT

---

## Project Overview | 项目概述

| Attribute | Value |
|-----------|-------|
| **Type** | Static knowledge navigation site |
| **Domain** | 3D Reconstruction, SLAM, Multi-Sensor Systems |
| **Framework** | Jekyll 4.x + Minimal Mistakes theme |
| **Hosting** | GitHub Pages |
| **Language** | Chinese (primary) + English |

**Core Mission**: Organize 3D reconstruction learning resources into a clear, topic-driven knowledge graph. The site connects calibration, time synchronization, reconstruction methods, and 3D Gaussian Splatting (3DGS) into coherent learning paths.

---

## Architecture | 技术架构

### Tech Stack
```
Static Site Generator : Jekyll 4.x
Theme                  : Minimal Mistakes (SCSS)
Markup                : Markdown (Kramdown)
Deployment            : GitHub Pages
Package Manager       : Ruby Gems (Bundler)
```

### Directory Structure
```
├── _config.yml           # Site configuration
├── _data/                # YAML data files
│   ├── topics.yml        # Four main topics & subtopics
│   ├── learning_paths.yml # Three-tier learning paths
│   ├── featured_resources.yml # Curated entry points
│   └── navigation.yml    # Navigation menu
├── _pages/               # Page content
│   ├── calibration.md    # Topic: Multi-sensor calibration
│   ├── sync.md           # Topic: Time synchronization
│   ├── reconstruction.md # Topic: 3D reconstruction
│   └── 3dgs.md           # Topic: 3D Gaussian Splatting
├── _papers/              # Paper collection (18 papers)
├── _tutorials/           # Tutorial collection
├── _projects/            # Open-source project entries (20 projects)
├── _videos/              # Video course collection
├── _books/               # Book recommendations
├── _includes/            # Reusable components
├── _layouts/             # Page templates
└── _sass/                # Theme styles
```

---

## Domain Model | 领域模型

### Four Main Topics | 四条主线

```
┌─────────────────────────────────────────────────────────────────┐
│                    3D RECONSTRUCTION ECOSYSTEM                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │   CALIBRATION     │  │      SYNC        │                     │
│  │   标定            │  │   时间同步        │                     │
│  ├──────────────────┤  ├──────────────────┤                     │
│  │ Single/Camera     │  │ Offset/Drift/     │                     │
│  │ Stereo/Multi      │  │ Latency          │                     │
│  │ LiDAR-Camera      │  │ Trigger/PPS/PTP   │                     │
│  │ Camera-IMU        │  │ ROS2 Filters     │                     │
│  │ LiDAR-IMU         │  │ Continuous-Time  │                     │
│  │ Radar-Camera      │  │ Diagnostics      │                     │
│  │ Spatiotemporal    │  │                  │                     │
│  └──────────────────┘  └──────────────────┘                     │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐                     │
│  │ RECONSTRUCTION    │  │     3DGS         │                     │
│  │ 重建              │  │ 3D高斯泼溅        │                     │
│  ├──────────────────┤  ├──────────────────┤                     │
│  │ SfM/MVS          │  │ Foundations       │                     │
│  │ TSDF/SDF         │  │ Geometry/2DGS    │                     │
│  │ SLAM Mapping     │  │ Dynamic/4D        │                     │
│  │ NeRF/Neural Fields│  │ Online/Incremental│                     │
│  │ Datasets/Benchmarks│ │ Large-Scale      │                     │
│  │                  │  │ Compression       │                     │
│  │                  │  │ Editable/Semantic │                     │
│  │                  │  │ GS-SLAM          │                     │
│  └──────────────────┘  └──────────────────┘                     │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Calibration Topic | 标定
- **标定基础**: Camera, Stereo/Multi-camera, LiDAR, IMU, Radar
- **跨传感器**: LiDAR-Camera, Camera-IMU, LiDAR-IMU, Radar-Camera, Radar-LiDAR, Radar-IMU
- **时空标定**: Spatiotemporal calibration (joint optimization of time offset + extrinsic)
- **工具**: Kalibr, LI-Init, TIER IV CalibrationTools

### Sync Topic | 时间同步
- **同步基础**: Offset, Drift, Latency concepts
- **硬件同步**: Trigger/Shared Clock, PTP/IEEE 1588, PPS
- **软件同步**: Driver timestamping, ROS/ROS2 message filters, Continuous-time modeling
- **诊断**: Overlay, lag scan, residual analysis

### Reconstruction Topic | 重建
- **传统方法**: SfM (Structure from Motion), MVS (Multi-View Stereo)
- **工具链**: COLMAP, OpenMVG, OpenMVS, Open3D
- **体素表示**: TSDF, SDF, KinectFusion, Voxel hashing
- **SLAM建图**: Visual SLAM, RGB-D SLAM, Neural SLAM
- **神经场**: NeRF, Neural Fields, Efficient NeRF
- **基准**: Datasets and benchmarks

### 3DGS Topic | 3D高斯泼溅 (Most Active)
- **基础**: Original 3DGS, Splatfacto, 2DGS, Mesh extraction
- **动态场景**: 4D Gaussians, Deformable 3DGS, Human/vehicle animation
- **大规模**: Online/Incremental, City-scale, Autonomous driving
- **压缩部署**: LightGaussian, Model compression, glTF standardization
- **应用**: GS-SLAM, Robotic mapping, Semantic segmentation, Editing

---

## Content Collections | 内容集合

### Papers | 论文 (`_papers/`)
| Paper | Year | Focus |
|-------|------|-------|
| Zhang Camera Calibration | 1999 | Classic single-camera calibration |
| 3D Gaussian Splatting | 2023 | Foundational 3DGS paper |
| 2D Gaussian Splatting | 2024 | Geometry-accurate 3DGS |
| 4D Gaussians | 2024 | Dynamic scene representation |
| Deformable 3D Gaussians | 2023 | Non-rigid scenes |
| GigaSAM | 2024 | Large-scale 3DGS |
| GS-SLAM | 2024 | 3DGS + SLAM integration |
| Photo-SLAM | 2024 | SLAM with Gaussians |
| NeRF | 2020 | Neural Radiance Fields |
| Continuous-Time Calibration Review | 2024 | Time synchronization |
| + 8 more | - | - |

### Projects | 开源项目 (`_projects/`)
| Project | Language | Category |
|---------|----------|----------|
| COLMAP | C++/Python | SfM/MVS |
| Open3D | C++/Python | Geometry processing |
| ORB-SLAM3 | C++ | Visual SLAM |
| NiceSLAM | Python | Neural SLAM |
| NeRFStudio | Python | NeRF framework |
| Gaussian Splatting | Python | Original 3DGS |
| GSplat | CUDA/Python | Fast 3DGS |
| Kalibr | Python/C++ | Multi-sensor calibration |
| OpenMVG | C++ | SfM |
| OpenMVS | C++ | Multi-view stereo |
| LinuxPTP | C | PTP synchronization |
| K-Radar | Python | Radar datasets |
| nuScenes | Python | Autonomous driving data |
| + 8 more | - | - |

### Tutorials | 教程 (`_tutorials/`)
- OpenCV Camera Calibration Guide
- ROS2 Message Filters
- 3DGS Tutorial
- (Template-based, expandable)

### Books | 书籍 (`_books/`)
- Multiple View Geometry (Hartley & Zisserman)
- State Estimation for Robotics

---

## Learning Paths | 学习路径

### 入门路径 (Beginner)
```
1. Camera model, intrinsic/extrinsic parameters, coordinate systems
2. OpenCV single-camera and stereo calibration
3. COLMAP: image → sparse/dense reconstruction pipeline
4. Understand TSDF, NeRF, 3DGS representation differences
```

### 进阶路径 (Intermediate)
```
1. Camera-IMU, LiDAR-Camera, LiDAR-IMU calibration
2. PTP/PPS/trigger/ROS2 message_filters trade-offs
3. Compare SfM/MVS, RGB-D, NeRF, 3DGS trade-offs
4. Overlay, lag scan, residual diagnostic methods
```

### 前沿路径 (Advanced)
```
1. GraphDECO 3DGS, Splatfacto, official tutorials
2. Track papers by: Dynamic, Geometry, Compression, Editing, SLAM
3. Priority: surveys, official implementations, reproducible benchmarks
4. glTF Gaussian Splatting standardization & Web/Engine ecosystem
```

---

## Quick Start | 快速开始

### Local Development
```bash
# Clone
git clone https://github.com/liuqian62/liuqian62.github.io.git
cd liuqian62.github.io

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve --livereload

# Access http://localhost:4000
```

### Deployment
1. Push to GitHub repository
2. Enable GitHub Pages in Settings → Pages
3. Select `main` branch as source
4. Auto-build and deploy

---

## Adding Content | 添加内容

### Adding a Paper
Create `_papers/your-paper.md`:
```markdown
---
title: "Paper Title"
collection: papers
permalink: /papers/your-paper/
authors: "Authors"
year: 2024
venue: "Conference/Journal"
arxiv: "https://arxiv.org/abs/xxxx"
code: "https://github.com/xxx"
project: "https://project-page.com"
tags:
  - 3DGS
  - Geometry
---

## Abstract / Summary
## Key Contributions
## Learning Notes
```

### Adding a Project
Create `_projects/your-project.md`:
```markdown
---
title: "Project Name"
collection: projects
permalink: /projects/your-project/
stars: "⭐ 10k+"
language: "Python"
github: "https://github.com/username/repo"
tags:
  - Reconstruction
  - Open Source
---

## Overview
## Key Features
## Quick Start
```

---

## Navigation Structure | 导航结构

| Page | Route | Content |
|------|-------|---------|
| Home | `/` | Topic-driven entry with featured resources |
| Calibration | `/calibration/` | Multi-sensor calibration hub |
| Sync | `/sync/` | Time synchronization hub |
| Reconstruction | `/reconstruction/` | 3D reconstruction methods |
| 3DGS | `/3dgs/` | 3D Gaussian Splatting frontier |
| Papers | `/papers/` | All papers archive |
| Tutorials | `/tutorials/` | All tutorials archive |
| Projects | `/projects/` | All projects archive |
| Videos | `/videos/` | Video courses |
| Books | `/books/` | Book recommendations |

---

## Design Philosophy | 设计理念

1. **Topic-First Organization**: Resources are grouped by problem domain (calibration, sync, reconstruction, 3DGS) rather than just type
2. **Learning Path Guidance**: Three-tier paths (beginner → intermediate → advanced) help users navigate
3. **Curated Entry Points**: Each topic has recommended starter resources
4. **Engineering Focus**: Emphasis on reproducible tools and practical workflows

---

## Acknowledgments | 致谢

- **Theme**: [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) by Michael Rose
- **Template**: [Academic Pages](https://github.com/academicpages/academicpages.github.io) by Stuart Geiger
- **Hosting**: [GitHub Pages](https://pages.github.com/)

---
permalink: /
title: "三维重建学习资源合集"
excerpt: "多传感器标定、时间同步、重建方法与 3D Gaussian Splatting 的学习导航。"
layout: single
author_profile: false
---

{% assign all_resources = site.papers | concat: site.tutorials | concat: site.projects | concat: site.videos | concat: site.books %}

<section class="home-hero">
  <div class="home-hero__eyebrow">3D Reconstruction Learning Hub</div>
  <h1>把标定、同步、重建和 3DGS 放到一条清晰的学习链路里</h1>
  <p>这个站点以主题优先的方式整理三维重建相关资源：先告诉你问题属于哪条技术链路，再给出精选论文、教程、项目、视频和书籍入口。</p>
  <p>
    <a href="/calibration/" class="btn">进入主题导航</a>
    <a href="/papers/" class="btn btn--inverse">浏览所有资源类型</a>
  </p>
</section>

<div class="section-header">
  <h2>四条主线</h2>
  <p>如果你是带着具体问题来的，优先从主题页进入；如果你只是想扫资源，再回到 Papers / Tutorials / Projects 等归档页。</p>
</div>

<div class="home-grid">
  {% for pair in site.data.topics %}
    {% assign key = pair[0] %}
    {% assign topic = pair[1] %}
    {% assign path = '/' | append: key | append: '/' %}
    {% if key == '3dgs' %}
      {% assign path = '/3dgs/' %}
    {% endif %}
    <article class="topic-card">
      <div class="topic-card__eyebrow">
        <span>{{ key }}</span>
      </div>
      <h3><a href="{{ path }}">{{ topic.title }}</a></h3>
      <p>{{ topic.intro }}</p>
      <a href="{{ path }}" class="btn btn--small">查看主题</a>
    </article>
  {% endfor %}
</div>

<div class="section-header">
  <h2>学习路径</h2>
  <p>按照你的阶段选择合适的阅读顺序，而不是一开始就陷入工具细节。</p>
</div>

<div class="home-grid">
  {% for path in site.data.learning_paths.paths %}
    <article class="path-card">
      <h3>{{ path.title }}</h3>
      <p>{{ path.audience }}</p>
      <ol>
        {% for step in path.steps %}
          <li>{{ step }}</li>
        {% endfor %}
      </ol>
    </article>
  {% endfor %}
</div>

<div class="section-header">
  <h2>工具链总览</h2>
  <p>从采集、标定、同步、重建到前沿表示，先记住这些主入口。</p>
</div>

<div class="tools-grid">
  <article class="tool-card">
    <h3>采集与标定</h3>
    <p>OpenCV、Kalibr、LI-Init、TIER IV CalibrationTools 覆盖相机、多相机、IMU、LiDAR 与联合时空标定。</p>
  </article>
  <article class="tool-card">
    <h3>同步与诊断</h3>
    <p>LinuxPTP、`ptp4l`、Linux PPS、ROS2 `message_filters` 是多传感器系统的工程基础设施。</p>
  </article>
  <article class="tool-card">
    <h3>传统重建与几何工具</h3>
    <p>COLMAP、OpenMVG、OpenMVS、Open3D 适合走通经典图片和 RGB-D 重建流程。</p>
  </article>
  <article class="tool-card">
    <h3>NeRF 与 3DGS</h3>
    <p>nerfstudio、GraphDECO Gaussian Splatting、2DGS、4DGaussians 和相关 survey 构成前沿入口。</p>
  </article>
</div>

<div class="section-header">
  <h2>精选资源</h2>
  <p>每个主题先放一条入门入口、一条主流工具和一篇代表论文，后续再持续扩展。</p>
</div>

{% for group in site.data.featured_resources.groups %}
  <section class="topic-section">
    <header class="topic-section__header">
      <h3>{{ group.title }}</h3>
    </header>
    <div class="resource-grid">
      {% for entry in group.entries %}
        {% assign matches = all_resources | where_exp: "item", "item.collection == entry.collection and item.slug == entry.slug" %}
        {% assign resource = matches | first %}
        {% if resource %}
          {% include resource-card.html resource=resource %}
        {% endif %}
      {% endfor %}
    </div>
  </section>
{% endfor %}

<div class="section-header">
  <h2>月度更新</h2>
  <p>更新最快的部分主要集中在 3DGS、benchmark、工具链兼容性和标准化动态。</p>
</div>

<div class="updates-list">
  {% for item in site.data.monthly_updates.items %}
    <article class="update-card">
      <p><strong>{{ item.category }}</strong></p>
      <h3>{{ item.title }}</h3>
      <p>{{ item.summary }}</p>
      <a href="{{ item.url }}" class="btn btn--small btn--inverse">查看来源</a>
    </article>
  {% endfor %}
</div>

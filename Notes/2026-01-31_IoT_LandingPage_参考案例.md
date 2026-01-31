---
title: IoT/工控类 Landing Page 设计参考案例库
date: 2026-01-31
tags: [Design, Inspiration, IoT, LandingPage]
concepts: [[Industrial UI]], [[SaaS Design]], [[Data Visualization]]
type: conversation-log
status: public
---

# IoT/工控类 Landing Page 设计参考案例库

## 🎯 核心问题 (The Hook)
> 为了设计“物联检测BOX”的首页，有哪些具体的、风格契合（深色、科技、数据感）的网站可以参考？

## 🔍 场景还原 (Context)
用户提问：登录前首页 (Landing Page) 给我一些参考示例。
背景：用户需要为其 IoT 项目设计首页，目标风格是深色模式、工控科技感，需要具体的对标案例。

## 💡 探索过程 (The Journey)
### 🙋 我
登录前首页 (Landing Page) 给我一些参考示例。

### 🤖 AI
针对“物联检测BOX”的深色工控风格，我精选了以下三类参考案例：

#### 1. 行业对标 (IoT & Data Platforms) - *最直接的参考*
这些是成熟的物联网或数据监控平台，它们的首页完美展示了如何把“复杂的技术”讲得“性感”。

*   **ThingsBoard (https://thingsboard.io/)**
    *   **理由**: 开源 IoT 平台的标杆。
    *   **看点**: 它的 Hero Section 直接展示了动态的仪表盘（Dashboard），非常直观。它的 Feature 区域使用了大量的图标+简短文字，非常适合你展示“传感器类型”。
*   **Grafana (https://grafana.com/)**
    *   **理由**: 数据可视化领域的王者，深色模式的教科书。
    *   **看点**: 注意它如何展示“数据大屏”截图，以及黑色背景下如何使用高饱和度的颜色（橙色/蓝色）做点缀。
*   **Particle (https://www.particle.io/)**
    *   **理由**: 硬件+软件结合的 IoT 平台。
    *   **看点**: 它的排版非常干净，展示了如何把“硬件板子”和“软件界面”放在同一张图里，体现软硬结合。
*   **Blynk (https://blynk.io/)**
    *   **理由**: 专注于移动端控制的 IoT 平台。
    *   **看点**: 它的首页非常现代化，使用了大量的设备 mockup（手机/平板壳子）来展示界面。

#### 2. 视觉风格对标 (Dark Mode & Tech) - *提升颜值*
这些虽然不是 IoT 产品，但它们的“深色科技风”非常适合移植到你的项目中。

*   **Supabase (https://supabase.com/)**
    *   **理由**: 开发者工具，深色绿色调。
    *   **看点**: 它的 **Bento Grid (便当盒布局)** 非常经典，用一个个小格子展示不同的功能点（数据库、认证、存储），非常适合你展示“16种传感器”。
*   **Linear (https://linear.app/)**
    *   **理由**: UI 设计界的“神”。
    *   **看点**: 极致的黑色背景 + 微妙的流光效果 (Glow effects)。如果你的首页能做到这个质感，会非常震撼。
*   **Raycast (https://www.raycast.com/)**
    *   **理由**: 效率工具，深色红色调。
    *   **看点**: 它的 Hero Section 只有一行字 + 一个巨大的、高保真的软件界面截图，非常自信。

#### 3. 现成模板 (Templates) - *快速实现*
如果你想直接抄代码（React + Tailwind），看这里：

*   **Aceternity UI (https://ui.aceternity.com/)**
    *   **推荐组件**: "Hero Parallax" (视差滚动首屏), "Bento Grid" (功能网格), "Sparkles" (粒子背景)。
    *   **风格**: 100% 契合你的赛博朋克/工控需求。
*   **Cruip (https://cruip.com/)**
    *   搜 "Open PRO" 或 "Cube"，有很多深色 SaaS 模板。

## 🧠 核心归因 (Root Cause)
优秀的 IoT Landing Page 都在做一件事：**可视化不可见的数据**。
通过展示仪表盘截图、硬件模型、数据流动画，让用户一眼看懂“原来这个盒子能看到这些数据”。

## ✅ 行动指南 (Actionable Takeaway)
- [ ] 打开 **Supabase** 官网，学习它的 Bento Grid 布局，用来设计你的“核心能力”板块。
- [ ] 打开 **Grafana** 官网，学习它的配色方案，如何让数据图表在黑底上不刺眼。
- [ ] 决定你的 Hero Image：是放一张高清的 Dashboard 截图，还是放一张 3D 的设备渲染图？

## 🔗 延伸思考
- 如何在首页通过简单的 CSS 动画（如数据跳动、连线传输）来暗示“实时性”？

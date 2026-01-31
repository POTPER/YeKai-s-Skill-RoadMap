# ALIGNMENT: Integrating QuestMap (Skill) into OdoBlog (Web)

> **文档状态**: Draft
> **创建时间**: 2026-01-31
> **目标**: 将 "QuestMap" 生成的学习博客无缝集成到 "OdoBlog" 个人网站中。

## 1. 现状分析

### 1.1 OdoBlog (前端容器)
*   **技术栈**: React + Vite + TypeScript + Tailwind CSS。
*   **当前状态**: 一个具有赛博朋克风格 (Cyberpunk UI) 的静态博客 Demo。
*   **核心功能**:
    *   `App.tsx`: 页面路由管理 (Home/Blog/Article)。
    *   `ArticleView.tsx`: 简单的 Markdown 渲染器（目前是手写解析逻辑）。
    *   `constants.ts`: 硬编码的 `BLOG_POSTS` 数据源。
    *   `AIChatWidget.tsx`: 右下角的 AI 聊天挂件。

### 1.2 QuestMap (内容生产工厂)
*   **技术栈**: Python (AI Skill)。
*   **功能**: 自动生成带有 Chat UI 结构 (HTML) 的 Markdown 文件。
*   **产物**: 位于 `Notes/` 目录下的 `.md` 文件。

---

## 2. 集成策略 (Integration Strategy)

为了让 OdoBlog 能够展示 QuestMap 生成的“对话式博客”，我们需要打通**数据加载**和**样式渲染**两个环节。

### 2.1 样式集成 (Style Integration)
*   **目标**: 让 QuestMap 生成的 `<div class="chat-message">` 在 OdoBlog 中正确显示。
*   **方案**:
    1.  将 `questmap/templates/chat.css` 的样式移植到 OdoBlog 的 `index.css` 或新建 `ChatStyles.css`。
    2.  确保 `ArticleView.tsx` 能够渲染 HTML 内容（目前它只支持简单的文本分割渲染）。

### 2.2 数据渲染升级 (Rendering Upgrade)
*   **现状**: `ArticleView.tsx` 目前使用极其简陋的 `split('\n')` 方式解析 Markdown，无法处理 HTML 标签。
*   **改进**: 引入 `react-markdown` 或 `dangerouslySetInnerHTML` (简单粗暴但有效) 来渲染 QuestMap 生成的复杂内容。
    *   鉴于 QuestMap 生成的是混合了 Markdown 和 HTML 的内容，推荐使用支持 HTML 的 Markdown 渲染器。

### 2.3 数据源打通 (Data Pipeline)
*   **现状**: 博客数据硬编码在 `constants.ts`。
*   **目标**: 读取本地 Markdown 文件。
*   **方案 (MVP)**:
    *   手动将 `Notes/*.md` 的内容转换为 `BLOG_POSTS` 格式（短期）。
    *   或者编写一个脚本，自动扫描 `Notes/` 目录，生成 `constants.ts`（自动化）。

---

## 3. 执行计划 (Action Plan)

### 3.1 [Step 1] 移植样式
*   创建 `c:\Users\Kai\Documents\GitHub\odoblog\src\styles\ChatStyles.css`。
*   复制 `chat.css` 的内容进去。
*   在 `main.tsx` 或 `App.tsx` 中引入。

### 3.2 [Step 2] 升级 ArticleView 组件
*   改造 `ArticleView.tsx`，使其支持渲染 HTML 内容（因为 QuestMap 的气泡是 HTML）。
*   添加对 Front Matter 元数据的显示支持。

### 3.3 [Step 3] 导入测试数据
*   将刚才生成的 "QuestMap产品设计演进.md" 的内容，手动添加到 `constants.ts` 中作为一篇新文章进行测试。

---

## 4. 疑问澄清
*   用户是否接受在 MVP 阶段通过手动复制 Markdown 内容到 `constants.ts` 来发布文章？（这是最快看到效果的方式，不需要搭建后端）。
*   用户是否愿意安装 `react-markdown` 等库来提升渲染质量？

**决策**: 优先采用**最少依赖**方案。
1.  样式：直接加 CSS。
2.  渲染：使用 `dangerouslySetInnerHTML` 渲染 QuestMap 生成的 HTML 部分（对话气泡）。
3.  数据：手动添加一条测试数据验证效果。

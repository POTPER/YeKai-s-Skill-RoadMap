# ALIGNMENT_QuestMap: 学习归因工具 (QuestMap Skill)

> **文档状态**: Draft
> **创建时间**: 2026-01-31
> **更新时间**: 2026-01-31
> **当前阶段**: Align (对齐阶段) - Pivot to Blog Integration

## 1. 项目背景与洞察

### 1.1 核心洞察 (User Insight)
用户希望建立一个可追溯的学习记录系统：
*   **过程价值**: 学习不仅仅是记住结论，提出问题的过程（对话）同样珍贵，是思考的快照。
*   **内容形态**: 博客/笔记不仅要展示“知识点”，还要展示“我是如何通过提问到达这个知识点的”。
*   **痛点**: 手动整理对话记录、关联知识点非常繁琐，容易打断心流。

### 1.2 产品形态调整 (Pivot)
*   **核心定义**: **QuestMap** 是一个辅助生成“对话式学习博客”的 **AI Skill**。
*   **功能定位**: 连接 **"Process (对话)"** 与 **"Result (知识点)"** 的桥梁。
    *   自动将当前的对话转化为一篇格式完美的 Markdown 博客文章。
    *   自动提取对话中的 Core Concept（核心知识点）。
    *   自动建立 Question -> Concept 的引用链接。

---

## 2. 需求分析与边界 (Requirements & Boundaries)

### 2.1 核心能力 (Core Skills/Functions)
这个 Skill 主要负责“加工”和“归档”：

1.  **`generate_learning_blog(conversation_summary, key_questions, core_concepts)`**:
    *   **输入**: 当前对话的摘要、关键问题列表、涉及的核心概念。
    *   **输出**: 在 `Notes/` 或 `Blog/` 目录下生成一篇 Markdown 文件。
    *   **格式**: 包含 Front Matter (元数据)，对话实录（Q&A形式），以及“知识点卡片”。

2.  **`link_concept(concept_name)`**:
    *   如果知识点已存在（在 `Skills/` 目录下），自动创建双向链接 `[[Concept Name]]`。
    *   如果知识点不存在，提示用户是否创建新的知识点文件。

### 2.2 博客内容结构 (Blog Structure)
生成的博客文章应包含以下板块，构成完整的学习闭环：

1.  **元数据 (Front Matter)**:
    *   方便检索和归档。
    *   包含：标题、日期、标签、关联的核心概念（Wiki Link）、难度等级。

2.  **核心问题 (The Hook)**:
    *   一句话描述触发这次学习的“痛点”或“疑惑”。
    *   作用：让读者（或未来的自己）快速判断是否遇到过同样问题。

3.  **场景还原 (Context)**:
    *   描述问题产生的背景（例如：“在写一个爬虫时，发现内存一直在涨...”）。
    *   作用：提供上下文，让问题更具体。

4.  **探索过程 (The Journey)**:
    *   精简版的对话实录。
    *   **关键：保留“错误尝试”和“思维转折”**。不仅仅记录正确答案，更要记录“我是怎么想错的”以及“AI 是怎么纠正我的”。
    *   这是“过程价值”的核心体现。

5.  **核心归因 (The Root Cause)**:
    *   从现象收敛到本质。
    *   例如：“这个问题表面上是内存泄漏，本质上是对 Python 垃圾回收机制（引用计数）的不理解。”
    *   此处必须链接到 `Skills/` 下的系统性知识文档。

6.  **行动指南 (Actionable Takeaway)**:
    *   “下次遇到类似情况，我该怎么办？”
    *   提供代码片段或检查清单 (Checklist)。

7.  **延伸思考 (Open Questions)**:
    *   记录本次对话中未解决但有价值的新问题（留给下一次探索）。

### 2.3 数据存储
*   **对话记录**: 存放在 `Notes/` 目录（延续现有习惯）。
*   **知识点**: 存放在 `Skills/` 目录。
*   **索引文件**: `quest_map.json` (可选，用于辅助检索关系)。

---

## 3. 智能决策策略 (Technical Strategy)

### 3.1 架构设计
*   **Skill 名称**: `LearningBlogger`
*   **实现方式**: Python 脚本 `tools/learning_blogger.py`。
*   **工作流**:
    1.  用户对话结束时，指令：“把这次对话整理成学习博客”。
    2.  LLM 调用 `generate_learning_blog`。
    3.  Skill 读取模板，填充内容，写入文件。
    4.  LLM 告知用户：“已生成博客文章 `Notes/2026-xx-xx_Topic.md`，并关联了知识点 `Skills/Python/List.md`”。

### 3.2 文件模板 (Template)
```markdown
---
title: {topic}
date: {date}
tags: [{tags}]
concepts: [[{concept_1}]], [[{concept_2}]]
type: conversation-log
---

# {topic}

## 核心问题
> {key_question}

## 探索过程 (Dialogue)
**我**: {user_question_1}
**AI**: {ai_answer_summary_1}

...

## 归因与总结
这个问题最终帮助我理解了 [[{concept_1}]] 的核心机制...
```

---

## 4. 疑问澄清 (Questions to User)

1.  **博客平台**: 你目前的 Markdown 文件是打算直接在 GitHub 上看，还是会用 Hugo/Hexo/VitePress 之类的工具渲染成网页？（这决定了图片和链接的格式）。
2.  **精简程度**: 你希望博客是**“逐字逐句的完整记录”**（作为档案），还是**“经过提炼的精华”**（作为文章）？

---

## 5. 下一步行动 (Next Steps)
1.  **Architect**: 设计 Markdown 模板和 Python 生成逻辑。
2.  **Atomize**: 编写 `learning_blogger.py`。
3.  **Automate**: 尝试用这个 Skill 生成一篇关于“QuestMap”本身的博客。

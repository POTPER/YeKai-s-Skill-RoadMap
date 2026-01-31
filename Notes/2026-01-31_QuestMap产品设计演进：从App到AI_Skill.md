---
title: QuestMap产品设计演进：从App到AI Skill
date: 2026-01-31
tags: [ProductDesign, AI, MetaLearning]
concepts: [[[Skill Engineering]], [[First Principles]], [[Learning Traceability]]]
type: conversation-log
status: public
---

# QuestMap产品设计演进：从App到AI Skill

## 🎯 核心问题 (The Hook)
> 我想开发一款软件 QuestMap，记录我的问题并指向同一个答案。我知道知识很重要，但感觉问题更重要，是问题的根本原因驱动了学习。

## 🔍 场景还原 (Context)

在与 AI 结对编程的过程中，我发现自己经常遇到各种零散的问题。
起初我想做一个独立的 Web App 来记录这些问题和答案的映射关系。
但在讨论中，我意识到与其重复造轮子做一个笔记软件，不如利用 AI 的能力。
于是我们将产品方向从“独立的 App”转向了“AI Skill（工具）”，并最终定型为“自动生成学习博客的工具”。
    

## 💡 探索过程 (The Journey)
### 🙋 我
我想开发一款软件，能够记录我的问题。同时，它指向同一个答案。我知道可能有点复杂，但是这是在寻找答案的过程中。也就是我问出这个问题的根本原因。

### 🤖 AI
这非常有价值。我们可以做一个“学习归因工具”。
MVP 方案建议：Next.js + JSON 本地存储。

### 🙋 我
也不是一款产品，可能是一个skill ，按照一些规则，成为大模型可以使用的工具。

### 🤖 AI
深刻的洞察！这正是 Skill Engineering 的精髓。与其造 App，不如造“义肢”。我们将 QuestMap 重构为一个 AI Skill。

### 🙋 我
或者说这样的我想把我的问题和ai的答案以对话的形式 展现在我的博客中，结合我整理的相关知识点。形成我的学习记录过程，可以追溯。

### 🤖 AI
明白。产品形态再次迭代：LearningBlogger Skill。它连接“对话过程”与“知识结果”，自动生成博客。



## 🧠 核心归因 (Root Cause)
这个问题本质上是关于 **[[Skill Engineering]]** 的。

这个产品的演进过程，本质上是对 **[[Skill Engineering]]** 的一次实践。
起初我陷入了“App思维”，想做界面、做数据库。
后来回归到“第一性原理”：我的目的是**记录学习过程**，而不是**开发软件**。
AI 时代，最好的交互界面就是自然语言，最好的软件形态就是 AI Skill。
    

## ✅ 行动指南 (Actionable Takeaway)
- [ ] 使用 LearningBlogger 生成第一篇博客
- [ ] 完善 `quest_map_skill.py` 的更多功能（如自动搜索相似问题）

## 🔗 延伸思考
- 如何让这个 Skill 不仅能生成 Markdown，还能自动推送到我的 Hugo 博客并部署上线？

---
title: {{ topic }}
date: {{ date }}
tags: [{{ tags }}]
concepts: [{{ concepts_links }}]
type: conversation-log
status: public
---

# {{ topic }}

## 🎯 核心问题 (The Hook)
> {{ context_summary }}

## 🔍 场景还原 (Context)
{{ context_detail }}

## 💡 探索过程 (The Journey)
{% for turn in dialogue %}
### {{ turn.role_display }}
{{ turn.content }}
{% endfor %}

## 🧠 核心归因 (Root Cause)
这个问题本质上是关于 **{{ main_concept_link }}** 的。
{{ root_cause_analysis }}

## ✅ 行动指南 (Actionable Takeaway)
- [ ] {{ action_item_1 }}
- [ ] {{ action_item_2 }}

## 🔗 延伸思考
- {{ open_question }}

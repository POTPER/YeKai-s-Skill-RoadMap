# 我的工具箱

一个美观的HTML工具导航页面，用于记录和管理日常使用的工具。

## 使用方法

1. 直接在浏览器中打开 `index.html` 文件即可查看
2. 支持本地离线使用，无需服务器

## 如何添加新工具

### 方法1: 在现有分类中添加工具

在对应的 `<div class="tools-grid">` 中添加新的工具卡片：

```html
<div class="tool-card">
    <div class="tool-header">
        <h3 class="tool-name">工具名称</h3>
        <p class="tool-subtitle">工具副标题</p>
        <a href="https://your-tool-url.com" target="_blank" class="tool-link">
            访问官网 →
        </a>
    </div>

    <div class="tool-description">
        工具的详细描述...
    </div>

    <ul class="features">
        <li>特性 1</li>
        <li>特性 2</li>
        <li>特性 3</li>
    </ul>

    <div class="tags">
        <span class="tag">标签1</span>
        <span class="tag">标签2</span>
    </div>
</div>
```

### 方法2: 添加新分类

复制并取消注释模板代码，或者添加新的分类区块：

```html
<div class="category">
    <h2 class="category-title">🔧 新分类名称</h2>
    <div class="tools-grid">
        <!-- 在这里添加工具卡片 -->
    </div>
</div>
```

## 特性

- ✨ 现代化渐变背景设计
- 📱 响应式布局，支持移动端
- 🎨 卡片悬浮动画效果
- 🔖 标签系统
- 🔗 可点击链接直达工具官网
- 📝 清晰的特性列表展示

## 自定义

### 修改配色

在 `<style>` 标签中找到以下变量进行修改：

- 背景渐变: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- 主色调: `#667eea`
- 次要色调: `#764ba2`

### 调整布局

在 `.tools-grid` 样式中修改：

```css
grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
```

调整 `350px` 值可以改变卡片的最小宽度。

## 当前工具列表

- **qView** - 极简图像查看器

---

*持续更新中...*


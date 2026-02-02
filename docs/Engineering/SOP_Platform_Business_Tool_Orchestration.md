# SOP 实训平台：业务流调用“沉降检测”工具流的实现说明

## 1. 你提出的问题（产品视角）

你指出的核心点是对的：

- **“砌体结构沉降裂缝安全性鉴定”属于业务流程（Business Workflow）**
- **“沉降检测/沉降监测”属于技术工具流程（Technical Inspection / Tool Flow）**
- 正确的关系应当是：**业务流在某个步骤“调用”沉降检测工具流，工具流完成后回到业务流继续推进**

如果把“鉴定流程”和“沉降检测流程”写在同一条 SOP 里，学生/用户会分不清：哪些是管理/业务步骤（委托、调查、综合评级），哪些是技术采集步骤（布点、测量、读取数据）。

## 2. 本次改动结论（你现在能看到的效果）

在 `Demo/SOP_Platform/index.html` 中实现了一个最小可用的“子任务编排”机制：

- 业务任务 `assessment_01` 中的步骤 **“专项检测：裂缝”**、**“专项检测：沉降”** 现在都是 **SubTaskLauncher（子任务启动器）**
- 点击 “立即前往检测现场” 会进入对应的技术工具流：
  - `insp_crack`（裂缝专项检测）
  - `insp_settlement`（沉降/倾斜监测）
- 在工具流走到最后一步时，主按钮会显示 **“完成并返回”**
- 点击后会自动：
  - 返回业务流
  - 并且跳转到业务流的“下一步”（即：调用完工具后自动继续）

## 3. 关键实现（前端/架构知识点）

### 3.1 配置驱动（Config-driven）仍然是核心

平台沿用 `TaskDatabase` 作为“模拟后端配置数据”，体现 `Architecture_Design_SOP_Pattern.md` 里说的：

- **流程标准化，内容插件化**
- 通过 JSON-like 配置切换不同 SOP

业务流与技术流的区别体现在配置层：

- **业务流（Business Workflows）**：`assessment_01`
- **技术流（Technical Inspections / Tools）**：`insp_crack`、`insp_settlement`

### 3.2 引入“任务栈 taskStack”（调用/返回的最小模型）

为了实现“调用工具 -> 返回主流程”，本次新增：

- `currentTaskId`：记录当前任务 ID
- `taskStack`：用于保存“调用前”的上下文

当业务流调用工具流：

- 把当前上下文 `{ taskId, stepIndex }` push 进 `taskStack`
- 然后 `loadTask(subTaskId, { mode: 'subtask' })`

当工具流结束：

- 如果 `taskStack.length > 0`，说明这是一个“被调用的工具流”
- pop 出父流程上下文
- `loadTask(parent.taskId, { mode: 'restore', stepIndex: parent.stepIndex + 1 })`

这相当于前端里常见的：

- **导航栈（Navigation Stack）**
- 或者流程编排里的 **Call/Return（调用/返回）**

### 3.3 修复 loadTask 对 event 的隐式依赖

之前 `loadTask` 依赖 `event.target` 来做菜单高亮：

- 用户点击菜单时没问题
- 但子任务启动是“程序化调用”（不是点击菜单 DOM），此时 `event` 不存在，会导致报错

本次改为：

- 给菜单项添加 `data-task="任务ID"`
- `loadTask` 通过 `querySelector(.menu-item[data-task=...])` 选中并高亮

这是典型的前端工程实践：

- **避免隐式全局变量依赖（event）**
- **让函数可被程序调用（可测试、可复用）**

### 3.4 UI 反馈：工具流最后一步按钮显示“完成并返回”

为了减少用户疑惑，页脚主按钮文案会根据上下文变化：

- 普通流程最后一步：`提交任务`
- 子任务（taskStack 非空）最后一步：`完成并返回`

这是典型的产品/交互设计要点：

- **用户必须知道“下一步会发生什么”**

### 3.5 恢复 ParamSetup 组件，避免技术任务被误伤

你前面为了引入 `SubTaskLauncher` 替换了 `ParamSetup` 的 UI，这会导致：

- `strength_01` / `rebar_01` 中引用 `ParamSetup` 的步骤失效

本次把 `ParamSetup` 组件实现加回去，保证旧任务仍可运行（兼容性）。

## 4. 与土木工程实训内容的对应关系（业务 vs 技术）

以 `5.1_Practical_Training_Case.md` 为例：

- **业务流（鉴定/管理）**
  - 委托/初步调查
  - 综合评级/出结论
- **技术工具流（现场采集）**
  - 裂缝普查/精测
  - 沉降监测（布点、读数、倾斜率计算）

本次实现的结构保证：

- 业务流可重复复用不同工具（裂缝、沉降、强度、钢筋等）
- 工具流也可以被不同业务流程复用（比如“危房鉴定”“应急监测方案”“施工影响评估”都可能调用沉降监测）

## 5. 后续可迭代方向（可选）

- **数据回传机制升级**：从 `window.globalTilt` / `window.globalCrackWidth` 这种全局变量，升级为 `context` 对象（更接近真实前后端架构）
- **支持多层嵌套子任务**：例如业务流 -> 沉降监测 -> 基准点复核
- **真正的“返回并带数据”**：子任务结束时返回结构化结果（如 `{ tilt: 0.8, settlement: [...] }`），由父流程统一生成报告

---

文件关联：

- Demo 页面：`Demo/SOP_Platform/index.html`
- 实训案例：`Skills/CivilEngineering/5.1_Practical_Training_Case.md`
- Web 落地方案：`Skills/CivilEngineering/5.1_Web_Implementation_Plan.md`
- 架构模式：`Demo/Architecture_Design_SOP_Pattern.md`

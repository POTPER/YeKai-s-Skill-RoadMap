# 土木工程检测实训平台 - 模块化架构设计 (SOP Strategy Pattern)

## 1. 核心设计理念

**“流程标准化，内容插件化”**

我们将系统分为两层：
1.  **通用执行器 (Task Runner)**: 负责导航、计分、用户交互框架（UI Shell）。
2.  **业务策略包 (Business Strategies)**: 定义具体的检测逻辑、工具和规范。

---

## 2. 数据结构设计 (Config Driven)

我们需要用 JSON 配置来定义不同的检测任务，而不是写死代码。

### 2.1 裂缝检测 SOP (Crack Detection Strategy)
```json
{
  "task_id": "crack_01",
  "title": "砌体结构沉降裂缝检测",
  "standard_ref": "JGJ 125-2016",
  "steps": [
    {
      "step_id": 1,
      "type": "inspection",
      "name": "裂缝测绘",
      "ui_component": "CrackMapper", // 调用绘图组件
      "validation": "check_crack_shape" // 校验正倒八字
    },
    {
      "step_id": 2,
      "type": "analysis",
      "name": "机理推演",
      "ui_component": "ReasoningQuiz",
      "data": { "options": ["中间沉降", "端部沉降"] }
    }
  ]
}
```

### 2.2 混凝土强度检测 SOP (Concrete Strength Strategy)
```json
{
  "task_id": "strength_01",
  "title": "回弹法检测混凝土抗压强度",
  "standard_ref": "JGJ/T 23-2011",
  "steps": [
    {
      "step_id": 1,
      "type": "selection",
      "name": "测区布置",
      "ui_component": "GridSelector", // 调用网格选择组件
      "rule": "min_points_10" // 规则：至少10个测区
    },
    {
      "step_id": 2,
      "type": "operation",
      "name": "回弹操作",
      "ui_component": "ReboundHammerSim", // 调用回弹仪模拟器
      "params": { "angle": 0, "surface": "dry" }
    },
    {
      "step_id": 3,
      "type": "calculation",
      "name": "数据修正",
      "ui_component": "DataForm",
      "formula": "strength_conversion_table" // 查表计算
    }
  ]
}
```

---

## 3. 目录结构规划

```text
/Src
  /Core               <-- [不变] 标准化流程引擎
    TaskRunner.js     // 负责加载 JSON，渲染对应的 Step
    ScoreEngine.js    // 负责计分
    ReportGenerator.js // 负责最后生成报告
    
  /Components         <-- [通用] UI 组件库
    BaseMap.js        // 底图查看器
    ImageViewer.js    // 照片查看器
    
  /Modules            <-- [变化] 具体的业务SOP
    /Crack            // 裂缝包
      config.json     // 裂缝流程定义
      CrackTool.js    // 特有工具：裂缝尺
      
    /Strength         // 强度包
      config.json     // 强度流程定义
      ReboundHammer.js // 特有工具：回弹仪
      CarbonationRuler.js // 特有工具：碳化深度尺
```

## 4. 扩展性示例

当我们要新增一个 **“钢筋保护层厚度检测”** 时：
1.  **不需要** 修改 `/Core` 中的任何代码。
2.  只需要在 `/Modules` 下新建 `/Rebar` 文件夹。
3.  编写 `config.json` 定义流程（扫描 -> 标记 -> 钻孔验证）。
4.  开发一个 `Scanner.js` (钢筋扫描仪) 组件。

这就是 **开闭原则 (Open-Closed Principle)**：对扩展开放，对修改关闭。

# 钢筋扫描仪组件设计文档 (Scanner.js Component Design)

## 1. 组件状态 (State Model)

组件内部维护的数据状态：

```javascript
{
  // 设备状态
  power: false,       // 开关机
  mode: 'thickness',  // 模式：厚度检测 / 间距扫描
  
  // 交互状态
  probeX: 100,        // 探头当前 X 坐标 (px)
  probeY: 100,        // 探头当前 Y 坐标 (px)
  isScanning: false,  // 是否正在按住拖动
  
  // 实时读数
  signalStrength: 0,  // 信号强度 (0-100)
  currentValue: 0,    // 当前读数 (mm)
  
  // 标记数据
  marks: [            // 用户标记的点
    { x: 150, y: 100, type: 'rebar_axis' } 
  ]
}
```

## 2. 模拟数据层 (Simulation Data Layer)

为了让扫描仪工作，底图（虚拟墙面）必须包含不可见的“元数据”：

```javascript
// 虚拟墙面的“真值”配置
const wallData = {
  rebars: [
    // 竖向钢筋
    { type: 'vertical', x: 150, diameter: 12, cover: 25 }, 
    { type: 'vertical', x: 300, diameter: 12, cover: 28 },
    // 横向钢筋
    { type: 'horizontal', y: 200, diameter: 8, cover: 20 }
  ],
  interference: [ // 干扰物（如预埋管线）
    { type: 'pipe', x: 450, depth: 40 }
  ]
};
```

## 3. 核心算法逻辑 (Core Logic)

`Scanner.js` 需要一个 `calculateSignal()` 函数，实时计算探头位置与钢筋的距离：

1.  **输入**: 探头坐标 `(px, py)`。
2.  **计算**: 遍历 `wallData.rebars`，计算探头中心到每一根钢筋轴线的垂直距离 `d`。
3.  **响应曲线**: 模拟电磁场衰减。
    *   当 `d < 50px` (感应范围) 时，信号增强。
    *   当 `d = 0` (正上方) 时，信号 `100%`，厚度读数 = `rebar.cover`。
4.  **输出**: 更新 UI 上的数字和进度条。

## 4. UI 表现层 (Presentation Layer)

### 4.1 视觉元素
*   **主机屏幕**: Canvas 绘制，显示类似于真实仪器的 LCD 界面（信号波形图、数字大字）。
*   **手持探头**: 一个可拖拽的 DOM 元素或 Canvas Sprite，带有中心准星。
*   **操作面板**: “校准”、“存储”、“模式切换”按钮。
*   **扫描轨迹**: 当探头移动时，在屏幕上留下一条淡淡的轨迹，帮助用户确认扫过的区域。

### 4.2 音效反馈
*   利用 **Web Audio API** 生成不同频率的蜂鸣声。
*   信号越强 -> 频率越高 / 间隔越短（模拟“滴-滴-滴”变“滴~~~~”）。

---

## 5. 使用示例 (Usage in config.json)

在 `config.json` 中，我们这样调用它：

```json
{
  "step_id": 2,
  "type": "operation",
  "name": "扫描钢筋位置",
  "ui_component": "Scanner",
  "props": {
    "wall_id": "wall_A_upper_zone", // 加载特定的墙面数据
    "target_rebar_count": 3,        // 任务目标：找到3根钢筋
    "allow_marking": true           // 允许打标记
  }
}
```

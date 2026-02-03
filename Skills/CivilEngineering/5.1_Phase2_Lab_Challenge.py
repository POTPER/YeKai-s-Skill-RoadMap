import time

# ------------------------------------------------------------------
# Phase 2: 神经符号逻辑注入 (Debug Challenge)
# ------------------------------------------------------------------
# 任务目标: 
# 这是一个 "未对齐 (Misaligned)" 的 Agent 代码。
# 它虽然能运行，但完全不懂 JGJ 125 规范，而且逻辑混乱。
# 请运行它，观察它的胡言乱语，然后修改代码中的 TODO 部分，将其纠正。

class NeuroSymbolicAgent:
    def __init__(self):
        self.name = "Structural_Inspector_v0 (Untrained)"
        
        # --- [TODO 1] 错误阈值 ---
        # 现状: Agent 觉得 50mm 宽的裂缝才算危险 (太离谱了！)
        # 任务: 请查阅 JGJ 125 4.2.1，将 50.0 改为正确数值 (10.0)
        self.crack_threshold_mm = 50.0 
        
        # --- [TODO 2] 错误逻辑 ---
        # 现状: Agent 认为只要不是所有指标都超标，就不是危房 (平均主义害死人)
        # 任务: 将 "average" 改为 "max" (木桶效应)
        self.safety_protocol = "average" 

    def evaluate(self, crack_width):
        print(f"\n[Agent] 正在检测裂缝: 宽度 = {crack_width}mm")
        
        # 判定逻辑
        is_dangerous = crack_width > self.crack_threshold_mm
        
        if is_dangerous:
            print("   -> 判定: D级 (危险)")
            return "D"
        else:
            print(f"   -> 判定: 非D级 (安全) [因为 {crack_width} < {self.crack_threshold_mm}]")
            return "Non-D"

# ------------------------------------------------------------------
# 模拟运行
# ------------------------------------------------------------------
if __name__ == "__main__":
    print("="*40)
    print(" ⚠️  Agent 初始测试 (Before Training)")
    print("="*40)
    
    agent = NeuroSymbolicAgent()
    
    # 测试案例: 12mm 的裂缝
    # 预期结果: 既然 > 10mm，必须报 D级
    result = agent.evaluate(12.0)
    
    print("\n" + "-"*40)
    if result == "D":
        print("🎉 成功: Agent 正确识别了危房！")
    else:
        print("❌ 失败: Agent 漏报了危房！")
        print("   原因: 阈值设定过高 (50mm)，导致 12mm 的裂缝被放过了。")
        print("   操作: 请修改代码中的 self.crack_threshold_mm 为 10.0")

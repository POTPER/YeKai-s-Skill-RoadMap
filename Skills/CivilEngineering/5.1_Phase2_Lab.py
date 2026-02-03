import time
import sys

# ------------------------------------------------------------------
# Phase 2: 神经符号逻辑注入 (Neuro-Symbolic Logic Injection) Lab
# ------------------------------------------------------------------
# 这是一个模拟后端逻辑的 Python 脚本。
# 在实际的 ABL (Agent-Based Learning) 系统中，这段代码运行在服务器端，
# 负责接收用户(Mentor)制定的规则，并将其应用到 LLM 的决策流中。

class NeuroSymbolicAgent:
    def __init__(self):
        self.name = "Structural_Inspector_v1"
        self.memory = {
            "visual": ["Inverted-V Crack (倒八字裂缝)", "Top Vertical Crack (顶部竖向裂缝)"],
            "environment": ["Deep Excavation (深基坑)", "Apron Displacement (散水坡错位)"]
        }
        # 初始状态：Agent 是空白的，没有判据
        self.rules = {
            "crack_threshold_mm": float('inf'), # 默认无穷大（不知敬畏）
            "tilt_threshold_percent": float('inf'),
            "causal_logic": None,
            "safety_protocol": "balanced" # balanced (avg), conservative (max)
        }
        print(f"[System] {self.name} initialized.")
        print(f"[System] Memory loaded: {self.memory}")

    def inject_thresholds(self, crack_mm, tilt_pct):
        """逻辑链 A: 注入量化阈值"""
        print(f"\n>> 正在注入规则 A (JGJ 125 阈值)...")
        time.sleep(0.5)
        self.rules["crack_threshold_mm"] = crack_mm
        self.rules["tilt_threshold_percent"] = tilt_pct
        
        # 校验反馈
        if crack_mm == 10 and tilt_pct == 1.0:
            print("   [√] 成功: 阈值符合 JGJ 125-2016 第 4.2.1 条。")
        else:
            print(f"   [!] 警告: 检测到非标阈值 (标准值应为 10mm, 1%)。Agent 行为可能偏离规范。")

    def inject_causality(self, conclusion_type):
        """逻辑链 B: 注入因果图谱"""
        print(f"\n>> 正在注入规则 B (因果逻辑)...")
        time.sleep(0.5)
        self.rules["causal_logic"] = conclusion_type
        
        # 校验反馈
        if conclusion_type == "settlement":
            print("   [√] 成功: 逻辑链 '倒八字 + 深基坑 -> 差异沉降' 符合土力学原理。")
        elif conclusion_type == "temperature":
            print("   [x] 错误: 逻辑冲突。倒八字裂缝通常不是由温度应力引起的（温度裂缝多为正八字或水平）。")
        else:
            print("   [?] 未知: 注入了模糊的逻辑。")

    def set_safety_bias(self, mode):
        """逻辑链 D: 注入安全偏好 (木桶效应)"""
        print(f"\n>> 正在注入规则 D (冲突仲裁)...")
        time.sleep(0.5)
        if mode not in ["average", "max"]:
            print("   [!] 错误: 无效的模式。")
            return
        
        self.rules["safety_protocol"] = mode
        if mode == "max":
            print("   [√] 成功: 已启用 '保守模式' (木桶效应/最大值原则)。")
        else:
            print("   [!] 警告: 已启用 '平衡模式' (平均值)。在工程鉴定中可能导致漏报 D 级危房。")

    def evaluate(self, case_crack, case_tilt):
        """运行推理引擎 (Inference Engine)"""
        print(f"\n[Agent] 正在评估案例: 裂缝={case_crack}mm, 倾斜={case_tilt}%")
        
        # 1. 独立评级
        rating_crack = "D" if case_crack > self.rules["crack_threshold_mm"] else "Non-D"
        rating_tilt = "D" if case_tilt > self.rules["tilt_threshold_percent"] else "Non-D"
        
        print(f"   - 裂缝评级: {rating_crack}")
        print(f"   - 倾斜评级: {rating_tilt}")
        
        # 2. 综合评级 (应用安全偏好)
        final_rating = "Unknown"
        
        if self.rules["safety_protocol"] == "max":
            # 木桶效应：只要有一个是 D，结果就是 D
            if rating_crack == "D" or rating_tilt == "D":
                final_rating = "D级 (整幢危房)"
            else:
                final_rating = "非 D级"
        else:
            # 平均化（错误逻辑）：如果一个D一个非D，可能判为C
            if rating_crack == "D" and rating_tilt == "D":
                final_rating = "D级 (整幢危房)"
            elif rating_crack == "D" or rating_tilt == "D":
                final_rating = "C级 (局部危房) [风险: 被平均化]"
            else:
                final_rating = "非 D级"
                
        return final_rating

# ------------------------------------------------------------------
# 交互式实训流程 (Main Loop)
# ------------------------------------------------------------------
def run_lab():
    agent = NeuroSymbolicAgent()
    
    print("\n" + "="*50)
    print("实训任务: 请根据 JGJ 125 规范教育你的 Agent")
    print("="*50)

    # --- Step 1: 阈值注入 ---
    print("\n[参考资料] JGJ 125-2016 第 4.2.1 条:")
    print("承重砌体墙产生宽度大于 10mm 的沉降裂缝，或房屋整体倾斜率大于 1%...")
    
    try:
        c_limit = float(input("\n请输入 D 级裂缝宽度阈值 (mm): "))
        t_limit = float(input("请输入 D 级倾斜率阈值 (%): "))
        agent.inject_thresholds(c_limit, t_limit)
    except ValueError:
        print("输入错误，使用默认宽松阈值。")
        agent.inject_thresholds(20, 2)

    # --- Step 2: 逻辑注入 ---
    print("\n[逻辑选择] 面对 '倒八字裂缝' 和 '深基坑'，Agent 应得出什么结论？")
    print("1. 温度应力 (Temperature)")
    print("2. 差异沉降 (Settlement)")
    choice = input("请选择 (1/2): ")
    logic_map = {"1": "temperature", "2": "settlement"}
    agent.inject_causality(logic_map.get(choice, "unknown"))

    # --- Step 3: 安全偏好 ---
    print("\n[冲突仲裁] 当裂缝很严重(D)但倾斜很小(A)时，如何定级？")
    print("1. 取平均值 (可能定为 C 级)")
    print("2. 取最大值 (木桶效应，定为 D 级)")
    bias_choice = input("请选择 (1/2): ")
    bias_map = {"1": "average", "2": "max"}
    agent.set_safety_bias(bias_map.get(bias_choice, "average"))

    # --- Unit Tests ---
    print("\n" + "-"*30)
    print("运行单元测试 (Unit Tests)")
    print("-" * 30)
    
    # Case A: 边界测试
    # 9.8mm (接近 10mm 但未超), 0.6%
    print("\n>> Case A (边界测试): 裂缝 9.8mm, 倾斜 0.6%")
    res_a = agent.evaluate(9.8, 0.6)
    print(f"   => 最终判定: {res_a}")
    
    # Case B: 关键风险测试
    # 12mm (超标), 0.2% (正常)
    print("\n>> Case B (关键风险): 裂缝 12.0mm, 倾斜 0.2%")
    res_b = agent.evaluate(12.0, 0.2)
    print(f"   => 最终判定: {res_b}")
    
    # 总结
    print("\n" + "="*50)
    if "D级" in res_b and "非 D级" in res_a:
        print("🎉 恭喜！Agent 已成功通过图灵测试（符合工程师逻辑）。")
    else:
        print("❌ 实训失败：Agent 的判断逻辑存在漏洞，请重新调整规则。")
        if "D级" not in res_b:
            print("   (原因: Case B 漏报了危房，可能是阈值过高或使用了平均化仲裁)")

if __name__ == "__main__":
    run_lab()

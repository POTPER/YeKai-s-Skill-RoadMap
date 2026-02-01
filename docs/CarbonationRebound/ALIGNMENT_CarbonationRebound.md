# ALIGNMENT: Carbonation Depth & Rebound Hammer Experiment

## 1. Project Context
- **Current File**: `Skills/CivilEngineering/SimulationDemo/index.html`
- **Current Function**: Simulates Carbonation Depth measurement (Drill -> Clean -> Drop Phenolphthalein -> Measure).
- **Goal**: Iterate the experiment to include Rebound Hammer (回弹仪) testing, forming a complete "Rebound-Carbonation Method" (回弹-碳化法) for concrete strength assessment.

## 2. Requirement Understanding
- **New Tool**: Rebound Hammer (回弹仪).
- **New Workflow**:
  1.  **Rebound Test (回弹测试)**: 
      -   Show a test area (zone).
      -   Grid of 16 test points (4x4).
      -   User uses Rebound Hammer on each point.
      -   Record 16 values.
      -   Calculate Mean Rebound Value ($R_m$) according to standard (remove 3 max, 3 min, average remaining 10).
  2.  **Carbonation Depth (碳化深度)**:
      -   (Existing steps) Drill -> Clean -> Drop -> Measure ($d_m$).
  3.  **Strength Estimation (强度推算)**:
      -   Use $R_m$ and $d_m$ to lookup/calculate Concrete Strength ($f_{cu}$).

## 3. Standards & Regulations
- **Standard**: **JGJ/T 23-2011** "Technical Specification for Inspection of Concrete Compressive Strength by Rebound Method" (回弹法检测混凝土抗压强度技术规程).
- **Key Rules**:
  -   Test Area: 20cm x 20cm usually.
  -   Points: 16 points.
  -   Calculation: Mean = Sum(10 middle values) / 10.
  -   Strength: Formula based on $R_m$ and $d_m$.

## 4. Ambiguities & Decisions
- **Q1**: Should we simulate the *angle* of the hammer (horizontal, upward, downward)?
  -   *Decision*: Assume **Horizontal** (0 degrees) for simplicity, as it's a wall.
- **Q2**: Should we simulate the *casting surface* (side, top, bottom)?
  -   *Decision*: Assume **Side** (casting direction is horizontal), testing on the side. No correction needed for top/bottom.
- **Q3**: How detailed should the rebound animation be?
  -   *Decision*: Simple animation: Hammer moves to point -> piston retracts/hits -> value displays.
- **Q4**: Should we implement the full lookup table or a simplified formula?
  -   *Decision*: Use a simplified fitting formula or a small lookup table for demonstration purposes.

## 5. Technical Specification
- **Tools Array**: Add `{ id: 'hammer', name: '回弹仪', icon: '🔫' }`.
- **Steps**: Insert 'Rebound Test' before 'Drill'.
- **Visuals**:
  -   Draw 4x4 grid points on the wall.
  -   Visual feedback for tested points (change color/show value).
  -   Panel to show the list of 16 values.

## 6. Acceptance Criteria
1.  User can select Rebound Hammer.
2.  User can click/drag to 16 points to get readings.
3.  System automatically calculates $R_m$ (excluding outliers).
4.  User proceeds to Carbonation Depth test (existing).
5.  Final result shows Strength estimate.

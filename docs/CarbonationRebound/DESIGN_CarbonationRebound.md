# DESIGN: Carbonation & Rebound Integration

## 1. System Architecture
- **Framework**: Vue 3 + Konva.js (Single File HTML).
- **State Management**: Vue Reactive `ref`.

## 2. Data Model
```javascript
const state = {
  currentStep: 0, // 0:Rebound, 1:Drill, 2:Clean, 3:Drop, 4:Measure
  reboundValues: [], // Array of 16 integers
  reboundMean: 0,
  carbonationDepth: 0,
  trueStrength: 35.0 // MPa (Target)
};
```

## 3. UI Layout
- **Main Canvas**:
  -   **Left/Center**: Wall surface.
      -   **Rebound Grid**: 4x4 points, spaced 40mm (approx 160px).
      -   **Drill Hole**: Center of the wall (hidden initially).
  -   **Right/Overlay**: Data Panel.
      -   Display 4x4 matrix of rebound values.
      -   Display calculated Mean (after 16 points).

## 4. Interaction Flow
1.  **Step 0: Rebound Test**
    -   User selects "Rebound Hammer".
    -   Grid points appear on wall.
    -   User clicks a point.
    -   **Animation**: Hammer moves to point -> "Click" sound/visual -> Value appears (e.g., 38).
    -   Repeat for 16 points.
    -   **Calc**: $R_m = \frac{\sum_{i=4}^{13} sorted(R_i)}{10}$.
    -   Button: "Finish Rebound" -> Transition to Drill.

2.  **Step 1-4: Carbonation (Existing)**
    -   Drill -> Clean -> Drop -> Measure.
    -   (No major changes, just indexing shift).

3.  **Step 5: Result**
    -   Show $R_m$ and $d_m$.
    -   Show Estimated Strength (Formula).

## 5. Technical Implementation
-   **Hammer Tool**: Needs a `performRebound(pos)` function.
-   **Grid Generation**: Loop 4x4, create Konva Circles.
-   **Value Generation**: `Math.round(TRUE_STRENGTH + Random(-3, 3))`.
-   **Strength Curve**: Use a simplified linear or power function approx for C30-C40 range. 
    -   Example: $f_{cu} = 0.025 \cdot R_m^{1.8} \cdot 10^{-0.05 d_m}$ (Just a placeholder, will use standard curve approx).
    -   JGJ/T 23-2011 standard curve is complex, we can use a lookup table or a simplified polynomial.
    -   For demo: $Strength = R_m \times 0.8 - d_m \times 1.5$ (Rough approx).

## 6. Interfaces
-   `calculateReboundMean(values)`
-   `getStrength(rm, dm)`

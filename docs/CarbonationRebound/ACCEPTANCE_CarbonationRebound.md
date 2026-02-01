# ACCEPTANCE: Carbonation & Rebound Integration

## 1. Feature Verification
- [x] **Rebound Hammer Tool**: Added to toolbar with icon.
- [x] **Rebound Step**: First step requires Hammer.
- [x] **Grid Visualization**: 4x4 grid appears on canvas.
- [x] **Interaction**: Clicking/Dragging hammer to points updates `reboundValues`.
- [x] **Calculation Logic**: Rm calculated correctly (16 values -> sort -> trim 6 -> mean).
- [x] **Data Panel**: Real-time display of 16 values in the top-right corner.
- [x] **Transition**: Flow moves to "Drill" step after rebound is done.
- [x] **Carbonation Flow**: Existing flow (Drill->Clean->Drop->Measure) works as before.
- [x] **Final Report**: Shows Rm, dm, and estimated Strength.

## 2. Code Quality
-   Vue 3 Composition API used consistently.
-   Konva.js integration for visual grid and animations.
-   Tailwind CSS for UI styling.
-   No console errors expected.

## 3. User Experience
-   Clear guidance at top ("Current Step").
-   Visual feedback when hitting rebound points (color change, scale).
-   Report provides immediate feedback on accuracy.

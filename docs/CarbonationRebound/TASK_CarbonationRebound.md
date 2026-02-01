# TASK: Carbonation & Rebound Implementation

## 1. Setup & State
- [ ] Add 'hammer' to `tools`.
- [ ] Insert 'Rebound Test' at start of `steps`.
- [ ] Add `reboundValues` (ref array), `reboundFinished` (ref bool).

## 2. Visual Components
- [ ] Create `drawReboundGrid()` function: Draws 4x4 circles on Konva layer.
- [ ] Create `drawHammer()` or use simple icon for cursor/animation.
- [ ] Create `ReboundPanel` Vue component (or just HTML overlay) to show the 16 values.

## 3. Interaction Logic
- [ ] Implement `performRebound(pos)`:
    -   Check if clicking a valid grid point.
    -   Check if point already tested.
    -   Generate value.
    -   Update state.
    -   Visual feedback (color change, text number).
- [ ] Implement `calculateReboundStrength()`:
    -   Sort values.
    -   Remove top 3, bottom 3.
    -   Average remaining 10.

## 4. Integration
- [ ] Update `handleToolAction` switch case.
- [ ] Ensure transition from Rebound -> Drill works (Grid should fade out or stay as context).
- [ ] Update `submitResult` to include Rebound data in the alert/report.

## 5. Refinement
- [ ] Add "Assessment Mode" vs "Training Mode" (Optional, keeping it simple for now as per "Iterate" request).
- [ ] Polish animations.

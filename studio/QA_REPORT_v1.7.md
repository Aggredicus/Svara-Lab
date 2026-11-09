# Svara Play v1.7 — QA evidence

## Scope
Reorder existing eight editing utilities and gently highlight the three highest-priority controls. Preserve every music, Sanskrit typing, Gāyatrī and clipboard function. No new data collection, dependencies or permissions.

| Test suite | Passed |
|---|---:|
| Existing studio audio/music and exports | 192 |
| Compact keyboard, layout and editing | 175 |
| Gāyatrī library and accent display | 175 |
| Emulated simultaneous touch/swipe | 3 |
| New utility-order, geometry and functionality checks | 86 |
| **Total** | **631** |

All 631 local Chromium/Playwright checks passed across the respective suites. New tests covered widths 320, 360, 390, 428, 780 (landscape) and 1440px.

The pinned board remained below 50% of viewport height and without internal scrolling. Verified the new utility order, caret movement, Unicode virāma insertion, space, backspace, undo, copy and paste. No page JavaScript exceptions in the focused suite.

## Limits
The relative frequency scores for non-text symbols are heuristics; 272 spaces and 257 virāmas were directly counted from the app's 38 mantra selections, not from individual user behavior. The 38% reach reduction is a simplified geometric model, not a usability study. Physical Android thumb testing and independent human review remain outstanding.

The previous v1.6 source is recoverable on its own branch; no changes to `main`.

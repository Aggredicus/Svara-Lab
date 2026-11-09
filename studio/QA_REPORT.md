# Svara Play v1.4 — release QA report

**Target:** `feature/svara-modal-keyboard-v1.4` of `Aggredicus/Svara-Lab`. The earlier `main`, v1.2, and v1.3 branches are not modified.

## Automated verification

- **192 / 192 passed** — previous v1.3 Playwright regression checks on 1440×900, 390×844, and 360×750 Chromium viewports: scale/key synchronization, all 72 melakarta scales, rāga/tāla catalogs, studio/audio controls, stop all, loops, drawers, pitch and MIDI/JSON exports, no horizontal page overflow, no JS errors.
- **108 / 108 passed** — new v1.4 keyboard checks across the same three viewports: center tapping, swipes up/right/down/left, hold-and-tap directional menu, vowel mātrā, cursor position preservation, pin/unpin, collapse/expand, position lock, live preview, mobile keyboard suppression toggle, copy-all, copy-selection, clipboard paste, denied-clipboard manual-paste fallback, target switching to in-app search field, no page errors/overflow.
- **Touch emulation:** Chromium DevTools `Input.dispatchTouchEvent` successfully exercised a real touch-style right-swipe (selects `ग`), long-hold menu and left-choice tap (selects `ङ`), and two simultaneous thumbs with reverse release order (correct consonant-vowel result `कि`). These are three separate checks outside the 300 test assertions above.
- **JavaScript:** all inline scripts passed Node's syntax check.
- **Security:** no external runtime assets or networking; existing restrictive no-network CSP preserved; dynamic clipboard / text preview content uses text nodes; test-only mocks not shipped in app.

## Findings corrected during implementation

1. Original flick controls did not visibly map each direction and exposed no hold-to-choose menu.
2. Copied text fallback could temporarily redirect the keyboard's target to the hidden copy textarea; that temporary element is now excluded.
3. Collapsing the keyboard initially only affected the pinned surface; both inline and pinned modes now collapse correctly.
4. Original small phone layout displayed eight tiny flick keys per row; pinned mobile keyboard now stacks the consonant/vowel grids with larger keys, while the editing preview remains sticky while scrolling.
5. Two-finger input could lose a character and invert ordering; pointer gestures now reserve an input ticket on touch-down and commit in press order.

## Known limitations and release gate

- Automated browser emulation is not identical to testing on physical Pixel/Android and iOS devices; check gesture reliability, safe-area docking, keyboard suppression, font shaping, voice/audio latency, and clipboard permission variations on hardware.
- When clipboard reads are blocked by browser security, a manual paste box is provided instead of silent failure.
- A pinned keyboard can obscure app controls by design; users may collapse, drag (when unlocked), unpin, or scroll its contents.
- Scientific, educational, historical, and phonetic caveats from v1.3 remain; no claim of authentic gamakas or accurate classical Sanskrit pronunciation.
- No GitHub-hosted CI status is claimed for this branch; this report describes local Chromium runs.

**Release status:** branch-ready standalone HTML feature build; local automated tests pass. Physical hardware/user acceptance review remains open.
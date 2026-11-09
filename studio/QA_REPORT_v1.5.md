# Svara Play v1.5 — Functional and layout QA

**Branch:** `feature/svara-compact-thumb-keyboard-v1.5`

## Tested and passed

- Full existing music studio Playwright regression: **192/192** (desktop, 390 × 844, 360 × 750); includes rāga switching, tāla, audio start/stop, composer, MIDI/JSON export, UI interactions and layout.
- Compact keyboard Playwright suite: **175/175** across **1440×900, 428×926, 390×844, 360×750 and 320×568**. Tests half-height cap, no internal scrolling or horizontal overflow, two-thumb alignment, five-position arrow-free glyph previews, live text and caret, left/right movement, space, grapheme-aware backspace, per-field undo, select/clear, device IME toggle, other-field input, copy/paste, hold menu, collapse and expand.
- Chrome DevTools Protocol emulated multitouch: **3/3** from existing touch suite (swipe and multi-touch input/order).
- Additional manual browser-geometry checks: **844×390, 780×360, 667×375, 320×320**. No key clipping observed; heights stayed below 50% viewport.
- JavaScript syntax check: **pass** using Node.js `--check` on the extracted scripts.
- Captured screenshots for desktop and small phone sizes; reviewed layout visually.

**Total automated functional assertions: 370 passed, 0 failed.** The four landscape measurements are additional inspected geometry checks, not included in the assertion total.

## Fixed during review

1. Original pinned UI stacked two full keyboards and used a large toolbar, causing scrolling and covering much of the screen. Replaced with side-by-side two-thumb grids of three short rows, a short target picker, and one-line caret-tracking preview.
2. Directional variants used arrows and multiple visual labels. Keys and hold popup now show only five Devanāgarī glyphs arranged by selection direction; semantic direction names remain available to assistive technology.
3. Old backspace dispatch could run a composer-only handler, deleting unexpected Sanskrit clusters and modifying the wrong field. The thumb backspace now goes through a target-aware handler and includes trailing spaces as graphemes.
4. Undo from secondary text fields previously affected the composer. Independent per-target edit history is used for those fields.
5. An early 780×360 landscape layout clipped the final utility row. Added height-sensitive compact sizing.

## Outstanding risks

- Automated Chromium touch emulation cannot establish feel, latency, or accessibility of swipes on an actual Pixel, iPhone, or low-powered tablet.
- Small Devanāgarī variant labels at 320 px wide may be hard to read for users with low vision; larger accessibility mode remains a potential enhancement.
- Browsers may deny clipboard permissions and may vary in support for `inputmode="none"`. Manual paste and a native-keyboard toggle are provided.
- Whole-glyph deletion depends on `Intl.Segmenter`; a codepoint fallback is provided for older browsers.
- No remote CI checks have been executed by the GitHub host. The tests reported above were run locally in the container.
- No `main` merge or Pages deployment has been performed.

## Rollback

Switch back to `feature/svara-modal-keyboard-v1.4` or use its `studio/index.html`. No existing files on `main` are changed by this release.
# Svara Play v1.5 — Compact two-thumb Sanskrit keyboard

This is a completely offline, single-file HTML music and Sanskrit practice app. The **v1.5 update** redesigns the pinned modal keyboard while retaining the existing Svara Play piano, movable Sa, rāga and tāla explorers, pronunciation experiment, seven-sound composer, art and learning tools.

## How to use

1. Open `index.html` (or `Svara_Play_v1.5.html`) directly in a modern browser. No account, server, app store or network is required.
2. Open **Sanskrit keyboard** in the musical studio and select **Pin**.
3. The pinned panel stays at **half the viewport height or less**, with consonant keys on the left and vowel keys on the right even on phones. The panel is sized to fit without scrolling through keyboard keys.
4. **Tap** a key for its center letter; **swipe up/right/down/left** for the letter shown at that position; or **hold** and tap the desired letter in the pop-up. The five letter glyphs occupy their natural positions without directional arrows.
5. The lower rows include **Undo, caret left, virāma/join, space** (left group) and **caret right, backspace, copy, paste** (right group). The top **⋯** menu holds select all, copy selected, clear active field, and the device-keyboard toggle.
6. Select the text field using the compact target selector, or tap any editable text field within the application. A one-line live preview keeps the active phrase and cursor visible while you type.
7. Use **Fold** for an even smaller preview, **Lock** to stop repositioning, or **Unpin** to restore the full inline view. **Device keyboard** lets Android/iOS show its standard keyboard when you prefer.

## Text editing conventions

- Sanskrit vowels typed after consonants become appropriate Devanāgarī mātrās; **्** creates conjuncts. This is Unicode orthography, not proof of authentic phonetic synthesis.
- **Backspace** deletes the preceding Unicode grapheme, including a trailing space, not simply the preceding nonspace syllable.
- **Undo** applies to the active text field, so changes in a search field no longer undo your composer phrase. The original seven-sound undo history remains intact.
- Copy and paste use the browser clipboard APIs where allowed; a manual paste dialog appears when clipboard reading is unavailable. All clipboard operations occur locally.
- The preview follows the caret; the text field remains independently editable with selection and normal system input.
- The modal keyboard targets text fields **inside the Svara Play document**, not arbitrary text fields in other browser tabs or apps.

## Public release scope

The code remains under the original MIT-license header and inherits the music-source attributions and cautions documented in the application. Rāga phrases are educational simplifications; piano tones and experimental vowel formants do not replace trained pronunciation or authentic rāga/gamaka performance. The app does not fetch scripts, audio samples or fonts over the network. Browser storage may be restricted under private or `file://` contexts; export JSON to keep a backup.

## Testing

Run in a Python environment with Playwright and Chromium:

```bash
python tests/test_studio.py
python tests/test_compact.py
python tests/test_touch.py
```

The tests use an in-memory HTML page load and browser simulations. See `QA_REPORT_v1.5.md`. Physical Android/iOS device tests and human Sanskrit UX review remain recommended before moving the public default branch or deploying GitHub Pages.

## GitHub preservation

Published on `feature/svara-compact-thumb-keyboard-v1.5`, branched from `feature/svara-modal-keyboard-v1.4`. The original `main`, earlier feature branches, and root VĀṆĪ `index.html` are intentionally untouched. The updated app is `studio/index.html` on the new branch.
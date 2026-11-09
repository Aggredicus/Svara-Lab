# Svara Play v1.4 — Gesture Keyboard

Svara Play is an **offline, single-file** Indian classical music learning studio. Version 1.4 improves the Sanskrit modal keyboard while preserving the v1.3 music studio, piano, seven-sound composer, rāga and tāla explorers, 72 melakarta scales, lessons, symbolic references, MIDI/JSON export, and local notebook.

## Open

Download `Svara_Play_v1.4.html` and open it directly in a Chromium-based, Firefox or Safari browser. Audio starts after a user interaction on many phones. No accounts, CDN, permissions, microphone or internet access are needed for the main studio. Copy/paste buttons may need browser clipboard permission; a manual paste fallback is built in.

## Quick keyboard guide

1. Find **Your seven-sound phrase**, then tap **अ Sanskrit keyboard**, or open the **Sanskrit keyboard** expandable section.
2. Tap any letter for its center symbol (`क` for the first consonant key).
3. **Press and slide** up, right, down, or left to select the corresponding alternate (`ख`, `ग`, `घ`, or `ङ`). The floating directional menu highlights the current choice. Release to enter it.
4. **Press and hold** without moving for approximately 350 ms, then release. The five-choice popup remains visible; tap one of the choices to insert it. For a screen reader or hardware keyboard, focus a key and use **Arrow keys** for variants or **Enter/Space** for center.
5. Press **⌖ Pin** to float the keyboard over the app, including when scrolling between music controls and text fields. **▾ Fold** collapses it into a compact live text preview. When pinned, drag its title to move it or activate **🔒 Lock** to keep the chosen position. **⌖ Unpin** returns it to the inline drawer. A compact phone-sized pinned layout provides larger keys in stacked consonant and vowel groups.
6. Tap a text field or use **Write into** to choose where keyboard keystrokes go. The preview shows the current text and caret position even when the keyboard is pinned and the original field is outside the viewport. You can target the seven-sound phrase and in-app text search fields; ordinary checkboxes and selection controls are not text-editable.
7. Use **Copy text**, **Copy selected**, **Paste**, or **Select all** in the keyboard toolbar. The phrase also has **Copy phrase** and **Paste phrase** shortcuts. On browsers that block clipboard reads (including some local-file contexts), **Paste** opens an in-app paste box; long-press and paste there, then tap **Insert pasted text**.
8. In the pinned keyboard, **Device keyboard** is off by default for the composer text box to prevent the Android keyboard from covering the musical keys; switch it on if you prefer ordinary typing. Unpinning restores normal text-input behavior.

## Sanskrit and input semantics

- Vowel keys insert an independent vowel by default. Immediately after a consonant, they insert the corresponding dependent vowel mark (mātrā) where appropriate. For example, `क` followed by up on `अ` gives `का`. `क` followed by up on `इ` gives `की`.
- Vowel variants include long vowels (up), anusvāra (right), visarga (down), and candrabindu (left). They are orthographic options, **not** a verified pronunciation model.
- **Virāma / join** enables conjunct consonant sequences; backspace deletes a Unicode grapheme when supported.
- Multiple simultaneous touches are queued in touch-down order, so lifting your thumbs out of order does not reverse the typed sequence.
- Insertion respects the text cursor/selection of the chosen in-app field. Ordinary pastes and direct physical typing continue to work.
- The seven-sound engine maps the first seven selected input units to musical events; text beyond seven is preserved but not sounded. Symbol-to-pitch mappings are educational/creative; they are not ancient Sanskrit musical notation.

## Preserved features

- Movable Sa across all 12 pitch classes, quick rāga changes without switching screens, optional automatic scale preview, adjustable tempo, drone, piano and note playback.
- Seven-sound composer with Latin/Devanāgarī/sargam entry, rāga-safe paths, different pitches/timbres, audible phrase/tāla pairing, looping, stop-all, transpose/compare.
- Scale library including 24 curated rāgas, 10 Hindustani thāṭs and 72 melakarta parent scales.
- 54 tāla/rhythm configurations (including 35 Sulādi Sapta combinations), tihāī, beat-group display and synthetic percussion.
- Ear training, lessons, chakra/svara symbolism distinguished from historical melakarta chakra categories, Sanskrit synthetic vowels, saved phrases, JSON and MIDI export.

## Running checks

Install Chromium and Python Playwright, then run:

```bash
python -m pip install playwright
python studio/tests/test_studio.py
python studio/tests/test_keyboard.py
```

The first script is the unchanged v1.3 regression suite. The second adds actual mouse gesture, hold, movable/collapsible keyboard, clipboard fallback, caret, and text-field targeting checks across desktop and narrow viewports. An additional DevTools touch-emulation check tested directional swipes, hold-and-tap, and overlapping thumb presses. See `studio/QA_REPORT.md`.

## Technical and security notes

`studio/index.html` retains the existing self-contained Web Audio and UI modules and adds an isolated `svara-modal-keyboard-v14` styling/behavior layer. No external scripts, fonts, or network calls are made. The app retains the existing CSP and MIT license statement. Dynamic user text is rendered through DOM text nodes, not injected as HTML. The clipboard fallback does not upload or transmit text. Browser localStorage is used for phrase persistence, not cloud sync.

This work is published to `feature/svara-modal-keyboard-v1.4`, derived from `feature/svara-play-unified-v1.3`. The root VĀṆĪ `index.html`, `main`, and all previous feature branches are preserved. No automatic GitHub Pages deployment or merge is performed.

## Limitations

A browser clipboard permission may be unavailable on `file://`; use the manual paste fallback. Mobile keyboard and phonetic rendering vary between devices. Piano/rāga synthesis remains a fixed-pitch educational approximation rather than validated traditional performance or spoken Sanskrit. Real Android and iOS device checks and review by Sanskrit-speaking musicians remain recommended before broad public launch.
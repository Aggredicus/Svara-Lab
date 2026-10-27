# Using Svara Lab's phone-keyboard switch (v1.7)

**Where:** Type workspace, beside the Sanskrit composition field. Switch text reads **Phone keys OFF** or **Phone keys ON**.

**OFF** (default for coarse-pointer phones): tapping the Devanāgarī text field does not invoke the native system keyboard because the field is temporarily non-editable (`contenteditable=false`). Keep composing with the two-thumb Sanskrit flick keyboard and Join/Space/Undo. Your text remains intact.

**ON:** the field becomes editable and supports the phone's software keyboard, paste, and hardware keyboard. The two-thumb keys continue to work. If the system keyboard opens and shrinks the visible viewport, Svara Lab compacts secondary chrome and prioritizes keeping both Sanskrit thumb pads visible. Switch OFF again when you prefer the custom keyboard.

**Desktop and hardware-keyboard environments:** defaults ON. The preference is saved locally when browser storage permits. Changing it does not affect system-wide keyboard preferences.

The browser may ignore `inputmode=none` or lack the experimental VirtualKeyboard API; the reliable OFF strategy is non-editability. The app tries to hide the OS keyboard when disabled, but OS/browser behavior varies.

## Regression and known limits

- Public and private editions: 162/162 scripted touch/layout checks passed over five device profiles, including a 568×320 landscape viewport.
- Public repeatable test: 68/68 assertions passed after adding a regression for **turning the switch OFF while the editor is still focused and the simulated keyboard-open viewport is reduced**.
- Audio engine: 15/15 checks per edition; 34/34 consonant mappings.
- These are **simulated Chromium viewport and pointer tests**, not physical Gboard/Safari/iOS keyboard automation.
- Physical Android/iOS/Samsung Internet/Firefox tests, accessibility zoom, screen readers and switch access still need manual review.

**Security/privacy:** The published GitHub app remains a standalone offline HTML without runtime third-party downloads. The user's private voice preset, reference recording and derived speaker profile are not included.

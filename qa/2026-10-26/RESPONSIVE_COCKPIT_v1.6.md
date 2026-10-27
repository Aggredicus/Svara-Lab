# Svara Lab v1.6 — Responsive Cockpit QA

## Scope
Viewport-fit studio interface without scrolling in the normal active tab. Public source contains **no personal calibration or speaker reference**. The user's private voice-calibrated instrument remains a separate local file.

## Browser evidence
Chromium browser-tested five functional profiles: 320×568, 390×844, 568×320, 768×1024 and 1440×900. **122/122 functional checks passed**, including tab transitions, no document overflow, 34-letter atlas visibility, Devanāgarī editing/backspace, consonant input, phrase PCM, 9 knobs, formant controls, modal keyboard preferences, sample-export UI, help topics and no JavaScript exceptions.

Additional layout-only checks on 360×640, 430×932, 1024×768, 1920×1080 were free of document overflow. Built-in DSP/WAV/ZIP checks: **15/15** passed. Generated WAV validated as RIFF/WAVE with nonempty data.

## UX decisions
- Native viewport-fit Type, Play, Shape, Export, Help, Home workspaces, preserving existing synth event handlers.
- Type includes all primary controls at once; full 34-consonant atlas is an overlay, keyboard preferences and rare punctuation pop over without reflow.
- Play shows vowel pads + gate and XY in one viewport.
- Shape splits 9-knob, formant and (private edition only) personal calibration into on-screen subviews; public build shows knobs and formants only.
- Export samples and QC have distinct on-screen subviews; rare vowel settings are in an on-screen popover.
- Help uses six concise topic pages, plus downloadable full manual text.
- All becomes Home: navigation, not a scrolling wall of panels.

## Limitations
This is a **Chromium** synthetic viewport test, not iOS/WebKit/Firefox certification or real smartphone usability validation. Extra-small displays, Android/Apple software keyboard resize, zoom/accessibility, screen-reader operation and sustainable two-thumb reach need independent physical tests. Computational audio integrity does not mean native Sanskrit pronunciation quality.

No changes automatically merged into `main`, no deployment enabled, and no actual personal voice samples or derived speaker parameters committed to this public repository.

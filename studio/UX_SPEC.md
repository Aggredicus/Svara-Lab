# Svara Play v1.3 — Interaction specification

## User story

While playing the piano or editing a seven-unit phrase, change the Indian pitch collection or movable tonic **without navigating away from the instrument**. Preserve every existing feature but reveal complex tools only when they are needed.

## Priority hierarchy

1. **Choose**: selected rāga and Sa with compact controls, fast favorite presets, ‹/› exploration, family filtering, and optional automatic scale preview.
2. **Play**: editable seven-unit phrase and fully playable piano occupy the first two primary cards.
3. **Feel**: the selected rāga's artwork and symbolism, plus a compact tāla companion, remain on the same page.
4. **Deepen**: use 14 disclosures for tone mapping, Sanskrit input, musical grammar, cadence experiments, reference libraries, and export.

## Acceptance criteria

- Every key or scale selection updates piano and composer note labels immediately, with no stale copy of selected state.
- `main` and v1.2 branch are not mutated.
- A mobile user at the piano can choose a different rāga or Sa with the persistent bottom dock; no global page-width overflow at 360 px.
- Toggling "Hear when selected" controls automatic melody preview.
- Stop halts playing note sequencer and active drums, without unexpectedly muting the separately controlled drone.
- All original options, input modes, rhythm cycles, audio functions, sources, artistic context and save/export affordances remain available in the same HTML file.
- Preserve reduced-motion support, focus-visible keyboard navigation, accessibility labels, and minimum touch-friendly sizes where possible.
- No external dependencies or network requests.

## Future enhancements (not claimed implemented)

Audio perceptual tests, user usability sessions, WAV phrase export, track layering, real-time MIDI keyboard support for melody performance, onscreen touch-piano resizing beyond horizontal scroll, and full-screen kiosk mode.
# Svara Lab v1.2 — regression audit

Date: 2026-10-26

## Automated verification

**48 / 48 checks passed** in headless Chromium across **390 × 844 mobile** and **1440 × 900 desktop** viewports. Tests were run on the actual standalone HTML using Playwright and browser Audio APIs, then text WAV artifacts were independently checked for RIFF/WAVE headers and container lengths.

| Area | Verified behavior |
|---|---|
| Load & layout | No uncaught page JavaScript errors; no horizontal overflow at either viewport |
| Workspace | Six modes: Compose, Perform, Shape, Export, Help, All |
| Text editing | Editable Devanāgarī field; pasted text retained; physical keyboard backspace and caret insertion work |
| Script parsing | राम, कृष्ण, नमः, and Roman IAST rāma; no spurious schwa inserted inside क्ष/ष्ण clusters |
| Audio synthesis | Text PCM is finite, non-silent, bounded to [-1,1], and rejects excessively long sequences |
| Text playback | Play creates a live speech track, pitch/volume controls adjust that track without recreating the audio source, Stop clears it |
| WAV export | Text WAV download contains valid RIFF/WAVE header and declared file size |
| Stable controls | HOLD VOICE label remains unchanged and the sustain hit target's dimensions/location are stable across simulated pointer down |
| Flick keyboard | Crowded always-visible corner labels removed from the face of each key; contextual directional compass is retained |
| Help | Usage manual is present and reachable in the dedicated Help tab |

## Tests not yet completed

- Manual listening with a Sanskrit specialist for native-like pronunciation and aspiration accuracy.
- Real multi-touch hardware trials on a range of phones/tablets and browsers (Playwright touch event simulation is not a substitute).
- Measured long-running audio latency and battery use on low-end hardware.
- Accessibility audit with screen readers and switch control.

## Honest interpretation

A passing browser/audio integrity test means the app is operable and the export data is valid. It does **not** establish authentic Sanskrit prosody. Consonant speech synthesis remains a simplified experimental layer on the vowel formant synthesizer, and all rendered samples are intended for artistic testing and refinement.

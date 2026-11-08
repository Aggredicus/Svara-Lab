# SVARA PLAY v1.3 — One Musical Workspace

A self-contained, offline-capable Indian classical music learning studio. It unifies the seven-sound phrase composer, piano, rāga explorer, tāla machine, Sanskrit thumb keyboard, and symbolic art in a **single scrolling workspace**.

## Start

Open `studio/index.html` in a modern browser. No installation, build tools, online requests, accounts, or CDNs are required. The first audio action may need a tap to unlock Web Audio on mobile. To serve via GitHub Pages in the future, select the v1.3 branch and `/studio` as the Pages source where supported, or create a dedicated deployment workflow. **This branch does not change GitHub Pages settings or `main`.**

## Five-second workflow

1. Choose a **rāga** with the top select, its ‹/› buttons, or the quick preset chips. Switch between familiar rāgas, the full library, thāṭs and all 72 mēḷakartā parent scales using **Explore a family**.
2. Choose **Sa** with the 12 key buttons. The same phrase instantly transposes; the piano and labels redraw.
3. Tap **Hear scale** or **Phrase**, or type a seven-character phrase and tap **Hear phrase**.
4. Try a **tāla** in the rhythm strip; turn on **With tāla** next to the phrase tempo for synchronized notes and percussion.
5. Open only the tools you need from expandable sections: sārgam/rāga details, Sanskrit two-thumb flick input, mapping and timbre controls, ear training, save/export, rāga/tāla atlases, melakarta, chakra/rāgamālā symbolism, lessons, and scholarly sources.

On phone-sized screens, the persistent bottom **rāga / Sa dock** keeps scale and tonic changes accessible while the large keyboard is in view. The piano scrolls horizontally and centers the current Sa, but the rest of the app does not pan horizontally.

## Retained features and behavior

- Seven-event composer: Latin letters, Sanskrit Devanāgarī graphemes, sargam tokens, rāga-safe path mapping, degree mapping and alphabet-based artwork mapping, piano/vowel/duet playback, compare two keys, loop, stop, timed events, autosave.
- Piano and seven svara pads, live tonic drone, instrument presets, fixed-pitch/experimental just-interval demonstration, volume, octave, A4 reference, preview-on-select and controllable tempos.
- 24 curated rāgas, 10 Hindustani thāṭs, 72 melakarta parent scales; searchable library tools and descriptive/critical references.
- Tāla catalog: 54 configurations including the 35 Sulādi Sapta combinations, group structures, synthetic percussion, subdivisions, tihāī, sam and khālī indicators.
- Sanskrit two-thumb flick keyboard, optional browser speech, experimental pitched vowel synthesis, sargam exercises, ear training, local notebook with JSON import/export and MIDI download.
- Historical and interpretive symbolism explicitly marked as such. Music-theory melakarta *chakras* are **not** the seven yoga chakras.

**Not an authentic performance synthesizer:** Fixed piano tuning and short schematic rāga phrases do not model gharānā-specific meend/andolan or Carnatic gamaka. Formant vowels are exploratory, not validated Sanskrit pronunciation. Speech synthesis depends on device voices. Tabla sounds are synthesized practice cues.

## Developer notes

The app has zero runtime dependencies and a strict no-network content security policy. `studio/index.html` includes the original v1.2 educational/audio engine and a separately identifiable **Unified workspace adapter**. The adapter *moves existing controls in the DOM rather than cloning or replacing their IDs*, and connects instant quick selectors to the existing state machine. Advanced tools retain their original event handlers in collapsible sections. Existing saved phrase JSON format `svara-seven-sounds` version 1 remains compatible.

Test on a desktop with installed Python/Playwright + Chromium:

```bash
python -m pip install playwright
python studio/tests/test_studio.py
```

The browser regression harness loads the HTML as in-memory content due to the test environment's blocked `file://` navigation. Real hardware testing remains recommended before labeling a general-availability public release.

## Preservation and rollback

This work targets `feature/svara-play-unified-v1.3` branched from `feature/seven-sounds-studio-v1.2`. The older v1.2 branch and the repository default `main` remain untouched. The original VĀṆĪ app is available at the repository root `index.html`; the v1.3 studio is at `studio/index.html` on the new branch. Rollback is simply selecting the old branch, not force-pushing or deleting the history.

## Privacy and licensing

No network calls, account, telemetry, or microphone access. Local device storage is used for preferences and saved compositions; export JSON for backup. Application code and original vector artwork retain the existing MIT license notice. Classical traditions are cited as sources, not claimed as original inventions.
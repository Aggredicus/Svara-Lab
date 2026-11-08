# SVARA STUDIO — Seven Sounds Composer v1.2

A **self-contained, offline-capable Indian classical music learning studio** with a new seven-event text-to-melody workspace, built alongside the existing piano, rāga, tāla, melakarta and symbolism explorers.

## Quick start

Open [`studio/index.html`](./index.html) directly in a modern browser. This file makes **no network calls** and requires no installation, build step, service worker, account, external libraries, or microphone permissions. Press **Enable** (or **Hear phrase**) once to activate Web Audio where your browser requires a user gesture.

The repository's original [`../index.html`](../index.html) remains the existing VĀṆĪ / Svara Lab Sanskrit keyboard and voice synthesizer. It is **not overwritten**. This new studio takes inspiration from its two-thumb gestures but contains a separate, compact keyboard implementation. Neither product silently replaces the other.

## Try it in one minute

1. Select **Seven Sounds** in the navigation. The default phrase is `NAMASTE` (seven Latin characters; it is **not** seven Sanskrit syllables).
2. Set **Sa / tonic** to C or D using the shared pitch controls. Each of seven slots displays its letter, sargam note and actual piano pitch.
3. Choose **Yaman**, **Bhūpālī** or another rāga using the composer rāga selector. The phrase stays unchanged; its pitches are remapped.
4. Choose **Rāga-safe path**, **Positions Sa–Ni**, or **Alphabet-to-degree art**. Omitted notes become visible rests rather than being silently replaced with out-of-scale tones.
5. Tap **Hear phrase**, **Loop**, or **Compare keys**, and optionally check **With tāla**. **Stop all** silences tracked piano voices, vowel voices and percussion.
6. Set **Input units → Devanāgarī graphemes**, tap/flick the thumb keys (or type directly). Tap a vowel after a consonant to attach an appropriate mātrā. Use **Virāma** before another consonant to form a conjunct.
7. Save a phrase locally or export MIDI / JSON. Imported JSON is validated and never executed.

## Features

- Seven large, tappable event slots. Typed characters and chosen pitches are **independent**, with local autosave and >7-unit warnings.
- Three text modes: Latin letters, Unicode Devanāgarī graphemes (not claimed as linguistic syllables), and explicit sargam token input (`S R g M+ P d N`).
- Three mappings: a simplified rāga-allowed path, seven degree positions with rests for omitted degrees, and a clearly marked creative alphabet-to-degree mapping.
- Global movable Sa; playable piano; two-tonic back-to-back A/B comparison.
- Reused Svara Studio musical sources: 24 curated rāga exemplars, 10 thāṭs, 72 melakarta scales, plus rhythm cycles, drone, seven svara keys and symbolic interpretation.
- Web Audio piano timbres, **experimental musical vowel formant synthesis**, and piano/vowel duet. No external samples.
- Phrase tempo 30–240 notes/minute; when **With tāla** is enabled, the shared tāla pulse controls timing (minimum 40 BPM due to the existing rhythm engine).
- Offline notebook (up to 30 entries), save/load/delete, downloadable structured JSON, and single-track standard MIDI Type 0 exports including tempo and rests.
- Accessible button names, semantic labels, keyboard input, visible focus, touch flicks, narrow-screen layouts and `prefers-reduced-motion` CSS.

## Musical and linguistic boundaries

**Rāga is more than a scale.** The piano sketches cannot fully reproduce melodic grammar, gamaka/meend, precise intonation or lineage-specific rendition. A seven-character string is not automatically a Sanskrit mantra. The formant tone is an approximate sung vowel, **not** a validated Sanskrit phonetic synthesizer; unvoiced consonants are not modeled correctly. The optional `Speak text` feature delegates to the device's speech engine and may lack a Sanskrit/Hindi voice.

Cultural or spiritual symbolism in the existing studio is labeled as artistic analogy, historically documented tradition, or classification. Melakarta's **12 numeric chakras** and the **seven yogic chakras** are different systems. No curative frequency claims are made.

## Architecture / privacy

- Single HTML containing CSS, data and browser-native JavaScript (no runtime imports).
- Rāga/tāla state and audio scheduler are reused from Svara Studio 1.1. The new composer stores separate state and uses the same audio context/master bus.
- Stop paths cancel pending event timers and actively silence all tracked voices, including while awaiting a user-gesture audio resume.
- Preferences and saved phrases use browser `localStorage` *when available*, falling back to export for persistence. Private/restricted `file://` storage may not survive a page reload.
- No telemetry, third-party resources, network access or uploaded user input. Files are exported only when the user clicks an export control.
- Content Security Policy restricts network requests (`connect-src 'none'`) and disallows object embedding. Inline script/style are required for the one-file build; do not treat it as a hardened untrusted-content host.

## Run optional tests

The app itself needs no dependencies. For regression tests, install Python Playwright and Chromium, then run:

```bash
python -m pip install playwright
python -m playwright install chromium
python studio/tests/test_studio.py
```

Use `SVARA_CHROMIUM` to override the Chromium executable path if needed. See [`QA_REPORT.md`](QA_REPORT.md) for test scope, evidence and residual risks. The release is hosted on an **isolated feature branch**. Review before any merge or public-site deployment.

## Licensing

The source Svara Studio v1.1 includes an MIT license header which is retained verbatim at the top of this file. The existing VĀṆĪ app in the repository remains untouched; its gestures inspired this new compact keyboard implementation. Third-party rāga information and cited learning links are for scholarship and attribution, not a claim of authorship of musical traditions.
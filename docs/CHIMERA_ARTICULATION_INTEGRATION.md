# CHIMERA → SVARA: articulation studio integration

Date: 2026-11-13. Branch: feat/chimera-inspired-articulation-studio.

## Sources and compatibility

- Fork reviewed: https://github.com/Aggredicus/chimera-vocal-synth
- Upstream: https://github.com/jamesondh/chimera-vocal-synth
- CHIMERA source license: MIT, copyright 2026 Jameson Hodge; see the fork's LICENSE.
- SVARA source license: GPL-3.0; see ../LICENSE. MIT code can be incorporated into a GPL-3 project with original MIT notice retained. **This increment copies no CHIMERA engine code, assets, voice data, tables, or bundled fonts.** Public architecture and synthesis methods inspired an independent JavaScript implementation.
- Bundled dictionaries, fonts and other third-party files must be checked separately before reuse.

## Code patterns and decisions

| CHIMERA source | Pattern | SVARA integration |
|---|---|---|
| docs/language-front-ends.md; phonetics modules | Separate orthography/phonology from acoustic renderer | Explicit consonant trait and place maps, keeping existing PCM synthesizer |
| phonetics/planner.rs | Stop releases, voiced aspiration, voice onset time and coarticulatory gestures | Contrastive stop timing and breathy-release approximation |
| control/score.rs, phonetics/planner.rs | Gestural score and segment timing | Playback segment timestamps synchronize anatomy illustration |
| ui/components/AnatomyView.tsx; render/anatomy.ts | Real-time head/tract view and articulator feedback | Independent, lightweight SVG side profile with moving tongue and velum plus analyser waveform |
| src/worklet/processor.ts and Rust engine | Physical airway model with AudioWorklet and WASM | Deferred; offline single-file launch retained |
| docs/speech-comparison.md and Rust tests | Native speech benchmarks and reproducible quality gates | Automated phonetic tests and planned expert listening evaluation |

## Delivered

1. **Voice** is the home view, replacing the old Home menu. The original two-thumb typing experience remains in Type with its layout unchanged.
2. Voice has the 25 traditional varga consonants (five articulation places × five grades), a 14-vowel selector, auditory preview, a live sound trace, and a tract illustration showing tongue, soft palate, lips and glottis.
3. Stop-release noise and timing distinguish aspirated/unaspirated and voiced/voiceless categories; voiced aspirates have a breathy-release approximation. Anusvāra adapts to a following consonant's place; Roman IAST no longer injects an unintended inherent vowel.
4. The single index.html remains offline and dependency-free. This is a **phonetic source/filter synth with an educational anatomy diagram**, not CHIMERA's physically modeled tract or validated native Sanskrit TTS.

## Verification

Run: node qa/2026-11-13/test_articulation.mjs

Automated checks include syntax, 25 varga consonants, 14 vowels, script parity, virāma, place-aware anusvāra, bounded finite samples, and aspiration timing. Direct JavaScript-runtime samples during development successfully rendered राम / rāma, कृष्ण, śānti, क / ख, ग / घ and others.

Not yet verified: speaker intelligibility, listening with Sanskrit experts, actual phone touch performance, iOS/Safari/Firefox layouts, long-running battery/CPU use, or reference-recording similarity. UI articulation is qualitative: its SVG position is not calculated from the sound waveguide.

Recommended native-speaker test corpus: each place × five stop grades in common vowel frames; dental versus retroflex; nasal places; short versus long vowels; clusters क्ष, ज्ञ, त्र; anusvāra, visarga and Vedic pitch accents. Keep consented voice recordings out of the public repository.

## Path to true CHIMERA-grade physics

In a separate phase, implement a Sanskrit syllable-to-phoneme front end against CHIMERA's language-independent backend. Provide explicit place, aspiration and breathy-voice gestures, build Rust to WASM and run DSP in an AudioWorklet; feed actual geometry and spectral telemetry into the visual component. Audit licensing and reference data, benchmark mobile CPU/latency, validate hearing with speakers, and keep the original JavaScript engine as a fallback.

A WASM/AudioWorklet package typically needs a secure browser context, which may be incompatible with simply opening index.html through file://. Do not silently add network dependencies or defeat browser security just to preserve a single-file launch.

## Second increment: audiovisual articulation (2026-11-13)

Branch: `feat/animated-anatomical-phonetics`.

- Replaced the former schematic with a layered, SVG sagittal head and vocal tract: face points left; hard palate and nasal space lie above the oral cavity; the pharynx and larynx sit posterior/inferior to the tongue. Original illustration, not a measured clinical scan.
- Replaced hard-coded contact snapping with frame-by-frame kinematic tongue geometry, velar lowering for nasals, lip closure for labials, and a vocal-fold aperture indicator; oral/nasal airflow and phase readouts follow the shared phoneme score.
- Added a common `articulationGesture` function with stop closure, place-sensitive release burst (including longer palatal affrication), aspiration duration and transition to vowel; visual and PCM tracks share its timing. Waveform feedback is derived from the Web Audio analyser.
- Reworked consonant audio for five distinct burst spectra; added weak prevoicing, breathy/murmured voice for voiced aspirates, differentiated nasal spectral poles and simple antiformant cancellation; an onset formant trajectory on the following vowel supports place cues.
- Added the **Compare** button (e.g. ka–kha–ka) for perceptual A/B exploration; all 25 consonants remain individually playable. The original two-thumb keyboard, formant controls, WAV export and offline single-file launch are preserved.
- Acoustic tests validate phase duration, all 25 phones, finite bounded PCM, prevoicing energy, aspiration ratio, place-coded spectral differences, homorganic nasal difference, and distinct vowel onset resonances. Chromium CI verifies mobile rendering, UI initialization, touch selection, tongue/velum/lip changes and Web Audio source startup.

### Phonetic and anatomical references

- [IGNCA, *Arrangement of the Syllabary*](https://ignca.gov.in/Asi_data/3374.pdf) — canonical five places and manners of consonants.
- [Joseph & Janda, *On the Unity of Sanskrit Aspiration* (1988)](https://bpb-us-w2.wpmucdn.com/u.osu.edu/dist/4/105142/files/2021/05/1988sktaspiration.pdf) — the separate voiceless-aspirated and voiced-aspirated series.
- [University of Iowa, *Sounds of Speech*](https://soundsofspeech.uiowa.edu/) — animated sagittal articulation and speech anatomy as a pedagogical pattern; its image assets, sound clips and code have **not** been used.
- [Sanskrit Guide: Five Places of Pronunciation](https://sanskritguide.com/03_Chapter_3_Five_Birthplaces_of_Sound.html) — pedagogical dental/retroflex/palatal and nasal distinctions.

### Accuracy boundaries and next validation

SVG head proportions and tongue targets are **illustrative anatomical estimates**, not patient-specific coordinates or a measured vocal-tract area function. Source/filter sound is *contrast enhanced* but not a validated Sanskrit pronunciation model; the tongue/velum shape does **not physically determine the spectrum**, both are driven by a shared idealized gesture plan. In particular, palatal affrication, phonation of voiced aspirates, real nasal antiformants, long vowels and accent patterns vary with tradition/speaker and require recordings and perceptual tests. Browser automation proves functionality, not acoustic accuracy.

Recommended next steps: (1) obtain opt-in, properly licensed reference pronunciations for all 25 stops/nasals plus 14 vowels in common CV frames; (2) native-speaker ABX, dental–retroflex confusion matrix and VOT/breathiness measurement; (3) fit tract geometry using published midsagittal MRI/EMA data with suitable consent/license and annotate distances; (4) implement a separately packaged Rust/WASM physical airway engine from permitted CHIMERA modules with licenses retained; (5) verify mobile CPU and Safari/WebKit compatibility. Keep the local JS engine as guaranteed offline fallback.

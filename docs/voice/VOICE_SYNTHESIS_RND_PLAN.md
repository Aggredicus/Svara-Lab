# Svara Lab — realistic Sanskrit voice synthesis R&D plan
Status: **research proposal** · 2026-10-26 · Do not treat goals as achieved.

## Mission
Create a **local-first** system that (1) pronounces Sanskrit words correctly from Devanāgarī or IAST, (2) convincingly approximates a consenting speaker's vocal identity, and (3) integrates with Svara Lab's low-latency, pitch/volume/timbre-controlled musical instrument. Pronunciation, voice identity, musical expression, and runtime are separate measurable objectives.

## Available initial evidence
A short, voluntarily supplied English alphabet reference was analyzed privately. Its measured characteristics must remain in local, speaker-controlled calibration artifacts; public repository documentation should not contain individual vocal pitch or other reference-derived identifiers. There are **no Sanskrit phonemic coverage labels** in this clip. It is suitable for preliminary voice-color embedding/zero-shot tests, not for training an accurate Sanskrit pronunciation system. The source recording is **private**; DO NOT commit, upload, redistribute, or include it in public artifacts. Obtain further speaker authorization for any externally hosted processing.

## Architecture
```
Devanāgarī / IAST / gesture keyboard
       ↓ Unicode NFC + script-aware validation
Sanskrit lexical and rule-based G2P (preserve Sanskrit vowel nuclei)
       ↓ phonemes + syllable boundaries + optional sandhi + duration tags
Prosody planner (spoken, rhythmic, chant, Vedic accent [future])
       ↓
[A] Low-latency DSP/formant engine   [B] Local Sanskrit neural TTS
  MIDI sustain; patchable timbre        words, coarticulation, utterances
          \                         /
           \-- explicit phoneme API -/
                     ↓
Optional consented voice-color adaptation / fine-tuning
                     ↓
Quality-gated PCM + formant-safe pitch/time controls
                     ↓
Local WAV samples, DAW sampler, interactive player
```
Keep engines **modular** and keep the original one-file HTML available offline. Large neural model weights are an opt-in **local workstation** backend, not hidden downloads triggered by touching the phone interface. No network dependence in the default instrument.

## Candidate baselines to evaluate (not yet installed or benchmarked)
1. **Vāgdhenu** (https://github.com/prathoshap/vagdhenu and https://huggingface.co/prathoshap/vagdhenu). Purpose-built Sanskrit metered-chant TTS, based on IndicF5 + BigVGAN-v2. Published model page reports expert MOS ~4.6 and strong conjunct rendering; these are **developer claims**, not independently reproduced here. The project explicitly does **not** implement Vedic svara accents. Check artifacts, precision, memory and separate component licenses. Reference-driven chant prosody is not the same as natural conversational Sanskrit.
2. **OpenVoice V2** (https://github.com/myshell-ai/OpenVoice). Test **voice-color conversion** after a Sanskrit base voice has already produced intelligible audio. Authors report MIT licensing and several native languages; Sanskrit is **not** one of the listed native languages, and conversion success must be tested. Do not conflate color transfer with correct pronunciation.
3. **IndicF5** (https://github.com/AI4Bharat/IndicF5). Good Indic flow-matching acoustic baseline and reference-driven voice generation; Sanskrit is **not** in its stated 11 supported languages. Standard Hindi-oriented processing can delete vowels required by Sanskrit. The Vāgdhenu approach uses a different script representation for Sanskrit to avoid this problem.
4. **F5-TTS** (https://github.com/SWivid/F5-TTS). Useful general architecture for development, but its released pretrained weights are **CC BY-NC**, despite MIT source code. Do not assume commercial permission or blindly inherit weights.
5. Preserve a **DSP-only ablation** to prove neural improvements in intelligibility, audio fidelity, and speaker similarity.

## Experimental milestones and gates
### Phase 0 — Stop UI/audio regressions
- One acoustic onset per intentional gesture, not once on finger-down plus finger-up; ramp click-prone transitions.
- Confirm left/right thumb audio, no false haptic/keypad sound, all mapped directions visible and testable.
- Gate: 34 consonant symbols + 14 vowel symbols mapped; zero duplicate event firings or discontinuity clicks in a deterministic capture.

### Phase 1 — Correct written-to-spoken Sanskrit
- NFC-normalized Unicode input; Devanāgarī ↔ IAST equivalence, avagraha, nukta policy, virāma, conjuncts and traditional vowels.
- Context-sensitive anusvāra / visarga rules and optional sandhi; user-visible pronunciation override.
- Avoid arbitrary Hindi schwa deletion. Preserve vowel length, dental/retroflex, voiced/voiceless and aspirated/unaspirated distinctions.
- Gate: 100% pass on an audited text → phoneme fixture of ≥250 cases (not proof of acoustic accuracy).

### Phase 2 — Acoustic Sanskrit baseline
- Compare DSP, Vāgdhenu, IndicF5 adaptation on blinded native-speaker / expert scores for intelligibility, minimal pairs and naturalness.
- Gate proposal: ≥95% correct words or syllables on held-out human transcription, ≥90% classification on balanced contrasts and no severe pronunciation class failures. These are **target thresholds**, not achieved metrics.

### Phase 3 — Your voice
- Initially use the current short English sample for a **local-only, illustrative speaker-reference experiment**; no claim of accurate cloning.
- Record 20–30 min pilot of structured Sanskrit sounds and words, then ~45–90 min of clear, consented balanced speech if actual speaker adaptation is promising. Keep the 9.56-s clip held out for speaker-similarity checks if useful.
- Evaluate neutral spoken vs chanted conditions separately. Keep training, validation and held-out sets isolated by **text**, not just clip.
- Gate proposal: blinded speaker similarity mean ≥4/5 and naturalness ≥4/5, judged by ≥5 consenting raters; strong phonetic performance must not regress.

### Phase 4 — Expressive real-time instrument
- Separate speech onset/transient from steady-state vowel body; enforce **single-trigger preview**.
- Render stable loopable phoneme sustains with formant-preserving pitch bend and amplitude response, legato and breath control. Prefer pre-rendered local sample banks on phone.
- Gate proposal: <100 ms note-on responsiveness on selected target phone, no audible seam at sustain loop, zero stuck notes in multitouch tests. Measure on physical hardware.

### Phase 5 — Release and governance
- Offline-first by default, publicly documented model origins and third-party licenses, consent record for speaker examples, no published voice biometric/template by default.
- A/B human evaluation, technical signal audit, no nonconsensual voice emulation; explicit labeling of synthesized voice where audio leaves the app.
- No automated main merges or public uploads of recordings. Preserve reviewable PRs, regression suites and rollback paths.

## Measurement matrix
| Objective | Measurements | Who/what validates |
| --- | --- | --- |
| Written pronunciation | G2P fixture accuracy, Sanskrit tokenization, spellings and sandhi | Unit tests + Sanskrit linguist |
| Acoustic pronunciation | Balanced minimal-pair confusion, PER, blinded transcription accuracy | Native Sanskrit readers / phoneticians |
| Speaker similarity | Paired blinded listening, speaker-embedding cosine similarity as secondary indicator | Speaker + ≥5 listeners |
| Voice naturalness | MOS-like 1–5 blind tests and qualitative artifacts | Human listening, not simulated personas |
| Instrument responsiveness | Note-on latency, clicks, loop seams, stuck notes, gesture event count | Hardware traces and DSP tests |
| Model feasibility | Peak RAM/VRAM, real-time factor, model weight size, energy, device support | Local profiling |
| Legal and privacy | Licenses of **each weight**, training corpus provenance, consent, no unintended network | Human governance gate |

**Stop rules:** stop if a model lacks clearly compatible rights, if Sanskrit pronunciation worsens, if a reference is published without consent, or if a prototype silently requires cloud access. Report all unverified claims and measured baselines separately.

## First proposed development sprint
1. Establish the **corpus and reference-audio protocol** in `RECORDING_PROTOCOL.md`.
2. Implement text/phoneme fixture set and contrast lists, independent of waveform generation.
3. Benchmark Vāgdhenu output offline against 20 short Sanskrit items (speaker-independent first).
4. Benchmark OpenVoice V2 tone-color transfer separately; never infer pronunciation from a voice similarity score.
5. Fix existing preview trigger/buzz/click issues; capture waveform and no-double-trigger regression.
6. Submit paired human listening results for review **before** fine-tuning or enabling any public voice-sharing feature.

## Research references
- Vāgdhenu code and weights: https://github.com/prathoshap/vagdhenu ; https://huggingface.co/prathoshap/vagdhenu
- IndicF5: https://github.com/AI4Bharat/IndicF5
- OpenVoice V2: https://github.com/myshell-ai/OpenVoice
- F5-TTS source/weights license distinction: https://github.com/SWivid/F5-TTS
- AI4Bharat Indic-TTS: https://github.com/AI4Bharat/Indic-TTS

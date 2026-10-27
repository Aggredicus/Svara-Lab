# Svara Lab v1.5 — Audio-trigger and consonant discoverability audit

Date: 2026-10-26. Evidence: instrumented Chromium testing and local analysis of a voluntary user-provided WAV. **Do not publish or commit the original recording or full typed text without permission.**

## Findings from WAV and code
The user's phrase export was 22.139 s, mono, 32 kHz, signed 16-bit PCM, peak 0.731 and RMS 0.217. A rapid, buzzy repeating syllabic sound is audible. Many repeated written consonants account for some repetition, but synthetic consonants remain insufficiently distinct.

**The WAV is an exported phrase, not a direct recording of keyboard taps.** It does not independently prove duplicated touch events. Code inspection separately confirmed v1.4 played the center consonant on pointer-down and another sample when swipe direction changed; old voices were stopped immediately.

## Fixes
- One audio audition **per completed gesture**, with no preview starts on touch-down or intermediate directions.
- Consonant+vowel two-thumb input within 95 ms is coalesced into one short syllable audition instead of two onsets.
- Fast replacement audio uses a short gain release rather than abruptly terminating a nonzero waveform; 8 ms outer-edge WAV fades reduce hard ends.
- Simple place-specific spectral shaping replaces uniform consonant noise bursts. It remains an exploratory speech model, not validated Sanskrit pronunciation.
- **34-button tappable atlas**, shown immediately, with glyph, IAST and flick direction; also visible examples of conjunct construction.
- **Practice (hear without typing)** prevents test sessions producing pages of duplicated glyphs.

## Checks actually executed
- **60/60** scripted browser checks at widths 320, 390, 768 and 1440 px. Tested atlas availability, audio starts before/after release, one-shot previews, rapid two-finger coalescing, practice mode, and layout.
- **34/34** directional consonant flick mappings gave correct glyphs.
- A real Chromium CDP native touch right-swipe on KA yielded **घ** and exactly **one** AudioBufferSourceNode.start.
- **15/15** DSP/WAV/ZIP integrity suite passed.
- 8 ready-made example buttons cover common conjuncts and vowel signs.
- New sample generated for comparison using the same generic 34-letter demonstration text; both remain visibly synthetic.

## Remaining limits
No actual physical phone trials, no native speaker ABX ratings, no haptic isolation testing, and no claim of natural articulatory quality. Live finger audio starts were tested via browser instrumentation; user-provided WAV analyses apply only to phrase export. This branch is not yet merged or deployed.

## Reproduction
The standalone QA bundle contains `qa_v15.py`, `gesture_matrix.py`, the test result JSONs and two generic audio comparison WAVs. No user-provided source audio is included.

InScript inspiration: <https://cdac.gov.in/index.aspx?id=print_page&print=mc_s_inscript> (vowels left, consonants right, phonetic vargas). This app's two-thumb flick positions are a variation, **not exact desktop InScript**.

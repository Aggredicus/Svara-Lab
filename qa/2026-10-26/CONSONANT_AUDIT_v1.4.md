# Svara Lab v1.4 — Consonant Recovery QA/QC
**Date:** 2026-10-26 · **Evidence:** instrumented browser automation + synthetic task personas (zero recruited humans)

## Defect ledger
| ID | Before | Root cause | Patch | Observed result |
|---|---|---|---|---|
| C-01 | Left consonant keys typed silently while right vowels played | Sound preview in `composerEvent` was restricted to `kind:'v'` | Offline `auditionLetter` for consonant and inherent 'a', triggered on touch-down/direction change | Browser AudioBufferSource actually started for consonant |
| C-02 | Directional swipes unreliable on device | Pointer-event lifecycle depended on capture and final coordinates | Track movement per pointer, restore last known coordinates; window move/up fallback | Real Chromium mobile `Input.dispatchTouchEvent`: KA → right → घ |
| C-03 | Empty directional slot silently typed the center glyph | `group.parts[d] || group.parts[0]` fallback | Explicit empty-direction no-op | No incorrect substitute letters |
| C-04 | Hard to learn full Sanskrit letter matrix | No visible comprehensive map; original side order unlike InScript | Letter map + optional InScript-inspired vowel-left/consonant-right arrangement | All 34 consonants visible with gestures |

## Character coverage
**34 consonants**: five vargas of five (क-वर्ग through प-वर्ग), य र ल व, श ष स ह, and extended Sanskrit ळ. Every individual mapping was checked for Unicode codepoint, IAST transliteration and finite/nonzero PCM. The vowel synthesizer preserves fourteen existing vowel symbols. Modern Devanagari nukta additions and full Vedic mark coverage are **not** implemented.

## Executed test results
- 12 synthetic persona/viewport sessions (320px through 1920px), 540/540 script assertions passed.
- Each of the 34 mapped consonants tested by `pointerdown → pointermove → pointerup` event sequence.
- Real Chromium DevTools touch-swipe on 390px phone viewport: KA→right commits **घ**.
- Real Chromium DevTools dual-contact test with vowel finger lifted first: **का** committed in down-order; two preview sound sources started.
- DSP/ZIP/WAV in-browser integrity: **15/15**.
- No browser errors or horizontal overflow detected in the scripted cohort.
- No human user responses are claimed.

## Remaining acceptance tests
Native speaker acoustic ABX discrimination of aspirates, retroflexes and sonorants; physical Android/iOS usability testing with measured swipe accuracy, latency and comfort; Safari/WebKit parity; screen reader interaction with gesture keyboard; policy for extended characters.

## Cultural/technical basis
C-DAC InScript says vowels on LEFT and consonants on RIGHT and uses varga organization: https://cdac.gov.in/index.aspx?id=print_page&print=mc_s_inscript
TDIL standardization: https://www.tdil-dc.in/index.php?lang=en&option=com_vertical&parentid=12
This two-thumb flick arrangement is inspired by phonetic grouping, not a byte-for-byte desktop InScript implementation.

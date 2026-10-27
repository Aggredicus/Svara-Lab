# VĀṆĪ / SVARA LAB

Offline, touch-first Sanskrit formant synthesizer and two-thumb gesture composer.

## Quick start

Open **[index.html](./index.html)** in a modern browser. No account, network access, build step, installation, or package manager is needed. The audio engine needs a user tap to start in many browsers. For GitHub Pages, deploy the repository root on the default branch after reviewing and merging this release.

## What is included (v1.2)

- **Compose**: editable Devanāgarī field, paste/type Sanskrit text, IAST transliteration, two-thumb consonant/vowel flick keyboard, conjunct joining, undo and text export.
- **Play text**: render typed Devanāgarī or IAST to an experimental offline consonant-and-vowel audio sequence; play, stop, change pace and export one WAV.
- **Perform**: 14 Sanskrit vowel pads, expressive pitch/intensity XY controller, hold/latch sustain, optional MIDI keyboard input.
- **Shape**: live voice presets, envelope, formants, source settings, and adjustable synthesis controls.
- **Export**: batch WAV/ZIP sample generation, sampler loop metadata and patch presets.
- **Help**: built-in usage guide for typing, gesture chords, playback, sustain, shaping and export.

### Two-thumb gestures

Tap a consonant-family key with one thumb and a vowel-family key with the other. Swipe up/down/left/right from a key for related letters. The direction compass is revealed during interaction rather than printed over crowded key faces. Use **JOIN (्)** to make conjuncts; independent vowels and dependent vowel signs are handled in the composer.

### Voice performance

Press and hold **HOLD VOICE** to sustain. Move on the XY area while holding for pitch bend (X) and loudness intensity (Y), or use the fixed controls at the bottom. Other knobs remain usable during sustain. The fixed size of the gate and its labels avoids nearby layout movement.

## Technical limitations

**This is an experimental sound instrument, not a native-speaker-validated Sanskrit TTS engine.** Vowels use formant synthesis. Text speech assembles approximate consonant transients/noise/nasals and vowels; natural coarticulation, prosody, Vedic pitch accents, consonant aspiration distinctions and phonetic precision are incomplete. The sound may be robotic by design. Vedic accents are not interpreted in the text speech output. Sampler-style pitch bending may shift formants. Use native-speaker comparison before linguistic publication.

### Privacy and security

The default experience runs entirely on-device. No analytics, audio upload, cloud APIs or third-party JavaScript dependencies. Typed text is stored locally in the browser for convenience (clear the text and/or site data to remove it). Downloaded WAV/ZIP exports stay on your device unless you share them.

## Validation

Browser regression checks passed **48/48** across 390px mobile and 1440px desktop viewports. Checks covered text editing, Devanāgarī and IAST parsing, consonant conjuncts (e.g., कृष्ण), visarga, synthesis bounds, playback, voice source continuity, hold-button dimensions/label stability, WAV header integrity, Help panel, mobile overflow and JavaScript errors. See [QA.md](./QA.md). Validation does not replace ear testing on Android/iOS devices.

## License

GNU General Public License v3.0. See [LICENSE](./LICENSE) for terms.

## Consonant recovery (v1.4)

The interactive consonant keyboard now auditions consonants through the local phrase PCM renderer (a short consonant + inherent-a sample), and swipes reliably select a directional alternative. The touch handler records movement, handles pointer release outside its key, and uses last-known coordinates when release locations are unavailable. A direction with no assigned consonant produces **no letter** rather than accidentally selecting the key center. A **Letter map** reveals all available gestures, and the **Test every consonant** button checks all 34 traditional/extended Sanskrit consonants for proper glyphs, transliteration, and nonzero synthetic audio. Original left-consonants/right-vowels is preserved; switch on *InScript-inspired hands* for the standard-like vowel-left/consonant-right arrangement. This is NOT identical to the 101-key desktop InScript layout.

**QA:** 12 synthetic persona/viewport sessions × 45 automated assertions each = 540/540 checks. Browser-generated real multi-touch sequence produced `का`, rightward KA swipe produced `घ`, and in-browser DSP/WAV/ZIP integrity remained 15/15. Synthetic audio accuracy and real-device touch ergonomics are not validated by people. See [v1.4 QA review](./qa/2026-10-26/CONSONANT_AUDIT_v1.4.md) and [C-DAC InScript reference](https://cdac.gov.in/index.aspx?id=print_page&print=mc_s_inscript).

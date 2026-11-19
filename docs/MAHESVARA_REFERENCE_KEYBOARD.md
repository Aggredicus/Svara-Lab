# Māheśvara Sūtras reference and restored modal keyboard

## What changed

The default start view is **⌨ Type** (the approved v1.7 two-thumb keyboard). The existing **◎ Voice** anatomy/synthesis studio is still accessible in the original tab. Fixed quick actions, **⌨ Pop-out** and **📖 Reference**, are available from every workspace.

**⌨ Pop-out** moves the *actual composer DOM element* into an accessible dialog (not a copy). All current gestures, text, local saved state, native keyboard switch, audition and undo handlers therefore remain active. Closing it returns the same composer to its original location and restores the previous active workspace. No new package or network dependency is used.

**📖 Reference** provides a persistent scrollable sidecar (desktop) or bottom reading sheet (mobile), independent of the current workspace. It includes:
- All 14 Māheśvara Sūtras in verified Devanāgarī, IAST, and English phoneme/marker glosses.
- Vowel inventory, lengths, nasal and breath marks.
- Five varga rows with consistent 5-way articulatory contrasts.
- Tongue/lip placement notes, semivowels and sibilants.
- Pratyāhāras (ac, hal, ik, yaṇ, ec, jaś).
- Core rules: iko yaṇ aci, akaḥ savarṇe dīrghaḥ, guṇa and vṛddhi.
- **Illustrations** shelf to import the seven matching PNG/JPEG guide pages from device Downloads.

The illustrated pages were generated in a separate ChatGPT conversation. They are **not embedded in the GitHub app**: source images were not available to the GitHub text-only publishing connector. Users can import the seven pages into the on-device gallery with one file chooser. Their images are stored locally in IndexedDB and work offline thereafter; no upload or telemetry is performed. The texts, sound-class tables and rules are bundled directly in \`index.html\` and work immediately, with no import required.

## Suggested student workflow

1. Launch the site; the Type keyboard is immediately ready.
2. Tap **📖 Reference**; learn the 14-sūtra sequence while composing a word.
3. Tap **⌨ Pop-out** from another mode to access the same approved keyboard as a dialog.
4. Use **◎ Voice** to explore the interactive anatomy; it remains an approximate simulation, not a native-speaker pronunciation standard.
5. Under **Illustrations**, import the seven guide PNGs from Downloads once.

## Text verification

The standard phoneme sequence is transcribed against:
- Arsha Vidya Center, *Sanskrit Grammar II: Sandhi*, Topic II (Māheśvarasūtrāṇi), https://arshavidyacenter.org/wp-content/uploads/Sanskrit/SanskritGrammar2Sandhi.pdf
- *Modeling the Pāṇinian System of Sanskrit Grammar*, https://tile.loc.gov/storage-services/master/gdc/gdcebookspublic/20/20/42/64/52/2020426452/2020426452.pdf
- University of Hyderabad, *Pāṇini and the Aṣṭādhyāyī* (phoneme sequences and pratyāhāras), https://sanskrit.uohyd.ac.in/faculty/amba/PUBLICATIONS/Lectures/UoHyd/10-4-2018/panini_ver4.pdf

The image-generated posters are illustrative: their Devanāgarī labels are not primary textual authority. The source-backed typeset guide panel is authoritative when illustrations disagree.

## Checks

- Existing syntax/phonetics suite updated for keyboard-first launch.
- Browser regression extended to check the 14 sūtra rows, reference switching, real modal DOM reparenting, return to Type, and explicit Voice navigation.
- Audio synthesis remains untouched.
- Actual physical Android/iOS keyboards and multi-touch still require hands-on testing.

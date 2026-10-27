# Svara Lab v1.7 — final QA/QC report
**Date:** 2026-10-27  
**Release scope:** system keyboard ON/OFF switch, adaptive visible viewport, compact landscape recovery and click-stability regression.

## Test evidence

| Test | Result | Meaning |
|---|---:|---|
| Public + private layout/input matrix | 162 / 162 | Ten edition/viewport profiles |
| Independent public switch regression | 68 / 68 | Five browser viewports, including OFF during simulated OSK |
| Audio engine (each edition) | 15 / 15 | Preexisting synth integrity regression |
| Consonant maps (each edition) | 34 / 34 | Unicode and non-silent phoneme coverage |

Viewports: 320×568, 390×844, 568×320, 768×1024, 1440×900. For keyboard-open simulation, reduced visible height by 270 px on portrait touch profiles. Zero page JavaScript exceptions in the scripted matrix.

## Bug discovered in independent review

The first public regression run revealed that clicking **Phone keys OFF** while the editor had focus on a viewport shrunk by the OS keyboard could **lose the click**. The editor's blur listener immediately collapsed the keyboard layout on pointerdown, moving the switch before pointerup. A delayed blur reflow preserves the click. Switched the toggle wrapper from a label to an explicit click-forwarding container to avoid inherited label activation ambiguities. Follow-up headless test now passes 68/68.

## Remaining limitations

Physical keyboards were simulated by viewport reduction. Headless Chromium does not show Android Gboard or iOS keyboard. Real-device checks, manual screen reader accessibility and production cross-browser coverage remain pending. A screen too short for two full touch keyboards may hide secondary controls, not reduce thumb pads to unusable target sizes. Non-silent Sanskrit audio is not proof of accurate human pronunciation.

## Release discipline

Publish generic files only. Private voice recordings, measurements and personalized calibration must not be committed. A reviewable PR precedes main integration; manual rollback via revert is available.

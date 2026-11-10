# Svara Play v1.8 — QA report

## Changes under test

Reorganized Svara Play v1.7 into a compact mobile-first work surface. Preserved all audio engines, program IDs, saved data formats, music catalogs, Gāyatrī library and user-approved v1.7 keyboard. Only appended a new scoped style and a DOM-moving UI adapter; no third-party libraries or new network requests.

## Verified local browser suites

| Suite | Checks | Result |
| --- | ---: | --- |
| Full studio music, input, playback/stop, rāga/tāla sync, JSON and MIDI exports | 192 | PASS |
| Compact keyboard geometry/editing (desktop and five mobile widths) | 175 | PASS |
| Emulated multitouch and swipe sequences | 3 | PASS |
| Thumb-utility ordering and function | 86 | PASS |
| Mantra catalog, accented/clean text, clipboard, editor | 175 | PASS |
| New mobile flow, section shortcuts, selectors, settings, keyboard pinning | 154 | PASS |
| **Total** | **785** | **PASS** |

Local Chromium browser automation used real app scripts in an in-memory document. The six viewport sizes in the new mobile-flow suite were 320×568, 360×750, 390×844, 428×926, 760×700, and 1440×900. No page JavaScript errors or horizontal document overflow were observed in these runs.

## Measured layout improvements

At Chromium 390×844, with default settings and the same input document:

- Previous top scale-selector card: **347 px** (v1.7); new card **145 px** (v1.8), approximately **58% shorter**.
- Piano begins at document **y ≈ 1358 px** in v1.7, and **y ≈ 583 px** in v1.8 (about 775 px higher).
- Pinned keyboard retains its v1.7 geometry, including **≤ 50% viewport height**; the new bottom navigation remains available in the reserved space beneath the keyboard.
- 14 advanced studio drawers, seven musical composer slots, 37 piano keys and 12 tonic options remain present.

## Regression and fix

The original studio tests clicked controls that v1.8 now intentionally houses in collapsed details. Test setup was updated to open **Keys · families · favorites** and **Timing · mapping notes**, and to change the hidden synchronized duplicate rāga selector via its normal DOM `change` event. Existing application functionality was not removed.

A Playwright navigation pass initially exposed an issue where the sticky scale header could obscure the Sanskrit Pin button in an opened tool drawer. The compact header now becomes non-sticky when an advanced drawer is open; the new flow suite confirms the Pin button is clickable and the keyboard remains visible.

## Risks and limitations

- Testing is automated Chromium emulation, not a verified physical Android/iOS touch-and-audio session. No claim of improved measured user task completion speed is made.
- Smaller mobile controls may still need ergonomics feedback on individual screen sizes and accessibility settings.
- Offline file contexts can restrict clipboard, speech synthesis, and local storage depending on browser settings; existing fallbacks remain.
- Rāga interpretation and Sanskrit phonetic accuracy require human expert verification.
- GitHub branch CI status, if any, is separate from these locally executed checks.

## Preservation

The original keyboard-related style/script blocks were compared byte-for-byte with the v1.7 source and match. No existing feature branch or `main` was edited.
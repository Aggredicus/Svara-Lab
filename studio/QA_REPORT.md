# Svara Studio v1.2 — release QA report

**Target:** `feature/seven-sounds-studio-v1.2` / `studio/index.html`.

## Scope

Retains Svara Studio v1.1 (rāgas, melakarta, piano, tāla, symbolism, playback fixes) while introducing a seven-event composer, Sanskrit flick typing, offline vowel timbre, A/B tonic compare, synchronous rhythm accompaniment, save/load, MIDI and JSON.

## Checks completed

- **90 / 90** automated Chromium/Playwright assertions passed at **1440×900**, **390×844**, and **360×750** viewport sizes in the development runner.
- JavaScript extracted from the final HTML passed `node --check`.
- No uncaught browser JavaScript errors observed under tested interactions, no horizontal overflow at tested sizes.
- Each viewport exercised: all 72 melakarta data entries still present; seven composer slots; edits and pitch display; global Sa change; Bhūpālī allowed-note path; omitted-degree rests; tempo control; start, stop and loop; composer/tāla paired start and cross-stop cancelling percussion; MIDI and JSON downloads; saved-phrase reload; Devanāgarī mātrā attachment and conjunct grapheme handling; sargam literal token mode; rejection of unknown tokens; and invalid virāma placement prevention.
- Sample MIDI export inspected structurally as Standard MIDI header (`MThd`) plus track (`MTrk`). Tempo, notes, rests and single-track format are generated without a third-party MIDI library.
- Browser tests loaded the app with `page.set_content(...)` because runner policy blocked navigation to file URLs and localhost. **Direct `file://` launch was not independently browser-tested in this runner.**

## QA limitations

1. Audio synthesis was exercised through Chromium Web Audio calls, **not judged by native Sanskrit speakers or Indian classical musicians**. Musical timbres, microtonal intonation and ornamentation need listening review.
2. Testing used emulated mobile viewport sizes, not physical Android or iOS devices or real two-thumb input. Hardware touch and audio latency remain device-specific.
3. `localStorage` availability varies by browser/URL origin. Always export JSON for archival backup.
4. Device speech (`speechSynthesis`) cannot be guaranteed on offline phones and does not provide accurate pitched classical Sanskrit vocals.
5. On a long-running loop, the MIDI export writes the **single seven-event phrase** rather than looped repeats. This is intentional for interoperability.
6. Current rāga paths are pitch-safe educational sketches, **not authenticated compositions**. The 24 curated rāgas and the 72 melakarta parent scales are not comprehensive recordings of living traditions.
7. Repository GitHub Pages hosting, physical phone testing, third-party security testing and formal public performance review are **not claimed**.

## Security / preservation

- New files added **under `studio/` only** on a new branch based on `main`.
- No changes to root `index.html` or existing VĀṆĪ source.
- No external JS/CSS/assets, network requests or microphone permissions.
- User-entered text is placed into DOM by `textContent`; imported JSON is validated and constrained; file export requires explicit click.
- This is a reversible feature-branch publication. Main branch and its deployed website are unchanged unless separately approved.

## Release decision

**Feature-branch v1.2 candidate: browser-regression PASS; public-musician and physical-device review outstanding.**
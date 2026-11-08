# Svara Play v1.3 — QA and release decision

**Scope:** Major interface reorganization without removing the v1.2 musical engines. The user can change keys, rāgas and rhythms without switching views, on desktop and mobile. New v1.3 changes are isolated in a new branch.

## Verified in current development environment

- **192/192** automated browser checks passed using Chromium and Playwright at **1440×900**, **390×844**, and **360×750**; additionally ran exploratory 768×1024 layout checks.
- New adapter's JavaScript passed `node --check`; no uncaught browser JavaScript exceptions in regression scenarios.
- No unintended horizontal page overflow on tested widths, including when all 14 advanced expandable sections are open. Piano and preset/key rails scroll *within their own containers*.
- Twelve Sa controls update tonic, pianist key highlights, composer pitches, and persistent mobile dock. Direct select, quick scale chips, next/previous and family selection update musical state and all editor selectors, including melakarta #65.
- All 72 parent-scale options, the catalog of rāgas/thāṭs, and 54 tāla options remain accessible; 14 expandable tools expose the existing education, Sanskrit keyboard, rhythm, and settings components.
- The shared speed slider changes phrase, scale and rhythm tempo inputs. Preview-on-select can be disabled or enabled without leaving the workspace.
- Playing the phrase with tāla starts the rhythm; **Stop** stops the current melody and percussion; loop and stop work; rhythm can be independently started/stopped.
- Local save works. Downloaded MIDI was verified to contain `MThd` and `MTrk`; exported JSON parsed correctly with schema `svara-seven-sounds`.
- Screenshots were visually reviewed in the phone and desktop viewports. Resolved initial mobile overflow and piano-header clipping when horizontally scrolling the keybed.

## Security and regressions

- Content security policy remains restrictive: no external network connections, libraries, scripts, or images.
- The new layout moves the original existing nodes and preserves single unique IDs and event handlers rather than rendering a second independent state machine.
- Existing saved composition schema is retained. Import, export and downloadable files remain user-initiated actions.
- No changes are made to the root app at `index.html` or to the original v1.2 branch or default branch.
- Reproducible test script included at `studio/tests/test_studio.py`.

## Not yet verified

1. **Physical Android / iOS** touch gestures, device sound latency, Web Audio unlock behavior, and OS text keyboard interaction.
2. **Perceptual fidelity** of Sanskrit pronunciation, synthetic vowel sound and Indian musical ornaments; professional music/speaker review recommended.
3. **Direct `file://` launch in automated browser:** testing policy blocks navigation with `net::ERR_BLOCKED_BY_ADMINISTRATOR`. The application was loaded in memory; direct file opening should be checked on a real device.
4. CI workflow and GitHub Pages deployment were not enabled or changed.
5. A full adversarial security audit has not been performed. No security guarantee is implied by passing browser checks.

**Decision:** Functional feature-branch candidate PASS (browser automation). Hardware and cultural/musical review outstanding before a polished public launch claim.
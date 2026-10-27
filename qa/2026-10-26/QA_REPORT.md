# Svara Lab — Recursive QA/QC Experiment — 2026-10-26

## Interpretation and scope

**Simulated participants, instrumented browser actions. NO real humans were recruited, interviewed, listened to, recorded, or surveyed.** Persona feedback statements are prospective testing hypotheses, separate from observed event logs. Each deterministic scripted session leaves a task, expected result, observed result, viewport, and pass/fail. Chromium/Playwright was the test environment; physical mobile multi-touch and human auditory judgments remain unknown.

## Capacity decision

- Pilot: **n=3** persona profiles × 7 checks = 21 cases.
- Scaled validation: **x=12** = 3 distinct task profiles × 4 viewport contexts (320×700, 360×780, 390×844, 1440×900). One pass per unique cell (avoids duplicate runs disguised as independent participants).
- Runtime budget for the expanded suite: **90 seconds** of browser testing; measured **9.277 seconds** for 12 sessions (0.77 seconds/session), using headless Chromium on this host. 12 was chosen as the finite coverage matrix, not as a statistical sample size.
- Stop condition: stop at 12 cells, time budget exhaustion, repeated identical findings without new coverage, or an unresolved blocker.

## Observed cycles

| Phase | Synthetic sessions | Script checks passed | Findings |
|---|---:|---:|---|
| A. Baseline pilot | 3 | 12 / 21 | Three repeatable issues (below) |
| B. Pilot after patch | 3 | 21 / 21 | Original tasks passed |
| C. Expanded cohort, initial | 12 | 161 / 165 | Deleting visarga also deleted preceding consonant in four novice sessions |
| D. Expanded cohort, final | 12 | **165 / 165** | All scripted cases passed |
| E. Prior independent v1.2 regression | 2 viewports | 48 / 48 | No observed regressions after edits |

## Reproducible defects and repairs

1. **Incorrect Backspace on pasted phrase.** `composerEvent(undo)` removed the entire `raw` composition event. Reproduced by three pilot profiles: paste `राम`, press keyboard Backspace, observed empty string instead of `रा`. Corrected by deleting an orthographic grapheme within the raw event while preserving its remaining text.
2. **Two-finger sustain prematurely ended.** A first finger's `pointerup` stopped the gate even while another finger still held the button. Reproduced by three pilot profiles. Fixed by tracking outstanding pointer IDs and stopping only after the final release; extra finger-downs do not retrigger the sound.
3. **Active workspace not announced.** `.modebtn` visually highlighted the selected workspace but lacked an `aria-pressed` state. Fixed by syncing `aria-pressed` to navigation state.
4. **Visarga deletion consumed a consonant.** First expanded cohort (4 novice cells) exposed a Unicode grapheme segmentation ambiguity: `रामः` → `रा` instead of `राम`. Refined raw-text Backspace to remove Sanskrit vowel signs/diacritics individually, otherwise delete one grapheme. The whole 12-cell suite was rerun after repair.

## Final validation by synthetic profile

| Scenario | Coverage cells | Checks passed |
|---|---:|---:|
| Novice | 4 | 52 / 52 |
| Sanskrit Editor | 4 | 53 / 53 |
| Music Producer | 4 | 60 / 60 |

## Evidence artifacts

- `pilot.json`: baseline pilot observed results; no human input.
- `cohort.json`: twelve task-driven synthetic sessions; explicitly separates observed tasks from simulated feedback hypotheses.
- `pilot.py`, `cohort.py`, `patch.py`: runnable headless-browser tests and auditable minimal code changes.
- `tests/test_browser.py`: original 48-check regression suite from Svara v1.2 release.
- `index_before.html` and `index.html`: application before and after modifications.
- `QA_dashboard.html`: offline interactive task/session evidence viewer.

## Unresolved risks and next steps

- Real phones: high-frequency multi-touch tracking, screen reader semantics, battery, latency, and visual motor ergonomics are **not verified**. Browser event simulation is insufficient.
- Sanskrit: the phoneme sequencing engine remains an approximate artistic synth. Native Sanskrit speakers should review recordings before claims of phonetic accuracy.
- Data collection: any human beta testing should require **specific opt-in** for session capture and audio recording, redact typed content by default, support deletion, and never ship invisible analytics.
- A useful future human cohort is *three actual volunteers* (beginner, Sanskrit-literate reader, music producer) with short consented tasks. Its data must never be merged with this synthetic cohort as though sourced the same way.

**Release gate**: suitable as a reviewable development PR; not a validated usability study or production speech product. No protected-branch merge was performed.
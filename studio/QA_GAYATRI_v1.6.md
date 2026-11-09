# Svara Play v1.6 — browser verification

**Edition:** `feature/gayatri-mantra-accent-library-v1.6` (based on v1.5 feature branch, does not modify default `main`).

## Completed checks

| Suite | Passing | Result |
|---|---:|---|
| Existing full studio regression | 192 | PASS |
| Existing compact-keyboard checks | 175 | PASS |
| Existing emulated touch swipes | 3 | PASS |
| New Gāyatrī corpus, UI and keyboard integration | 175 | PASS |
| **Total** | **545** | **PASS** |

New 175-check suite in `studio/tests/test_gayatri.py` was executed across 1440×900, 428×926, 390×844, 360×750 and 320×568 Chromium page viewports. Local browser runner restricts file:// and localhost navigation; tests load the **entire offline HTML source in memory** without a network request. There were no uncaught JavaScript page errors in the new suite.

Verified: all 38 records, three provenance categories, 11 exclusively source-attested accent-bearing entries, three Sāvitrī lines, U+0951 / U+0952 display and reversible plain-mode stripping, nicṛd-Gāyatrī explanation, optional invocatory preface, clipboard copy payload integrity (stubbed clipboard), one-click catalog copy, disable accent-copy for unsourced entries, IAST-name search, full-length text transfer, edited-text preview, pinned Sanskrit keyboard as live editor, pinned height cap at 50%, and absence of horizontal page overflow.

## Untested or remaining limitations

- Browser-automation validation **is not** a trained Vedic reciter's assessment; no synthetic playback is represented as authentic chanting.
- Physical Android/iOS keyboard, shaping and clipboard permission tests are pending. An installed fallback lets users select and copy text if clipboard writes are blocked.
- Manual collation of all textual variations and traditional sources remains appropriate. The MNU compilation has documented edition/recension differences and is linked in-app.
- The devotional entries are Gāyatrī-*style* formulas, **not** asserted to have source-authenticated pitch markings or independently verified 8+8+8 syllable counts.
- The original seven-sound composer still plays only the first seven segmented units of a longer mantra; this is explicitly disclosed in the app and is not a 24-syllable chanting engine.
- GitHub CI may report no automated checks for the new branch: these tests ran locally in the container with the specified Chromium binary.

No alterations to the original root `index.html` or to earlier branches are intended in this release.
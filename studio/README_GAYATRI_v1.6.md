# Svara Play v1.6 — Gāyatrī mantra library and Vedic accent reading

**Standalone, offline-capable music and Sanskrit composition app.** Open `index.html` in a modern Chromium, Firefox, or Safari browser. Local browser policies may restrict the clipboard API when opened from Downloads or `file://`; the app supplies a manual selectable-text fallback. Audio instruments require user interaction to start.

This release adds the **Gāyatrī mantra library** to the unified Svara Play workspace without deleting the existing rāga, tāla, piano, Sanskrit flick keyboard, pronunciation experiment, and seven-sound composition tools. The mantra module is embedded in the single HTML file and never fetches internet resources.

## Library

38 curated selections, grouped by *textual provenance*, not by an unsupported popularity ranking:

- **11 accent-attested Vedic verses**: Ṛgveda 3.62.10 (Sāvitrī), the nine Agni verses in Ṛgveda 1.1, and the Sarasvatī verse in Ṛgveda 6.61.7. These preserve the explicitly sourced Unicode Devanāgarī `॑` (svarita in the common Ṛgvedic display convention) and `॒` (anudātta) marks.
- **18 unaccented Upaniṣadic Gāyatrī-form invocations** from the 18 verses grouped in section 3 of the twenty-five-section Mahānārāyaṇa Upaniṣad transcription linked below. This source is **not** an accent-bearing witness. Alternative recensions and formula variants exist.
- **9 later/popular devotional Gāyatrī-style formulae**, including Hanumān, Sarasvatī, Lakṣmī, Rāma, Kṛṣṇa, Sītā, Gaṇeśa, Durgā and Śiva. These are labeled as devotional variants, **not authenticated as accent-bearing Vedic verse**; 8+8+8 scansion has not been independently established for every variant.

The original Sāvitrī verse is technically **nicṛd Gāyatrī** in a standard metrical analysis: its first pāda has an apparent short count with *vareṇyaṃ*, while *vareṇiyam* provides a metrical restoration. The common invocation `ॐ भूर्भुवः स्वः` may be optionally prefixed for copying; it is not part of the canonical Ṛgveda 3.62.10 verse.

## How to use

1. Open the main composer and expand **ॐ Gāyatrī mantra library** under the phrase editor.
2. Search or filter by textual tradition; tap a mantra to view its text, source, theme and meter status.
3. For Vedic entries, leave **Show authentic Vedic accents** enabled to see the original marks **above and below Devanāgarī characters**. Switch it off for plain text.
4. Tap the **⧉** next to a library entry for an immediate plain-text copy, or use the larger **Copy plain** / **Copy with accents** actions for the selected verse. Every verse line has its own copy button.
5. **Load into editor** makes a full-length draft. Focus its field, pin the Sanskrit keyboard and type or edit without losing the original source preview. Check **Preview my edited text** to inspect the marks already present in your edited copy. Marks are never invented.
6. **Insert / replace → Seven Sounds phrase** transfers the full text to the existing composer. That composer intentionally plays its **first seven input units**, not a full Vedic 24-syllable recitation. Its melodic output is unrelated to authentic Vedic pitch accents.
7. If the browser denies clipboard access, the app exposes a selectable text field for copy using your system menu.

## What the accent lines mean

In the **common Ṛgvedic Devanāgarī transcription** used here:

- `॒` (U+0952) is used for *anudātta*, the marked low accent.
- `॑` (U+0951) is generally used for *svarita*, a post-accent or other contextual contour, printed above the syllable.
- An **unmarked syllable is not always automatically an udātta**: context, pragṛhya/pracaya, sandhi, and recension-specific conventions matter. Unlike a modern keyboard note, a Vedic accent category is *not an absolute frequency*.

Sanskrit is more diverse than the label “classical Sanskrit accents” suggests: Vedic recensional pitch notation is not standard orthography in the later classical Sanskrit literary corpus. The app does not claim its piano, vowel synthesizer, or seven-note mapping delivers authentic oral lineage-specific Vedic chanting.

## Sources and text handling

Every selection links its supporting edition inside the interface. Key references:

- [Ṛgveda 3.62.10 — Vedshala](https://vedshala.org/gayatri-mantra) — accent-marked Śākala Sāvitrī.
- [Ṛgveda 1.1 — Vedic Samhita](https://www.vedicsamhita.in/vedas/rigveda/1/1) — verse-level accents and meter classification. Also consult [Sanskrit Wikisource Ṛgveda 1.1](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१.१) and the historic Vedic text itself.
- [Ṛgveda 6.61.7 — Vande Mataram Library](https://vmlt.in/rigveda/06/061/7) — Sarasvatī accent transcription.
- [Mahānārāyaṇa Upaniṣad — Adiveda edition](https://adiveda.in/reading/upanishad/mahanarayana-upanishad/) — section 3 and edition/recension cautions.
- [Later devotional formulae — Sanskrit Documents](https://sanskritdocuments.org/doc_z_misc_major_works/gaayatriimantraaH_devanagari.html) — variant-rich devotional catalog.
- [Understanding the three accents](https://www.learnsanskrit.org/ends/sounds/accent/) and [Unicode Devanāgarī code chart](https://www.unicode.org/charts/PDF/U0900.pdf).

*Catalog inclusion is not a claim of exhaustiveness or a statistically determined popularity ranking.* Texts, textual variants, and pronunciation require an expert native Sanskrit/Vedic reciter review before using the app as an authoritative recitation guide. No outside site's creative editorial material or audio is embedded. The Sanskrit verse texts are ancient or traditionally circulating words; provided links disclose textual witnesses, not ownership of those traditions.

## Code and testing

- Single-file `studio/index.html` has no network fetches or third-party JS dependencies.
- Human-readable machine catalog in `studio/data/gayatri_catalog.json` for source inspection; the same data is bundled in the HTML for offline operation.
- Run `python studio/tests/test_gayatri.py` from a checkout with Chromium and Playwright installed (Chromium binary path can be adapted in the script).
- Previous music-studio, compact keyboard, and touch tests are preserved and also pass under the current browser-run environment.

**Limits:** The Unicode accent glyph shape and below/above placement depend on the device's Devanāgarī font engine; Android/iOS physical-device verification and scholarly recitation comparison remain outstanding. User-edited drafts are not auto-corrected. The library editor's contents are not automatically added to the 30-item seven-sound local notebook unless the user uses that notebook explicitly.
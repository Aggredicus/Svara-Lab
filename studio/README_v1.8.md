# Svara Play v1.8 · Mobile Flow

A **single-file, offline Indian classical music and Sanskrit typing studio**, redesigned around one continuous mobile-first instrument surface.

## Open and use

Open `Svara_Play_v1.8.html` directly in a modern Android, iOS, or desktop browser. In the repository, open `studio/index.html`. No build, account, internet access, library CDN, or backend service is required. Tap a note or the sound-enable button to permit Web Audio in browsers requiring user interaction.

### The new everyday workflow

1. **Select a rāga** with the compact top picker; tap ‹ / › to cycle. Change **Sa** with the adjacent − / + buttons, without navigating anywhere.
2. Tap **Keys · families · favorites** to expand the optional twelve-key strip, scale-family filter, favorite rāgas and auto-preview toggle. Fold it when done.
3. **Write** a seven-sound phrase and hear, loop, compare or stop it. Use the compact Sanskrit keyboard, copy/paste, or your normal device keyboard.
4. **Play** on the three-octave piano or seven svara buttons, and **Beat** to start a tāla. Adjust playback speed from the small rhythm control.
5. Use the bottom **Play / Write / Beat / Mantras / Explore** shortcuts to jump to the relevant area *in the same page*. The shortcuts remain accessible in the bottom area reserved by the original pinned keyboard, so you can jump between parts of the app while composing.
6. Expand **Story and symbolism**, **Timing · mapping notes**, **Tuning · piano tips**, or any of the compact explorer cards for advanced controls without losing the current music state.

### Everything retained

- Svara/piano synthesis, movable Sa, chromatic key changes, just-intonation option, drone, instrument settings and responsive keyboard
- Hindustani rāgas and thāṭs, 72 Carnatic mēḷakartā scales, curated phrases and learning exercises
- Hindustani and Carnatic rhythm catalog, beat grid, subdivisions and tihāī lab
- Seven-sound text composer, Sanskrit text mode, experimental vowel voice, looping, notes, comparative transposition, MIDI and JSON imports/exports, local notebook
- Original two-thumb Sanskrit modal keyboard with directional gestures, visible five-position variants, pinned/collapsible position, clipboard controls and text-field targeting
- Gāyatrī library with 38 selections, 11 source-attested Vedic accent-marked verses, full-length editor, searchable list and copying of plain or accent-marked text
- Symbolism, rāgamālā art context, research sources and explanatory limitations

### Keyboard design locked

**No changes to the v1.7 keyboard implementation or its styling** were made for this release. The v1.4 five-way keyboard script and styles and the v1.5 compact two-thumb keyboard style were compared byte-for-byte against v1.7. v1.7 utility ergonomics are preserved. The new application navigation hides only while the keyboard is pinned.

### Musical and scholarly limitations

A rāga is more than a scale; piano tones do not fully reproduce gamakas, meend, and singing style. Vedic accent marks are traditional notation, not a fixed Western pitch score. Later devotional mantra selections without verified Vedic accent readings are not given invented marks. The experimental vowel synthesizer is not a fully validated Sanskrit pronunciation engine. Seek experienced teachers and primary-source editions for authentic chant training.

### Privacy and offline operation

Audio and interface code run locally. Phrase saves use the browser's local storage when available. JSON/MIDI export is the recommended durable backup. Browser speech synthesis depends on the device's installed voices, and clipboard operations depend on browser permissions; manual fallback is retained. This release adds no analytics, external requests or new permissions.

## Development and QA

The change is incremental and reversible, committed only to `feature/svara-mobile-flow-v1.8`, based on the preserved v1.7 branch. Main and prior feature branches are untouched.

The local Chromium regression runs passed **785/785 checks** across studio, compact keyboard, touch events, thumb-utility ergonomics, mantra library and new mobile-flow tests. The old studio browser test was adjusted to expand the now-collapsed options before testing them. See `QA_REPORT_v1.8.md` for scope and limitations. Real Android and iOS usability tests and independent musical/scholarly reviews are still recommended before merging this branch to main or presenting the app as an authoritative performance guide.
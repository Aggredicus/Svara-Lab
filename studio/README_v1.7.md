# Svara Play v1.7 — ergonomic two-thumb utility layout

The v1.6 music and mantra app is retained unchanged except for the order and subtle emphasis of keyboard utility buttons.

### Utility arrangement

- Left thumb, final row: **Undo ↶ | Virāma ् | Caret left ◀ | Caret right ▶**
- Right thumb, final row: **Copy ⧉ | Space ␣ | Backspace ⌫**
- Right thumb, spare cell directly above: **Paste ⤓**

The right vowel grid contains seven character keys, so moving low-frequency Paste into its pre-existing open slot keeps all the frequent editing controls in comfortable bottom-row positions without adding a new letter or an empty spacer.

### Frequency and reach rationale

In the built-in 38-mantra Sanskrit corpus, 272 spaces and 257 virāmas were measured. Relative scores: Space 100, Virāma 94, Backspace 32, Caret-left 20, Caret-right 18, Copy 14, Paste 13, Undo 9. The last six figures are design assumptions, **not user telemetry**.

At 390px viewport width, a simplified horizontal reach model placing virtual thumb rests at 25% and 75% of screen width yields a frequency-weighted mean button distance of **50.1px in v1.6 versus 31.1px in v1.7**, a **38% decrease in the model**. This is not a measured typing-speed or comfort improvement.

References: [NIOSH/CDC thumb posture study](https://stacks.cdc.gov/view/cdc/224411) and [two-thumb text-entry touch error study](https://pubmed.ncbi.nlm.nih.gov/34340012/).

### Usage
Open `studio/index.html`, expand Sanskrit keyboard, tap **Pin**, then type. The keyboard remains under half screen height, with all functions available. Copy and paste still act on the selected text field.

See [design baseline](./KEYBOARD_DESIGN_LOCK.md) and [QA report](./QA_REPORT_v1.7.md). All earlier branches remain untouched.

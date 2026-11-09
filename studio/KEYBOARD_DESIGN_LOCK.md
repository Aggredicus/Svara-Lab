# Approved Sanskrit keyboard baseline

**Design reference:** The user explicitly approved the November 9, 2026 Android screenshot as the desired visual tone. Preserve the existing Svara Play dark teal, illuminated sea-glass borders, compact rounded keys and readable Sanskrit glyphs. The screenshot is intentionally **not** committed because it shows phone status and notification chrome.

## Locked interaction characteristics
- Two-thumb keyboard: four-column consonant grid left and vowel grid right, positioned as in the approved screenshot.
- Five glyph choices visibly arranged by center, up, right, down and left, without drawn arrow decorations.
- Tap/hold/directional-swipe character entry; preserve correct two-thumb ordering.
- Pinned, position-lockable and collapsible floating board with live text preview, text-field selection, clipboard, undo and caret editing.
- Pinned layout limited to half the viewport height without internal key scrolling.
- All existing piano, rāga, tāla, Sanskrit and Gāyatrī tools remain functional.

## v1.7 approved-scope modification
Only the utility placement changes. Left row: Undo / Virāma / Cursor-left / Cursor-right. Right bottom: Copy / Space / Backspace. Paste remains in the existing spare cell above. Maintain eight stable button IDs and event handlers.

For future changes, prioritize reversible commits, explicit user approval for broader restyling, browser tests and real-phone checks.

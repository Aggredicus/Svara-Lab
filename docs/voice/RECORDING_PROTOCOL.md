# Svara Lab — speaker-consented recording protocol
Status: **proposed**. No new recording is required to complete this research design.

## Privacy and permission
- Record only the consenting target speaker. Keep **original voice audio local/private**; do not put it in the public Svara Lab GitHub repository or embed it in the shipped website.
- Obtain explicit, separate permission for any third-party model API, public demo, shared dataset, or voice checkpoint release. Using audio inside a private research session is **not** blanket approval to publish it.
- Store each take as an immutable file plus a UTF-8 transcript and quality metadata; support local deletion of audio and derived voice embeddings. Treat speaker embeddings and voice models as sensitive biometric-like artifacts.
- Before accepting external donations of recordings, record permission and license for that exact use.

## Recording setup
- Prefer mono PCM WAV, 48,000 Hz, 24-bit (16-bit acceptable) in a quiet, acoustically consistent room. Disable automatic effects such as aggressive denoising, reverb, automatic gain control and echo cancellation when possible.
- Microphone distance ~15–20 cm with consistent orientation and a pop filter; avoid clipping and excessive plosives. Record 1–2 s of room tone at beginning and end.
- Use natural speaking volume and pace, no theatrical overarticulation unless the prompt explicitly requires it.
- Capture a short calibration phrase each day and verify levels before recording a large corpus; retake after environmental changes.
- Record phrases with short silences between them. Mark mistaken takes rather than improvising their transcripts.
- Use Unicode Devanāgarī **and** IAST for annotations; verify exact word/letter order. Preserve the intended traditional Sanskrit pronunciation, including long vowels and aspirated stops.

## Pilot corpus (20–30 minutes)
### A — independent vowels (14)
अ आ इ ई उ ऊ ऋ ॠ ऌ ॡ ए ऐ ओ औ
Read each independently **three times** at normal pitch and duration; then hold the phonation where possible for 1–2 s for the musical sustain experiment. Note that ॠ, ऌ, ॡ are rare and may need phonetic coaching.

### B — consonant classes (33 canonical + optional ळ)
क ख ग घ ङ
च छ ज झ ञ
ट ठ ड ढ ण
त थ द ध न
प फ ब भ म
य र ल व श ष स ह
ळ
Read each consonant as a natural CV syllable with the inherent अ. **Do not pretend an isolated stop consonant is a sustain-capable vowel.** For the plosives, compare release burst, aspiration and the following vowel.

### C — balanced vowel contexts
For each consonant class and individual member, sample 4–5 vowels (for example अ आ इ उ ऋ) at least once. This is an experimental **CV matrix**; fewer entries are acceptable for the rare phonemes in a short pilot. Record separate phone-level boundaries where feasible.

### D — minimal-pair and contrast exercises
- Dental vs retroflex: त / ट, द / ड, न / ण
- Aspiration: क / ख, ग / घ, प / फ, ब / भ
- Voicing: क / ग, त / द, प / ब
- Vowel length: अ / आ, इ / ई, उ / ऊ, ऋ / ॠ
- Sibilants: श / ष / स
- Nasals: ङ / ञ / ण / न / म
Clearly read target pairs with a pause; repeat in several vowel contexts.

### E — words and consonant clusters
राम, सीता, कृष्ण, राधा, गुरु, योग, धर्म, ज्ञान, शान्ति, सत्य, प्रेम, जीवन, करुणा, ब्रह्म, क्षमा, प्रज्ञा, श्रुति
Conjunct prompts: क्ष, त्र, ज्ञ, श्र, क्र, ग्र, स्त्र, द्ध, द्भ, स्फ. Some are **not** independent lexical words; mark them as cluster tests rather than teaching their utterance in isolation as if they were ordinary words.

### F — connected speech and prosody
Read several short prose sentences and traditional verses of known provenance; annotate all text and choose ordinary spoken Sanskrit vs metered chanting explicitly. For devotional practice, separately collect a consenting speaker's actual recitation style. **Do not treat Vedic accent as the same task as classical śloka chant.**

## Expanded corpus (45–90 minutes)
- Add short, medium and long Sanskrit phrases with diverse phoneme contexts, word boundaries and sandhi patterns.
- Add conversational, recited, and intentionally sustained musical vowel sessions as **separate speaking styles**.
- Capture varied but labelled pitch, intensity, breathiness and pace; do not mix these styles in unlabelled training data.
- Keep ≥10–15% of the **text prompts** entirely unseen for evaluation. Avoid splitting duplicates of the same prompt across train and held-out partitions.
- Label reference confidence and uncertain pronunciations; seek an expert check for rare sounds and Vedic accented samples.

## Suggested private manifest per take
```json
{
  "schema": "svara-speaker-take/v1",
  "take_id": "private-0001",
  "speaker_permission": "local-research-only",
  "text_devanagari": "क ख ग घ ङ",
  "text_iast": "ka kha ga gha ṅa",
  "audio_path": "private/recordings/0001.wav",
  "sample_rate_hz": 48000,
  "speaker_style": "spoken",
  "microphone": "user-described-mic",
  "room_id": "private-room-A",
  "quality_review": "pending",
  "language": "sa",
  "is_public": false,
  "split": "unassigned",
  "phonetic_notes": ""
}
```
Audio paths, hashes and speaker identifiers stay **private**; public QA reports use opaque IDs and aggregated statistics only.

## Why the original English ABC clip remains useful
Its clean English letter names can provide a modest signal for general voice character and a tone-conversion proof of concept; they do not demonstrate Sanskrit aspiration, retroflexion, vowel length, anusvāra or conjunct coarticulation. Keep it as a separate reference sample and **do not** label it as Sanskrit data.

## Stop criteria
Stop a take when clipping, room changes, major pitch drift, or transcript mismatch is detected. Stop data publishing/training when consent or commercial rights are unclear.

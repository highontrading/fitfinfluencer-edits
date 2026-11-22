# Editing pipeline

The pipeline that produces the FitFinfluencer edits. Every edit from batch 5 onwards must follow [`../EDITING_RULES.md`](../EDITING_RULES.md).

## v2 flow (batch 5 onwards)

1. **Transcribe and chunk:** `transcribe.py`, then `chunks.py`, writing `ch<N>.json`.
2. **Find retakes:** run `takes.py work/ch<N>.json`. It flags earlier takes so you keep the last one. It is advisory only, so read each take in context.
3. **Write the EDL:** `edl/v<N>.json` lists the chunks to keep (last takes), with the Hinglish caption text. Speed is 1.1.
4. **Cut:** `cut.py edl/v<N>.json work`. This frame-aligns the shots and speeds them up to 1.1x with pitch and formant preserved. The voice gets no other processing.
5. **Track the face:** `face.py work v<N>`.
6. **Build the spec:** `build_v<N>.py`, using `spec_lib2.Spec`. It blocks emojis; all on-screen text must be in English. Helpers:
   - `kin()` for free-position kinetic text;
   - `behind()` for a word behind the speaker;
   - `ecg`, `callout`, `stamp`, `photo`, `cine` components;
   - `broll()` for stock footage or the creator's own clips and photos.
   See `example_v2_build.py`.
7. **Render:** `pipe2.sh <N>`. It runs:
   - `mix.py`: voice untouched, sound effects at 30%, no music;
   - `render/render2.js`: front and behind overlay layers;
   - `compose2.py`: person cut-out from `personseg.py`, B-roll, grain.
8. **Preview:** `preview2.sh v<N> t1 t2 …` makes a contact sheet of stills. Check it before the full render.
9. **Deliver:** `deliver.sh in.mp4 out.mp4` keeps each file under ~95 MB. List the stock used in `STOCK_CREDITS.md`.

## Long-form (landscape 16:9)

- Build specs with `Spec(..., size=[1920,1080])`. See `build_v25.py`:
  - chapter cards use `cine` bars and a big title;
  - card panels sit on the right (`CARD=[1000,90,860,900]`), and the speaker stays on the left.
- At 1080p the PNG overlays do not fit on disk. Render with `pipe2stream.sh <N>` instead:
  - the renderer keeps at most 900 frames ahead of the compositor;
  - the compositor deletes each frame after it is used;
  - the vignette is drawn in the compositor (`vigInCompose`).
- **Delivery:** GitHub caps files at 100 MB, so the long-form goes in the repo as parts split at chapter starts. Each part is cut with stream copy at forced keyframes. The full file is sent directly.
- `hinglish.py` converts Devanagari transcripts to Hinglish caption text.
- `credits5.py` writes `STOCK_CREDITS.md`, covering both Mixkit and Wikimedia Commons assets.

## Batch 6 additions (queues and checks)

- **`gaps.py <N>`:** lists transcript words that fall outside every chunk. Use it to catch words the pause splitter dropped, e.g. "fake" in v26. Fix these with `s`/`e` overrides in the EDL.
- **`cutq.sh N...`, `renderq.sh N...`:**
  - These run cuts and renders one at a time.
  - `pipe6.sh` builds the spec, mixes the audio, then streams the render and compose.
  - To wait for an earlier queue, use `while kill -0 PID`. Never grep `ps` for a pattern that also appears in your own command line.
- **`qa6.sh N`:** builds a 30-frame contact sheet of the final render and reports loudness.
- **ffmpeg in a `while read` loop:** run it with `< /dev/null`, otherwise it consumes the loop's input.
- **Stamp position (portrait):**
  - Captions sit around y 1360–1450, so keep stamps above them (y about 1150–1190, size 120 or less for one line, about 80 for two lines).
  - Never show a stamp in card mode, because it covers the speaker inset.
- **Anchors:**
  - `T(word)` returns the FIRST occurrence of the word. Anchor repeated words ('kaise', 'aapke', 'bill', 'baat') with `after`.
  - Numbers normalise with dashes stripped: "6-8" becomes `T('68')`.
- **Mixkit licensing:** most medical, salt and tea clips are personal-use-only. Use Wikimedia Commons PD, CC0 or CC BY images through the `photo` event instead.
- **`fetch_stock.py`:** now merges into `meta.json` instead of overwriting it.

## Re-editing old recordings (batch 7)

- **`oldedl.py N M`:** compares an old EDL (`edl/vM.json`) with the new chunking of the same raw (`chN.json`), showing the takes flags.
  - The chunker is deterministic, so chunk ids line up.
  - Reuse the old captions, but re-check the last takes: the old v13–v18 EDLs predate the "always keep the last take" rule in a few places.
- **`renderd.sh`:** renders everything listed in `work/rq7.txt`, one at a time, and stops after `END`. It survives queue edits.
  - Never rewrite `renderq7.log` in place while it is running: an open `>>` handle keeps writing to the old file.

## Setup in a new session

- Copy this folder to a scratch dir and fix the `S=` path in the `*.sh` scripts.
- In `render/`, run `npm install`.
- Install the Python dependencies: `pip install faster-whisper mediapipe soundfile scipy opencv-python-headless gdown`, plus `apt-get install libegl1` for mediapipe.
- Use the Chromium that is pre-installed with Playwright.
- `models/selfie_multiclass.tflite` is the person-segmentation model (MediaPipe, Apache-2.0).
- `face.py` needs `face_detection_yunet_2023mar.onnx` (OpenCV Zoo).

## Stock licensing

- **Mixkit:** only clips whose page says "Free License" (`lic_scan.py`). Never use Restricted ones.
- **Wikimedia Commons:** `commons.py` keeps only Public domain, CC0 and CC BY files (no ShareAlike, NC or ND).
- **Stock metadata:** `stock/*.json`. The clips themselves are not in the repo.

## Batch 8 additions (new container, Moon Crew, queues)

- **Fonts are bundled.** `render/fonts/base.css` (Poppins, Montserrat, Anton, JetBrains Mono) and `mc.css` (Cormorant Garamond, Michroma, Manrope) are local web fonts.
  - A fresh container has none of these installed, and the cards silently fell back to a serif.
  - `render2.js` preloads every bundled font before the first frame.
- **Chromium path:** use the stable symlink `/opt/pw-browsers/chromium`. Versioned paths change between containers.
- **`mkedl.py N`:** builds `edl/vN.json` from a compact keep list `work/kN.txt` (`cid [s=..] [e=..] | caption`).
  - It auto-extends a chunk edge to cover a transcript word the pause splitter clipped.
  - The extension is capped at 0.45s and clamped to the neighbouring chunks.
  - Keep lists are saved in `edl/keep/`.
- **Language:** whisper sometimes detects Hindi as Urdu (`ur`). In that case re-run with `transcribe_hi.py`, which forces `language='hi'`.
- **Daemons:** `cutd.sh` (reads `work/cq8.txt`), `renderd8.sh` (`work/rq8.txt`) and `deliverd8.sh` (QA sheet plus `deliver.sh` for each "vN RENDERED", using `work/names8.txt`).
  - To re-render or re-deliver, remove that video's line from `renderq8.log` / `deliver8.log` **in place** (open `r+`, rewrite, truncate). Never use `sed -i`.
- **Moon Crew theme (`mc_theme.py`):** for the creator's Mooncrew Club videos (English, rave/festival topics).
  - Colours: black, ivory, champagne. Type: Cormorant Garamond headlines, Michroma labels, Manrope body.
  - B-roll is graded darker and softer (`bright=-0.17, sat=0.78`).
  - The end card carries the exact final Mooncrew logo (`MC.end_card`). Brand pill: "MOONCREW CLUB".
  - Pass `extra={'css': MC.CSS}` to `S.save`. The overlay injects `spec.css`, and the `html` event type renders free-form markup such as the logo.
- **Labels at y=110 or y=1600:** Michroma (`font='label'`) is very wide, so keep these to about 32 characters. Bottom labels sit at y=1600, clear of two-line captions.
- **Anchor pitfall (again):** `T('your')`, `T('this')`, `T('ill')` (I'll) and `T('aur', T(x))` point *after* `x`. For the word *before* `x`, anchor on an earlier unique word.

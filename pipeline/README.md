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

#!/bin/bash
# preview2.sh name t1 t2 ... -> work/sheet_<name>.jpg (fully composited v2 frames)
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S; name=$1; shift
rm -rf work/pv_$name; mkdir -p work/pv_$name
FR=$(python3 -c "import sys; print(','.join(str(round(float(t)*30000/1001)) for t in sys.argv[1:]))" "$@")
node render/render2.js work/${name}_spec.json work/pv_$name 2 $FR > /dev/null
FRAMES=$FR python3 -I scripts/compose2.py work $name work/pv_$name none work/pv_$name/c 2>&1 | grep -v -E "^$name|^W0000|^I0000|absl|XNNPACK|TfLite|Exception ignored|Traceback|File \"|TypeError|lib =|^\s|InitGoogle"
python3 -I - "$name" <<'PY'
import cv2, numpy as np, glob, sys
n = sys.argv[1]; fs = sorted(glob.glob(f'work/pv_{n}/c_*.jpg')); tiles = []
for f in fs:
    im = cv2.imread(f); im = cv2.resize(im, (270, 480) if im.shape[0] > im.shape[1] else (480, 270), interpolation=cv2.INTER_AREA)
    fr = int(f.split('_')[-1][:-4]); cv2.putText(im, f'{fr*1001/30000:.1f}', (8, im.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2); tiles.append(im)
C = 6 if tiles[0].shape[0] > tiles[0].shape[1] else 4
while len(tiles) % C: tiles.append(np.zeros_like(tiles[0]))
cv2.imwrite(f'work/sheet_{n}.jpg', np.vstack([np.hstack(tiles[i:i+C]) for i in range(0, len(tiles), C)]), [cv2.IMWRITE_JPEG_QUALITY, 85])
PY

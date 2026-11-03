#!/bin/bash
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S
for v in "$@"; do
  python3 -I scripts/face.py work v$v > work/face_v$v.log 2>&1
  rm -rf work/ov_v$v; node render/render.js work/v${v}_spec.json work/ov_v$v 3 > work/ov_v$v.log 2>&1
done
echo DONE >> work/ov_batch_$1.log

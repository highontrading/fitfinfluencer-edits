#!/bin/bash
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S
for v in 12 10 11; do
  rm -rf work/ov_v$v; node render/render.js work/v${v}_spec.json work/ov_v$v 3 > work/ov_v$v.log 2>&1
  python3 -I scripts/compose.py work v$v work/ov_v$v work/v${v}_mix.wav out/v${v}_final.mp4 > work/comp4_v$v.log 2>&1
  rm -rf work/ov_v$v
done
echo ALLDONE > work/final4.done

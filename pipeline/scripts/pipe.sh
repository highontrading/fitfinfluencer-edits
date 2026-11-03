#!/bin/bash
# pipe.sh N : wait for cut, then face -> spec -> mix -> overlay -> compose
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S; v=$1
until grep -q "^v$v " work/cut4_log.txt 2>/dev/null; do sleep 15; done
python3 -I scripts/face.py work v$v > work/face_v$v.log 2>&1
python3 scripts/build_v$v.py work > work/build_v$v.log 2>&1
python3 -I scripts/mix.py work v$v audio > work/mix_v$v.log 2>&1
rm -rf work/ov_v$v; node render/render.js work/v${v}_spec.json work/ov_v$v 3 > work/ov_v$v.log 2>&1
python3 -I scripts/compose.py work v$v work/ov_v$v work/v${v}_mix.wav out/v${v}_final.mp4 > work/comp5_v$v.log 2>&1
rm -rf work/ov_v$v
echo DONE > work/pipe_v$v.done

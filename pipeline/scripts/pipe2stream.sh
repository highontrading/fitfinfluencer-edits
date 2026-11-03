#!/bin/bash
# like pipe2.sh, but overlay frames are streamed to the compositor and deleted after use (for long videos / low disk)
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S; v=$1
[ -f work/v${v}_face.json ] || python3 -I scripts/face.py work v$v > work/face_v$v.log 2>&1
python3 scripts/build_v$v.py work > work/build_v$v.log 2>&1 || { echo BUILD FAILED; exit 1; }
python3 -I scripts/mix.py work v$v audio > work/mix_v$v.log 2>&1
rm -rf work/ov_v$v; mkdir -p work/ov_v$v
STREAM=1 node render/render2.js work/v${v}_spec.json work/ov_v$v 2 > work/ov_v$v.log 2>&1 &
STREAM=1 python3 -I scripts/compose2.py work v$v work/ov_v$v work/v${v}_mix.wav out/v${v}_final.mp4 > work/comp_v$v.log 2>&1
wait
rm -rf work/ov_v$v
echo DONE > work/pipe_v$v.done

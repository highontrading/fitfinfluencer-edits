#!/bin/bash
# batch 6: build spec -> mix (voice untouched, sfx 30%, no music) -> streamed 2-layer overlay + compose
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S; v=$1
(cd scripts && python3 build_v$v.py ../work) > work/build_v$v.log 2>&1 || { echo "v$v BUILD FAILED"; exit 1; }
python3 -I scripts/mix.py work v$v audio > work/mix_v$v.log 2>&1 || { echo "v$v MIX FAILED"; exit 1; }
rm -rf work/ov_v$v; mkdir -p work/ov_v$v
STREAM=1 node render/render2.js work/v${v}_spec.json work/ov_v$v 2 > work/ov_v$v.log 2>&1 &
STREAM=1 python3 -I scripts/compose2.py work v$v work/ov_v$v work/v${v}_mix.wav out/v${v}_final.mp4 > work/comp_v$v.log 2>&1
wait; rm -rf work/ov_v$v
[ -s out/v${v}_final.mp4 ] && echo "v$v RENDERED $(ffprobe -v error -show_entries format=duration -of csv=p=0 out/v${v}_final.mp4)" || echo "v$v RENDER FAILED"

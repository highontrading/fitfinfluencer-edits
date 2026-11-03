#!/bin/bash
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S
until grep -q "rendered" work/ov_v3.log 2>/dev/null; do sleep 5; done
rm -rf work/ov_v1; node render/render.js work/v1_spec.json work/ov_v1 2 > work/ov_v1.log 2>&1 &
python3 -I scripts/compose.py work v2 work/ov_v2 work/v2_mix.wav out/v2_final.mp4 > work/comp_v2.log 2>&1
python3 -I scripts/compose.py work v3 work/ov_v3 work/v3_mix.wav out/v3_final.mp4 > work/comp_v3.log 2>&1
wait
python3 -I scripts/compose.py work v1 work/ov_v1 work/v1_mix.wav out/v1_final.mp4 > work/comp_v1.log 2>&1
echo ALLDONE > work/final.done

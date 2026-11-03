#!/bin/bash
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S
for v in 8 6 5 7 9 4; do
  until grep -q "^rendered" work/ov_v$v.log 2>/dev/null; do sleep 10; done
  python3 -I scripts/compose.py work v$v work/ov_v$v work/v${v}_mix.wav out/v${v}_final.mp4 > work/comp3_v$v.log 2>&1
done
echo ALLDONE > work/final3.done

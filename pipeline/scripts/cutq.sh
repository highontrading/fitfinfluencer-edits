#!/bin/bash
# cut + face-track each EDL given, in order
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S/scripts
for v in "$@"; do
  python3 cut.py ../edl/v$v.json ../work > ../work/cut_v$v.log 2>&1 && python3 face.py ../work v$v >> ../work/cut_v$v.log 2>&1 && echo "cut v$v ok $(head -1 ../work/cut_v$v.log)" || echo "cut v$v FAILED"
done

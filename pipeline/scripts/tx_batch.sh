#!/bin/bash
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad
cd $S/scripts
python3 -I transcribe.py $S/work 13 14 15 16 17 18 > $S/work/tx4.log 2>&1
for i in 13 14 15 16 17 18; do
  lang=$(grep "^$i " $S/work/tx4.log | awk '{print $2}')
  python3 -I chunks.py $S/work $i ${lang:-hi} -42 > $S/work/ch$i.txt 2>/dev/null
done
echo DONE >> $S/work/tx4.log

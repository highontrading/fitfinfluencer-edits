#!/bin/bash
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
for n in 42 43 44 45 46 47 48 49 50 51; do
  until grep -q "^v$n done" work/fetch8.log 2>/dev/null; do sleep 20; done
  (cd scripts && python3 -I transcribe.py ../work $n >> ../work/tx8.log 2>&1)
  lang=$(grep "^$n " work/tx8.log | awk '{print $2}')
  (cd scripts && python3 -I chunks.py ../work $n ${lang:-hi} -42 > ../work/ch$n.txt 2>/dev/null)
  python3 -I scripts/takes.py work/ch$n.json > work/takes$n.txt
  echo "ch$n ready" >> work/tx8.log
done
echo ALLDONE >> work/tx8.log

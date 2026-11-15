#!/bin/bash
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
for n in 26 27 28 29 30 31 32; do
  until grep -q "^v$n done" work/fetch6.log 2>/dev/null; do sleep 20; done
  (cd scripts && python3 -I transcribe.py ../work $n >> ../work/tx6.log 2>&1)
  lang=$(grep "^$n " work/tx6.log | awk '{print $2}')
  (cd scripts && python3 -I chunks.py ../work $n ${lang:-hi} -42 > ../work/ch$n.txt 2>/dev/null)
  python3 -I scripts/takes.py work/ch$n.json > work/takes$n.txt
  echo "ch$n ready" >> work/tx6.log
done
echo ALLDONE >> work/tx6.log

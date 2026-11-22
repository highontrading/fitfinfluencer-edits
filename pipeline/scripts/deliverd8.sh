#!/bin/bash
# delivery daemon: for each "vN RENDERED" in renderq8.log not yet in deliver8.log -> qa sheet + deliver.sh into edited/batch8
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S; R=/home/user/fitfinfluencer-edits
touch work/deliver8.log
while true; do
  for v in $(grep -o "^v[0-9]* RENDERED" work/renderq8.log | cut -c2- | cut -d' ' -f1); do
    grep -q "^d$v " work/deliver8.log && continue
    nm=$(grep "^$v " work/names8.txt | cut -d' ' -f2); [ -z "$nm" ] && continue
    scripts/qa6.sh $v > work/qa_v$v.txt 2>&1 < /dev/null
    out=$(scripts/deliver.sh out/v${v}_final.mp4 $R/edited/batch8/$nm.mp4 < /dev/null)
    echo "d$v $out" >> work/deliver8.log
  done
  grep -q "^ALLDELIVERED" work/deliver8.log && exit 0
  sleep 30
done

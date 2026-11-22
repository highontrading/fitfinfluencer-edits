#!/bin/bash
# cut daemon: cuts every N listed in work/cq8.txt (one per line) not yet in work/cutd8.log; stops at END
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
while true; do
  next=""
  while read -r v; do
    [ "$v" = END ] && { [ -z "$next" ] && exit 0; break; }
    grep -q "^cut v$v " work/cutd8.log 2>/dev/null || { next=$v; break; }
  done < work/cq8.txt
  if [ -z "$next" ]; then sleep 15; continue; fi
  scripts/cutq.sh $next >> work/cutd8.log 2>&1 < /dev/null
done

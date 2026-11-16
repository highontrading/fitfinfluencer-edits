#!/bin/bash
# render daemon: renders every video listed in work/rq7.txt (one at a time), stops after a line END and nothing left
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
touch work/rq7.txt work/renderq7.log
while true; do
  next=""
  for v in $(grep -v END work/rq7.txt); do grep -q "^v$v \(RENDERED\|RENDER FAILED\|BUILD FAILED\|MIX FAILED\)" work/renderq7.log || { next=$v; break; }; done
  if [ -z "$next" ]; then grep -q END work/rq7.txt && exit 0; sleep 30; continue; fi
  while pgrep -f "scripts/pipe6.sh" > /dev/null; do sleep 20; done
  grep -q "^v$next RENDERED" work/renderq7.log || scripts/pipe6.sh $next >> work/renderq7.log 2>&1 < /dev/null
done

#!/bin/bash
# render each video in order (one render at a time)
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
for v in "$@"; do scripts/pipe6.sh $v; done

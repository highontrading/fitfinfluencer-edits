#!/bin/bash
# sheet_final.sh in.mp4 out.jpg t1 t2 ...
in=$1; out=$2; shift 2; d=$(mktemp -d -p work); i=0
for t in "$@"; do ffmpeg -v error -ss $t -i $in -frames:v 1 -vf "scale=270:480,drawtext=text='$t':x=8:y=455:fontcolor=yellow:fontsize=20" $d/$(printf %03d $i).jpg; i=$((i+1)); done
ffmpeg -v error -y -pattern_type glob -i "$d/*.jpg" -vf tile=6x$(( (i+5)/6 )) -frames:v 1 $out; rm -rf $d

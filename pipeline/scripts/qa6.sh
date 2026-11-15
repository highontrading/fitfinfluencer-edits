#!/bin/bash
# qa6.sh v -> work/qa_v.jpg : 30 frames sampled across the final render
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S; v=$1
f=out/v${v}_final.mp4; d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)
rm -rf work/qa$v; mkdir -p work/qa$v
for i in $(seq 0 29); do t=$(python3 -c "print(round(($i+0.5)*$d/30,2))"); ffmpeg -v error -y -ss $t -i $f -frames:v 1 -vf "scale=270:480,drawtext=text='$t':x=6:y=h-24:fontsize=18:fontcolor=yellow" work/qa$v/$(printf %02d $i).jpg; done
ffmpeg -v error -y -pattern_type glob -i "work/qa$v/*.jpg" -vf tile=6x5 work/qa_v$v.jpg
ffprobe -v error -show_entries stream=codec_name,width,height,bit_rate -show_entries format=duration,size -of compact $f
python3 -I -c "
import subprocess,json,sys
r=subprocess.run(['ffmpeg','-i','$f','-af','volumedetect','-vn','-f','null','-'],capture_output=True,text=True).stderr
print([l.split(']')[1].strip() for l in r.splitlines() if 'max_volume' in l or 'mean_volume' in l])"

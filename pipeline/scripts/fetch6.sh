#!/bin/bash
# batch 6: download each raw (Drive folder "15. nov"), keep the camera file as the working source, extract 16k mono for ASR
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
mkdir -p raw6; n=25
for id in 1-Aj_3iP3eBkssp1kxvRJzKnFFgiahZTG 1lSbVRE3Xcm6vLlPew0Zn2GQpeHHqSeWi 1xVaXajmW00Hmxv79yYLtvBVrW8gIz0kw 1FOGPI_g8FSdmTJ8gLazEHyWabOqh1dUv 16Q-lApUGLbEvgsWW2478Bdt1GLKMMfNJ 1kbyWuhRZMpPHpB7g23U5ng-S0mfzAlHD 1fUtmIy61LWatH-MFAgWXwyFLAL1UUJJV; do
  n=$((n+1))
  for k in 1 2 3; do python3 -I -c "import gdown,sys; gdown.download(id=sys.argv[1], output=sys.argv[2], quiet=True)" $id raw6/r$n.mp4 && [ -s raw6/r$n.mp4 ] && break; sleep 10; done
  ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt -show_entries format=duration,size -of compact raw6/r$n.mp4 > work/probe$n.txt
  mv raw6/r$n.mp4 work/v$n.mp4
  ffmpeg -v error -y -i work/v$n.mp4 -map 0:a:0 -ac 1 -ar 16000 -c:a pcm_s16le work/a$n.wav
  echo "v$n done $(head -1 work/probe$n.txt) $(grep format work/probe$n.txt)" >> work/fetch6.log
done
echo ALLDONE >> work/fetch6.log

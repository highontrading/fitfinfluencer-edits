#!/bin/bash
# batch 6: download each raw (Drive folders "25 oct" + "27 oct"), keep the camera file as the working source, extract 16k mono for ASR
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
mkdir -p raw7; n=32
for id in 1Zry-c3pwBYv7q1qTQIekYjw1xbefG6s8 1fUkC2MElIzUPANXjRUueGyL2dcq70pPc 1J5SgpyEEvXljkh5JROJhTJViIZeUYvIq 1vu_Sm95Nm2PU73rQKccD8e4Xr-cmNN45 1hsYZdWbBeA020VfmMmCrsJWPY1XYufj6 1sGdl8e470X3IcIUVw9yF9AzllaVG7hef 1LUl8dd00sxDJc87birOggu7MiRovKEsr 1trhL1oLvM-rZj4xtPjBrIQuTXvQSwOd8 10Sxl_n8BlIekzzSXTc1JCvK_EIqaSFZY; do
  n=$((n+1))
  for k in 1 2 3; do python3 -I -c "import gdown,sys; gdown.download(id=sys.argv[1], output=sys.argv[2], quiet=True)" $id raw7/r$n.mp4 && [ -s raw7/r$n.mp4 ] && break; sleep 10; done
  ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt -show_entries format=duration,size -of compact raw7/r$n.mp4 > work/probe$n.txt
  mv raw7/r$n.mp4 work/v$n.mp4
  ffmpeg -v error -y -i work/v$n.mp4 -map 0:a:0 -ac 1 -ar 16000 -c:a pcm_s16le work/a$n.wav
  echo "v$n done $(head -1 work/probe$n.txt) $(grep format work/probe$n.txt)" >> work/fetch7.log
done
echo ALLDONE >> work/fetch7.log

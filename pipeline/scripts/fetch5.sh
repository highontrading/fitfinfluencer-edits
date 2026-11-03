#!/bin/bash
# download each raw, make a working copy (H.264 1080x1920 + original audio stream copied), delete the original
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
n=19
for id in 17C1-ARoNLuhh6kjMlRUx5P1CUY0WWuPf 1yR5or3z1x-nkzp-wcB4_2LOHlTOtcgGk 1e_T2O1l8cxOSrNDgJsNL8ahsOuGF-JMb 16LWhQPhgKRyutfmJgWQyfDVkFY-7mSMZ 10bnZ1CWSalWYkM2qL3uGd0Sc3nq2U0TK 1IH1wimy4JRsawF1VogdUmAR5_tuga9tD; do
  n=$((n+1))
  python3 -I -c "import gdown,sys; gdown.download(id=sys.argv[1], output=sys.argv[2], quiet=True)" $id raw5/r$n.mp4
  ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt -show_entries format=duration,size -of compact raw5/r$n.mp4 > work/probe$n.txt
  ffmpeg -v error -y -i raw5/r$n.mp4 -map 0:v:0 -map 0:a:0 -vf "scale=1080:1920:flags=lanczos,format=yuv420p" -c:v libx264 -preset fast -crf 14 -c:a copy work/v$n.mp4 && rm -f raw5/r$n.mp4
  ffmpeg -v error -y -i work/v$n.mp4 -ac 1 -ar 16000 -c:a pcm_s16le work/a$n.wav
  echo "v$n done $(cat work/probe$n.txt | tr '\n' ' ')" >> work/fetch5.log
done
echo ALLDONE >> work/fetch5.log

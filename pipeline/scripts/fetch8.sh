#!/bin/bash
# batch 8: Drive folder (reel/ + long form/), reels -> v42..v50, long form -> v51
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S
mkdir -p raw8; n=41
for id in 1CTzeTbfc4H9uZ6FBmVRNrIF8tOPpv0ID 1apyyiqNBN3pVO48SOYsw91g2CW6QNLSG 1BN8w9ujFt7_fXxiFDmEwiVi7VdgywTaa 1G3oe_oL1uhNxGmnCGdnuTqSOOwhY5-ZM 1X3du_hAdAr0_XMffbshvecdLJ0egX6Co 1EoxFVmow4dSeqGuz6ZVzQ72dU6YXkOPy 1EZRruHyuQ0CwX84nlGObPuWdlqHQeDYM 16c-cNz1pAB-sv3F-KfWQni_OmRethhCp 1Wo3C5EC-nwvUcjwL1jddcXGIcy845Xom 1yV9sRTMTwc79mRWMVu7rUj2mPkyRSC6Q; do
  n=$((n+1))
  for k in 1 2 3; do python3 -I -c "import gdown,sys; gdown.download(id=sys.argv[1], output=sys.argv[2], quiet=True)" $id raw8/r$n.mp4 && [ -s raw8/r$n.mp4 ] && break; sleep 10; done
  ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt -show_entries format=duration,size -of compact raw8/r$n.mp4 > work/probe$n.txt
  mv raw8/r$n.mp4 work/v$n.mp4
  ffmpeg -v error -y -i work/v$n.mp4 -map 0:a:0 -ac 1 -ar 16000 -c:a pcm_s16le work/a$n.wav < /dev/null
  echo "v$n done $(head -1 work/probe$n.txt) $(grep format work/probe$n.txt)" >> work/fetch8.log
done
echo ALLDONE >> work/fetch8.log

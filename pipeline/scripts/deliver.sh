#!/bin/bash
# deliver.sh in.mp4 out.mp4 -> H.264 under ~95MB
in=$1; out=$2
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$in")
mr=$(python3 -c "print(round(min(7.0, 92*8/$dur - 0.25), 2))")
ffmpeg -v error -y -i "$in" -c:v libx264 -preset slow -crf 19 -maxrate ${mr}M -bufsize 14M -pix_fmt yuv420p -movflags +faststart -c:a copy "$out"
echo "$out $(du -m "$out" | cut -f1)MB maxrate ${mr}M"

#!/bin/bash
# long-form: build spec -> music -> mix (voice untouched, sfx 30%, ducked music) -> streamed render + compose
S=/tmp/claude-0/-home-user-fitfinfluencer-edits/2a167408-7f47-59d7-83a9-be8322dc90b6/scratchpad; cd $S; v=$1
(cd scripts && python3 build_v$v.py ../work) > work/build_v$v.log 2>&1 || { echo "v$v BUILD FAILED"; exit 1; }
[ "$v" = 52 ] && python3 -I scripts/silence_pre.py work >> work/build_v$v.log 2>&1
[ -s work/v${v}_music.wav ] && [ work/v${v}_music.wav -nt work/v${v}_music.json ] || python3 -I scripts/lf_music.py work/v${v}_music.json work/v${v}_music.wav > work/music_v$v.log 2>&1 || { echo "v$v MUSIC FAILED"; exit 1; }
python3 -I scripts/mix_lf.py work v$v audio work/v${v}_music.wav > work/mix_v$v.log 2>&1 || { echo "v$v MIX FAILED"; exit 1; }
rm -rf work/ov_v$v; mkdir -p work/ov_v$v
STREAM=1 node render/render2.js work/v${v}_spec.json work/ov_v$v 2 > work/ov_v$v.log 2>&1 &
STREAM=1 python3 -I scripts/compose2.py work v$v work/ov_v$v work/v${v}_mix.wav out/v${v}_final.mp4 > work/comp_v$v.log 2>&1
wait; rm -rf work/ov_v$v
[ -s out/v${v}_final.mp4 ] && echo "v$v RENDERED $(ffprobe -v error -show_entries format=duration -of csv=p=0 out/v${v}_final.mp4)" || echo "v$v RENDER FAILED"

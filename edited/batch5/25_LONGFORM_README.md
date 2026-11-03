# 25 Epigenome / Biological Age (long-form, 16:9)

- **Format:** 13:01 at 1920x1080, landscape, in 8 chapters.
- **Why it is split:** GitHub limits each file to 100 MB, so the repo copy is in 6 parts, cut at chapter starts. The full single file was sent directly in the chat.

| Part | Starts at | Contents |
|---|---|---|
| part1 | 0:00 | Hook, Chapter 1 YOUR DNA |
| part2 | 2:21 | Chapter 2 THE EPIGENOME, Chapter 3 WHY WE AGE |
| part3 | 5:08 | Chapter 4 EVERY ORGAN HAS ITS OWN AGE, Chapter 5 THE TWIN STUDY |
| part4 | 7:30 | Chapter 6 ZOMBIE CELLS |
| part5 | 9:12 | Chapter 7 WHAT I DID |
| part6 | 11:20 | Chapter 8 THE FUTURE, CTA |

To rejoin the parts losslessly:

```
printf "file '%s'\n" 25_*_part*.mp4 > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy 25_full.mp4
```

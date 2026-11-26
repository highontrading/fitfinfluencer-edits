# 51 — Billionaire Brain (Neuroscience) — Long form, Hindi

**Length:** 27:39 total = trailer 0:53 + main video 26:45
**Format:** 1920x1080, 29.97 fps, H.264 + AAC 192k

GitHub caps files at 100 MB, so the full video (~995 MB) is stored here as 15 parts, cut at chapter starts.
The full single file was also delivered directly in the session.

## Parts
| Part | Starts at | Contents | Size |
|---|---|---|---|
| 01 | 0:00 | Trailer + cold open (1/2) | 50.8 MB |
| 02 | 1:25 | Trailer + cold open (2/2) | 51.2 MB |
| 03 | 2:50 | Part 1: Your brain's storyteller (DMN) (1/2) | 51.9 MB |
| 04 | 4:17 | Part 1: Your brain's storyteller (DMN) (2/2) | 52.2 MB |
| 05 | 5:43 | Part 2: Design your beliefs (1/2) | 62.2 MB |
| 06 | 7:27 | Part 2: Design your beliefs (2/2) | 62.2 MB |
| 07 | 9:11 | Part 3: Goals need a plan | 63.6 MB |
| 08 | 10:57 | Part 4: The bad-habit loop (1/2) | 95.7 MB |
| 09 | 13:36 | Part 4: The bad-habit loop (2/2) | 95.8 MB |
| 10 | 16:16 | Part 5: Boredom = ideas | 89.2 MB |
| 11 | 18:45 | Part 6: The 5 AM club myth (1/2) | 63.3 MB |
| 12 | 20:30 | Part 6: The 5 AM club myth (2/2) | 63.4 MB |
| 13 | 22:16 | Part 7: Burnout + the 3M framework (1/2) | 60.3 MB |
| 14 | 23:56 | Part 7: Burnout + the 3M framework (2/2) | 60.4 MB |
| 15 | 25:37 | Recap + close | 72.5 MB |

## Join the parts back into one file
All parts share the same encode, so they join losslessly:
```
cd parts
for f in 51_*_part*.mp4; do echo "file '$f'"; done > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy 51_Billionaire_Brain_FULL.mp4
```

## What was done (per the approved plan, 51_LONGFORM_PLAN.md)
- Best take of every line, script order kept; repeats, false starts and long pauses removed. Voice: only the approved 1.1x speed-up (pitch and formants preserved).
- 8 chapters with chapter cards: Storyteller brain (DMN), Design your beliefs, Goals need a plan, Bad-habit loop, Boredom = ideas, 5 AM club myth, Burnout + 3M framework, Recap.
- Animated science diagrams: default mode network hubs, neurons that fire together, habit loop, CEN/DMN seesaw, chronotype energy curves, stress curve, plus checklists and stock B-roll (credits in ../STOCK_CREDITS.md).
- Hinglish captions exactly as spoken; English on-screen text; no emojis.
- Background music (as the brief asked): an original score per section, by mood, ducked under the voice (about 18 dB below it while speaking). SFX at 30%.
- Trailer (0:54) at the start: question cards and the strongest moments, then the title card.
- Nobel point: kept your final take; on-screen text reads "2017 NOBEL PRIZE: HOW THE BODY CLOCK WORKS".

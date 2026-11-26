# Join trailer (v52) + main (v51) into one file and split it into <~90 MB parts at chapter starts for the repo.
import json, subprocess, os, sys
W = 'work'; OUT = sys.argv[1]; NAME = '51_Billionaire_Brain_Neuroscience_LongForm_Hindi'
tl = json.load(open(f'{W}/v51_tl.json')); SS = {}
for sh in tl['shots']: SS.setdefault(sh['c'], sh['out0'])
td = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', 'out/v52_final.mp4'], capture_output=True, text=True).stdout)
md = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', 'out/v51_final.mp4'], capture_output=True, text=True).stdout)
chap = [(0, 'Trailer + cold open'), (SS[51], 'Part 1: Your brain\'s storyteller (DMN)'), (SS[145], 'Part 2: Design your beliefs'), (SS[240], 'Part 3: Goals need a plan'),
        (SS[306], 'Part 4: The bad-habit loop'), (SS[504], 'Part 5: Boredom = ideas'), (SS[574], 'Part 6: The 5 AM club myth'), (SS[663], 'Part 7: Burnout + the 3M framework'),
        (SS[757], 'Recap + close')]
starts = [(0.0, chap[0][1])] + [(td + t, n) for t, n in chap[1:]]
MAXLEN = 150.0   # ~4.6 Mbps -> ~86 MB per 150 s
cuts = []
for (a, n), (b, _) in zip(starts, starts[1:] + [(td + md, None)]):
    k = max(1, int((b - a) // MAXLEN) + (1 if (b - a) % MAXLEN > 20 else 0)); step = (b - a) / k
    for i in range(k): cuts.append((round(a + i * step, 3), n + (f' ({i + 1}/{k})' if k > 1 else '')))
times = [c[0] for c in cuts[1:]]
full = f'{OUT}/{NAME}_FULL.mp4'
kf = ','.join(f'{t:.3f}' for t in times)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'out/v52_final.mp4', '-i', 'out/v51_final.mp4', '-filter_complex', '[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1[v][a]',
                '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'slow', '-crf', '20', '-maxrate', '4.6M', '-bufsize', '9M', '-pix_fmt', 'yuv420p',
                '-force_key_frames', kf, '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', full], check=True)
pdir = f'{OUT}/parts'; os.makedirs(pdir, exist_ok=True)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', full, '-c', 'copy', '-map', '0', '-f', 'segment', '-segment_times', kf, '-reset_timestamps', '1',
                f'{pdir}/{NAME}_part%02d.mp4'], check=True)
info = []
for i, (t, n) in enumerate(cuts):
    p = f'{pdir}/{NAME}_part{i:02d}.mp4'; sz = os.path.getsize(p) / 1e6
    info.append({'part': i + 1, 'file': os.path.basename(p).replace(f'part{i:02d}', f'part{i+1:02d}'), 'start': t, 'contents': n, 'mb': round(sz, 1)})
    os.rename(p, f'{pdir}/{NAME}_part{i+1:02d}.mp4')
json.dump({'trailer': td, 'main': md, 'total': td + md, 'parts': info}, open(f'{OUT}/parts.json', 'w'), indent=1)
print(json.dumps(info, indent=1)); print('full', round(os.path.getsize(full) / 1e6), 'MB', round((td + md) / 60, 2), 'min')

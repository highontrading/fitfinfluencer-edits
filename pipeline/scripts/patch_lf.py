# Encode re-composited frame ranges (work/ovpatch/c_NNNNN.jpg) into short patch clips out/v51_patchK.mp4.
import json, subprocess, os, shutil
G = json.load(open('work/patch_frames.json'))
for k, (a, b) in enumerate(G):
    d = f'work/ovpatch/seq{k}'; os.makedirs(d, exist_ok=True)
    for i, f in enumerate(range(a, b)): shutil.move(f'work/ovpatch/c_{f:05d}.jpg', f'{d}/{i:05d}.jpg')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', '30000/1001', '-i', f'{d}/%05d.jpg', '-c:v', 'libx264', '-crf', '12', '-preset', 'medium',
                    '-pix_fmt', 'yuv420p', f'out/v51_patch{k}.mp4'], check=True)
    print('patch', k, a, b)

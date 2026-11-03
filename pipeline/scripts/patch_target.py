# Re-draw a flow chart's gold "target" node (its accent word was gold-on-gold) onto an already-encoded video.
import sys, json, subprocess, glob, os, numpy as np, cv2
work, name, src, dst, maxrate = sys.argv[1:6]
spec = json.load(open(f'{work}/{name}_spec.json'))
FR = spec['fps'][0] / spec['fps'][1]
ev = next(e for e in spec['events'] if e['type'] == 'flow' and any(n.get('target') and '*' in n['text'] for n in e['nodes']))
tn = next(n for n in ev['nodes'] if n.get('target'))
sp = dict(spec, events=[ev], captions=[], capMoves=[]); sp.pop('brand', None)
json.dump(sp, open(f'{work}/{name}_patchspec.json', 'w'))
f0 = int((tn['t'] - 0.1) * FR); f1 = min(int((ev['t1'] + 0.7) * FR), spec['frames'] - 1)
od = f'{work}/patch_{name}'; subprocess.run(['rm', '-rf', od]); os.makedirs(od)
frs = list(range(f0, f1 + 1))
subprocess.run(['node', 'render/stills_f.js', f'{work}/{name}_patchspec.json', od, ','.join(map(str, frs))], check=True)
# bbox of the target node: largest gold component in a settled frame
fm = int(min(tn['t'] + 0.6, (tn['t'] + ev['t1']) / 2 + 0.1) * FR)
im = cv2.imread(f'{od}/{fm:05d}.png', cv2.IMREAD_UNCHANGED)
b, g, r, a = cv2.split(im)
mask = ((a > 240) & (np.arange(a.shape[0])[:, None] > 60) & (r > 200) & (g > 120) & (b < 120)).astype(np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
n, lab, st, _ = cv2.connectedComponentsWithStats(mask)
i = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
x, y, w, h = st[i, :4]; x, y, w, h = int(x) - 2, int(y) - 2, int(w) + 4, int(h) + 4
x -= x % 2; y -= y % 2; w += w % 2; h += h % 2
for f in frs:
    pp = f'{od}/{f:05d}.png'; q = cv2.imread(pp, cv2.IMREAD_UNCHANGED)
    al = ((q[:, :, 3] >= 250).astype(np.uint8) * 255); al = cv2.erode(al, np.ones((3, 3), np.uint8))
    q[:, :, 3] = al; cv2.imwrite(pp, q)
print(name, 'node', tn['text'], 'bbox', x, y, w, h, 'frames', f0, f1)
fc = f'[1:v]crop={w}:{h}:{x}:{y},setpts=PTS-STARTPTS+{f0}/({FR})/TB[p];[0:v][p]overlay={x}:{y}:eof_action=pass:format=auto[v]'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-framerate', f'{spec["fps"][0]}/{spec["fps"][1]}', '-start_number', str(f0), '-i', f'{od}/%05d.png',
                '-filter_complex', fc, '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'slow', '-crf', '19', '-maxrate', maxrate, '-bufsize', '14M',
                '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-c:a', 'copy', dst], check=True)
cv2.imwrite(f'{work}/patchchk_{name}.jpg', cv2.imread(f'{od}/{fm:05d}.png')[max(0, y - 60):y + h + 60, max(0, x - 60):x + w + 60])

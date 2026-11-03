# Face track for auto-reframe: per output frame (cx, cy, h) in 1080x1920 coords, smoothed within each shot.
import sys, json, subprocess, numpy as np, cv2
work, name = sys.argv[1], sys.argv[2]
tl = json.load(open(f'{work}/{name}_tl.json'))
W, H, S = 360, 640, 3.0
det = cv2.FaceDetectorYN.create('/root/face_detection_yunet_2023mar.onnx', '', (W, H), 0.6, 0.3, 5)
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', f'{work}/{name}_cut.mp4', '-vf', f'scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)
raw = []
f = 0
while True:
    buf = p.stdout.read(W * H * 3)
    if len(buf) < W * H * 3: break
    if f % 2 == 0:
        img = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        _, faces = det.detect(img)
        if faces is not None and len(faces):
            fc = max(faces, key=lambda r: r[2] * r[3])
            x, y, w, h = fc[:4]
            raw.append((f, (x + w / 2) * S, (y + h / 2) * S, h * S))
        else:
            raw.append((f, np.nan, np.nan, np.nan))
    f += 1
N = tl['frames']
arr = np.full((N, 3), np.nan)
for fr, cx, cy, hh in raw:
    if fr < N: arr[fr] = (cx, cy, hh)
# per-shot: interpolate gaps, then heavy smoothing (no smoothing across cuts)
out = np.zeros((N, 3))
fi = 0
med = np.nanmedian(arr, axis=0)
for sh in tl['shots']:
    n = int(round(sh['out1'] / (1001 / 30000))) - int(round(sh['out0'] / (1001 / 30000))); n = max(0, min(n, N - fi))
    if n == 0: continue
    seg = arr[fi:fi + n].copy()
    for c in range(3):
        v = seg[:, c]; ok = ~np.isnan(v)
        if ok.sum() == 0: v[:] = med[c]
        else: v[:] = np.interp(np.arange(n), np.flatnonzero(ok), v[ok])
        # gaussian smooth, sigma ~0.4s
        sig = 12; k = np.exp(-0.5 * (np.arange(-36, 37) / sig) ** 2); k /= k.sum()
        pad = np.pad(v, 36, mode='edge'); seg[:, c] = np.convolve(pad, k, 'same')[36:-36]
    out[fi:fi + n] = seg; fi += n
json.dump({'face': out.round(1).tolist(), 'median': med.tolist()}, open(f'{work}/{name}_face.json', 'w'))
print(name, 'face median', med.round(1), 'detected', int((~np.isnan(arr[:, 0])).sum()), 'of', N // 2)

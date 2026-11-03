# Compositor v2 (EDITING_RULES): text behind the speaker via person cut-out, film grain, photo B-roll.
# Final compositor: auto-reframe + jump-cut zooms + speaker-card mode + overlay blend -> H.264/AAC master.
import sys, json, subprocess, numpy as np, cv2, os
work, name, ovdir, audio, outp = sys.argv[1:6]
preview = len(sys.argv) > 6 and sys.argv[6] == 'preview'
only = set(int(x) for x in os.environ.get('FRAMES', '').split(',') if x)
tl = json.load(open(f'{work}/{name}_tl.json'))
spec = json.load(open(f'{work}/{name}_spec.json'))
face = np.array(json.load(open(f'{work}/{name}_face.json'))['face'])
cam = spec['camera']
FPS = 30000 / 1001
N = spec['frames']
OW, OH = spec.get('size', [1080, 1920])
SW, SH = OW, OH

def clamp(x, a, b): return max(a, min(b, x))
def ease(t): t = clamp(t, 0, 1); return 4*t*t*t if t < .5 else 1 - (-2*t + 2)**3 / 2
def outexpo(t): t = clamp(t, 0, 1); return 1 if t >= 1 else 1 - 2 ** (-10 * t)

shot_of = np.zeros(N, int); shot_t0 = np.zeros(N); shot_d = np.zeros(N)
fi = 0
for k, sh in enumerate(tl['shots']):
    n = int(round(sh['out1'] / (1001 / 30000))) - int(round(sh['out0'] / (1001 / 30000)))
    shot_of[fi:fi+n] = k; shot_t0[fi:fi+n] = sh['out0']; shot_d[fi:fi+n] = sh['out1'] - sh['out0']; fi += n

zooms = cam.get('zooms', [1.0, 1.18])
# zoom choice per shot: alternate, but allow explicit per-shot overrides computed by the spec builder
shot_zoom = cam.get('shot_zoom') or [zooms[k % len(zooms)] for k in range(len(tl['shots']))]

zseq = cam.get('zseq') or []
zt = np.array([z['t'] for z in zseq])

def range_mix(t, key):
    """0..1 weight of camera ranges of a given mode at time t with eased transitions."""
    best = (0, None)
    for r in cam.get('ranges', []):
        if r.get('mode') != key: continue
        tr = r.get('tr', 0.35)
        if r['t0'] - tr <= t <= r['t1'] + tr:
            w = min(ease((t - (r['t0'] - tr)) / tr), ease(((r['t1'] + tr) - t) / tr))
            if w > best[0]: best = (w, r)
    return best

def punch(t):
    z = 1.0
    for p in cam.get('punches', []):
        d = t - p['t']
        if d < 0: continue
        hold = p.get('hold', 0.8)
        if d < hold: z *= 1 + p['amt'] * outexpo(d / 0.16)
        elif d < hold + 0.35: z *= 1 + p['amt'] * (1 - ease((d - hold) / 0.35))
    return z

def shake(t):
    dx = dy = 0
    for s in cam.get('shakes', []):
        d = t - s['t']
        if 0 <= d < 0.35:
            a = s.get('amt', 14) * (1 - d / 0.35)
            dx += a * np.sin(d * 90); dy += a * np.cos(d * 70)
    return dx, dy

def window(fx, fy, scale, rw, rh, faceY):
    """source window (x0,y0,w,h) that maps to an output rect of rw x rh at `scale` out-px per src-px."""
    w, h = rw / scale, rh / scale
    w = min(w, SW); h = min(h, SH)
    cx = 0.75 * fx + 0.25 * SW / 2
    x0 = clamp(cx - w / 2, 0, SW - w)
    y0 = clamp(fy - faceY * h, 0, SH - h)
    return x0, y0, w, h

def warp(src, win, rw, rh):
    x0, y0, w, h = win
    sx, sy = rw / w, rh / h
    M = np.float32([[sx, 0, -x0 * sx], [0, sy, -y0 * sy]])
    return cv2.warpAffine(src, M, (int(rw), int(rh)), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)

mask_cache = {}
def rmask(w, h, r):
    key = (w, h, r)
    if key not in mask_cache:
        m = np.zeros((h, w), np.uint8)
        cv2.rectangle(m, (r, 0), (w - r, h), 255, -1); cv2.rectangle(m, (0, r), (w, h - r), 255, -1)
        for cx, cy in ((r, r), (w - r - 1, r), (r, h - r - 1), (w - r - 1, h - r - 1)):
            cv2.circle(m, (cx, cy), r, 255, -1, cv2.LINE_AA)
        if len(mask_cache) > 64: mask_cache.clear()
        mask_cache[key] = m
    return mask_cache[key]

dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', f'{work}/{name}_cut.mp4', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
enc_args = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{OW}x{OH}', '-r', '30000/1001', '-i', '-',
            '-i', audio, '-map', '0:v', '-map', '1:a',
            '-c:v', 'libx264', '-preset', 'veryfast' if preview else 'slow', '-crf', '23' if preview else '17', '-profile:v', 'high', '-pix_fmt', 'yuv420p',
            '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709',
            '-c:a', 'aac', '-b:a', '256k', '-ar', '48000', '-movflags', '+faststart', '-shortest', outp]
enc = None if only else subprocess.Popen(enc_args, stdin=subprocess.PIPE)
dfy = cam.get('faceY', 0.36)
card_default = cam.get('card', {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.25, 'faceY': 0.42})

def render_cam(src, fx, fy, z, t, br=None):
    """A-roll (br=None) or b-roll frame through the camera: full frame or speaker-card layout."""
    if br is not None:
        p = clamp((t - br['t0']) / max(br['t1'] - br['t0'], 0.1), 0, 1)
        kb = br.get('kb', 0.07)
        z = 1.0 + kb * p; fx, fy = SW / 2, SH * br.get('y', 0.5)
        fdy = 0.5
    else:
        fdy = dfy
    full = warp(src, window(fx, fy, z, OW, OH, fdy), OW, OH)
    dx, dy = shake(t)
    if dx or dy:
        full = cv2.warpAffine(full, np.float32([[1, 0, dx], [0, 1, dy]]), (OW, OH), borderMode=cv2.BORDER_REFLECT)
    m, rc = range_mix(t, 'card')
    if m > 0.001:
        cd = dict(card_default); cd.update(rc.get('card', {}))
        X, Y, Wc, Hc = cd['rect']
        rx, ry = X * m, Y * m
        rw, rh = OW + (Wc - OW) * m, OH + (Hc - OH) * m
        if br is not None:
            sc = z + (max(Wc / SW, Hc / SH) * z - z) * m; fyy = 0.5
        else:
            sc = z + (cd['scale'] - z) * m
            fyy = dfy + (cd['faceY'] - dfy) * m
        content = warp(src, window(fx, fy, sc, rw, rh, fyy), rw, rh)
        small = cv2.resize(full, (OW // 8, OH // 8), interpolation=cv2.INTER_AREA)
        small = cv2.GaussianBlur(small, (0, 0), 6)
        bg = cv2.resize(small, (OW, OH), interpolation=cv2.INTER_LINEAR).astype(np.float32)
        bg *= 1 - 0.62 * m
        # soft drop shadow
        rr = int(cd['r'] * m + 0.5)
        iw, ih = int(rw), int(rh); ix, iy = int(rx), int(ry)
        sh = np.zeros((OH // 4, OW // 4), np.float32)
        cv2.rectangle(sh, ((ix) // 4, (iy + 24) // 4), ((ix + iw) // 4, (iy + ih + 24) // 4), 1.0, -1)
        sh = cv2.resize(cv2.GaussianBlur(sh, (0, 0), 10), (OW, OH))
        bg *= (1 - 0.55 * m * sh)[..., None]
        out = bg.astype(np.uint8)
        mk = rmask(iw, ih, max(rr, 1)).astype(np.float32)[..., None] / 255
        roi = out[iy:iy + ih, ix:ix + iw].astype(np.float32)
        cont = content[:ih, :iw].astype(np.float32)
        out[iy:iy + ih, ix:ix + iw] = (roi * (1 - mk) + cont * mk).astype(np.uint8)
        if m > 0.3:
            outer = rmask(iw, ih, max(rr, 1)); inner = cv2.erode(outer, np.ones((5, 5), np.uint8))
            ring = ((outer.astype(np.int16) - inner) > 60)
            al = 0.55 * clamp((m - 0.3) / 0.7, 0, 1)
            sub = out[iy:iy + ih, ix:ix + iw]
            sub[ring] = (sub[ring] * (1 - al) + np.array([255, 205, 110]) * al).clip(0, 255).astype(np.uint8)
    else:
        out = full
    return out

brolls = spec.get('broll', [])
bdec = {}
def broll_cmd(br, extra_ss=0.0):
    if br.get('fit') == 'card' and SH > SW:   # wide crop matching the speaker-card window, centred in a portrait canvas
        ch = 940
        geo = (f"scale={SW}:{ch}:force_original_aspect_ratio=increase:flags=lanczos,crop={SW}:{ch}:(iw-ow)*{br.get('x', 0.5)}:(ih-oh)*{br.get('cy', 0.5)},"
               f"pad={SW}:{SH}:0:{(SH - ch) // 2}")
    else:
        geo = f"scale={SW}:{SH}:force_original_aspect_ratio=increase:flags=lanczos,crop={SW}:{SH}:(iw-ow)*{br.get('x', 0.5)}:(ih-oh)*{br.get('cy', 0.5)}"
    vf = f"{geo},fps=30000/1001,eq=contrast=1.05:saturation={br.get('sat', 1.05)}:gamma=0.98:brightness={br.get('bright', 0)},unsharp=5:5:0.3,format=rgb24"
    if br['file'].lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):   # still photo: hold it, Ken Burns comes from the camera
        return ['ffmpeg', '-v', 'error', '-loop', '1', '-i', br['file'], '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    return ['ffmpeg', '-v', 'error', '-ss', f"{br.get('off', 0.5) + extra_ss:.3f}", '-i', br['file'], '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
def broll_frame(bi, br, t):
    if only:
        r = subprocess.run(broll_cmd(br, t - br['t0']) [:-1] + ['-frames:v', '1', '-'], capture_output=True).stdout
        return np.frombuffer(r[:SW*SH*3], np.uint8).reshape(SH, SW, 3) if len(r) >= SW*SH*3 else None
    d = bdec.get(bi)
    if d is None:
        d = bdec[bi] = {'p': subprocess.Popen(broll_cmd(br), stdout=subprocess.PIPE), 'last': None}
    buf = d['p'].stdout.read(SW * SH * 3)
    if len(buf) == SW * SH * 3: d['last'] = np.frombuffer(buf, np.uint8).reshape(SH, SW, 3)
    return d['last']

SEG = None
import time
STREAM = bool(os.environ.get('STREAM'))
VIG = None
if spec.get('vigInCompose'):   # same look as the overlay's CSS vignette, applied here so overlay frames stay small
    yy, xx = np.mgrid[0:OH, 0:OW].astype(np.float32)
    rr = np.sqrt(((xx - 0.5 * OW) / (0.5 * OW)) ** 2 + ((yy - 0.45 * OH) / (0.55 * OH)) ** 2) / np.sqrt(2)
    VIG = (1 - 0.38 * np.clip((rr - 0.55) / 0.45, 0, 1))[..., None]
GR = cam.get('grain', 0)
rng = np.random.default_rng(7)
grain = [rng.normal(0, GR, (OH // 2, OW // 2)).astype(np.float32) for _ in range(6)] if GR else None
last_buf = None
for f in range(N):
    buf = dec.stdout.read(SW * SH * 3)
    if len(buf) < SW * SH * 3:
        if last_buf is None: break
        buf = last_buf          # end hold: freeze the final frame
    last_buf = buf
    if only and f not in only:
        if f > max(only): break
        continue
    src = np.frombuffer(buf, np.uint8).reshape(SH, SW, 3)
    t = f / FPS
    fx, fy, fh = face[min(f, len(face) - 1)]
    # base zoom per shot + gentle push within shot + punches
    if zseq:
        j = max(0, np.searchsorted(zt, t, side='right') - 1)
        z = zseq[j]['z']; seg0 = zt[j]; seg1 = zt[j + 1] if j + 1 < len(zt) else tl['dur']
        z *= 1 + cam.get('drift', 0.03) * clamp((t - seg0) / max(seg1 - seg0, 0.1), 0, 1)
    else:
        z = shot_zoom[shot_of[f]]
        z *= 1 + cam.get('drift', 0.03) * clamp((t - shot_t0[f]) / max(shot_d[f], 0.1), 0, 1)
    z *= punch(t)
    wz, rz = range_mix(t, 'zoom')
    if rz: z = z * (1 - wz) + rz['z'] * wz
    out = render_cam(src, fx, fy, z, t)
    # stock b-roll cut-ins (crossfaded)
    for bi, br in enumerate(brolls):
        xf = br.get('xf', 0.16)
        if br['t0'] - 1e-6 <= t < br['t1']:
            al = min(clamp((t - br['t0']) / xf, 0, 1) if br.get('fadein', True) else 1, clamp((br['t1'] - t) / xf, 0, 1) if br.get('fadeout', True) else 1)
            bf = broll_frame(bi, br, t)
            if bf is not None:
                ob = render_cam(bf, 0, 0, 1.0, t, br)
                out = ob if al >= 1 else (out.astype(np.float32) * (1 - al) + ob.astype(np.float32) * al).astype(np.uint8)
    # text behind the speaker: behind-layer under a person cut-out
    op = os.path.join(ovdir, f'{f:05d}.png')
    if STREAM:
        while not os.path.exists(op) and not os.path.exists(os.path.join(ovdir, '_done')): time.sleep(0.05)
        time.sleep(0.01)
    bp = os.path.join(ovdir, f'b_{f:05d}.png')
    if os.path.exists(bp):
        bov = cv2.imread(bp, cv2.IMREAD_UNCHANGED)
        a = bov[..., 3:4].astype(np.float32) / 255 * (1.0 - range_mix(t, 'card')[0])   # behind-text fades out as the speaker card comes in
        blended = out.astype(np.float32) * (1 - a) + bov[..., 2::-1].astype(np.float32) * a
        in_broll = any(br['t0'] - 1e-6 <= t < br['t1'] for br in brolls)
        if not in_broll and range_mix(t, 'card')[0] < 0.001:
            if SEG is None:
                sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from personseg import PersonSeg; SEG = PersonSeg()
            pm = (SEG.mask(src, f) * 255).astype(np.uint8)
            pmo = render_cam(cv2.merge([pm, pm, pm]), fx, fy, z, t)[..., :1].astype(np.float32) / 255
            out = (blended * (1 - pmo) + out.astype(np.float32) * pmo).astype(np.uint8)
        else:
            out = blended.astype(np.uint8)
    if grain is not None:
        g = cv2.resize(grain[f % len(grain)], (OW, OH), interpolation=cv2.INTER_LINEAR)
        out = np.clip(out.astype(np.float32) + g[..., None], 0, 255).astype(np.uint8)
    if VIG is not None:
        out = (out.astype(np.float32) * VIG).astype(np.uint8)
    # overlay
    op = os.path.join(ovdir, f'{f:05d}.png')

    ov = cv2.imread(op, cv2.IMREAD_UNCHANGED)
    if STREAM:
        for q in (op, bp):
            try: os.remove(q)
            except OSError: pass
        if f % 30 == 0: open(os.path.join(ovdir, '_pos'), 'w').write(str(f))
    if ov is not None:
        a = ov[..., 3:4].astype(np.uint16)
        rgb = ov[..., 2::-1].astype(np.uint16)
        out = ((out.astype(np.uint16) * (255 - a) + rgb * a) // 255).astype(np.uint8)
    if only:
        cv2.imwrite(f'{outp}_{f:05d}.jpg', cv2.cvtColor(out, cv2.COLOR_RGB2BGR), [cv2.IMWRITE_JPEG_QUALITY, 88]); continue
    enc.stdin.write(np.ascontiguousarray(out).tobytes())
    if f % 300 == 0: print(name, f, '/', N, flush=True)
if enc: enc.stdin.close(); enc.wait()
dec.kill()
print('wrote', outp)

# Original, procedurally generated score for the long-form (royalty-free by construction: no samples, no external music).
# python3 -I scripts/lf_music.py sections.json out.wav
# sections.json: {"dur": seconds, "sections": [{"t0":..,"t1":..,"mood":".."}], "drops": [t,...], "hits": [t,...]}
import sys, json, numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

SR = 48000
rng = np.random.default_rng(11)
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def mtof(m): return 440.0 * 2 ** ((m - 69) / 12)
def adsr(n, a, d, s, r):
    e = np.ones(n) * s; A, D, R = int(a * SR), int(d * SR), int(r * SR)
    A = min(A, n); e[:A] = np.linspace(0, 1, A, endpoint=False)
    D2 = min(D, max(0, n - A)); e[A:A + D2] = np.linspace(1, s, D2)
    R = min(R, n); e[n - R:] *= np.linspace(1, 0, R)
    return e
def osc_saw(f, n, det=0.0):
    t = np.arange(n) / SR; out = np.zeros(n)
    for d in (-det, 0, det):
        ph = (t * f * (1 + d)) % 1.0; out += 2 * ph - 1
    return out / 3
def piano(f, d):
    n = int(d * SR); t = np.arange(n) / SR
    x = sum(np.sin(2 * np.pi * f * k * t) * (0.6 ** (k - 1)) * np.exp(-t * (1.6 + 0.9 * k)) for k in range(1, 7))
    att = np.minimum(1, t / 0.004)
    return x * att * 0.5
def pluck(f, d):   # Karplus-Strong
    n = int(d * SR); P = max(2, int(SR / f)); buf = rng.uniform(-1, 1, P); out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % P]; buf[i % P] = 0.5 * (buf[i % P] + buf[(i + 1) % P]) * 0.994
    return lp(out, 3500) * 0.6
def pad(chord, d, cutoff=1400, det=0.004, a=1.2, r=1.5):
    n = int(d * SR); x = sum(osc_saw(mtof(m), n, det) for m in chord) / len(chord)
    return lp(x, cutoff, 2) * adsr(n, a, 0.5, 0.85, r)
def strings(chord, d, cutoff=2200):
    n = int(d * SR); t = np.arange(n) / SR
    x = sum(osc_saw(mtof(m) * (1 + 0.002 * np.sin(2 * np.pi * 5.2 * t)), n, 0.006) for m in chord) / len(chord)
    return lp(x, cutoff, 2) * adsr(n, 0.9, 0.3, 0.9, 1.2)
def sub(f, d, decay=6.0):
    n = int(d * SR); t = np.arange(n) / SR
    return np.sin(2 * np.pi * f * t) * np.exp(-t * decay) * np.minimum(1, t / 0.01)
def kick(d=0.5):
    n = int(d * SR); t = np.arange(n) / SR; f = 50 + 90 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)
def hat(d=0.08):
    n = int(d * SR); return hp(rng.standard_normal(n), 7000) * np.exp(-np.arange(n) / SR * 60) * 0.25
def clap(d=0.25):
    n = int(d * SR); return lp(hp(rng.standard_normal(n), 900), 4000) * np.exp(-np.arange(n) / SR * 22) * 0.35
def put(buf, x, t, g=1.0, pan=0.0):
    i = int(t * SR)
    if i >= buf.shape[1] or i < 0: return
    x = x[:buf.shape[1] - i] * g
    buf[0, i:i + len(x)] += x * (1 - max(0, pan)); buf[1, i:i + len(x)] += x * (1 + min(0, pan))

# ---- moods: key progression (MIDI chords), tempo, and which layers play
P_MIN = [[50, 53, 57], [46, 50, 53], [53, 57, 60], [48, 52, 55]]        # Dm Bb F C
P_TEACH = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]      # Am F C G
P_UP = [[48, 52, 55], [55, 59, 62], [57, 60, 64], [53, 57, 60]]         # C G Am F
P_FOCUS = [[52, 55, 59], [48, 52, 55], [55, 59, 62], [50, 54, 57]]      # Em C G D
P_DARK = [[48, 51, 55], [44, 48, 51], [46, 50, 53], [43, 47, 50]]       # Cm Ab Bb G
P_HOPE = [[48, 52, 55], [53, 57, 60], [57, 60, 64], [55, 59, 62]]       # C F Am G
P_LIGHT = [[55, 59, 62], [52, 55, 59], [48, 52, 55], [50, 54, 57]]      # G Em C D
P_ENER = [[57, 60, 64], [55, 59, 62], [53, 57, 60], [52, 56, 59]]       # Am G F E
P_CALM = [[50, 54, 57], [55, 59, 62], [47, 50, 54], [52, 55, 59]]       # D G Bm Em
MOODS = {
    'trailer':   dict(prog=P_MIN, bpm=96, layers=['strings', 'pulse', 'build']),
    'curiosity': dict(prog=P_MIN, bpm=84, layers=['strings', 'pulse']),
    'teaching':  dict(prog=P_TEACH, bpm=80, layers=['piano_arp', 'softpad']),
    'uplift':    dict(prog=P_UP, bpm=88, layers=['piano_arp', 'pad', 'pulse_late']),
    'focus':     dict(prog=P_FOCUS, bpm=100, layers=['pluck_arp', 'beat_min', 'softpad']),
    'dark':      dict(prog=P_DARK, bpm=64, layers=['drone', 'heartbeat']),
    'hope':      dict(prog=P_HOPE, bpm=80, layers=['pad', 'piano_arp']),
    'light':     dict(prog=P_LIGHT, bpm=108, layers=['pizz', 'softpad']),
    'energy':    dict(prog=P_ENER, bpm=112, layers=['beat', 'bass', 'pluck_arp']),
    'calm':      dict(prog=P_CALM, bpm=70, layers=['softpad', 'piano_sparse']),
    'inspire':   dict(prog=P_UP, bpm=90, layers=['strings', 'piano_arp', 'pulse', 'build']),
}

def render_section(mood, d):
    M = MOODS[mood]; beat = 60 / M['bpm']; bar = 4 * beat; prog = M['prog']; n = int(d * SR) + SR * 3
    buf = np.zeros((2, n)); nb = int(np.ceil(d / bar)) + 1
    for b in range(nb):
        t = b * bar; ch = prog[b % 4]; prog_frac = b / max(1, nb - 1)
        for L in M['layers']:
            if L == 'strings': put(buf, strings([m + 12 for m in ch] + [ch[0]], bar + 1.0), t, 0.16)
            if L == 'pad': put(buf, pad([m + 12 for m in ch], bar + 1.2), t, 0.13)
            if L == 'softpad': put(buf, pad([m + 12 for m in ch], bar + 1.5, cutoff=900, a=1.6), t, 0.10)
            if L in ('pulse', 'pulse_late') and (L == 'pulse' or prog_frac > 0.45):
                for k in range(8): put(buf, sub(mtof(ch[0] - 12), beat / 2, 9), t + k * beat / 2, 0.22)
            if L == 'build':
                g = 0.04 + 0.12 * prog_frac
                for k in range(16): put(buf, hat(), t + k * beat / 4, g, 0.3 * (1 if k % 2 else -1))
            if L == 'piano_arp':
                pat = [0, 1, 2, 1, 0, 2, 1, 2]
                for k, p_ in enumerate(pat): put(buf, piano(mtof(ch[p_] + 12), beat * 1.8), t + k * beat / 2, 0.11, 0.25 * (k % 2 * 2 - 1))
            if L == 'piano_sparse':
                put(buf, piano(mtof(ch[0] + 12), bar), t, 0.10); put(buf, piano(mtof(ch[2] + 24), bar * 0.75), t + 2 * beat, 0.07, 0.3)
            if L == 'pluck_arp':
                pat = [0, 2, 1, 2, 0, 2, 1, 2]
                for k, p_ in enumerate(pat): put(buf, pluck(mtof(ch[p_] + 12), beat * 0.9), t + k * beat / 2, 0.12, 0.3 * (k % 2 * 2 - 1))
            if L == 'pizz':
                for k, p_ in enumerate([0, 1, 2, 1]): put(buf, pluck(mtof(ch[p_] + 12), beat * 0.8), t + k * beat, 0.16, 0.4 * (k % 2 * 2 - 1))
            if L == 'beat_min':
                for k in range(4): put(buf, kick(), t + k * beat, 0.18)
                for k in range(8): put(buf, hat(), t + k * beat / 2 + beat / 4, 0.10)
            if L == 'beat':
                for k in range(4): put(buf, kick(), t + k * beat, 0.24)
                for k in (1, 3): put(buf, clap(), t + k * beat, 0.16)
                for k in range(8): put(buf, hat(), t + k * beat / 2 + beat / 4, 0.12)
            if L == 'bass':
                for k in range(8): put(buf, lp(osc_saw(mtof(ch[0] - 12), int(beat / 2 * SR)), 400) * adsr(int(beat / 2 * SR), 0.005, 0.1, 0.6, 0.05), t + k * beat / 2, 0.16)
            if L == 'drone':
                nn = int((bar + 1.0) * SR); tt = np.arange(nn) / SR
                x = osc_saw(mtof(ch[0] - 12), nn, 0.003) + 0.5 * osc_saw(mtof(ch[0] - 5), nn, 0.003)
                x = lp(x, 500 + 300 * np.sin(2 * np.pi * 0.1 * (t + tt)).mean(), 2) * adsr(nn, 1.0, 0.2, 0.9, 1.0)
                put(buf, x, t, 0.20)
            if L == 'heartbeat':
                for k in (0, 2):
                    put(buf, kick(0.4), t + k * beat, 0.20); put(buf, kick(0.4), t + k * beat + 0.28, 0.13)
    buf = buf[:, :int(d * SR)]
    return buf

def riser(d=2.0):
    n = int(d * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
    out = np.zeros(n); step = SR // 100
    for i in range(0, n, step):
        f = 400 + 6000 * (i / n) ** 2; seg = x[i:i + step]; out[i:i + step] = sosfilt(butter(2, [f, f * 1.6], 'band', fs=SR, output='sos'), seg)
    return out * (t / d) ** 2 * 0.5
def hit():
    n = int(2.5 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 45 * t) * np.exp(-t * 2.5) + lp(rng.standard_normal(n), 2000) * np.exp(-t * 6) * 0.4) * 0.8

OFF = {'calm': -2, 'teaching': -1, 'trailer': 2, 'inspire': 1, 'dark': -1}
if __name__ == '__main__':
    cfg = json.load(open(sys.argv[1])); D = cfg['dur']; N = int(D * SR) + SR
    out = np.zeros((2, N)); XF = 2.0
    for s in cfg['sections']:
        t0, t1 = max(0, s['t0'] - XF / 2), min(D, s['t1'] + XF / 2)
        x = render_section(s['mood'], t1 - t0)
        rms = np.sqrt((x ** 2).mean()) + 1e-9; x *= 10 ** (OFF.get(s['mood'], 0) / 20) * 10 ** (-23 / 20) / rms   # equal loudness per section
        env = np.ones(x.shape[1]); k = int(XF * SR)
        if s['t0'] > 0: env[:k] = np.linspace(0, 1, k) ** 0.8
        if s['t1'] < D: env[-k:] = np.linspace(1, 0, k) ** 0.8
        put(out, x[0] * env, t0, 1.0, -1.0); put(out, x[1] * env, t0, 1.0, 1.0)   # pan -1/+1 keeps L/R as rendered
        print('section', s['mood'], round(s['t0'], 1), round(s['t1'], 1), flush=True)
    for t in cfg.get('drops', []):   # silence drop: 1.4s before a big point, back in after it
        a, b = int((t - 1.4) * SR), int((t + 0.6) * SR)
        if a < 0: continue
        g = np.ones(N); r = int(0.25 * SR)
        g[a - r:a] = np.linspace(1, 0, r); g[a:b] = 0; g[b:b + r * 4] = np.linspace(0, 1, r * 4)
        out *= g
    for t in cfg.get('hits', []):
        put(out, riser(), t - 2.0, 0.5); put(out, hit(), t, 0.7)
    out = out[:, :int(D * SR)]
    pk = np.abs(out).max()
    if pk > 0.95: out *= 0.95 / pk
    sf.write(sys.argv[2], out.T.astype(np.float32), SR, subtype='FLOAT')
    print('music written', round(D, 1), 's')

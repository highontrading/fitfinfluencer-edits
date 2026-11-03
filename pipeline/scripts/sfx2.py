# Extra procedural, license-free SFX for the v2 style (mood-matched: serious/medical palette).
import sys, numpy as np, soundfile as sf
sys.argv = [sys.argv[0], sys.argv[1]]
from music import SR, rng, lp, hp, bp, reverb, whoosh
OUT = sys.argv[1]
def norm(s, g): return s / np.abs(s).max() * g
def st(x): return np.stack([x, x])
def heartbeat():   # lub-dub
    nn = int(0.9 * SR); t = np.arange(nn) / SR; s = np.zeros(nn)
    for t0, f, a in ((0.0, 55, 1.0), (0.22, 70, 0.75)):
        tt = np.clip(t - t0, 0, None); s += a * np.sin(2 * np.pi * f * tt) * np.exp(-tt * 18) * (t >= t0)
    return st(norm(lp(s, 180), 0.9))
def ecg_beep():
    nn = int(0.16 * SR); t = np.arange(nn) / SR
    s = np.sin(2 * np.pi * 1000 * t) * np.minimum(1, t / 0.004) * np.exp(-np.maximum(0, t - 0.09) * 60)
    return st(norm(s, 0.5))
def sub_drop():
    nn = int(1.8 * SR); t = np.arange(nn) / SR
    s = np.sin(2 * np.pi * np.cumsum(30 + 70 * np.exp(-t * 4)) / SR) * np.exp(-t * 1.6)
    return norm(reverb(s, 2.2, 0.2), 0.95)
def hit_soft():
    nn = int(0.7 * SR); t = np.arange(nn) / SR
    s = np.sin(2 * np.pi * np.cumsum(60 + 60 * np.exp(-t * 20)) / SR) * np.exp(-t * 7) + lp(rng.standard_normal(nn), 900) * np.exp(-t * 30) * 0.3
    return norm(reverb(s, 1.0, 0.2), 0.8)
def shutter():
    nn = int(0.18 * SR); t = np.arange(nn) / SR
    s = hp(rng.standard_normal(nn), 1800) * (np.exp(-t * 90) + 0.7 * np.exp(-np.maximum(0, t - 0.07) * 120) * (t > 0.07))
    return st(norm(s, 0.55))
def tension():     # dark low swell into a reveal (not music: no melody, no beat)
    d = 2.2; nn = int(d * SR); t = np.arange(nn) / SR
    s = lp(rng.standard_normal(nn), 220) * (t / d) ** 2 + 0.3 * np.sin(2 * np.pi * 48 * t) * (t / d) ** 1.5
    return norm(reverb(s, 1.6, 0.3), 0.7)
def glitch():
    nn = int(0.25 * SR); s = np.zeros(nn)
    for k in range(7):
        a = rng.integers(0, nn - 2000); L = rng.integers(400, 2000)
        s[a:a + L] += bp(rng.standard_normal(L), 800 + 400 * k, 4000 + 600 * k) * 0.8
    return st(norm(s, 0.5))
def whoosh_soft():
    return whoosh(0.45, True) * 0.6
if __name__ == '__main__':
    for n, fn in [('heartbeat', heartbeat), ('ecg_beep', ecg_beep), ('sub_drop', sub_drop), ('hit_soft', hit_soft), ('shutter', shutter),
                  ('tension', tension), ('glitch', glitch), ('whoosh_soft', whoosh_soft)]:
        sf.write(f'{OUT}/sfx_{n}.wav', fn().T.astype(np.float32), SR)
    print('sfx2 done')

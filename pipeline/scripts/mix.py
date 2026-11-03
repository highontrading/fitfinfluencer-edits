# Mix: original voice (untouched) + sound effects at 30%. No background music, no normalisation/limiting (EDITING_RULES).
import sys, json, subprocess, numpy as np, soundfile as sf
work, name, adir = sys.argv[1:4]
SFX_LEVEL = 0.30   # creator asked for sound effects at 30% of the old level
spec = json.load(open(f'{work}/{name}_spec.json'))
v, sr = sf.read(f'{work}/{name}_voice.wav', dtype='float32')
if v.ndim > 1: v = v.mean(1)
v = np.pad(v, (0, int(round(spec.get('hold', 0) * sr))))
n = len(v)
fx = np.zeros((n, 2), np.float32)
for ev in spec.get('sfx', []):
    s, ssr = sf.read(f"{adir}/sfx_{ev['s']}.wav", dtype='float32')
    assert ssr == sr
    if s.ndim == 1: s = np.stack([s, s], 1)
    i = int(ev['t'] * sr)
    if i >= n or i < 0: continue
    s = s[:n - i] * (10 ** (ev.get('db', -14) / 20)) * SFX_LEVEL
    fx[i:i+len(s)] += s
# keep sound effects from ever clipping on top of the voice; the voice itself is never scaled
room = np.maximum(0.0, 0.99 - np.abs(v))[:, None]
fx = np.clip(fx, -room, room)
mix = np.stack([v, v], 1) + fx
sf.write(f'{work}/{name}_mix.wav', mix, sr, subtype='FLOAT')
print(name, 'mixed: voice untouched, sfx x%.2f, voice peak %.3f' % (SFX_LEVEL, np.abs(v).max()))

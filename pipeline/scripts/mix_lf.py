# Long-form mix: original voice (untouched) + sound effects at 30% + generated music, ducked under the voice.
# python3 -I scripts/mix_lf.py work vN audio music.wav [under_db]
import sys, json, numpy as np, soundfile as sf
from scipy.ndimage import uniform_filter1d
work, name, adir, mus = sys.argv[1:5]; UNDER = float(sys.argv[5]) if len(sys.argv) > 5 else 19.0
SFX_LEVEL = 0.30
spec = json.load(open(f'{work}/{name}_spec.json'))
v, sr = sf.read(f'{work}/{name}_voice.wav', dtype='float32')
if v.ndim > 1: v = v.mean(1)
v = np.pad(v, (0, int(round(spec.get('hold', 0) * sr)))); n = len(v)
fx = np.zeros((n, 2), np.float32)
for ev in spec.get('sfx', []):
    s, ssr = sf.read(f"{adir}/sfx_{ev['s']}.wav", dtype='float32')
    if s.ndim == 1: s = np.stack([s, s], 1)
    i = int(ev['t'] * sr)
    if i >= n or i < 0: continue
    s = s[:n - i] * (10 ** (ev.get('db', -14) / 20)) * SFX_LEVEL; fx[i:i + len(s)] += s
m, msr = sf.read(mus, dtype='float32'); assert msr == sr, (msr, sr)
m = m[:n] if len(m) >= n else np.pad(m, ((0, n - len(m)), (0, 0)))
# voice activity -> ducking envelope
hop = sr // 100; k = n // hop
rms = np.sqrt(uniform_filter1d((v[:k * hop].reshape(k, hop) ** 2).mean(1), 5) + 1e-12); db = 20 * np.log10(rms)
act = (db > -45).astype(np.float32)
g = np.zeros(k, np.float32); a_up, a_dn = 1 - np.exp(-1 / 8), 1 - np.exp(-1 / 50)   # 80 ms attack, 500 ms release
for i in range(1, k): g[i] = g[i - 1] + (act[i] - g[i - 1]) * (a_up if act[i] > g[i - 1] else a_dn)
mask = np.zeros(n, bool); mask[:k * hop] = np.repeat(act, hop).astype(bool)
v_db = 20 * np.log10(np.sqrt((v[mask] ** 2).mean()) + 1e-9) if mask.any() else -20.0
m_db = 20 * np.log10(np.sqrt((m ** 2).mean()) + 1e-9)
under = v_db - UNDER - m_db                       # gain (dB) that puts music UNDER dB below the voice
gain_db = under + (1 - g) * 6.0                    # +6 dB in pauses / graphics-only moments
gain = np.repeat(10 ** (gain_db / 20), hop); gain = np.pad(gain, (0, n - len(gain)), 'edge')[:n]
mus_out = m * gain[:, None]
room = np.maximum(0.0, 0.99 - np.abs(v))[:, None]
bed = np.clip(fx + mus_out, -room, room)          # effects + music never clip on top of the voice; the voice itself is never scaled
mix = np.stack([v, v], 1) + bed
sf.write(f'{work}/{name}_mix.wav', mix, sr, subtype='FLOAT')
print(name, 'mixed: voice untouched (active level %.1f dBFS), music %.0f dB under voice, sfx x%.2f' % (v_db, UNDER, SFX_LEVEL))

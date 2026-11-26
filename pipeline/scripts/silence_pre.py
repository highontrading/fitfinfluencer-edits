# Zero the trailer voice inside the question-card lead-ins (silence only; the voice itself is never altered).
import sys, json, numpy as np, soundfile as sf
work = sys.argv[1]; p = json.load(open(f'{work}/v52_pre.json'))
v, sr = sf.read(f'{work}/v52_voice.wav', dtype='float32'); f = int(0.03 * sr)
for t0, t1 in p['pre']:
    a, b = int(t0 * sr), int((t1 + 0.04) * sr); v[a:b] = 0
    v[b:b + f] *= np.linspace(0, 1, f)[:len(v[b:b + f])]
sf.write(f'{work}/v52_voice.wav', v, sr, subtype='FLOAT'); print('silenced', len(p['pre']), 'lead-ins')

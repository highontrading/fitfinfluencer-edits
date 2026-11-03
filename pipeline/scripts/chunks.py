# Split audio into utterance chunks at pauses, transcribe each chunk separately.
import sys, json, wave, numpy as np
from faster_whisper import WhisperModel
work, v, lang = sys.argv[1], sys.argv[2], sys.argv[3]
thr = float(sys.argv[4]) if len(sys.argv) > 4 else -40
w = wave.open(f'{work}/a{v}.wav'); sr = w.getframerate()
x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)/32768
hop = 160; n = len(x)//hop
db = 20*np.log10(np.sqrt((x[:n*hop].reshape(n, hop)**2).mean(1))+1e-9)
db = np.convolve(db, np.ones(3)/3, 'same')
sp = db > thr
# close tiny gaps (<0.22s) and drop tiny blips (<0.12s)
def runs(m):
    r = []; i = 0
    while i < len(m):
        j = i
        while j < len(m) and m[j] == m[i]: j += 1
        r.append([bool(m[i]), i, j]); i = j
    return r
for val, i, j in runs(sp):
    if not val and (j-i)*0.01 < 0.22 and i > 0 and j < len(sp): sp[i:j] = True
for val, i, j in runs(sp):
    if val and (j-i)*0.01 < 0.12: sp[i:j] = False
chunks = [(i*0.01, j*0.01) for val, i, j in runs(sp) if val]
m = WhisperModel('/root/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/snapshots/0a363e9161cbc7ed1431c9597a8ceaf0c4f78fcf', device='cpu', compute_type='int8', cpu_threads=4)
out = []
for k, (a, b) in enumerate(chunks):
    pa, pb = max(0, a-0.15), min(len(x)/sr, b+0.15)
    seg = x[int(pa*sr):int(pb*sr)]
    seg = np.concatenate([np.zeros(int(0.3*sr), np.float32), seg, np.zeros(int(0.3*sr), np.float32)])
    segs, _ = m.transcribe(seg, language=lang, word_timestamps=True, condition_on_previous_text=False, beam_size=5)
    words = []
    for s in segs:
        for wd in s.words:
            words.append({'w': wd.word.strip(), 's': round(min(max(wd.start-0.3+pa, a), b), 3), 'e': round(min(max(wd.end-0.3+pa, a), b), 3)})
    text = ' '.join(wd['w'] for wd in words)
    out.append({'id': k, 's': round(a, 2), 'e': round(b, 2), 'text': text, 'words': words})
    print(f"{k:3d} {a:7.2f}-{b:7.2f} ({b-a:4.2f}) {text}", flush=True)
json.dump(out, open(f'{work}/ch{v}.json', 'w'), indent=1, ensure_ascii=False)

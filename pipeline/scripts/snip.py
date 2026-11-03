import sys, wave, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel('/root/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/snapshots/0a363e9161cbc7ed1431c9597a8ceaf0c4f78fcf', device='cpu', compute_type='int8', cpu_threads=4)
work = sys.argv[1]
for spec in sys.argv[2:]:
    v, a, b, lang = spec.split(':')
    w = wave.open(f'{work}/a{v}.wav'); sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)/32768
    x = x[int(float(a)*sr):int(float(b)*sr)]
    segs, _ = m.transcribe(x, language=lang, word_timestamps=True, condition_on_previous_text=False)
    print(f'--- v{v} {a}-{b}')
    print(' '.join(f"{wd.word.strip()}[{wd.start+float(a):.2f}-{wd.end+float(a):.2f}]" for s in segs for wd in s.words))

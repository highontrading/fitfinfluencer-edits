import sys, numpy as np, soundfile as sf
from scipy.signal import resample_poly
from faster_whisper import WhisperModel
m = WhisperModel('/root/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/snapshots/0a363e9161cbc7ed1431c9597a8ceaf0c4f78fcf', device='cpu', compute_type='int8', cpu_threads=4)
x, sr = sf.read(sys.argv[1], dtype='float32')
if x.ndim > 1: x = x.mean(1)
x = resample_poly(x, 1, 3).astype(np.float32)
segs, _ = m.transcribe(x, language=sys.argv[2], condition_on_previous_text=False, vad_filter=False)
for s in segs: print(f'{s.start:6.2f}-{s.end:6.2f} {s.text}', flush=True)

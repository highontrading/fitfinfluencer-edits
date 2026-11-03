import sys, json, wave, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel('/root/.cache/huggingface/hub/models--mobiuslabsgmbh--faster-whisper-large-v3-turbo/snapshots/0a363e9161cbc7ed1431c9597a8ceaf0c4f78fcf', device='cpu', compute_type='int8', cpu_threads=4)
for i in sys.argv[2:]:
    wf=wave.open(f'{sys.argv[1]}/a{i}.wav'); aud=np.frombuffer(wf.readframes(wf.getnframes()),np.int16).astype(np.float32)/32768
    segs, info = m.transcribe(aud, word_timestamps=True, vad_filter=False, condition_on_previous_text=False)
    out = {'lang': info.language, 'segments': []}
    for s in segs:
        out['segments'].append({'start': s.start, 'end': s.end, 'text': s.text, 'words': [{'s': w.start, 'e': w.end, 'w': w.word, 'p': w.probability} for w in s.words]})
    json.dump(out, open(f'{sys.argv[1]}/t{i}.json', 'w'), indent=1)
    print(i, info.language, flush=True)

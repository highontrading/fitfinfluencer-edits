# Split EDL items at internal pauses (> GAP s below -42 dB) so long silences inside a chunk are removed.
# Caption text is split proportionally to the chunk's transcript words on each side of the pause.
# python3 -I scripts/tighten.py N [gap]
import json, sys, wave, numpy as np
n = sys.argv[1]; GAP = float(sys.argv[2]) if len(sys.argv) > 2 else 0.42
e = json.load(open(f'edl/v{n}.json')); ch = {c['id']: c for c in json.load(open(f'work/ch{n}.json'))}
w = wave.open(f'work/a{n}.wav'); a = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
hop = 160; m = len(a) // hop; db = 20 * np.log10(np.sqrt((a[:m * hop].reshape(m, hop) ** 2).mean(1)) + 1e-9)
out = []; saved = 0
for it in e['keep']:
    c = ch[it['c']]; s = it.get('s', c['s'] - e['lead']); en = it.get('e', c['e'] + e['tail'])
    sil = db[int(s * 100):int(en * 100)] < -42
    # trim silent edges (keep 0.08s before speech, 0.14s after)
    k = 0
    while k < len(sil) and sil[k]: k += 1
    if k / 100 > 0.12 and k < len(sil): s0 = s; s = s + k / 100 - 0.08; saved += s - s0
    k = 0
    while k < len(sil) and sil[len(sil) - 1 - k]: k += 1
    if k / 100 > 0.2 and k < len(sil): e0 = en; en = en - k / 100 + 0.14; saved += e0 - en
    it = dict(it, s=round(s, 3), e=round(en, 3))
    sil = db[int(s * 100):int(en * 100)] < -42
    cuts = []; i = 0
    while i < len(sil):
        if sil[i]:
            j = i
            while j < len(sil) and sil[j]: j += 1
            if (j - i) / 100 > GAP and i > 0 and j < len(sil): cuts.append((s + i / 100 + 0.12, s + j / 100 - 0.08))
            i = j
        else: i += 1
    if not cuts: out.append(it); continue
    words = [x for x in c['words'] if s - 0.05 <= (x['s'] + x['e']) / 2 <= en + 0.05] or c['words']
    toks = it['text'].split(); bounds = [s] + [x for cu in cuts for x in cu] + [en]
    segs = [(bounds[k], bounds[k + 1]) for k in range(0, len(bounds), 2)]
    # tokens per segment, proportional to transcript words falling in each segment
    cnt = [sum(1 for x in words if a0 <= (x['s'] + x['e']) / 2 < b0) for a0, b0 in segs]
    if sum(cnt) == 0 or any(v == 0 for v in cnt): out.append(it); continue
    tot = sum(cnt); acc = 0; pos = [0]
    for v in cnt[:-1]: acc += v; pos.append(round(acc * len(toks) / tot))
    pos.append(len(toks))
    if any(pos[k + 1] <= pos[k] for k in range(len(segs))): out.append(it); continue
    for k, (a0, b0) in enumerate(segs):
        out.append({'c': it['c'], 's': round(a0, 3), 'e': round(b0, 3), 'text': ' '.join(toks[pos[k]:pos[k + 1]])})
    saved += sum(b - a for a, b in cuts)
e['keep'] = out; json.dump(e, open(f'edl/v{n}.json', 'w'), indent=1, ensure_ascii=False)
print(f'v{n}: {len(out)} items, removed {saved:.1f}s of pauses (source time)')

# Build a tight cut from a chunk-based EDL: frame-aligned shots, graded video-only cut.mp4,
# polished voice.wav and an output timeline (shots + caption words in output time).
import json, sys, subprocess, numpy as np, soundfile as sf, re, os
from align import align

FPS_N, FPS_D = 30000, 1001
FD = FPS_D / FPS_N

def build(edl, work):
    name = edl['name']; src = f"{work}/{edl['src']}"
    ch = {c['id']: c for c in json.load(open(f"{work}/{edl['chunks']}"))}
    lead, tail = edl.get('lead', 0.06), edl.get('tail', 0.10)
    fullw = [{'w': w['w'].strip(), 's': w['s'], 'e': w['e']} for sg in json.load(open(f"{work}/{edl['transcript']}"))['segments'] for w in sg['words']]
    items = []
    for it in edl['keep']:
        c = ch[it['c']]
        s = it.get('s', c['s'] - lead); e = it.get('e', c['e'] + tail)
        items.append((it, c, s, e))
    # frame-align shots, never overlapping
    shots = []
    for it, c, s, e in items:
        n0 = int(round(s / FD)); n1 = int(round(e / FD))
        if shots and n0 < shots[-1]['n1'] and it.get('c') != shots[-1]['c']:
            n0 = max(n0, shots[-1]['n1'])
        shots.append({'n0': n0, 'n1': n1, 'c': it['c'], 'it': it})
    t = 0.0; tl_shots = []; words = []
    for k, sh in enumerate(shots):
        d = (sh['n1'] - sh['n0']) * FD
        s0 = sh['n0'] * FD
        tl_shots.append({'k': k, 'c': sh['c'], 'src0': s0, 'src1': sh['n1'] * FD, 'out0': t, 'out1': t + d, 'n0': sh['n0'], 'n1': sh['n1']})
        c = ch[sh['c']]; it = sh['it']
        wf = [w for w in fullw if w['e'] > s0 + 0.02 and w['s'] < sh['n1'] * FD - 0.02]
        wc = [w for w in c['words'] if w['e'] > s0 + 0.02 and w['s'] < sh['n1'] * FD - 0.02]
        cl = lambda L: sum(len(w['w']) for w in L)
        ws = wc if cl(wc) >= 0.85 * cl(wf) else wf
        ws = [dict(w, s=max(w['s'], s0), e=min(w['e'], sh['n1'] * FD)) for w in ws]
        text = it.get('text')
        if text is None:
            out_words = [(w['w'], w['s'], w['e']) for w in ws]
        else:
            tw = text.split()
            best = None
            for cand in (wf, wc):
                cand = [dict(w, s=max(w['s'], s0), e=min(w['e'], sh['n1'] * FD)) for w in cand]
                if not cand: continue
                tt, q = align(tw, cand)
                if best is None or q > best[1]: best = (tt, q)
            if best is None:
                best = ([(s0 + (sh['n1'] * FD - s0) * i / len(tw), s0 + (sh['n1'] * FD - s0) * (i + 1) / len(tw)) for i in range(len(tw))], 0)
            if best[1] < 0.5: print('  low alignment', round(best[1], 2), text[:60])
            out_words = [(tw[i], best[0][i][0], best[0][i][1]) for i in range(len(tw))]
        for w, a, b in out_words:
            a = max(a, s0); b = min(b, sh['n1'] * FD)
            if b <= a: b = a + 0.12
            words.append({'w': w, 't0': round(t + a - s0, 3), 't1': round(t + b - s0, 3), 'shot': k, 'brk': False})
        if words: words[-1]['brk'] = True   # phrase boundary at end of every shot
        t += d
    total = sum(s['n1'] - s['n0'] for s in shots)
    sp = float(edl.get('speed', 1.1))
    nout = int(round(total / sp))
    if sp != 1.0:
        for w in words: w['t0'] = round(w['t0'] / sp, 3); w['t1'] = round(w['t1'] / sp, 3)
        for sh in tl_shots: sh['out0'] /= sp; sh['out1'] /= sp
    json.dump({'fps': [FPS_N, FPS_D], 'frames': nout, 'dur': nout * FD, 'speed': sp, 'shots': tl_shots, 'words': words},
              open(f"{work}/{name}_tl.json", 'w'), indent=1, ensure_ascii=False)

    if os.environ.get('TL_ONLY'):
        print(name, 'timeline only'); return
    # video
    sel = '+'.join(f"between(n,{s['n0']},{s['n1']-1})" for s in shots)
    grade = edl.get('grade', "eq=contrast=1.07:saturation=1.10:gamma=0.98,colorbalance=rs=0.025:gs=0.0:bs=-0.03:rm=0.015:bm=-0.015:rh=0.02:bh=-0.02,unsharp=5:5:0.35")
    vf = f"select='{sel}',setpts=N/(30000/1001)/TB/{sp},fps=30000/1001,{grade},format=yuv420p"
    open(f"{work}/{name}_vf.txt", 'w').write(vf)
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-map', '0:v:0', '-filter_script:v', f"{work}/{name}_vf.txt",
                    '-frames:v', str(nout), '-c:v', 'libx264', '-preset', 'fast', '-crf', str(edl.get('crf', 13)), '-an',
                    f"{work}/{name}_cut.mp4"], check=True)
    # audio
    full = f"{work}/{edl['src']}.48k.wav"
    if not os.path.exists(full):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-map', '0:a:0', '-ac', '1', '-ar', '48000', '-c:a', 'pcm_f32le', full], check=True)
    a, sr = sf.read(full, dtype='float32')
    fade = int(0.008 * sr); parts = []
    for s in shots:
        s0 = int(round(s['n0'] * FD * sr)); s1 = int(round(s['n1'] * FD * sr))
        p = a[s0:s1].copy()
        p[:fade] *= np.linspace(0, 1, fade); p[-fade:] *= np.linspace(1, 0, fade)
        parts.append(p)
    v = np.concatenate(parts)
    want = int(round(total * FD * sr)); v = np.pad(v, (0, max(0, want - len(v))))[:want]
    sf.write(f"{work}/{name}_voice_raw.wav", v, sr, subtype='FLOAT')
    if sp != 1.0:   # pitch-preserving speed-up
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', f"{work}/{name}_voice_raw.wav", '-af', f'rubberband=tempo={sp}:pitchq=quality:formant=preserved',
                        '-ar', '48000', '-c:a', 'pcm_f32le', f"{work}/{name}_voice_rb.wav"], check=True)
        v, _ = sf.read(f"{work}/{name}_voice_rb.wav", dtype='float32')
        want = int(round(nout * FD * sr)); v = np.pad(v, (0, max(0, want - len(v))))[:want]
        sf.write(f"{work}/{name}_voice_raw.wav", v, sr, subtype='FLOAT')
    # EDITING_RULES: the voice is never processed (no EQ/denoise/compression/limiter). Only the 1.1x speed-up above.
    import shutil; shutil.copyfile(f"{work}/{name}_voice_raw.wav", f"{work}/{name}_voice.wav")
    print(name, 'shots', len(shots), 'speed', sp, 'dur %.2f' % (nout * FD), 'frames', nout)

if __name__ == '__main__':
    build(json.load(open(sys.argv[1])), sys.argv[2])

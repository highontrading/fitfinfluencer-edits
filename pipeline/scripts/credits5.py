import json, os, re
m = json.load(open('stock/meta.json')); cm = json.load(open('stock/commons.json'))
byfile = {os.path.basename(v['file']): v for v in cm.values() if v.get('file')}
names = {20: '20_Breakfast_Myth_Fasting_Reel_Hindi', 21: '21_Sugar_Glycation_Reel_Hindi', 22: '22_Overcooked_Vegetables_Polyphenols_Reel_Hindi',
         23: '23_72_Hour_Fast_Autophagy_Reel_Hindi', 24: '24_Loud_Music_DNA_Aging_Reel_Hindi', 25: '25_Epigenome_Biological_Age_LongForm_Hindi'}
out = ['# Stock footage and images used (batch 5)', '',
       '- **Mixkit (mixkit.co):** each clip page was checked and states it is free "for commercial or personal use, under the Mixkit Stock Video Free License" (https://mixkit.co/license/#videoFree). Restricted (personal-use-only) clips were excluded.',
       '- **Wikimedia Commons:** only Public Domain, CC0 or CC BY files were used (no ShareAlike or NonCommercial), credited below as their licence requires.',
       '- **Animated science graphics** (DNA helix, cells, ECG monitor, flowcharts) are drawn by the editing pipeline itself.', '']
for v, n in names.items():
    p = f'work/v{v}_spec.json'
    if not os.path.exists(p): continue
    s = json.load(open(p))
    rows = []
    for b in sorted(s['broll'], key=lambda b: b['t0']):
        if b['clip'] in m:
            mm = m[b['clip']]; rows.append(f"| {b['t0']:.1f}–{b['t1']:.1f}s | {mm['slug'].replace('-', ' ')} | Mixkit Free License | {mm.get('page') or ''} |")
    for e in s['events']:
        if e['type'] == 'photo':
            c = byfile.get(os.path.basename(e['src']))
            if c: rows.append(f"| {e['t0']:.1f}–{e['t1']:.1f}s | {c['title'][5:]} by {re.sub(r'\s+', ' ', c['artist'])[:80]} | {c['license']} | {c['page']} |")
    out += [f'## {n}.mp4', '', '| Time in video | Asset | Licence | Source |', '|---|---|---|---|'] + rows + ['']
open('deliver5/STOCK_CREDITS.md', 'w').write('\n'.join(out)); print('\n'.join(out[:12]))

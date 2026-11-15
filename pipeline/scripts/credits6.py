import json, os, re
m = json.load(open('stock/meta.json')); cm = json.load(open('stock/commons.json'))
byfile = {os.path.basename(v['file']): v for v in cm.values() if v.get('file')}
names = {26: '26_Peptides_3_Categories_Reel_Hindi', 27: '27_Low_Sodium_Salt_BP_Reel_Hindi', 28: '28_Wife_BP_170_110_Silent_Killer_Reel_Hindi',
         29: '29_Wall_Sit_Lowers_BP_Reel_Hindi', 30: '30_Health_Insurance_Illness_EMI_Reel_Hindi', 31: '31_Peptides_Ranked_Free_Works_Reel_Hindi',
         32: '32_Chai_Biscuit_Slow_Poison_Reel_Hindi'}
out = ['# Stock footage and images used (batch 6)', '',
       '- **Mixkit (mixkit.co):** each clip page was checked and states it is free "for commercial or personal use, under the Mixkit Stock Video Free License" (https://mixkit.co/license/#videoFree). Restricted (personal-use-only) clips were excluded.',
       '- **Wikimedia Commons:** only Public Domain, CC0 or CC BY files were used (no ShareAlike or NonCommercial), credited below as their licence requires.',
       '- **Animated science graphics** (flowcharts, checklists, charts, counters) are drawn by the editing pipeline itself.', '']
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
open('deliver6/STOCK_CREDITS.md', 'w').write('\n'.join(out)); print('\n'.join(out[:12]))

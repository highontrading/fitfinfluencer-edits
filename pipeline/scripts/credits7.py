import json, os, re
m = json.load(open('stock/meta.json')); cm = json.load(open('stock/commons.json'))
byfile = {os.path.basename(v['file']): v for v in cm.values() if v.get('file')}
names = {33: '33_Roti_Gluten_Modified_Wheat_Reel_Hindi', 34: '34_Salt_Not_The_Villain_Reel_Hindi', 35: '35_Sugar_Addiction_Like_Cocaine_Reel_Hindi',
         36: '36_Naked_Carbs_Dress_Them_Up_Reel_Hindi', 37: '37_Water_Minerals_Sea_Salt_Reel_Hindi', 38: '38_Thin_Fat_Indians_TOFI_Reel_Hindi',
         39: '39_Meal_Sequencing_Order_Reel_Hindi', 40: '40_Alcohol_Fake_Sleep_Reel_Hindi', 41: '41_Indian_Thaali_Best_Diet_Reel_Hindi'}
out = ['# Stock footage and images used (batch 7)', '',
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
open('deliver7/STOCK_CREDITS.md', 'w').write('\n'.join(out)); print('\n'.join(out[:12]))

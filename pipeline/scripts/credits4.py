import json
m = json.load(open('stock/meta.json'))
names = {13: '13_Naked_Carbs_Reel_Hindi', 14: '14_Water_Minerals_Reel_Hindi', 15: '15_Thin_Fat_Indians_Reel_Hindi',
         16: '16_Meal_Sequencing_Reel_Hindi', 17: '17_Alcohol_Sleep_Reel_Hindi', 18: '18_Indian_Thali_Reel_Hindi'}
out = ['# Stock footage used (batch 4)', '',
       'All clips are from Mixkit (mixkit.co). Each clip page was checked before use and states: "Download this free stock video clip for commercial or personal use, under the Mixkit Stock Video Free License." Clips under the "Restricted License (personal use only)" were excluded.',
       '', 'License: https://mixkit.co/license/#videoFree', '']
for v, n in names.items():
    s = json.load(open(f'work/v{v}_spec.json'))
    out += [f'## {n}.mp4', '', '| Time in video | Clip | Mixkit page |', '|---|---|---|']
    for b in sorted(s['broll'], key=lambda b: b['t0']):
        mm = m[b['clip']]; page = mm.get('page') or f"https://mixkit.co/free-stock-video/{mm['slug']}-{b['clip']}/"
        out.append(f"| {b['t0']:.1f}–{b['t1']:.1f}s | {mm['slug'].replace('-', ' ')} | {page} |")
    out.append('')
open('deliver4/STOCK_CREDITS.md', 'w').write('\n'.join(out))
print('\n'.join(out[:20]))

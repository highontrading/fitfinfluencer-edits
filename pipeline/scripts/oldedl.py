# compare an old EDL (pipeline/edl/vM.json) with the new chunking of the same raw (work/chN.json) + takes flags
import json, sys
n, m = sys.argv[1], sys.argv[2]
ch = {c['id']: c for c in json.load(open(f'work/ch{n}.json'))}
old = {x['c']: x for x in json.load(open(f'/home/user/fitfinfluencer-edits/pipeline/edl/v{m}.json'))['keep']}
flags = {int(l.split()[0]): l.split('use c')[-1].strip() for l in open(f'work/takes{n}.txt') if 'EARLIER' in l}
for i in sorted(ch):
    o = old.get(i)
    tag = 'KEEP' if o else '    '
    fl = f' [earlier take -> c{flags[i]}]' if i in flags else ''
    print(i, tag, round(ch[i]['s'], 1), ch[i]['text'][:90], fl, '||', (o['text'][:70] + (f" s={o.get('s')}" if 's' in o else '') + (f" e={o.get('e')}" if 'e' in o else '')) if o else '')

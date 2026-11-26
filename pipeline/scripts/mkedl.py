# Build edl/vN.json from a compact keep list (work/kN.txt): lines "cid [s=..] [e=..] | caption text".
# Auto-extends a chunk's start/end to cover transcript words the pause splitter clipped at its edges.
import json, sys, re
n = sys.argv[1]; W = 'work'
ch = {c['id']: c for c in json.load(open(f'{W}/ch{n}.json'))}
tw = [w for sg in json.load(open(f'{W}/t{n}.json'))['segments'] for w in sg['words']]
keep = []
for ln in open(f'{W}/k{n}.txt', encoding='utf-8'):
    ln = ln.strip()
    if not ln or ln.startswith('#'): continue
    head, text = ln.split('|', 1)
    p = head.split(); c = ch[int(p[0])]; it = {'c': int(p[0])}
    for q in p[1:]:
        k, v = q.split('=')
        if k == 'sw': it['s'] = round(c['words'][int(v)]['s'] - 0.05, 3)      # start at word N of the chunk
        elif k == 'ew': it['e'] = round(c['words'][int(v)]['s'] - 0.04, 3)    # end just before word N
        else: it[k] = float(v)
    if 's' not in it:
        pre = [w for w in tw if w['e'] > c['s'] - 0.6 and w['s'] < c['s'] - 0.08 and w['e'] <= c['s'] + 0.35]
        if pre: it['s'] = round(max(min(w['s'] for w in pre) - 0.06, c['s'] - 0.45, ch[c['id'] - 1]['e'] + 0.02 if c['id'] - 1 in ch else 0), 3)
    if 'e' not in it:
        post = [w for w in tw if w['s'] > c['e'] - 0.1 and w['s'] < c['e'] + 0.3 and w['e'] - c['e'] > 0.08]
        if post: it['e'] = round(min(max(w['e'] for w in post) + 0.08, c['e'] + 0.45, ch[c['id'] + 1]['s'] - 0.02 if c['id'] + 1 in ch else 1e9), 3)
    it['text'] = text.strip(); keep.append(it)
json.dump({'name': f'v{n}', 'src': f'v{n}.mp4', 'chunks': f'ch{n}.json', 'transcript': f't{n}.json', 'speed': 1.1, 'keep': keep, 'lead': 0.06, 'tail': 0.10},
          open(f'edl/v{n}.json', 'w'), indent=1, ensure_ascii=False)
print(f'v{n}: {len(keep)} chunks, src speech {sum(it.get("e", ch[it["c"]]["e"]) - it.get("s", ch[it["c"]]["s"]) for it in keep):.1f}s')

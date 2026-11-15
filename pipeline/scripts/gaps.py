# print transcript words that fall outside every chunk (speech the pause-splitter may have dropped)
import json, sys
n = sys.argv[1]; w = 'work'
ch = json.load(open(f'{w}/ch{n}.json')); t = json.load(open(f'{w}/t{n}.json'))
iv = [(c['s'] - 0.05, c['e'] + 0.05) for c in ch]
out = []
for sg in t['segments']:
    for x in sg['words']:
        m = (x['s'] + x['e']) / 2
        if not any(a <= m <= b for a, b in iv): out.append('%s@%.1f' % (x['w'].strip(), x['s']))
print(' '.join(out) or 'none')

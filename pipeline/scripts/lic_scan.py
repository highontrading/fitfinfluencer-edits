import json, sys, os, re, html, subprocess, concurrent.futures as cf, time
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'stock')
idx = json.load(open(f'{D}/index.json'))
lp = f'{D}/lic.json'; lic = json.load(open(lp)) if os.path.exists(lp) else {}
qs = sys.argv[2:]; N = int(sys.argv[1])
todo = []
for q in qs:
    es = [e for e in idx.values() if e['q'] == q][:N]
    todo += [e for e in es if str(e['id']) not in lic]
def chk(e):
    for k in range(6):
        r = subprocess.run(['curl', '-s', '-m', '25', '-A', 'Mozilla/5.0', '-w', '\n%{http_code}', f"https://mixkit.co/free-stock-video/{e['slug']}-{e['id']}/"], capture_output=True, text=True).stdout
        t, code = r.rsplit('\n', 1)
        if code == '200': break
        time.sleep(5 * (k + 1))
    time.sleep(1.0)
    free = 'clip for commercial or personal use, under the' in t
    restr = 'personal use only' in t
    d = re.findall(r'"description":"([^"]*)"', t)
    d = [x for x in d if not x.startswith('Mixkit is')]
    return str(e['id']), {'free': free, 'restricted': restr, 'slug': e['slug'], 'q': e['q'], 'desc': html.unescape(d[0]) if d else ''}
for i, e in enumerate(todo):
    k, v = chk(e); lic[k] = v
    if i % 20 == 0: json.dump(lic, open(lp, 'w'), indent=1); print('..', i, len(todo), flush=True)
json.dump(lic, open(lp, 'w'), indent=1)
for q in qs:
    es = [e for e in idx.values() if e['q'] == q][:N]
    fr = [f"{e['id']}:{e['slug'][:42]}" for e in es if lic.get(str(e['id']), {}).get('free')]
    print(f'## {q} free {len(fr)}/{len(es)}: ' + ' | '.join(fr))

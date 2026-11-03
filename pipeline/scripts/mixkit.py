# Mixkit stock search: python3 mixkit.py search q1 q2 ... -> stock/index.json ; python3 mixkit.py info id ...
import sys, re, json, html, os, subprocess, concurrent.futures as cf
UA = 'Mozilla/5.0'
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'stock')
def get(u):
    r = subprocess.run(['curl', '-s', '-m', '25', '-A', UA, u], capture_output=True, text=True)
    return r.stdout
def search(q):
    out = []
    for page in ('', '?page=2'):
        t = get(f'https://mixkit.co/free-stock-video/{q}/{page}')
        for slug, vid in re.findall(r'href="/free-stock-video/([a-z0-9-]+)-(\d+)/"', t):
            out.append((int(vid), slug))
    seen = set(); res = []
    for v, s in out:
        if v not in seen: seen.add(v); res.append({'id': v, 'slug': s, 'q': q})
    return res
def info(vid, slug):
    t = get(f'https://mixkit.co/free-stock-video/{slug}-{vid}/')
    lic = re.search(r'"license":"([^"]+)"', t)
    desc = re.search(r'"description":"([^"]*)"', t)
    free = 'commercial or personal use, under the' in t and 'videoFree' in (lic.group(1) if lic else '')
    dims = re.findall(r'(\d{3,4}) ?x ?(\d{3,4})', t)
    return {'id': vid, 'slug': slug, 'license': lic.group(1) if lic else None, 'free': free,
            'desc': html.unescape(desc.group(1)) if desc else '', 'thumb': f'https://assets.mixkit.co/videos/{vid}/{vid}-thumb-720-0.jpg'}
if __name__ == '__main__':
    os.makedirs(D, exist_ok=True)
    idx_p = os.path.join(D, 'index.json')
    idx = json.load(open(idx_p)) if os.path.exists(idx_p) else {}
    if sys.argv[1] == 'search':
        with cf.ThreadPoolExecutor(6) as ex:
            for q, res in zip(sys.argv[2:], ex.map(search, sys.argv[2:])):
                print(f'## {q}: {len(res)}')
                for r in res[:30]:
                    idx.setdefault(str(r['id']), r)
                    print(f"  {r['id']} {r['slug']}")
        json.dump(idx, open(idx_p, 'w'), indent=1)

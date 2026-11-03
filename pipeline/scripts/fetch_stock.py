import json, subprocess, os, concurrent.futures as cf
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'stock')
lic = json.load(open(f'{D}/lic.json'))
ids = open(f'{D}/picks.txt').read().split()
os.makedirs(f'{D}/clips', exist_ok=True); os.makedirs(f'{D}/thumbs', exist_ok=True)
def work(i):
    L = lic.get(i)
    if not L or not L['free']: return i, {'err': 'NOT VERIFIED FREE'}
    m = dict(L); p = f'{D}/clips/{i}.mp4'
    for res in ('2160', '1080', '720'):
        r = subprocess.run(['curl', '-sf', '-m', '240', '-A', 'Mozilla/5.0', '-o', p, f'https://assets.mixkit.co/videos/{i}/{i}-{res}.mp4'])
        if r.returncode == 0 and os.path.getsize(p) > 10000: m['res'] = res; break
    else: return i, {'err': 'download failed'}
    subprocess.run(['curl', '-sf', '-m', '30', '-o', f'{D}/thumbs/{i}.jpg', f'https://assets.mixkit.co/videos/{i}/{i}-thumb-720-0.jpg'])
    j = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height:format=duration', '-of', 'json', p], capture_output=True, text=True).stdout)
    m.update({'w': j['streams'][0]['width'], 'h': j['streams'][0]['height'], 'dur': float(j['format']['duration']), 'file': p,
              'page': f"https://mixkit.co/free-stock-video/{L['slug']}-{i}/"})
    return i, m
meta = {}
with cf.ThreadPoolExecutor(3) as ex:
    for i, m in ex.map(work, ids):
        meta[i] = m; print(i, m.get('err', ''), m.get('res'), m.get('w'), m.get('h'), round(m.get('dur', 0), 1), m.get('slug', '')[:50], flush=True)
json.dump(meta, open(f'{D}/meta.json', 'w'), indent=1)

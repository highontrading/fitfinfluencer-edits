# Wikimedia Commons search limited to commercial-safe licences (Public domain, CC0, CC BY - no ShareAlike / NC / ND).
# python3 scripts/commons.py search "query" [video|image] [limit]  -> appends to stock/commons.json
import sys, json, os, re, html, urllib.parse, subprocess
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'stock'); P = f'{D}/commons.json'
UA = 'FitFinfluencerEditPipeline/1.0 (video editing; contact via repository owner)'
OK = re.compile(r'^(public domain|pd.*|cc0.*|cc by \d(\.\d)?( [a-z-]+)?)$', re.I)
def api(params):
    q = urllib.parse.urlencode({**params, 'format': 'json'})
    import time
    for k in range(6):
        r = subprocess.run(['curl', '-s', '-m', '40', '-A', UA, f'https://commons.wikimedia.org/w/api.php?{q}'], capture_output=True, text=True).stdout
        try: return json.loads(r)
        except ValueError: time.sleep(60 * (k + 1))
    return {}
def search(q, kind='image', limit=30):
    ft = 'filetype:video' if kind == 'video' else 'filetype:bitmap'
    js = api({'action': 'query', 'generator': 'search', 'gsrsearch': f'{q} {ft}', 'gsrnamespace': 6, 'gsrlimit': limit,
              'prop': 'imageinfo', 'iiprop': 'url|size|mime|extmetadata', 'iiurlwidth': 1920})
    db = json.load(open(P)) if os.path.exists(P) else {}
    out = []
    for pg in (js.get('query', {}).get('pages', {}) or {}).values():
        ii = (pg.get('imageinfo') or [{}])[0]; em = ii.get('extmetadata', {})
        lic = html.unescape(re.sub('<[^>]+>', '', em.get('LicenseShortName', {}).get('value', ''))).strip()
        if 'sa' in lic.lower().split() or '-sa' in lic.lower() or 'nc' in lic.lower() or 'nd' in lic.lower() or not OK.match(lic): continue
        art = html.unescape(re.sub('<[^>]+>', '', em.get('Artist', {}).get('value', ''))).strip()[:120]
        desc = html.unescape(re.sub('<[^>]+>', '', em.get('ImageDescription', {}).get('value', ''))).strip()[:160]
        key = pg['title']
        db[key] = {'title': key, 'q': q, 'kind': kind, 'license': lic, 'artist': art, 'desc': desc, 'w': ii.get('width'), 'h': ii.get('height'),
                   'mime': ii.get('mime'), 'url': ii.get('url'), 'thumb': ii.get('thumburl'), 'page': ii.get('descriptionurl'),
                   'dur': float(em.get('Duration', {}).get('value', 0) or 0) if kind == 'video' else 0}
        out.append(db[key])
    json.dump(db, open(P, 'w'), indent=1, ensure_ascii=False)
    for e in out: print(f"{e['license']:<16} {e['w']}x{e['h']} {e['title'][:70]} | {e['artist'][:30]}")
    print('##', q, kind, len(out))
if __name__ == '__main__':
    search(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else 'image', int(sys.argv[4]) if len(sys.argv) > 4 else 30)

# Helpers to author a per-video spec (captions, graphics, camera, sfx) against the cut timeline.
import json, re

def norm(s): return re.sub(r'[^\w%./]', '', s.lower()).strip('.')

class Spec:
    def __init__(self, work, name):
        self.work, self.name = work, name
        self.tl = json.load(open(f'{work}/{name}_tl.json'))
        self.words = self.tl['words']
        self.events, self.sfx = [], []
        self.cam = {'zooms': [1.0, 1.16], 'faceY': 0.36, 'ranges': [], 'punches': [], 'shakes': [], 'zseq': []}
        self.capMoves = []
        self.hl = set()

    # word lookup: first word matching regex at/after time `after` (nth occurrence)
    def w(self, pat, after=0.0, n=1):
        k = 0
        for wd in self.words:
            if wd['t0'] + 1e-6 >= after and re.fullmatch(pat, norm(wd['w'])):
                k += 1
                if k == n: return wd
        raise KeyError(f'{pat} after {after}')
    def T(self, pat, after=0.0, n=1): return self.w(pat, after, n)['t0']
    def TE(self, pat, after=0.0, n=1): return self.w(pat, after, n)['t1']

    def add(self, ev, sfx=True):
        self.events.append(ev)
        if not sfx: return ev
        ty = ev['type']
        if ty == 'title': self.fx('swipe', ev['t0'] - 0.05, -17)
        elif ty == 'chips':
            for it in ev['items']: self.fx('pop', it['t'], -13)
        elif ty == 'checklist':
            self.fx('swipe', ev['t0'] - 0.05, -17)
            for it in ev['items']: self.fx('click', it['t'] + 0.25, -11); self.fx('pop', it['t'], -19)
        elif ty == 'flow':
            for nd in ev['nodes']: self.fx('whoosh' if nd.get('target') else 'pop', nd['t'] - (0.15 if nd.get('target') else 0), -13 if nd.get('target') else -14)
        elif ty == 'stat': self.fx('whoosh', ev['t0'] - 0.1, -16); self.fx('ding', ev['t0'] + 1.0, -17)
        elif ty == 'compare':
            for i, it in enumerate(ev['items']): self.fx('pop', it['t'], -13)
            self.fx('ding', ev['items'][-1]['t'] + 0.8, -17)
        elif ty == 'slam':
            self.fx('impact', ev['t0'], -11); self.cam['shakes'].append({'t': ev['t0'], 'amt': 12})
            self.events.append({'type': 'flash', 't0': ev['t0'], 't1': ev['t0'] + 0.3, 'a': 0.35})
        elif ty == 'badge': self.fx('pop', ev['t0'], -12); self.fx('ding', ev['t0'] + 0.15, -19)
        elif ty == 'chain':
            for it in ev['items']: self.fx('click', it['t'], -12); self.fx('pop', it['t'] + 0.05, -18)
        elif ty == 'cta':
            self.fx('riser', ev['t0'] - 1.55, -17); self.fx('impact', ev['t0'], -14); self.fx('whoosh', ev['t0'] - 0.2, -16)
        return ev

    def fx(self, s, t, db=-14): self.sfx.append({'s': s, 't': round(max(0, t), 3), 'db': db})

    def card(self, t0, t1, cap_y=1690, **kw):
        self.cam['ranges'].append({'mode': 'card', 't0': t0, 't1': t1, **({'card': kw} if kw else {})})
        self.capMoves.append({'t0': t0, 't1': t1, 'y': cap_y})
        self.fx('whoosh', t0 - 0.4, -17); self.fx('whoosh_dn', t1 - 0.05, -21)

    def punch(self, t, amt=0.10, hold=0.9): self.cam['punches'].append({'t': t, 'amt': amt, 'hold': hold})

    def captions(self, max_words=3, max_chars=17, hl_pats=()):
        pages, cur = [], []
        def flush():
            if cur: pages.append(list(cur)); cur.clear()
        for wd in self.words:
            txt = wd['w']
            cur.append(wd)
            chars = sum(len(x['w']) + 1 for x in cur)
            end_p = bool(re.search(r'[.,?!:;]$', txt))
            if wd.get('brk') or end_p or len(cur) >= max_words or chars >= max_chars:
                flush()
        flush()
        out = []
        for i, pg in enumerate(pages):
            t0 = pg[0]['t0']
            nxt = pages[i + 1][0]['t0'] if i + 1 < len(pages) else None
            t1 = pg[-1]['t1'] + 0.25
            if nxt is not None and nxt - pg[-1]['t1'] < 0.6: t1 = nxt
            if nxt is not None: t1 = min(t1, nxt)
            ws = []
            for wd in pg:
                clean = re.sub(r'[,.;:]+$', '', wd['w']).strip()
                hl = any(re.fullmatch(p, norm(clean)) for p in hl_pats) or bool(re.fullmatch(r'[\d./%]+', norm(clean)))
                ws.append({'w': clean, 't0': wd['t0'], 't1': wd['t1'], 'hl': hl})
            out.append({'t0': t0, 't1': t1, 'words': ws})
        return out

    def alt_zoom(self, zooms, extra_breaks=()):
        """Snap-zoom changes at every shot start and at sentence starts inside long shots."""
        times = set(round(s['out0'], 3) for s in self.tl['shots'])
        prev_end = False
        for wd in self.words:
            if prev_end and wd['t0'] - 0.02 > 0: times.add(round(wd['t0'] - 0.03, 3))
            prev_end = bool(re.search(r'[.?!]$', wd['w']))
        times.update(extra_breaks)
        ts = sorted(times)
        # drop changes closer than 1.2s to the previous one
        keep = []
        for t in ts:
            if not keep or t - keep[-1] >= 1.2: keep.append(t)
        self.cam['zseq'] = [{'t': t, 'z': zooms[i % len(zooms)]} for i, t in enumerate(keep)]

    def save(self, cap_pages, cta_t=None, cap_y=1360, music_offset=0.0, extra=None, hold=0.0, brand=None):
        hf = int(round(hold * 30000 / 1001))
        spec = {'fps': self.tl['fps'], 'frames': self.tl['frames'] + hf, 'dur': (self.tl['frames'] + hf) * 1001 / 30000, 'hold': hold,
                'captions': cap_pages, 'events': self.events, 'camera': self.cam, 'capY': cap_y,
                'capMoves': self.capMoves, 'sfx': sorted(self.sfx, key=lambda x: x['t']), 'ctaT': cta_t,
                'musicOffset': music_offset}
        if brand: spec['brand'] = brand
        if extra: spec.update(extra)
        json.dump(spec, open(f'{self.work}/{self.name}_spec.json', 'w'), indent=1, ensure_ascii=False)
        print('spec saved', self.name, len(self.events), 'events', len(cap_pages), 'caption pages', len(self.sfx), 'sfx')

# ---- stock b-roll (Mixkit Free License clips; see stock/meta.json) ----
import os as _os
STOCK = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'stock')
CROP = {'43850': .25, '28886': .65, '42898': .43, '43786': .38, '4701': .43, '50931': .65, '44432': .43, '4834': .57, '10443': .36,
        '28894': .65, '4773': .43, '722': .57, '42896': .65, '44438': .55, '10446': .57, '40529': .65, '3795': .4, '32792': .45,
        '609': .57, '887': .28, '34566': .28, '597': .5, '4840': .43, '4733': .65,
        '4629': .67, '1439': .4, '4761': .65, '28321': .18, '4911': .72, '144': .55, '2948': .28, '4764': .55, '372': .35, '4546': .47, '108': 1.0, '1086': .55, '42729': .72,
        '41227': .5, '40830': .5, '50426': .5, '42910': .5, '4779': .5,
        '4607': .5, '42620': .5, '26089': .45, '40883': .5, '985': .5, '43908': .5, '3692': .5, '43900': .5, '43030': .5, '8692': .5, '8711': .5, '51399': .5, '51394': .5, '31415': .5, '31407': .5, '52459': .5, '50576': .5, '2186': .5, '4547': .5, '40520': .5, '10420': .5, '52467': .5}

def _broll(self, clip, t0, t1, off=0.6, kb=0.07, xf=0.12, **kw):
    if t1 - t0 < 0.35: return None
    xf = min(xf, (t1 - t0) / 4)
    meta = json.load(open(f'{STOCK}/meta.json'))[str(clip)]
    assert 'file' in meta, clip
    assert t1 - t0 + off < meta['dur'] - 0.1, (clip, t1 - t0, meta['dur'])
    in_card = any(r['mode'] == 'card' and r['t0'] - 0.01 <= t0 and t1 <= r['t1'] + 0.01 for r in self.cam['ranges'])
    b = {'clip': str(clip), 'file': meta['file'], 't0': round(t0, 3), 't1': round(t1, 3), 'off': off, 'kb': kb, 'xf': xf,
         'x': CROP.get(str(clip), 0.5), 'fit': 'card' if in_card else 'full', 'vertical': meta['h'] > meta['w']}
    b.update(kw)
    if b['fit'] == 'full': self.fx('swipe', t0 - 0.06, -24)
    self.cam.setdefault('broll', []).append(b)
    return b
Spec.broll = _broll
_orig_save = Spec.save
def _save(self, *a, **k):
    extra = k.pop('extra', None) or {}
    extra['broll'] = self.cam.get('broll', [])
    _orig_save(self, *a, extra=extra, **k)
Spec.save = _save

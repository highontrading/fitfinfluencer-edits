# v2 spec helpers (EDITING_RULES): English on-screen text, no emojis, text behind speaker, free-position kinetic type, ECG, callouts.
import json, re
from spec_lib import Spec as _Spec, STOCK, CROP

EMOJI = re.compile('[\U0001F000-\U0001FAFF☀-➿⬀-⯿️‍⃣←-⇿]')
ARROWLESS_OK = set('→')   # a plain arrow is typography, not an emoji

def _strings(x, path=''):
    if isinstance(x, str): yield path, x
    elif isinstance(x, dict):
        for k, v in x.items(): yield from _strings(v, f'{path}.{k}')
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from _strings(v, f'{path}[{i}]')

class Spec(_Spec):
    MOOD_SFX = {   # palette per mood: (text-in, emphasis, reveal)
        'serious': ('whoosh_soft', 'hit_soft', 'sub_drop'),
        'energetic': ('swipe', 'impact', 'riser'),
    }
    def __init__(self, work, name, mood='serious'):
        super().__init__(work, name); self.mood = mood
    def add(self, ev, sfx=True):
        ty = ev['type']; inn, emph, rev = self.MOOD_SFX[self.mood]
        if ty in ('kinetic', 'stamp', 'callout', 'ecg', 'cine'):
            self.events.append(ev)
            if sfx:
                if ty == 'kinetic': self.fx(ev.get('sfx', inn if ev.get('anim') != 'slam' else emph), ev['t0'] - 0.05, ev.get('db', -16))
                elif ty == 'stamp': self.fx('impact' if self.mood == 'energetic' else 'hit_soft', ev['t0'], -12)
                elif ty == 'callout': self.fx('click', ev['t0'] + 0.1, -14)
                elif ty == 'ecg':
                    self.fx('whoosh_soft', ev['t0'] - 0.1, -18)
                    bpm = ev.get('bpm', 72); t = ev['t0'] + 0.4
                    while t < ev['t1'] - 0.2: self.fx('ecg_beep', t, -20); t += 60 / bpm
            return ev
        return super().add(ev, sfx)
    def kin(self, t0, t1, lines, x=540, y=300, **kw):
        if isinstance(lines, str): lines = [lines]
        return self.add({'type': 'kinetic', 't0': t0, 't1': t1, 'lines': lines, 'x': x, 'y': y, **kw})
    def behind(self, t0, t1, word, size=330, z=1.25, overlap=0.42, **kw):
        """Huge word behind the speaker: auto-placed so the head covers its lower part; camera held steady meanwhile."""
        import numpy as np
        face = np.array(json.load(open(f'{self.work}/{self.name}_face.json'))['face'])
        f0, f1 = int(t0 * 30000 / 1001), max(int(t0 * 30000 / 1001) + 1, int(t1 * 30000 / 1001))
        fx, fy, fh = np.median(face[f0:f1], axis=0)
        faceY = self.cam.get('faceY', 0.40); h = 1920 / z
        y0 = min(max(fy - faceY * h, 0), 1920 - h)
        out_fy = (fy - y0) * z; head_top = out_fy - 0.62 * fh * z
        cap = 0.70 * size                       # Bebas/Anton cap height
        ytop = head_top + overlap * cap - 0.83 * size   # glyph bottom sits `overlap` of cap-height below the head top
        self.cam['ranges'].append({'mode': 'zoom', 't0': t0 - 0.05, 't1': t1, 'z': z, 'tr': 0.25})
        kw.setdefault('font', 'bebas'); kw.setdefault('anim', 'track'); kw.setdefault('opacity', 0.97); kw.setdefault('color', '#FFC53D'); kw.setdefault('fit', 1010)
        return self.kin(t0, t1, [word], x=540, y=int(ytop), sizes=[size], layer='behind', **kw)
    def lint(self):
        bad = []
        for p, s in _strings({'events': self.events}):
            for ch in EMOJI.findall(s):
                if ch not in ARROWLESS_OK: bad.append((p, s))
        if bad:
            raise SystemExit('EMOJI in on-screen text (EDITING_RULES): ' + '; '.join(f'{p}: {s!r}' for p, s in bad[:8]))
        for ev in self.events:
            for it in ev.get('items', []):
                if 'icon' in it: raise SystemExit(f"icon field not allowed (use num/img): {it}")
    def save(self, *a, **k):
        self.lint()
        k.setdefault('extra', {})['overlay'] = 'v2'
        super().save(*a, **k)

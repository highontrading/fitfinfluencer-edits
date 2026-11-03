import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v5'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('health') - 0.05, 'y': 140, 'lines': ['*5 saal* lag gaye', 'ye samajhne mein'], 'sizes': [112, 72], 'hideCaps': True})
S.add({'type': 'title', 't0': T('health'), 't1': T('aap') - 0.1, 'y': 150, 'kicker': 'Health ka sabse bada problem', 'lines': ['~Information~ nahi', '*Implementation* hai'], 'sizes': [92, 92]})
S.punch(T('implementation'), 0.12, 0.8)
k0 = T('aap') - 0.1; k1 = TE('hai', T('cheez')) + 0.2
S.card(k0, k1)
S.add({'type': 'checklist', 't0': k0, 't1': k1, 'y': 170, 'title': 'Aap sab jaante ho', 'items': [
    {'t': T('khana'), 'text': 'Kya <span>khana hai</span>', 'mark': 'check'},
    {'t': T('exercise'), 'text': 'Exercise <span>karni hai</span>', 'mark': 'check'},
    {'t': T('stress'), 'text': 'Stress <span>kharab hai</span>', 'mark': 'check'}]})
S.add({'type': 'slam', 't0': T('par') - 0.05, 't1': TE('na', T('rukta')) + 0.2, 'y': 200, 'text': 'Par karte ho? 🤷', 'size': 112})
S.add({'type': 'title', 't0': T('kyunki') - 0.05, 't1': T('aaj') - 0.1, 'y': 170, 'lines': ['~Koi system nahi~', '~Koi sequence nahi~'], 'sizes': [88, 88]})
x0 = T('aaj') - 0.1; x1 = TE('karunga') + 0.4
S.card(x0, x1)
S.add({'type': 'checklist', 't0': x0, 't1': x1, 'y': 170, 'title': 'Bina system ke', 'items': [
    {'t': T('diet'), 'text': 'Diet <span>· aaj kiya, kal chhoda</span>', 'mark': 'x'},
    {'t': T('gym'), 'text': 'Gym <span>· 2–3 hafte, phir band</span>', 'mark': 'x'},
    {'t': T('fasting'), 'text': 'Fasting <span>· random din</span>', 'mark': 'x'},
    {'t': T('meditation'), 'text': 'Meditation <span>· "kal se"</span>', 'mark': 'x'}]})
S.add({'type': 'chips', 't0': T('koi', x1) - 0.1, 't1': T('jo', T('youtube')) - 0.1, 'y': 150, 'items': [
    {'t': T('information', x1), 'icon': 'ℹ️', 'text': 'Information ki kami?'},
    {'t': T('youtube'), 'icon': '▶️', 'text': 'YouTube pe *free* hai'}]})
d0 = T('jo', T('youtube')) - 0.1; d1 = TE('jaayengi') + 0.2
S.card(d0, d1)
S.add({'type': 'title', 't0': d0, 't1': T('aaj', d0) - 0.1, 'y': 280, 'kicker': 'Jo nahi hai', 'lines': ['*Personalized*', 'system'], 'sizes': [104, 104]})
xs = [190, 500, 810]
dn = [{'t': T(k, d0), 'x': x, 'y': 200, 'text': tx, 'sub': 'kya karna hai'} for x, (k, tx) in zip(xs, [('aaj', 'Aaj'), ('kal', 'Kal'), ('parson', 'Parson')])]
dn.append({'t': T('agar', d0), 'x': 500, 'y': 480, 'icon': '📅', 'text': 'Daily *system*', 'target': True})
dw = [{'t': T('kal', d0) - 0.3, 'd': 'M 300 200 L 390 200'}, {'t': T('parson') - 0.3, 'd': 'M 610 200 L 700 200'},
      {'t': T('agar', d0) - 0.3, 'd': 'M 500 260 L 500 420'}]
S.add({'type': 'flow', 't0': T('aaj', d0) - 0.1, 't1': d1, 'y': 170, 'w': 1000, 'h': 620, 'nodes': dn, 'wires': dw})
p0 = T('isi') - 0.1; p1 = TE('milega') + 0.2
S.card(p0, p1)
grid = [(260, 90), (740, 90), (260, 300), (740, 300)]
pn = [{'t': T(k, p0), 'x': x, 'y': y, 'num': i + 1, 'text': tx} for i, ((x, y), (k, tx)) in enumerate(zip(grid, [('fasting', 'Fasting'), ('diet', 'Diet'), ('exercise', 'Exercise'), ('meditation', 'Meditation')]))]
pn.append({'t': T('personalized', p0), 'x': 500, 'y': 540, 'icon': '🗓️', 'text': 'Personalized system', 'sub': 'Daily time table', 'target': True})
pw = [{'t': T('personalized', p0) - 0.35, 'd': f'M {x} {y + 45} C {x} 450, 500 420, 500 480'} for x, y in grid[2:]]
S.add({'type': 'title', 't0': p0, 't1': T('fasting', p0) - 0.05, 'y': 280, 'kicker': 'Isi liye maine banaya', 'lines': ['Ye *protocol*'], 'sizes': [120]})
S.add({'type': 'flow', 't0': T('fasting', p0) - 0.1, 't1': p1, 'y': 170, 'w': 1000, 'h': 640, 'nodes': pn, 'wires': pw})
S.add({'type': 'chips', 't0': T('ghar') - 0.1, 't1': TE('mein', T('duniya')) + 0.2, 'y': 150, 'items': [
    {'t': T('ghar'), 'icon': '🏠', 'text': 'Ghar se'}, {'t': T('gym', T('ghar')), 'icon': '🏋️', 'text': 'Gym se'},
    {'t': T('kahin'), 'icon': '🌍', 'text': 'Duniya mein *kahin se bhi*'}]})
r0 = T('mera') - 0.1; r1 = TE('se', T('change', T('psoriasis'))) + 0.25
S.card(r0, r1)
S.add({'type': 'stat', 't0': T('110') - 0.3, 't1': T('10%') - 0.05, 'y': 230, 'kicker': 'Mera result', 'fromText': '110 KG', 'from': 110, 'to': 85, 'unit': 'KG', 'label': 'Aaj', 'pill': '▼ 25 KG', 'dir': 'down', 'count': 1.3})
S.add({'type': 'stat', 't0': T('10%') - 0.05, 't1': T('maine', T('10%')) - 0.05, 'y': 230, 'kicker': 'Sirf 30 din mein', 'from': 0, 'to': 10, 'unit': '%', 'label': 'Body fat kam', 'dir': 'down', 'count': 1.0})
S.add({'type': 'checklist', 't0': T('maine', T('10%')) - 0.05, 't1': r1, 'y': 170, 'title': 'Sirf lifestyle change se', 'items': [
    {'t': T('wife'), 'text': 'Wife ka BP <span>· normal</span>', 'mark': 'check'},
    {'t': T('doctor'), 'text': 'Doctor ki <span>guidance mein</span>', 'mark': 'check'},
    {'t': T('psoriasis'), 'text': 'Mummy ka psoriasis <span>· behtar</span>', 'mark': 'check'}]})
S.add({'type': 'title', 't0': T('teen', r0) - 0.05, 't1': TE('gaye', T('fix')) + 0.2, 'y': 160, 'lines': ['*3 log* · 1 system', '3 problems ^fixed^'], 'sizes': [96, 80]})
S.punch(T('fix'), 0.10, 1.0)
S.add({'type': 'title', 't0': T('aur', T('fix')) - 0.05, 't1': T('but', T('fix')) - 0.08, 'y': 170, 'lines': ['*5 saal* ka system'], 'sizes': [104]})
S.add({'type': 'badge', 't0': T('but', T('fix')) - 0.05, 't1': T('link') - 0.1, 'y': 200, 'text': '1 Live webinar', 'sub': 'Saari cheezein *ek jagah*'})
cta = T('link') - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 1030, 'kicker': '🔴 Live webinar', 'title': 'Link<br>*neeche* hai', 'sub': 'Milte hain webinar mein!', 'button': 'ABHI JOIN KARO', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'health', r'information', r'implementation', r'exercise', r'stress', r'system', r'sequence', r'diet', r'gym', r'fasting', r'meditation',
                           r'youtube', r'free', r'personalized', r'protocol', r'daily', r'result', r'kilo', r'kg', r'fat', r'bp', r'psoriasis', r'webinar', r'link'])

B = S.broll
B(28890, T('5') - 0.1, T('health') - 0.05, off=1.0)
B(4911, T('information'), T('aap') - 0.1, off=1.0)
B(40529, T('khana'), T('aap', T('khana')) - 0.05)
B(52080, T('exercise'), T('aap', T('exercise')) - 0.05, off=4.0)
B(25592, T('stress'), k1 - 0.1, off=1.5)
B(372, T('par') - 0.05, T('kyunki') - 0.05, off=1.0)
B(3533, T('diet'), T('gym') - 0.05, off=1.0)
B(44432, T('gym'), T('fasting') - 0.05, off=1.0)
B(28897, T('fasting'), T('aur', T('fasting')) - 0.05, off=1.0)
B(51405, T('meditation'), x1 - 0.1, off=2.0)
B(4911, T('youtube') - 0.1, T('jo', T('youtube')) - 0.1, off=5.0)
B(50109, T('personalized'), T('aaj', d0) - 0.1, off=1.0)
B(42898, T('ghar'), T('gym', T('ghar')) - 0.05, off=1.0)
B(44438, T('gym', T('ghar')), T('kahin') - 0.05, off=0.5)
B(4629, T('kahin'), TE('mein', T('duniya')) + 0.15, off=1.0)
B(40349, T('mummy') - 0.05, r1 - 0.1, off=1.0)
B(39767, T('teen', r0) - 0.05, TE('gaye', T('fix')) + 0.15, off=1.0)
B(10443, T('but', T('fix')) - 0.05, T('link') - 0.12, off=1.0)
S.save(caps, cta_t=cta, hold=1.2)

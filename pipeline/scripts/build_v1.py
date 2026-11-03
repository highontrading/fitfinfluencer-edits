import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v1'); T, TE = S.T, S.TE
D = S.tl['dur']

# HOOK
S.add({'type': 'title', 't0': 0.05, 't1': T('but') - 0.05, 'y': 140, 'lines': ['Sab log health ko', '~complicate~ karte hain'], 'sizes': [74, 86], 'hideCaps': True})
t4 = T('4')
S.add({'type': 'title', 't0': T('asli') - 0.05, 't1': T('kyunki') - 0.1, 'y': 130, 'kicker': 'Asli secret', 'lines': ['Sirf *4 cheezein*'], 'sizes': [118]})
S.punch(t4, 0.12, 1.6)
S.add({'type': 'chips', 't0': T('supplement') - 0.15, 't1': TE('lega') + 0.25, 'y': 130, 'items': [
    {'t': T('supplement'), 'icon': '💊', 'text': 'Supplement market ~khatam~'},
    {'t': T('gym'), 'icon': '🏋️', 'text': 'Gym membership ~band~'}]})

# THE 4 THINGS — numbered grid, card layout
g0 = T('main') - 0.15
g1 = T('important', T('gym', T('lega'))) - 0.25          # "aur sabse important part"
t_fast, t_diet, t_ex = T('fasting'), T('diet'), T('exercise')
grid = [(260, 110), (740, 110), (260, 400), (740, 400)]
S.card(g0, TE('hongi') + 0.3)
S.add({'type': 'title', 't0': g0, 't1': t_fast - 0.05, 'y': 300, 'lines': ['Main batata hoon', '*4 cheezein*'], 'sizes': [76, 120]})
nodes = [
    {'t': t_fast, 'x': grid[0][0], 'y': grid[0][1], 'num': 1, 'text': 'Fasting', 'sub': 'Kab khana, kab nahi'},
    {'t': t_diet, 'x': grid[1][0], 'y': grid[1][1], 'num': 2, 'text': 'Diet', 'sub': 'Kya aur kitna'},
    {'t': t_ex, 'x': grid[2][0], 'y': grid[2][1], 'num': 3, 'text': 'Exercise', 'sub': 'Kaun si · kitni · kab'},
    {'t': T('meditation') - 0.05, 'x': grid[3][0], 'y': grid[3][1], 'num': 4, 'text': 'Mind', 'sub': 'Stress · sleep · anxiety'}]
S.add({'type': 'flow', 't0': t_fast - 0.1, 't1': T('ye', T('anxiety')) - 0.05, 'y': 170, 'w': 1000, 'h': 520, 'nodes': nodes, 'wires': []})
S.fx('ding', T('important', T('lega')) - 0.1, -18)
# foundation: mind holds up the other three
tf = T('ye', T('anxiety'))
base = [{'t': tf, 'x': 500, 'y': 470, 'text': '🧘 Mind · Stress · Sleep', 'target': True, 'sub': 'Sabse important foundation'}]
top = [{'t': T('pichhli') + 0.1 * i, 'x': x, 'y': 150, 'text': tx} for i, (x, tx) in enumerate([(190, 'Fasting'), (500, 'Diet'), (810, 'Exercise')])]
wires = [{'t': T('pichhli') + 0.1 * i + 0.1, 'd': f'M {x} 200 C {x} 300, 500 300, 500 395'} for i, x in enumerate([190, 500, 810])]
S.add({'type': 'flow', 't0': tf - 0.05, 't1': TE('hongi') + 0.3, 'y': 170, 'w': 1000, 'h': 600, 'nodes': base + top, 'wires': wires})

# SYSTEM
s0 = T('aur', TE('hongi')) - 0.1
S.add({'type': 'title', 't0': s0, 't1': T('main', T('system')) - 0.1, 'y': 170, 'kicker': '4 cheezein', 'lines': ['Ek *system* mein'], 'sizes': [120]})
S.punch(T('system'), 0.10, 1.2)

# RESULTS — card layout
r0 = T('main', T('system')) - 0.15
r1 = TE('hai', T('burn')) + 0.1
S.card(r0, r1)
S.add({'type': 'stat', 't0': T('110') - 0.25, 't1': T('85', T('kilo', T('85'))) - 0.1, 'y': 230, 'kicker': 'Mera transformation', 'fromText': '110 KG',
       'from': 110, 'to': 85, 'unit': 'KG', 'label': 'Aaj', 'pill': '▼ 25 KG', 'dir': 'down', 'count': 1.3})
c_now = T('15%'); c_then = T('26.9%')
S.add({'type': 'compare', 't0': c_now - 0.7, 't1': T('aur', c_then) - 0.05, 'y': 170, 'title': 'Body fat', 'max': 27, 'items': [
    {'t': c_then - 0.6, 'label': '30 din pehle', 'value': 26.9, 'dec': 1, 'unit': '%', 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': c_now, 'label': 'Aaj', 'value': 15, 'unit': '%', 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
# compare columns appear in speaking order: "aaj 15%" first, then "30 din pehle 26.9%"
S.events[-1]['items'][0]['t'] = c_then - 0.4
S.events[-1]['items'][1]['t'] = c_now
S.add({'type': 'stat', 't0': T('aur', c_then) - 0.05, 't1': r1, 'y': 230, 'kicker': 'Sirf 30 din mein', 'from': 0, 'to': 10, 'unit': 'KG',
       'label': 'Vajan kam', 'pill': '🔥 10 ki 10 kilo FAT', 'dir': 'down', 'count': 1.2})

# PERSONALIZED

S.add({'type': 'title', 't0': T('par', r1 - 0.5) - 0.05, 't1': T('personalized') - 0.1, 'y': 170, 'kicker': 'Sabse important baat', 'lines': ['Pata hai *kya* hai?'], 'sizes': [96]})
S.add({'type': 'slam', 't0': T('personalized') - 0.05, 't1': T('ek', T('personalized')) + 0.4, 'y': 210, 'text': '*Personalized*', 'size': 90, 'sub': 'System poora ka poora'})
S.punch(T('personalized'), 0.12, 1.0)
b0 = T('ek', T('personalized')) + 0.1
b1 = TE('system', T('liye', T('alagalag'))) + 0.3
S.card(b0, b1)
S.add({'type': 'title', 't0': b0 + 0.35, 't1': T('body', b0) - 0.35, 'y': 300, 'lines': ['Ek system', '~sab ke liye nahi~'], 'sizes': [100, 84]})
tb = T('body', b0) - 0.3; ts = T('toh', tb)
xs = [190, 500, 810]
bn = [{'t': tb + 0.15 * i, 'x': x, 'y': 130, 'text': f'🧍 Body {k}'} for i, (x, k) in enumerate(zip(xs, 'ABC'))]
sn = [{'t': T('system', ts) - 0.2 + 0.15 * i, 'x': x, 'y': 470, 'text': f'System {k}', 'target': True} for i, (x, k) in enumerate(zip(xs, 'ABC'))]
bw = [{'t': T('system', ts) - 0.45 + 0.15 * i, 'd': f'M {x} 180 L {x} 420'} for i, x in enumerate(xs)]
S.add({'type': 'flow', 't0': tb - 0.05, 't1': b1, 'y': 200, 'w': 1000, 'h': 600, 'nodes': bn + sn, 'wires': bw})
S.punch(T('seekhna'), 0.10, 1.4)

# WEBINAR
S.add({'type': 'badge', 't0': T('live') - 0.1, 't1': T('aapke') - 0.05, 'y': 200, 'text': 'Live webinar', 'sub': 'Poora system · *live*'})
S.add({'type': 'title', 't0': T('aapke') - 0.05, 't1': TE('loge') + 0.1, 'y': 170, 'kicker': 'Webinar mein', 'lines': ['Aapka *personalized*', 'system'], 'sizes': [84, 84]})

# CTA
cta = T('link') - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 1, 'y': 1030, 'kicker': '🔴 Live webinar', 'title': 'Abhi<br>*join* kariye',
       'sub': 'Milte hain webinar mein!', 'button': 'LINK NEECHE HAI', 'hideCaps': True})
S.punch(cta, 0.06, 99)

S.alt_zoom([1.1, 1.28])
S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'health', r'secret', r'fasting', r'diet', r'exercise', r'meditation', r'stress', r'sleep', r'anxiety', r'system',
                           r'kilo', r'fat', r'personalized', r'webinar', r'live', r'supplement', r'gym', r'important', r'join', r'link'])
S.save(caps, cta_t=cta, music_offset=9.6)

# ===== stock b-roll =====
B = S.broll
B(43850, T('unnecessarily'), T('but') - 0.05, off=1.0)
B(1776, T('supplement') - 0.05, T('aur', T('supplement')) - 0.05)
B(52080, T('gym', T('supplement')) - 0.05, TE('lega') + 0.15, off=2.0)
B(28886, T('fasting'), T('diet') - 0.05)
B(40531, T('diet'), T('exercise') - 0.05)
B(40248, T('exercise'), T('ghar') - 0.05, off=1.5)
B(42898, T('ghar'), T('aur', T('ghar')) - 0.05, off=1.0)
B(43786, T('meditation'), T('stress') - 0.02, xf=0.08)
B(4701, T('stress'), T('sleep') - 0.02, xf=0.08, off=1.5)
B(50931, T('sleep'), T('anxiety') - 0.02, xf=0.08, off=1.0)
B(25592, T('anxiety'), T('ye', T('anxiety')) - 0.02, xf=0.08, off=1.5)
B(44432, T('kareeban'), T('mera', T('kareeban')) - 0.05, off=1.0)
B(43737, T('body', b0) - 0.3, T('toh', T('body', b0)) - 0.05, off=0.5)
B(4834, T('live') - 0.1, T('aapke') - 0.05, off=1.0)
B(10443, T('aapke'), T('ye', T('aapke')) - 0.05, off=1.0)
S.save(caps, cta_t=cta, music_offset=9.6)

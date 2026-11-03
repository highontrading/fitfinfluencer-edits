import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v7'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('ye') - 0.05, 'y': 150, 'lines': ['Sunne mein', '*fake* lagega'], 'sizes': [84, 120], 'hideCaps': True})
S.add({'type': 'slam', 't0': T('100%') - 0.05, 't1': T('maine') - 0.1, 'y': 200, 'text': '*100%* sach', 'size': 140})
S.punch(T('100%'), 0.12, 0.8)
a0 = T('maine') - 0.1; a1 = TE('hai', T('aaya')) + 0.25
S.card(a0, a1)
S.add({'type': 'chips', 't0': a0, 't1': a1, 'y': 160, 'items': [
    {'t': T('25'), 'icon': '⚖️', 'text': '*25 KG* · 45 din mein'},
    {'t': T('wife'), 'icon': '❤️', 'text': 'Wife ka *BP normal*'},
    {'t': T('psoriasis'), 'icon': '🩺', 'text': 'Mummy ka *psoriasis* theek'},
    {'t': T('5000'), 'icon': '💧', 'text': '*5000+* logon ko water fast'}]})
S.add({'type': 'title', 't0': T('aap') - 0.05, 't1': T('lekin') - 0.08, 'y': 160, 'lines': ['Ye toh', '*sab bolte hain*'], 'sizes': [92, 92]})
S.add({'type': 'slam', 't0': T('proof') - 0.1, 't1': T('ek', T('proof')) - 0.05, 'y': 200, 'text': '*Proof* 📈', 'size': 150})
S.punch(T('proof'), 0.14, 0.8)
S.add({'type': 'stat', 't0': T('ek', T('proof')) - 0.05, 't1': T('aur', T('karayi')) - 0.05, 'y': 230, 'kicker': 'Ek nahi, teen nahi', 'from': 0, 'to': 5000, 'unit': '+', 'label': 'Logon ko water fasting', 'pill': '💧 Water fasting', 'dir': 'down', 'count': 1.6})
r0 = T('aur', T('karayi')) - 0.1; r1 = TE('hai', T('flare')) + 0.25
S.card(r0, r1)
S.add({'type': 'checklist', 't0': r0, 't1': r1, 'y': 170, 'title': 'Results', 'items': [
    {'t': T('insulin'), 'text': 'Insulin resistance <span>· theek</span>', 'mark': 'check'},
    {'t': T('weight'), 'text': 'Weight loss <span>· achha</span>', 'mark': 'check'},
    {'t': T('bp', r0), 'text': 'BP patients <span>· normal</span>', 'mark': 'check'},
    {'t': T('psoriasis', r0), 'text': 'Psoriasis flare <span>· kam</span>', 'mark': 'check'}]})
S.add({'type': 'title', 't0': T('aur', r1 - 0.3) - 0.05, 't1': T('toh', T('aayi')) - 0.08, 'y': 160, 'kicker': 'Sab kuch', 'lines': ['Sirf *lifestyle*', '*changes* se'], 'sizes': [96, 96]})
s0 = T('toh', T('aayi')) - 0.1; s1 = TE('ho', T('bana', T('tareeke'))) + 0.2
S.card(s0, s1)
S.add({'type': 'title', 't0': s0, 't1': T('kaise') - 0.1, 'y': 270, 'kicker': 'Aapko chahiye', 'lines': ['Ek *proper*', 'system'], 'sizes': [104, 104]})
xs = [(260, 90), (740, 90), (260, 300), (740, 300)]
sn = [{'t': T(k, s0, n), 'x': x, 'y': y, 'text': tx} for (x, y), (k, n, tx) in zip(xs, [('kaise', 1, 'Kaise khana'), ('kya', 1, 'Kya khana'), ('kaise', 2, 'Kaun si exercise'), ('kaun', 1, 'Kaise exercise')])]
sn[2]['text'], sn[3]['text'] = 'Kaise exercise', 'Kaun si exercise'
sn.append({'t': T('day', s0), 'x': 500, 'y': 520, 'icon': '📅', 'text': '*Day by day* plan', 'target': True})
sw = [{'t': T('day', s0) - 0.35, 'd': f'M {x} {y + 45} C {x} 450, 500 430, 500 470'} for x, y in xs[2:]]
S.add({'type': 'flow', 't0': T('kaise') - 0.1, 't1': s1, 'y': 170, 'w': 1000, 'h': 640, 'nodes': sn, 'wires': sw})
S.add({'type': 'slam', 't0': T('coincidence') - 0.1, 't1': TE('hai', T('system', T('coincidence'))) + 0.25, 'y': 200, 'text': '~Coincidence~ ✗<br>*System* ✓', 'size': 100})
S.punch(T('system', T('coincidence')), 0.12, 0.9)
S.add({'type': 'badge', 't0': T('aur', T('system', T('coincidence'))) - 0.05, 't1': T('link') - 0.1, 'y': 200, 'text': 'Live webinar', 'sub': 'Poora *system*'})
cta = T('link') - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 1030, 'kicker': '🔴 Live webinar', 'title': 'Abhi<br>*join* kariye', 'sub': 'Milte hain webinar mein!', 'button': 'LINK NEECHE HAI', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'fake', r'100%', r'kilo', r'bp', r'psoriasis', r'water', r'fast', r'fasting', r'proof', r'insulin', r'resistance', r'weight',
                           r'lifestyle', r'protocol', r'system', r'coincidence', r'webinar', r'link', r'exercise'])

B = S.broll
B(108, T('5000') - 0.1, a1 - 0.1, off=1.0)
B(2948, T('aap') - 0.05, T('lekin') - 0.08, off=1.0)
B(4437, T('ek', T('proof')) - 0.05, T('aur', T('karayi')) - 0.08, off=4.0)
B(4733, T('insulin'), T('in', T('insulin')) - 0.05, off=1.0)
B(44432, T('weight'), T('bahut', T('weight')) - 0.05, off=1.0)
B(40349, T('psoriasis', r0) - 0.2, r1 - 0.1, off=1.0)
B(4546, T('aur', r1 - 0.3), T('toh', T('aayi')) - 0.08, off=1.0)
B(50109, T('protocol', s0), T('proper') - 0.05, off=0.5)
B(3795, T('kaise', s0), T('kaise', s0, 2) - 0.05, off=1.0)
B(40248, T('exercise', s0), T('ye', T('exercise', s0)) - 0.05, off=1.5)
B(4834, T('aur', T('system', T('coincidence'))) - 0.05, T('link') - 0.12, off=1.0)
S.save(caps, cta_t=cta, hold=1.2)

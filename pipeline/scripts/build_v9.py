import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v9'); T, TE = S.T, S.TE
D = S.tl['dur']
c1 = TE('hai', T('15.6%')) + 0.25
S.card(0.0, c1)
S.add({'type': 'compare', 't0': 0.05, 't1': c1, 'y': 170, 'title': 'Mera body fat', 'max': 27, 'items': [
    {'t': T('26.9%') - 0.2, 'label': '30 din pehle', 'value': 26.9, 'dec': 1, 'unit': '%', 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('15.5') - 0.1, 'label': 'Aaj', 'value': 15.5, 'dec': 1, 'unit': '%', 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
m0 = T('aur') - 0.1; m1 = TE('hai', T('workout')) + 0.25
S.card(m0, m1)
S.add({'type': 'checklist', 't0': m0, 't1': m1, 'y': 140, 'title': 'Kaise kiya', 'items': [
    {'t': T('water'), 'text': 'Water fasting', 'mark': 'check'},
    {'t': T('intermittent'), 'text': 'Intermittent fasting', 'mark': 'check'},
    {'t': T('diet'), 'text': 'Achhi diet', 'mark': 'check'},
    {'t': T('exercise'), 'text': 'Achhi exercise', 'mark': 'check'},
    {'t': T('workout'), 'text': 'Khoob saara workout', 'mark': 'check'}]})
S.add({'type': 'title', 't0': T('aap', T('workout')) - 0.05, 't1': T('mindset') - 0.08, 'y': 170, 'lines': ['Aap bhi', '*kar sakte ho*'], 'sizes': [84, 112]})
S.add({'type': 'slam', 't0': T('mindset'), 't1': T('agar', T('mindset')) - 0.05, 'y': 200, 'text': '*Mindset* 🧠', 'size': 140, 'sub': 'Ka game hai'})
S.punch(T('mindset'), 0.14, 0.8)
f0 = T('agar', T('mindset')) - 0.1; f1 = TE('protocol') + 0.3
S.card(f0, f1)
fn = [{'t': T('soch'), 'x': 260, 'y': 90, 'icon': '✅', 'text': 'Soch liya', 'sub': 'Toh kar loge'},
      {'t': T('kharab'), 'x': 740, 'y': 90, 'icon': '❌', 'text': 'Mindset ~kharab~', 'sub': 'Toh nahi kar paoge'},
      {'t': T('protocol') - 0.1, 'x': 500, 'y': 420, 'icon': '🧭', 'text': 'Mindset = *Protocol*', 'target': True}]
fw = [{'t': T('banane') - 0.2, 'd': 'M 260 150 C 260 300, 500 300, 500 360'}, {'t': T('banane') - 0.2, 'd': 'M 740 150 C 740 300, 500 300, 500 360'}]
S.add({'type': 'flow', 't0': f0, 't1': f1, 'y': 170, 'w': 1000, 'h': 600, 'nodes': fn, 'wires': fw})
S.add({'type': 'title', 't0': T('toh', T('protocol')) - 0.05, 't1': T('aur', T('bana')) - 0.08, 'y': 170, 'kicker': 'Aap logon ke liye', 'lines': ['Protocol *ready* hai'], 'sizes': [104]})
S.add({'type': 'badge', 't0': T('aur', T('bana')) - 0.05, 't1': T('aap', T('discuss')) - 0.1, 'y': 200, 'text': 'Live webinar', 'sub': 'Saari cheezein *discuss* karunga'})
cta = T('aap', T('discuss')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 1030, 'kicker': '🔴 Live webinar', 'title': '*Turant*<br>join karo', 'sub': 'Milte hain webinar mein!', 'button': 'LINK NEECHE HAI', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.08, 1.24]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.0, 'faceY': 0.45}
caps = S.captions(hl_pats=[r'body', r'fat', r'water', r'fasting', r'intermittent', r'diet', r'exercise', r'workout', r'mindset', r'protocol', r'webinar', r'join', r'link'])

B = S.broll
B(108, T('water'), T('intermittent') - 0.05, off=1.0)
B(28886, T('intermittent'), T('achhi') - 0.05)
B(40531, T('diet'), T('achhi', T('diet')) - 0.05)
B(52080, T('exercise'), T('khoob') - 0.05, off=4.0)
B(40248, T('khoob'), m1 - 0.1, off=1.5)
B(34566, T('aap', T('workout')) - 0.05, T('mindset') - 0.08, off=1.0)
B(1086, T('mindset') - 0.05, T('agar', T('mindset')) - 0.08, off=2.0)
B(10443, T('aur', T('bana')) - 0.05, cta - 0.08, off=1.0)
S.save(caps, cta_t=cta, hold=1.2)

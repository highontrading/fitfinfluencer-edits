import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v27', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
CM = '../stock/commons/'
# ---------------- hook
Bh(0.05, T('kaun') - 0.05, 'SALT', size=380, font='anton', anim='slam')
K(0.15, T('kaun') - 0.05, ['A COMMENT ASKED:'], x=540, y=1540, sizes=[72], font='serif', anim='type')
K(T('kaun') - 0.03, T('sab') - 0.05, ['WHICH SALT IS BEST', 'FOR *BLOOD PRESSURE?*'], x=540, y=300, sizes=[80, 96], anim='slam')
K(T('sab') - 0.03, T('kisi') - 0.05, ['"EAT LESS SALT"'], x=70, y=300, align='left', sizes=[110], anim='wipe')
K(T('kisi') - 0.03, T('jo', T('bhai')) - 0.05, ['BUT WHICH', '*ALTERNATIVE?*'], x=1010, y=300, align='right', sizes=[90, 120], anim='slam')
K(T('jo', T('bhai')) - 0.03, T('but') - 0.05, ['ONE THAT WORKS.', '*PROVEN BY SCIENCE.*'], x=540, y=300, sizes=[84, 96], anim='rise', stagger=0.6)
K(T('but') - 0.03, T('kuch', T('bana')) - 0.05, ['NOT FOR', '~EVERYONE~'], x=70, y=300, align='left', sizes=[110, 140], anim='slam')
S.add({'type': 'stamp', 't0': T('dangerous') - 0.1, 't1': T('ab') - 0.05, 'y': 1150, 'text': 'DANGEROUS<br>FOR SOME', 'rot': -7, 'size': 80}); S.punch(T('dangerous'), 0.14, 0.7)
K(T('ab') - 0.03, T('normal') - 0.05, ['TODAY:', '^LOW SODIUM SALT^'], x=540, y=300, sizes=[80, 120], anim='slam')
# ---------------- mechanism: normal salt
m0 = T('normal') - 0.08; m1 = T('usmein') - 0.08
S.card(m0, m1)
mn = [{'t': T('normal') + 0.2, 'x': 500, 'y': 60, 'text': 'Normal salt = *NaCl*'}, {'t': T('blood') - 0.1, 'x': 500, 'y': 215, 'text': 'Raises *blood volume*'},
      {'t': T('rok') - 0.4, 'x': 500, 'y': 370, 'text': 'Sodium *holds water*'}, {'t': T('vessels'), 'x': 500, 'y': 530, 'text': '~Pressure on vessels~', 'target': True}]
mw = [{'t': T('blood') - 0.4, 'd': 'M 500 105 L 500 165'}, {'t': T('rok') - 0.7, 'd': 'M 500 260 L 500 320'}, {'t': T('vessels') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': m0, 't1': T('toh', T('volume', T('vessels'))) - 0.05, 'y': 140, 'w': 1000, 'h': 640, 'nodes': mn, 'wires': mw})
S.add({'type': 'badge', 't0': T('toh', T('volume', T('vessels'))) - 0.05, 't1': m1, 'y': 300, 'text': 'So what is *low sodium salt?*'})
# ---------------- low sodium salt
l0 = m1 + 0.02; l1 = T('potassium', T('typically', T('kcl'))) + 0.6
K(l0 + 0.02, T('typically') - 0.05, ['SODIUM PARTLY', 'REPLACED BY', '*POTASSIUM CHLORIDE (KCl)*'], x=540, y=280, sizes=[70, 70, 80], anim='rise', stagger=0.5)
S.card(T('typically') - 0.08, T('potassium', T('typically')) + 1.0)
S.add({'type': 'compare', 't0': T('typically') - 0.08, 't1': T('potassium', T('typically')) + 1.0, 'y': 170, 'title': 'Typical low sodium salt', 'max': 75, 'items': [
    {'t': T('75%') - 0.1, 'label': 'Sodium', 'unit': '%', 'value': 75, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('25%') - 0.1, 'label': 'Potassium', 'unit': '%', 'value': 25, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
# ---------------- potassium mechanism
p0 = T('potassium', T('25%')) + 1.02; p1 = T('ab', T('gir')) - 0.08
S.card(p0, p1)
S.add({'type': 'photo', 't0': p0, 't1': T('kidney', p0) - 0.05, 'x': 140, 'y': 160, 'w': 800, 'h': 680, 'src': CM + 'Blausen_0592_KidneyAnatomy_01.png', 'fit': 'contain', 'bg': '#ffffff', 'label': 'Kidney', 'credit': 'Blausen Medical, CC BY 3.0'})
S.add({'type': 'chain', 't0': T('kidney', p0) - 0.05, 't1': p1, 'y': 150, 'title': 'What potassium does', 'show': 4, 'items': [
    {'t': T('kidney', p0), 'text': 'Signals the *kidney*'}, {'t': T('flush'), 'text': 'Flush the *sodium* out', 'st': 'down', 'stc': 'green'},
    {'t': T('blood', T('flush')), 'text': 'Blood volume *drops*', 'st': 'down', 'stc': 'green'}, {'t': T('gir'), 'text': '^Blood pressure falls^', 'st': 'down', 'stc': 'green'}]})
S.fx('ding', T('gir'), -14)
# ---------------- SSaSS trial
s0 = T('ab', T('gir')) - 0.05
K(s0, T('isko', s0) - 0.05, ['A HUGE TRIAL.', '*WORLD FAMOUS.*'], x=540, y=300, sizes=[96, 110], anim='rise', stagger=0.8)
Bh(T('isko', s0) - 0.03, T('salt', T('ssass')) - 0.05, 'SSaSS', size=380, font='anton', anim='slam', color=Y)
K(T('salt', T('ssass')) - 0.03, T('20000') - 0.05, ['SALT SUBSTITUTE', 'AND STROKE STUDY'], x=540, y=300, sizes=[84, 84], font='serif', anim='type')
S.add({'type': 'stat', 't0': T('20000') - 0.05, 't1': T('stroke', T('roughly')) - 0.05, 'y': 260, 'kicker': 'People in the trial', 'from': 0, 'to': 20000, 'unit': '', 'label': 'Salt swapped, *no extra salt added*', 'dir': 'up', 'count': 1.0})
r0 = T('stroke', T('roughly')) - 0.08; r1 = T('ab', T('12%')) - 0.08
S.card(r0, r1)
S.add({'type': 'compare', 't0': r0, 't1': r1, 'y': 170, 'title': 'Risk drop with the salt swap', 'max': 14, 'items': [
    {'t': T('14%') - 0.1, 'label': 'Stroke', 'unit': '%', 'value': 14, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('12%') - 0.1, 'label': 'Death', 'unit': '%', 'value': 12, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
# ---------------- who must NOT
w0 = T('ab', T('12%')) - 0.05
K(w0, T('kidney', w0) - 0.05, ['WHO SHOULD', '~NOT~ USE IT'], x=540, y=300, sizes=[100, 140], anim='slam'); S.punch(T('nahi', w0), 0.12, 0.7)
k0 = T('kidney', w0) - 0.08; k1 = T('number', T('rhythm')) - 0.08
S.card(k0, k1)
S.add({'type': 'chain', 't0': k0, 't1': k1, 'y': 150, 'title': '1. Kidney disease', 'show': 4, 'items': [
    {'t': T('flush', k0), 'text': 'Kidneys flush out *potassium*'}, {'t': T('weak'), 'text': 'Weak kidneys: potassium *builds up*', 'st': 'up', 'stc': 'red'},
    {'t': T('hyperkalemia'), 'text': '~Hyperkalemia~', 'st': 'no', 'stc': 'red'}, {'t': T('lethal'), 'text': 'More *lethal* than high BP', 'st': 'up', 'stc': 'red'},
    {'t': T('rhythm'), 'text': '~Heart rhythm can break~', 'st': 'no', 'stc': 'red'}]})
S.fx('sub_drop', T('hyperkalemia'), -12)
n0 = k1 + 0.02; n1 = T('number', T('danger')) - 0.08
S.card(n0, n1)
S.add({'type': 'checklist', 't0': n0, 't1': n1, 'y': 150, 'title': '2. People on these medicines', 'items': [
    {'t': T('ace'), 'text': 'ACE inhibitors', 'mark': 'x'}, {'t': T('arbs'), 'text': 'ARBs', 'mark': 'x'},
    {'t': T('potassiumsparing'), 'text': 'Potassium-sparing diuretics', 'mark': 'x'}, {'t': T('badha'), 'text': 'They already *raise potassium*', 'mark': 'x'}]})
o0 = n1 + 0.02
K(o0, T('baaki') - 0.05, ['3. ELDERLY PATIENTS', 'WITH *WEAK KIDNEYS*'], x=540, y=300, sizes=[84, 96], anim='rise', stagger=0.6)
S.add({'type': 'stamp', 't0': T('high', o0) - 0.1, 't1': T('baaki') - 0.05, 'y': 1160, 'text': 'NO HIGH-<br>POTASSIUM SALT', 'rot': -6, 'size': 70})
# ---------------- everyone else
K(T('baaki') - 0.03, T('2025') - 0.05, ['EVERYONE ELSE:', 'A *SIMPLE, PROVEN SWAP*'], x=540, y=300, sizes=[80, 100], anim='rise', stagger=0.5)
S.add({'type': 'badge', 't0': T('2025') - 0.05, 't1': T('but', T('2025')) - 0.05, 'y': 260, 'text': 'WHO, 2025', 'sub': 'Recommends *low sodium salt*'})
K(T('pehle') - 0.05, T('aur', T('consult')) - 0.05, ['ASK YOUR', '*DOCTOR FIRST*'], x=540, y=330, sizes=[90, 120], anim='slam')
import os
DOC = CM + 'Female_doctor_showing_blood_pressure_monitor_closeup.png'
if os.path.exists(DOC):   # run from scripts/, same relative root as render/
    S.card(T('aur', T('consult')) - 0.05, T('sawaal') - 0.05)
    S.add({'type': 'photo', 't0': T('aur', T('consult')) - 0.05, 't1': T('sawaal') - 0.05, 'x': 140, 'y': 180, 'w': 800, 'h': 640, 'src': DOC, 'fit': 'cover', 'label': 'On BP medicine? Ask first', 'credit': 'Shixart1985, CC BY 2.0'})
else:
    B(2863, T('aur', T('consult')) - 0.05, T('sawaal') - 0.05, off=1.0)
    K(T('bp', T('consult')) - 0.05, T('sawaal') - 0.05, ['ON BP MEDICINE?', '*ASK FIRST*'], x=540, y=330, sizes=[84, 110], anim='rise')
K(T('sawaal') - 0.03, T('mera') - 0.05, ['CHANGING SALT MATTERS.', 'UNDERSTAND *THE SCIENCE* FIRST.'], x=540, y=300, sizes=[70, 70], anim='rise', stagger=0.8)
cta = T('mera') - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Know someone with high BP?', 'title': 'Send this<br>*to them*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'SHARE', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'namak', r'bp', r'salt', r'sodium', r'potassium', r'chloride', r'nacl', r'kcl', r'dangerous', r'blood', r'volume', r'pressure',
                           r'vessels', r'kidney', r'flush', r'trial', r'ssass', r'stroke', r'death', r'risk', r'14%', r'12%', r'75%', r'25%', r'20000',
                           r'hyperkalemia', r'lethal', r'heart', r'rhythm', r'ace', r'arbs', r'diuretics', r'who', r'doctor', r'science'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

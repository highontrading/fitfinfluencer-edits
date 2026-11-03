import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v20', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'
K = S.kin; Bh = S.behind
# --- hook: myth
K(0.05, T('pata') - 0.05, ['YOU WERE TAUGHT', 'THE *OPPOSITE*'], x=70, y=260, align='left', sizes=[84, 130], font='bebas', anim='wipe')
Bh(T('breakfast') - 0.1, T('aur') - 0.05, 'BREAKFAST', size=300)
K(T('most') - 0.05, T('aur') - 0.05, ['= THE MOST IMPORTANT MEAL?'], x=540, y=1600, sizes=[60], font='oswald', anim='rise')
S.add({'type': 'stamp', 't0': T('jhooth') - 0.1, 't1': T('aapko') - 0.05, 'y': 1120, 'text': 'A LIE', 'rot': -9}); S.punch(T('jhooth'), 0.14, 0.7)
q1 = T('kisne', T('scientist')) - 0.05
K(T('mummy') - 0.05, q1, ['PARENTS?'], x=70, y=330, align='left', sizes=[92], anim='slam')
K(T('dada') - 0.05, q1, ['GRANDPARENTS?'], x=1010, y=560, align='right', sizes=[92], anim='slam')
K(T('doctor') - 0.05, q1, ['A DOCTOR?'], x=70, y=790, align='left', sizes=[92], anim='slam')
K(T('scientist') - 0.05, q1, ['A SCIENTIST?'], x=1010, y=1020, align='right', sizes=[92], anim='slam')
K(q1 + 0.02, T('1944') - 0.08, ['WHO', 'TOLD YOU?'], x=540, y=430, sizes=[160, 116], font='anton', anim='slam'); S.punch(q1 + 0.05, 0.12, 0.6)
# --- 1944 flashback
c0 = T('1944') - 0.1; c1 = T('kyun', T('day')) - 0.05
S.add({'type': 'cine', 't0': c0, 't1': c1, 'h': 160}); S.fx('tension', c0 - 1.6, -14)
Bh(T('1944') - 0.05, T('cereal') - 0.12, '1944', size=380, font='anton', anim='slam')
K(T('cereal') - 0.05, T('isko') - 0.05, ['A *CEREAL COMPANY*'], x=540, y=1560, sizes=[74], font='oswald', anim='wipe')
K(T('marketing') - 0.05, T('ki', T('tha')) - 0.05, ['A MARKETING', 'CAMPAIGN'], x=1010, y=300, align='right', sizes=[120, 120], anim='rise', color='#FFC53D')
K(T('ki', T('tha')) - 0.05, c1, ['"BREAKFAST IS THE MOST', 'IMPORTANT MEAL OF THE DAY"'], x=540, y=320, sizes=[62, 62], font='serif', anim='type')
# --- the logic
K(T('raat') - 0.1, T('toh', T('raat')) - 0.05, ['FASTING', 'ALL NIGHT'], x=70, y=300, align='left', sizes=[116, 116], anim='wipe')
K(T('breakfast', T('raat')) - 0.05, T('kyun', T('karna')) - 0.05, ['SO BREAKFAST', 'IS *ESSENTIAL*?'], x=1010, y=300, align='right', sizes=[90, 110], anim='rise')
K(T('kyunki', T('kyun', T('karna'))) - 0.05, T('harvard') - 0.08, ['SO THEY COULD', 'SELL *MORE CEREAL*'], x=540, y=340, sizes=[82, 116], anim='rise')
# --- authority
a1 = T('aur', T('anti.*')) - 0.05
S.add({'type': 'callout', 't0': T('harvard') - 0.05, 't1': T('25') - 0.1, 'px': 640, 'py': 640, 'lx': 980, 'ly': 470, 'text': 'HARVARD PROFESSOR'})
K(T('david') - 0.05, a1, ['DR. DAVID SINCLAIR'], x=70, y=1600, align='left', sizes=[66], font='oswald', anim='wipe')
K(T('25') - 0.05, a1, ['25 YEARS OF', 'ANTI-AGING RESEARCH'], x=1010, y=280, align='right', sizes=[74, 74], font='oswald', anim='rise')
K(T('kehna') - 0.05, T('not') - 0.12, ['HIS VERDICT:'], x=540, y=330, sizes=[90], anim='track')
Bh(T('not') - 0.1, T('david', T('not')) - 0.05, 'NOT', size=430, font='anton', anim='slam', color=R)
K(T('not') + 0.1, T('david', T('not')) - 0.05, ['THE MOST IMPORTANT MEAL'], x=540, y=1600, sizes=[60], font='oswald', anim='rise'); S.punch(T('not'), 0.12, 0.8)
# --- mTOR
m0 = T('david', T('not')) - 0.05
K(m0, T('teen') - 0.05, ['ALWAYS EATING?'], x=70, y=300, align='left', sizes=[110], anim='slam')
S.add({'type': 'chips', 't0': T('teen') - 0.05, 't1': T('pathway') - 0.08, 'y': 200, 'items': [
    {'t': T('teen'), 'text': 'Breakfast'}, {'t': T('chaar'), 'text': 'Lunch'}, {'t': T('meal', T('chaar')), 'text': 'Dinner'}, {'t': T('snacks'), 'text': 'Snacks in between'}]})
K(T('pathway') - 0.05, T('mtor') - 0.08, ['A PATHWAY', 'SWITCHES *ON*'], x=1010, y=300, align='right', sizes=[96, 120], anim='rise')
Bh(T('mtor') - 0.05, T('aur', T('rapamycin')) - 0.48, 'mTOR', size=420, font='inter', anim='slam', color=R, case='none')
K(T('mechanistic') - 0.05, T('aur', T('rapamycin')) - 0.05, ['MECHANISTIC TARGET OF RAPAMYCIN'], x=540, y=1600, sizes=[52], font='mono', anim='type')
# --- growth signal: cells divide, DNA copies break
g0 = T('aur', T('rapamycin')) - 0.1; g1 = TE('hai', T('fast', T('aging'))) + 0.25
S.card(g0, g1)
K(g0, T('cells') - 0.05, ['A *GROWTH* SIGNAL'], x=540, y=330, sizes=[120], anim='slam')
S.add({'type': 'cells', 't0': T('cells') - 0.1, 't1': T('dna') - 0.05, 'x': 40, 'y': 160, 'w': 1000, 'h': 640, 'n0': 8, 'rate': 0.07, 'max': 36})
K(T('cells') - 0.05, T('dna') - 0.05, ['CELLS KEEP DIVIDING'], x=540, y=840, sizes=[64], font='oswald', anim='wipe')
S.add({'type': 'dna', 't0': T('dna') - 0.05, 't1': T('epigenome') - 0.05, 'x': 40, 'y': 260, 'w': 1000, 'h': 420, 'breakT': T('breaks'), 'label': 'DNA COPIED AGAIN AND AGAIN'})
K(T('breaks') - 0.05, T('epigenome') - 0.05, ['*BREAKS* IN EVERY COPY'], x=540, y=160, sizes=[80], anim='slam', color=R)
K(T('epigenome') - 0.05, T('toh', T('bigda')) - 0.05, ['EPIGENOME', '~DAMAGED~'], x=540, y=280, sizes=[110, 140], anim='slam')
K(T('toh', T('bigda')) - 0.03, g1, ['AGING', 'SPEEDS UP'], x=540, y=280, sizes=[150, 110], anim='slam', color=R); S.fx('sub_drop', T('aging') - 0.05, -12)
# --- AMPK
p0 = T('lekin', g1 - 0.3) - 0.05
K(p0, T('doosra') - 0.08, ['BUT WHEN', 'YOU *FAST*'], x=70, y=300, align='left', sizes=[100, 130], anim='wipe')
K(T('doosra') - 0.05, T('ampk') - 0.1, ['A SECOND', 'PATHWAY'], x=1010, y=300, align='right', sizes=[100, 100], anim='rise')
Bh(T('ampk') - 0.05, T('ab', T('kinase')) - 0.48, 'AMPK', size=420, font='anton', anim='slam', color=G)
K(T('activated') - 0.05, T('ab', T('kinase')) - 0.05, ['ACTIVATED PROTEIN KINASE'], x=540, y=1600, sizes=[56], font='mono', anim='type')
f0 = T('ab', T('kinase')) - 0.1; f1 = TE('hai', T('slow')) + 0.25
S.card(f0, f1)
fn = [{'t': f0 + 0.1, 'x': 500, 'y': 60, 'text': '*AMPK* on'},
      {'t': T('sirtuins'), 'x': 500, 'y': 215, 'text': 'Sirtuins', 'sub': '7 anti-aging enzymes'},
      {'t': T('repair'), 'x': 500, 'y': 380, 'text': 'DNA repair + stable epigenome'},
      {'t': T('slow') - 0.3, 'x': 500, 'y': 540, 'text': 'Aging *slows down*', 'target': True}]
fw = [{'t': T('sirtuins') - 0.3, 'd': 'M 500 105 L 500 160'}, {'t': T('repair') - 0.3, 'd': 'M 500 275 L 500 335'}, {'t': T('slow') - 0.6, 'd': 'M 500 425 L 500 490'}]
S.add({'type': 'flow', 't0': f0, 't1': f1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': fn, 'wires': fw})
# --- the rule
r0 = T('matlab', f1 - 0.3) - 0.05
K(r0, T('aur', T('se', T('boodhi'))) - 0.05, ['EVERY MEAL', '= ~AGING~'], x=70, y=300, align='left', sizes=[110, 130], anim='slam')
K(T('aur', T('se', T('boodhi'))) - 0.03, T('zyada', T('paayegi')) - 0.05, ['EVERY FAST', '= ^LONGER LIFE^'], x=1010, y=300, align='right', sizes=[110, 120], anim='slam')
K(T('zyada', T('paayegi')) - 0.03, T('meri') - 0.05, ['LESS EATING.', '*LESS AGING.*'], x=540, y=300, sizes=[100, 130], anim='track')
# --- my mistake
Bh(T('meri') - 0.05, T('5') - 0.08, 'MISTAKE', size=330, font='anton', anim='slam', color=R)
K(T('meri') - 0.05, T('5') - 0.08, ['MY BIGGEST'], x=540, y=1580, sizes=[72], font='oswald', anim='rise')
K(T('5') - 0.05, T('5', T('baar', T('magar'))) - 0.05, ['5-6 SMALL MEALS', 'EVERY DAY'], x=70, y=300, align='left', sizes=[100, 100], anim='wipe')
K(T('5', T('baar', T('magar'))) - 0.03, T('but', T('hoga')) - 0.05, ['"EATING OFTEN', 'BOOSTS METABOLISM"'], x=540, y=320, sizes=[70, 70], font='serif', anim='type')
S.add({'type': 'stamp', 't0': T('laga') - 0.1, 't1': T('but', T('hoga')) - 0.05, 'y': 1120, 'text': 'MYTH', 'rot': -8})
K(T('but', T('hoga')) - 0.03, T('jab', T('jhooth', T('hoga'))) - 0.05, ['A COMPLETE', '~LIE~'], x=540, y=300, sizes=[110, 180], anim='slam'); S.punch(T('jhooth', T('hoga')), 0.12, 0.7)
# --- fasting windows
Bh(T('16.*') - 0.05, T('phir', T('16.*')) - 0.05, '16:8', size=400, font='anton', anim='slam')
K(T('16.*') + 0.2, T('phir', T('16.*')) - 0.05, ['INTERMITTENT FASTING'], x=540, y=1600, sizes=[60], font='oswald', anim='rise')
Bh(T('18.*') - 0.05, T('toh', T('18.*')) - 0.02, '18:6', size=400, font='anton', anim='slam', color=G)
# --- autophagy
u0 = T('toh', T('18.*')) + 0.45; u1 = T('110') - 0.08
S.card(u0, u1)
K(u0, T('jitni') - 0.05, ['TAKE CARE OF', 'YOUR BODY'], x=540, y=300, sizes=[110, 110], anim='rise')
S.add({'type': 'cells', 't0': T('jitni') - 0.1, 't1': T('isi', T('karegi')) - 0.05, 'x': 40, 'y': 260, 'w': 1000, 'h': 560, 'n0': 14, 'rate': 0.5, 'max': 18, 'color': '80,200,255'})
K(T('jitni') - 0.05, T('isi', T('karegi')) - 0.05, ['EMPTY STOMACH', '= *REPAIR MODE*'], x=540, y=150, sizes=[84, 100], anim='wipe')
K(T('isi', T('karegi')) - 0.03, u1, ['AUTOPHAGY'], x=540, y=300, sizes=[190], font='anton', anim='slam', color=G)
# --- proof: me
S.add({'type': 'stat', 't0': T('110') - 0.05, 't1': T('biological') - 0.08, 'y': 260, 'kicker': 'My own body', 'fromText': '110 KG', 'from': 110, 'to': 85, 'unit': 'KG', 'label': 'Weight now', 'pill': 'Down 25 kg', 'dir': 'down', 'count': 1.2})
b0 = T('biological') - 0.1; b1 = T('11') - 0.45
S.card(b0, b1)
S.add({'type': 'compare', 't0': b0, 't1': b1, 'y': 170, 'title': 'My age', 'max': 35, 'items': [
    {'t': T('actual'), 'label': 'Passport age', 'text': '35', 'value': 35, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('biological') + 0.3, 'label': 'Biological age', 'text': '23-24', 'value': 24, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
Bh(T('11') - 0.05, T('fasting', T('difference')) - 0.48, '11 YEARS', size=300, font='anton', anim='slam', color=G)
K(T('11') + 0.15, T('fasting', T('difference')) - 0.05, ['YOUNGER THAN MY PASSPORT AGE'], x=540, y=1600, sizes=[52], font='oswald', anim='rise')
# --- protocol
k0 = T('fasting', T('difference')) - 0.1; k1 = TE('step', T('by')) + 0.3
S.card(k0, k1)
S.add({'type': 'checklist', 't0': k0, 't1': k1, 'y': 150, 'title': 'The complete fasting protocol', 'items': [
    {'t': T('kab', k0), 'text': 'When to eat', 'mark': 'check'}, {'t': T('kab', T('kab', k0) + 0.2), 'text': 'When not to eat', 'mark': 'check'},
    {'t': T('kitna', k0), 'text': 'How much to eat', 'mark': 'check'}, {'t': T('kya', k0), 'text': 'What to eat', 'mark': 'check'},
    {'t': T('kaise', k0), 'text': 'How to start', 'mark': 'check'}]})
n0 = T('main', k1 - 0.3) - 0.05
K(n0, T('main', n0 + 0.5) - 0.05, ["I'M NOT SAYING", '~STOP EATING~'], x=70, y=300, align='left', sizes=[80, 120], anim='wipe')
K(T('main', n0 + 0.5) - 0.03, T('but', T('peejiye')) - 0.05, ["OR", '~ONLY DRINK WATER~'], x=1010, y=300, align='right', sizes=[80, 110], anim='wipe')
K(T('but', T('peejiye')) - 0.03, T('toh', T('banta')) - 0.05, ['BUT TRY', '*WATER FASTING*'], x=540, y=300, sizes=[100, 140], anim='slam')
cta = T('toh', T('banta')) - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'You are watching', 'title': 'Fit<span class="acc">Finfluencer</span>', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW FOR MORE', 'hideCaps': True})
S.punch(cta, 0.06, 99)
# --- camera
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'breakfast', r'jhooth', r'doctor', r'scientist', r'1944', r'cereal', r'marketing', r'campaign', r'fast', r'harvard', r'sinclair', r'research',
                           r'not', r'mtor', r'growth', r'cells', r'divide', r'dna', r'breaks', r'epigenome', r'aging', r'ampk', r'sirtuins', r'enzymes', r'repair', r'boodhi',
                           r'galti', r'metabolism', r'fasting', r'intermittent', r'autophagy', r'biological', r'age', r'protocol', r'water'])
B = S.broll
B(4779, T('doctor') - 0.1, T('scientist') - 0.08, off=2.0)
B(4767, T('scientist') - 0.05, q1, off=2.0)
B(41133, T('cereal') - 0.1, T('marketing') - 0.08, off=0.5)
B(41148, T('ki', T('tha')) - 0.05, c1 - 0.05, off=2.0)
B(28886, T('raat') - 0.1, T('breakfast', T('raat')) - 0.08, off=1.0)
B(41142, T('kyunki', T('kyun', T('karna'))) - 0.05, T('harvard') - 0.1, off=1.0)
B(4712, T('research') - 0.25, a1, off=2.0)
B(44001, T('snacks') - 0.15, T('pathway') - 0.1, off=1.0)
B(3768, T('sirtuins') - 0.1, T('ye', T('enzymes')) - 0.05, off=1.0)
B(4764, T('boodhi') - 0.4, T('aur', T('se', T('boodhi'))) - 0.05, off=1.0)
B(28894, T('jab', T('jhooth', T('hoga'))) - 0.05, T('16.*') - 0.1, off=1.0)
B(4546, T('water') - 0.2, T('toh', T('banta')) - 0.1, off=1.0)
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

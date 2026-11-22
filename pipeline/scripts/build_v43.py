import sys
from spec_lib2 import Spec
import mc_theme as MC
S = Spec(sys.argv[1], 'v43', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; IV = '#EDE7DA'; CH = '#CDB98B'; K = S.kin; Bh = S.behind; B = lambda *a, **k: S.broll(*a, bright=-0.17, sat=0.78, **k)  # brand grade: darker, softer film look
# ---------------- hook
B(1776, 0.0, T('but') - 0.05, off=1.0)
K(0.05, T('but') - 0.05, ['EVERYONE TAKES THIS PILL', '*after a rave*'], x=540, y=300, sizes=[70, 110], anim='rise', stagger=0.9)
Bh(T('but') - 0.03, T('and', T('serotonin')) - 0.05, 'SEROTONIN', size=200, font='mc', anim='slam', color=IV)
K(T('doesnt') - 0.05, T('and', T('serotonin')) - 0.05, ["IT DOESN'T EVEN ~MAKE IT~"], x=540, y=1600, sizes=[56], font='label', anim='rise')
K(T('and', T('serotonin')) - 0.03, T('your') - 0.05, ['GIVE ME', '*one minute*'], x=540, y=300, sizes=[100, 130], anim='rise', stagger=0.9)
# ---------------- neurotransmitters
B(40531, T('your') - 0.05, T('the', T('food')) - 0.05, off=1.0)
K(T('your') - 0.03, T('the', T('food')) - 0.05, ['YOUR FEEL-GOOD CHEMICALS', 'are made *from food*'], x=540, y=300, sizes=[66, 100], anim='rise', stagger=1.0)
n0 = T('the', T('food')) - 0.08; n1 = T('this', T('neurotransmitters')) - 0.08
S.card(n0, n1)
nn = [{'t': n0 + 0.2, 'x': 500, 'y': 60, 'text': 'Brain cell'}, {'t': T('messages') - 0.1, 'x': 500, 'y': 215, 'text': 'Carries a *chemical message*'},
      {'t': T('next'), 'x': 500, 'y': 370, 'text': 'Next brain cell'}, {'t': T('neurotransmitters'), 'x': 500, 'y': 530, 'text': 'NEUROTRANSMITTERS', 'target': True}]
nw = [{'t': T('messages') - 0.4, 'd': 'M 500 105 L 500 165'}, {'t': T('next') - 0.3, 'd': 'M 500 260 L 500 320'}, {'t': T('neurotransmitters') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': n0, 't1': n1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': nn, 'wires': nw})
# ---------------- L-tyrosine -> dopamine
Bh(T('this', T('neurotransmitters')) - 0.03, T('and', T('ltyrosine')) - 0.05, 'L-TYROSINE', size=190, font='mc', anim='slam', color=CH)
d0 = T('and', T('ltyrosine')) - 0.08; d1 = T('but', T('happy')) - 0.08
S.card(d0, d1)
S.add({'type': 'chain', 't0': d0, 't1': d1, 'y': 150, 'title': 'What L-tyrosine becomes', 'show': 4, 'items': [
    {'t': T('tyrosine', d0), 'text': '*Tyrosine*'}, {'t': T('dopamine'), 'text': 'becomes *dopamine*', 'st': 'up', 'stc': 'green'},
    {'t': T('focus'), 'text': '*Focus* and *drive*', 'st': 'yes', 'stc': 'green'}, {'t': T('calm'), 'text': '~Calm and happy~', 'st': 'no', 'stc': 'red'}]})
# ---------------- serotonin needs tryptophan
s0 = T('but', T('happy')) - 0.08; s1 = T('and', T('tryptophan')) - 0.08
S.card(s0, s1)
S.add({'type': 'checklist', 't0': s0, 't1': s1, 'y': 150, 'title': 'Two different raw materials', 'items': [
    {'t': s0 + 0.2, 'text': 'Dopamine: from *tyrosine*', 'mark': 'check'}, {'t': T('tryptophan') - 0.1, 'text': 'Serotonin: from *tryptophan*', 'mark': 'check'}]})
K(T('and', T('tryptophan')) - 0.03, T('tyrosine', T('problem')) - 0.05, ["HERE'S", '~the problem~'], x=540, y=300, sizes=[96, 130], anim='rise', stagger=0.7)
Bh(T('tyrosine', T('problem')) - 0.03, T('they', T('door')) - 0.05, 'SAME DOOR', size=230, font='mc', anim='slam', color=IV)
K(T('door') - 0.1, T('they', T('door')) - 0.05, ['ONE SHARED TRANSPORTER INTO THE BRAIN (LAT1)'], x=540, y=1600, sizes=[34], font='label', anim='rise', fit=980)
f0 = T('they', T('door')) - 0.08; f1 = T('so', T('harder')) - 0.08
S.card(f0, f1)
S.add({'type': 'chain', 't0': f0, 't1': f1, 'y': 150, 'title': 'They compete for the same door', 'show': 4, 'items': [
    {'t': T('space'), 'text': 'They *fight for space*'}, {'t': T('more', T('space')), 'text': 'More tyrosine...', 'st': 'up', 'stc': 'red'},
    {'t': T('serotonin', T('space')), 'text': '~No extra serotonin~', 'st': 'no', 'stc': 'red'}, {'t': T('harder'), 'text': 'Less *tryptophan* gets in', 'st': 'down', 'stc': 'red'}]})
# ---------------- what helps
K(T('so', T('harder')) - 0.03, T('number') - 0.05, ['SO WHAT ACTUALLY HELPS', '*after a big weekend?*'], x=540, y=300, sizes=[70, 96], anim='rise', stagger=1.0)
h0 = T('number') - 0.08; h1 = T('ill', T('sunlight')) - 0.08
S.card(h0, h1)
S.add({'type': 'checklist', 't0': h0, 't1': h1, 'y': 150, 'title': 'After a big weekend', 'items': [
    {'t': T('sleep'), 'text': 'Good *sleep*', 'mark': 'check'}, {'t': T('real'), 'text': 'Real *food*', 'mark': 'check'},
    {'t': T('sunlight'), 'text': 'Morning *sunlight*', 'mark': 'check'}]})
B(4397, T('ill', T('sunlight')) - 0.05, T('comment') - 0.05, off=0.6)
K(T('ill', T('sunlight')) - 0.03, T('comment') - 0.05, ['THE SUNLIGHT PART:', '*next video*'], x=540, y=300, sizes=[76, 120], anim='rise', stagger=0.8)
cta = T('comment') - 0.05
MC.end_card(S, cta, D + 2, 'Comment<br>*"Rave Protocol"*', 'For the next video. Follow Moon Crew for more.')
S.alt_zoom([1.0, 1.18, 1.06, 1.26]); S.cam['faceY'] = 0.40; S.cam['grain'] = 5
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'pill', r'rave', r'serotonin', r'chemicals', r'food', r'messages?', r'brain', r'neurotransmitters', r'ltyrosine', r'tyrosine',
                           r'dopamine', r'focus', r'drive', r'calm', r'happy', r'tryptophan', r'problem', r'door', r'space', r'harder', r'helps', r'weekend',
                           r'sleep', r'real', r'sunlight', r'protocol', r'moon', r'crew'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': MC.BRAND['text'], 't0': 3.0, 't1': cta}, extra={'css': MC.CSS})

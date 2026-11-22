import sys
from spec_lib2 import Spec
import mc_theme as MC
S = Spec(sys.argv[1], 'v46', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; IV = '#EDE7DA'; CH = '#CDB98B'; K = S.kin; Bh = S.behind; B = lambda *a, **k: S.broll(*a, bright=-0.17, sat=0.78, **k)  # brand grade: darker, softer film look
# ---------------- hook
B(2856, 0.0, T('i') - 0.05, off=0.6)
K(0.05, T('i') - 0.05, ['DOES L-TYROSINE', '*actually work?*'], x=540, y=300, sizes=[80, 120], anim='rise', stagger=0.8)
K(T('i') - 0.03, T('and', T('situation')) - 0.05, ['YES.', 'BUT ONLY IN *one situation*'], x=540, y=300, sizes=[140, 72], anim='rise', stagger=1.0)
K(T('and', T('situation')) - 0.03, T('quick') - 0.05, ["AND MOST PEOPLE TAKING IT", "~AREN'T IN IT~"], x=540, y=300, sizes=[64, 100], anim='rise', stagger=1.2)
# ---------------- recap
r0 = T('quick') - 0.08; r1 = T('a', T('alert')) - 0.08
S.card(r0, r1)
S.add({'type': 'chain', 't0': r0, 't1': r1, 'y': 150, 'title': 'Quick recap', 'show': 4, 'items': [
    {'t': T('tyrosine', r0), 'text': '*Tyrosine*'}, {'t': T('dopamine', r0), 'text': 'becomes *dopamine*'},
    {'t': T('focus'), 'text': 'Helps you *focus*', 'st': 'up', 'stc': 'green'}, {'t': T('alert'), 'text': 'And *stay alert*', 'st': 'up', 'stc': 'green'}]})
# ---------------- the 2015 review
S.add({'type': 'badge', 't0': T('a', T('alert')) - 0.05, 't1': T('and', T('studies')) - 0.05, 'y': 260, 'text': 'Review, 2015', 'sub': 'Looked at *all the studies*'})
B(4773, T('a', T('alert')) - 0.05, T('and', T('studies')) - 0.05, off=0.6)
h0 = T('and', T('studies')) - 0.08; h1 = T('on', T('sleep')) - 0.08
S.card(h0, h1)
S.add({'type': 'checklist', 't0': h0, 't1': h1, 'y': 150, 'title': 'It only helped when dopamine ran low', 'items': [
    {'t': T('stress'), 'text': 'Heavy *stress*', 'mark': 'check'}, {'t': T('extreme'), 'text': 'Extreme *cold*', 'mark': 'check'},
    {'t': T('sleep'), 'text': '*No sleep*', 'mark': 'check'}]})
K(T('on', T('sleep')) - 0.03, T('you', T('nothing')) - 0.05, ['ON A NORMAL DAY:', '~it did nothing~'], x=540, y=300, sizes=[84, 120], anim='rise', stagger=0.9)
Bh(T('you', T('nothing')) - 0.03, T('and', T('full')) - 0.05, 'FULL TANK', size=230, font='mc', anim='slam', color=IV)
K(T('fill') - 0.1, T('and', T('full')) - 0.05, ["YOU CAN'T FILL A TANK THAT'S ALREADY FULL"], x=540, y=1600, sizes=[34], font='label', anim='rise', fit=980)
# ---------------- dose
S.add({'type': 'stat', 't0': T('and', T('full')) - 0.05, 't1': T('and', T('capsule')) - 0.05, 'y': 260, 'kicker': 'The doses that worked', 'from': 0, 'to': 100, 'unit': ' MG',
       'label': 'Per *kilo* of body weight', 'pill': 'Not one small capsule', 'dir': 'up', 'count': 1.0})
# ---------------- safety
Bh(T('and', T('capsule')) - 0.03, T('if', T('important')) - 0.05, 'IMPORTANT', size=210, font='mc', anim='slam', color=CH)
w0 = T('if', T('important')) - 0.08; w1 = T('and', T('rave')) - 0.08
S.card(w0, w1)
S.add({'type': 'checklist', 't0': w0, 't1': w1, 'y': 150, 'title': 'Talk to your doctor first if you take', 'items': [
    {'t': T('antidepressants'), 'text': '*Antidepressants*', 'mark': 'x'}, {'t': T('thyroid'), 'text': '*Thyroid* medicine', 'mark': 'x'}]})
K(T('doctor') - 0.1, w1, ['THEN THE RAVE. THEN THE TYROSINE.'], x=540, y=760, sizes=[40], font='label', anim='rise', fit=960)
K(T('and', T('rave')) - 0.03, T('and', T('stamina')) - 0.05, ["IT WON'T HELP YOU", '~dance for longer~'], x=540, y=300, sizes=[84, 110], anim='rise', stagger=0.9)
K(T('studies', T('dance')) - 0.1, T('and', T('stamina')) - 0.05, ['ALMOST NO EFFECT ON STAMINA'], x=540, y=1600, sizes=[40], font='label', anim='rise', fit=980)
cta = T('and', T('stamina')) - 0.05
MC.end_card(S, cta, D + 2, 'Comment<br>*"Rave Protocol"*', "I'll tell you each and everything about rave. Follow Moon Crew for more.")
S.alt_zoom([1.0, 1.18, 1.06, 1.26]); S.cam['faceY'] = 0.40; S.cam['grain'] = 5
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'ltyrosine', r'tyrosine', r'yes', r'situation', r'dopamine', r'focus', r'alert', r'2015', r'review', r'studies', r'low',
                           r'stress', r'extreme', r'cold', r'sleep', r'nothing', r'tank', r'full', r'worked', r'100', r'milligrams', r'kilo', r'capsule',
                           r'important', r'antidepressants', r'thyroid', r'doctor', r'rave', r'dance', r'stamina', r'protocols?', r'moon', r'crew'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': MC.BRAND['text'], 't0': 3.0, 't1': cta}, extra={'css': MC.CSS})

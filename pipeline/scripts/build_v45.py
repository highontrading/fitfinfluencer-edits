import sys
from spec_lib2 import Spec
import mc_theme as MC
S = Spec(sys.argv[1], 'v45', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; IV = '#EDE7DA'; CH = '#CDB98B'; K = S.kin; Bh = S.behind; B = lambda *a, **k: S.broll(*a, bright=-0.17, sat=0.78, **k)  # brand grade: darker, softer film look
# ---------------- hook
Bh(0.05, T('your') - 0.05, 'CREATINE', size=210, font='mc', anim='slam', color=IV)
K(0.1, T('your') - 0.05, ['NOT JUST FOR YOUR ~MUSCLES~'], x=540, y=1600, sizes=[44], font='label', anim='rise', fit=980)
K(T('your') - 0.03, T('because') - 0.05, ['YOUR *BRAIN*', 'USES IT TOO'], x=540, y=300, sizes=[120, 90], anim='rise', stagger=0.6)
B(4344, T('because') - 0.05, T('and', T('festival')) - 0.05, off=0.5)
K(T('because') - 0.03, T('and', T('festival')) - 0.05, ['TESTED ON PEOPLE WHO', 'STAYED UP *all night*'], x=540, y=300, sizes=[70, 100], anim='rise', stagger=1.2)
K(T('and', T('festival')) - 0.03, T('but') - 0.05, ['AND IT', '^worked^'], x=540, y=300, sizes=[100, 150], anim='rise', stagger=0.9)
K(T('but') - 0.03, T('every') - 0.05, ['BUT THERE IS', '*a catch*'], x=540, y=300, sizes=[96, 130], anim='rise', stagger=0.6)
# ---------------- how it works
a0 = T('every') - 0.08; a1 = T('in', T('brain', T('muscles', T('fast')))) - 0.08
S.card(a0, a1)
an = [{'t': a0 + 0.2, 'x': 500, 'y': 60, 'text': 'Every cell runs on *ATP*'}, {'t': T('low') - 0.1, 'x': 500, 'y': 215, 'text': 'The cell *runs low*'},
      {'t': T('refill') - 0.2, 'x': 500, 'y': 370, 'text': 'Creatine *refills it fast*'}, {'t': T('brain', T('muscles', T('fast'))) - 0.2, 'x': 500, 'y': 530, 'text': 'Muscles AND brain', 'target': True}]
aw = [{'t': T('low') - 0.4, 'd': 'M 500 105 L 500 165'}, {'t': T('refill') - 0.5, 'd': 'M 500 260 L 500 320'}, {'t': T('brain', T('muscles', T('fast'))) - 0.5, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': a0, 't1': a1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': an, 'wires': aw})
K(T('atp') - 0.1, T('and', T('atp')) - 0.05, ['ATP = YOUR CELLS\' ENERGY'], x=540, y=110, sizes=[32], font='label', anim='rise', fit=1000)
# ---------------- the 2024 study
s0 = T('in', T('brain', T('muscles', T('fast')))) - 0.08; s1 = T('so', T('nine')) - 0.08
S.card(s0, s1)
S.add({'type': 'chain', 't0': s0, 't1': s1, 'y': 150, 'title': 'Sleep-deprivation study, 2024', 'show': 4, 'items': [
    {'t': T('15'), 'text': '*15 people* awake all night'}, {'t': T('took'), 'text': 'Took *creatine*'},
    {'t': T('thought'), 'text': 'Thought *faster*', 'st': 'up', 'stc': 'green'}, {'t': T('remembered'), 'text': 'Remembered *better*', 'st': 'up', 'stc': 'green'},
    {'t': T('three'), 'text': 'Kicked in after *~3 hours*'}, {'t': T('nine'), 'text': 'Lasted up to *9 hours*'}]})
# ---------------- the catch
K(T('so', T('nine')) - 0.03, T('they', T('catch', T('nine'))) - 0.05, ["HERE'S", '*the catch*'], x=540, y=300, sizes=[96, 130], anim='rise', stagger=0.6)
S.add({'type': 'stat', 't0': T('they', T('catch', T('nine'))) - 0.05, 't1': T('that', T('70')) - 0.05, 'y': 260, 'kicker': 'One single dose', 'from': 0, 'to': 25, 'unit': ' G',
       'label': 'For a *70 kg* person', 'dir': 'up', 'count': 1.0})
K(T('that', T('70')) - 0.03, T('and', T('home')) - 0.05, ['A LAB TEST.', "~DON'T TRY THIS AT HOME~"], x=540, y=300, sizes=[96, 76], anim='rise', stagger=1.0)
# ---------------- what works
K(T('and', T('home')) - 0.03, T('take') - 0.05, ['WHAT ACTUALLY WORKS?', '*very simple*'], x=540, y=300, sizes=[76, 120], anim='rise', stagger=1.0)
w0 = T('take') - 0.08; w1 = T('but', T('training')) - 0.08
S.card(w0, w1)
S.add({'type': 'checklist', 't0': w0, 't1': w1, 'y': 150, 'title': 'What actually works', 'items': [
    {'t': T('3', w0), 'text': '*3-5 g* of creatine', 'mark': 'check'}, {'t': T('every', w0), 'text': '*Every day*', 'mark': 'check'},
    {'t': T('weeks'), 'text': 'Muscles *fill up* in a few weeks', 'mark': 'check'}, {'t': T('training'), 'text': 'Your *training* gets better', 'mark': 'check'}]})
B(44416, T('weeks') - 0.3, w1, off=0.8)
K(T('but', T('training')) - 0.03, T('comment') - 0.05, ['KIDNEY PROBLEMS?', '*ask your doctor first*'], x=540, y=300, sizes=[90, 96], anim='rise', stagger=0.9)
cta = T('comment') - 0.05
MC.end_card(S, cta, D + 2, 'Comment<br>*"Rave Protocol"*', 'For more of this. Follow Moon Crew for more.')
S.alt_zoom([1.0, 1.18, 1.06, 1.26]); S.cam['faceY'] = 0.40; S.cam['grain'] = 5
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'creatine', r'muscles', r'brain', r'night', r'festival', r'worked', r'catch', r'cell', r'energy', r'atp', r'low', r'refill',
                           r'2024', r'15', r'awake', r'faster', r'better', r'three', r'nine', r'huge', r'25', r'grams', r'70', r'lab', r'home', r'simple',
                           r'5', r'day', r'weeks', r'training', r'kidney', r'doctor', r'protocol', r'moon', r'crew'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': MC.BRAND['text'], 't0': 3.0, 't1': cta}, extra={'css': MC.CSS})

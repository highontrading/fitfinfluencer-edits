import sys
from spec_lib2 import Spec
import mc_theme as MC
S = Spec(sys.argv[1], 'v44', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; IV = '#EDE7DA'; CH = '#CDB98B'; K = S.kin; Bh = S.behind; B = lambda *a, **k: S.broll(*a, bright=-0.17, sat=0.78, **k)  # brand grade: darker, softer film look
# ---------------- hook: the Monday after
B(4188, 0.0, T('so') - 0.05, off=0.5)
K(0.05, T('so') - 0.05, ['THE FESTIVAL WAS', '*amazing*'], x=540, y=300, sizes=[80, 130], anim='rise', stagger=0.8)
Bh(T('so') - 0.03, T('because') - 0.05, 'MONDAY', size=270, font='mc', anim='slam', color=IV)
K(T('empty') - 0.1, T('because') - 0.05, ['WHY DO YOU FEEL SO ~EMPTY?~'], x=540, y=1600, sizes=[44], font='label', anim='rise', fit=980)
K(T('because') - 0.03, T('two') - 0.05, ["IT'S NOT", 'JUST *the party*'], x=540, y=300, sizes=[96, 120], anim='rise', stagger=0.7)
K(T('two') - 0.03, T('both') - 0.05, ['2 THINGS IN YOUR BRAIN', 'GOT *knocked out*'], x=540, y=300, sizes=[76, 110], anim='slam', stagger=0.9)
K(T('both') - 0.03, T('number') - 0.05, ['BOTH ARE', '^free to fix^'], x=540, y=300, sizes=[96, 130], anim='rise', stagger=0.6)
# ---------------- #1 dopamine
Bh(T('number') - 0.03, T('your', T('key')) - 0.05, 'DOPAMINE', size=220, font='mc', anim='slam', color=CH)
K(T('key') - 0.15, T('your', T('key')) - 0.05, ['= A KEY'], x=540, y=1600, sizes=[60], font='label', anim='rise')
r0 = T('your', T('key')) - 0.08; r1 = T('in', T('receptors')) - 0.08
S.card(r0, r1)
rn = [{'t': r0 + 0.1, 'x': 500, 'y': 60, 'text': 'Dopamine = *the key*'}, {'t': T('lock') - 0.1, 'x': 500, 'y': 215, 'text': 'Brain cells have *a lock*'},
      {'t': T('these') - 0.1, 'x': 500, 'y': 370, 'text': 'The lock is called a...'}, {'t': T('receptors') - 0.1, 'x': 500, 'y': 530, 'text': 'RECEPTOR', 'target': True}]
rw = [{'t': T('lock') - 0.4, 'd': 'M 500 105 L 500 165'}, {'t': T('these') - 0.4, 'd': 'M 500 260 L 500 320'}, {'t': T('receptors') - 0.4, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': r0, 't1': r1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': rn, 'wires': rw})
s0 = T('in', T('receptors')) - 0.08; s1 = T('same') - 0.08
S.card(s0, s1)
S.add({'type': 'chain', 't0': s0, 't1': s1, 'y': 150, 'title': 'Brain scans, 2012', 'show': 4, 'items': [
    {'t': T('2012'), 'text': 'Scientists *scanned brains*'}, {'t': T('night'), 'text': 'After *one night* without sleep'},
    {'t': T('fewer'), 'text': '*Fewer open* dopamine receptors', 'st': 'down', 'stc': 'red'}, {'t': T('reward'), 'text': 'In the *reward area* (striatum)'}]})
B(51405, T('same') - 0.05, T('second') - 0.05, off=0.5)
K(T('same') - 0.03, T('second') - 0.05, ['SAME DOPAMINE. FEWER LOCKS.', '~nothing feels good~'], x=540, y=300, sizes=[60, 110], anim='rise', stagger=1.3)
# ---------------- #2 serotonin
Bh(T('second') - 0.03, T('a', T('serotonin')) - 0.05, 'SEROTONIN', size=200, font='mc', anim='slam', color=CH)
S.add({'type': 'badge', 't0': T('a', T('serotonin')) - 0.05, 't1': T('their') - 0.05, 'y': 260, 'text': 'The Lancet', 'sub': 'A study of *101 men*'})
B(1086, T('their') - 0.05, T('so', T('sunlight')) - 0.05, off=0.5)
K(T('their') - 0.03, T('so', T('sunlight')) - 0.05, ['MORE BRIGHT SUNLIGHT', '= MORE *serotonin* MADE'], x=540, y=300, sizes=[70, 96], anim='rise', stagger=1.4)
# ---------------- the fix
f0 = T('so', T('sunlight')) - 0.08; f1 = T('if', T('phone')) - 0.08
S.card(f0, f1)
S.add({'type': 'checklist', 't0': f0, 't1': f1, 'y': 150, 'title': "Here's the fix", 'items': [
    {'t': T('get'), 'text': 'One long, *proper sleep*', 'mark': 'check'}, {'t': T('morning'), 'text': '*Morning sun*', 'mark': 'check'},
    {'t': T('phone'), 'text': 'Before you *check your phone*', 'mark': 'check'}]})
K(T('if', T('phone')) - 0.03, T('comment') - 0.05, ['STILL LOW AFTER 2 WEEKS?', '*talk to someone*'], x=540, y=300, sizes=[70, 110], anim='rise', stagger=1.0)
cta = T('comment') - 0.05
MC.end_card(S, cta, D + 2, 'Comment<br>*"Rave Protocol"*', 'For more videos like this. Follow Moon Crew for more.')
S.alt_zoom([1.0, 1.18, 1.06, 1.26]); S.cam['faceY'] = 0.40; S.cam['grain'] = 5
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'festival', r'amazing', r'empty', r'monday', r'party', r'brain', r'knocked', r'free', r'dopamine', r'key', r'lock', r'locks',
                           r'receptors', r'2012', r'scanned', r'sleep', r'fewer', r'reward', r'good', r'serotonin', r'lancet', r'101', r'sunlight', r'fix',
                           r'proper', r'morning', r'sun', r'phone', r'low', r'weeks', r'someone', r'protocol', r'moon', r'crew'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': MC.BRAND['text'], 't0': 3.0, 't1': cta}, extra={'css': MC.CSS})

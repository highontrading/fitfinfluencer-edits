import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v40', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('raat') - 0.05, ['1 IN EVERY 4-5 INDIANS', 'DRINKS *ALCOHOL*'], x=540, y=300, sizes=[76, 110], anim='slam')
B(5145, T('raat') - 0.05, T('aur', T('uthe')) - 0.05, off=0.8)
K(T('raat') - 0.03, T('aur', T('uthe')) - 0.05, ["CAN'T SLEEP?", '*"ONE DRINK."*'], x=540, y=330, sizes=[96, 110], anim='slam', stagger=1.0)
K(T('aur', T('uthe')) - 0.03, T('kyunki') - 0.05, ['8 HOURS OF SLEEP.', '~STILL TIRED.~'], x=540, y=300, sizes=[90, 110], anim='slam', stagger=0.8)
Bh(T('kyunki') - 0.03, T('samjho') - 0.05, 'FAKE SLEEP', size=270, font='anton', anim='slam', color=R); S.punch(T('fake'), 0.12, 0.7)
K(T('samjho') - 0.03, T('chaaron') - 0.05, ['SLEEP HAS', '*4 STAGES*'], x=540, y=300, sizes=[96, 140], anim='slam')
# ---------------- the 4 stages
s0 = T('chaaron') - 0.08; s1 = T('ab', T('complete')) - 0.08
S.card(s0, s1)
S.add({'type': 'chain', 't0': s0, 't1': s1, 'y': 150, 'title': 'The 4 stages of sleep', 'show': 4, 'items': [
    {'t': T('stage'), 'text': 'Stage 1-2: *light sleep*, body relaxes'}, {'t': T('deep'), 'text': 'Stage 3: *deep sleep*, body repairs'},
    {'t': T('2.5'), 'text': 'Only *~2.5 hrs* of deep sleep in 8'}, {'t': T('muscles'), 'text': 'Fixes *muscles, bones, immunity*'},
    {'t': T('rem'), 'text': 'Stage 4: *REM sleep*'}, {'t': T('organize'), 'text': 'Brain *organizes*'},
    {'t': T('consolidate'), 'text': '*Memory* consolidates'}, {'t': T('emotions'), 'text': '*Emotions* processed'}]})
# ---------------- what alcohol does
a0 = T('ab', T('complete')) - 0.05
Bh(a0, T('fast') - 0.05, 'ALCOHOL', size=330, font='anton', anim='slam', color=Y)
c0 = T('fast') - 0.08; c1 = T('aur', T('thake', T('organizing'))) - 0.08
S.card(c0, c1)
S.add({'type': 'compare', 't0': c0, 't1': c1, 'y': 170, 'title': 'What alcohol does to sleep', 'max': 10, 'items': [
    {'t': T('light', c0), 'label': 'Light sleep', 'text': 'FASTER', 'value': 8, 'cls': 'acc', 'color': 'linear-gradient(180deg,#FFD873,#E59A00)'},
    {'t': T('destroy') - 0.2, 'label': 'Deep + REM', 'text': 'GONE', 'value': 1, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
K(T('repairing') - 0.1, c1, ['NO REPAIR. NO ORGANIZING.'], x=540, y=760, sizes=[50], font='oswald', anim='rise')
K(T('aur', T('thake', T('organizing'))) - 0.03, T('jab', T('dikhaati')) - 0.05, ['THAT "HANGOVER"', '= ~NO REAL SLEEP~'], x=540, y=300, sizes=[90, 100], anim='slam')
K(T('jab', T('dikhaati')) - 0.03, T('studies') - 0.05, ['SKIP SLEEP LONG ENOUGH:', '*HANGOVER ANYWAY*'], x=540, y=300, sizes=[70, 96], anim='rise', stagger=0.8)
# ---------------- the breakfast study
b0 = T('studies') - 0.08; b1 = T('matlab', T('spike', T('kam'))) - 0.08
S.card(b0, b1)
S.add({'type': 'compare', 't0': b0, 't1': b1, 'y': 170, 'title': 'Same breakfast, different sleep', 'max': 10, 'items': [
    {'t': T('6', b0), 'label': '6 hrs sleep', 'text': 'HIGH', 'value': 10, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('7', b0), 'label': '7 hrs', 'text': 'MID', 'value': 6, 'cls': 'acc', 'color': 'linear-gradient(180deg,#FFD873,#E59A00)'},
    {'t': T('8', b0), 'label': '8 hrs, quality', 'text': 'LOW', 'value': 3, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
K(b0 + 0.3, b1, ['GLUCOSE SPIKE'], x=540, y=760, sizes=[50], font='oswald', anim='rise')
K(T('matlab', T('spike', T('kam'))) - 0.03, T('6', T('jaayega', T('exercise'))) - 0.05, ['BAD SLEEP =', 'DIET ~FAILS~. EXERCISE ~FAILS~.'], x=540, y=300, sizes=[90, 76], anim='slam', stagger=0.9)
S.add({'type': 'stat', 't0': T('6', T('jaayega', T('exercise'))) - 0.05, 't1': T('sleep', T('osteoporosis')) - 0.05, 'y': 260, 'kicker': '6-hour sleepers', 'from': 0, 'to': 40, 'unit': '%', 'label': 'More *fractures* + osteoporosis', 'dir': 'up', 'count': 0.9})
# ---------------- the hidden pillar
Bh(T('sleep', T('osteoporosis')) - 0.03, T('aur', T('pillar')) - 0.05, 'HIDDEN PILLAR', size=220, font='anton', anim='slam', color=G)
K(T('aur', T('pillar')) - 0.03, T('agar', T('important')) - 0.05, ['NOT JUST DIET + EXERCISE.', '*SLEEP IS #1*'], x=540, y=300, sizes=[70, 110], anim='slam', stagger=1.4)
r0 = T('agar', T('important')) - 0.08; r1 = T('aur', T('khaane', T('workout'))) - 0.08
S.card(r0, r1)
S.add({'type': 'chain', 't0': r0, 't1': r1, 'y': 150, 'title': 'Without proper sleep', 'show': 4, 'items': [
    {'t': T('repair', r0), 'text': 'No *repair*', 'st': 'no', 'stc': 'red'}, {'t': T('tootti'), 'text': 'Body *breaks down*', 'st': 'down', 'stc': 'red'},
    {'t': T('thake', r0), 'text': '*Tired* every day', 'st': 'down', 'stc': 'red'}, {'t': T('patle'), 'text': 'You never get lean', 'st': 'no', 'stc': 'red'}]})
K(T('aur', T('khaane', T('workout'))) - 0.03, T('agar', T('isliye')) - 0.05, ['IT HAPPENED', 'TO *ME*'], x=540, y=300, sizes=[100, 130], anim='slam')
cta = T('agar', T('isliye')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want my full system?', 'title': 'Comment<br>*"SYSTEM"*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'sharaab', r'drink', r'neend', r'thake', r'fake', r'sleep', r'stages?', r'light', r'deep', r'repair', r'muscles', r'bone',
                           r'immune', r'rem', r'brain', r'memory', r'emotions', r'alcohol', r'destroy', r'hangover', r'thakaan', r'studies', r'breakfast',
                           r'glucose', r'spike', r'insulin', r'fail', r'40%', r'fracture', r'osteoporosis', r'protocol', r'pillar', r'important', r'patle', r'system'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

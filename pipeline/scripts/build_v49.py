import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v49', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook: the comment
K(0.05, T('feet') - 0.05, ['A COMMENT I GOT:', '*"I\'M 59 KG"*'], x=540, y=300, sizes=[76, 120], anim='slam', stagger=0.8)
K(T('feet') - 0.03, T('145') - 0.05, ['5\'6". THIN.', 'STILL ~HIGH BP~'], x=540, y=300, sizes=[110, 110], anim='slam', stagger=0.9)
Bh(T('145') - 0.05, T('toh', T('aisa')) - 0.05, '145/95', size=300, font='anton', anim='slam', color=R)
K(T('toh', T('aisa')) - 0.03, T('main', T('galat')) - 0.05, ['"BP IS A FAT PERSON\'S PROBLEM"', '~COMPLETELY WRONG~'], x=540, y=300, sizes=[64, 110], anim='slam', stagger=1.6)
K(T('main', T('galat')) - 0.03, T('ab', T('alag')) - 0.05, ['BP AT 50 KG. BP AT 60 KG.', 'DIFFERENT *REASONS*'], x=540, y=300, sizes=[76, 110], anim='rise', stagger=1.0)
K(T('ab', T('alag')) - 0.03, T('number') - 0.05, ['5 REASONS', 'THIN PEOPLE GET *HIGH BP*'], x=540, y=300, sizes=[130, 76], anim='slam', stagger=0.8)
# ---------------- 1 genetics
a0 = T('number') - 0.08; a1 = T('number', T('genes')) - 0.08
S.card(a0, a1)
S.add({'type': 'chain', 't0': a0, 't1': a1, 'y': 150, 'title': 'Reason 1: Genetics', 'show': 4, 'items': [
    {'t': T('100'), 'text': '*100+ genes* linked to BP'}, {'t': T('parents'), 'text': 'Parents with *high BP*?'},
    {'t': T('guna'), 'text': 'Your risk: *2-3x*', 'st': 'up', 'stc': 'red'}, {'t': T('independent'), 'text': '*Independent* of body weight', 'st': 'yes', 'stc': 'red'}]})
# ---------------- 2 sodium sensitivity
b0 = T('number', T('genes')) - 0.08; b1 = T('reason', T('important')) - 0.08
S.card(b0, b1)
S.add({'type': 'chain', 't0': b0, 't1': b1, 'y': 150, 'title': 'Reason 2: Sodium sensitivity', 'show': 4, 'items': [
    {'t': T('sensitivity'), 'text': 'Differs for *everyone*'}, {'t': T('sensitive'), 'text': 'Some are *more sensitive*'},
    {'t': T('namak'), 'text': 'Same salt, *more sodium effect*'}, {'t': T('badhega'), 'text': 'BP rises *more*', 'st': 'up', 'stc': 'red'}]})
# ---------------- 3 stress
c0 = T('reason', T('important')) - 0.08; c1 = T('ab', T('independent', T('cortisol'))) - 0.08
S.card(c0, c1)
cn = [{'t': T('chronic') - 0.1, 'x': 500, 'y': 60, 'text': 'Chronic *stress*'}, {'t': T('cortisol', T('chronic')) - 0.1, 'x': 500, 'y': 215, 'text': '*Cortisol* rises'},
      {'t': T('sympathetic') - 0.1, 'x': 500, 'y': 370, 'text': 'Nervous system *overreacts*'}, {'t': T('arteries') - 0.1, 'x': 500, 'y': 530, 'text': 'Arteries tighten: BP UP', 'target': True}]
cw = [{'t': T('cortisol', T('chronic')) - 0.4, 'd': 'M 500 105 L 500 165'}, {'t': T('sympathetic') - 0.4, 'd': 'M 500 260 L 500 320'}, {'t': T('arteries') - 0.4, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': c0, 't1': c1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': cn, 'wires': cw})
K(c0 + 0.1, c1, ['REASON 3: STRESS + CORTISOL'], x=540, y=110, sizes=[48], font='oswald', anim='rise', fit=1000)
# ---------------- 4 sleep
d0 = T('ab', T('independent', T('cortisol'))) - 0.08; d1 = T('aur', T('37%')) - 0.08
S.card(d0, d1)
S.add({'type': 'chain', 't0': d0, 't1': d1, 'y': 150, 'title': 'Reason 4: Sleep', 'show': 4, 'items': [
    {'t': T('sleep'), 'text': 'Less than *6-8 hours* of sleep'}, {'t': T('active'), 'text': 'Nervous system *stays active*', 'st': 'up', 'stc': 'red'},
    {'t': T('norepinephrine'), 'text': 'Releases *norepinephrine*', 'st': 'up', 'stc': 'red'}, {'t': T('37%'), 'text': '1 hr less sleep: *+37% risk*', 'st': 'up', 'stc': 'red'}]})
K(T('norepinephrine') - 0.1, d1, ['NOREPINEPHRINE = A STRESS HORMONE'], x=540, y=780, sizes=[44], font='oswald', anim='rise', fit=1000)
# ---------------- 5 kidneys
e0 = T('aur', T('37%')) - 0.08; e1 = T('toh', T('chhoti')) - 0.08
S.card(e0, e1)
S.add({'type': 'chain', 't0': e0, 't1': e1, 'y': 150, 'title': 'Reason 5: Hidden kidney issues', 'show': 4, 'items': [
    {'t': T('hidden'), 'text': 'Kidney issues you *don\'t know about*'}, {'t': T('volume'), 'text': 'Kidneys *regulate blood volume*'},
    {'t': T('chhoti'), 'text': 'A *small* kidney issue'}, {'t': T('badha', T('chhoti')), 'text': 'Can *raise your BP*', 'st': 'up', 'stc': 'red'}]})
# ---------------- summary
K(T('toh', T('chhoti')) - 0.03, T('genetics', T('myth')) - 0.05, ['THE MYTH:', '"ONLY ~WEIGHT~ RAISES BP"'], x=540, y=300, sizes=[96, 84], anim='slam', stagger=0.9)
S.add({'type': 'chips', 't0': T('genetics', T('myth')) - 0.05, 't1': T('59', T('myth')) - 0.05, 'y': 200, 'items': [
    {'t': T('genetics', T('myth')), 'text': 'Genetics'}, {'t': T('sodium', T('myth')), 'text': 'Sodium sensitivity'}, {'t': T('stress', T('myth')), 'text': 'Stress'},
    {'t': T('sleep', T('myth')), 'text': 'Sleep'}, {'t': T('kidney', T('myth')), 'text': 'Kidney problems'}, {'t': T('matter'), 'text': '*All of them matter*'}]})
K(T('59', T('myth')) - 0.03, T('agar', T('120')) - 0.05, ['59 KG OR 120 KG:', '*CHECK YOUR BP*'], x=540, y=300, sizes=[96, 120], anim='slam', stagger=0.9)
K(T('agar', T('120')) - 0.03, T('aur', T('myth', T('120'))) - 0.05, ['"I\'M THIN, SO I\'M HEALTHY"', '~THE BIGGEST MYTH~'], x=540, y=300, sizes=[70, 110], anim='slam', stagger=1.2)
cta = T('aur', T('myth', T('120'))) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': "Don't believe me?", 'title': 'Check<br>*the data*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'59', r'kg', r'patla', r'bp', r'145', r'95', r'mote', r'galat', r'reasons?', r'genetics', r'genes', r'parents', r'guna',
                           r'independent', r'sodium', r'sensitivity', r'sensitive', r'namak', r'stress', r'cortisol', r'chronic', r'sympathetic', r'arteries',
                           r'tight', r'sleep', r'norepinephrine', r'37%', r'kidney', r'kidneys', r'volume', r'myth', r'120', r'check', r'important', r'data', r'science'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

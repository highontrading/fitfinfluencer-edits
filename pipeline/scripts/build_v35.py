import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v35', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('aur') - 0.05, ["YOU'RE A", '~DRUG ADDICT~'], x=540, y=300, sizes=[100, 140], anim='slam')
K(T('aur') - 0.03, T('sugar') - 0.05, ["AND YOU DON'T", 'EVEN KNOW IT'], x=540, y=300, sizes=[90, 90], anim='rise', stagger=0.6)
Bh(T('sugar') - 0.03, T('agar') - 0.05, 'SUGAR', size=400, font='anton', anim='slam', color=R); S.punch(T('sugar'), 0.14, 0.7)
K(T('agar') - 0.03, T('but', T('nasha')) - 0.05, ['COCAINE HABIT?', '*"GO TO REHAB."*'], x=70, y=300, align='left', sizes=[90, 100], anim='slam', stagger=0.9)
K(T('but', T('nasha')) - 0.03, T('par', T('hans')) - 0.05, ['SWEET TOOTH?', '^"HA HA."^'], x=1010, y=300, align='right', sizes=[90, 110], anim='slam', stagger=0.9)
K(T('par', T('hans')) - 0.03, T('aur', T('hit', T('cocaine', T('jisko')))) - 0.05, ['SAME BRAIN CENTER', 'AS *COCAINE*'], x=540, y=300, sizes=[84, 120], anim='slam')
Bh(T('8') - 0.05, T('samjho') - 0.05, '8X', size=460, font='anton', anim='slam', color=R)
K(T('addictive') - 0.1, T('samjho') - 0.05, ['MORE ADDICTIVE THAN COCAINE'], x=540, y=1540, sizes=[56], font='oswald', anim='rise')
# ---------------- reward center
r0 = T('samjho') - 0.08; r1 = T('problem', T('nahi', T('lagega'))) - 0.08
S.card(r0, r1)
rn = [{'t': T('nucleus') - 0.1, 'x': 500, 'y': 60, 'text': '*Nucleus accumbens*'}, {'t': T('reward'), 'x': 500, 'y': 215, 'text': 'Your *reward center*'},
      {'t': T('dopamine'), 'x': 500, 'y': 370, 'text': 'Sugar releases *dopamine*'}, {'t': T('pleasure'), 'x': 500, 'y': 530, 'text': 'Pleasure hormone: *feels good*', 'target': True}]
rw = [{'t': T('reward') - 0.3, 'd': 'M 500 105 L 500 165'}, {'t': T('dopamine') - 0.3, 'd': 'M 500 260 L 500 320'}, {'t': T('pleasure') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': r0, 't1': r1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': rn, 'wires': rw})
# ---------------- tolerance
K(T('problem', T('nahi', T('lagega'))) - 0.03, T('matlab', T('depend')) - 0.05, ['THE PROBLEM:', 'YOUR CENTER *DEPENDS* ON IT'], x=540, y=300, sizes=[84, 84], anim='rise', stagger=0.7)
t0 = T('matlab', T('depend')) - 0.08; t1 = T('ab', T('tolerance', T('sugar', T('tolerance')))) - 0.08
S.card(t0, t1)
S.add({'type': 'compare', 't0': t0, 't1': T('aur', T('paanch')) - 0.05, 'y': 170, 'title': 'Laddoos for the same happiness', 'max': 5, 'items': [
    {'t': T('ek', t0), 'label': 'Before', 'unit': '', 'value': 1, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('do', t0), 'label': 'Then', 'unit': '', 'value': 2, 'cls': 'acc', 'color': 'linear-gradient(180deg,#FFD873,#E59A00)'},
    {'t': T('teen', t0), 'label': 'Then', 'unit': '', 'value': 3, 'cls': 'acc', 'color': 'linear-gradient(180deg,#FFD873,#E59A00)'},
    {'t': T('paanch'), 'label': 'Then', 'unit': '+', 'value': 5, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
S.add({'type': 'badge', 't0': T('aur', T('paanch')) - 0.05, 't1': t1, 'y': 260, 'text': 'Tolerance', 'sub': 'Exactly the *cocaine addiction* pattern'})
# ---------------- India
Bh(T('ab', T('tolerance', T('sugar', T('tolerance')))) - 0.03, T('protein', T('deficient')) - 0.05, '73%', size=420, font='anton', anim='slam', color=R)
K(T('indian') - 0.1, T('protein', T('deficient')) - 0.05, ['OF INDIANS ARE *PROTEIN DEFICIENT*'], x=540, y=1540, sizes=[52], font='oswald', anim='rise')
i0 = T('protein', T('deficient')) - 0.08; i1 = T('is') - 0.08
S.card(i0, i1)
S.add({'type': 'chain', 't0': i0, 't1': i1, 'y': 150, 'title': 'Sugar pushed from both sides', 'show': 4, 'items': [
    {'t': T('protein', T('deficient')), 'text': 'Low protein'}, {'t': T('craving'), 'text': 'Body *manufactures* sugar cravings', 'st': 'up', 'stc': 'red'},
    {'t': T('namak', i0), 'text': 'Low salt: *more cravings*', 'st': 'up', 'stc': 'red'}, {'t': T('diabetes'), 'text': '~India: diabetes capital~', 'st': 'no', 'stc': 'red'}]})
S.fx('sub_drop', T('diabetes'), -12)
# ---------------- the system
Bh(T('is') - 0.03, T('aur', T('system', T('ek', T('rehab'))) ) - 0.05, 'REHAB', size=380, font='anton', anim='slam', color=Y)
K(T('system') - 0.1, T('aur', T('system', T('ek', T('rehab')))) - 0.05, ['BREAKING IT NEEDS *A SYSTEM*'], x=540, y=1540, sizes=[56], font='oswald', anim='rise')
K(T('aur', T('system', T('ek', T('rehab')))) - 0.03, T('brain', T('hoga')) - 0.05, ['"JUST DON\'T EAT SWEETS"', '~DOES NOTHING~'], x=540, y=300, sizes=[76, 100], font='serif', anim='rise', stagger=0.9)
s0 = T('brain', T('hoga')) - 0.08; s1 = T('aur', T('integrated', T('kaha'))) - 0.08
S.card(s0, s1)
S.add({'type': 'checklist', 't0': s0, 't1': s1, 'y': 150, 'title': 'An integrated system', 'items': [
    {'t': T('rewire'), 'text': '*Rewire* the brain', 'mark': 'check'}, {'t': T('timing'), 'text': 'Fix *protein timing*', 'mark': 'check'},
    {'t': T('sodium'), 'text': 'Balance *sodium*', 'mark': 'check'}]})
K(T('aur', T('integrated', T('kaha'))) - 0.03, T('jitne') - 0.05, ['I BUILT', 'THIS SYSTEM'], x=540, y=300, sizes=[110, 110], anim='slam')
K(T('jitne') - 0.03, T('aur', T('fastest')) - 0.05, ['THE FASTEST WEIGHT LOSS', 'OF *ANYONE I KNOW*'], x=540, y=300, sizes=[72, 90], anim='rise', stagger=0.6)
K(T('aur', T('fastest')) - 0.03, T('agar', T('fastest')) - 0.05, ['ALL BECAUSE OF', '*THE SYSTEM*'], x=540, y=300, sizes=[84, 110], anim='slam')
cta = T('agar', T('fastest')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want the system?', 'title': 'Comment<br>*"SYSTEM"*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'drug', r'addict', r'sugar', r'cocaine', r'rehab', r'nasha', r'meetha', r'science', r'brain', r'center', r'8', r'addictive',
                           r'nucleus', r'accumbens', r'reward', r'dopamine', r'pleasure', r'depend', r'laddoo', r'tolerance', r'73%', r'protein', r'deficient',
                           r'craving', r'namak', r'diabetes', r'system', r'rewire', r'timing', r'sodium', r'integrated', r'fastest', r'weight'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

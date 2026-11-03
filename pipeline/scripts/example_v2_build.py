import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v90', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']
# hook: big claim behind him, small setup line in a different spot
S.kin(0.05, T('pata') - 0.05, ['YOU WERE TAUGHT', 'THE *OPPOSITE*'], x=70, y=250, align='left', sizes=[80, 120], font='bebas', anim='wipe')
S.behind(T('breakfast') - 0.1, T('aur') - 0.05, 'BREAKFAST', size=300)
S.kin(T('most') - 0.05, T('aur') - 0.05, ['= MOST IMPORTANT MEAL?'], x=540, y=1600, sizes=[64], font='oswald', anim='rise')
S.add({'type': 'stamp', 't0': T('jhooth') - 0.1, 't1': T('aapko') - 0.05, 'y': 1120, 'text': 'A LIE', 'rot': -9})
S.punch(T('jhooth'), 0.14, 0.7)
# who told you? questions pop in different corners
S.kin(T('mummy') - 0.05, T('kisne', T('scientist')) - 0.05, ['PARENTS?'], x=70, y=330, align='left', sizes=[90], font='bebas', anim='slam')
S.kin(T('dada') - 0.05, T('kisne', T('scientist')) - 0.05, ['GRANDPARENTS?'], x=1010, y=560, align='right', sizes=[90], font='bebas', anim='slam')
S.kin(T('doctor') - 0.05, T('kisne', T('scientist')) - 0.05, ['A DOCTOR?'], x=70, y=790, align='left', sizes=[90], font='bebas', anim='slam')
S.kin(T('scientist') - 0.05, T('kisne', T('scientist')) - 0.05, ['A SCIENTIST?'], x=1010, y=1020, align='right', sizes=[90], font='bebas', anim='slam')
S.kin(T('kisne', T('scientist')) - 0.03, T('1944') - 0.08, ['WHO', 'TOLD YOU?'], x=540, y=420, sizes=[150, 110], font='anton', anim='slam')
# 1944: cinematic flashback
S.add({'type': 'cine', 't0': T('1944') - 0.1, 't1': T('kyun', T('day')) - 0.05, 'h': 160})
S.behind(T('1944') - 0.05, T('isko') - 0.05, '1944', size=380, font='anton', anim='slam')
S.kin(T('cereal') - 0.05, T('isko') - 0.05, ['A *CEREAL COMPANY*'], x=540, y=1600, sizes=[70], font='oswald', anim='wipe')
S.kin(T('marketing') - 0.05, T('ki', T('tha')) - 0.05, ['MARKETING', 'CAMPAIGN'], x=1010, y=300, align='right', sizes=[120, 120], font='bebas', anim='rise', color='#FFC53D')
S.kin(T('breakfast', T('tha')) - 0.05, T('kyun', T('day')) - 0.05, ['"BREAKFAST IS THE MOST', 'IMPORTANT MEAL OF THE DAY"'], x=540, y=330, sizes=[62, 62], font='serif', anim='type')
# the logic
S.kin(T('raat') - 0.1, T('toh', T('raat')) - 0.05, ['FASTING', 'ALL NIGHT'], x=70, y=300, align='left', sizes=[110, 110], font='bebas', anim='wipe')
S.kin(T('cereal', T('kyunki', T('important'))) - 0.05, T('harvard') - 0.08, ['SO THEY COULD', 'SELL *MORE CEREAL*'], x=540, y=360, sizes=[80, 110], font='bebas', anim='rise')
# authority
S.add({'type': 'callout', 't0': T('harvard') - 0.05, 't1': T('aur', T('anti.*')) - 0.05, 'px': 700, 'py': 700, 'lx': 980, 'ly': 520, 'text': 'HARVARD PROFESSOR'})
S.kin(T('david') - 0.05, T('aur', T('anti.*')) - 0.05, ['DR. DAVID SINCLAIR'], x=70, y=1600, align='left', sizes=[66], font='oswald', anim='wipe')
S.kin(T('25') - 0.05, T('aur', T('anti.*')) - 0.05, ['25 YEARS OF', 'ANTI-AGING RESEARCH'], x=1010, y=260, align='right', sizes=[70, 70], font='oswald', anim='rise')
S.behind(T('not') - 0.1, D, 'NOT', size=420, font='anton', anim='slam', color='#FF4D5E')
S.kin(T('not') + 0.1, D, ['THE MOST IMPORTANT MEAL'], x=540, y=1600, sizes=[60], font='oswald', anim='rise')
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'breakfast', r'jhooth', r'doctor', r'scientist', r'1944', r'cereal', r'marketing', r'campaign', r'fast', r'harvard', r'sinclair', r'research', r'not'])
B = S.broll
B(3795, T('breakfast') - 0.1, T('most') - 0.1, off=1.0)
B(4779, T('doctor') - 0.1, T('scientist') - 0.08, off=2.0)
B(4767, T('scientist') - 0.05, T('kisne', T('scientist')) - 0.05, off=2.0)
B(42908, T('cereal') - 0.1, T('marketing') - 0.08, off=1.0)
B(28886, T('raat') - 0.1, T('breakfast', T('raat')) - 0.05, off=1.0)
B(4712, T('research') - 0.2, T('aur', T('anti.*')) - 0.05, off=2.0)
S.save(caps, cta_t=None, hold=0.6, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': D})

import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v31', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('but') - 0.05, ['"EAT PEPTIDES."', '"INJECT PEPTIDES."'], x=540, y=300, sizes=[100, 100], anim='slam', stagger=0.9)
K(T('but') - 0.03, T('log') - 0.05, ['WHICH ARE ^GOOD^?', 'WHICH ARE ~BAD~?', 'WHICH ARE *FDA APPROVED*?'], x=70, y=260, align='left', sizes=[80, 80, 80], anim='rise', stagger=1.1)
S.add({'type': 'chips', 't0': T('log') - 0.05, 't1': T('lekin') - 0.05, 'y': 240, 'items': [
    {'t': T('bpc157'), 'text': 'BPC-157'}, {'t': T('ozempic'), 'text': 'Ozempic'}, {'t': T('sermorelin'), 'text': 'Sermorelin'}, {'t': T('basket') - 0.1, 'text': 'One basket?'}]})
K(T('lekin') - 0.03, T('sabka') - 0.05, ['MADE FOR', '*DIFFERENT JOBS*'], x=1010, y=300, align='right', sizes=[90, 110], anim='slam')
K(T('sabka') - 0.03, T('sab', T('risk')) - 0.05, ['DIFFERENT *EVIDENCE.*', 'DIFFERENT ~RISK.~'], x=540, y=300, sizes=[90, 90], anim='rise', stagger=0.9)
K(T('sab', T('risk')) - 0.03, T('video', T('bataunga')) - 0.05, ['THE *SIMPLEST* VERSION'], x=540, y=330, sizes=[110], anim='slam')
K(T('video', T('bataunga')) - 0.03, T('category') - 0.05, ['WATCH TO', 'THE END'], x=540, y=330, sizes=[100, 120], font='anton', anim='slam')
# ---------------- category 1
c0 = T('category') - 0.08; c1 = T('category', T('kyunki')) - 0.08
S.card(c0, c1)
S.add({'type': 'checklist', 't0': c0, 't1': c1, 'y': 150, 'title': 'Category 1: GLP-1 drugs', 'items': [
    {'t': T('ozempic', c0), 'text': 'Ozempic', 'mark': 'check'}, {'t': T('mounjaro'), 'text': 'Mounjaro', 'mark': 'check'},
    {'t': T('retatrutide'), 'text': 'Retatrutide', 'mark': 'check'}, {'t': T('phase'), 'text': '*Phase 3* trials', 'mark': 'check'},
    {'t': T('fda', c0), 'text': '*FDA approved*', 'mark': 'check'}, {'t': T('millions'), 'text': 'Used by *millions*', 'mark': 'check'}, {'t': T('5') - 0.1, 'text': 'Rating: *5/5*', 'mark': 'check'}]})
# ---------------- category 2
d0 = c1 + 0.02
K(d0 + 0.02, T('yaani', d0) - 0.05, ['CATEGORY 2', '*GH SECRETAGOGUES*'], x=540, y=300, sizes=[80, 100], anim='slam')
S.add({'type': 'chips', 't0': T('yaani', d0) - 0.05, 't1': T('tesamorelin') - 0.05, 'y': 240, 'items': [
    {'t': T('sermorelin', d0), 'text': 'Sermorelin'}, {'t': T('ipamorelin'), 'text': 'Ipamorelin'}, {'t': T('mk677'), 'text': 'MK-677'}, {'t': T('growth'), 'text': 'Raise *growth hormone*'}]})
K(T('tesamorelin') - 0.03, T('evidence', T('tesamorelin')) - 0.05, ['TESAMORELIN: *FDA APPROVED*', 'FOR ONE CONDITION.', 'THE REST: *RESEARCH*'], x=70, y=260, align='left', sizes=[70, 64, 70], anim='rise', stagger=1.0)
Bh(T('evidence', T('tesamorelin')) - 0.03, T('number') - 0.05, 'MIXED', size=340, font='anton', anim='slam', color=Y)
# ---------------- category 3
e0 = T('number') - 0.05
K(e0, T('in', e0) - 0.05, ['CATEGORY 3', '*RECOVERY PEPTIDES*'], x=540, y=300, sizes=[80, 100], anim='slam')
S.add({'type': 'chips', 't0': T('bpc157', e0) - 0.05, 't1': T('in', e0) - 0.05, 'y': 520, 'items': [
    {'t': T('bpc157', e0), 'text': 'BPC-157'}, {'t': T('tb500'), 'text': 'TB-500'}, {'t': T('wolverine'), 'text': '"Wolverine stack"'}]})
B(43385, T('in', e0) - 0.05, T('100') - 0.05, off=0.8)
K(T('in', e0) - 0.03, T('100') - 0.05, ['THE MOST POPULAR', 'ON *INSTAGRAM*'], x=540, y=330, sizes=[80, 110], anim='rise')
s0 = T('100') - 0.08; s1 = T('toh', T('rct')) - 0.08
S.card(s0, s1)
S.add({'type': 'chain', 't0': s0, 't1': s1, 'y': 150, 'title': 'The evidence for recovery peptides', 'show': 4, 'items': [
    {'t': T('100'), 'text': 'Studies on *100+ animals*'}, {'t': T('insaanon'), 'text': 'Humans: *2-3 small pilot studies*', 'st': 'down', 'stc': 'red'},
    {'t': T('0'), 'text': '~Zero RCTs~', 'st': 'no', 'stc': 'red'}]})
S.add({'type': 'stamp', 't0': T('unsafe') - 0.15, 't1': T('jitne') + 1.0, 'y': 1180, 'text': 'UNSAFE', 'rot': -7, 'size': 140}); S.punch(T('unsafe'), 0.14, 0.7)
K(T('jitne') - 0.03, T('toh', T('jitne')) - 0.05, ['"BPC-157 IS GREAT."', '"TB-500 IS GREAT."'], x=540, y=300, sizes=[84, 84], font='serif', anim='rise', stagger=1.4)
K(T('toh', T('jitne')) - 0.03, T('toh', T('proven', T('jitne'))) - 0.05, ['NOT EVEN', '~PROPERLY PROVEN~'], x=540, y=300, sizes=[96, 110], anim='slam')
# ---------------- irony
Bh(T('toh', T('proven', T('jitne'))) - 0.03, T('jo', T('irony')) - 0.05, 'IRONY', size=360, font='anton', anim='slam')
K(T('jo', T('irony')) - 0.03, T('aur', T('evidence', T('irony'))) - 0.05, ['MOST POPULAR ON INSTAGRAM', '= ~NO EVIDENCE~'], x=540, y=330, sizes=[64, 96], anim='rise', stagger=0.8)
K(T('aur', T('evidence', T('irony'))) - 0.03, T('kyun', T('irony')) - 0.05, ['ACTUALLY PROVEN', '= *NOBODY TALKS ABOUT IT*'], x=540, y=330, sizes=[64, 84], anim='rise', stagger=0.6)
S.add({'type': 'stamp', 't0': T('boring') - 0.15, 't1': T('aur', T('boring')) + 1.0, 'y': 1180, 'text': 'BORING', 'rot': -7, 'size': 140, 'color': '#FFC53D'})
# ---------------- the proven, free stuff
f0 = T('aur', T('boring')) - 0.05
K(f0, T('fasting') - 0.05, ['WHAT IS', '*MOST PROVEN?*'], x=540, y=300, sizes=[90, 120], anim='slam')
S.add({'type': 'chips', 't0': T('fasting') - 0.05, 't1': T('kyunki', T('kyun', T('meditation'))) - 0.05, 'y': 240, 'items': [
    {'t': T('fasting'), 'text': 'Fasting'}, {'t': T('diet'), 'text': 'Diet'}, {'t': T('exercise'), 'text': 'Exercise'}, {'t': T('meditation'), 'text': 'Meditation'}]})
Bh(T('kyunki', T('kyun', T('meditation'))) - 0.03, T('fasting', T('shortcut')) - 0.05, 'SHORTCUTS', size=300, font='anton', anim='slam', color=R)
c2 = T('fasting', T('shortcut')) - 0.08; c3 = T('ye', T('free', T('meditation', T('shortcut')))) - 0.08
S.card(c2, c3)
S.add({'type': 'checklist', 't0': c2, 't1': c3, 'y': 150, 'title': 'What it costs', 'items': [
    {'t': T('fasting', T('shortcut')), 'text': 'Fasting: *free*', 'mark': 'check'}, {'t': T('diet', T('shortcut')), 'text': 'Diet: *free*', 'mark': 'check'},
    {'t': T('exercise', T('shortcut')), 'text': 'Exercise: *free*', 'mark': 'check'}, {'t': T('meditation', T('shortcut')), 'text': 'Meditation: *free*', 'mark': 'check'}]})
K(c3 + 0.05, T('110') - 0.05, ['BUT WHO', 'WANTS TO DO IT?'], x=540, y=300, sizes=[96, 96], anim='rise')
j0 = T('110') - 0.08; j1 = T('kisi') - 0.08
S.card(j0, j1)
S.add({'type': 'stat', 't0': j0, 't1': j1, 'y': 200, 'kicker': 'My weight', 'from': 110, 'to': 85, 'unit': ' KG', 'label': 'In *45 days*', 'pill': 'With ZERO peptides', 'dir': 'down', 'count': 1.4})
S.fx('ding', T('zero'), -14)
K(T('kisi') - 0.03, T('achhi', T('dhakel')) - 0.05, ['PUT ME IN', 'ANY CATEGORY:'], x=540, y=300, sizes=[96, 96], anim='rise')
B(52089, T('achhi', T('dhakel')) - 0.05, T('category', T('dhakel')) - 0.05, off=1.0)
K(T('achhi', T('dhakel')) - 0.03, T('category', T('dhakel')) - 0.05, ['GOOD DIET.', 'GOOD FASTING.', '*GOOD EXERCISE.*'], x=540, y=300, sizes=[90, 90, 100], anim='rise', stagger=0.8)
cta = T('category', T('dhakel')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Know the category. Know the evidence.', 'title': 'Then<br>*decide*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'peptides?', r'fda', r'approved', r'bpc157', r'ozempic', r'sermorelin', r'ipamorelin', r'tesamorelin', r'retatrutide', r'mounjaro',
                           r'glp1', r'mk677', r'tb500', r'wolverine', r'evidence', r'risk', r'category', r'proven', r'star', r'growth', r'mixed', r'instagram',
                           r'animals', r'pilot', r'rct', r'unsafe', r'irony', r'boring', r'fasting', r'diet', r'exercise', r'meditation', r'free', r'shortcut',
                           r'110', r'85', r'zero'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})


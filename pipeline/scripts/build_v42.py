import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v42', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
RED = 'linear-gradient(180deg,#FF6B79,#C21D35)'; GRN = 'linear-gradient(180deg,#5CFFB5,#0FA968)'; AMB = 'linear-gradient(180deg,#FFD873,#E59A00)'
# ---------------- hook: the most expensive EMI
Bh(0.05, T('ghar') - 0.05, 'EMI', size=420, font='anton', anim='slam', color=Y)
K(0.1, T('ghar') - 0.05, ['WHICH ONE COSTS THE MOST?'], x=540, y=1600, sizes=[64], font='oswald', anim='rise')
S.add({'type': 'chips', 't0': T('ghar') - 0.05, 't1': T('mujhe') - 0.05, 'y': 260, 'items': [
    {'t': T('ghar'), 'text': 'Home?'}, {'t': T('car'), 'text': 'Car?'}, {'t': T('beemari'), 'text': '*Your illness?*'}]})
K(T('mujhe') - 0.03, T('car', T('mujhe')) - 0.05, ['THE EMI OF ILLNESS', '~NEVER ENDS~'], x=540, y=300, sizes=[84, 120], anim='slam', stagger=1.2)
e0 = T('car', T('mujhe')) - 0.08; e1 = T('sab') - 0.08
S.card(e0, e1)
S.add({'type': 'compare', 't0': e0, 't1': e1, 'y': 170, 'title': 'How long you pay', 'max': 40, 'items': [
    {'t': T('5'), 'label': 'Car', 'unit': ' yrs', 'value': 5, 'cls': 'green', 'color': GRN},
    {'t': T('20'), 'label': 'Home', 'unit': ' yrs', 'value': 20, 'cls': 'acc', 'color': AMB},
    {'t': T('zindagi') - 0.2, 'label': 'Illness', 'text': 'LIFE', 'value': 40, 'cls': 'red', 'color': RED}]})
# ---------------- insurance fails
K(T('sab') - 0.03, T('asli') - 0.05, ['EVERYONE', '~OVERCOMPLICATES~ THIS'], x=540, y=300, sizes=[80, 96], anim='rise')
K(T('asli') - 0.03, T('lekin') - 0.05, ['MANY PEOPLE HAVE', '*HEALTH INSURANCE*'], x=70, y=300, align='left', sizes=[80, 100], anim='wipe')
K(T('lekin') - 0.03, T('pata', T('lekin')) - 0.05, ['BUT WHEN YOU NEED IT,', "~IT DOESN'T WORK~"], x=1010, y=300, align='right', sizes=[70, 96], anim='slam')
K(T('pata', T('lekin')) - 0.03, T('india') - 0.05, ["HERE'S WHY"], x=540, y=330, sizes=[120], anim='track')
Bh(T('india') - 0.03, T('aur', T('jeb')) - 0.05, '65%', size=420, font='anton', anim='slam', color=R)
K(T('out') - 0.05, T('aur', T('jeb')) - 0.05, ['OF MEDICAL COSTS IN INDIA:', '*FROM YOUR OWN POCKET*'], x=540, y=1600, sizes=[50, 64], font='oswald', anim='rise')
K(T('aur', T('jeb')) - 0.03, T('monthly') - 0.05, ['TAKE ONE EXAMPLE:', '*BLOOD PRESSURE*'], x=540, y=300, sizes=[76, 110], anim='slam', stagger=1.0)
c0 = T('monthly') - 0.08; c1 = T('ab', T('turant')) - 0.08
S.card(c0, c1)
S.add({'type': 'chain', 't0': c0, 't1': c1, 'y': 150, 'title': 'What BP costs you', 'show': 4, 'items': [
    {'t': T('monthly'), 'text': 'Medicine: *Rs 500-2,000*/month'}, {'t': T('quarterly'), 'text': 'Blood tests: *Rs 1,500-3,000*'},
    {'t': T('visit'), 'text': 'Doctor visits: *Rs 500-1,000*'}, {'t': T('complication'), 'text': 'Complications: heart, kidney, liver', 'st': 'up', 'stc': 'red'},
    {'t': T('lakh'), 'text': '~Rs 2 - 10 lakh~ instant bill', 'st': 'up', 'stc': 'red'}]})
B(18263, T('lakh') - 0.1, c1, off=0.8)
S.fx('sub_drop', T('lakh'), -12)
# ---------------- IRDAI rule
i0 = T('ab', T('turant')) - 0.05
K(i0, T('irdai') - 0.05, ['THE TRUTH ABOUT', '*HEALTH INSURANCE*'], x=540, y=300, sizes=[76, 110], anim='slam')
S.add({'type': 'badge', 't0': T('irdai') - 0.05, 't1': T('36') - 0.05, 'y': 260, 'text': 'IRDAI rule change, 2024', 'sub': 'Pre-existing disease *waiting period*'})
Bh(T('36') - 0.05, T('matlab', T('36')) - 0.05, '36 MONTHS', size=260, font='anton', anim='slam', color=Y)
K(T('matlab', T('36')) - 0.03, T('ab', T('teen')) - 0.05, ['BP DIAGNOSED TODAY?', 'COVERED ONLY AFTER *3 YEARS*'], x=540, y=300, sizes=[70, 80], anim='rise', stagger=0.8)
Bh(T('ab', T('teen')) - 0.03, T('jab', T('trap')) - 0.05, 'THE TRAP', size=330, font='anton', anim='slam', color=R)
t0 = T('jab', T('trap')) - 0.08; t1 = T('middle') - 0.08
S.card(t0, t1)
S.add({'type': 'chain', 't0': t0, 't1': t1, 'y': 150, 'title': 'The insurance trap', 'show': 4, 'items': [
    {'t': T('healthy'), 'text': 'Healthy: *"Why do I need it?"*'}, {'t': T('beemar'), 'text': 'Fall ill: it *won\'t cover* you', 'st': 'no', 'stc': 'red'},
    {'t': T('preexisting', T('beemar')), 'text': 'Pre-existing = *waiting period*', 'st': 'no', 'stc': 'red'}, {'t': T('laakhon'), 'text': '~Lakhs~ spent by then', 'st': 'up', 'stc': 'red'}]})
# ---------------- middle class
K(T('middle') - 0.03, T('ek', T('middle')) - 0.05, ["THE MIDDLE CLASS'S", '*BIGGEST PROBLEM*'], x=540, y=300, sizes=[76, 100], anim='rise')
B(4701, T('ek', T('middle')) - 0.05, T('financial') - 0.05, off=1.0)
K(T('ek', T('middle')) - 0.03, T('financial') - 0.05, ['ONE EMERGENCY.', '~SAVINGS GONE.~', 'THE EMIs BEGIN.'], x=540, y=280, sizes=[96, 104, 70], anim='slam', stagger=1.1)
v0 = T('financial') - 0.08; v1 = T('do', T('cycle')) - 0.08
S.card(v0, v1)
vn = [{'t': T('financial') + 0.1, 'x': 500, 'y': 60, 'text': 'Financial *crisis*'}, {'t': T('stress', v0), 'x': 500, 'y': 215, 'text': '*Stress* shoots up'},
      {'t': T('health', v0), 'x': 500, 'y': 370, 'text': 'Health gets *worse*'}, {'t': T('vicious'), 'x': 500, 'y': 530, 'text': '~A vicious cycle~', 'target': True}]
vw = [{'t': T('stress', v0) - 0.3, 'd': 'M 500 105 L 500 165'}, {'t': T('health', v0) - 0.3, 'd': 'M 500 260 L 500 320'}, {'t': T('vicious') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': v0, 't1': v1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': vn, 'wires': vw})
# ---------------- what to do
K(T('do', T('cycle')) - 0.03, T('sabse', T('maaniye')) - 0.05, ['DO THESE', '*2 THINGS*'], x=540, y=300, sizes=[96, 140], anim='slam')
d0 = T('sabse', T('maaniye')) - 0.08; d1 = T('ya', T('wait')) - 0.08
S.card(d0, d1)
S.add({'type': 'checklist', 't0': d0, 't1': d1, 'y': 150, 'title': '#1: Insure early', 'items': [
    {'t': T('health', d0), 'text': 'Buy insurance *while healthy*', 'mark': 'check'}, {'t': T('waiting', d0), 'text': 'The *waiting period* starts counting', 'mark': 'check'},
    {'t': T('baad', d0), 'text': 'BP after buying: *covered*', 'mark': 'check'}, {'t': T('pehle', T('lene')), 'text': 'BP before buying: *3-year wait*', 'mark': 'x'}]})
K(T('ya', T('wait')) - 0.03, T('maine') - 0.05, ['#2: FOLLOW A', '*HEALTH PROTOCOL*'], x=540, y=300, sizes=[84, 110], anim='slam', stagger=0.8)
K(T('taaki', T('wait')) - 0.05, T('maine') - 0.05, ['SO ILLNESS NEVER COMES'], x=540, y=1600, sizes=[60], font='oswald', anim='rise')
# ---------------- my results
j0 = T('maine') - 0.08; j1 = T('saare', T('110')) - 0.08
S.card(j0, j1)
S.add({'type': 'stat', 't0': j0, 't1': j1, 'y': 200, 'kicker': 'My own journey', 'from': 110, 'to': 85, 'unit': ' KG', 'label': 'Weight *lost*', 'dir': 'down', 'count': 1.2})
f0 = T('saare', T('110')) - 0.08; f1 = T('aur', T('psoriasis')) - 0.08
S.card(f0, f1)
S.add({'type': 'checklist', 't0': f0, 't1': f1, 'y': 150, 'title': 'My family today', 'items': [
    {'t': T('ldl'), 'text': 'My high LDL: *normal*', 'mark': 'check'}, {'t': T('wife'), 'text': "Wife's BP: *controlled*", 'mark': 'check'},
    {'t': T('psoriasis'), 'text': "Mom's psoriasis: *improved*", 'mark': 'check'}]})
K(T('aur', T('psoriasis')) - 0.03, T('itna', T('kam')) - 0.05, ['THE DOCTOR BILL?', '^VERY LOW^'], x=540, y=300, sizes=[90, 130], anim='slam', stagger=1.3)
K(T('itna', T('kam')) - 0.03, T('toh', T('afford')) - 0.05, ['AFFORDABLE', 'FOR *ANYONE*'], x=540, y=300, sizes=[96, 110], anim='rise')
K(T('toh', T('afford')) - 0.03, T('prevention') - 0.05, ['ILLNESS MONEY:', '~THE MOST EXPENSIVE~'], x=70, y=300, align='left', sizes=[90, 100], anim='slam')
K(T('prevention') - 0.03, T('agar', T('investment')) - 0.05, ['PREVENTION:', '^AN INVESTMENT^'], x=1010, y=300, align='right', sizes=[90, 100], anim='slam')
cta = T('agar', T('investment')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want prevention in your life?', 'title': 'Comment<br>*"HEALTH PROTOCOL"*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'emi', r'mehngi', r'beemari', r'lifetime', r'zindagi', r'insurance', r'65%', r'pocket', r'jeb', r'bp', r'dawai', r'blood', r'test', r'doctor',
                           r'complication', r'kidney', r'heart', r'liver', r'lakh', r'irdai', r'2024', r'preexisting', r'waiting', r'36', r'months', r'trap',
                           r'healthy', r'middle', r'emergency', r'savings', r'financial', r'crisis', r'stress', r'vicious', r'cycle', r'protocol', r'110', r'85',
                           r'cholesterol', r'ldl', r'normal', r'control', r'psoriasis', r'bill', r'kam', r'prevention', r'investment'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

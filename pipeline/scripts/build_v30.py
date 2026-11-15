import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v30', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook: the most expensive EMI
Bh(0.05, T('car') - 0.05, 'EMI', size=420, font='anton', anim='slam', color=Y)
K(0.1, T('car') - 0.05, ['THE MOST EXPENSIVE ONE?'], x=540, y=1540, sizes=[70], font='oswald', anim='rise')
S.add({'type': 'chips', 't0': T('car') - 0.05, 't1': T('aur') - 0.05, 'y': 260, 'items': [
    {'t': T('car'), 'text': 'Car?'}, {'t': T('ghar'), 'text': 'Home?'}, {'t': T('beemari'), 'text': '*Your illness?*'}]})
K(T('aur') - 0.03, T('car', T('khatam')) - 0.05, ['THE EMI OF ILLNESS', '~NEVER ENDS~'], x=540, y=300, sizes=[84, 120], anim='slam')
e0 = T('car', T('khatam')) - 0.08; e1 = T('sab') - 0.08
S.card(e0, e1)
S.add({'type': 'compare', 't0': e0, 't1': e1, 'y': 170, 'title': 'How long you pay', 'max': 40, 'items': [
    {'t': T('5'), 'label': 'Car', 'unit': ' yrs', 'value': 5, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('20'), 'label': 'Home', 'unit': ' yrs', 'value': 20, 'cls': 'acc', 'color': 'linear-gradient(180deg,#FFD873,#E59A00)'},
    {'t': T('lifetime') - 0.2, 'label': 'Illness', 'text': 'LIFE', 'value': 40, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
# ---------------- insurance fails
K(T('sab') - 0.03, T('health') - 0.05, ['EVERYONE', '~OVERCOMPLICATES~ THIS'], x=540, y=300, sizes=[80, 96], anim='rise')
K(T('health') - 0.03, T('lekin', T('health')) - 0.05, ['MANY PEOPLE HAVE', '*HEALTH INSURANCE*'], x=70, y=300, align='left', sizes=[80, 100], anim='wipe')
K(T('lekin', T('health')) - 0.03, T('chalo') - 0.05, ['BUT WHEN YOU NEED IT,', '~IT DOESN\'T WORK~'], x=1010, y=300, align='right', sizes=[70, 96], anim='slam')
K(T('chalo') - 0.03, T('india') - 0.05, ["LET'S SEE WHY"], x=540, y=330, sizes=[110], anim='track')
Bh(T('india') - 0.03, T('monthly') - 0.05, '65%', size=420, font='anton', anim='slam', color=R)
K(T('out') - 0.05, T('monthly') - 0.05, ['OF MEDICAL COSTS IN INDIA:', '*FROM YOUR OWN POCKET*'], x=540, y=1520, sizes=[50, 64], font='oswald', anim='rise')
c0 = T('monthly') - 0.08; c1 = T('aur', T('instant')) - 0.08
S.card(c0, c1)
S.add({'type': 'chain', 't0': c0, 't1': c1, 'y': 150, 'title': 'What a lifestyle disease costs you', 'show': 4, 'items': [
    {'t': T('monthly'), 'text': 'Medicine: *Rs 500 - 3,000* a month'}, {'t': T('quarterly'), 'text': 'Blood tests: *Rs 1,500 - 3,000*'},
    {'t': T('visit'), 'text': 'Doctor visit: *Rs 500 - 1,000*'}, {'t': T('complications'), 'text': 'Complications: kidney, heart', 'st': 'up', 'stc': 'red'},
    {'t': T('lakh'), 'text': '~Rs 2 - 10 lakh~ instant bill', 'st': 'up', 'stc': 'red'}]})
B(18263, T('lakh') - 0.1, c1, off=0.8)
S.fx('sub_drop', T('lakh'), -12)
# ---------------- IRDAI rule
i0 = T('aur', T('instant')) - 0.05
K(i0, T('ne', i0) - 0.05, ['HEALTH INSURANCE +', '*IRDAI*'], x=540, y=300, sizes=[70, 120], anim='slam')
S.add({'type': 'badge', 't0': T('ne', i0) - 0.05, 't1': T('36') - 0.05, 'y': 260, 'text': 'New rule, 2024', 'sub': 'Pre-existing disease *waiting period*'})
Bh(T('36') - 0.05, T('matlab', T('36')) - 0.05, '36 MONTHS', size=260, font='anton', anim='slam', color=Y)
K(T('matlab', T('36')) - 0.03, T('ye', T('nahi', T('teen'))) - 0.05, ['DIAGNOSED WITH BP TODAY?', 'UP TO *3 YEARS* OF WAITING'], x=540, y=300, sizes=[64, 84], anim='rise', stagger=0.8)
Bh(T('trap') - 0.2, T('jab', T('trap')) - 0.05, 'THE TRAP', size=330, font='anton', anim='slam', color=R)
t0 = T('jab', T('trap')) - 0.08; t1 = T('middle') - 0.08
S.card(t0, t1)
S.add({'type': 'chain', 't0': t0, 't1': t1, 'y': 150, 'title': 'The insurance trap', 'show': 4, 'items': [
    {'t': T('healthy'), 'text': 'Healthy: *"I don\'t need insurance"*'}, {'t': T('beemar'), 'text': 'Fall ill: it *won\'t cover* you', 'st': 'no', 'stc': 'red'},
    {'t': T('preexisting', T('beemar')), 'text': 'Pre-existing = *waiting period*', 'st': 'no', 'stc': 'red'}, {'t': T('10'), 'text': '~Rs 10 lakh+~ spent by then', 'st': 'up', 'stc': 'red'}]})
# ---------------- middle class
K(T('middle') - 0.03, T('ek', T('middle')) - 0.05, ["THE MIDDLE CLASS'S", '*BIGGEST PROBLEM*'], x=540, y=300, sizes=[76, 100], anim='rise')
B(4701, T('ek', T('middle')) - 0.05, T('aur', T('upar')) - 0.05, off=1.0)
K(T('ek', T('middle')) - 0.03, T('aur', T('upar')) - 0.05, ['ONE EMERGENCY.', '~SAVINGS GONE.~'], x=540, y=300, sizes=[100, 110], anim='slam', stagger=0.9)
v0 = T('aur', T('upar')) - 0.08; v1 = T('toh', T('cycle')) - 0.08
S.card(v0, v1)
vn = [{'t': T('stress', v0 + 0.5) - 0.3, 'x': 500, 'y': 60, 'text': 'Financial *stress*'}, {'t': T('health', v0), 'x': 500, 'y': 215, 'text': 'Health gets *worse*'},
      {'t': T('kharab', v0) + 0.2, 'x': 500, 'y': 370, 'text': 'More *medical bills*'}, {'t': T('vicious'), 'x': 500, 'y': 530, 'text': '~A vicious cycle~', 'target': True}]
vw = [{'t': T('health', v0) - 0.3, 'd': 'M 500 105 L 500 165'}, {'t': T('kharab', v0), 'd': 'M 500 260 L 500 320'}, {'t': T('vicious') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': v0, 't1': v1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': vn, 'wires': vw})
# ---------------- what to do
d0 = T('toh', T('cycle')) - 0.08; d1 = T('lifestyle') - 0.08
S.card(d0, d1)
S.add({'type': 'checklist', 't0': d0, 't1': d1, 'y': 150, 'title': 'Do these 2 things', 'items': [
    {'t': T('health', d0), 'text': 'Buy insurance *while healthy*', 'mark': 'check'}, {'t': T('waiting', d0), 'text': 'Let the *waiting period* run out', 'mark': 'check'},
    {'t': T('protocols'), 'text': 'Follow a *health protocol*', 'mark': 'check'}, {'t': T('beemari', d0 + 3), 'text': 'So illness *never comes*', 'mark': 'check'}]})
K(T('lifestyle') - 0.03, T('comment') - 0.05, ['BUILD A', '*LIFESTYLE PROTOCOL*'], x=540, y=300, sizes=[80, 110], anim='slam')
S.add({'type': 'badge', 't0': T('comment') - 0.05, 't1': T('110') - 0.05, 'y': 260, 'text': 'Comment "LIFESTYLE PROTOCOL"', 'sub': "I'll send you *the protocol*"})
j0 = T('110') - 0.08; j1 = T('kyun', j0) - 0.08
S.card(j0, j1)
S.add({'type': 'stat', 't0': j0, 't1': j1, 'y': 200, 'kicker': 'My own journey', 'from': 110, 'to': 85, 'unit': ' KG', 'label': 'In *45 days*', 'pill': 'Water fasting + good food + training', 'dir': 'down', 'count': 1.4})
B(52079, T('workout') - 0.4, j1, off=1.0)
K(T('kyun', j0) - 0.03, T('agar', T('kyunki', j0)) - 0.05, ['STRONG', '*UP HERE*'], x=540, y=300, sizes=[130, 110], font='anton', anim='slam')
K(T('agar', T('kyunki', j0)) - 0.03, T('meri') - 0.05, ['YOU CAN', '*DO IT TOO*'], x=540, y=300, sizes=[110, 130], anim='rise', stagger=0.6)
f0 = T('meri') - 0.08; f1 = T('toh', T('insurance', T('meri'))) - 0.08
S.card(f0, f1)
S.add({'type': 'checklist', 't0': f0, 't1': f1, 'y': 150, 'title': 'My family today', 'items': [
    {'t': T('controlled'), 'text': "Wife's BP: *controlled*", 'mark': 'check'}, {'t': T('psoriasis'), 'text': "Mom's psoriasis: *improved*", 'mark': 'check'},
    {'t': T('bill', f0), 'text': 'Doctor bills: *covered by insurance*', 'mark': 'check'}]})
K(T('toh', T('insurance', T('meri'))) - 0.03, T('aur', T('mehnga')) - 0.05, ['ILLNESS MONEY:', '~THE MOST EXPENSIVE~'], x=70, y=300, align='left', sizes=[90, 100], anim='slam')
K(T('aur', T('mehnga')) - 0.03, T('toh', T('investment')) - 0.05, ['PREVENTION:', '^THE CHEAPEST INVESTMENT^'], x=1010, y=300, align='right', sizes=[90, 84], anim='slam')
cta = T('toh', T('investment')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want my protocol?', 'title': 'Comment<br>*"LIFESTYLE PROTOCOL"*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'emi', r'beemari', r'lifetime', r'mehnat', r'insurance', r'65%', r'pocket', r'jeb', r'dawai', r'blood', r'test', r'doctor',
                           r'complications', r'kidney', r'heart', r'lakh', r'irdai', r'2024', r'preexisting', r'waiting', r'36', r'months', r'bp', r'trap',
                           r'healthy', r'middle', r'emergency', r'savings', r'stress', r'vicious', r'cycle', r'protocols?', r'lifestyle', r'110', r'85', r'45',
                           r'fasting', r'workout', r'strong', r'controlled', r'psoriasis', r'covered', r'prevention', r'investment'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

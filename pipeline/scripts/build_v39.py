import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v39', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('sirf') - 0.05, ['GET LEAN WITHOUT', '*GIVING UP ANYTHING?*'], x=540, y=300, sizes=[84, 100], anim='slam')
Bh(T('40%') - 0.3, T('khaane') - 0.05, '-40%', size=440, font='anton', anim='slam', color=G)
K(T('glucose') - 0.1, T('khaane') - 0.05, ['GLUCOSE SPIKE'], x=540, y=1540, sizes=[70], font='oswald', anim='rise')
K(T('khaane') - 0.03, T('samjho', T('jaoge')) - 0.05, ['JUST CHANGE', 'THE *ORDER* YOU EAT IN'], x=540, y=300, sizes=[90, 96], anim='slam')
# ---------------- wash basin analogy
w0 = T('samjho', T('jaoge')) - 0.08; w1 = T('toh', T('lagegi')) - 0.08
S.card(w0, w1)
wn = [{'t': T('basin') - 0.1, 'x': 500, 'y': 60, 'text': 'Your gut = a *wash basin*'}, {'t': T('drain'), 'x': 500, 'y': 215, 'text': 'Blood sugar = the *drain pipe*'},
      {'t': T('waise'), 'x': 500, 'y': 370, 'text': 'Pour straight in: ~fast spike~'}, {'t': T('jaali'), 'x': 500, 'y': 530, 'text': 'Add a *fiber mesh* first', 'target': True}]
ww = [{'t': T('drain') - 0.3, 'd': 'M 500 105 L 500 165'}, {'t': T('waise') - 0.3, 'd': 'M 500 260 L 500 320'}, {'t': T('jaali') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': w0, 't1': T('toh', T('kavach')) - 0.05, 'y': 140, 'w': 1000, 'h': 640, 'nodes': wn, 'wires': ww})
S.add({'type': 'chain', 't0': T('toh', T('kavach')) - 0.05, 't1': w1, 'y': 150, 'title': 'With the fiber shield', 'show': 4, 'items': [
    {'t': T('slowly'), 'text': 'Carbs absorbed *slowly*', 'st': 'down', 'stc': 'green'}, {'t': T('dheere'), 'text': 'Insulin rises *gently*', 'st': 'yes', 'stc': 'green'},
    {'t': T('crash'), 'text': 'Gentle *crash*', 'st': 'yes', 'stc': 'green'}, {'t': T('bhookh'), 'text': '*Less hunger*', 'st': 'down', 'stc': 'green'}]})
# ---------------- the 4 steps
s0 = T('toh', T('lagegi')) - 0.08; s1 = T('toh', T('aate', T('bazaar'))) - 0.08
B(40531, T('kachcha') - 0.1, T('kheera') + 0.8, off=1.0)
K(s0, T('kachcha') - 0.05, ['STEP 1'], x=540, y=330, sizes=[140], font='anton', anim='slam')
K(T('kachcha') - 0.05, T('kheera') + 0.8, ['RAW *SALAD* FIRST'], x=540, y=330, sizes=[110], anim='slam')
S.card(T('kheera') + 0.8, T('step', T('protective')) - 0.08)
S.add({'type': 'checklist', 't0': T('kheera') + 0.8, 't1': T('step', T('protective')) - 0.08, 'y': 150, 'title': 'Step 1: raw salad', 'items': [
    {'t': T('kheera') + 0.8, 'text': 'Kheera, gajar, tamatar', 'mark': 'check'}, {'t': T('resistant'), 'text': 'Acts like *resistant starch*', 'mark': 'check'},
    {'t': T('protective'), 'text': '*Protective layer* in your gut', 'mark': 'check'}, {'t': T('slow', T('protective')), 'text': 'Slows the *spike* and the *crash*', 'mark': 'check'}]})
q0 = T('step', T('protective')) - 0.08
S.card(q0, s1)
S.add({'type': 'chain', 't0': q0, 't1': s1, 'y': 150, 'title': 'The plate order', 'show': 4, 'items': [
    {'t': T('step', T('protective')), 'text': 'Step 2: *50% sabzi*'}, {'t': T('daal'), 'text': 'Step 3: *50% daal / protein*'},
    {'t': T('soyabean'), 'text': 'Veg: *soyabean, tofu*'}, {'t': T('step', T('tofu')), 'text': 'Step 4: roti / chawal, *very little*'},
    {'t': T('gluten', T('tofu')), 'text': 'Market atta: *high gluten*', 'st': 'up', 'stc': 'red'}]})
g0 = T('toh', T('aate', T('bazaar'))) - 0.08; g1 = T('aur', T('16%')) - 0.08
S.card(g0, g1)
S.add({'type': 'compare', 't0': g0, 't1': g1, 'y': 170, 'title': 'Gluten in atta', 'max': 16, 'items': [
    {'t': T('56%') - 0.1, 'label': 'Home-ground', 'text': '5-6', 'unit': '%', 'value': 6, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('pandrah') - 0.1, 'label': 'Packaged', 'text': '15-16', 'unit': '%', 'value': 16, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
# ---------------- meal sequencing
Bh(T('aur', T('16%')) - 0.03, T('jo', T('sequencing')) - 0.05, 'MEAL SEQUENCING', size=190, font='anton', anim='slam', color=G)
S.add({'type': 'stat', 't0': T('jo', T('sequencing')) - 0.05, 't1': T('aur', T('spike', T('less'))) - 0.05, 'y': 260, 'kicker': 'Same food, different order', 'from': 0, 'to': 40, 'unit': '%', 'label': '*Lower* glucose spike', 'pill': 'Proven in studies', 'dir': 'down', 'count': 1.0})
K(T('aur', T('spike', T('less'))) - 0.03, T('jo', T('ancestors')) - 0.05, ['OUR *ANCESTORS*', 'ALREADY DID THIS'], x=540, y=300, sizes=[90, 90], anim='rise')
B(4764, T('jo', T('ancestors')) - 0.05, T('carb', T('ancestors')) - 0.05, off=0.5)
K(T('jo', T('ancestors')) - 0.03, T('2024') - 1.05, ['SALAD. PROTEIN.', 'THEN *CARBS*.'], x=540, y=330, sizes=[100, 110], anim='rise', stagger=1.2)
S.add({'type': 'badge', 't0': T('2024') - 1.0, 't1': T('but', T('2024')) - 0.3, 'y': 260, 'text': 'Research, 2024', 'sub': 'Proved what our *grandparents* did'})
K(T('but', T('2024')) - 0.28, T('khoob') - 0.05, ['DAADI-DADA ATE THIS WAY.', '*NO FAT.*'], x=540, y=300, sizes=[70, 120], anim='slam')
B(40765, T('khoob') - 0.05, T('par', T('rahe', T('10', T('2525')))) - 0.05, off=1.0)
S.add({'type': 'compare', 't0': T('2525') - 0.05, 't1': T('par', T('rahe', T('10', T('2525')))) - 0.05, 'y': 170, 'title': 'Steps a day', 'max': 25, 'items': [
    {'t': T('2525'), 'label': 'Then', 'unit': 'K', 'value': 25, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('10', T('2525')), 'label': 'Now', 'text': '<10', 'unit': 'K', 'value': 10, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
# ---------------- the full day
K(T('par', T('rahe', T('10', T('2525')))) - 0.03, T('aap', T('trick')) + 0.6, ['BUT THIS IS', 'JUST *ONE TRICK*'], x=540, y=300, sizes=[90, 110], anim='slam')
d0 = T('aap', T('trick')) + 0.6; d1 = T('aur', T('mote')) - 0.08
S.card(d0, d1)
S.add({'type': 'chain', 't0': d0, 't1': d1, 'y': 150, 'title': 'All day long', 'show': 4, 'items': [
    {'t': T('chai'), 'text': 'From *morning chai* onwards'}, {'t': T('spike', T('chai')), 'text': 'Every spike', 'st': 'up', 'stc': 'red'},
    {'t': T('crash', T('chai')), 'text': '= a *crash*', 'st': 'down', 'stc': 'red'}, {'t': T('bhookh', T('chai')), 'text': '= more *hunger*', 'st': 'up', 'stc': 'red'},
    {'t': T('khaoge'), 'text': '= more *eating*', 'st': 'up', 'stc': 'red'}, {'t': T('mote'), 'text': '~You keep gaining~', 'st': 'no', 'stc': 'red'}]})
K(T('aur', T('mote')) - 0.03, T('comment') - 0.05, ['HOW I CONTROLLED IT:', 'MY *HEALTH PROTOCOL*'], x=540, y=300, sizes=[76, 100], anim='rise', stagger=0.8)
cta = T('comment') - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want the full system?', 'title': 'Comment<br>*"HEALTH PROTOCOL"*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'patle', r'glucose', r'spike', r'40%', r'order', r'basin', r'drain', r'carb', r'jaali', r'fiber', r'kavach', r'slowly', r'insulin',
                           r'crash', r'bhookh', r'step', r'salad', r'kheera', r'gajar', r'tamatar', r'resistant', r'starch', r'gut', r'protective', r'sabzi',
                           r'daal', r'protein', r'anda', r'chicken', r'soyabean', r'tofu', r'roti', r'chawal', r'gluten', r'gehun', r'56%', r'16%', r'sequencing',
                           r'studies', r'ancestors', r'traditional', r'2024', r'research', r'daadi', r'steps', r'trick', r'chai', r'mote', r'protocol'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

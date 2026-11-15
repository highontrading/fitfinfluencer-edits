import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v29', mood='energetic'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('isko') - 0.05, ['ONE EXERCISE THAT CAN', '*LOWER YOUR BP*'], x=540, y=300, sizes=[70, 110], anim='slam')
Bh(T('isko') - 0.03, T('aur') - 0.05, 'WALL SIT', size=330, font='anton', anim='slam', color=G)
K(T('aur') - 0.03, T('ismein', T('jaana')) - 0.05, ['NO GYM.'], x=70, y=300, align='left', sizes=[130], font='anton', anim='slam')
K(T('ismein', T('jaana')) - 0.03, T('bas') - 0.05, ['NO RUNNING.'], x=1010, y=300, align='right', sizes=[130], font='anton', anim='slam')
K(T('bas') - 0.03, T('jis') - 0.05, ['JUST *A WALL.*'], x=540, y=330, sizes=[130], anim='slam')
S.add({'type': 'checklist', 't0': T('jis') - 0.05, 't1': T('but') - 0.05, 'y': 220, 'title': 'The wall sit', 'items': [
    {'t': T('peeth'), 'text': 'Back flat on the wall', 'mark': 'check'}, {'t': T('90', T('peeth')), 'text': 'Hold for *90 seconds*', 'mark': 'check'},
    {'t': T('degree'), 'text': 'Knees at *90 degrees*', 'mark': 'check'}, {'t': T('jitna'), 'text': 'As long as you can', 'mark': 'check'}]})
K(T('but') - 0.03, T('ab') - 0.05, ['NOTHING IS', '*SIMPLER*'], x=540, y=330, sizes=[100, 140], anim='slam')
K(T('ab') - 0.03, T('toh', T('giraayegi')) - 0.05, ['BUT HOW DOES IT', '*LOWER BP?*'], x=540, y=300, sizes=[84, 120], anim='rise', stagger=0.5)
K(T('toh', T('giraayegi')) - 0.03, T('jab') - 0.05, ['THE SCIENCE IS', '*FASCINATING*'], x=540, y=300, sizes=[80, 110], anim='track')
# ---------------- mechanism
m0 = T('jab') - 0.08; m1 = T('aur', T('contraction')) - 0.08
S.card(m0, m1)
mn = [{'t': T('squeeze') - 0.2, 'x': 500, 'y': 60, 'text': 'Muscles *squeeze*'}, {'t': T('move'), 'x': 500, 'y': 215, 'text': 'But nothing *moves*'},
      {'t': T('isometric'), 'x': 500, 'y': 400, 'text': '= *Isometric contraction*', 'target': True}]
mw = [{'t': T('move') - 0.3, 'd': 'M 500 105 L 500 165'}, {'t': T('isometric') - 0.3, 'd': 'M 500 260 L 500 345'}]
S.add({'type': 'flow', 't0': m0, 't1': m1, 'y': 160, 'w': 1000, 'h': 520, 'nodes': mn, 'wires': mw})
c0 = m1 + 0.02; c1 = T('aur', T('improve')) - 0.08
S.card(c0, c1)
S.add({'type': 'chain', 't0': c0, 't1': c1, 'y': 150, 'title': 'What happens to your vessels', 'show': 4, 'items': [
    {'t': T('compress'), 'text': 'Blood vessels *compress*'}, {'t': T('restrict'), 'text': 'Blood flow *restricted*', 'st': 'down', 'stc': 'red'},
    {'t': T('rush'), 'text': 'Release: *blood rushes in*', 'st': 'up', 'stc': 'green'}, {'t': T('dilate'), 'text': 'Vessels *dilate*', 'st': 'up', 'stc': 'green'},
    {'t': T('flexible'), 'text': 'Repeat: vessels get *flexible*', 'st': 'yes', 'stc': 'green'}, {'t': T('endothelium'), 'text': '*Endothelium* works better', 'st': 'yes', 'stc': 'green'}]})
S.fx('ding', T('improve'), -14)
K(T('aur', T('improve')) - 0.03, T('nitric') - 0.35, ['THE MOST', '*IMPORTANT PART*'], x=540, y=300, sizes=[90, 110], anim='rise')
Bh(T('nitric') - 0.3, T('yaani', T('vasodilator')) - 0.05, 'NITRIC OXIDE', size=220, font='anton', anim='slam', color=G)
S.add({'type': 'badge', 't0': T('vasodilator') - 0.3, 't1': T('yaani', T('vasodilator')) - 0.05, 'y': 1500, 'text': "Your body's natural *vasodilator*"})
K(T('yaani', T('vasodilator')) - 0.03, T('2025') - 0.05, ['WHAT BP MEDICINE DOES,', '*NITRIC OXIDE* DOES TOO'], x=540, y=300, sizes=[64, 84], font='oswald', anim='rise', stagger=0.6)
# ---------------- evidence
e0 = T('2025') - 0.08
K(e0, T('isometric', e0) - 0.05, ['2025 META-ANALYSIS'], x=540, y=300, sizes=[100], anim='slam')
S.add({'type': 'chips', 't0': T('30', e0) - 0.1, 't1': T('isometric', e0) - 0.05, 'y': 460, 'items': [
    {'t': T('30', e0), 'text': '*30* studies'}, {'t': T('1700'), 'text': '*1,700* participants'}]})
r0 = T('isometric', e0) - 0.08; r1 = T('british') - 0.08
S.card(r0, r1)
S.add({'type': 'compare', 't0': r0, 't1': r1, 'y': 170, 'title': 'BP drop from isometric exercise', 'max': 7, 'items': [
    {'t': T('systolic') - 0.1, 'label': 'Systolic', 'unit': ' mmHg', 'value': 7, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('diastolic') - 0.1, 'label': 'Diastolic', 'unit': ' mmHg', 'value': 3, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
K(T('british') - 0.03, T('sabse', T('british')) - 0.05, ['BRITISH JOURNAL OF', '*SPORTS MEDICINE*'], x=540, y=300, sizes=[70, 90], font='serif', anim='type')
K(T('sabse', T('british')) - 0.03, T('wo', T('reduction')) - 0.05, ['MOST EFFECTIVE', 'EXERCISE FOR *BP?*'], x=540, y=300, sizes=[90, 100], anim='rise')
Bh(T('wo', T('reduction')) - 0.03, T('running') - 0.05, 'ISOMETRIC', size=300, font='anton', anim='slam', color=Y)
B(722, T('running') - 0.05, T('swimming') - 0.05, off=1.0)
K(T('running') - 0.03, T('swimming') - 0.05, ['BEATS *RUNNING*'], x=540, y=330, sizes=[120], anim='slam')
B(3168, T('swimming') - 0.05, T('weight') - 0.05, off=1.0)
K(T('swimming') - 0.03, T('weight') - 0.05, ['BEATS *SWIMMING*'], x=540, y=330, sizes=[120], anim='slam')
B(40248, T('weight') - 0.05, T('toh', T('training')) - 0.05, off=1.0)
K(T('weight') - 0.03, T('toh', T('training')) - 0.05, ['BEATS *WEIGHTS*'], x=540, y=330, sizes=[120], anim='slam')
S.add({'type': 'badge', 't0': T('toh', T('training')) - 0.05, 't1': T('kaise', T('gira', T('isometric', T('training')))) - 0.05, 'y': 260, 'text': 'Isometric exercise', 'sub': 'Lowers BP *the best*'})
# ---------------- how to
h0 = T('kaise', T('gira', T('isometric', T('training')))) - 0.08; h1 = T('meri') - 0.08
S.card(h0, h1)
S.add({'type': 'checklist', 't0': h0, 't1': h1, 'y': 150, 'title': 'How to do it', 'items': [
    {'t': T('back'), 'text': 'Back *against the wall*', 'mark': 'check'}, {'t': T('90', T('back')), 'text': 'Knees at *90 degrees*', 'mark': 'check'},
    {'t': T('jitni'), 'text': 'Hold as long as you can', 'mark': 'check'}, {'t': T('minute'), 'text': '*1 to 2 minutes*', 'mark': 'check'},
    {'t': T('regular'), 'text': 'Do it *regularly*', 'mark': 'check'}]})
# ---------------- wife
w0 = T('meri') - 0.05; w1 = T('aapke', w0) - 0.08
K(w0, T('deewar', w0) - 0.05, ['MY WIFE', 'DID THIS TOO'], x=540, y=300, sizes=[100, 90], anim='slam')
S.card(T('deewar', w0) - 0.08, w1)
S.add({'type': 'compare', 't0': T('deewar', w0) - 0.08, 't1': w1, 'y': 170, 'title': 'Her wall sit', 'max': 120, 'items': [
    {'t': T('30', w0) - 0.1, 'label': 'First 3 days', 'unit': 's', 'value': 25, 'text': '<30', 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('do', T('aaj')) - 0.1, 'label': 'Today', 'unit': ' min', 'value': 120, 'text': '2', 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
# ---------------- no excuses
K(T('aapke', w0) - 0.03, T('deewar', T('hongi')) - 0.05, ['NO GYM?', 'NO EQUIPMENT?'], x=70, y=300, align='left', sizes=[110, 110], anim='rise', stagger=0.9)
K(T('deewar', T('hongi')) - 0.03, T('wo', T('aapko')) - 0.05, ['THERE IS A WALL', '*EVERYWHERE*'], x=1010, y=300, align='right', sizes=[90, 120], anim='slam')
S.add({'type': 'stamp', 't0': T('bahaana') - 0.2, 't1': T('main', T('bahaana')) - 0.05, 'y': 1180, 'text': 'NO EXCUSES', 'rot': -7, 'size': 120}); S.punch(T('bahaana'), 0.14, 0.7)
K(T('main', T('bahaana')) - 0.03, T('mera') - 0.05, ["IT'S PROVEN.", '*START TODAY.*'], x=540, y=300, sizes=[100, 120], anim='rise', stagger=0.8)
cta = T('mera') - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Try it today', 'title': 'Save this<br>*wall sit*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'SAVE', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'exercise', r'bp', r'wall', r'sit', r'gym', r'deewar', r'90', r'second', r'degree', r'simple', r'science', r'squeeze',
                           r'isometric', r'contraction', r'blood', r'vessels', r'compress', r'restrict', r'rush', r'dilate', r'flexible', r'endothelium',
                           r'nitric', r'oxide', r'vasodilator', r'telmisartan', r'2025', r'30', r'1700', r'systolic', r'diastolic', r'mmhg', r'running',
                           r'swimming', r'weight', r'minute', r'wife', r'target', r'equipment', r'bahaana', r'proven'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

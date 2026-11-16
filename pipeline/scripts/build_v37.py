import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v37', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('phir', T('washroom')) - 0.05, ['I DRANK', '*3-4 LITRES* A DAY'], x=540, y=300, sizes=[90, 110], anim='slam')
K(T('phir', T('washroom')) - 0.05, T('pata') - 0.05, ['STILL ~THIRSTY~'], x=540, y=330, sizes=[130], font='anton', anim='slam')
K(T('pata') - 0.03, T('aap') - 0.05, ['I WASN\'T DRINKING', 'WATER *THE RIGHT WAY*'], x=540, y=300, sizes=[80, 96], anim='rise', stagger=0.7)
Bh(T('h2o') - 0.2, T('har') - 0.05, 'H2O', size=440, font='anton', anim='slam', color=Y)
K(T('chemical') - 0.1, T('h2o') - 0.25, ['JUST A *CHEMICAL*'], x=540, y=1540, sizes=[64], font='oswald', anim='rise')
K(T('hydrogen') - 0.1, T('har') - 0.05, ['2 HYDROGEN + 1 OXYGEN. THAT\'S IT.'], x=540, y=1540, sizes=[52], font='oswald', anim='rise')
K(T('har') - 0.03, T('stream') - 0.05, ['WHICH WATER', 'SHOULD YOU DRINK?'], x=540, y=300, sizes=[90, 100], anim='rise')
B(50576, T('stream') - 0.05, T('pattharon') - 0.05, off=1.0)
K(T('stream') - 0.03, T('pattharon') - 0.05, ['STREAMS. *RIVERS.*'], x=540, y=330, sizes=[110], anim='slam')
B(2186, T('pattharon') - 0.05, T('tabhi') - 0.05, off=1.0)
K(T('pattharon') - 0.03, T('tabhi') - 0.05, ['WATER THAT FLOWED', 'OVER *ROCKS*'], x=540, y=330, sizes=[90, 120], anim='rise')
m0 = T('tabhi') - 0.08; m1 = T('phir', T('h2o', T('banta'))) - 0.08
S.card(m0, m1)
S.add({'type': 'checklist', 't0': m0, 't1': m1, 'y': 150, 'title': 'Minerals it picks up', 'items': [
    {'t': T('calcium'), 'text': 'Calcium', 'mark': 'check'}, {'t': T('magnesium'), 'text': 'Magnesium', 'mark': 'check'},
    {'t': T('sodium'), 'text': 'Sodium', 'mark': 'check'}, {'t': T('potassium'), 'text': 'Potassium', 'mark': 'check'}]})
# ---------------- RO
K(T('phir', T('h2o', T('banta'))) - 0.03, T('ro') - 0.05, ['THEN CAME', '~POLLUTION~'], x=540, y=300, sizes=[90, 120], anim='slam')
S.add({'type': 'chips', 't0': T('ro') - 0.3, 't1': T('par', T('kiya')) - 0.05, 'y': 240, 'items': [
    {'t': T('filter'), 'text': 'Filters'}, {'t': T('ro'), 'text': 'RO'}, {'t': T('gandagi'), 'text': 'Dirt removed: *good*'}]})
Bh(T('par', T('kiya')) - 0.03, T('india') - 0.05, 'ZERO MINERALS', size=210, font='anton', anim='slam', color=R)
K(T('maar') - 0.6, T('india') - 0.05, ['RO KILLS ALL THE ~MINERALS~ TOO'], x=540, y=1540, sizes=[52], font='oswald', anim='rise')
K(T('india') - 0.03, T('is', T('dikhaunga')) - 0.05, ["INDIA'S WATER:", '~IN BAD SHAPE~'], x=540, y=300, sizes=[84, 110], anim='slam')
S.add({'type': 'badge', 't0': T('is', T('dikhaunga')) - 0.05, 't1': T('ab', T('follow')) - 0.05, 'y': 260, 'text': 'Research papers coming', 'sub': '*Follow* this channel'})
# ---------------- intra vs extra
x0 = T('ab', T('follow')) - 0.08; x1 = T('aur', T('dehydrated', T('dehydrated'))) - 0.08
S.card(x0, x1)
S.add({'type': 'compare', 't0': x0, 't1': x1, 'y': 170, 'title': 'Two kinds of body water', 'max': 10, 'items': [
    {'t': T('intracellular', T('extracellular')), 'label': 'Intracellular', 'text': 'INSIDE', 'value': 10, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('extracellular', T('karata')), 'label': 'Extracellular', 'text': 'OUTSIDE', 'value': 3, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
K(T('organs') - 0.1, T('extracellular', T('karata')) - 0.05, ['RUNS YOUR *ORGANS*, BRAIN, REACTIONS'], x=540, y=760, sizes=[44], font='oswald', anim='rise')
K(T('guzar') - 0.1, x1, ['JUST *PASSES THROUGH*: MOUTH TO BLADDER'], x=540, y=760, sizes=[44], font='oswald', anim='rise')
S.add({'type': 'stamp', 't0': x1 + 0.1, 't1': x1 + 1.3, 'y': 1180, 'text': 'DEHYDRATED', 'rot': -7, 'size': 120}); S.punch(x1 + 0.1, 0.14, 0.7)
# ---------------- brain dehydration
b0 = T('aur', T('dehydrated', T('dehydrated'))) - 0.05
K(b0 + 1.25, T('sirf', b0) - 0.05, ['YOUR *BRAIN*', 'DEHYDRATES TOO'], x=540, y=300, sizes=[96, 96], anim='rise')
c0 = T('sirf', b0) - 0.08; c1 = T('sochiye') - 0.08
S.card(c0, c1)
S.add({'type': 'stat', 't0': c0, 't1': T('memory') - 0.08, 'y': 220, 'kicker': 'Just', 'from': 0, 'to': 2, 'unit': '%', 'label': 'Dehydration drops your *cognitive skills*', 'dir': 'down', 'count': 0.6})
S.add({'type': 'checklist', 't0': T('memory') - 0.08, 't1': c1, 'y': 150, 'title': 'What 2% dehydration does', 'items': [
    {'t': T('memory'), 'text': '*Memory* slows', 'mark': 'x'}, {'t': T('mood'), 'text': '*Mood* disturbed', 'mark': 'x'},
    {'t': T('focus'), 'text': '*Focus* breaks', 'mark': 'x'}, {'t': T('decision'), 'text': '*Decision making* weakens', 'mark': 'x'}]})
B(4607, T('sochiye') - 0.05, T('ye', T('raha', T('focus', T('sochiye')))) - 0.05, off=1.0)
K(T('sochiye') - 0.03, T('meeting') - 0.05, ['3 LITRES A DAY.', '~STILL NO FOCUS.~'], x=540, y=330, sizes=[90, 100], anim='rise', stagger=1.2)
K(T('pandemic') - 0.2, T('meeting') - 0.05, ['A *PANDEMIC*'], x=540, y=1540, sizes=[70], font='oswald', anim='rise')
S.add({'type': 'chips', 't0': T('meeting') - 0.05, 't1': T('aur', T('cheezein', T('sprain'))) - 0.05, 'y': 240, 'items': [
    {'t': T('meeting'), 'text': 'Blank in *meetings*'}, {'t': T('irritated'), 'text': '*Irritated* by evening'}, {'t': T('sprain'), 'text': '*Sprains* at the gym'},
    {'t': T('muscles'), 'text': 'Muscles *pulling*'}]})
# ---------------- the fix
f0 = T('aur', T('cheezein', T('sprain'))) - 0.05
K(f0, T('sea') - 0.05, ['THE FIX?', 'SIMPLE *KHAARI NAMAK*'], x=540, y=300, sizes=[96, 100], anim='slam')
Bh(T('sea') - 0.03, T('aur', T('jaayenge')) - 0.05, 'SEA SALT', size=320, font='anton', anim='slam', color=G)
K(T('paani', T('sea')) - 0.1, T('aur', T('jaayenge')) - 0.05, ['A PINCH IN YOUR WATER = *ALL THE MINERALS*'], x=540, y=1540, sizes=[48], font='oswald', anim='rise')
K(T('aur', T('jaayenge')) - 0.03, T('toh', T('diye', T('protocol'))) - 0.05, ['PART OF MY', '*HEALTH PROTOCOL*'], x=540, y=300, sizes=[90, 110], anim='rise')
cta = T('toh', T('diye', T('protocol'))) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want the protocol?', 'title': 'Comment<br>*"HP"*', 'sub': "I'll send you the link.", 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'litre', r'paani', r'pyaas', r'washroom', r'chemical', r'h2o', r'hydrogen', r'oxygen', r'stream', r'nadiyon', r'pattharon',
                           r'minerals', r'calcium', r'magnesium', r'sodium', r'potassium', r'pollution', r'filter', r'ro', r'gandagi', r'india', r'research',
                           r'follow', r'intracellular', r'extracellular', r'organs', r'brain', r'bladder', r'dehydrated', r'dehydration', r'2%', r'cognitive',
                           r'memory', r'mood', r'focus', r'decision', r'pandemic', r'meeting', r'irritated', r'gym', r'sprain', r'muscles', r'namak', r'sea',
                           r'salt', r'protocol', r'hp'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

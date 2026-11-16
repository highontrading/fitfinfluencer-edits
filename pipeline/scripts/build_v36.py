import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v36', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('poha') - 0.05, ['WHAT DID YOU EAT', 'THIS MORNING?'], x=540, y=300, sizes=[84, 100], anim='slam')
S.add({'type': 'chips', 't0': T('poha') - 0.05, 't1': T('healthy') - 0.05, 'y': 240, 'items': [
    {'t': T('poha'), 'text': 'Poha?'}, {'t': T('upma'), 'text': 'Upma?'}, {'t': T('aloo'), 'text': 'Aloo paratha?'}, {'t': T('bread'), 'text': 'Bread butter?'}]})
K(T('healthy') - 0.03, T('par') - 0.05, ['YOU THOUGHT IT', 'WAS *HEALTHY*'], x=540, y=300, sizes=[90, 110], anim='rise')
Bh(T('par') - 0.03, T('ab', T('pehne')) - 0.05, 'NAKED CARBS', size=230, font='anton', anim='slam', color=R)
K(T('kapde') - 0.1, T('ab', T('pehne')) - 0.05, ['CARBS WITH ~NO CLOTHES ON~'], x=540, y=1540, sizes=[60], font='oswald', anim='rise')
c0 = T('ab', T('pehne')) - 0.08; c1 = T('ab', T('meal')) - 0.08
S.card(c0, c1)
S.add({'type': 'checklist', 't0': c0, 't1': c1, 'y': 150, 'title': "A carb's clothes", 'items': [
    {'t': T('fiber'), 'text': 'A layer of *fiber*', 'mark': 'check'}, {'t': T('protein'), 'text': 'A layer of *protein*', 'mark': 'check'},
    {'t': T('proper'), 'text': '= A *proper meal*', 'mark': 'check'}]})
# ---------------- the spike and crash
s0 = T('ab', T('meal')) - 0.08; s1 = T('ab', T('aankh')) - 0.08
S.card(s0, s1)
S.add({'type': 'chain', 't0': s0, 't1': s1, 'y': 150, 'title': 'What a naked carb does', 'show': 4, 'items': [
    {'t': T('glucose', s0), 'text': 'Breaks down into *glucose*'}, {'t': T('bloodstream'), 'text': 'Straight into the *bloodstream*'},
    {'t': T('spike', s0), 'text': 'Blood sugar *spikes fast*', 'st': 'up', 'stc': 'red'}, {'t': T('pancreas'), 'text': 'Pancreas: *"Release insulin!"*'},
    {'t': T('aggressive'), 'text': 'Insulin comes *aggressive*', 'st': 'up', 'stc': 'red'}, {'t': T('dhakel'), 'text': 'Glucose shoved into cells'},
    {'t': T('crash'), 'text': '~Sugar crash~', 'st': 'down', 'stc': 'red'}, {'t': T('energy'), 'text': 'Brain energy: *gone*', 'st': 'down', 'stc': 'red'},
    {'t': T('neend'), 'text': 'Sleepy, *lethargic*', 'st': 'no', 'stc': 'red'}, {'t': T('focus'), 'text': '*Focus* gone', 'st': 'no', 'stc': 'red'}]})
S.fx('sub_drop', T('crash'), -12)
K(T('do', T('focus')) - 0.03, T('ab', T('aankh')) - 0.05, ['EYES CLOSING', 'BY *2-3 PM*'], x=540, y=780, sizes=[64, 80], anim='rise')
# ---------------- dress it up
d0 = T('ab', T('aankh')) - 0.05
K(d0, T('pehle', d0) - 0.05, ['NOW', '*DRESS IT UP*'], x=540, y=300, sizes=[96, 130], anim='slam')
e0 = T('pehle', d0) - 0.08; e1 = T('ab', T('protein', T('anda'))) - 0.08
S.card(e0, e1)
S.add({'type': 'checklist', 't0': e0, 't1': e1, 'y': 150, 'title': 'The same poha, dressed up', 'items': [
    {'t': T('salad'), 'text': 'First, *salad*: kheera, tamatar', 'mark': 'check'}, {'t': T('resistant'), 'text': 'Fiber: *resistant starch*', 'mark': 'check'},
    {'t': T('slowly'), 'text': 'Digests *slowly*, layers your gut', 'mark': 'check'},
    {'t': T('sprouts'), 'text': 'Sprouts, chana, *boiled egg*', 'mark': 'check'},
    {'t': T('protein', T('anda')), 'text': '= Your *protein*', 'mark': 'check'}]})
g0 = T('ab', T('protein', T('anda'))) - 0.08; g1 = T('toh', T('lagegi')) - 0.08
S.card(g0, g1)
gn = [{'t': g0 + 0.3, 'x': 500, 'y': 60, 'text': 'Glucose released *slowly*'}, {'t': T('gently', T('slowly', g0)), 'x': 500, 'y': 215, 'text': 'Insulin rises *gently*'},
      {'t': T('crash', g0), 'x': 500, 'y': 370, 'text': '^No crash^'}, {'t': T('bhookh'), 'x': 500, 'y': 530, 'text': 'No *hunger* after meals', 'target': True}]
gw = [{'t': T('gently', T('slowly', g0)) - 0.3, 'd': 'M 500 105 L 500 165'}, {'t': T('crash', g0) - 0.3, 'd': 'M 500 260 L 500 320'}, {'t': T('bhookh') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': g0, 't1': g1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': gn, 'wires': gw})
S.fx('ding', T('crash', g0), -14)
K(T('toh', T('lagegi')) - 0.03, T('carb', T('galat')) - 0.05, ['POHA IS', '^NOT THE PROBLEM^'], x=540, y=300, sizes=[90, 120], anim='slam')
K(T('carb', T('galat')) - 0.03, T('aur', T('mote')) - 0.05, ['CARBS: ^FINE^', 'NAKED CARBS: ~THE PROBLEM~'], x=540, y=300, sizes=[96, 84], anim='slam', stagger=1.0)
# ---------------- every meal
m0 = T('aur', T('mote')) - 0.08; m1 = T('maine') - 0.08
S.card(m0, m1)
S.add({'type': 'chips', 't0': m0, 't1': m1, 'y': 200, 'items': [
    {'t': T('breakfast'), 'text': 'Breakfast'}, {'t': T('lunch'), 'text': 'Lunch'}, {'t': T('dinner'), 'text': 'Dinner'}, {'t': T('snacks'), 'text': 'Snacks'},
    {'t': T('management'), 'text': '= *Glucose management*'}, {'t': T('personalized'), 'text': 'All *personalized*'}]})
# ---------------- my journey
K(T('maine') - 0.03, T('main', T('kami')) - 0.05, ['WHEN I LOST', 'MY WEIGHT'], x=540, y=300, sizes=[96, 110], anim='rise')
K(T('main', T('kami')) - 0.03, T('toh', T('dekhta')) - 0.05, ['I WORE A', '*GLUCOSE METER*'], x=70, y=300, align='left', sizes=[90, 110], anim='slam')
Bh(T('architecture') - 0.4, T('aur', T('architecture')) + 2.0, 'MEAL ARCHITECTURE', size=180, font='anton', anim='slam', color=G)
K(T('khoobsurat') - 0.1, T('jab', T('confidence')) - 0.05, ['MY BODY SAYS', '*THANK YOU*'], x=540, y=300, sizes=[96, 130], anim='slam')
K(T('halka') - 0.1, T('jab', T('confidence')) - 0.05, ['LIGHTER. BETTER.', '^CONFIDENT AGAIN.^'], x=540, y=1540, sizes=[56, 64], font='oswald', anim='rise', stagger=0.8)
K(T('jab', T('confidence')) - 0.03, T('mera', T('soch')) - 0.4, ['A PLATE BUILT', 'ON *SCIENCE*'], x=540, y=300, sizes=[96, 120], anim='slam')
cta = T('mera', T('soch')) - 0.35
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Dress up your carbs', 'title': 'Follow for<br>*more science*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'poha', r'upma', r'paratha', r'bread', r'healthy', r'naked', r'carbs?', r'kapde', r'fiber', r'protein', r'meal', r'glucose',
                           r'bloodstream', r'spike', r'pancreas', r'insulin', r'crash', r'energy', r'neend', r'lethargic', r'focus', r'salad', r'resistant',
                           r'starch', r'gut', r'sprouts', r'chane', r'anda', r'slowly', r'gently', r'bhookh', r'galat', r'breakfast', r'lunch', r'dinner',
                           r'snacks', r'personalized', r'meter', r'architecture', r'confidence', r'thaali', r'science'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

import sys
from spec_lib2 import Spec
import mc_theme as MC
S = Spec(sys.argv[1], 'v47', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; IV = '#EDE7DA'; CH = '#CDB98B'; K = S.kin; Bh = S.behind; B = lambda *a, **k: S.broll(*a, bright=-0.17, sat=0.78, **k)  # brand grade: darker, softer film look
# ---------------- hook
B(4344, 0.0, T('but') - 0.05, off=0.5)
K(0.05, T('but') - 0.05, ['MOST PEOPLE EAT BEFORE A RAVE', 'like a *dinner date*'], x=540, y=300, sizes=[56, 100], anim='rise', stagger=0.9)
Bh(T('but') - 0.03, T('ill') - 0.05, '6 HOURS', size=280, font='mc', anim='slam', color=IV)
K(T('six') + 0.3, T('ill') - 0.05, ['ON YOUR FEET'], x=540, y=1600, sizes=[52], font='label', anim='rise')
K(T('ill') - 0.03, T('your', T('hospital')) - 0.05, ['WHAT TO EAT.', 'AND *the water mistake*'], x=540, y=300, sizes=[96, 90], anim='rise', stagger=1.0)
K(T('biggest') - 0.1, T('your', T('hospital')) - 0.05, ['THE ONE THAT SENDS PEOPLE TO HOSPITAL'], x=540, y=1600, sizes=[34], font='label', anim='rise', fit=980)
# ---------------- glycogen
g0 = T('your', T('hospital')) - 0.08; g1 = T('so') - 0.08
S.card(g0, g1)
gn = [{'t': g0 + 0.2, 'x': 500, 'y': 60, 'text': 'Muscles run on *glycogen*'}, {'t': T('stored', T('glycogen')) - 0.1, 'x': 500, 'y': 215, 'text': 'Stored in *muscles + liver*'},
      {'t': T('dance') - 0.1, 'x': 500, 'y': 370, 'text': 'Dance for hours: *you burn it*'}, {'t': T('carbs') - 0.1, 'x': 500, 'y': 530, 'text': 'CARBS REFILL IT', 'target': True}]
gw = [{'t': T('stored', T('glycogen')) - 0.4, 'd': 'M 500 105 L 500 165'}, {'t': T('dance') - 0.4, 'd': 'M 500 260 L 500 320'}, {'t': T('carbs') - 0.4, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': g0, 't1': g1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': gn, 'wires': gw})
K(T('glycogen') - 0.1, T('its') - 0.05, ['GLYCOGEN = STORED SUGAR'], x=540, y=110, sizes=[34], font='label', anim='rise', fit=1000)
# ---------------- the meal
m0 = T('so') - 0.08; m1 = T('and', T('great')) - 0.08
S.card(m0, m1)
S.add({'type': 'checklist', 't0': m0, 't1': m1, 'y': 150, 'title': 'Eat 3-4 hours before', 'items': [
    {'t': T('proper'), 'text': 'A *proper meal*', 'mark': 'check'}, {'t': T('dal'), 'text': '*Dal rice*, rajma rice', 'mark': 'check'},
    {'t': T('easy'), 'text': '*Easy carbs* + some protein', 'mark': 'check'}, {'t': T('oily'), 'text': 'Not too oily', 'mark': 'check'},
    {'t': T('breakfast'), 'text': 'Or a *healthy breakfast*', 'mark': 'check'}]})
# ---------------- water
Bh(T('and', T('great')) - 0.03, T('if', T('water', T('great'))) - 0.05, 'WATER', size=330, font='mc', anim='slam', color=CH)
w0 = T('if', T('water', T('great'))) - 0.08; w1 = T('so', T('seizures')) - 0.08
S.card(w0, w1)
wn = [{'t': w0 + 0.2, 'x': 500, 'y': 60, 'text': 'Only *plain water* all night'}, {'t': T('salt') - 0.1, 'x': 500, 'y': 215, 'text': 'Your *salt* gets watered down'},
      {'t': T('hyponatremia') - 0.1, 'x': 500, 'y': 370, 'text': 'HYPONATREMIA'}, {'t': T('seizures') - 0.2, 'x': 500, 'y': 530, 'text': 'Bad cases: SEIZURES', 'target': True}]
ww = [{'t': T('salt') - 0.4, 'd': 'M 500 105 L 500 165'}, {'t': T('hyponatremia') - 0.4, 'd': 'M 500 260 L 500 320'}, {'t': T('seizures') - 0.5, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': w0, 't1': w1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': wn, 'wires': ww})
K(T('hyponatremia') - 0.1, w1, ['HYPONATREMIA = LOW BLOOD SODIUM'], x=540, y=110, sizes=[32], font='label', anim='rise', fit=1000)
K(T('so', T('seizures')) - 0.03, T('after') - 0.05, ['MORE WATER IS', '~not always safer~'], x=540, y=300, sizes=[96, 110], anim='rise', stagger=0.8)
K(T('after') - 0.03, T('so', T('dehydrated')) - 0.05, ['WATER WITHOUT SALT', "~DOESN'T HYDRATE YOU PROPERLY~"], x=540, y=300, sizes=[76, 60], anim='rise', stagger=1.2)
# ---------------- the fix
f0 = T('so', T('dehydrated')) - 0.08; f1 = T('if', T('bottle')) - 0.08
S.card(f0, f1)
S.add({'type': 'checklist', 't0': f0, 't1': f1, 'y': 150, 'title': 'The water fix', 'items': [
    {'t': T('thirsty'), 'text': 'Drink *when you are thirsty*', 'mark': 'check'}, {'t': T('ors'), 'text': 'Add *ORS*, lemon or salt', 'mark': 'check'},
    {'t': T('bottle'), 'text': 'To *your bottle*', 'mark': 'check'}, {'t': T('all', T('bottle')), 'text': "That's *all you need*", 'mark': 'check'}]})
cta = T('if', T('bottle')) - 0.05
MC.end_card(S, cta, D + 2, 'Comment<br>*"Rave Protocol"*', 'Get my PDF. And follow Moon Crew.')
S.alt_zoom([1.0, 1.18, 1.06, 1.26]); S.cam['faceY'] = 0.40; S.cam['grain'] = 5
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'rave', r'dinner', r'six', r'hours', r'feet', r'water', r'mistake', r'hospital', r'muscles', r'glycogen', r'liver', r'dance',
                           r'burn', r'carbs', r'proper', r'meal', r'34', r'dal', r'rice', r'rajma', r'protein', r'oily', r'breakfast', r'plain', r'salt',
                           r'hyponatremia', r'seizures', r'safer', r'dehydrated', r'thirsty', r'ors', r'lemon', r'bottle', r'protocol', r'pdf', r'moon', r'crew'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': MC.BRAND['text'], 't0': 3.0, 't1': cta}, extra={'css': MC.CSS})

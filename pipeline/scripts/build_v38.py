import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v38', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('bahar') - 0.05, ['WHY DO INDIANS', 'GET *BELLY FAT?*'], x=540, y=300, sizes=[90, 110], anim='slam')
K(T('bahar') - 0.03, T('saare') - 0.05, ['THIN OUTSIDE.', '~FAT INSIDE.~'], x=540, y=300, sizes=[100, 110], anim='slam', stagger=1.0)
S.add({'type': 'chips', 't0': T('saare') - 0.05, 't1': T('aur', T('dikhega')) - 0.05, 'y': 240, 'items': [
    {'t': T('haath'), 'text': 'Thin arms'}, {'t': T('pair'), 'text': 'Thin legs'}, {'t': T('pet', T('pair')), 'text': '~Big belly~'}]})
K(T('aur', T('dikhega')) - 0.03, T('iska') - 0.05, ["HERE'S WHY"], x=540, y=330, sizes=[120], anim='track')
Bh(T('iska') - 0.03, T('bengal') - 0.05, 'BRITISH RAJ', size=230, font='anton', anim='slam', color=R); S.punch(T('british'), 0.12, 0.7)
f0 = T('bengal') - 0.08; f1 = T('jab', T('generations')) - 0.08
S.card(f0, f1)
S.add({'type': 'chain', 't0': f0, 't1': f1, 'y': 150, 'title': 'Famines under British rule', 'show': 4, 'items': [
    {'t': T('bengal'), 'text': '*Bengal famine*, 1770'}, {'t': T('madras'), 'text': '*Madras famine*, 1877'},
    {'t': T('chheena'), 'text': 'Our food was *taken*', 'st': 'no', 'stc': 'red'}, {'t': T('karodon'), 'text': '*Crores* starved to death', 'st': 'no', 'stc': 'red'},
    {'t': T('generations'), 'text': 'Hungry for *generations*', 'st': 'down', 'stc': 'red'}]})
# ---------------- thrifty genes
K(T('jab', T('generations')) - 0.03, T('dna') - 0.05, ['THE BODY', '*ADAPTED*'], x=540, y=300, sizes=[100, 130], anim='slam')
K(T('dna') - 0.05, T('isko') - 0.05, ['A CHANGE AT THE', '*DNA LEVEL*'], x=540, y=300, sizes=[84, 120], anim='rise')
Bh(T('isko') - 0.03, T('aur', T('mutation')) - 0.05, 'THRIFTY GENES', size=220, font='anton', anim='slam', color=Y)
K(T('thrifty') - 0.1, T('aur', T('mutation')) - 0.05, ['"THRIFTY GENE" MUTATION'], x=540, y=1540, sizes=[56], font='oswald', anim='rise')
t0 = T('aur', T('mutation')) - 0.08; t1 = T('kyunki', T('disease')) - 0.08
S.card(t0, t1)
tn = [{'t': T('storer') - 0.2, 'x': 500, 'y': 60, 'text': 'Body becomes a *storer*'}, {'t': T('fat'), 'x': 500, 'y': 215, 'text': 'Turn every meal into *fat*'},
      {'t': T('kal'), 'x': 500, 'y': 370, 'text': '"What if there\'s *no food tomorrow?*"'}, {'t': T('disease'), 'x': 500, 'y': 530, 'text': 'Survival then. ~Disease now.~', 'target': True}]
tw = [{'t': T('fat') - 0.3, 'd': 'M 500 105 L 500 165'}, {'t': T('kal') - 0.3, 'd': 'M 500 260 L 500 320'}, {'t': T('disease') - 0.3, 'd': 'M 500 415 L 500 480'}]
S.add({'type': 'flow', 't0': t0, 't1': t1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': tn, 'wires': tw})
K(T('200') - 0.05, t1, ['200 YEARS AGO'], x=540, y=120, sizes=[44], font='oswald', anim='rise')
# ---------------- surplus today
Bh(T('kyunki', T('disease')) - 0.03, T('par', T('bhar')) - 0.05, 'SURPLUS', size=360, font='anton', anim='slam', color=G)
K(T('zomato') - 0.1, T('par', T('bhar')) - 0.05, ['ZOMATO. SWIGGY. A FULL FRIDGE.'], x=540, y=1540, sizes=[56], font='oswald', anim='rise')
K(T('par', T('bhar')) - 0.03, T('aur', T('karte', T('genes'))) - 0.05, ['BUT YOUR GENES STILL', '~STORE LIKE A FAMINE~'], x=540, y=300, sizes=[76, 96], anim='rise', stagger=0.9)
# ---------------- TOFI
Bh(T('aur', T('karte', T('genes'))) - 0.03, T('bahar', T('inside')) - 0.05, 'TOFI', size=440, font='anton', anim='slam', color=R)
K(T('thin', T('tofi')) - 0.1, T('bahar', T('inside')) - 0.05, ['THIN OUTSIDE, *FAT INSIDE*'], x=540, y=1540, sizes=[60], font='oswald', anim='rise')
v0 = T('bahar', T('inside')) - 0.08; v1 = T('aur', T('heart', T('insulin'))) - 0.08
S.card(v0, v1)
S.add({'type': 'checklist', 't0': v0, 't1': v1, 'y': 150, 'title': 'Inside a TOFI body', 'items': [
    {'t': T('visceral'), 'text': '*Visceral fat* packed in', 'mark': 'x'}, {'t': T('insulin'), 'text': 'More *insulin resistance*', 'mark': 'x'},
    {'t': T('diabetes'), 'text': 'More *diabetes* risk', 'mark': 'x'}, {'t': T('heart', T('insulin')), 'text': 'More *heart* risk', 'mark': 'x'}]})
# ---------------- proof
p0 = T('aur', T('heart', T('insulin'))) - 0.05
K(p0, T('kyunki', T('comparison')) - 0.05, ['THE PROOF: INDIANS IN AMERICA', 'SAME FOOD. SAME LIFESTYLE.', '~MORE DIABETES + HEART DISEASE~'], x=540, y=260, sizes=[60, 64, 64], anim='rise', stagger=1.6)
K(T('kyunki', T('comparison')) - 0.03, T('par', T('generation')) - 0.05, ['THE GENES', '*CHANGED*'], x=540, y=300, sizes=[100, 130], anim='slam')
# ---------------- but
K(T('par', T('generation')) - 0.03, T('matlab', T('predisposition')) - 0.05, ['GENETICS IS', '^NOT A SENTENCE^'], x=540, y=300, sizes=[96, 120], anim='slam')
K(T('matlab', T('predisposition')) - 0.03, T('genetics', T('trigger')) - 0.05, ['THE GUN IS LOADED.', 'YOU PULL THE *TRIGGER*.'], x=540, y=300, sizes=[84, 90], anim='rise', stagger=1.0)
g0 = T('genetics', T('trigger')) - 0.08; g1 = T('par', T('control')) - 0.08
S.card(g0, g1)
S.add({'type': 'compare', 't0': g0, 't1': g1, 'y': 170, 'title': 'What controls your outcome', 'max': 70, 'items': [
    {'t': T('30%') - 0.1, 'label': 'Genetics', 'unit': '%', 'value': 30, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('70%') - 0.1, 'label': 'Lifestyle', 'unit': '%', 'value': 70, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
K(T('par', T('control')) - 0.03, T('western') - 0.05, ['INDIAN BODIES NEED', 'A *SPECIAL PROTOCOL*'], x=540, y=300, sizes=[84, 100], anim='rise')
K(T('western') - 0.03, T('aur', T('programmed')) - 0.05, ['WESTERN DIET PLANS', '~DON\'T WORK ON US~'], x=540, y=300, sizes=[84, 100], anim='slam')
K(T('programmed') - 0.2, T('aur', T('programmed')) - 0.05, ['PROGRAMMED DIFFERENTLY'], x=540, y=1540, sizes=[60], font='oswald', anim='rise')
cta = T('aur', T('programmed')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'I built the system', 'title': 'Comment<br>*"HEALTH"*', 'sub': "I'll send you the link. My job was to bring you the science.", 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'indians', r'pet', r'charbi', r'patla', r'mota', r'british', r'raj', r'bengal', r'famine', r'madras', r'1770', r'1877',
                           r'bhookhe', r'generations?', r'adapt', r'dna', r'thrifty', r'genes?', r'mutation', r'storer', r'fat', r'store', r'200', r'survival',
                           r'disease', r'surplus', r'zomato', r'swiggy', r'fridge', r'phenotype', r'tofi', r'visceral', r'insulin', r'diabetes', r'heart',
                           r'america', r'genetics', r'predisposition', r'gun', r'trigger', r'lifestyle', r'30%', r'70%', r'protocol', r'western', r'programmed'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

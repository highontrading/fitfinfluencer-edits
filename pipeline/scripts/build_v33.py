import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v33', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('but') - 0.05, ['"QUIT ROTI."'], x=540, y=300, sizes=[130], font='anton', anim='slam')
K(T('internet') - 0.05, T('but') - 0.05, ['SAYS EVERY SECOND PERSON ONLINE'], x=540, y=1540, sizes=[52], font='oswald', anim='rise')
K(T('but') - 0.03, T('par') - 0.05, ["DON'T QUIT ROTI."], x=540, y=330, sizes=[120], anim='slam')
K(T('par') - 0.03, T('gluten') - 0.05, ["WHAT'S INSIDE", '*THE WHEAT?*'], x=540, y=300, sizes=[90, 120], anim='rise')
Bh(T('gluten') - 0.03, T('roti', T('elastic')) - 0.05, 'GLUTEN', size=360, font='anton', anim='slam', color=Y)
K(T('elastic') - 0.1, T('roti', T('elastic')) - 0.05, ['THE PROTEIN THAT MAKES DOUGH *ELASTIC*'], x=540, y=1540, sizes=[50], font='oswald', anim='rise')
B(42467, T('roti', T('elastic')) - 0.05, T('pizza') - 0.05, off=0.8)
S.add({'type': 'chips', 't0': T('roti', T('elastic')) - 0.05, 't1': T('ab', T('pizza')) - 0.05, 'y': 240, 'items': [
    {'t': T('phoolti') - 0.3, 'text': 'Roti *puffs up*'}, {'t': T('paratha'), 'text': 'Paratha *stretches*'}, {'t': T('pizza') - 0.1, 'text': 'Pizza dough *stretches*'}]})
B(1663, T('pizza') - 0.05, T('ab', T('pizza')) - 0.05, off=1.0)
# ---------------- gluten went up
g0 = T('ab', T('pizza')) - 0.08; g1 = T('ab', T('zyada', T('15%'))) - 0.08; p0 = T('par', T('banta')) - 0.08
S.card(g0, p0)
S.add({'type': 'compare', 't0': g0, 't1': p0, 'y': 170, 'title': 'Gluten in wheat', 'max': 15, 'items': [
    {'t': T('56%') - 0.1, 'label': 'Originally', 'text': '5-6', 'unit': '%', 'value': 6, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
K(p0 + 0.05, T('unhone') - 0.05, ['BIG COMPANIES WANTED:'], x=540, y=200, sizes=[70], anim='rise')
S.add({'type': 'chips', 't0': T('softest') - 0.1, 't1': T('unhone') - 0.05, 'y': 330, 'items': [
    {'t': T('softest'), 'text': 'The *softest* bread'}, {'t': T('fluffiest'), 'text': 'The *fluffiest* croissant'}, {'t': T('longest'), 'text': 'The *longest* shelf life'}]})
K(T('unhone') - 0.05, T('aur', T('gehun', T('unhone'))) - 0.05, ['SO THE WHEAT', 'WAS ~MODIFIED~'], x=540, y=300, sizes=[90, 120], anim='slam')
m0 = T('aur', T('gehun', T('unhone'))) - 0.08
S.card(m0, g1)
S.add({'type': 'compare', 't0': m0, 't1': g1, 'y': 170, 'title': 'Gluten in wheat', 'max': 15, 'items': [
    {'t': m0 + 0.1, 'label': 'Originally', 'text': '5-6', 'unit': '%', 'value': 6, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('15%') - 0.3, 'label': 'Today', 'text': '10-15', 'unit': '%', 'value': 15, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
K(T('3') - 0.05, g1, ['*3X* MORE GLUTEN'], x=540, y=740, sizes=[56], font='oswald', anim='rise')
S.fx('sub_drop', T('3'), -12)
# ---------------- the enzyme
e0 = T('ab', T('zyada', T('15%'))) - 0.05
K(e0, T('dipeptidyl') - 0.05, ['YOUR BODY HAS', 'AN *ENZYME*'], x=540, y=300, sizes=[90, 120], anim='rise')
Bh(T('dipeptidyl') - 0.03, T('digest') - 0.05, 'DPP-IV', size=380, font='anton', anim='slam', color=G)
K(T('dipeptidyl') + 0.2, T('digest') - 0.05, ['DIPEPTIDYL PEPTIDASE: BREAKS DOWN GLUTEN'], x=540, y=1540, sizes=[46], font='oswald', anim='rise')
c0 = T('digest') - 0.08; c1 = T('usko', T('irritate')) - 0.08
S.card(c0, c1)
S.add({'type': 'compare', 't0': c0, 't1': T('enzyme', T('teen')) - 0.08, 'y': 170, 'title': 'Built for vs what we eat', 'max': 15, 'items': [
    {'t': T('5%') - 0.1, 'label': 'Enzyme built for', 'unit': '%', 'value': 5, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('15%', T('5%')) - 0.1, 'label': 'We load', 'unit': '%', 'value': 15, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
S.add({'type': 'chain', 't0': T('enzyme', T('teen')) - 0.08, 't1': c1, 'y': 150, 'title': 'What happens next', 'show': 4, 'items': [
    {'t': T('exhaust'), 'text': 'Enzyme gets *exhausted*', 'st': 'down', 'stc': 'red'}, {'t': T('adhoora'), 'text': 'Gluten breaks down *halfway*', 'st': 'no', 'stc': 'red'},
    {'t': T('lining'), 'text': 'Irritates your *gut lining*', 'st': 'up', 'stc': 'red'}]})
r0 = T('usko', T('irritate')) - 0.05; r1 = T('aur', T('angry')) - 0.08
K(r0, T('gas') - 0.05, ['A ~CHAIN REACTION~'], x=540, y=330, sizes=[110], anim='slam')
S.add({'type': 'chips', 't0': T('gas') - 0.05, 't1': r1, 'y': 240, 'items': [
    {'t': T('gas'), 'text': 'Gas'}, {'t': T('bloating'), 'text': 'Bloating'}, {'t': T('acidity'), 'text': 'Acidity'},
    {'t': T('inflammation'), 'text': 'Skin *inflammation*'}, {'t': T('acne'), 'text': '*Acne*'}, {'t': T('angry'), 'text': '~Angry skin~'}]})
K(T('aur', T('angry')) - 0.03, T('ab', T('modified')) - 0.05, ['NOT THE WHEAT.', 'THE ~MODIFIED~ WHEAT.'], x=540, y=300, sizes=[96, 96], anim='slam', stagger=1.4)
# ---------------- personalised
K(T('ab', T('modified')) - 0.03, T('aapke', T('active')) - 0.05, ['HOW LONG IS YOUR', 'ENZYME *ACTIVE?*'], x=540, y=300, sizes=[84, 110], anim='rise')
S.add({'type': 'chips', 't0': T('aapke', T('active')) - 0.05, 't1': T('ye', T('accept')) - 0.05, 'y': 240, 'items': [
    {'t': T('grain'), 'text': 'Which grain for *you?*'}, {'t': T('bajra'), 'text': 'Bajra'}, {'t': T('jau'), 'text': 'Jau'}, {'t': T('ragi'), 'text': 'Ragi'}]})
Bh(T('ye', T('accept')) - 0.03, T('mere') - 0.05, 'PERSONAL', size=310, font='anton', anim='slam', color=G)
K(T('mere') - 0.03, T('110') - 0.05, ['MY *HEALTH PROTOCOL*:', 'KNOW YOUR BODY. PICK YOUR GRAINS.'], x=540, y=280, sizes=[80, 52], anim='rise', stagger=0.8)
j0 = T('110') - 0.08; j1 = T('mera') - 0.08
S.card(j0, j1)
S.add({'type': 'stat', 't0': j0, 't1': j1, 'y': 200, 'kicker': 'Done on my own body', 'from': 110, 'to': 85, 'unit': ' KG', 'label': 'In *45-46 days*', 'dir': 'down', 'count': 1.2})
cta = T('mera') - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': "Don't quit roti. Understand it.", 'title': 'Follow for<br>*more science*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'roti', r'gehun', r'gluten', r'protein', r'elastic', r'phoolti', r'paratha', r'pizza', r'56%', r'companies', r'softest', r'fluffiest',
                           r'croissant', r'shelf', r'genetically', r'modify', r'15%', r'5%', r'3', r'enzyme', r'dipeptidyl', r'peptidase', r'digest', r'exhaust.*',
                           r'adhoora', r'gut', r'lining', r'irritate', r'chain', r'gas', r'bloating', r'acidity', r'skin', r'inflammation', r'acne', r'modified',
                           r'grain', r'bajra', r'jau', r'ragi', r'personalized', r'protocol', r'110', r'85'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

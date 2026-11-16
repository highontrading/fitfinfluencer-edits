import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v41', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('mediterranean') - 0.05, ['GOOGLE:', '"BEST DIET IN THE WORLD"'], x=540, y=300, sizes=[84, 84], font='serif', anim='rise', stagger=0.6)
Bh(T('mediterranean') - 0.1, T('ab') - 0.05, 'MEDITERRANEAN', size=170, font='anton', anim='slam', color=Y)
B(52467, T('mediterranean') - 0.05, T('ab') - 0.05, off=0.8)
K(T('ab') - 0.03, T('salad') - 0.05, ['NOW LOOK AT', 'THE *INDIAN THAALI*'], x=540, y=300, sizes=[84, 110], anim='slam')
t0 = T('salad') - 0.08; t1 = T('chalo') - 0.08
S.card(t0, t1)
S.add({'type': 'checklist', 't0': t0, 't1': t1, 'y': 150, 'title': 'The Indian thaali', 'items': [
    {'t': T('salad'), 'text': 'Salad', 'mark': 'check'}, {'t': T('achaar'), 'text': 'Achaar, dahi: *probiotics*', 'mark': 'check'},
    {'t': T('sabzi'), 'text': '2 sabzis: *fiber*', 'mark': 'check'}, {'t': T('daal'), 'text': 'Daal, paneer: *protein*', 'mark': 'check'},
    {'t': T('roti'), 'text': 'Roti, chawal: *carbs*', 'mark': 'check'}, {'t': T('ghee'), 'text': 'Ghee, buttermilk', 'mark': 'check'}]})
# ---------------- achaar = probiotic
K(T('chalo') - 0.03, T('500') - 0.05, ['LET\'S TALK', '*ACHAAR*'], x=540, y=300, sizes=[90, 130], anim='slam')
S.add({'type': 'stat', 't0': T('500') - 0.05, 't1': T('logon', T('500')) - 0.05, 'y': 260, 'kicker': 'Probiotic supplement market', 'from': 0, 'to': 500, 'unit': '+ CR', 'label': 'Rupees, every year', 'dir': 'up', 'count': 1.0})
K(T('logon', T('500')) - 0.03, T('achaar', T('raha')) - 0.05, ['THE BIGGEST PROBIOTIC', 'IS *ALREADY AT HOME*'], x=540, y=300, sizes=[76, 96], anim='rise', stagger=0.7)
p0 = T('achaar', T('raha')) - 0.08; p1 = T('yoga') - 0.08
S.card(p0, p1)
S.add({'type': 'chain', 't0': p0, 't1': p1, 'y': 150, 'title': 'Probiotics in your kitchen', 'show': 4, 'items': [
    {'t': T('lactobacillus'), 'text': 'Achaar: *Lactobacillus*'}, {'t': T('capsules'), 'text': 'Same bacteria as *expensive capsules*'},
    {'t': T('acidophilus'), 'text': 'Dahi: Lactobacillus + *Acidophilus*'}, {'t': T('idli'), 'text': 'Idli, dosa batter, *kaanji*'},
    {'t': T('microbiome'), 'text': 'Food for your *gut microbiome*', 'st': 'yes', 'stc': 'green'}]})
# ---------------- the West rebranded it
B(887, T('yoga') - 0.05, T('turmeric') - 0.05, off=1.0)
K(T('yoga') - 0.03, T('turmeric') - 0.05, ['YOGA: OURS.', 'NOW A *BILLION-DOLLAR* INDUSTRY'], x=540, y=300, sizes=[96, 70], anim='rise', stagger=0.9)
K(T('turmeric') - 0.03, T('aur', T('latte')) - 0.05, ['TURMERIC: OURS.', 'NOW A *LATTE*'], x=540, y=300, sizes=[96, 96], anim='rise', stagger=0.8)
B(43786, T('aur', T('latte')) - 0.05, T('hamari', T('app')) - 0.05, off=1.0)
K(T('aur', T('latte')) - 0.03, T('hamari', T('app')) - 0.05, ['MEDITATION: OURS.', 'NOW *AN APP*'], x=540, y=300, sizes=[96, 96], anim='rise', stagger=0.8)
K(T('hamari', T('app')) - 0.03, T('aur', T('kehte', T('sequencing'))) - 0.05, ["DAADI'S WAY OF EATING", 'NOW CALLED *"MEAL SEQUENCING"*'], x=540, y=300, sizes=[76, 76], anim='rise', stagger=0.9)
# ---------------- we copy them
c0 = T('aur', T('kehte', T('sequencing'))) - 0.08; c1 = T('main', T('nutrition')) - 0.08
S.card(c0, c1)
S.add({'type': 'compare', 't0': c0, 't1': T('almond') - 0.08, 'y': 170, 'title': 'We swap ours for theirs', 'max': 10, 'items': [
    {'t': T('quinoa'), 'label': 'Quinoa', 'text': 'vs RAJMA', 'value': 6, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('avocado'), 'label': 'Avocado', 'text': 'vs GHEE', 'value': 6, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
K(T('haryana') - 0.1, T('almond') - 0.08, ['HARYANA + PUNJAB: GHEE IN EVERYTHING.', '*AND STRONGER THAN US.*'], x=540, y=760, sizes=[40, 48], font='oswald', anim='rise', stagger=0.8)
S.add({'type': 'compare', 't0': T('almond') - 0.08, 't1': c1, 'y': 170, 'title': 'Almond milk vs makkhan', 'max': 10, 'items': [
    {'t': T('almond'), 'label': 'Almond milk', 'text': 'TREND', 'value': 4, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('makkhan'), 'label': 'Makkhan', 'text': 'WINS', 'value': 9, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
# ---------------- my protocol
m0 = T('main', T('nutrition')) - 0.08; m1 = T('same', T('solution')) - 0.08
S.card(m0, m1)
S.add({'type': 'chips', 't0': m0, 't1': m1, 'y': 200, 'items': [
    {'t': T('moong'), 'text': 'Moong daal, sattu'}, {'t': T('paneer', T('sattu')), 'text': 'Paneer, chicken'},
    {'t': T('chana'), 'text': 'Chana daal, kaala chana'}, {'t': T('haldi'), 'text': 'Haldi, ghee, achaar'}]})
K(T('ghar', T('haldi')) - 0.1, m1, ['INDIAN KITCHEN. INDIAN BUDGET. *INDIAN BODY.*'], x=540, y=110, sizes=[40], font='oswald', anim='rise', fit=1000)
K(T('same', T('solution')) - 0.03, T('agar', T('bhasha')) - 0.05, ['SAME SCIENCE.', 'DIFFERENT *LANGUAGE*.'], x=540, y=300, sizes=[100, 100], anim='slam', stagger=0.8)
cta = T('agar', T('bhasha')) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want the Indian health protocol?', 'title': 'Comment<br>*"HP"*', 'sub': "I'll send you the link. My job was to bring you the science.", 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'google', r'diet', r'mediterranean', r'thaali', r'salad', r'fermented', r'achaar', r'probiotics?', r'dahi', r'sabzi', r'fiber',
                           r'daal', r'protein', r'carb', r'paneer', r'soya', r'ghee', r'fat', r'buttermilk', r'hydration', r'500', r'crore', r'lactobacillus',
                           r'acidophilus', r'bacteria', r'capsules', r'idli', r'dosa', r'kaanji', r'microbiome', r'yoga', r'billion', r'turmeric', r'latte',
                           r'meditation', r'headspace', r'daadi', r'sequencing', r'western', r'quinoa', r'rajma', r'avocado', r'haryana', r'punjab', r'almond',
                           r'makkhan', r'nutrition', r'protocol', r'moong', r'sattu', r'chicken', r'chana', r'haldi', r'indian'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

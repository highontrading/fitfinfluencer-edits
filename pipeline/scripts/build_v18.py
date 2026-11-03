import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v18'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('ab') - 0.05, 'y': 150, 'kicker': 'Google: best diet in the world', 'lines': ['*Mediterranean*?'], 'sizes': [84], 'hideCaps': True})
S.add({'type': 'title', 't0': T('ab') - 0.03, 't1': T('salad') - 0.08, 'y': 170, 'lines': ['Ab dekho', '*Indian thaali*'], 'sizes': [84, 112]})
t0_ = T('salad') - 0.1; t1_ = T('haalanki') - 0.08
S.card(t0_, t1_)
S.add({'type': 'chain', 't0': t0_, 't1': t1_, 'y': 150, 'title': 'Indian thaali', 'show': 4, 'items': [
    {'t': T('salad'), 'icon': '🥗', 'text': 'Salad', 'st': '✓'},
    {'t': T('achaar'), 'icon': '🫙', 'text': 'Achaar · fermented', 'st': '✓'},
    {'t': T('dahi'), 'icon': '🥛', 'text': 'Dahi · probiotic', 'st': '✓'},
    {'t': T('sabzi'), 'icon': '🥦', 'text': '2 sabzi · fiber', 'st': '✓'},
    {'t': T('daal'), 'icon': '🍲', 'text': 'Daal · protein', 'st': '✓'},
    {'t': T('roti'), 'icon': '🍚', 'text': 'Roti chawal · carb', 'st': '✓'}]})
for it in S.events[-1]['items']: it['stc'] = 'green'
S.add({'type': 'chips', 't0': t1_ + 0.03, 't1': T('ghee') - 0.08, 'y': 140, 'items': [
    {'t': T('paneer'), 'icon': '🧀', 'text': 'Paneer'}, {'t': T('soya'), 'icon': '🫘', 'text': 'Soya'},
    {'t': T('achhe'), 'icon': '💪', 'text': '*Achha protein*'}]})
S.add({'type': 'chips', 't0': T('ghee') - 0.05, 't1': T('chalo') - 0.08, 'y': 140, 'items': [
    {'t': T('ghee'), 'icon': '🧈', 'text': 'Ghee · *healthy fat*'}, {'t': T('buttermilk'), 'icon': '🥛', 'text': 'Buttermilk · probiotic'},
    {'t': T('hydration'), 'icon': '💧', 'text': 'Hydration'}]})
S.add({'type': 'stat', 't0': T('chalo') - 0.05, 't1': T('logon', T('crore')) - 0.08, 'y': 230, 'kicker': 'Probiotic supplements market', 'from': 0, 'to': 500, 'unit': 'Cr+', 'label': '₹ crore se zyada', 'pill': '💊 Capsules ka business', 'dir': 'up', 'count': 1.2})
S.add({'type': 'title', 't0': T('logon', T('crore')) - 0.05, 't1': T('achaar', T('logon', T('crore'))) - 0.08, 'y': 170, 'kicker': 'Sabse bada probiotic', 'lines': ['*Ghar* mein hai'], 'sizes': [112]})
a0 = T('achaar', T('logon', T('crore'))) - 0.1; a1 = T('dahi', T('capsules')) - 0.1
S.card(a0, a1)
an = [{'t': a0 + 0.15, 'x': 500, 'y': 90, 'icon': '🫙', 'text': 'Achaar · *fermented*'},
      {'t': T('lactobacillus'), 'x': 500, 'y': 280, 'icon': '🦠', 'text': 'Lactobacillus bacteria'},
      {'t': T('expensive'), 'x': 500, 'y': 470, 'icon': '💊', 'text': 'Wahi jo *capsules* mein', 'target': True}]
aw = [{'t': T('lactobacillus') - 0.3, 'd': 'M 500 140 L 500 225'}, {'t': T('expensive') - 0.35, 'd': 'M 500 330 L 500 410'}]
S.add({'type': 'flow', 't0': a0, 't1': a1, 'y': 170, 'w': 1000, 'h': 600, 'nodes': an, 'wires': aw})
d0 = a1; d1 = TE('hai', T('microbiome')) + 0.25
S.card(d0, d1)
S.add({'type': 'checklist', 't0': d0, 't1': d1, 'y': 170, 'title': 'Gut microbiome ka khaana', 'items': [
    {'t': T('dahi', T('capsules')), 'text': 'Dahi <span>· Lactobacillus + Acidophilus</span>', 'mark': 'check'},
    {'t': T('idli'), 'text': 'Idli dosa batter <span>· fermented</span>', 'mark': 'check'},
    {'t': T('kaanji'), 'text': 'Kaanji <span>· fermented</span>', 'mark': 'check'},
    {'t': T('microbiome'), 'text': 'Gut <span>microbiome</span>', 'mark': 'check'}]})
w0 = T('yoga') - 0.1; w1 = TE('hain', T('sequencing')) + 0.25
S.card(w0, w1)
S.add({'type': 'chain', 't0': w0, 't1': w1, 'y': 150, 'title': 'Hamara tha · West ne bech diya', 'show': 4, 'items': [
    {'t': T('yoga'), 'icon': '🧘', 'text': 'Yoga → billion $ industry', 'st': ''},
    {'t': T('turmeric'), 'icon': '🟡', 'text': 'Haldi → "turmeric latte"', 'st': ''},
    {'t': T('meditation'), 'icon': '🧠', 'text': 'Meditation → Headspace app', 'st': ''},
    {'t': T('daadi'), 'icon': '👵', 'text': 'Daadi → "meal sequencing"', 'st': ''}]})
S.add({'type': 'title', 't0': T('hum') - 0.05, 't1': T('quinoa') - 0.08, 'y': 170, 'lines': ['Apna chhod ke', '~doosron ko follow~'], 'sizes': [84, 84]})
q0 = T('quinoa') - 0.1; q1 = TE('ismein') + 0.25
S.card(q0, q1)
S.add({'type': 'chain', 't0': q0, 't1': q1, 'y': 150, 'title': 'Western vs Desi', 'show': 4, 'items': [
    {'t': T('quinoa'), 'icon': '🌾', 'text': 'Quinoa? *Rajma* better', 'st': '✓'},
    {'t': T('avocado'), 'icon': '🥑', 'text': 'Avocado? *Desi ghee*', 'st': '✓'},
    {'t': T('haryana'), 'icon': '💪', 'text': 'Punjab: ghee = mazboot', 'st': '✓'},
    {'t': T('almond'), 'icon': '🥛', 'text': 'Almond milk? *Makkhan*', 'st': '✓'}]})
for it in S.events[-1]['items']: it['stc'] = 'green'
p0 = T('main', q1 - 0.3) - 0.1; p1 = T('ghar', T('haldi')) - 0.1
S.card(p0, p1)
S.add({'type': 'title', 't0': p0, 't1': T('moong') - 0.08, 'y': 240, 'kicker': 'Mere health protocol mein', 'lines': ['~No~ Western ingredients'], 'sizes': [80]})
S.add({'type': 'checklist', 't0': T('moong') - 0.05, 't1': p1, 'y': 170, 'title': 'Desi protocol', 'items': [
    {'t': T('moong'), 'text': 'Moong daal <span>· sattu · paneer</span>', 'mark': 'check'},
    {'t': T('chicken'), 'text': 'Chicken <span>· chana daal</span>', 'mark': 'check'},
    {'t': T('kaala'), 'text': 'Kaala chana', 'mark': 'check'},
    {'t': T('haldi'), 'text': 'Haldi <span>· ghee · achaar</span>', 'mark': 'check'}]})
S.add({'type': 'chips', 't0': p1 + 0.03, 't1': T('same', T('solution')) - 0.08, 'y': 140, 'items': [
    {'t': T('ghar', T('haldi')), 'icon': '🏠', 'text': 'Ghar ka khaana'}, {'t': T('kitchen'), 'icon': '🍳', 'text': 'Indian kitchen'},
    {'t': T('budget'), 'icon': '💰', 'text': 'Indian budget'}, {'t': T('solution'), 'icon': '✅', 'text': 'Indian body ka *real solution*'}]})
S.add({'type': 'title', 't0': T('same', T('solution')) - 0.05, 't1': T('agar', T('rehti')) - 0.08, 'y': 170, 'lines': ['Same baat', '*Alag bhasha*'], 'sizes': [84, 108]})
cta = T('agar', T('rehti')) - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Health protocol chahiye?', 'title': 'Comment<br>*"HP"*', 'sub': 'Mera kaam tha science pahunchana · decision aapka hai', 'button': '💬 COMMENT "HP"', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'mediterranean', r'thaali', r'salad', r'fermented', r'achaar', r'probiotics?', r'dahi', r'sabzi', r'fiber', r'daal', r'protein', r'carb', r'paneer',
                           r'soya', r'ghee', r'buttermilk', r'hydration', r'lactobacillus', r'acidophilus', r'capsules', r'idli', r'dosa', r'kaanji', r'microbiome', r'yoga',
                           r'turmeric', r'latte', r'meditation', r'headspace', r'quinoa', r'rajma', r'avocado', r'makkhan', r'almond', r'sattu', r'chana', r'haldi', r'hp'])
B = S.broll
B(52467, T('answer') - 0.1, T('ab') - 0.05, off=1.0)
B(10420, T('sabzi') - 0.4, T('daal') - 0.05, off=1.0)
B(3816, T('roti') - 0.05, t1_ - 0.1, off=1.0)
B(43030, T('ghee') - 0.05, T('buttermilk') - 0.1, off=1.0)
B(10436, T('dahi', T('capsules')) - 0.1, T('aur', T('dahi', T('capsules'))) - 0.05, off=1.0)
B(887, T('yoga') - 0.05, T('turmeric') - 0.1, off=1.0)
B(43786, T('meditation') - 0.1, T('hamari', T('meditation')) - 0.1, off=2.0)
B(3692, T('avocado') - 0.1, T('kyunki', T('avocado')) - 0.05, off=1.0)
B(40531, T('ghar', T('haldi')) - 0.1, T('aur', T('ghar', T('haldi'))) + 0.2, off=1.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

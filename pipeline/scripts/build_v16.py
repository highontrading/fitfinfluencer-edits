import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v16'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('sirf') - 0.05, 'y': 150, 'kicker': 'Patle hone ke liye', 'lines': ['Kuch bhi *chhodna*', '~nahi~ hai?'], 'sizes': [96, 96], 'hideCaps': True})
S.add({'type': 'stat', 't0': T('sirf') - 0.03, 't1': T('toh', T('dijiye')) - 0.08, 'y': 230, 'kicker': 'Sirf ek cheez', 'from': 0, 'to': 40, 'unit': '%', 'label': 'Kam glucose spike', 'pill': '🍽️ Khaane ka order badlo', 'dir': 'down', 'count': 1.0})
S.add({'type': 'title', 't0': T('toh', T('dijiye')) - 0.05, 't1': T('samjho', T('jaoge')) - 0.08, 'y': 170, 'lines': ['Kaam ho gaya', '*Patle* ho jaoge'], 'sizes': [84, 104]})
b0 = T('samjho', T('jaoge')) - 0.1; b1 = TE('jaayega', T('spike', T('waise'))) + 0.25
S.card(b0, b1)
S.add({'type': 'chain', 't0': b0, 't1': b1, 'y': 150, 'title': 'Pet = wash basin', 'show': 4, 'items': [
    {'t': T('wash'), 'icon': '🚰', 'text': 'Pet = wash basin', 'st': ''},
    {'t': T('blood'), 'icon': '🩸', 'text': 'Blood sugar = drain pipe', 'st': ''},
    {'t': T('seedha'), 'icon': '💦', 'text': 'Seedha paani → tez drain', 'st': '↓↓'},
    {'t': T('carb'), 'icon': '🍚', 'text': 'Seedha carb → *spike*', 'st': '↑↑', 'stc': 'red'}]})
f0 = T('par', b1 - 0.3) - 0.1; f1 = TE('hoga', T('absorb')) + 0.25
S.card(f0, f1)
fn = [{'t': T('jaali'), 'x': 500, 'y': 90, 'icon': '🥗', 'text': '*Fiber* ki jaali'},
      {'t': T('kavach'), 'x': 500, 'y': 280, 'icon': '🛡️', 'text': 'Poora *kavach*'},
      {'t': T('absorb') - 0.6, 'x': 500, 'y': 470, 'icon': '🐢', 'text': 'Carb *slowly* absorb', 'target': True}]
fw = [{'t': T('kavach') - 0.3, 'd': 'M 500 140 L 500 225'}, {'t': T('absorb') - 0.95, 'd': 'M 500 330 L 500 410'}]
S.add({'type': 'title', 't0': f0, 't1': T('jaali') - 0.08, 'y': 260, 'lines': ['Pehle *jaali* lagao'], 'sizes': [96]})
S.add({'type': 'flow', 't0': T('jaali') - 0.1, 't1': f1, 'y': 170, 'w': 1000, 'h': 600, 'nodes': fn, 'wires': fw})
g0 = T('toh', f1 - 0.3) - 0.1; g1 = TE('lagegi') + 0.25
S.card(g0, g1)
S.add({'type': 'chain', 't0': g0, 't1': g1, 'y': 150, 'title': 'Fiber pehle toh', 'show': 4, 'items': [
    {'t': T('insulin', g0), 'icon': '〰️', 'text': 'Insulin dheere spike', 'st': '✓'},
    {'t': T('crash', g0), 'icon': '🛡️', 'text': 'Crash bhi dheere', 'st': '✓'},
    {'t': T('bhookh', g0), 'icon': '😌', 'text': 'Bhookh kam lagegi', 'st': '✓'}]})
for it in S.events[-1]['items']: it['stc'] = 'green'
S.add({'type': 'title', 't0': T('toh', g1 - 0.3) - 0.05, 't1': T('kheera') - 0.08, 'y': 170, 'kicker': 'Step 1', 'lines': ['Pehle *kachcha salad*'], 'sizes': [96]})
S.add({'type': 'chips', 't0': T('kheera') - 0.05, 't1': T('ek', T('kheera')) - 0.1, 'y': 140, 'items': [
    {'t': T('kheera'), 'icon': '🥒', 'text': 'Kheera'}, {'t': T('gajar'), 'icon': '🥕', 'text': 'Gajar'}, {'t': T('tamatar'), 'icon': '🍅', 'text': 'Tamatar'}]})
r0 = T('ek', T('kheera')) - 0.1; r1 = T('step', T('bhi', T('crash', T('kheera')))) - 0.1
S.card(r0, r1)
S.add({'type': 'checklist', 't0': r0, 't1': r1, 'y': 170, 'title': 'Salad = resistant starch', 'items': [
    {'t': T('protective'), 'text': 'Gut mein <span>protective layer</span>', 'mark': 'check'},
    {'t': T('slow', r0), 'text': 'Insulin spike <span>slow</span>', 'mark': 'check'},
    {'t': T('crash', r0), 'text': 'Insulin crash <span>slow</span>', 'mark': 'check'}]})
q0 = r1; q1 = T('kyunki', T('khaiye', r1)) - 0.08
S.card(q0, q1)
S.add({'type': 'checklist', 't0': q0, 't1': q1, 'y': 170, 'title': 'Meal sequencing · plate', 'items': [
    {'t': q0 + 0.15, 'text': '1. Salad <span>sabse pehle</span>', 'mark': 'check'},
    {'t': T('plate'), 'text': '2. 50% plate <span>sabzi</span>', 'mark': 'check'},
    {'t': T('daal'), 'text': '3. Daal · anda · chicken <span>· tofu</span>', 'mark': 'check'},
    {'t': T('roti', q0), 'text': '4. Roti / chawal <span>bahut kam</span>', 'mark': 'check'}]})
S.add({'type': 'title', 't0': q1 + 0.03, 't1': T('toh', T('aate')) - 0.08, 'y': 170, 'kicker': 'Aajkal roti mein', 'lines': ['*Gluten* bahut zyada'], 'sizes': [100]})
c0 = T('toh', T('aate')) - 0.1; c1 = TE('hai', T('16%')) + 0.3
S.card(c0, c1)
S.add({'type': 'compare', 't0': c0, 't1': c1, 'y': 170, 'title': 'Atte mein gluten', 'max': 16, 'items': [
    {'t': T('gehun'), 'label': 'Ghar pe pisa', 'text': '5–6%', 'value': 6, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('pandrah'), 'label': 'Bazaar atta', 'text': '15–16%', 'value': 16, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
S.add({'type': 'slam', 't0': T('aur', c1 - 0.3) - 0.05, 't1': T('jo', T('sequencing')) - 0.05, 'y': 200, 'text': 'MEAL *SEQUENCING*', 'size': 100, 'sub': 'Khaane ka order'})
S.punch(T('sequencing'), 0.14, 0.8)
S.add({'type': 'stat', 't0': T('jo', T('sequencing')) - 0.03, 't1': T('aur', T('less')) - 0.08, 'y': 230, 'kicker': 'Same food · different order', 'from': 0, 'to': 40, 'unit': '%', 'label': 'Kam glucose spike', 'pill': '📚 Studies prove karti hain', 'dir': 'down', 'count': 1.2})
S.add({'type': 'title', 't0': T('aur', T('less')) - 0.05, 't1': T('hamare') - 0.08, 'y': 170, 'lines': ['Interesting *baat*?'], 'sizes': [100]})
a0 = T('hamare') - 0.1; a1 = TE('log', T('khaate')) + 0.25
S.card(a0, a1)
S.add({'type': 'chain', 't0': a0, 't1': a1, 'y': 150, 'title': 'Ancestors ka traditional method', 'show': 4, 'items': [
    {'t': T('ancestors'), 'icon': '👵', 'text': 'Hamare ancestors', 'st': ''},
    {'t': T('traditional'), 'icon': '🏺', 'text': 'Traditional method', 'st': ''},
    {'t': T('salad', a0), 'icon': '🥗', 'text': 'Pehle salad', 'st': '1'},
    {'t': T('protein', a0), 'icon': '🍗', 'text': 'Phir protein', 'st': '2'},
    {'t': T('carb', a0), 'icon': '🍚', 'text': 'Phir carb', 'st': '3'}]})
for it in S.events[-1]['items']: it['stc'] = 'green'
S.add({'type': 'badge', 't0': T('aur', a1 - 0.3) - 0.05, 't1': T('aur', T('chuka')) - 0.08, 'y': 200, 'text': '2024 Research', 'sub': 'Science ne *prove* kiya'})
d0 = T('aur', T('chuka')) - 0.1; d1 = T('par', T('hain', T('steps', T('10')))) - 0.08
S.card(d0, d1)
S.add({'type': 'title', 't0': d0, 't1': T('khoob') - 0.08, 'y': 260, 'kicker': 'Daadi · dada ji', 'lines': ['Fat *nahi* chadhta tha'], 'sizes': [88]})
S.add({'type': 'compare', 't0': T('khoob') - 0.05, 't1': d1, 'y': 170, 'title': 'Roz ke steps', 'max': 25, 'items': [
    {'t': T('25.*'), 'label': 'Pehle', 'text': '25,000', 'value': 25, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('10'), 'label': 'Aaj', 'text': '<10,000', 'value': 9, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
S.add({'type': 'title', 't0': d1 + 0.03, 't1': T('aap', d1 + 1.0) - 0.08, 'y': 170, 'lines': ['Par ye sirf', '*ek trick* hai'], 'sizes': [84, 100]})
e0 = T('aap', d1 + 1.0) - 0.1; e1 = TE('jaoge', T('mote')) + 0.3
S.card(e0, e1)
S.add({'type': 'chain', 't0': e0, 't1': e1, 'y': 150, 'title': 'Din bhar khaate raho toh', 'show': 4, 'items': [
    {'t': T('chai'), 'icon': '☕', 'text': 'Subah ki chai se shuru', 'st': ''},
    {'t': T('spike', e0), 'icon': '📈', 'text': 'Glucose spike', 'st': '↑'},
    {'t': T('crash', e0), 'icon': '📉', 'text': 'Crash', 'st': '↓'},
    {'t': T('bhookh', e0), 'icon': '😋', 'text': 'Baar baar bhookh', 'st': ''},
    {'t': T('khaoge'), 'icon': '🍪', 'text': 'Baar baar khaoge', 'st': ''},
    {'t': T('mote'), 'icon': '⚖️', 'text': 'Mote hote jaoge', 'st': '✗'}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
cta = T('toh', T('chahiye', T('agar', T('daal', e1)))) - 0.1
S.add({'type': 'badge', 't0': T('aur', e1 - 0.3) - 0.05, 't1': cta - 0.05, 'y': 200, 'text': 'Mera system', 'sub': 'Sab kuch *health protocol* mein'})
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Poora system chahiye?', 'title': 'Comment<br>*"HEALTH PROTOCOL"*', 'sub': 'Mera kaam tha science pahunchana · decision aapka hai', 'button': '💬 COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'patle', r'glucose', r'spike', r'order', r'basin', r'drain', r'carb', r'jaali', r'fiber', r'kavach', r'slowly', r'insulin', r'crash', r'bhookh',
                           r'salad', r'kheera', r'gajar', r'tamatar', r'resistant', r'starch', r'protective', r'sabzi', r'daal', r'protein', r'anda', r'chicken', r'tofu',
                           r'roti', r'chawal', r'gluten', r'meal', r'sequencing', r'ancestors', r'traditional', r'steps', r'trick', r'mote', r'health', r'protocol', r'system'])
B = S.broll
B(40531, T('khaane') - 0.1, T('toh', T('dijiye')) - 0.08, off=1.0)
B(108, T('seedha') - 0.1, T('waise') - 0.05, off=2.0)
B(5078, T('glucose', T('waise')) - 0.1, b1 - 0.1, off=2.0)
B(40520, T('salad', T('step')) - 0.3, T('kheera') + 1.2, off=1.0)
B(10420, T('plate') - 0.3, T('aur', T('plate')) - 0.05, off=1.0)
B(42910, T('anda') - 0.2, T('agar', T('anda')) - 0.05, off=1.0)
B(3816, T('roti', q0) - 0.1, q1 - 0.1, off=1.0)
B(42463, q1 + 0.1, c0 - 0.1, off=1.0)
B(10431, T('salad', a0) - 0.1, T('toh', T('karo')) - 0.05, off=1.0)
B(4629, T('25.*') - 0.2, T('aaj', T('25.*')) - 0.05, off=1.0)
B(41117, T('chai') - 0.3, T('kitni') - 0.05, off=1.0)
B(44001, T('itna', T('khaoge')) - 0.1, T('aur', T('rahegi')) - 0.1, off=1.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

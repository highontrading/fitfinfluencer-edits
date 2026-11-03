import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v10'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('but') - 0.05, 'y': 150, 'kicker': 'Internet kehta hai', 'lines': ['Roti ~chhod do~'], 'sizes': [118], 'hideCaps': True})
S.add({'type': 'slam', 't0': T('but'), 't1': T('par') - 0.05, 'y': 200, 'text': 'Roti *chhodo mat*', 'size': 120})
S.punch(T('mat'), 0.12, 0.8)
S.add({'type': 'title', 't0': T('par'), 't1': T('gluten') - 0.1, 'y': 170, 'lines': ['Gehun ke andar', '*kya* hota hai?'], 'sizes': [84, 104]})
S.add({'type': 'slam', 't0': T('gluten'), 't1': T('aur', T('gluten')) + 0.6, 'y': 200, 'text': '*GLUTEN* 🌾', 'size': 150, 'sub': 'Gehun ka protein'})
S.punch(T('gluten'), 0.14, 0.8)
S.add({'type': 'chips', 't0': T('roti', T('elastic')) - 0.1, 't1': TE('hai', T('pizza')) + 0.2, 'y': 140, 'items': [
    {'t': T('roti', T('elastic')), 'icon': '🫓', 'text': 'Roti *phoolti* hai'},
    {'t': T('paratha'), 'icon': '🥞', 'text': 'Paratha *stretch*'},
    {'t': T('pizza'), 'icon': '🍕', 'text': 'Pizza dough *stretch*'}]})
o0 = T('ab') - 0.1; o1 = TE('tha', T('paratha', T('originally'))) + 0.2
S.card(o0, o1)
S.add({'type': 'stat', 't0': o0, 't1': o1, 'y': 230, 'kicker': 'Originally gehun mein', 'from': 0, 'to': 6, 'unit': '%', 'label': 'Gluten (5–6%)', 'pill': '🫓 Roti isi pe banti thi', 'dir': 'down', 'count': 1.0})
S.add({'type': 'chips', 't0': T('companies') - 0.1, 't1': T('unhone') - 0.08, 'y': 150, 'items': [
    {'t': T('companies'), 'icon': '🏭', 'text': 'Badi *companies* aayi'},
    {'t': T('softest'), 'icon': '🍞', 'text': 'Softest bread'},
    {'t': T('fluffiest'), 'icon': '🥐', 'text': 'Fluffiest croissant'},
    {'t': T('longest'), 'icon': '📦', 'text': 'Longest shelf life'}]})
S.add({'type': 'title', 't0': T('unhone'), 't1': T('aur', T('unhone')) - 0.08, 'y': 170, 'lines': ['*Modified*', 'gehun'], 'sizes': [118, 96]})
g0 = T('aur', T('unhone')) - 0.1; g1 = TE('zyada', T('15%')) + 0.25
S.card(g0, g1)
S.add({'type': 'compare', 't0': g0, 't1': g1, 'y': 170, 'title': 'Gehun mein gluten', 'max': 15, 'items': [
    {'t': g0 + 0.1, 'label': 'Pehle', 'text': '5–6%', 'value': 6, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('10', g0), 'label': 'Aaj', 'text': '10–15%', 'value': 15, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
S.add({'type': 'slam', 't0': T('3', g0) - 0.05, 't1': g1, 'y': 760, 'text': '*3X* ↑', 'size': 110})
e0 = T('ab', g1 - 0.3) - 0.1; e1 = TE('zyada', T('teen')) + 0.25
S.card(e0, e1)
S.add({'type': 'title', 't0': e0, 't1': T('par', e0) - 0.1, 'y': 270, 'kicker': 'Body ka enzyme', 'lines': ['*DPP-4*', 'gluten todta hai'], 'sizes': [120, 70]})
en = [{'t': T('5%'), 'x': 260, 'y': 90, 'icon': '🧬', 'text': 'Enzyme bana', 'sub': 'sirf 5% gluten ke liye'},
      {'t': T('15%', T('5%')), 'x': 740, 'y': 90, 'icon': '🌾', 'text': 'Load hota', 'sub': '15% gluten'},
      {'t': T('teen'), 'x': 500, 'y': 360, 'icon': '⚠️', 'text': '*3X* overload', 'target': True}]
ew = [{'t': T('teen') - 0.35, 'd': 'M 260 150 C 260 280, 400 330, 410 330'}, {'t': T('teen') - 0.35, 'd': 'M 740 150 C 740 280, 600 330, 590 330'}]
S.add({'type': 'flow', 't0': T('par', e0) - 0.1, 't1': e1, 'y': 170, 'w': 1000, 'h': 560, 'nodes': en, 'wires': ew})
x0 = T('enzyme', e1 - 0.3) - 0.1; x1 = TE('acidity') + 0.3
S.card(x0, x1)
S.add({'type': 'chain', 't0': x0, 't1': x1, 'y': 150, 'title': 'Chain reaction', 'show': 4, 'items': [
    {'t': T('exhaust'), 'icon': '😩', 'text': 'Enzyme exhaust', 'st': ''},
    {'t': T('adhoora'), 'icon': '🧩', 'text': 'Gluten adhoora toota', 'st': ''},
    {'t': T('irritate'), 'icon': '🔥', 'text': 'Gut lining irritate', 'st': ''},
    {'t': T('gas'), 'icon': '💨', 'text': 'Gas · bloating · acidity', 'st': ''}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
S.add({'type': 'chips', 't0': T('kuch') - 0.1, 't1': TE('hai', T('angry')) + 0.2, 'y': 150, 'items': [
    {'t': T('inflammation'), 'icon': '🔴', 'text': 'Skin *inflammation*'},
    {'t': T('acne'), 'icon': '😣', 'text': '*Acne*'},
    {'t': T('angry'), 'icon': '😤', 'text': '*Angry skin*'}]})
S.add({'type': 'title', 't0': T('aur', T('angry')) - 0.05, 't1': T('ab', T('modified', T('angry'))) - 0.08, 'y': 160, 'lines': ['Galti gehun ki ~nahi~', '*Modified gehun* ki'], 'sizes': [80, 92]})
S.add({'type': 'title', 't0': T('ab', T('modified', T('angry'))), 't1': T('aapke') - 0.08, 'y': 170, 'kicker': 'Sawaal ye hai', 'lines': ['Enzyme kitni der', '*active* rehta hai?'], 'sizes': [80, 92]})
S.add({'type': 'chips', 't0': T('aapke') - 0.1, 't1': TE('karegi') + 0.2, 'y': 150, 'items': [
    {'t': T('bajra'), 'icon': '🌾', 'text': '*Bajra*'}, {'t': T('jau'), 'icon': '🌾', 'text': '*Jau*'}, {'t': T('ragi'), 'icon': '🌾', 'text': '*Ragi*'},
    {'t': T('accept'), 'icon': '❓', 'text': 'Aapki body kaun sa *accept* karegi?'}]})
p0 = T('ye', T('karegi')) - 0.1; p1 = TE('mein', T('46')) + 0.25
S.card(p0, p1)
S.add({'type': 'checklist', 't0': p0, 't1': T('kyunki', p0) - 0.05, 'y': 170, 'title': 'Mera health protocol', 'items': [
    {'t': T('samajhna', p0), 'text': 'Body ko <span>samajhna</span>', 'mark': 'check'},
    {'t': T('grains', p0), 'text': 'Grains <span>select karna</span>', 'mark': 'check'},
    {'t': T('load', p0), 'text': 'Enzyme <span>load</span>', 'mark': 'check'}]})
S.add({'type': 'stat', 't0': T('kyunki', p0) - 0.05, 't1': p1, 'y': 230, 'kicker': 'Khud apni body pe', 'fromText': '110 KG', 'from': 110, 'to': 85, 'unit': 'KG', 'label': '45–46 din mein', 'pill': '▼ 25 KG', 'dir': 'down', 'count': 1.3})
cta = T('mera') - 0.1
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'You are watching', 'title': 'Fit<span class="acc">Finfluencer</span>', 'sub': 'Mera kaam tha science pahunchana · decision aapka hai', 'button': 'FOLLOW FOR MORE', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'roti', r'gehun', r'protein', r'gluten', r'elastic', r'paratha', r'pizza', r'companies', r'genetically', r'modify', r'enzyme',
                           r'digest', r'gut', r'gas', r'bloating', r'acidity', r'skin', r'acne', r'grains?', r'bajra', r'jau', r'ragi', r'protocol', r'kg', r'science'])
B = S.broll
B(42463, T('gluten') - 0.05, T('aur', T('gluten')) + 0.5, off=1.0)
B(1663, T('elastic'), T('roti', T('elastic')) - 0.08, off=1.0)
B(42472, T('pizza'), TE('hai', T('pizza')) + 0.2, off=1.0)
B(44001, T('companies') - 0.1, T('unhone') - 0.08, off=0.5)
B(4701, T('gas') - 0.2, x1 - 0.1, off=1.5)
B(50426, T('kuch') - 0.1, TE('hai', T('angry')) + 0.15, off=2.0)
B(3816, T('bajra') - 0.2, TE('karegi') + 0.15, off=1.0)
B(42464, T('grains', p0) - 0.2, T('kyunki', p0) - 0.08, off=1.0)
B(44432, T('110', p0) - 0.2, p1 - 0.1, off=1.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

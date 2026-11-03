import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v15'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('bahar') - 0.05, 'y': 150, 'kicker': 'Indians ke pet pe', 'lines': ['Itni *charbi*', 'kyun?'], 'sizes': [112, 96], 'hideCaps': True})
S.add({'type': 'title', 't0': T('bahar') - 0.03, 't1': T('saare') - 0.08, 'y': 170, 'lines': ['Bahar se ^patla^', 'Andar se ~mota~'], 'sizes': [92, 92]})
S.add({'type': 'chips', 't0': T('saare') - 0.05, 't1': T('aur', T('dikhega')) - 0.1, 'y': 140, 'items': [
    {'t': T('haath'), 'icon': '💪', 'text': 'Haath patle'}, {'t': T('pair'), 'icon': '🦵', 'text': 'Pair patle'},
    {'t': T('pet', T('pair')), 'icon': '⚠️', 'text': 'Pet *bada*'}]})
S.add({'type': 'title', 't0': T('aur', T('dikhega')) - 0.05, 't1': T('iska') - 0.08, 'y': 170, 'lines': ['Aisa *kyun*', 'hota hai?'], 'sizes': [112, 84]})
S.add({'type': 'slam', 't0': T('iska') - 0.05, 't1': T('bengal') - 0.05, 'y': 200, 'text': '*BRITISH RAJ*', 'size': 120, 'sub': 'Iska jawab'})
S.punch(T('british'), 0.14, 0.8)
h0 = T('bengal') - 0.1; h1 = TE('rahe', T('generations')) + 0.25
S.card(h0, h1)
S.add({'type': 'chain', 't0': h0, 't1': h1, 'y': 150, 'title': 'Itihaas', 'show': 4, 'items': [
    {'t': T('bengal'), 'icon': '🌾', 'text': 'Bengal famine · 1770', 'st': ''},
    {'t': T('madras'), 'icon': '🌾', 'text': 'Madras famine · 1877', 'st': ''},
    {'t': T('angrezon'), 'icon': '🚫', 'text': 'Angrezon ne khana chheena', 'st': ''},
    {'t': T('karodon'), 'icon': '💀', 'text': 'Karodon log bhookhe mare', 'st': ''},
    {'t': T('generations'), 'icon': '⏳', 'text': 'Generations tak bhookh', 'st': ''}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
a0 = T('jab') - 0.1; a1 = TE('aaya', T('dna')) + 0.3
S.card(a0, a1)
an = [{'t': T('jab') + 0.1, 'x': 500, 'y': 90, 'icon': '🍽️', 'text': 'Khana *nahi* mila'},
      {'t': T('adapt'), 'x': 500, 'y': 280, 'icon': '🧬', 'text': 'Body ne *adapt* kiya'},
      {'t': T('dna'), 'x': 500, 'y': 470, 'icon': '🔁', 'text': '*DNA* level pe change', 'target': True}]
aw = [{'t': T('adapt') - 0.3, 'd': 'M 500 140 L 500 225'}, {'t': T('dna') - 0.35, 'd': 'M 500 330 L 500 410'}]
S.add({'type': 'flow', 't0': a0, 't1': a1, 'y': 170, 'w': 1000, 'h': 600, 'nodes': an, 'wires': aw})
S.add({'type': 'slam', 't0': T('isko') - 0.1, 't1': T('aur', T('mutation')) - 0.05, 'y': 200, 'text': 'THRIFTY *GENE*', 'size': 116, 'sub': 'Mutation'})
S.punch(T('thrifty'), 0.14, 0.8)
g0 = T('aur', T('mutation')) - 0.1; g1 = TE('karenge') + 0.25
S.card(g0, g1)
S.add({'type': 'chain', 't0': g0, 't1': g1, 'y': 150, 'title': 'Thrifty genes kya karte hain', 'show': 4, 'items': [
    {'t': T('storer'), 'icon': '🏦', 'text': 'Body = *storer*', 'st': ''},
    {'t': T('khana', T('jo')), 'icon': '🍚', 'text': 'Jo bhi khana mile', 'st': ''},
    {'t': T('fat'), 'icon': '🧈', 'text': 'Zyada se zyada *fat*', 'st': '↑'},
    {'t': T('store', T('fat')), 'icon': '📦', 'text': 'Store kar lo', 'st': ''},
    {'t': T('kal'), 'icon': '❓', 'text': 'Kal khana na mile toh?', 'st': ''}]})
S.add({'type': 'title', 't0': T('aur', T('karenge')) - 0.05, 't1': T('kyunki', T('gaya')) - 0.08, 'y': 170, 'kicker': 'Thrifty gene', 'lines': ['200 saal pehle: ^survival^', 'Aaj: ~disease~'], 'sizes': [76, 96]})
S.add({'type': 'title', 't0': T('kyunki', T('gaya')) - 0.05, 't1': T('zomato') - 0.08, 'y': 170, 'lines': ['Kami nahi', '*Surplus* hai'], 'sizes': [84, 108]})
S.add({'type': 'chips', 't0': T('zomato') - 0.1, 't1': T('par', T('ho')) - 0.08, 'y': 140, 'items': [
    {'t': T('zomato'), 'icon': '🛵', 'text': 'Zomato'}, {'t': T('swiggy'), 'icon': '🛵', 'text': 'Swiggy'},
    {'t': T('fridge'), 'icon': '🧊', 'text': 'Bhara fridge'}, {'t': T('kooda.*'), 'icon': '🗑️', 'text': 'Pet = *kooda-daan*'}]})
S.add({'type': 'title', 't0': T('par', T('ho')) - 0.05, 't1': T('aur', T('the')) - 0.08, 'y': 170, 'kicker': 'Par body + genes', 'lines': ['Abhi bhi *store*', 'mode mein'], 'sizes': [100, 84]})
S.add({'type': 'slam', 't0': T('tofi') - 0.1, 't1': T('bahar', T('inside')) - 0.05, 'y': 200, 'text': '*T.O.F.I.*', 'size': 130, 'sub': 'Thin Outside · Fat Inside'})
S.punch(T('tofi'), 0.14, 0.9)
S.add({'type': 'title', 't0': T('aur', T('the')) - 0.05, 't1': T('tofi') - 0.12, 'y': 170, 'kicker': 'Isi liye Indians ka', 'lines': ['*Phenotype*'], 'sizes': [112]})
t0_ = T('bahar', T('inside')) - 0.1; t1_ = TE('hai', T('heart')) + 0.25
S.card(t0_, t1_)
S.add({'type': 'chain', 't0': t0_, 't1': t1_, 'y': 150, 'title': 'TOFI body', 'show': 4, 'items': [
    {'t': T('bahar', T('inside')), 'icon': '🧍', 'text': 'Bahar se patla', 'st': ''},
    {'t': T('visceral'), 'icon': '⚠️', 'text': 'Andar *visceral fat*', 'st': '↑'},
    {'t': T('insulin'), 'icon': '💉', 'text': 'Insulin resistance', 'st': '↑'},
    {'t': T('diabetes'), 'icon': '🩸', 'text': 'Diabetes risk', 'st': '↑'},
    {'t': T('heart'), 'icon': '❤️', 'text': 'Heart risk', 'st': '↑'}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
p0 = T('aur', T('heart')) - 0.05; p1 = T('kyunki', T('comparison')) - 0.08
S.add({'type': 'title', 't0': p0, 't1': T('indians', p0) - 0.08, 'y': 170, 'lines': ['Iska *proof*?'], 'sizes': [112]})
q0 = T('indians', p0) - 0.1
S.card(q0, p1)
S.add({'type': 'checklist', 't0': q0, 't1': p1, 'y': 170, 'title': 'America mein Indians vs Whites', 'items': [
    {'t': T('khaana', q0), 'text': 'Same <span>khaana</span>', 'mark': 'check'},
    {'t': T('same', q0), 'text': 'Same <span>lifestyle</span>', 'mark': 'check'},
    {'t': T('diabetes', q0), 'text': 'Phir bhi <span>diabetes ↑</span>', 'mark': 'x'},
    {'t': T('heart', q0), 'text': 'Heart disease <span>↑</span>', 'mark': 'x'}]})
S.add({'type': 'title', 't0': p1 - 0.03, 't1': T('par', p1) - 0.08, 'y': 170, 'lines': ['*Genes* change', 'ho chuke hain'], 'sizes': [108, 84]})
S.add({'type': 'slam', 't0': T('par', p1) - 0.05, 't1': T('matlab', p1) - 0.05, 'y': 200, 'text': 'Genetics ≠ *sentence*', 'size': 100, 'sub': 'Sirf ek predisposition'})
S.punch(T('sentence'), 0.12, 0.8)
S.add({'type': 'title', 't0': T('matlab', p1) - 0.03, 't1': T('genetics', T('kheenchte')) - 0.08, 'y': 170, 'lines': ['Gun *loaded* hai', 'Trigger = ^lifestyle^'], 'sizes': [92, 92]})
l0 = T('genetics', T('kheenchte')) - 0.1; l1 = T('par', T('hai', T('control'))) - 0.08
S.card(l0, l1)
S.add({'type': 'compare', 't0': l0, 't1': l1, 'y': 170, 'title': 'Aapki health', 'max': 70, 'items': [
    {'t': l0 + 0.2, 'label': 'Genetics', 'text': '30%', 'value': 30, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('lifestyle', l0), 'label': 'Lifestyle', 'text': '70%', 'value': 70, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'}]})
S.add({'type': 'title', 't0': l1 + 0.03, 't1': T('western') - 0.08, 'y': 170, 'kicker': 'Indian body ke liye', 'lines': ['*Special protocol*'], 'sizes': [100]})
S.add({'type': 'badge', 't0': T('western') - 0.05, 't1': T('aur', T('programmed')) - 0.08, 'y': 200, 'text': 'Western diet plans ✗', 'sub': 'Hamari body *differently programmed* hai'})
cta = T('toh', T('chahiye', T('agar'))) - 0.1
S.add({'type': 'badge', 't0': T('aur', T('programmed')) - 0.05, 't1': cta - 0.05, 'y': 200, 'text': 'Mera system', 'sub': 'Sab kuch ek *system* mein'})
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'System chahiye?', 'title': 'Comment<br>*"HEALTH"*', 'sub': 'Mera kaam tha science pahunchana · You are watching FitFinfluencer', 'button': '💬 COMMENT "HEALTH"', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'indians', r'charbi', r'patla', r'patle', r'mota', r'pet', r'british', r'raj', r'bengal', r'madras', r'famine', r'bhookhe', r'generations', r'dna',
                           r'thrifty', r'genes?', r'mutation', r'storer', r'fat', r'store', r'survival', r'disease', r'surplus', r'zomato', r'swiggy', r'fridge', r'tofi',
                           r'visceral', r'insulin', r'diabetes', r'heart', r'proof', r'genetics', r'sentence', r'predisposition', r'lifestyle', r'protocol', r'system', r'health'])
B = S.broll
B(28894, T('generations') - 0.1, h1 - 0.1, off=1.0)
B(4733, T('dna') - 0.1, a1 - 0.1, off=2.0)
B(26089, T('zomato') - 0.1, T('fridge') - 0.05, off=1.0)
B(3533, T('fridge') - 0.05, T('aap', T('cheezein')) - 0.05, off=1.0)
B(4779, T('diabetes') - 0.1, T('aur', T('heart')) - 0.1, off=1.0)
B(4437, T('america') - 0.3, T('same', T('americans')) - 0.05, off=2.0)
B(722, T('apni', T('kheenchte')) - 0.1, l0 - 0.1, off=3.0)
B(4547, T('aur', T('programmed')) - 0.05, cta - 0.1, off=3.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

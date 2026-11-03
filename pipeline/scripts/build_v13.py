import sys
from spec_lib import Spec
S = Spec(sys.argv[1], 'v13'); T, TE = S.T, S.TE
D = S.tl['dur']
S.add({'type': 'title', 't0': 0.05, 't1': T('poha') - 0.05, 'y': 150, 'lines': ['Aaj subah', 'kya *khaya*?'], 'sizes': [84, 112], 'hideCaps': True})
S.add({'type': 'chips', 't0': T('poha') - 0.05, 't1': T('par') - 0.1, 'y': 140, 'items': [
    {'t': T('poha'), 'icon': '🍚', 'text': 'Poha'}, {'t': T('upma'), 'icon': '🥣', 'text': 'Upma'},
    {'t': T('aloo'), 'icon': '🫓', 'text': 'Aloo paratha'}, {'t': T('bread'), 'icon': '🍞', 'text': 'Bread butter'},
    {'t': T('healthy'), 'icon': '🤔', 'text': '"*Healthy*" samajh ke'}]})
S.add({'type': 'slam', 't0': T('naked') - 0.05, 't1': T('ab') - 0.05, 'y': 200, 'text': '*NAKED* CARB', 'size': 130, 'sub': 'Carb jisne kapde nahi pehne'})
S.punch(T('naked'), 0.14, 0.8)
k0 = T('ab') - 0.1; k1 = TE('hai', T('banti')) + 0.25
S.card(k0, k1)
kn = [{'t': T('fiber'), 'x': 260, 'y': 90, 'icon': '🥗', 'text': '*Fiber* layer'},
      {'t': T('protein'), 'x': 740, 'y': 90, 'icon': '🥚', 'text': '*Protein* layer'},
      {'t': T('carb', T('dono')), 'x': 500, 'y': 280, 'icon': '🍚', 'text': 'Carb'},
      {'t': T('proper'), 'x': 500, 'y': 470, 'icon': '🍽️', 'text': 'Proper *meal*', 'target': True}]
kw = [{'t': T('dono') - 0.1, 'd': 'M 260 140 C 260 230, 380 270, 400 275'}, {'t': T('dono') - 0.1, 'd': 'M 740 140 C 740 230, 620 270, 600 275'},
      {'t': T('proper') - 0.35, 'd': 'M 500 330 L 500 410'}]
S.add({'type': 'title', 't0': k0, 't1': T('ek', k0) - 0.1, 'y': 280, 'lines': ['Carb ke *kapde*?'], 'sizes': [104]})
S.add({'type': 'flow', 't0': T('ek', k0) - 0.1, 't1': k1, 'y': 170, 'w': 1000, 'h': 600, 'nodes': kn, 'wires': kw})
c0 = T('ab', k1 - 0.3) - 0.1; c1 = TE('ki', T('aankh')) + 0.25
S.card(c0, c1)
S.add({'type': 'chain', 't0': c0, 't1': c1, 'y': 150, 'title': 'Naked carb khaya toh', 'show': 4, 'items': [
    {'t': T('poha', c0), 'icon': '🍚', 'text': 'Poha → glucose', 'st': ''},
    {'t': T('spike', c0), 'icon': '📈', 'text': 'Blood sugar spike', 'st': '↑↑'},
    {'t': T('insulin', c0), 'icon': '💉', 'text': 'Insulin aggressive', 'st': '↑↑'},
    {'t': T('crash'), 'icon': '📉', 'text': 'Sugar crash', 'st': '↓↓'},
    {'t': T('brain', c0), 'icon': '🧠', 'text': 'Brain energy khatam', 'st': ''},
    {'t': T('neend'), 'icon': '😴', 'text': 'Neend · lethargy', 'st': ''},
    {'t': T('focus'), 'icon': '🎯', 'text': 'Focus gaya', 'st': '✗'},
    {'t': (T('baje') - 0.7), 'icon': '🕑', 'text': '2–3 baje aankh band', 'st': ''}]})
for it in S.events[-1]['items']: it['stc'] = 'red'
S.add({'type': 'title', 't0': T('ab', c1 - 0.3) - 0.05, 't1': T('pehle', c1) - 0.1, 'y': 170, 'kicker': 'Wahi poha', 'lines': ['*Dress up* karke?'], 'sizes': [104]})
d0 = T('pehle', c1) - 0.1; d1 = TE('bani') + 0.25
S.card(d0, d1)
S.add({'type': 'checklist', 't0': d0, 't1': d1, 'y': 170, 'title': 'Dressed-up poha', 'items': [
    {'t': T('salad'), 'text': '1. Pehle <span>salad · kheera, tamatar</span>', 'mark': 'check'},
    {'t': T('resistant'), 'text': 'Fiber <span>· gut mein layer</span>', 'mark': 'check'},
    {'t': T('poha', T('layer', d0)), 'text': '2. Poha <span>+ protein</span>', 'mark': 'check'},
    {'t': T('sprouts'), 'text': 'Sprouts · chane <span>· anda</span>', 'mark': 'check'}]})
g0 = T('ab', d1 - 0.3) - 0.1; g1 = TE('karega', T('crash', d1)) + 0.25
S.card(g0, g1)
S.add({'type': 'chain', 't0': g0, 't1': g1, 'y': 150, 'title': 'Ab kya hota hai', 'show': 4, 'items': [
    {'t': T('slowly', g0), 'icon': '🐢', 'text': 'Glucose slowly release', 'st': ''},
    {'t': T('gently', g0, 2), 'icon': '〰️', 'text': 'Insulin gently spike', 'st': ''},
    {'t': T('normal', g0), 'icon': '✅', 'text': 'Insulin normal', 'st': ''},
    {'t': T('crash', g0), 'icon': '🛡️', 'text': 'No crash', 'st': '✓'}]})
for it in S.events[-1]['items']: it['stc'] = 'green'
S.add({'type': 'title', 't0': T('toh', g1 - 0.3) - 0.05, 't1': T('carb', T('galat')) - 0.08, 'y': 170, 'lines': ['Baar baar *bhookh*', '~nahi lagegi~'], 'sizes': [92, 84]})
S.add({'type': 'slam', 't0': T('carb', T('galat')) - 0.05, 't1': T('aur', T('mote')) - 0.05, 'y': 200, 'text': 'Carb ✓<br>~Naked carb~ ✗', 'size': 104})
S.punch(T('naked', T('galat')), 0.12, 0.9)
S.add({'type': 'chips', 't0': T('aur', T('mote')) - 0.05, 't1': T('maine') - 0.1, 'y': 140, 'items': [
    {'t': T('breakfast'), 'icon': '🍳', 'text': 'Breakfast'}, {'t': T('lunch'), 'icon': '🍛', 'text': 'Lunch'},
    {'t': T('dinner'), 'icon': '🍲', 'text': 'Dinner'}, {'t': T('snacks'), 'icon': '🍪', 'text': 'Snacks'},
    {'t': T('management'), 'icon': '📊', 'text': '*Glucose management*'}]})
m0 = T('maine') - 0.1; m1 = TE('banaya') + 0.25
S.card(m0, m1)
S.add({'type': 'checklist', 't0': m0, 't1': m1, 'y': 170, 'title': 'Maine vajan ghataya toh samjha', 'items': [
    {'t': T('kami'), 'text': 'Body mein <span>kya kami hai</span>', 'mark': 'check'},
    {'t': T('insulin', m0), 'text': 'Insulin <span>kaise spike hota</span>', 'mark': 'check'},
    {'t': T('meter'), 'text': 'Glucose meter <span>se tracking</span>', 'mark': 'check'},
    {'t': T('architecture'), 'text': 'Meal ka <span>architecture</span>', 'mark': 'check'}]})
S.add({'type': 'title', 't0': T('aur', m1 - 0.3) - 0.05, 't1': T('jab', T('confidence')) - 0.1, 'y': 160, 'kicker': 'Aaj meri body', 'lines': ['*Thank you* bolti hai'], 'sizes': [100]})
S.add({'type': 'title', 't0': T('jab', T('confidence')) - 0.05, 't1': T('toh', T('soch')) - 0.05 if False else T('mera', T('soch')) - 0.1, 'y': 170, 'lines': ['Thaali =', '*Science* ki basis pe'], 'sizes': [84, 96]})
cta = T('mera', T('soch')) - 0.15
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'You are watching', 'title': 'Fit<span class="acc">Finfluencer</span>', 'sub': 'Mera kaam tha science pahunchana · decision aapka hai', 'button': 'FOLLOW FOR MORE', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.1, 1.28]); S.cam['faceY'] = 0.40
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'poha', r'upma', r'paratha', r'bread', r'healthy', r'naked', r'carb', r'fiber', r'protein', r'meal', r'glucose', r'spike', r'insulin',
                           r'crash', r'pancreas', r'neend', r'focus', r'salad', r'sprouts', r'anda', r'gently', r'bhookh', r'architecture', r'science', r'thaali'])
B = S.broll
B(43030, T('bread') - 0.1, T('healthy') - 0.05, off=1.0)
B(5078, T('glucose', c0) - 0.1, T('theek', c0) - 0.05, off=2.0)
B(4607, T('neend') - 0.1, T('focus') - 0.05, off=2.0)
B(42620, T('focus'), (T('baje') - 0.7) - 0.05, off=1.0)
B(51405, (T('baje') - 0.7), c1 - 0.1, off=2.0)
B(43908, T('salad') - 0.1, T('kyunki', T('salad')) - 0.05, off=1.0)
B(42910, T('anda') - 0.3, d1 - 0.1, off=1.0)
B(10431, T('breakfast') - 0.1, T('sabka') - 0.05, off=1.0)
B(44432, T('vajan') - 0.2, T('ki', T('chali')) - 0.05, off=1.0)
B(31407, T('itna', T('bataun')) - 0.1, T('jab', T('confidence')) - 0.08, off=1.0)
B(40531, T('thaali') - 0.3, cta, off=1.0)
S.save(caps, cta_t=cta, hold=1.2, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

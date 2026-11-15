import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v32', mood='energetic'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('chai') - 0.05, ['EVERY HOUSE', 'YOU VISIT...'], x=540, y=300, sizes=[90, 90], anim='rise', stagger=0.5)
K(T('chai') - 0.05, T('subah') - 0.05, ['"HAVE SOME CHAI, BETA."', '"TAKE A BISCUIT."'], x=540, y=300, sizes=[76, 76], font='serif', anim='rise', stagger=1.3)
Bh(T('subah') - 0.03, T('ye', T('yaar')) - 0.05, 'CHAI + BISCUIT', size=210, font='anton', anim='slam', color=Y)
K(T('ye', T('yaar')) - 0.03, T('ye', T('breakfast')) - 0.05, ['THIS IS', '~NOT BREAKFAST~'], x=70, y=300, align='left', sizes=[100, 120], anim='slam')
S.add({'type': 'stamp', 't0': T('slow') - 0.1, 't1': T('aur', T('poison')) - 0.05, 'y': 1180, 'text': 'SLOW POISON', 'rot': -7, 'size': 120}); S.punch(T('slow'), 0.14, 0.7)
K(T('aur', T('poison')) - 0.03, T('ek') - 0.05, ["CRORES OF PEOPLE'S", '*DAILY ROUTINE*'], x=540, y=300, sizes=[76, 100], anim='rise')
S.add({'type': 'chips', 't0': T('ek') - 0.05, 't1': T('ab', T('naashta')) - 0.05, 'y': 240, 'items': [
    {'t': T('chai', T('ek') - 0.1), 'text': '1 chai'}, {'t': T('biscuit', T('ek')), 'text': '2 biscuits'}, {'t': T('namkeen'), 'text': 'Some namkeen'},
    {'t': T('naashta') - 0.1, 'text': '= *Breakfast done?*'}]})
K(T('ab', T('naashta')) - 0.03, T('aur', T('dekhna')) - 0.05, ["LET'S BREAK IT", '*WITH SCIENCE*'], x=540, y=300, sizes=[90, 110], anim='slam')
K(T('aur', T('dekhna')) - 0.03, T('ab', T('na', T('healthy'))) - 0.05, ['SEND THIS TO', '*YOUR PARENTS*'], x=1010, y=300, align='right', sizes=[84, 110], anim='slam')
# ---------------- the chai
a0 = T('ab', T('na', T('healthy'))) - 0.08; a1 = T('isi', T('resistant')) - 0.08
K(a0 + 0.05, T('do', T('chai', a0)) - 0.05, ['THE CHAI:', 'MILK + *SUGAR*'], x=540, y=300, sizes=[96, 110], anim='slam')
B(5078, T('do', T('chai', a0)) - 0.05, T('10') - 0.05, off=0.5)
S.add({'type': 'stat', 't0': T('10') - 0.05, 't1': T('glucose') - 0.05, 'y': 260, 'kicker': '2 spoons of sugar', 'from': 0, 'to': 10, 'unit': ' g', 'label': 'Into your body *at once*', 'dir': 'up', 'count': 0.8})
S.card(T('glucose') - 0.08, T('aur', T('resistance')) - 0.08)
S.add({'type': 'chain', 't0': T('glucose') - 0.08, 't1': T('aur', T('resistance')) - 0.08, 'y': 150, 'title': 'What the sugar does', 'show': 4, 'items': [
    {'t': T('glucose'), 'text': 'Instant *glucose spike*', 'st': 'up', 'stc': 'red'}, {'t': T('surge'), 'text': '*Insulin surge*', 'st': 'up', 'stc': 'red'},
    {'t': T('cells'), 'text': 'Cells become *insulin resistant*', 'st': 'no', 'stc': 'red'}, {'t': T('resistance'), 'text': '= ~Insulin resistance~', 'st': 'no', 'stc': 'red'}]})
Bh(T('aur', T('resistance')) - 0.03, T('ab', T('raasta')) - 0.05, 'TYPE 2 DIABETES', size=190, font='anton', anim='slam', color=R)
K(T('raasta') - 0.1, T('ab', T('raasta')) - 0.05, ['THE STRAIGHT ROAD'], x=540, y=1540, sizes=[70], font='oswald', anim='rise')
# ---------------- the biscuit
b0 = T('ab', T('raasta')) - 0.05
K(b0, T('maida') - 0.05, ['NOW,', 'THE *BISCUIT*'], x=540, y=300, sizes=[90, 120], anim='slam')
b1 = T('ab', T('galat')) - 0.08
S.card(T('maida') - 0.08, b1)
S.add({'type': 'chain', 't0': T('maida') - 0.08, 't1': b1, 'y': 150, 'title': "What's inside", 'show': 4, 'items': [
    {'t': T('maida'), 'text': '*Maida* (refined flour)'}, {'t': T('85'), 'text': 'Glycemic index *85+*', 'st': 'up', 'stc': 'red'},
    {'t': T('palm'), 'text': '*Palm oil*: saturated fat', 'st': 'up', 'stc': 'red'}, {'t': T('ldl'), 'text': 'Raises *LDL cholesterol*', 'st': 'up', 'stc': 'red'},
    {'t': T('umar'), 'text': '~"It rises with age"~: wrong', 'st': 'no', 'stc': 'red'}]})
S.add({'type': 'stamp', 't0': T('galat') - 0.1, 't1': b1 + 0.8, 'y': 1180, 'text': 'WRONG', 'rot': -7, 'size': 130})
Bh(T('ab', T('galat')) - 0.03, T('68') - 0.05, 'HIDDEN SUGAR', size=230, font='anton', anim='slam', color=R)
S.add({'type': 'stat', 't0': T('68') - 0.05, 't1': T('aur', T('sugar', T('extra'))) - 0.05, 'y': 260, 'kicker': 'Sugar in 4 biscuits', 'from': 0, 'to': 8, 'unit': ' g', 'label': '*6-8 g*: even 2 biscuits = *4 g extra*', 'dir': 'up', 'count': 0.8})
K(T('aur', T('sugar', T('extra'))) - 0.03, T('ab', T('khatarnaak')) - 0.05, ['SOME BRANDS:', '~TRANS FAT~'], x=70, y=300, align='left', sizes=[90, 120], anim='slam')
K(T('khatarnaak') - 0.1, T('toh', T('khaaoge')) - 0.05, ['THE WORST FOR', 'YOUR *ARTERIES*'], x=540, y=1540, sizes=[56, 70], font='oswald', anim='rise')
K(T('toh', T('khaaoge')) - 0.03, T('ab', T('badhegi')) - 0.05, ['BP GOES *UP*'], x=540, y=330, sizes=[130], font='anton', anim='slam')
# ---------------- the namkeen
n0 = T('ab', T('badhegi')) - 0.08; n1 = T('toh', T('rahe', T('tihaai'))) - 0.08
K(n0 + 0.05, T('ek', n0) - 0.05, ['AND THE', '*NAMKEEN*'], x=540, y=300, sizes=[90, 120], anim='slam')
S.card(T('ek', n0) - 0.08, n1)
S.add({'type': 'compare', 't0': T('ek', n0) - 0.08, 't1': n1, 'y': 170, 'title': 'Sodium: one serving vs daily limit', 'max': 1500, 'items': [
    {'t': T('300') - 0.1, 'label': 'One serving', 'unit': ' mg', 'value': 500, 'text': '300-500', 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'},
    {'t': T('1500') - 0.1, 'label': 'BP daily limit', 'unit': ' mg', 'value': 1500, 'cls': 'acc', 'color': 'linear-gradient(180deg,#FFD873,#E59A00)'}]})
# ---------------- summary
m0 = n1 + 0.02; m1 = T('aur', T('micronutrients')) - 0.08
S.card(m0, m1)
S.add({'type': 'checklist', 't0': m0, 't1': m1, 'y': 150, 'title': 'Your "small breakfast"', 'items': [
    {'t': T('spike', m0), 'text': '*Sugar spike*', 'mark': 'x'}, {'t': T('resistance', m0), 'text': '*Insulin resistance*', 'mark': 'x'},
    {'t': T('ldl', m0), 'text': 'Higher *LDL*', 'mark': 'x'}, {'t': T('sodium', m0), 'text': '1/3 of your *sodium*', 'mark': 'x'},
    {'t': T('fiber'), 'text': 'No fiber, no protein', 'mark': 'x'}, {'t': T('micronutrients'), 'text': 'No micronutrients', 'mark': 'x'}]})
K(T('aur', T('micronutrients')) - 0.03, T('aap', T('nahi', T('behtar'))) - 0.05, ['"NOTHING BEATS', 'CHAI BISCUIT"'], x=540, y=300, sizes=[90, 90], font='serif', anim='type')
Bh(T('aap', T('nahi', T('behtar'))) - 0.03, T('ab', T('nashedi')) - 0.05, 'ADDICTED', size=330, font='anton', anim='slam', color=R)
# ---------------- replacement
r0 = T('ab', T('nashedi')) - 0.05
K(r0, T('chai', T('replacement', r0 + 3)) - 0.05, ['THE *REPLACEMENT*', '(SEND IT TO YOUR PARENTS)'], x=540, y=300, sizes=[110, 56], anim='slam', stagger=0.6)
s0 = T('chai', T('replacement', r0 + 3)) - 0.08; s1 = T('aapki', T('same')) - 0.08
S.card(s0, s1)
S.add({'type': 'checklist', 't0': s0, 't1': T('aap', T('jagah', T('biscuit', T('paani')))) - 0.05, 'y': 150, 'title': 'Swap the chai', 'items': [
    {'t': T('cheeni', s0), 'text': '*No sugar*', 'mark': 'check'}, {'t': T('doodh', s0), 'text': '*No milk*', 'mark': 'check'},
    {'t': T('paani', s0), 'text': 'Make it with *water*', 'mark': 'check'}]})
S.add({'type': 'checklist', 't0': T('aap', T('jagah', T('biscuit', T('paani')))) - 0.05, 't1': T('same') - 0.05, 'y': 150, 'title': 'Swap the biscuit + namkeen', 'items': [
    {'t': T('omelette'), 'text': 'Omelette', 'mark': 'check'}, {'t': T('akhrot'), 'text': 'Walnuts', 'mark': 'check'}, {'t': T('kela'), 'text': 'Banana', 'mark': 'check'},
    {'t': T('chana'), 'text': 'Roasted chana', 'mark': 'check'}, {'t': T('makhana'), 'text': 'Makhana', 'mark': 'check'}]})
K(T('same') - 0.03, s1, ['SAME CONVENIENCE.', '^DAMAGE CONTROLLED.^'], x=540, y=300, sizes=[84, 96], anim='rise', stagger=0.9)
B(5075, T('same') - 0.05, s1, off=0.5)
K(T('aapki', T('same')) - 0.03, T('agar', T('audit')) - 0.05, ['YOUR PLATE DECIDES', '*YOUR HEALTH*'], x=540, y=300, sizes=[80, 110], anim='slam')
K(T('agar', T('audit')) - 0.03, T('mera') - 0.05, ['AUDIT', 'YOUR PLATE.'], x=540, y=300, sizes=[130, 110], font='anton', anim='slam')
cta = T('mera') - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Your parents need this', 'title': 'Send it<br>*to them*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'SHARE', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'chai', r'biscuit', r'breakfast', r'slow', r'poison', r'namkeen', r'science', r'healthy', r'cheeni', r'10', r'glucose', r'spike',
                           r'insulin', r'resistan.*', r'diabetes', r'maida', r'refined', r'85', r'palm', r'saturated', r'ldl', r'cholesterol', r'hidden', r'sugar',
                           r'trans', r'arteries', r'bp', r'sodium', r'1500', r'tihaai', r'fiber', r'protein', r'micronutrients', r'nashedi', r'replacement',
                           r'doodh', r'paani', r'omelette', r'akhrot', r'kela', r'chana', r'makhana', r'plate', r'audit'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})


import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v34', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('toh') - 0.05, ['IF SALT IS', '~POISON~...'], x=540, y=300, sizes=[100, 140], anim='slam')
K(T('toh') - 0.03, T('kisi') - 0.05, ['WHY DO HOSPITALS', 'PUT IT *IN YOUR VEINS?*'], x=540, y=300, sizes=[80, 90], anim='rise', stagger=0.6)
S.add({'type': 'chips', 't0': T('kisi') - 0.05, 't1': T('saline') - 0.05, 'y': 240, 'items': [
    {'t': T('stroke'), 'text': 'Stroke'}, {'t': T('heart'), 'text': 'Heart attack'}, {'t': T('collapse'), 'text': 'Collapse'}, {'t': T('behosh'), 'text': 'Unconscious'}]})
K(T('pooche') - 0.1, T('saline') - 0.05, ['NO QUESTIONS ASKED'], x=540, y=1540, sizes=[60], font='oswald', anim='rise')
Bh(T('saline') - 0.03, T('ab') - 0.05, 'SALINE', size=360, font='anton', anim='slam', color=Y); S.punch(T('saline'), 0.12, 0.7)
K(T('nacl') - 0.1, T('ab') - 0.05, ['= NaCl = *SODIUM CHLORIDE*'], x=540, y=1540, sizes=[60], font='oswald', anim='rise')
s0 = T('ab') - 0.08; s1 = T('ab', T('nason')) - 0.08
S.card(s0, s1)
S.add({'type': 'stat', 't0': s0, 't1': s1, 'y': 200, 'kicker': 'Sodium in one saline bag', 'from': 0, 'to': 9000, 'unit': ' mg', 'label': 'Sometimes *2 bags* = *18,000 mg*', 'pill': 'Straight into your veins', 'dir': 'up', 'count': 1.2})
# ---------------- what sodium does
n0 = T('ab', T('nason')) - 0.08; n1 = T('ab', T('dengi')) - 0.08
S.card(n0, n1)
S.add({'type': 'checklist', 't0': n0, 't1': n1, 'y': 150, 'title': 'Sodium is an electrolyte', 'items': [
    {'t': T('balance'), 'text': 'Water balance *in and out of cells*', 'mark': 'check'}, {'t': T('kidneys'), 'text': 'Kidneys *filter*', 'mark': 'check'},
    {'t': T('heart', n0), 'text': 'Heart *pumps*', 'mark': 'check'}, {'t': T('nerves'), 'text': 'Nerves *signal*', 'mark': 'check'}]})
# ---------------- the secret function
k0 = T('ab', T('dengi')) - 0.05
Bh(k0, T('jab', k0) - 0.05, 'SECRET', size=380, font='anton', anim='slam', color=G)
K(k0 + 0.3, T('jab', k0) - 0.05, ["YOUR KIDNEYS' SECRET FUNCTION"], x=540, y=1540, sizes=[56], font='oswald', anim='rise')
c0 = T('jab', k0) - 0.08; c1 = T('aapko', T('meethe')) - 0.08
S.card(c0, c1)
S.add({'type': 'chain', 't0': c0, 't1': c1, 'y': 150, 'title': 'When sodium is low', 'show': 4, 'items': [
    {'t': T('kam', c0), 'text': 'Sodium *low*', 'st': 'down', 'stc': 'red'}, {'t': T('reabsorb'), 'text': 'Kidneys must *reabsorb* sodium'},
    {'t': T('insulin', c0), 'text': 'That needs *insulin* to rise', 'st': 'up', 'stc': 'red'}, {'t': T('pancreas'), 'text': 'Brain signals the *pancreas*'},
    {'t': T('blood', c0), 'text': 'Blood sugar pulled into cells'}, {'t': T('drop'), 'text': '*Sugar drops*', 'st': 'down', 'stc': 'red'},
    {'t': T('danger'), 'text': 'Brain: ~"DANGER!"~', 'st': 'no', 'stc': 'red'}, {'t': T('meetha'), 'text': '*Craving sweets*', 'st': 'up', 'stc': 'red'}]})
S.fx('sub_drop', T('danger'), -12)
# ---------------- the twist
K(T('aapko', T('meethe')) - 0.03, T('par', T('aapko', T('meethe'))) - 0.05, ['YOU THOUGHT YOU', 'NEEDED *SUGAR*'], x=70, y=300, align='left', sizes=[84, 110], anim='slam')
K(T('par', T('aapko', T('meethe'))) - 0.03, T('aur', T('namak', T('par', T('aapko', T('meethe'))))) - 0.05, ['YOUR BODY NEEDED', '^SALT^'], x=1010, y=300, align='right', sizes=[84, 140], anim='slam')
K(T('aur', T('namak', T('par', T('aapko', T('meethe'))))) - 0.03, T('taaki') - 0.05, ['SO THE WORLD MADE', 'SALT ~THE VILLAIN~'], x=540, y=300, sizes=[80, 110], anim='slam')
K(T('taaki') - 0.03, T('ek', T('taaki')) - 0.05, ['SO THE *SUGAR INDUSTRY*', 'COULD SHINE'], x=540, y=300, sizes=[84, 84], anim='rise', stagger=0.8)
# ---------------- excess salt vs sugar
x0 = T('ek', T('taaki')) - 0.08; x1 = T('ab', T('permanently')) - 0.08
S.card(x0, x1)
S.add({'type': 'compare', 't0': x0, 't1': x1, 'y': 170, 'title': 'What happens to the excess', 'max': 10, 'items': [
    {'t': T('salt', x0), 'label': 'Excess salt', 'text': 'URINE', 'value': 4, 'cls': 'green', 'color': 'linear-gradient(180deg,#5CFFB5,#0FA968)'},
    {'t': T('sugar', x0), 'label': 'Excess sugar', 'text': 'FAT', 'value': 10, 'cls': 'red', 'color': 'linear-gradient(180deg,#FF6B79,#C21D35)'}]})
K(T('permanently') - 0.1, x1, ['STORED ~PERMANENTLY~'], x=540, y=760, sizes=[60], font='oswald', anim='rise')
# ---------------- which salt
w0 = T('ab', T('permanently')) - 0.05
K(w0, T('salt', T('kaun')) - 0.05, ['HOW MUCH SODIUM', 'IS RIGHT *FOR YOU?*'], x=540, y=300, sizes=[84, 100], anim='rise')
S.add({'type': 'chips', 't0': T('salt', T('kaun')) - 0.05, 't1': T('aur', T('sea')) - 0.05, 'y': 240, 'items': [
    {'t': T('iodized'), 'text': 'Iodized?'}, {'t': T('rock'), 'text': 'Rock salt?'}, {'t': T('sea'), 'text': 'Sea salt?'}]})
S.add({'type': 'chips', 't0': T('aur', T('sea')) - 0.05, 't1': T('personalized') - 0.15, 'y': 240, 'items': [
    {'t': T('weight'), 'text': 'Body *weight*'}, {'t': T('activity'), 'text': 'Activity *level*'}, {'t': T('sweat'), 'text': '*Sweat* rate'}]})
Bh(T('personalized') - 0.1, T('kyunki', T('personalized')) - 0.05, 'PERSONAL', size=320, font='anton', anim='slam', color=G)
K(T('kyunki', T('personalized')) - 0.03, T('toh', T('kharab')) - 0.05, ['I TESTED IT', 'ON *MY OWN BODY*'], x=540, y=300, sizes=[90, 110], anim='rise', stagger=0.7)
K(T('toh', T('kharab')) - 0.03, T('mera') - 0.05, ['NOBODY', 'TOLD ME THIS'], x=540, y=300, sizes=[110, 110], anim='slam')
cta = T('mera') - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Salt is not the villain', 'title': 'Follow for<br>*more science*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'FOLLOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'namak', r'zeher', r'hospital', r'stroke', r'heart', r'collapse', r'behosh', r'saline', r'nacl', r'sodium', r'chloride', r'9000',
                           r'18000', r'nason', r'electrolyte', r'balance', r'kidneys', r'nerves', r'secret', r'reabsorb', r'insulin', r'pancreas', r'sugar',
                           r'drop', r'danger', r'meetha', r'villain', r'industries', r'excess', r'salt', r'urine', r'fat', r'permanently', r'iodized', r'rock',
                           r'sea', r'weight', r'activity', r'sweat', r'personalized', r'science'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

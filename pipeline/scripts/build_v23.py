import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v23', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; K = S.kin; Bh = S.behind; B = S.broll
K(0.05, T('ek') - 0.05, ['WHAT YOU ARE ABOUT TO HEAR', '*CHANGED MY LIFE*'], x=70, y=280, align='left', sizes=[66, 110], anim='wipe')
K(T('ek') - 0.03, T('teen') - 0.05, ['A SECRET', 'NOBODY TALKS ABOUT'], x=1010, y=300, align='right', sizes=[120, 80], anim='slam'); S.fx('tension', T('ek') - 1.8, -15)
Bh(T('teen') - 0.05, T('aur', T('only')) - 0.05, '72 HOURS', size=330, font='anton', anim='slam')
K(T('teen') + 0.1, T('aur', T('only')) - 0.05, ['NO FOOD FOR 3 DAYS'], x=540, y=1600, sizes=[66], font='oswald', anim='rise')
K(T('aur', T('only')) - 0.03, T('chauthe') - 0.05, ['YOUR BODY DOES', '*SOMETHING MAGICAL*'], x=540, y=300, sizes=[84, 110], anim='rise')
Bh(T('chauthe') - 0.05, T('aur', T('on')) - 0.05, 'DAY 4', size=420, font='anton', anim='slam', color=G)
K(T('aapka', T('chauthe')) - 0.05, T('aur', T('on')) - 0.05, ['YOUR BRAIN *TURNS ON*'], x=540, y=1600, sizes=[64], font='oswald', anim='rise'); S.punch(T('brain'), 0.12, 0.7)
K(T('aur', T('on')) - 0.03, T('ab', T('sakte', T('maza'))) - 0.05, ['AND WHAT COMES NEXT', 'YOU CAN\'T EVEN *IMAGINE*'], x=540, y=300, sizes=[76, 96], anim='rise')
K(T('ab', T('sakte', T('maza'))) - 0.03, T('pehli') - 0.05, ['AFTER 72 HOURS', '*2 THINGS* HAPPEN'], x=70, y=300, align='left', sizes=[84, 120], anim='wipe')
# 1. CMA
a0 = T('pehli') - 0.1; a1 = T('normal', T('cleaning')) - 0.08
S.card(a0, a1)
S.add({'type': 'chain', 't0': a0, 't1': a1, 'y': 150, 'title': 'Number 1: autophagy', 'show': 4, 'items': [
    {'t': T('autophagy'), 'text': 'Autophagy switches on'}, {'t': T('normal'), 'text': 'Not *normal* autophagy'},
    {'t': T('cma', T('normal')), 'text': '*CMA*: chaperone-mediated'}, {'t': T('deep'), 'text': "The body's *deep cleaning*", 'st': 'yes', 'stc': 'green'}]})
c0 = a1 + 0.02; c1 = T('number') - 0.08
S.card(c0, c1)
cn = [{'t': c0 + 0.1, 'x': 500, 'y': 40, 'text': 'Normal: random clean-up'},
      {'t': T('protein', c0), 'x': 500, 'y': 165, 'text': 'CMA: *HSC70* protein', 'sub': 'finds old, damaged proteins'},
      {'t': T('lamp.*'), 'x': 500, 'y': 305, 'text': 'Carries them to *LAMP-2A*', 'sub': 'receptor'},
      {'t': T('lysosome'), 'x': 500, 'y': 440, 'text': 'Dumped into the *lysosome*'},
      {'t': T('destroy'), 'x': 500, 'y': 570, 'text': 'Destroyed: *deep clean*', 'target': True}]
cw = [{'t': T('protein', c0) - 0.3, 'd': 'M 500 80 L 500 110'}, {'t': T('lamp.*') - 0.3, 'd': 'M 500 225 L 500 255'},
      {'t': T('lysosome') - 0.3, 'd': 'M 500 360 L 500 400'}, {'t': T('destroy') - 0.3, 'd': 'M 500 480 L 500 525'}]
S.add({'type': 'flow', 't0': c0, 't1': c1, 'y': 110, 'w': 1000, 'h': 680, 'nodes': cn, 'wires': cw})
B(3968, T('lysosome') - 0.1, T('poori', T('lysosome')) - 0.05, off=1.0)
# 2. fat -> ketones
K(T('number') - 0.1, T('teen', T('number')) + 0.3, ['NUMBER 2'], x=540, y=300, sizes=[200], font='anton', anim='slam')
f0 = T('teen', T('number')) - 0.1; f1 = T('aur', T('ho', T('caffeine'))) - 0.08
S.card(f0, f1)
S.add({'type': 'chain', 't0': f0, 't1': f1, 'y': 150, 'title': 'By day 3', 'show': 4, 'items': [
    {'t': T('glucose', f0), 'text': 'Glucose: *used up*', 'st': 'down', 'stc': 'red'}, {'t': T('body', T('ka', T('glucose', f0))), 'text': 'Body burns *fat*'},
    {'t': T('fat', T('se', T('energy'))), 'text': 'Fat = dense *energy*', 'st': 'up', 'stc': 'green'}, {'t': T('caffeine'), 'text': 'Feels like *caffeine*'}]})
B(209, T('caffeine') - 0.1, f1 - 0.1, off=2.0)
k0 = f1 + 0.02; k1 = T('aur', T('leta')) - 0.08
S.card(k0, k1)
kn = [{'t': T('liver'), 'x': 500, 'y': 50, 'text': 'Liver makes *ketones*'},
      {'t': T('bhb'), 'x': 500, 'y': 200, 'text': '*BHB*', 'sub': 'beta-hydroxybutyrate'},
      {'t': T('barrier') - 0.5, 'x': 500, 'y': 360, 'text': 'Crosses the blood-brain barrier'},
      {'t': T('glucose', T('isko')), 'x': 500, 'y': 530, 'text': 'Brain fuel *better than glucose*', 'target': True}]
kw = [{'t': T('bhb') - 0.3, 'd': 'M 500 95 L 500 150'}, {'t': T('barrier') - 0.8, 'd': 'M 500 255 L 500 315'}, {'t': T('glucose', T('isko')) - 0.3, 'd': 'M 500 405 L 500 480'}]
S.add({'type': 'flow', 't0': k0, 't1': k1, 'y': 140, 'w': 1000, 'h': 640, 'nodes': kn, 'wires': kw})
# my experience
K(k1 + 0.03, T('then') - 0.05, ['MY 72-HOUR', '*WATER FAST*'], x=70, y=300, align='left', sizes=[100, 130], anim='wipe')
K(T('then') - 0.03, T('like') - 0.05, ['SUPER AWAKE.', 'MORE ENERGETIC.'], x=1010, y=300, align='right', sizes=[100, 100], anim='rise', stagger=0.6)
B(808, T('like') - 0.05, T('mujhe', T('caffeine')) - 0.08, off=1.0)
K(T('mujhe', T('caffeine')) - 0.03, T('aur', T('phir', T('khaaya'))) - 0.05, ['SO MUCH ENERGY', '~WITHOUT EATING~'], x=540, y=300, sizes=[100, 110], anim='rise')
K(T('aur', T('phir', T('khaaya'))) - 0.03, T('aur', T('evolution')) - 0.05, ['NOT HUNGER.', '*EVOLUTION.*'], x=540, y=300, sizes=[120, 150], anim='slam')
Bh(T('hunting') - 0.05, T('aur', T('baad', T('hunting'))) - 0.05, 'HUNTER MODE', size=260, font='anton', anim='slam')
K(T('aur', T('baad', T('hunting'))) - 0.03, T('jab', T('zindagi')) - 0.05, ['A DULL BRAIN', "CAN'T HUNT.", "*CAN'T SUCCEED.*"], x=70, y=260, align='left', sizes=[90, 90, 110], anim='rise', stagger=0.5)
e0 = T('jab', T('zindagi')) - 0.1; e1 = T('ab', T('gayi', T('badh'))) - 0.08
S.card(e0, e1)
S.add({'type': 'checklist', 't0': e0, 't1': e1, 'y': 150, 'title': 'My first 3-day fast', 'items': [
    {'t': T('do', T('honestly')), 'text': 'Day 1-2: <span>very hard</span>', 'mark': 'x'}, {'t': T('teesre'), 'text': 'Day 3: <span>magic</span>', 'mark': 'check'},
    {'t': T('clarity'), 'text': 'Clarity', 'mark': 'check'}, {'t': T('focus', T('clarity')), 'text': 'Focus', 'mark': 'check'}, {'t': T('energy', T('clarity')), 'text': 'Energy', 'mark': 'check'}]})
K(e1 + 0.03, T('cma', T('jaaye')) - 0.05, ['EVERY MONTH:', 'A *3-DAY FAST*'], x=70, y=300, align='left', sizes=[90, 130], anim='wipe')
K(T('cma', T('jaaye')) - 0.03, T('zombie') - 0.05, ['CMA ON.', 'DEEP CLEAN.'], x=1010, y=300, align='right', sizes=[120, 120], anim='slam')
Bh(T('zombie') - 0.05, T('aur', T('doonga')) - 0.05, 'ZOMBIE CELLS', size=230, font='anton', anim='slam', color=R)
K(T('zombie') + 0.2, T('aur', T('doonga')) - 0.05, ['ELIMINATED'], x=540, y=1600, sizes=[70], font='oswald', anim='rise')
K(T('aur', T('doonga')) - 0.03, T('110') - 0.05, ['A PROMISE', 'TO MYSELF'], x=540, y=300, sizes=[110, 110], font='serif', anim='rise')
S.add({'type': 'stat', 't0': T('110') - 0.05, 't1': T('ho', T('days')) - 0.08, 'y': 260, 'kicker': 'My transformation', 'fromText': '110 KG', 'from': 110, 'to': 85, 'unit': 'KG', 'label': 'In just 45 days', 'pill': 'Down 25 kg', 'dir': 'down', 'count': 1.2})
K(T('ho', T('days')) - 0.03, T('but', T('chahiye')) - 0.05, ['"IS THIS', 'EVEN SAFE?"'], x=540, y=300, sizes=[110, 130], font='serif', anim='rise')
K(T('but', T('chahiye')) - 0.03, T('har') - 0.05, ["I'LL NEVER SAY", 'FASTING IS ~BAD~'], x=70, y=300, align='left', sizes=[90, 120], anim='wipe')
K(T('har') - 0.03, T('aap', T('help')) - 0.05, ['FASTING HELPS', '*IN EVERYTHING*'], x=1010, y=300, align='right', sizes=[96, 120], anim='rise')
K(T('aap', T('help')) - 0.03, T('but', T('gaye')) - 0.05, ['EVEN WITH DIABETES:', 'SUGAR WON\'T CRASH', '*IF YOU DO IT RIGHT*'], x=540, y=260, sizes=[70, 90, 90], anim='rise', stagger=0.4)
w0 = T('but', T('gaye')) - 0.05; w1 = T('toh', T('chale')) - 0.08
S.add({'type': 'cine', 't0': w0, 't1': w1, 'h': 150})
S.add({'type': 'stamp', 't0': w0 + 0.1, 't1': T('main', T('seedha')) - 0.05, 'y': 1060, 'text': "DON'T START<br>WITH 3 DAYS", 'rot': -6, 'size': 100})
K(T('main', T('seedha')) - 0.03, w1, ['THERE ARE', '*RULES*'], x=540, y=300, sizes=[110, 180], anim='slam')
cta = w1 + 0.02
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want the full fasting rules?', 'title': 'Comment<br>*"HEALTH PROTOCOL"*', 'sub': 'My job was to bring you the science. The decision is yours.', 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'secret', r'72', r'hours', r'magic', r'brain', r'autophagy', r'cma', r'chaperone.*', r'deep', r'cleaning', r'hsc70', r'proteins?', r'lamp.*',
                           r'lysosome', r'destroy', r'glucose', r'fat', r'energy', r'caffeine', r'liver', r'ketones?', r'bhb', r'beta.*', r'barrier', r'efficiently',
                           r'evolution', r'hunting', r'sharp', r'clarity', r'focus', r'zombie', r'diabetes', r'rules', r'regulations', r'protocol'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})

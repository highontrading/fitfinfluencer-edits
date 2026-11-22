import sys
from spec_lib2 import Spec
S = Spec(sys.argv[1], 'v50', mood='serious'); T, TE = S.T, S.TE
D = S.tl['dur']; G = '#37F59B'; R = '#FF4D5E'; Y = '#FFC53D'; K = S.kin; Bh = S.behind; B = S.broll
# ---------------- hook
K(0.05, T('toh') - 0.05, ['"HOW DID YOU BUILD', 'THE *HEALTH PROTOCOL*?"'], x=540, y=300, sizes=[84, 96], anim='slam', stagger=0.8)
K(T('toh') - 0.03, T('ye', T('scenes')) - 0.05, ['FOR THE FIRST TIME:', '*BEHIND THE SCENES*'], x=540, y=300, sizes=[76, 110], anim='slam', stagger=0.8)
S.add({'type': 'chips', 't0': T('ye', T('scenes')) - 0.05, 't1': T('aur', T('banaye')) - 0.05, 'y': 220, 'items': [
    {'t': T('raat'), 'text': '~Not built overnight~'}, {'t': T('saal'), 'text': '*2 years* of research'},
    {'t': T('teen'), 'text': 'Tested on *3 family members*'}, {'t': T('hazaaron'), 'text': '*Thousands* of papers'}]})
# ---------------- my story
K(T('aur', T('banaye')) - 0.03, T('tabhi') - 0.05, ['I WAS ABOUT TO', '~GIVE UP~ ON MY BODY'], x=540, y=300, sizes=[90, 96], anim='slam', stagger=1.0)
K(T('tabhi') - 0.03, T('110') - 0.05, ['THEN: *FASTING*', 'TODAY: ^MUSCLES GROWING^'], x=540, y=300, sizes=[100, 84], anim='rise', stagger=1.4)
Bh(T('110') - 0.05, T('but', T('110')) - 0.05, '110 KG', size=320, font='anton', anim='slam', color=R)
K(T('doctor') - 0.1, T('but', T('110')) - 0.05, ['"LOSE WEIGHT OR YOU\'LL GET BP"'], x=540, y=1600, sizes=[56], font='oswald', anim='rise', fit=980)
K(T('but', T('110')) - 0.03, T('youtube') - 0.05, ['"JUST EAT HOME FOOD"', 'STILL ~NOT LOSING WEIGHT~'], x=540, y=300, sizes=[90, 84], anim='slam', stagger=1.4)
S.add({'type': 'chips', 't0': T('youtube') - 0.05, 't1': T('tab', T('baat')) - 0.05, 'y': 220, 'items': [
    {'t': T('supplement'), 'text': '"Take this supplement"'}, {'t': T('diet'), 'text': '"Do this diet"'}, {'t': T('juice'), 'text': '"Drink this juice"'},
    {'t': T('contradict'), 'text': '~All contradicting~'}]})
r0 = T('tab', T('baat')) - 0.08; r1 = T('number') - 0.08
S.card(r0, r1)
S.add({'type': 'chain', 't0': r0, 't1': r1, 'y': 150, 'title': 'So I went to the research', 'show': 4, 'items': [
    {'t': T('who'), 'text': '*WHO* research papers'}, {'t': T('pubmed'), 'text': '*PubMed* studies'}, {'t': T('google'), 'text': '*Google Scholar*'},
    {'t': T('metaanalyses'), 'text': '*Meta-analyses*'}, {'t': T('chaar'), 'text': 'Found *4 pillars*', 'st': 'yes', 'stc': 'green'}]})
# ---------------- pillar 1 fasting
f0 = T('number') - 0.08; f1 = T('number', T('trials')) - 0.08
S.card(f0, f1)
S.add({'type': 'chain', 't0': f0, 't1': f1, 'y': 150, 'title': 'Pillar 1: Fasting', 'show': 4, 'items': [
    {'t': T('ampk'), 'text': '*AMPK* switched on'}, {'t': T('autophagy'), 'text': '*Autophagy*: cell clean-up'},
    {'t': T('insulin'), 'text': 'Better *insulin sensitivity*', 'st': 'up', 'stc': 'green'}, {'t': T('thousands'), 'text': '*Thousands* of trials'}]})
K(T('ampk') - 0.1, T('autophagy') + 1.2, ["AMPK = YOUR CELLS' ENERGY SENSOR"], x=540, y=110, sizes=[44], font='oswald', anim='rise', fit=1000)
# ---------------- pillar 2 diet
B(10420, T('number', T('trials')) - 0.05, T('polyphenols') - 0.05, off=0.5)
K(T('number', T('trials')) - 0.03, T('polyphenols') - 0.05, ['PILLAR 2:', '*DIET*'], x=540, y=300, sizes=[90, 150], anim='slam', stagger=0.6)
d0 = T('polyphenols') - 0.08; d1 = T('exercise') - 0.08
S.card(d0, d1)
S.add({'type': 'chain', 't0': d0, 't1': d1, 'y': 150, 'title': 'Pillar 2: Diet', 'show': 4, 'items': [
    {'t': T('polyphenols'), 'text': '*Polyphenols*'}, {'t': T('colour'), 'text': 'Plant colours made for *survival*'},
    {'t': T('sirt1'), 'text': 'Activates *SIRT1*', 'st': 'up', 'stc': 'green'}, {'t': T('immunity'), 'text': 'Stronger *immunity*', 'st': 'up', 'stc': 'green'},
    {'t': T('decades'), 'text': '*Decades* of data'}]})
K(T('polyphenols') - 0.1, T('sirt1') - 0.2, ['POLYPHENOLS = PROTECTIVE PLANT COMPOUNDS'], x=540, y=110, sizes=[40], font='oswald', anim='rise', fit=1000)
K(T('sirt1') - 0.1, d1, ['SIRT1 = A SIRTUIN, LINKED TO CELL REPAIR'], x=540, y=110, sizes=[40], font='oswald', anim='rise', fit=1000)
# ---------------- pillar 3 exercise
B(44416, T('exercise') - 0.05, T('but', T('exercise')) - 0.05, off=0.5)
K(T('exercise') - 0.03, T('but', T('exercise')) - 0.05, ['PILLAR 3:', '*EXERCISE*'], x=540, y=300, sizes=[90, 150], anim='slam', stagger=0.6)
x0 = T('but', T('exercise')) - 0.08; x1 = T('meditation') - 0.08
S.card(x0, x1)
S.add({'type': 'checklist', 't0': x0, 't1': x1, 'y': 150, 'title': 'Pillar 3: Exercise', 'items': [
    {'t': T('resistance'), 'text': '*Resistance* training', 'mark': 'check'}, {'t': T('aerobic'), 'text': '*Aerobic* exercise', 'mark': 'check'},
    {'t': T('running'), 'text': 'Better than *just running*', 'mark': 'check'}, {'t': T('muscle'), 'text': '*Muscle* = insulin sensitivity', 'mark': 'check'}]})
# ---------------- pillar 4 meditation + sleep
m0 = T('meditation') - 0.08; m1 = T('in', T('proven')) - 0.35
S.card(m0, m1)
S.add({'type': 'chain', 't0': m0, 't1': m1, 'y': 150, 'title': 'Pillar 4: Meditation + sleep', 'show': 4, 'items': [
    {'t': T('meditation'), 'text': '*Meditation*'}, {'t': T('sleep'), 'text': '*Sleep*'}, {'t': T('cortisol'), 'text': '*Cortisol* balanced', 'st': 'yes', 'stc': 'green'},
    {'t': T('inflammation'), 'text': '*Inflammation* goes down', 'st': 'down', 'stc': 'green'}, {'t': T('proven'), 'text': 'Proven in *research*', 'st': 'yes', 'stc': 'green'}]})
# ---------------- personalised
K(m1 + 0.02, T('same') - 0.05, ['4 PILLARS. ONE PROTOCOL.', '*PERSONALIZED*'], x=540, y=300, sizes=[76, 120], anim='slam', stagger=1.0)
K(T('same') - 0.03, T('ab', T('exercises', T('same'))) - 0.05, ['SAME DIET', "~DOESN'T WORK FOR EVERYONE~"], x=540, y=300, sizes=[110, 76], anim='slam', stagger=0.9)
K(T('body', T('same')) - 0.1, T('ab', T('exercises', T('same'))) - 0.05, ['DIFFERENT BODY TYPES. DIFFERENT PLANS.'], x=540, y=1600, sizes=[50], font='oswald', anim='rise', fit=980)
q0 = T('ab', T('exercises', T('same'))) - 0.08; q1 = T('har') - 0.08
S.card(q0, q1)
S.add({'type': 'checklist', 't0': q0, 't1': q1, 'y': 150, 'title': 'Tested on my own family', 'items': [
    {'t': T('85'), 'text': 'Me: *110 kg to 85 kg*', 'mark': 'check'}, {'t': T('170'), 'text': "Wife's BP 170/110: *off meds*", 'mark': 'check'},
    {'t': T('85%'), 'text': "Mom's psoriasis: *85% better*", 'mark': 'check'}, {'t': T('gym'), 'text': 'Mom now goes to *the gym*', 'mark': 'check'},
    {'t': T('arthritis'), 'text': 'Her arthritis: *improving*', 'mark': 'check'}]})
K(T('har') - 0.03, T('toh', T('har')) - 0.05, ['EVERY STEP:', '*DATA TRACKED*'], x=540, y=300, sizes=[96, 120], anim='slam', stagger=0.8)
S.add({'type': 'chips', 't0': T('toh', T('har')) - 0.05, 't1': T('aur', T('kara')) - 0.05, 'y': 220, 'items': [
    {'t': T('research', T('toh', T('har'))), 'text': 'Research'}, {'t': T('testing', T('har')), 'text': 'Testing'},
    {'t': T('data', T('testing', T('har'))), 'text': 'Data'}, {'t': T('khud', T('har')), 'text': '*Tested on myself*'}]})
S.add({'type': 'stat', 't0': T('aur', T('kara')) - 0.05, 't1': T('toh', T('help')) - 0.05, 'y': 260, 'kicker': 'After my fasting', 'from': 0, 'to': 15, 'unit': ' KG',
       'label': 'Lost by *people I helped*', 'pill': '10 to 15 kg', 'dir': 'down', 'count': 1.0})
K(T('toh', T('help')) - 0.03, T('agar', T('banaya', T('available'))) - 0.05, ["I'M NOT A DOCTOR.", 'BUILT ON *PUBLISHED RESEARCH*'], x=540, y=300, sizes=[96, 84], anim='slam', stagger=1.2)
cta = T('agar', T('banaya', T('available'))) - 0.05
S.add({'type': 'cta', 't0': cta, 't1': D + 2, 'y': 980, 'kicker': 'Want the health protocol?', 'title': 'Comment<br>*"HP"*', 'sub': "I'll send you the link. My job was to bring you the science.", 'button': 'COMMENT NOW', 'hideCaps': True})
S.punch(cta, 0.06, 99)
S.alt_zoom([1.0, 1.22, 1.08, 1.32]); S.cam['faceY'] = 0.40; S.cam['grain'] = 4
S.cam['card'] = {'rect': [80, 1010, 920, 800], 'r': 44, 'scale': 1.1, 'faceY': 0.5}
caps = S.captions(hl_pats=[r'protocol', r'scenes', r'raat', r'saal', r'research', r'testing', r'papers', r'fasting', r'muscles', r'110', r'bp',
                           r'youtube', r'supplement', r'diet', r'juice', r'contradict', r'who', r'pubmed', r'google', r'scholar', r'metaanalyses', r'pillar',
                           r'ampk', r'autophagy', r'insulin', r'sensitivity', r'trials', r'polyphenols?', r'colour', r'survival', r'sirt1', r'immunity',
                           r'decades', r'exercise', r'resistance', r'aerobic', r'running', r'muscle', r'meditation', r'sleep', r'cortisol', r'inflammation',
                           r'proven', r'personalize', r'85', r'170', r'85%', r'psoriasis', r'gym', r'arthritis', r'data', r'10', r'15', r'doctor', r'hp'])
S.save(caps, cta_t=cta, hold=1.0, brand={'text': 'Fit<b>Finfluencer</b>', 't0': 3.0, 't1': cta})
